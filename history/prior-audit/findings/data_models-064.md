# data_models — findings 6301–6400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06575"></a>
## FND-06575: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_IPAY88 = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_IPAY88 = 25;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4512.

```text
YMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYM
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06576"></a>
## FND-06576: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_M_PESA = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_M_PESA = 26;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4542.

```text
 PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06577"></a>
## FND-06577: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4572.

```text
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06578"></a>
## FND-06578: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_CRYPTO = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_CRYPTO = 28;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4617.

```text
NT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06579"></a>
## FND-06579: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_GOOGLEPAY = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_GOOGLEPAY = 29;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4647.

```text
NT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06580"></a>
## FND-06580: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_APPLEPAY = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_APPLEPAY = 30;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4680.

```text
METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06581"></a>
## FND-06581: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_NEQUI = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_NEQUI = 31;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4712.

```text
7;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06582"></a>
## FND-06582: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_PIX = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_PIX = 32;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4741.

```text
28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEAC
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06583"></a>
## FND-06583: enum declaration: chesscom.payments.v1.PaymentTrigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentTrigger {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4769.

```text
AY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum Product
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06584"></a>
## FND-06584: chesscom.payments.v1.PaymentTrigger.PAYMENT_TRIGGER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TRIGGER_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4793.

```text
D_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06585"></a>
## FND-06585: chesscom.payments.v1.PaymentTrigger.PAYMENT_TRIGGER_USER_INITIATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TRIGGER_USER_INITIATED = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4828.

```text
EQUI = 31;
  PAYMENT_METHOD_PIX = 32;
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06586"></a>
## FND-06586: chesscom.payments.v1.PaymentTrigger.PAYMENT_TRIGGER_AUTOMATED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TRIGGER_AUTOMATED = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4866.

```text
}

enum PaymentTrigger {
  PAYMENT_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06587"></a>
## FND-06587: enum declaration: chesscom.payments.v1.PlanState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlanState {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4900.

```text
_TRIGGER_UNSPECIFIED = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRO
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06588"></a>
## FND-06588: chesscom.payments.v1.PlanState.PLAN_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4919.

```text
D = 0;
  PAYMENT_TRIGGER_USER_INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06589"></a>
## FND-06589: chesscom.payments.v1.PlanState.PLAN_STATE_ACTIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE_ACTIVE = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4949.

```text
INITIATED = 1;
  PAYMENT_TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMB
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06590"></a>
## FND-06590: chesscom.payments.v1.PlanState.PLAN_STATE_PAST_DUE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE_PAST_DUE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4974.

```text
TRIGGER_AUTOMATED = 2;
}

enum PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum Memb
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06591"></a>
## FND-06591: chesscom.payments.v1.PlanState.PLAN_STATE_CANCELLED_ACTIVE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE_CANCELLED_ACTIVE = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5001.

```text
num PlanState {
  PLAN_STATE_UNSPECIFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06592"></a>
## FND-06592: chesscom.payments.v1.PlanState.PLAN_STATE_CANCELLED_DEACTIVATED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAN_STATE_CANCELLED_DEACTIVATED = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5036.

```text
IFIED = 0;
  PLAN_STATE_ACTIVE = 1;
  PLAN_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06593"></a>
## FND-06593: enum declaration: chesscom.payments.v1.ProductType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ProductType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5077.

```text
N_STATE_PAST_DUE = 2;
  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_AB
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06594"></a>
## FND-06594: chesscom.payments.v1.ProductType.PRODUCT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5098.

```text

  PLAN_STATE_CANCELLED_ACTIVE = 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06595"></a>
## FND-06595: chesscom.payments.v1.ProductType.PRODUCT_TYPE_MEMBERSHIP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_MEMBERSHIP = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5130.

```text
 3;
  PLAN_STATE_CANCELLED_DEACTIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06596"></a>
## FND-06596: chesscom.payments.v1.ProductType.PRODUCT_TYPE_DONATION = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_DONATION = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5161.

```text
TIVATED = 4;
}

