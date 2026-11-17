# data_models — findings 6201–6300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06475"></a>
## FND-06475: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_COUPON = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_COUPON = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1077.

```text
CENTIVE_CHARGE_TYPE_NEXT_X_CHARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06476"></a>
## FND-06476: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_SPECIAL_OFFER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_SPECIAL_OFFER = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1106.

```text
ARGES = 3;
}

enum IncentiveType {
  INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OF
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06477"></a>
## FND-06477: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1142.

```text
 INCENTIVE_TYPE_UNSPECIFIED = 0;
  INCENTIVE_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06478"></a>
## FND-06478: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1185.

```text
E_TYPE_COUPON = 1;
  INCENTIVE_TYPE_SPECIAL_OFFER = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06479"></a>
## FND-06479: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_STUDENT_DISCOUNT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1234.

```text
 = 2;
  INCENTIVE_TYPE_SPECIAL_OFFER_WINDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06480"></a>
## FND-06480: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_REACTIVATION_OFFER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_REACTIVATION_OFFER = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1273.

```text
NDOW = 3;
  INCENTIVE_TYPE_SPECIAL_OFFER_TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06481"></a>
## FND-06481: chesscom.payments.v1.IncentiveType.INCENTIVE_TYPE_FREEVIEW = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TYPE_FREEVIEW = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1314.

```text
TENURE_BASED = 4;
  INCENTIVE_TYPE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum Subscri
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06482"></a>
## FND-06482: enum declaration: chesscom.payments.v1.IncentiveOfferType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IncentiveOfferType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1346.

```text
PE_STUDENT_DISCOUNT = 5;
  INCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06483"></a>
## FND-06483: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1374.

```text
NCENTIVE_TYPE_REACTIVATION_OFFER = 6;
  INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06484"></a>
## FND-06484: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_FREE_TIME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_FREE_TIME = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1414.

```text
INCENTIVE_TYPE_FREEVIEW = 7;
}

enum IncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY =
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06485"></a>
## FND-06485: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_DISCOUNT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_DISCOUNT = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1452.

```text
ncentiveOfferType {
  INCENTIVE_OFFER_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06486"></a>
## FND-06486: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1489.

```text
_TYPE_UNSPECIFIED = 0;
  INCENTIVE_OFFER_TYPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MON
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06487"></a>
## FND-06487: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1531.

```text
YPE_FREE_TIME = 1;
  INCENTIVE_OFFER_TYPE_DISCOUNT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06488"></a>
## FND-06488: chesscom.payments.v1.IncentiveOfferType.INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1579.

```text
NT = 2;
  INCENTIVE_OFFER_TYPE_FREE_LIFETIME = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEM
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06489"></a>
## FND-06489: enum declaration: chesscom.payments.v1.SubscriptionDurationUnit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SubscriptionDurationUnit {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1622.

```text
E = 3;
  INCENTIVE_OFFER_TYPE_DISCOUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06490"></a>
## FND-06490: chesscom.payments.v1.SubscriptionDurationUnit.SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1656.

```text
OUNT_PERCENTAGE = 4;
  INCENTIVE_OFFER_TYPE_OPENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUM
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06491"></a>
## FND-06491: chesscom.payments.v1.SubscriptionDurationUnit.SUBSCRIPTION_DURATION_UNIT_DAY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_DURATION_UNIT_DAY = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1702.

