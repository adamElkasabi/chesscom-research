# data_models — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00375"></a>
## FND-00375: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_INVALID = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_INVALID = 21;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 986.

```text
_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00376"></a>
## FND-00376: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1028.

```text
ED = 11;
  ERROR_REASON_PHONE_NUMBER_INVALID_TYPE = 13;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_R
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00377"></a>
## FND-00377: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_MISSING = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_MISSING = 25;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1082.

```text
;
  ERROR_REASON_PHONE_NUMBER_INVALID = 21;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_AL
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00378"></a>
## FND-00378: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1124.

```text
;
  ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY = 22;
  ERROR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_M
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00379"></a>
## FND-00379: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1185.

```text
OR_REASON_PHONE_NUMBER_MISSING = 25;
  ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00380"></a>
## FND-00380: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1239.

```text
ONE_NUMBER_VERIFICATION_LIMIT_REACHED = 45;
  ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASO
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00381"></a>
## FND-00381: chesscom.api.v1.ErrorReason.ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1308.

```text
ER_FRAUDULENT_ACTIVITY = 48;
  ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_ME
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00382"></a>
## FND-00382: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1365.

```text
ACCOUNT_VERIFICATION_LIMIT_REACHED = 61;
  ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GRO
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00383"></a>
## FND-00383: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1424.

```text
NE_NUMBER_UNSUBSCRIBED_RECIPIENT = 62;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00384"></a>
## FND-00384: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1492.

```text
IP_JOIN_ALREADY_PREMIUM = 14;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USE
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00385"></a>
## FND-00385: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1548.

```text
RSHIP_JOIN_CROSS_BORDER_RESTRICTION = 15;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00386"></a>
## FND-00386: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1607.

```text
OUP_MEMBERSHIP_JOIN_INVALID_TYPE = 16;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALL
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00387"></a>
## FND-00387: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1669.

```text
MBERSHIP_JOIN_ALL_SEATS_TAKEN = 17;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORT
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00388"></a>
## FND-00388: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1731.

```text
RSHIP_JOIN_INVITATION_EXPIRED = 18;
  ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATIO
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00389"></a>
## FND-00389: chesscom.api.v1.ErrorReason.ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1779.

```text
ON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION = 19;
  ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00390"></a>
## FND-00390: chesscom.api.v1.ErrorReason.ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1832.

```text
RROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND = 20;
  ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_A
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00391"></a>
## FND-00391: chesscom.api.v1.ErrorReason.ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1890.

```text
N_GROUP_MEMBERSHIP_USER_NOT_FOUND = 23;
  ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUN
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00392"></a>
## FND-00392: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 1947.

```text
GNUP_ISSUE_CHALLENGE_LIMIT_REACHED = 24;
  ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOU
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00393"></a>
## FND-00393: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2005.

```text
GNUP_UNSUPPORTED_CHALLENGE_METHOD = 63;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00394"></a>
## FND-00394: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2068.

```text
_ACCOUNTS_NOT_SUPPORTED_TYPE = 26;
  ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EX
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00395"></a>
## FND-00395: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2120.

```text
TERNAL_ACCOUNTS_STATE_VALIDATION_FAILED = 27;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00396"></a>
## FND-00396: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2182.

```text
XTERNAL_ACCOUNTS_NO_AUTH_CODE = 28;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOT
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00397"></a>
## FND-00397: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2240.

```text
L_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST = 29;
  ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAIL
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00398"></a>
## FND-00398: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2303.

```text
_ACCOUNTS_PROVIDER_EXCEPTION = 30;
  ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00399"></a>
## FND-00399: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2373.

```text
_PERMISSIONS_PROVIDED = 31;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00400"></a>
## FND-00400: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2446.

```text
ECTED_SAME_ACCOUNT = 32;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVAL
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00401"></a>
## FND-00401: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2519.

```text
ED_ANOTHER_ACCOUNT = 33;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERR
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00402"></a>
## FND-00402: chesscom.api.v1.ErrorReason.ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2586.

```text
ONNECTED_TO_ANOTHER_USER = 34;
  ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EM
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00403"></a>
## FND-00403: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2673.

