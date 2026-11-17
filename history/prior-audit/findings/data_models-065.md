# data_models — findings 6401–6500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06675"></a>
## FND-06675: chesscom.payments.v1.ListEligibleGiftRecipientsRequest.product = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.Product product = 2;

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 166.

```text
o3

package chesscom.payments.v1;

message ListEligibleGiftRecipientsRequest {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  repeated string user_uuids = 1;
}

message ListEligibleGiftRecipientsResponse {
  repeated string eligible_user_uuids = 1;
}

```

**Source references:** SRC-0490, SRC-1461  
**URL references:** None independently associated  
**Related findings:** FND-06673, FND-06674

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06676"></a>
## FND-06676: chesscom.payments.v1.ListEligibleGiftRecipientsRequest.user_uuids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string user_uuids = 1;

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 215.

```text
igibleGiftRecipientsRequest {
  oneof _product {
  .chesscom.payments.v1.Product product = 2;
  }
  repeated string user_uuids = 1;
}

message ListEligibleGiftRecipientsResponse {
  repeated string eligible_user_uuids = 1;
}

```

**Source references:** SRC-0490, SRC-1461  
**URL references:** None independently associated  
**Related findings:** FND-06673, FND-06674, FND-06675

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06677"></a>
## FND-06677: message declaration: chesscom.payments.v1.ListEligibleGiftRecipientsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListEligibleGiftRecipientsResponse {

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 250.

```text
of _product {
  .chesscom.payments.v1.Product product = 2;
  }
  repeated string user_uuids = 1;
}

message ListEligibleGiftRecipientsResponse {
  repeated string eligible_user_uuids = 1;
}

```

**Source references:** SRC-0490, SRC-1461  
**URL references:** None independently associated  
**Related findings:** FND-06673, FND-06674, FND-06675

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06678"></a>
## FND-06678: chesscom.payments.v1.ListEligibleGiftRecipientsResponse.eligible_user_uuids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string eligible_user_uuids = 1;

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 297.

```text
roduct = 2;
  }
  repeated string user_uuids = 1;
}

message ListEligibleGiftRecipientsResponse {
  repeated string eligible_user_uuids = 1;
}

```

**Source references:** SRC-0490, SRC-1461  
**URL references:** None independently associated  
**Related findings:** FND-06673, FND-06674, FND-06675

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06679"></a>
## FND-06679: enum declaration: chesscom.payments.v1.GoodwillSiteFault

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GoodwillSiteFault {

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 97.

```text
// source: chesscom/payments/v1/goodwill.proto
// syntax: proto3

package chesscom.payments.v1;

enum GoodwillSiteFault {
  GOODWILL_SITE_FAULT_UNSPECIFIED = 0;
  GOODWILL_SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAM
```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06680"></a>
## FND-06680: chesscom.payments.v1.GoodwillSiteFault.GOODWILL_SITE_FAULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOODWILL_SITE_FAULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 124.

```text
ents/v1/goodwill.proto
// syntax: proto3

package chesscom.payments.v1;

enum GoodwillSiteFault {
  GOODWILL_SITE_FAULT_UNSPECIFIED = 0;
  GOODWILL_SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED 
```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06681"></a>
## FND-06681: chesscom.payments.v1.GoodwillSiteFault.GOODWILL_SITE_FAULT_OUTAGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOODWILL_SITE_FAULT_OUTAGE = 1;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 163.

```text
3

package chesscom.payments.v1;

enum GoodwillSiteFault {
  GOODWILL_SITE_FAULT_UNSPECIFIED = 0;
  GOODWILL_SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DA
```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06682"></a>
## FND-06682: chesscom.payments.v1.GoodwillSiteFault.GOODWILL_SITE_FAULT_BUG = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOODWILL_SITE_FAULT_BUG = 2;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 197.

```text
enum GoodwillSiteFault {
  GOODWILL_SITE_FAULT_UNSPECIFIED = 0;
  GOODWILL_SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06683"></a>
## FND-06683: chesscom.payments.v1.GoodwillSiteFault.GOODWILL_SITE_FAULT_FAILED_OPERATION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 228.

```text
WILL_SITE_FAULT_UNSPECIFIED = 0;
  GOODWILL_SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06684"></a>
## FND-06684: chesscom.payments.v1.GoodwillSiteFault.GOODWILL_SITE_FAULT_WRONG_ACTION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOODWILL_SITE_FAULT_WRONG_ACTION = 4;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 272.

```text
SITE_FAULT_OUTAGE = 1;
  GOODWILL_SITE_FAULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06685"></a>
## FND-06685: enum declaration: chesscom.payments.v1.GrantGoodwillDiamondResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GrantGoodwillDiamondResult {

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 313.

```text
ULT_BUG = 2;
  GOODWILL_SITE_FAULT_FAILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06686"></a>
## FND-06686: chesscom.payments.v1.GrantGoodwillDiamondResult.GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 349.

```text
AILED_OPERATION = 3;
  GOODWILL_SITE_FAULT_WRONG_ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06687"></a>
## FND-06687: chesscom.payments.v1.GrantGoodwillDiamondResult.GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 398.

```text
ACTION = 4;
}