enum ProductType {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06597"></a>
## FND-06597: chesscom.payments.v1.ProductType.PRODUCT_TYPE_COURSE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_COURSE = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5190.

```text
ype {
  PRODUCT_TYPE_UNSPECIFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06598"></a>
## FND-06598: chesscom.payments.v1.ProductType.PRODUCT_TYPE_VERIFIED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_VERIFIED = 9;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5217.

```text
IFIED = 0;
  PRODUCT_TYPE_MEMBERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06599"></a>
## FND-06599: chesscom.payments.v1.ProductType.PRODUCT_TYPE_GROUP_MEMBERSHIP = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5246.

```text
BERSHIP = 1;
  PRODUCT_TYPE_DONATION = 7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATIN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06600"></a>
## FND-06600: enum declaration: chesscom.payments.v1.MembershipLevel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MembershipLevel {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5285.

```text
7;
  PRODUCT_TYPE_COURSE = 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 5
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06601"></a>
## FND-06601: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5310.

```text
= 8;
  PRODUCT_TYPE_VERIFIED = 9;
  PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MOD
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06602"></a>
## FND-06602: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_CHEATER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_CHEATER = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5346.

```text
PRODUCT_TYPE_GROUP_MEMBERSHIP = 10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAF
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06603"></a>
## FND-06603: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_ABUSER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_ABUSER = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5378.

```text
10;
}

enum MembershipLevel {
  MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  P
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06604"></a>
## FND-06604: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5409.

```text
 MEMBERSHIP_LEVEL_UNSPECIFIED = 0;
  MEMBERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  P
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06605"></a>
## FND-06605: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_BASIC = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_BASIC = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5450.

```text
ERSHIP_LEVEL_CHEATER = 5;
  MEMBERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_S
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06606"></a>
## FND-06606: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_NO_ADS = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_NO_ADS = 20;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5481.

```text
BERSHIP_LEVEL_ABUSER = 6;
  MEMBERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06607"></a>
## FND-06607: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_GOLD = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_GOLD = 30;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5513.

```text
ERSHIP_LEVEL_VOLUNTARY_CLOSED = 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06608"></a>
## FND-06608: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_PLATINUM = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_PLATINUM = 40;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5543.

```text
= 7;
  MEMBERSHIP_LEVEL_BASIC = 10;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06609"></a>
## FND-06609: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_DIAMOND = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_DIAMOND = 50;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5577.

```text
;
  MEMBERSHIP_LEVEL_NO_ADS = 20;
  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialSta
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06610"></a>
## FND-06610: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_MODERATOR = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_MODERATOR = 60;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5610.

```text