```text
TION = 35;
  ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00404"></a>
## FND-00404: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2727.

```text
CONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION = 60;
  ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT =
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00405"></a>
## FND-00405: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2777.

```text
R_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID = 36;
  ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_I
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00406"></a>
## FND-00406: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2836.

```text
SON_ACCOUNT_NEW_PASSWORD_INVALID = 37;
  ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED 
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00407"></a>
## FND-00407: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2883.

```text
REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED = 38;
  ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00408"></a>
## FND-00408: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2939.

```text
OR_REASON_ACCOUNT_NEW_EMAIL_INVALID = 39;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00409"></a>
## FND-00409: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 2997.

```text
CCOUNT_EMAIL_UPDATE_LIMIT_REACHED = 40;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  E
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00410"></a>
## FND-00410: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3054.

```text
COUNT_EMAIL_UPDATE_FILLER_PASSWORD = 41;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REAS
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00411"></a>
## FND-00411: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3111.

```text
CCOUNT_EMAIL_UPDATE_EQUALS_CURRENT = 42;
  ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00412"></a>
## FND-00412: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3164.

```text
ON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE = 43;
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00413"></a>
## FND-00413: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3209.

```text
  ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED = 57;
  ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LAT
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00414"></a>
## FND-00414: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3265.

```text
RROR_REASON_ACCOUNT_EMAIL_NOT_FOUND = 58;
  ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXI
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00415"></a>
## FND-00415: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3316.

```text
EASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED = 59;
  ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EX
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00416"></a>
## FND-00416: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3364.

```text
 ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED = 44;
  ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53
```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00417"></a>
## FND-00417: chesscom.api.v1.ErrorReason.ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3425.

```text
SON_ACCOUNT_OLD_PASSWORD_EXIST = 46;
  ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00418"></a>
## FND-00418: chesscom.api.v1.ErrorReason.ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3488.

```text
LL_CANNOT_BE_UPDATED_ANYMORE = 49;
  ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00419"></a>
## FND-00419: chesscom.api.v1.ErrorReason.ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3540.

```text
COUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL = 56;
  ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00420"></a>
## FND-00420: chesscom.api.v1.ErrorReason.ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3597.

```text
SON_OTVC_CHALLENGE_TRY_AGAIN_LATER = 50;
  ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00421"></a>
## FND-00421: chesscom.api.v1.ErrorReason.ERROR_REASON_SURVEY_NO_ANSWERS = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_SURVEY_NO_ANSWERS = 53;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3649.

```text
SON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00422"></a>
## FND-00422: chesscom.api.v1.ErrorReason.ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;

### Evidence

- **SRC-0213** `research/proto/chesscom/api/v1/error_reason.proto` — [preserved redacted evidence](../evidence/text/5d14ddbf4feef5712f9b089d44e64dabd3a63dfb929abccbd8b988950cc62148.proto)
  Character offset 3688.

```text
 = 51;
  ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS = 52;
  ERROR_REASON_SURVEY_NO_ANSWERS = 53;
  ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED = 64;
}

```