```text
ENING_OFFER = 5;
}

enum SubscriptionDurationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06492"></a>
## FND-06492: chesscom.payments.v1.SubscriptionDurationUnit.SUBSCRIPTION_DURATION_UNIT_WEEK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_DURATION_UNIT_WEEK = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1740.

```text
urationUnit {
  SUBSCRIPTION_DURATION_UNIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MOND
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06493"></a>
## FND-06493: chesscom.payments.v1.SubscriptionDurationUnit.SUBSCRIPTION_DURATION_UNIT_MONTH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_DURATION_UNIT_MONTH = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1779.

```text
NIT_UNSPECIFIED = 0;
  SUBSCRIPTION_DURATION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRID
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06494"></a>
## FND-06494: chesscom.payments.v1.SubscriptionDurationUnit.SUBSCRIPTION_DURATION_UNIT_YEAR = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUBSCRIPTION_DURATION_UNIT_YEAR = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1819.

```text
TION_UNIT_DAY = 1;
  SUBSCRIPTION_DURATION_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06495"></a>
## FND-06495: enum declaration: chesscom.payments.v1.IncentiveTemplate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IncentiveTemplate {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1859.

```text
ON_UNIT_WEEK = 2;
  SUBSCRIPTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SP
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06496"></a>
## FND-06496: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1886.

```text
PTION_DURATION_UNIT_MONTH = 3;
  SUBSCRIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06497"></a>
## FND-06497: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_BAU = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_BAU = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1924.

```text
RIPTION_DURATION_UNIT_YEAR = 4;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06498"></a>
## FND-06498: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_SUMMER_SALE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_SUMMER_SALE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1954.

```text
;
}

enum IncentiveTemplate {
  INCENTIVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06499"></a>
## FND-06499: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 1992.

```text
IVE_TEMPLATE_UNSPECIFIED = 0;
  INCENTIVE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06500"></a>
## FND-06500: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_CYBER_MONDAY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2031.

```text
VE_TEMPLATE_BAU = 1;
  INCENTIVE_TEMPLATE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06501"></a>
## FND-06501: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2070.

```text
TE_SUMMER_SALE = 2;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;

```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06502"></a>
## FND-06502: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2114.

```text
CK_FRIDAY = 3;
  INCENTIVE_TEMPLATE_CYBER_MONDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMO
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06503"></a>
## FND-06503: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2158.

```text
NDAY = 4;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06504"></a>
## FND-06504: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2201.

```text
_2025 = 5;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2025 = 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORD
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06505"></a>
## FND-06505: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2251.

```text
= 6;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026 = 7;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06506"></a>
## FND-06506: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2302.

```text
NCENTIVE_TEMPLATE_SPRING_SALE_2026_PICNIC = 8;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHAS
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06507"></a>
## FND-06507: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2347.

```text
;
  INCENTIVE_TEMPLATE_SPRING_SALE_2026_WINBACK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06508"></a>
## FND-06508: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2392.

```text
CK = 9;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026 = 10;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06509"></a>
## FND-06509: chesscom.payments.v1.IncentiveTemplate.INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2445.

```text
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026 = 11;
  INCENTIVE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06510"></a>
## FND-06510: enum declaration: chesscom.payments.v1.OrderType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum OrderType {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2499.

```text
VE_TEMPLATE_BLACK_FRIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIF
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06511"></a>
## FND-06511: chesscom.payments.v1.OrderType.ORDER_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2518.

```text
RIDAY_2026_DIAMOND = 12;
  INCENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06512"></a>
## FND-06512: chesscom.payments.v1.OrderType.ORDER_TYPE_GIFT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_GIFT = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2548.

```text
ENTIVE_TEMPLATE_CYBER_MONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06513"></a>
## FND-06513: chesscom.payments.v1.OrderType.ORDER_TYPE_PRODUCT_CHANGE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_PRODUCT_CHANGE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2571.

```text
ONDAY_2026_DIAMOND = 13;
}

enum OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAY
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06514"></a>
## FND-06514: chesscom.payments.v1.OrderType.ORDER_TYPE_PURCHASE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_PURCHASE = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2604.

```text
OrderType {
  ORDER_TYPE_UNSPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06515"></a>
## FND-06515: chesscom.payments.v1.OrderType.ORDER_TYPE_RENEWAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_RENEWAL = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2631.

```text
SPECIFIED = 0;
  ORDER_TYPE_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06516"></a>
## FND-06516: chesscom.payments.v1.OrderType.ORDER_TYPE_TRIAL = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_TRIAL = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2657.

```text
E_GIFT = 1;
  ORDER_TYPE_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06517"></a>
## FND-06517: chesscom.payments.v1.OrderType.ORDER_TYPE_TRIAL_CONVERSION = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_TRIAL_CONVERSION = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2681.

```text
_PRODUCT_CHANGE = 2;
  ORDER_TYPE_PURCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06518"></a>
## FND-06518: chesscom.payments.v1.OrderType.ORDER_TYPE_FREE_EXTENSION = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_FREE_EXTENSION = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2716.