  MEMBERSHIP_LEVEL_GOLD = 30;
  MEMBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06611"></a>
## FND-06611: chesscom.payments.v1.MembershipLevel.MEMBERSHIP_LEVEL_STAFF = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MEMBERSHIP_LEVEL_STAFF = 70;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5645.

```text
MBERSHIP_LEVEL_PLATINUM = 40;
  MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06612"></a>
## FND-06612: enum declaration: chesscom.payments.v1.PriceGroup

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PriceGroup {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5677.

```text
MEMBERSHIP_LEVEL_DIAMOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06613"></a>
## FND-06613: chesscom.payments.v1.PriceGroup.PRICE_GROUP_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5697.

```text
MOND = 50;
  MEMBERSHIP_LEVEL_MODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TR
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06614"></a>
## FND-06614: chesscom.payments.v1.PriceGroup.PRICE_GROUP_SEPT_2022 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_SEPT_2022 = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5728.

```text
ODERATOR = 60;
  MEMBERSHIP_LEVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enu
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06615"></a>
## FND-06615: chesscom.payments.v1.PriceGroup.PRICE_GROUP_SEPT_2026_V1 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_SEPT_2026_V1 = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5757.

```text
EVEL_STAFF = 70;
}

enum PriceGroup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06616"></a>
## FND-06616: chesscom.payments.v1.PriceGroup.PRICE_GROUP_SEPT_2026_V2 = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_SEPT_2026_V2 = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5789.

```text
oup {
  PRICE_GROUP_UNSPECIFIED = 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSIN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06617"></a>
## FND-06617: chesscom.payments.v1.PriceGroup.PRICE_GROUP_JAN_2027_V2 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_JAN_2027_V2 = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5821.

```text
= 0;
  PRICE_GROUP_SEPT_2022 = 1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSIN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06618"></a>
## FND-06618: chesscom.payments.v1.PriceGroup.PRICE_GROUP_JAN_2027_V3 = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRICE_GROUP_JAN_2027_V3 = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5852.

```text
1;
  PRICE_GROUP_SEPT_2026_V1 = 2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

en
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06619"></a>
## FND-06619: enum declaration: chesscom.payments.v1.TrialState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrialState {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5884.

```text
2;
  PRICE_GROUP_SEPT_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06620"></a>
## FND-06620: chesscom.payments.v1.TrialState.TRIAL_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5904.

```text
T_2026_V2 = 3;
  PRICE_GROUP_JAN_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06621"></a>
## FND-06621: chesscom.payments.v1.TrialState.TRIAL_STATE_ACTIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE_ACTIVE = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5935.

```text
N_2027_V2 = 4;
  PRICE_GROUP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  ST
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06622"></a>
## FND-06622: chesscom.payments.v1.TrialState.TRIAL_STATE_ENDED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE_ENDED = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5961.

```text
UP_JAN_2027_V3 = 5;
}

enum TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  ST
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06623"></a>
## FND-06623: chesscom.payments.v1.TrialState.TRIAL_STATE_CANCELLED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE_CANCELLED = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 5986.

```text
um TrialState {
  TRIAL_STATE_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06624"></a>
## FND-06624: chesscom.payments.v1.TrialState.TRIAL_STATE_CONVERTED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRIAL_STATE_CONVERTED = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6015.

```text
_UNSPECIFIED = 0;
  TRIAL_STATE_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REV
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06625"></a>
## FND-06625: enum declaration: chesscom.payments.v1.BusinessEntity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BusinessEntity {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6045.

```text
E_ACTIVE = 1;
  TRIAL_STATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06626"></a>
## FND-06626: chesscom.payments.v1.BusinessEntity.BUSINESS_ENTITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BUSINESS_ENTITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6069.

```text
ATE_ENDED = 2;
  TRIAL_STATE_CANCELLED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06627"></a>
## FND-06627: chesscom.payments.v1.BusinessEntity.BUSINESS_ENTITY_CHESSCOM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BUSINESS_ENTITY_CHESSCOM = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6104.

```text
LED = 3;
  TRIAL_STATE_CONVERTED = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06628"></a>
## FND-06628: chesscom.payments.v1.BusinessEntity.BUSINESS_ENTITY_CHESSABLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BUSINESS_ENTITY_CHESSABLE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6136.

```text
 = 4;
}

enum BusinessEntity {
  BUSINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATU
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06629"></a>
## FND-06629: enum declaration: chesscom.payments.v1.StatusCode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StatusCode {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6170.

```text
USINESS_ENTITY_UNSPECIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06630"></a>
## FND-06630: chesscom.payments.v1.StatusCode.STATUS_CODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6190.

```text
CIFIED = 0;
  BUSINESS_ENTITY_CHESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANC
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06631"></a>
## FND-06631: chesscom.payments.v1.StatusCode.STATUS_CODE_ADMIN_CANCEL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_ADMIN_CANCEL = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6221.

```text
HESSCOM = 1;
  BUSINESS_ENTITY_CHESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06632"></a>
## FND-06632: chesscom.payments.v1.StatusCode.STATUS_CODE_CANCEL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_CANCEL = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6253.

```text
HESSABLE = 2;
}