**Source references:** SRC-0213, SRC-1184  
**URL references:** None independently associated  
**Related findings:** FND-00357, FND-00358, FND-00359

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00423"></a>
## FND-00423: message declaration: chesscom.api.v1.Language

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Language {

### Evidence

- **SRC-0214** `research/proto/chesscom/api/v1/i18n.proto` — [preserved redacted evidence](../evidence/text/052d60b9d329bbc8548a60bd174fc5e7ba5e433495b6062171e5cb7a1ed903c6.proto)
  Character offset 83.

```text
// source: chesscom/api/v1/i18n.proto
// syntax: proto3

package chesscom.api.v1;

message Language {
  oneof _native_name {
  string native_name = 2;
  }
  optional string locale = 1;
}

```

**Source references:** SRC-0214, SRC-1185  
**URL references:** None independently associated  
**Related findings:** FND-00424, FND-00425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00424"></a>
## FND-00424: oneof declaration: chesscom.api.v1.Language._native_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _native_name {

### Evidence

- **SRC-0214** `research/proto/chesscom/api/v1/i18n.proto` — [preserved redacted evidence](../evidence/text/052d60b9d329bbc8548a60bd174fc5e7ba5e433495b6062171e5cb7a1ed903c6.proto)
  Character offset 104.

```text
ource: chesscom/api/v1/i18n.proto
// syntax: proto3

package chesscom.api.v1;

message Language {
  oneof _native_name {
  string native_name = 2;
  }
  optional string locale = 1;
}

```

**Source references:** SRC-0214, SRC-1185  
**URL references:** None independently associated  
**Related findings:** FND-00423, FND-00425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00425"></a>
## FND-00425: chesscom.api.v1.Language.native_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string native_name = 2;

### Evidence

- **SRC-0214** `research/proto/chesscom/api/v1/i18n.proto` — [preserved redacted evidence](../evidence/text/052d60b9d329bbc8548a60bd174fc5e7ba5e433495b6062171e5cb7a1ed903c6.proto)
  Character offset 127.

```text
i18n.proto
// syntax: proto3

package chesscom.api.v1;

message Language {
  oneof _native_name {
  string native_name = 2;
  }
  optional string locale = 1;
}

```

**Source references:** SRC-0214, SRC-1185  
**URL references:** None independently associated  
**Related findings:** FND-00423, FND-00424

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00426"></a>
## FND-00426: chesscom.api.v1.Language.locale = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string locale = 1;

### Evidence

- **SRC-0214** `research/proto/chesscom/api/v1/i18n.proto` — [preserved redacted evidence](../evidence/text/052d60b9d329bbc8548a60bd174fc5e7ba5e433495b6062171e5cb7a1ed903c6.proto)
  Character offset 157.

```text
package chesscom.api.v1;

message Language {
  oneof _native_name {
  string native_name = 2;
  }
  optional string locale = 1;
}

```

**Source references:** SRC-0214, SRC-1185  
**URL references:** None independently associated  
**Related findings:** FND-00423, FND-00424, FND-00425

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00427"></a>
## FND-00427: message declaration: chesscom.api.v1.Location

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Location {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 87.

```text
// source: chesscom/api/v1/location.proto
// syntax: proto3

package chesscom.api.v1;

message Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _time
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00428"></a>
## FND-00428: oneof declaration: chesscom.api.v1.Location._city

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _city {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 108.

```text
e: chesscom/api/v1/location.proto
// syntax: proto3

package chesscom.api.v1;

message Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timez
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00429"></a>
## FND-00429: chesscom.api.v1.Location.city = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string city = 2;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 124.

```text
v1/location.proto
// syntax: proto3

package chesscom.api.v1;

message Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  o
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00430"></a>
## FND-00430: oneof declaration: chesscom.api.v1.Location._region

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _region {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 147.

```text
ntax: proto3

package chesscom.api.v1;

message Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00431"></a>
## FND-00431: chesscom.api.v1.Location.region = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string region = 3;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 165.

```text
age chesscom.api.v1;

message Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  option
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00432"></a>
## FND-00432: oneof declaration: chesscom.api.v1.Location._continent_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _continent_code {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 190.

```text
sage Location {
  oneof _city {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 
```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00433"></a>
## FND-00433: chesscom.api.v1.Location.continent_code = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string continent_code = 4;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 216.

```text
ity {
  string city = 2;
  }
  oneof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00434"></a>
## FND-00434: oneof declaration: chesscom.api.v1.Location._postal_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _postal_code {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 249.

```text
eof _region {
  string region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00435"></a>
## FND-00435: chesscom.api.v1.Location.postal_code = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string postal_code = 5;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 272.

```text
region = 3;
  }
  oneof _continent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00436"></a>
## FND-00436: oneof declaration: chesscom.api.v1.Location._latitude

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _latitude {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 302.

```text
nent_code {
  string continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00437"></a>
## FND-00437: chesscom.api.v1.Location.latitude = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float latitude = 6;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 322.

```text
 continent_code = 4;
  }
  oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00438"></a>
## FND-00438: oneof declaration: chesscom.api.v1.Location._longitude

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _longitude {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 348.

```text
 oneof _postal_code {
  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00439"></a>
## FND-00439: chesscom.api.v1.Location.longitude = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float longitude = 7;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 369.

```text

  string postal_code = 5;
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00440"></a>
## FND-00440: oneof declaration: chesscom.api.v1.Location._timezone

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timezone {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 396.

```text
  }
  oneof _latitude {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00441"></a>
## FND-00441: chesscom.api.v1.Location.timezone = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string timezone = 8;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 416.

```text
e {
  float latitude = 6;
  }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00442"></a>
## FND-00442: oneof declaration: chesscom.api.v1.Location._asn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _asn {

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 443.

```text
 }
  oneof _longitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00443"></a>
## FND-00443: chesscom.api.v1.Location.asn = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 asn = 9;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 458.

```text
gitude {
  float longitude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00444"></a>
## FND-00444: chesscom.api.v1.Location.country_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 1;

### Evidence

- **SRC-0215** `research/proto/chesscom/api/v1/location.proto` — [preserved redacted evidence](../evidence/text/59930a0fe2c4d1160ba8185d4227bddafdd23aca7314eabb026b97b72bb5782f.proto)
  Character offset 479.

```text
itude = 7;
  }
  oneof _timezone {
  string timezone = 8;
  }
  oneof _asn {
  int32 asn = 9;
  }
  optional string country_code = 1;
}

```

**Source references:** SRC-0215, SRC-1186  
**URL references:** None independently associated  
**Related findings:** FND-00427, FND-00428, FND-00429

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00445"></a>
## FND-00445: message declaration: chesscom.api.v1.Money

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Money {

### Evidence

- **SRC-0216** `research/proto/chesscom/api/v1/money.proto` — [preserved redacted evidence](../evidence/text/700cb79422b1cec34b9e9d97f3118094e5c406331a11730fb13d1116af578fa1.proto)
  Character offset 84.

```text
// source: chesscom/api/v1/money.proto
// syntax: proto3

package chesscom.api.v1;

message Money {
  optional string amount = 1;
  optional string currency_code = 2;
}

```

**Source references:** SRC-0216, SRC-1187  
**URL references:** None independently associated  
**Related findings:** FND-00446, FND-00447

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00446"></a>
## FND-00446: chesscom.api.v1.Money.amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string amount = 1;

### Evidence

- **SRC-0216** `research/proto/chesscom/api/v1/money.proto` — [preserved redacted evidence](../evidence/text/700cb79422b1cec34b9e9d97f3118094e5c406331a11730fb13d1116af578fa1.proto)
  Character offset 102.

```text
 source: chesscom/api/v1/money.proto
// syntax: proto3

package chesscom.api.v1;

message Money {
  optional string amount = 1;
  optional string currency_code = 2;
}

```

**Source references:** SRC-0216, SRC-1187  
**URL references:** None independently associated  
**Related findings:** FND-00445, FND-00447

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00447"></a>
## FND-00447: chesscom.api.v1.Money.currency_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string currency_code = 2;

### Evidence

- **SRC-0216** `research/proto/chesscom/api/v1/money.proto` — [preserved redacted evidence](../evidence/text/700cb79422b1cec34b9e9d97f3118094e5c406331a11730fb13d1116af578fa1.proto)
  Character offset 132.

```text
.proto
// syntax: proto3

package chesscom.api.v1;

message Money {
  optional string amount = 1;
  optional string currency_code = 2;
}

```

**Source references:** SRC-0216, SRC-1187  
**URL references:** None independently associated  
**Related findings:** FND-00445, FND-00446

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00448"></a>
## FND-00448: message declaration: chesscom.api.v1.RequestPagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestPagination {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 89.

```text
// source: chesscom/api/v1/pagination.proto
// syntax: proto3

package chesscom.api.v1;

message RequestPagination {
  oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00449, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00449"></a>
## FND-00449: oneof declaration: chesscom.api.v1.RequestPagination._page_size

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _page_size {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 119.

```text
/api/v1/pagination.proto
// syntax: proto3

package chesscom.api.v1;

message RequestPagination {
  oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00450"></a>
## FND-00450: chesscom.api.v1.RequestPagination.page_size = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 page_size = 1;

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 140.

```text
oto
// syntax: proto3

package chesscom.api.v1;

message RequestPagination {
  oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00451"></a>
## FND-00451: oneof declaration: chesscom.api.v1.RequestPagination._page_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _page_token {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 167.

```text
age chesscom.api.v1;

message RequestPagination {
  oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00452"></a>
## FND-00452: chesscom.api.v1.RequestPagination.page_token = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string page_token = 2;

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 189.

```text
message RequestPagination {
  oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00453"></a>
## FND-00453: message declaration: chesscom.api.v1.ResponsePagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ResponsePagination {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 219.

```text
oneof _page_size {
  int32 page_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00454"></a>
## FND-00454: oneof declaration: chesscom.api.v1.ResponsePagination._next_page_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _next_page_token {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 250.

```text
_size = 1;
  }
  oneof _page_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00455"></a>
## FND-00455: chesscom.api.v1.ResponsePagination.next_page_token = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string next_page_token = 1;

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 277.

```text
e_token {
  string page_token = 2;
  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00456"></a>
## FND-00456: oneof declaration: chesscom.api.v1.ResponsePagination._total_size

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_size {

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 311.

```text

  }
}

message ResponsePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00457"></a>
## FND-00457: chesscom.api.v1.ResponsePagination.total_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_size = 2;

### Evidence

- **SRC-0217** `research/proto/chesscom/api/v1/pagination.proto` — [preserved redacted evidence](../evidence/text/bf3ad16b1762687e7e5bdf7abe87fe33f50bed2fe859c6a3e9bcd558c3501786.proto)
  Character offset 333.

```text
sePagination {
  oneof _next_page_token {
  string next_page_token = 1;
  }
  oneof _total_size {
  int32 total_size = 2;
  }
}

```

**Source references:** SRC-0217, SRC-1188  
**URL references:** None independently associated  
**Related findings:** FND-00448, FND-00449, FND-00450

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00458"></a>
## FND-00458: enum declaration: chesscom.api.v1.Platform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Platform {

### Evidence

- **SRC-0218** `research/proto/chesscom/api/v1/platform.proto` — [preserved redacted evidence](../evidence/text/80fdbeb03cb7e61347e16e7c58ecb55279b47beb73a2fbea71cec0a006498b2a.proto)
  Character offset 87.

```text
// source: chesscom/api/v1/platform.proto
// syntax: proto3

package chesscom.api.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_IOS = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_WEB = 3;
}

```

**Source references:** SRC-0218, SRC-1189  
**URL references:** None independently associated  
**Related findings:** FND-00459, FND-00460

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00459"></a>
## FND-00459: chesscom.api.v1.Platform.PLATFORM_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_UNSPECIFIED = 0;

### Evidence

- **SRC-0218** `research/proto/chesscom/api/v1/platform.proto` — [preserved redacted evidence](../evidence/text/80fdbeb03cb7e61347e16e7c58ecb55279b47beb73a2fbea71cec0a006498b2a.proto)
  Character offset 105.

```text
urce: chesscom/api/v1/platform.proto
// syntax: proto3

package chesscom.api.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_IOS = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_WEB = 3;
}

```

**Source references:** SRC-0218, SRC-1189  
**URL references:** None independently associated  
**Related findings:** FND-00458, FND-00460

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00460"></a>
## FND-00460: chesscom.api.v1.Platform.PLATFORM_IOS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_IOS = 1;

### Evidence

- **SRC-0218** `research/proto/chesscom/api/v1/platform.proto` — [preserved redacted evidence](../evidence/text/80fdbeb03cb7e61347e16e7c58ecb55279b47beb73a2fbea71cec0a006498b2a.proto)
  Character offset 133.

```text
rm.proto
// syntax: proto3

package chesscom.api.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_IOS = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_WEB = 3;
}

```

**Source references:** SRC-0218, SRC-1189  
**URL references:** None independently associated  
**Related findings:** FND-00458, FND-00459

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00461"></a>
## FND-00461: chesscom.api.v1.Platform.PLATFORM_ANDROID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_ANDROID = 2;

### Evidence

- **SRC-0218** `research/proto/chesscom/api/v1/platform.proto` — [preserved redacted evidence](../evidence/text/80fdbeb03cb7e61347e16e7c58ecb55279b47beb73a2fbea71cec0a006498b2a.proto)
  Character offset 153.

```text
proto3

package chesscom.api.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_IOS = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_WEB = 3;
}

```

**Source references:** SRC-0218, SRC-1189  
**URL references:** None independently associated  
**Related findings:** FND-00458, FND-00459, FND-00460

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00462"></a>
## FND-00462: chesscom.api.v1.Platform.PLATFORM_WEB = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_WEB = 3;

### Evidence

- **SRC-0218** `research/proto/chesscom/api/v1/platform.proto` — [preserved redacted evidence](../evidence/text/80fdbeb03cb7e61347e16e7c58ecb55279b47beb73a2fbea71cec0a006498b2a.proto)
  Character offset 177.

```text
.api.v1;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_IOS = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_WEB = 3;
}

```

**Source references:** SRC-0218, SRC-1189  
**URL references:** None independently associated  
**Related findings:** FND-00458, FND-00459, FND-00460

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00463"></a>
## FND-00463: message declaration: chesscom.api.v1.SemanticVersion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SemanticVersion {

### Evidence

- **SRC-0219** `research/proto/chesscom/api/v1/semantic_version.proto` — [preserved redacted evidence](../evidence/text/7f68ec1dcd96cd35c214bc1ef87f9c38ebd2971090d7af6d113e10af45f5aa44.proto)
  Character offset 95.

```text
// source: chesscom/api/v1/semantic_version.proto
// syntax: proto3

package chesscom.api.v1;

message SemanticVersion {
  optional int32 major = 1;
  optional int32 minor = 2;
  optional int32 patch = 3;
}

```

**Source references:** SRC-0219, SRC-1190  
**URL references:** None independently associated  
**Related findings:** FND-00464, FND-00465

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00464"></a>
## FND-00464: chesscom.api.v1.SemanticVersion.major = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 major = 1;

### Evidence

- **SRC-0219** `research/proto/chesscom/api/v1/semantic_version.proto` — [preserved redacted evidence](../evidence/text/7f68ec1dcd96cd35c214bc1ef87f9c38ebd2971090d7af6d113e10af45f5aa44.proto)
  Character offset 123.

```text
/v1/semantic_version.proto
// syntax: proto3

package chesscom.api.v1;

message SemanticVersion {
  optional int32 major = 1;
  optional int32 minor = 2;
  optional int32 patch = 3;
}

```

**Source references:** SRC-0219, SRC-1190  
**URL references:** None independently associated  
**Related findings:** FND-00463, FND-00465

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00465"></a>
## FND-00465: chesscom.api.v1.SemanticVersion.minor = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 minor = 2;

### Evidence

- **SRC-0219** `research/proto/chesscom/api/v1/semantic_version.proto` — [preserved redacted evidence](../evidence/text/7f68ec1dcd96cd35c214bc1ef87f9c38ebd2971090d7af6d113e10af45f5aa44.proto)
  Character offset 151.

```text
/ syntax: proto3

package chesscom.api.v1;

message SemanticVersion {
  optional int32 major = 1;
  optional int32 minor = 2;
  optional int32 patch = 3;
}

```

**Source references:** SRC-0219, SRC-1190  
**URL references:** None independently associated  
**Related findings:** FND-00463, FND-00464

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00466"></a>
## FND-00466: chesscom.api.v1.SemanticVersion.patch = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 patch = 3;

### Evidence

- **SRC-0219** `research/proto/chesscom/api/v1/semantic_version.proto` — [preserved redacted evidence](../evidence/text/7f68ec1dcd96cd35c214bc1ef87f9c38ebd2971090d7af6d113e10af45f5aa44.proto)
  Character offset 179.

```text
esscom.api.v1;

message SemanticVersion {
  optional int32 major = 1;
  optional int32 minor = 2;
  optional int32 patch = 3;
}

```

**Source references:** SRC-0219, SRC-1190  
**URL references:** None independently associated  
**Related findings:** FND-00463, FND-00464, FND-00465

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00467"></a>
## FND-00467: message declaration: chesscom.api.v1.Speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Speech {

### Evidence

- **SRC-0220** `research/proto/chesscom/api/v1/speech.proto` — [preserved redacted evidence](../evidence/text/c0188778a2d044a8c901a2cf0971f912d12cd37a9b00f6142a7862e3e83fb355.proto)
  Character offset 85.

```text
// source: chesscom/api/v1/speech.proto
// syntax: proto3

package chesscom.api.v1;

message Speech {
  optional string text = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0220, SRC-1191  
**URL references:** None independently associated  
**Related findings:** FND-00468, FND-00469

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00468"></a>
## FND-00468: chesscom.api.v1.Speech.text = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text = 1;

### Evidence

- **SRC-0220** `research/proto/chesscom/api/v1/speech.proto` — [preserved redacted evidence](../evidence/text/c0188778a2d044a8c901a2cf0971f912d12cd37a9b00f6142a7862e3e83fb355.proto)
  Character offset 104.

```text
ource: chesscom/api/v1/speech.proto
// syntax: proto3

package chesscom.api.v1;

message Speech {
  optional string text = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0220, SRC-1191  
**URL references:** None independently associated  
**Related findings:** FND-00467, FND-00469

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00469"></a>
## FND-00469: chesscom.api.v1.Speech.audio_url_hash = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string audio_url_hash = 2;

### Evidence

- **SRC-0220** `research/proto/chesscom/api/v1/speech.proto` — [preserved redacted evidence](../evidence/text/c0188778a2d044a8c901a2cf0971f912d12cd37a9b00f6142a7862e3e83fb355.proto)
  Character offset 132.

```text
h.proto
// syntax: proto3

package chesscom.api.v1;

message Speech {
  optional string text = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0220, SRC-1191  
**URL references:** None independently associated  
**Related findings:** FND-00467, FND-00468

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00470"></a>
## FND-00470: message declaration: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IsAuthenticatedUserInAudiencesRequest {

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 122.

```text
diences/v1/authenticated_audiences_service.proto
// syntax: proto3

package chesscom.audiences.v1;

message IsAuthenticatedUserInAudiencesRequest {
  repeated string audience_keys = 1;
}

message IsAuthenticatedUserInAudiencesResponse {
  repeated .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value 
```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00471, FND-00472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00471"></a>
## FND-00471: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesRequest.audience_keys = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string audience_keys = 1;

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 172.

```text
/ syntax: proto3

package chesscom.audiences.v1;

message IsAuthenticatedUserInAudiencesRequest {
  repeated string audience_keys = 1;
}

message IsAuthenticatedUserInAudiencesResponse {
  repeated .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00472"></a>
## FND-00472: message declaration: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IsAuthenticatedUserInAudiencesResponse {

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 210.

```text
iences.v1;

message IsAuthenticatedUserInAudiencesRequest {
  repeated string audience_keys = 1;
}

message IsAuthenticatedUserInAudiencesResponse {
  repeated .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00471

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00473"></a>
## FND-00473: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.in_audience = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 261.

```text
equest {
  repeated string audience_keys = 1;
}

message IsAuthenticatedUserInAudiencesResponse {
  repeated .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00471, FND-00472

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00474"></a>
## FND-00474: message declaration: chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InAudienceEntry {

### Evidence

- **SRC-0221** `research/proto/chesscom/audiences/v1/authenticated_audiences_service.proto` — [preserved redacted evidence](../evidence/text/c9b124c41ef2a6d8314aad4f81e9517e948b63507a42bd46598ddd8ceb448140.proto)
  Character offset 367.

```text
ed .chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse.InAudienceEntry in_audience = 1;
  message InAudienceEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0221, SRC-1192  
**URL references:** None independently associated  
**Related findings:** FND-00470, FND-00471, FND-00472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