```text
URCHASE = 3;
  ORDER_TYPE_RENEWAL = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06519"></a>
## FND-06519: chesscom.payments.v1.OrderType.ORDER_TYPE_FREE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ORDER_TYPE_FREE = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2749.

```text
 = 4;
  ORDER_TYPE_TRIAL = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06520"></a>
## FND-06520: enum declaration: chesscom.payments.v1.PaymentAction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentAction {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2773.

```text
 = 5;
  ORDER_TYPE_TRIAL_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06521"></a>
## FND-06521: chesscom.payments.v1.PaymentAction.PAYMENT_ACTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_ACTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2796.

```text
L_CONVERSION = 6;
  ORDER_TYPE_FREE_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06522"></a>
## FND-06522: chesscom.payments.v1.PaymentAction.PAYMENT_ACTION_AUTHORISE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_ACTION_AUTHORISE = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2830.

```text
E_EXTENSION = 7;
  ORDER_TYPE_FREE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum Paym
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06523"></a>
## FND-06523: chesscom.payments.v1.PaymentAction.PAYMENT_ACTION_PAY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_ACTION_PAY = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2862.

```text
EE = 8;
}

enum PaymentAction {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNS
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06524"></a>
## FND-06524: chesscom.payments.v1.PaymentAction.PAYMENT_ACTION_RENEW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_ACTION_RENEW = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2888.

```text
ion {
  PAYMENT_ACTION_UNSPECIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06525"></a>
## FND-06525: chesscom.payments.v1.PaymentAction.PAYMENT_ACTION_DONATE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_ACTION_DONATE = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2916.

```text
CIFIED = 0;
  PAYMENT_ACTION_AUTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TAR
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06526"></a>
## FND-06526: enum declaration: chesscom.payments.v1.PaymentContext

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentContext {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2946.

```text
UTHORISE = 1;
  PAYMENT_ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum Payment
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06527"></a>
## FND-06527: chesscom.payments.v1.PaymentContext.PAYMENT_CONTEXT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_CONTEXT_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 2970.

```text
ACTION_PAY = 2;
  PAYMENT_ACTION_RENEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06528"></a>
## FND-06528: chesscom.payments.v1.PaymentContext.PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3005.

```text
NEW = 3;
  PAYMENT_ACTION_DONATE = 4;
}

enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06529"></a>
## FND-06529: chesscom.payments.v1.PaymentContext.PAYMENT_CONTEXT_MEMBERSHIP = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_CONTEXT_MEMBERSHIP = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3044.

```text


enum PaymentContext {
  PAYMENT_CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06530"></a>
## FND-06530: chesscom.payments.v1.PaymentContext.PAYMENT_CONTEXT_DONATION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_CONTEXT_DONATION = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3078.

```text
CONTEXT_UNSPECIFIED = 0;
  PAYMENT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_AP
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06531"></a>
## FND-06531: chesscom.payments.v1.PaymentContext.PAYMENT_CONTEXT_COURSE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_CONTEXT_COURSE = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3110.

```text
NT_CONTEXT_GIFT_MEMBERSHIP = 1;
  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06532"></a>
## FND-06532: enum declaration: chesscom.payments.v1.PaymentTarget

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentTarget {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3141.

```text

  PAYMENT_CONTEXT_MEMBERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06533"></a>
## FND-06533: chesscom.payments.v1.PaymentTarget.PAYMENT_TARGET_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TARGET_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3164.

```text
ERSHIP = 2;
  PAYMENT_CONTEXT_DONATION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06534"></a>
## FND-06534: chesscom.payments.v1.PaymentTarget.PAYMENT_TARGET_SELF = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TARGET_SELF = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3198.

```text
TION = 3;
  PAYMENT_CONTEXT_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEB
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06535"></a>
## FND-06535: chesscom.payments.v1.PaymentTarget.PAYMENT_TARGET_OTHER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_TARGET_OTHER = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3225.

```text
_COURSE = 4;
}

enum PaymentTarget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06536"></a>
## FND-06536: enum declaration: chesscom.payments.v1.PaymentGateway

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentGateway {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3254.

```text
arget {
  PAYMENT_TARGET_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06537"></a>
## FND-06537: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3278.

```text
_UNSPECIFIED = 0;
  PAYMENT_TARGET_SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_G
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06538"></a>
## FND-06538: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_AUTHORIZE_NET = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_AUTHORIZE_NET = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3313.

```text
SELF = 1;
  PAYMENT_TARGET_OTHER = 2;
}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEW
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06539"></a>
## FND-06539: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_PAYPAL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_PAYPAL = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3350.

```text

}

enum PaymentGateway {
  PAYMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06540"></a>
## FND-06540: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_APPLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_APPLE = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3380.

```text
YMENT_GATEWAY_UNSPECIFIED = 0;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIE
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06541"></a>
## FND-06541: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_LITLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_LITLE = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3409.

```text
;
  PAYMENT_GATEWAY_AUTHORIZE_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDI
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06542"></a>
## FND-06542: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_STRIPE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_STRIPE = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3438.

```text
_NET = 1;
  PAYMENT_GATEWAY_PAYPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06543"></a>
## FND-06543: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_ADYEN = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_ADYEN = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3468.

```text
YPAL = 2;
  PAYMENT_GATEWAY_APPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_A
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06544"></a>
## FND-06544: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_FACEBOOK = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_FACEBOOK = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3497.

```text
PPLE = 3;
  PAYMENT_GATEWAY_LITLE = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PA
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06545"></a>
## FND-06545: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_GOOGLE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_GOOGLE = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3529.

```text
E = 4;
  PAYMENT_GATEWAY_STRIPE = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06546"></a>
## FND-06546: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_HUAWEI = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_HUAWEI = 9;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3559.

```text
E = 5;
  PAYMENT_GATEWAY_ADYEN = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL =
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06547"></a>
## FND-06547: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_CRYPTO = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_CRYPTO = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3589.

```text
 = 6;
  PAYMENT_GATEWAY_FACEBOOK = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06548"></a>
## FND-06548: chesscom.payments.v1.PaymentGateway.PAYMENT_GATEWAY_DLOCAL = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_GATEWAY_DLOCAL = 11;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3620.

```text
K = 7;
  PAYMENT_GATEWAY_GOOGLE = 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06549"></a>
## FND-06549: enum declaration: chesscom.payments.v1.PaymentMethod

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PaymentMethod {

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3652.

```text
= 8;
  PAYMENT_GATEWAY_HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CAR
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06550"></a>
## FND-06550: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_UNSPECIFIED = 0;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3675.

```text
HUAWEI = 9;
  PAYMENT_GATEWAY_CRYPTO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAY
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06551"></a>
## FND-06551: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_CREDIT_CARD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_CREDIT_CARD = 1;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3709.

```text
TO = 10;
  PAYMENT_GATEWAY_DLOCAL = 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06552"></a>
## FND-06552: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_GOOGLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_GOOGLE = 2;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3743.

```text
= 11;
}

enum PaymentMethod {
  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06553"></a>
## FND-06553: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_APPLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_APPLE = 3;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3772.

```text

  PAYMENT_METHOD_UNSPECIFIED = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 1
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06554"></a>
## FND-06554: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_PAYPAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_PAYPAL = 4;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3800.

```text
D = 0;
  PAYMENT_METHOD_CREDIT_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_P
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06555"></a>
## FND-06555: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_ADYEN = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_ADYEN = 5;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3829.

```text
T_CARD = 1;
  PAYMENT_METHOD_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06556"></a>
## FND-06556: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_IDEAL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_IDEAL = 6;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3857.

```text
_GOOGLE = 2;
  PAYMENT_METHOD_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_ME
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06557"></a>
## FND-06557: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_NO_PAYMENT_METHOD = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3885.

```text
D_APPLE = 3;
  PAYMENT_METHOD_PAYPAL = 4;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMEN
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06558"></a>
## FND-06558: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_SOFORT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_SOFORT = 8;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3925.

```text
;
  PAYMENT_METHOD_ADYEN = 5;
  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_MET
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06559"></a>
## FND-06559: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_CARRIER_BILLING = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_CARRIER_BILLING = 9;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3954.

```text

  PAYMENT_METHOD_IDEAL = 6;
  PAYMENT_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
 
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06560"></a>
## FND-06560: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_GIROPAY = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_GIROPAY = 10;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 3992.

```text
_METHOD_NO_PAYMENT_METHOD = 7;
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06561"></a>
## FND-06561: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4023.

```text
  PAYMENT_METHOD_SOFORT = 8;
  PAYMENT_METHOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  P
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06562"></a>
## FND-06562: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_WORLD_PAY = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_WORLD_PAY = 12;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4064.

```text
THOD_CARRIER_BILLING = 9;
  PAYMENT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06563"></a>
## FND-06563: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_HUAWEI_POINTS = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_HUAWEI_POINTS = 13;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4097.

```text
NT_METHOD_GIROPAY = 10;
  PAYMENT_METHOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06564"></a>
## FND-06564: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_FREE_WEEK = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_FREE_WEEK = 14;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4134.

```text
HOD_SEPA_DIRECT_DEBIT = 11;
  PAYMENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_MET
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06565"></a>
## FND-06565: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_FACEBOOK = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_FACEBOOK = 15;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4167.

```text
MENT_METHOD_WORLD_PAY = 12;
  PAYMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHO
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06566"></a>
## FND-06566: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_MONEY_ORDER = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_MONEY_ORDER = 16;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4199.

```text
YMENT_METHOD_HUAWEI_POINTS = 13;
  PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06567"></a>
## FND-06567: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_HUAWEI_POINT_CARD = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4234.

```text
PAYMENT_METHOD_FREE_WEEK = 14;
  PAYMENT_METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METH
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06568"></a>
## FND-06568: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_HUAWEI_WALLET = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_HUAWEI_WALLET = 18;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4275.

```text
METHOD_FACEBOOK = 15;
  PAYMENT_METHOD_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06569"></a>
## FND-06569: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_ALIPAY = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_ALIPAY = 19;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4312.

```text
D_MONEY_ORDER = 16;
  PAYMENT_METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06570"></a>
## FND-06570: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_DEBIT_CARD = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_DEBIT_CARD = 20;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4342.

```text
METHOD_HUAWEI_POINT_CARD = 17;
  PAYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06571"></a>
## FND-06571: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_WECHAT_PAY = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_WECHAT_PAY = 21;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4376.

```text
AYMENT_METHOD_HUAWEI_WALLET = 18;
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_A
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06572"></a>
## FND-06572: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_GIFT_CARD = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_GIFT_CARD = 22;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4410.

```text
  PAYMENT_METHOD_ALIPAY = 19;
  PAYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQ
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06573"></a>
## FND-06573: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_BALANCE = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_BALANCE = 23;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4443.

```text
AYMENT_METHOD_DEBIT_CARD = 20;
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
  PAYMENT_METHOD_BALANCE = 23;
  PAYMENT_METHOD_ANT_CREDIT_PAY = 24;
  PAYMENT_METHOD_IPAY88 = 25;
  PAYMENT_METHOD_M_PESA = 26;
  PAYMENT_METHOD_PAYMENT_NOT_AVAILABLE = 27;
  PAYMENT_METHOD_CRYPTO = 28;
  PAYMENT_METHOD_GOOGLEPAY = 29;
  PAYMENT_METHOD_APPLEPAY = 30;
  PAYMENT_METHOD_NEQUI = 31;
  PAYMENT_METHOD_PIX = 3
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06574"></a>
## FND-06574: chesscom.payments.v1.PaymentMethod.PAYMENT_METHOD_ANT_CREDIT_PAY = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_METHOD_ANT_CREDIT_PAY = 24;

### Evidence

- **SRC-0488** `research/proto/chesscom/payments/v1/enums.proto` — [preserved redacted evidence](../evidence/text/dfc0d5e446cb560cb3948ce590667b2f3001d412fa6b6a936d03bd36e52aaee0.proto)
  Character offset 4474.

```text
  PAYMENT_METHOD_WECHAT_PAY = 21;
  PAYMENT_METHOD_GIFT_CARD = 22;
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
  P
```

**Source references:** SRC-0488, SRC-1459  
**URL references:** None independently associated  
**Related findings:** FND-06449, FND-06450, FND-06451

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