enum StatusCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSIT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06633"></a>
## FND-06633: chesscom.payments.v1.StatusCode.STATUS_CODE_CHARGEBACK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_CHARGEBACK = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6279.

```text
usCode {
  STATUS_CODE_UNSPECIFIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PR
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06634"></a>
## FND-06634: chesscom.payments.v1.StatusCode.STATUS_CODE_CHARGEBACK_REVERSED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_CHARGEBACK_REVERSED = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6309.

```text
FIED = 0;
  STATUS_CODE_ADMIN_CANCEL = 1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_RE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06635"></a>
## FND-06635: chesscom.payments.v1.StatusCode.STATUS_CODE_DUPLICATE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_DUPLICATE = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6348.

```text
1;
  STATUS_CODE_CANCEL = 2;
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06636"></a>
## FND-06636: chesscom.payments.v1.StatusCode.STATUS_CODE_ENDED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_ENDED = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6377.

```text
  STATUS_CODE_CHARGEBACK = 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 1
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06637"></a>
## FND-06637: chesscom.payments.v1.StatusCode.STATUS_CODE_FAILED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_FAILED = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6402.

```text
= 3;
  STATUS_CODE_CHARGEBACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06638"></a>
## FND-06638: chesscom.payments.v1.StatusCode.STATUS_CODE_NEW = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_NEW = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6428.

```text
ACK_REVERSED = 4;
  STATUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_T
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06639"></a>
## FND-06639: chesscom.payments.v1.StatusCode.STATUS_CODE_PAYPAL_AGREEMENT = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_PAYPAL_AGREEMENT = 9;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6451.

```text
TUS_CODE_DUPLICATE = 5;
  STATUS_CODE_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STAT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06640"></a>
## FND-06640: chesscom.payments.v1.StatusCode.STATUS_CODE_PAYPAL_CANCEL = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_PAYPAL_CANCEL = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6487.

```text
E_ENDED = 6;
  STATUS_CODE_FAILED = 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06641"></a>
## FND-06641: chesscom.payments.v1.StatusCode.STATUS_CODE_PENDING = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_PENDING = 11;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6521.

```text
= 7;
  STATUS_CODE_NEW = 8;
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06642"></a>
## FND-06642: chesscom.payments.v1.StatusCode.STATUS_CODE_PLAN_TRANSITION = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_PLAN_TRANSITION = 12;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6549.

```text
  STATUS_CODE_PAYPAL_AGREEMENT = 9;
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06643"></a>
## FND-06643: chesscom.payments.v1.StatusCode.STATUS_CODE_PROCESSED = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_PROCESSED = 13;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6585.

```text
  STATUS_CODE_PAYPAL_CANCEL = 10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessCh
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06644"></a>
## FND-06644: chesscom.payments.v1.StatusCode.STATUS_CODE_REACTIVATED = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_REACTIVATED = 14;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6615.

```text
10;
  STATUS_CODE_PENDING = 11;
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURS
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06645"></a>
## FND-06645: chesscom.payments.v1.StatusCode.STATUS_CODE_REFUND = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_REFUND = 15;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6647.

```text
  STATUS_CODE_PLAN_TRANSITION = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIF
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06646"></a>
## FND-06646: chesscom.payments.v1.StatusCode.STATUS_CODE_SHUTOFF = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_SHUTOFF = 16;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6674.

```text
ON = 12;
  STATUS_CODE_PROCESSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06647"></a>
## FND-06647: chesscom.payments.v1.StatusCode.STATUS_CODE_TRIAL_CANCEL = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_TRIAL_CANCEL = 17;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6702.