enum GrantGoodwillDiamondResult {
  GRANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06688"></a>
## FND-06688: chesscom.payments.v1.GrantGoodwillDiamondResult.GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;

### Evidence

- **SRC-0491** `research/proto/chesscom/payments/v1/goodwill.proto` — [preserved redacted evidence](../evidence/text/4f9d1356f721e898126961ff3fb4ab050e16ee27e04826809d197401027b55fc.proto)
  Character offset 451.

```text
ANT_GOODWILL_DIAMOND_RESULT_UNSPECIFIED = 0;
  GRANT_GOODWILL_DIAMOND_RESULT_DIAMOND_STARTED = 1;
  GRANT_GOODWILL_DIAMOND_RESULT_DAYS_ADDED = 2;
}

```

**Source references:** SRC-0491, SRC-1462  
**URL references:** None independently associated  
**Related findings:** FND-06679, FND-06680, FND-06681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06689"></a>
## FND-06689: enum declaration: chesscom.payments.v1.JoinEligibilityStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum JoinEligibilityStatus {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 116.

```text
com/payments/v1/group_membership_invitation.proto
// syntax: proto3

package chesscom.payments.v1;

enum JoinEligibilityStatus {
  JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0;
  JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;
  JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JO
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06690"></a>
## FND-06690: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 147.

```text
p_invitation.proto
// syntax: proto3

package chesscom.payments.v1;

enum JoinEligibilityStatus {
  JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0;
  JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;
  JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_I
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06691"></a>
## FND-06691: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 190.

```text
ge chesscom.payments.v1;

enum JoinEligibilityStatus {
  JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0;
  JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;
  JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_RE
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06692"></a>
## FND-06692: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 237.

```text
tatus {
  JOIN_ELIGIBILITY_STATUS_UNSPECIFIED = 0;
  JOIN_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;
  JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06693"></a>
## FND-06693: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 293.

```text
N_ELIGIBILITY_STATUS_ALREADY_PREMIUM = 1;
  JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06694"></a>
## FND-06694: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 337.

```text
JOIN_ELIGIBILITY_STATUS_CROSS_BORDER_RESTRICTION = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06695"></a>
## FND-06695: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 384.

```text
N = 2;
  JOIN_ELIGIBILITY_STATUS_INVALID_TYPE = 3;
  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06696"></a>
## FND-06696: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 434.

```text

  JOIN_ELIGIBILITY_STATUS_ALL_SEATS_TAKEN = 4;
  JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus stat
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06697"></a>
## FND-06697: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 484.

```text
JOIN_ELIGIBILITY_STATUS_INVITATION_EXPIRED = 5;
  JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

me
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06698"></a>
## FND-06698: chesscom.payments.v1.JoinEligibilityStatus.JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 534.

```text
JOIN_ELIGIBILITY_STATUS_INVALID_INVITATION = 6;
  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional str
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06699"></a>
## FND-06699: message declaration: chesscom.payments.v1.InvitationPlanDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvitationPlanDetails {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 581.

```text

  JOIN_ELIGIBILITY_STATUS_REMOVED_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.u
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06700"></a>
## FND-06700: chesscom.payments.v1.InvitationPlanDetails.max_secondary_members = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_secondary_members = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 615.

```text
_BY_PRIMARY = 7;
  JOIN_ELIGIBILITY_STATUS_TRIAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_ho
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06701"></a>
## FND-06701: message declaration: chesscom.payments.v1.JoinEligibility

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message JoinEligibility {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 660.

```text
IAL_COOLDOWN = 8;
}

message InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.In
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06702"></a>
## FND-06702: oneof declaration: chesscom.payments.v1.JoinEligibility._status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _status {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 688.

```text
 InvitationPlanDetails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_det
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06703"></a>
## FND-06703: chesscom.payments.v1.JoinEligibility.status = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.JoinEligibilityStatus status = 2;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 706.

```text
ails {
  optional int32 max_secondary_members = 1;
}

message JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  option
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06704"></a>
## FND-06704: chesscom.payments.v1.JoinEligibility.is_eligible = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_eligible = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 768.

```text
JoinEligibility {
  oneof _status {
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message Pendi
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06705"></a>
## FND-06705: message declaration: chesscom.payments.v1.PendingInvitationForInvitee

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PendingInvitationForInvitee {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 802.

```text
{
  .chesscom.payments.v1.JoinEligibilityStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identi
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06706"></a>
## FND-06706: chesscom.payments.v1.PendingInvitationForInvitee.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 842.

```text
yStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user =
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06707"></a>
## FND-06707: chesscom.payments.v1.PendingInvitationForInvitee.primary_account_holder = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView primary_account_holder = 2;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 881.

```text
 is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message 
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06708"></a>
## FND-06708: chesscom.payments.v1.PendingInvitationForInvitee.plan_details = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 947.

```text
nal string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optio
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06709"></a>
## FND-06709: chesscom.payments.v1.PendingInvitationForInvitee.expires_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 4;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1020.

```text
mary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.T
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06710"></a>
## FND-06710: message declaration: chesscom.payments.v1.PendingInviteeIdentity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PendingInviteeIdentity {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1075.

```text
v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06711"></a>
## FND-06711: oneof declaration: chesscom.payments.v1.PendingInviteeIdentity.identity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof identity {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1110.

```text
ls = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_i
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06712"></a>
## FND-06712: chesscom.payments.v1.PendingInviteeIdentity.user = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user.v1.UserView user = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1129.

```text
.google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06713"></a>
## FND-06713: chesscom.payments.v1.PendingInviteeIdentity.email = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string email = 2;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1168.

```text
 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06714"></a>
## FND-06714: message declaration: chesscom.payments.v1.PendingInvitation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PendingInvitation {

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1193.

```text
iteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user = 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06715"></a>
## FND-06715: chesscom.payments.v1.PendingInvitation.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 842.

```text
yStatus status = 2;
  }
  optional bool is_eligible = 1;
}

message PendingInvitationForInvitee {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView primary_account_holder = 2;
  optional .chesscom.payments.v1.InvitationPlanDetails plan_details = 3;
  optional .google.protobuf.Timestamp expires_at = 4;
}

message PendingInviteeIdentity {
  oneof identity {
  .chesscom.user.v1.UserView user =
```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06716"></a>
## FND-06716: chesscom.payments.v1.PendingInvitation.invitee = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView invitee = 2;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1262.

```text
 1;
  string email = 2;
  }
}

message PendingInvitation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06717"></a>
## FND-06717: chesscom.payments.v1.PendingInvitation.expires_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 3;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1313.

```text
ation {
  optional string invitation_hash = 1;
  optional .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06718"></a>
## FND-06718: chesscom.payments.v1.PendingInvitation.invitee_identity = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;

### Evidence

- **SRC-0492** `research/proto/chesscom/payments/v1/group_membership_invitation.proto` — [preserved redacted evidence](../evidence/text/bb9e565e8e7df8be99b9dfcd63f13b4d6133311b3e2c6a7bc88656fde14f075f.proto)
  Character offset 1367.

```text
nal .chesscom.user.v1.UserView invitee = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional .chesscom.payments.v1.PendingInviteeIdentity invitee_identity = 4;
}

```

**Source references:** SRC-0492, SRC-1463  
**URL references:** None independently associated  
**Related findings:** FND-06689, FND-06690, FND-06691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06719"></a>
## FND-06719: message declaration: chesscom.payments.v1.GenerateInvitationLinkRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GenerateInvitationLinkRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 113.

```text
esscom/payments/v1/group_membership_service.proto
// syntax: proto3

package chesscom.payments.v1;

message GenerateInvitationLinkRequest {
}

message GenerateInvitationLinkResponse {
  optional string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message I
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06720"></a>
## FND-06720: message declaration: chesscom.payments.v1.GenerateInvitationLinkResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GenerateInvitationLinkResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 156.

```text
.proto
// syntax: proto3

package chesscom.payments.v1;

message GenerateInvitationLinkRequest {
}

message GenerateInvitationLinkResponse {
  optional string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identi
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06721"></a>
## FND-06721: chesscom.payments.v1.GenerateInvitationLinkResponse.invitation_link = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_link = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 199.

```text
payments.v1;

message GenerateInvitationLinkRequest {
}

message GenerateInvitationLinkResponse {
  optional string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06722"></a>
## FND-06722: message declaration: chesscom.payments.v1.CheckJoinEligibilityRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckJoinEligibilityRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 239.

```text
LinkRequest {
}

message GenerateInvitationLinkResponse {
  optional string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06723"></a>
## FND-06723: oneof declaration: chesscom.payments.v1.CheckJoinEligibilityRequest.member_identifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof member_identifier {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 279.

```text
ionLinkResponse {
  optional string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  option
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06724"></a>
## FND-06724: chesscom.payments.v1.CheckJoinEligibilityRequest.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string id = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 307.

```text
 string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}


```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06725"></a>
## FND-06725: chesscom.payments.v1.CheckJoinEligibilityRequest.email = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string email = 2;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 324.

```text
n_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMem
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06726"></a>
## FND-06726: message declaration: chesscom.payments.v1.CheckJoinEligibilityResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckJoinEligibilityResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 349.

```text
eckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message 
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06727"></a>
## FND-06727: chesscom.payments.v1.CheckJoinEligibilityResponse.is_eligible = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_eligible = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 390.

```text
r_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

messag
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06728"></a>
## FND-06728: message declaration: chesscom.payments.v1.InviteMemberRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InviteMemberRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 424.

```text
string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06729"></a>
## FND-06729: oneof declaration: chesscom.payments.v1.InviteMemberRequest.invitee_identifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof invitee_identifier {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 456.

```text
 CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06730"></a>
## FND-06730: chesscom.payments.v1.InviteMemberRequest.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string id = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 307.

```text
 string invitation_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}


```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06731"></a>
## FND-06731: chesscom.payments.v1.InviteMemberRequest.email = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string email = 2;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 324.

```text
n_link = 1;
}

message CheckJoinEligibilityRequest {
  oneof member_identifier {
  string id = 1;
  string email = 2;
  }
}

message CheckJoinEligibilityResponse {
  optional bool is_eligible = 1;
}

message InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMem
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06732"></a>
## FND-06732: message declaration: chesscom.payments.v1.InviteMemberResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InviteMemberResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 527.

```text
sage InviteMemberRequest {
  oneof invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSeco
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06733"></a>
## FND-06733: message declaration: chesscom.payments.v1.RemoveMemberRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveMemberRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 561.

```text
 invitee_identifier {
  string id = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated 
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06734"></a>
## FND-06734: chesscom.payments.v1.RemoveMemberRequest.member_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string member_id = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 593.

```text
d = 1;
  string email = 2;
  }
}

message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secon
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06735"></a>
## FND-06735: message declaration: chesscom.payments.v1.RemoveMemberResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveMemberResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 627.

```text
message InviteMemberResponse {
}

message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .ches
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06736"></a>
## FND-06736: message declaration: chesscom.payments.v1.GetMaxSecondaryMembersRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetMaxSecondaryMembersRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 661.

```text
message RemoveMemberRequest {
  optional string member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06737"></a>
## FND-06737: message declaration: chesscom.payments.v1.GetMaxSecondaryMembersResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetMaxSecondaryMembersResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 704.

```text
ring member_id = 1;
}

message RemoveMemberResponse {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveG
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06738"></a>
## FND-06738: chesscom.payments.v1.GetMaxSecondaryMembersResponse.max_secondary_members = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_secondary_members = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 747.

```text
Response {
}

message GetMaxSecondaryMembersRequest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGro
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06739"></a>
## FND-06739: message declaration: chesscom.payments.v1.GetSecondaryMembersRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSecondaryMembersRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 792.

```text
equest {
}

message GetMaxSecondaryMembersResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvi
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06740"></a>
## FND-06740: message declaration: chesscom.payments.v1.GetSecondaryMembersResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSecondaryMembersResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 832.

```text
rsResponse {
  optional int32 max_secondary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  stri
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06741"></a>
## FND-06741: chesscom.payments.v1.GetSecondaryMembersResponse.secondary_members = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user.v1.UserView secondary_members = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 872.

```text
ary_members = 1;
}

message GetSecondaryMembersRequest {
}

message GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string inv
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06742"></a>
## FND-06742: chesscom.payments.v1.GetSecondaryMembersResponse.pending_invitations = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 933.

```text
essage GetSecondaryMembersResponse {
  repeated .chesscom.user.v1.UserView secondary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  on
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06743"></a>
## FND-06743: message declaration: chesscom.payments.v1.LeaveGroupMembershipRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LeaveGroupMembershipRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1010.

```text
condary_members = 1;
  repeated .chesscom.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_ho
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06744"></a>
## FND-06744: message declaration: chesscom.payments.v1.LeaveGroupMembershipResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LeaveGroupMembershipResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1051.

```text
.payments.v1.PendingInvitation pending_invitations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06745"></a>
## FND-06745: message declaration: chesscom.payments.v1.PreviewInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PreviewInvitationRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1093.

```text
itations = 2;
}

message LeaveGroupMembershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06746"></a>
## FND-06746: oneof declaration: chesscom.payments.v1.PreviewInvitationRequest._source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _source {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1130.

```text
mbershipRequest {
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .ch
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06747"></a>
## FND-06747: chesscom.payments.v1.PreviewInvitationRequest.source = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string source = 2;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1148.

```text
}

message LeaveGroupMembershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06748"></a>
## FND-06748: chesscom.payments.v1.PreviewInvitationRequest.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1173.

```text
ershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibil
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06749"></a>
## FND-06749: message declaration: chesscom.payments.v1.PreviewInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PreviewInvitationResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1213.

```text
ationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitat
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06750"></a>
## FND-06750: oneof declaration: chesscom.payments.v1.PreviewInvitationResponse._primary_account_holder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _primary_account_holder {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1251.

```text
ing source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitat
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06751"></a>
## FND-06751: chesscom.payments.v1.PreviewInvitationResponse.primary_account_holder = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user.v1.UserView primary_account_holder = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1285.

```text
ing invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroup
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06752"></a>
## FND-06752: oneof declaration: chesscom.payments.v1.PreviewInvitationResponse._plan_details

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _plan_details {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1346.

```text
 {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsReq
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06753"></a>
## FND-06753: chesscom.payments.v1.PreviewInvitationResponse.plan_details = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.payments.v1.InvitationPlanDetails plan_details = 2;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1370.

```text
unt_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPe
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06754"></a>
## FND-06754: chesscom.payments.v1.PreviewInvitationResponse.eligibility = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.JoinEligibility eligibility = 3;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1438.

```text
;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingI
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06755"></a>
## FND-06755: message declaration: chesscom.payments.v1.JoinGroupFromInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message JoinGroupFromInvitationRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1505.

```text
nDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRe
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06756"></a>
## FND-06756: chesscom.payments.v1.JoinGroupFromInvitationRequest.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1173.

```text
ershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibil
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06757"></a>
## FND-06757: message declaration: chesscom.payments.v1.JoinGroupFromInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message JoinGroupFromInvitationResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1588.

```text
gibility = 3;
}

message JoinGroupFromInvitationRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06758"></a>
## FND-06758: message declaration: chesscom.payments.v1.ListPendingInvitationsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListPendingInvitationsRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1633.

```text
ionRequest {
  optional string invitation_hash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  opt
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06759"></a>
## FND-06759: message declaration: chesscom.payments.v1.ListPendingInvitationsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListPendingInvitationsResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1676.

```text
ash = 1;
}

message JoinGroupFromInvitationResponse {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

messag
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06760"></a>
## FND-06760: chesscom.payments.v1.ListPendingInvitationsResponse.invitations = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1719.

```text
Response {
}

message ListPendingInvitationsRequest {
}

message ListPendingInvitationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

message RevokeInvitationResponse {
}

```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06761"></a>
## FND-06761: message declaration: chesscom.payments.v1.DeclineInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeclineInvitationRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1798.

```text
itationsResponse {
  repeated .chesscom.payments.v1.PendingInvitationForInvitee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

message RevokeInvitationResponse {
}

```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06762"></a>
## FND-06762: chesscom.payments.v1.DeclineInvitationRequest.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1173.

```text
ershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibil
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06763"></a>
## FND-06763: message declaration: chesscom.payments.v1.DeclineInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeclineInvitationResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1875.

```text
ee invitations = 1;
}

message DeclineInvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

message RevokeInvitationResponse {
}

```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06764"></a>
## FND-06764: message declaration: chesscom.payments.v1.RevokeInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RevokeInvitationRequest {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1914.

```text
nvitationRequest {
  optional string invitation_hash = 1;
}

message DeclineInvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

message RevokeInvitationResponse {
}

```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06765"></a>
## FND-06765: chesscom.payments.v1.RevokeInvitationRequest.invitation_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_hash = 1;

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1173.

```text
ershipResponse {
}

message PreviewInvitationRequest {
  oneof _source {
  string source = 2;
  }
  optional string invitation_hash = 1;
}

message PreviewInvitationResponse {
  oneof _primary_account_holder {
  .chesscom.user.v1.UserView primary_account_holder = 1;
  }
  oneof _plan_details {
  .chesscom.payments.v1.InvitationPlanDetails plan_details = 2;
  }
  optional .chesscom.payments.v1.JoinEligibility eligibil
```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06766"></a>
## FND-06766: message declaration: chesscom.payments.v1.RevokeInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RevokeInvitationResponse {

### Evidence

- **SRC-0493** `research/proto/chesscom/payments/v1/group_membership_service.proto` — [preserved redacted evidence](../evidence/text/95cafe7e610966fb5780ba58e10eca380d6bb16ead4633f58041540b74d7c7bd.proto)
  Character offset 1990.

```text
InvitationResponse {
}

message RevokeInvitationRequest {
  optional string invitation_hash = 1;
}

message RevokeInvitationResponse {
}

```

**Source references:** SRC-0493, SRC-1464  
**URL references:** None independently associated  
**Related findings:** FND-06719, FND-06720, FND-06721

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06767"></a>
## FND-06767: enum declaration: chesscom.payments.v1.GroupMembershipType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GroupMembershipType {

### Evidence

- **SRC-0494** `research/proto/chesscom/payments/v1/group_membership_type.proto` — [preserved redacted evidence](../evidence/text/49ce95bf6fc421866613f399a07c53920ac9da8bdbb36e3858516a67303b2ef9.proto)
  Character offset 110.

```text
 chesscom/payments/v1/group_membership_type.proto
// syntax: proto3

package chesscom.payments.v1;

enum GroupMembershipType {
  GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0;
  GROUP_MEMBERSHIP_TYPE_PRIMARY = 1;
  GROUP_MEMBERSHIP_TYPE_SECONDARY = 2;
}

```

**Source references:** SRC-0494, SRC-1465  
**URL references:** None independently associated  
**Related findings:** FND-06768, FND-06769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06768"></a>
## FND-06768: chesscom.payments.v1.GroupMembershipType.GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0494** `research/proto/chesscom/payments/v1/group_membership_type.proto` — [preserved redacted evidence](../evidence/text/49ce95bf6fc421866613f399a07c53920ac9da8bdbb36e3858516a67303b2ef9.proto)
  Character offset 139.

```text
embership_type.proto
// syntax: proto3

package chesscom.payments.v1;

enum GroupMembershipType {
  GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0;
  GROUP_MEMBERSHIP_TYPE_PRIMARY = 1;
  GROUP_MEMBERSHIP_TYPE_SECONDARY = 2;
}

```

**Source references:** SRC-0494, SRC-1465  
**URL references:** None independently associated  
**Related findings:** FND-06767, FND-06769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06769"></a>
## FND-06769: chesscom.payments.v1.GroupMembershipType.GROUP_MEMBERSHIP_TYPE_PRIMARY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROUP_MEMBERSHIP_TYPE_PRIMARY = 1;

### Evidence

- **SRC-0494** `research/proto/chesscom/payments/v1/group_membership_type.proto` — [preserved redacted evidence](../evidence/text/49ce95bf6fc421866613f399a07c53920ac9da8bdbb36e3858516a67303b2ef9.proto)
  Character offset 180.

```text
ackage chesscom.payments.v1;

enum GroupMembershipType {
  GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0;
  GROUP_MEMBERSHIP_TYPE_PRIMARY = 1;
  GROUP_MEMBERSHIP_TYPE_SECONDARY = 2;
}

```

**Source references:** SRC-0494, SRC-1465  
**URL references:** None independently associated  
**Related findings:** FND-06767, FND-06768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06770"></a>
## FND-06770: chesscom.payments.v1.GroupMembershipType.GROUP_MEMBERSHIP_TYPE_SECONDARY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROUP_MEMBERSHIP_TYPE_SECONDARY = 2;

### Evidence

- **SRC-0494** `research/proto/chesscom/payments/v1/group_membership_type.proto` — [preserved redacted evidence](../evidence/text/49ce95bf6fc421866613f399a07c53920ac9da8bdbb36e3858516a67303b2ef9.proto)
  Character offset 217.

```text
oupMembershipType {
  GROUP_MEMBERSHIP_TYPE_UNSPECIFIED = 0;
  GROUP_MEMBERSHIP_TYPE_PRIMARY = 1;
  GROUP_MEMBERSHIP_TYPE_SECONDARY = 2;
}

```

**Source references:** SRC-0494, SRC-1465  
**URL references:** None independently associated  
**Related findings:** FND-06767, FND-06768, FND-06769

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06771"></a>
## FND-06771: message declaration: chesscom.payments.v1.Incentive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Incentive {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 98.

```text
// source: chesscom/payments/v1/incentive.proto
// syntax: proto3

package chesscom.payments.v1;

message Incentive {
  oneof _free_time {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
 
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06772"></a>
## FND-06772: oneof declaration: chesscom.payments.v1.Incentive._free_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _free_time {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 120.

```text
payments/v1/incentive.proto
// syntax: proto3

package chesscom.payments.v1;

message Incentive {
  oneof _free_time {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recur
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06773"></a>
## FND-06773: chesscom.payments.v1.Incentive.free_time = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 free_time = 4;

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 141.

```text
.proto
// syntax: proto3

package chesscom.payments.v1;

message Incentive {
  oneof _free_time {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06774"></a>
## FND-06774: oneof declaration: chesscom.payments.v1.Incentive._discount_percentage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _discount_percentage {

### Evidence

- **SRC-0495** `research/proto/chesscom/payments/v1/incentive.proto` — [preserved redacted evidence](../evidence/text/c1d9b0ba6034551220b10e68f84919d13d0fd6814560e5cecb78a29c6fdc5a33.proto)
  Character offset 168.

```text
ackage chesscom.payments.v1;

message Incentive {
  oneof _free_time {
  int32 free_time = 4;
  }
  oneof _discount_percentage {
  float discount_percentage = 5;
  }
  oneof _discount_amount {
  .chesscom.api.v1.Money discount_amount = 6;
  }
  oneof _discount_charge_type {
  .chesscom.payments.v1.IncentiveChargeType discount_charge_type = 7;
  }
  oneof _discount_recurring_limit {
  int32 discount_recurring_limit = 
```

**Source references:** SRC-0495, SRC-1466  
**URL references:** None independently associated  
**Related findings:** FND-06771, FND-06772, FND-06773

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