```text
SSED = 13;
  STATUS_CODE_REACTIVATED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06648"></a>
## FND-06648: chesscom.payments.v1.StatusCode.STATUS_CODE_TRIAL_ENDED = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_TRIAL_ENDED = 18;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6735.

```text
TED = 14;
  STATUS_CODE_REFUND = 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_C
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06649"></a>
## FND-06649: chesscom.payments.v1.StatusCode.STATUS_CODE_INCENTIVE_REDEMPTION = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_INCENTIVE_REDEMPTION = 19;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6767.

```text
 15;
  STATUS_CODE_SHUTOFF = 16;
  STATUS_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

en
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06650"></a>
## FND-06650: chesscom.payments.v1.StatusCode.STATUS_CODE_REFUND_FAILED = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_REFUND_FAILED = 20;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6808.

```text
_CODE_TRIAL_CANCEL = 17;
  STATUS_CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_R
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06651"></a>
## FND-06651: chesscom.payments.v1.StatusCode.STATUS_CODE_REFUND_PENDING = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_CODE_REFUND_PENDING = 21;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6842.

```text
CODE_TRIAL_ENDED = 18;
  STATUS_CODE_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SU
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06652"></a>
## FND-06652: enum declaration: chesscom.payments.v1.PlatformCourseAccessChangedAction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlatformCourseAccessChangedAction {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6878.

```text
_INCENTIVE_REDEMPTION = 19;
  STATUS_CODE_REFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CAN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06653"></a>
## FND-06653: chesscom.payments.v1.PlatformCourseAccessChangedAction.PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6921.

```text
EFUND_FAILED = 20;
  STATUS_CODE_REFUND_PENDING = 21;
}

enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  C
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06654"></a>
## FND-06654: chesscom.payments.v1.PlatformCourseAccessChangedAction.PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 6978.

```text
enum PlatformCourseAccessChangedAction {
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REAS
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06655"></a>
## FND-06655: chesscom.payments.v1.PlatformCourseAccessChangedAction.PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7031.

```text
OURSE_ACCESS_CHANGED_ACTION_UNSPECIFIED = 0;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMF
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06656"></a>
## FND-06656: enum declaration: chesscom.payments.v1.CancelSurveyReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CancelSurveyReason {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7085.

```text
M_COURSE_ACCESS_CHANGED_ACTION_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06657"></a>
## FND-06657: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7113.

```text
ON_GRANTED = 1;
  PLATFORM_COURSE_ACCESS_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06658"></a>
## FND-06658: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7153.

```text
_CHANGED_ACTION_REVOKED = 2;
}

enum CancelSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaym
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06659"></a>
## FND-06659: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7195.

```text
lSurveyReason {
  CANCEL_SURVEY_REASON_UNSPECIFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06660"></a>
## FND-06660: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_USING_OTHER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_USING_OTHER = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7240.

```text
IFIED = 0;
  CANCEL_SURVEY_REASON_TOO_EXPENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATU
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06661"></a>
## FND-06661: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_LESS_INTEREST = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_LESS_INTEREST = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7280.

```text
PENSIVE = 1;
  CANCEL_SURVEY_REASON_TECHNICAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYM
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06662"></a>
## FND-06662: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7322.

```text
CAL_ISSUES = 2;
  CANCEL_SURVEY_REASON_USING_OTHER = 3;
  CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTIO
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06663"></a>
## FND-06663: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_OTHER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_OTHER = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7379.

```text
 CANCEL_SURVEY_REASON_LESS_INTEREST = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06664"></a>
## FND-06664: chesscom.payments.v1.CancelSurveyReason.CANCEL_SURVEY_REASON_NOT_USING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CANCEL_SURVEY_REASON_NOT_USING = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7413.

```text
T = 4;
  CANCEL_SURVEY_REASON_NOT_COMFORTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06665"></a>
## FND-06665: enum declaration: chesscom.payments.v1.SubscriptionPaymentStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SubscriptionPaymentStatus {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7452.

```text
RTABLE_AUTO_RENEWAL = 5;
  CANCEL_SURVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06666"></a>
## FND-06666: chesscom.payments.v1.SubscriptionPaymentStatus.SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7487.

```text
URVEY_REASON_OTHER = 6;
  CANCEL_SURVEY_REASON_NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06667"></a>
## FND-06667: chesscom.payments.v1.SubscriptionPaymentStatus.SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7534.

```text
NOT_USING = 7;
}

enum SubscriptionPaymentStatus {
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06668"></a>
## FND-06668: chesscom.payments.v1.SubscriptionPaymentStatus.SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7583.

```text
{
  SUBSCRIPTION_PAYMENT_STATUS_UNSPECIFIED = 0;
  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06669"></a>
## FND-06669: chesscom.payments.v1.SubscriptionPaymentStatus.SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 7631.

```text

  SUBSCRIPTION_PAYMENT_STATUS_GOOD_STANDING = 1;
  SUBSCRIPTION_PAYMENT_STATUS_SOFT_FAILURE = 2;
  SUBSCRIPTION_PAYMENT_STATUS_HARD_FAILURE = 3;
}

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06670"></a>
## FND-06670: message declaration: chesscom.payments.v1.FoundCharge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FoundCharge {

### Evidence

- **SRC-0489** `research/proto/chesscom/payments/v1/found_charge.proto` — [preserved redacted evidence](../evidence/text/d36536778e0389328a09118501d063cd3ae6fc18476ad91d3e940fc7302f394f.proto)
  Character offset 101.

```text
/ source: chesscom/payments/v1/found_charge.proto
// syntax: proto3

package chesscom.payments.v1;

message FoundCharge {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.Charge charge = 2;
}

```

**Source references:** SRC-0489, SRC-1460  
**URL references:** None independently associated  
**Related findings:** FND-06671, FND-06672

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06671"></a>
## FND-06671: chesscom.payments.v1.FoundCharge.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0489** `research/proto/chesscom/payments/v1/found_charge.proto` — [preserved redacted evidence](../evidence/text/d36536778e0389328a09118501d063cd3ae6fc18476ad91d3e940fc7302f394f.proto)
  Character offset 125.

```text
nts/v1/found_charge.proto
// syntax: proto3

package chesscom.payments.v1;

message FoundCharge {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.Charge charge = 2;
}

```

**Source references:** SRC-0489, SRC-1460  
**URL references:** None independently associated  
**Related findings:** FND-06670, FND-06672

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06672"></a>
## FND-06672: chesscom.payments.v1.FoundCharge.charge = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.Charge charge = 2;

### Evidence

- **SRC-0489** `research/proto/chesscom/payments/v1/found_charge.proto` — [preserved redacted evidence](../evidence/text/d36536778e0389328a09118501d063cd3ae6fc18476ad91d3e940fc7302f394f.proto)
  Character offset 158.

```text
ax: proto3

package chesscom.payments.v1;

message FoundCharge {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.Charge charge = 2;
}

```

**Source references:** SRC-0489, SRC-1460  
**URL references:** None independently associated  
**Related findings:** FND-06670, FND-06671

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06673"></a>
## FND-06673: message declaration: chesscom.payments.v1.ListEligibleGiftRecipientsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListEligibleGiftRecipientsRequest {

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 101.

```text
/ source: chesscom/payments/v1/gift_service.proto
// syntax: proto3

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
**Related findings:** FND-06674, FND-06675

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06674"></a>
## FND-06674: oneof declaration: chesscom.payments.v1.ListEligibleGiftRecipientsRequest._product

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product {

### Evidence

- **SRC-0490** `research/proto/chesscom/payments/v1/gift_service.proto` — [preserved redacted evidence](../evidence/text/1ce7a50e4bae03c7979a420158f5cc9001ac9cf5c3cd4f203373e9f377995b3f.proto)
  Character offset 147.

```text
oto
// syntax: proto3

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
**Related findings:** FND-06673, FND-06675

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
