# data_models — findings 10301–10400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10575"></a>
## FND-10575: chesscom.user_properties.v1.PIIPropertyDefinition.PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 459.

```text
 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10576"></a>
## FND-10576: chesscom.user_properties.v1.PIIPropertyDefinition.PAYPAL_EMAILS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYPAL_EMAILS = 16;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 500.

```text
DE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  one
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10577"></a>
## FND-10577: chesscom.user_properties.v1.PIIPropertyDefinition.PHONE_NUMBER = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PHONE_NUMBER = 17;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 522.

```text
AILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  s
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10578"></a>
## FND-10578: chesscom.user_properties.v1.PIIPropertyDefinition.PREVIOUS_PHONE_NUMBERS = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREVIOUS_PHONE_NUMBERS = 18;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 543.

```text
COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10579"></a>
## FND-10579: chesscom.user_properties.v1.PIIPropertyDefinition.USCF_ID = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USCF_ID = 19;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 574.

```text
_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10580"></a>
## FND-10580: chesscom.user_properties.v1.PIIPropertyDefinition.FIDE_ID = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIDE_ID = 20;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 590.

```text
L = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10581"></a>
## FND-10581: message declaration: chesscom.user_properties.v1.PIIProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PIIProperty {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 607.

```text
EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10582"></a>
## FND-10582: oneof declaration: chesscom.user_properties.v1.PIIProperty._email

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _email {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 631.

```text
BER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezo
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10583"></a>
## FND-10583: chesscom.user_properties.v1.PIIProperty.email = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string email = 1;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 648.

```text
OUS_PHONE_NUMBERS = 18;
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string las
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10584"></a>
## FND-10584: oneof declaration: chesscom.user_properties.v1.PIIProperty._first_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_name {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 672.

```text
  USCF_ID = 19;
  FIDE_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  on
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10585"></a>
## FND-10585: chesscom.user_properties.v1.PIIProperty.first_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string first_name = 2;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 694.

```text
_ID = 20;
}

message PIIProperty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10586"></a>
## FND-10586: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_name {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 723.

```text
rty {
  oneof _email {
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10587"></a>
## FND-10587: chesscom.user_properties.v1.PIIProperty.last_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_name = 3;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 744.

```text
{
  string email = 1;
  }
  oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_cit
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10588"></a>
## FND-10588: oneof declaration: chesscom.user_properties.v1.PIIProperty._country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 772.

```text
oneof _first_name {
  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10589"></a>
## FND-10589: chesscom.user_properties.v1.PIIProperty.country = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string country = 4;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 791.

```text

  string first_name = 2;
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_r
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10590"></a>
## FND-10590: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_country {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 817.

```text
  }
  oneof _last_name {
  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_regi
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10591"></a>
## FND-10591: chesscom.user_properties.v1.PIIProperty.last_country = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_country = 5;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 841.

```text

  string last_name = 3;
  }
  oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _la
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10592"></a>
## FND-10592: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_ip_address

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_ip_address {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 872.

```text
oneof _country {
  string country = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_lat
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10593"></a>
## FND-10593: chesscom.user_properties.v1.PIIProperty.last_ip_address = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_ip_address = 6;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 899.

```text
ountry = 4;
  }
  oneof _last_country {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _la
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10594"></a>
## FND-10594: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_timezone

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_timezone {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 933.

```text
try {
  string last_country = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longi
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10595"></a>
## FND-10595: chesscom.user_properties.v1.PIIProperty.last_timezone = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_timezone = 7;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 958.

```text
ry = 5;
  }
  oneof _last_ip_address {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _p
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10596"></a>
## FND-10596: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_continent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_continent {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 990.

```text
ress {
  string last_ip_address = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string paymen
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10597"></a>
## FND-10597: chesscom.user_properties.v1.PIIProperty.last_continent = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_continent = 8;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1016.

```text
dress = 6;
  }
  oneof _last_timezone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneo
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10598"></a>
## FND-10598: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_city

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_city {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1049.

```text
zone {
  string last_timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_lev
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10599"></a>
## FND-10599: chesscom.user_properties.v1.PIIProperty.last_city = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_city = 9;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1070.

```text
timezone = 7;
  }
  oneof _last_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10600"></a>
## FND-10600: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_region

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_region {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1098.

```text
ast_continent {
  string last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10601"></a>
## FND-10601: chesscom.user_properties.v1.PIIProperty.last_region = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_region = 10;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1121.

```text
g last_continent = 8;
  }
  oneof _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10602"></a>
## FND-10602: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_latitude

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_latitude {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1152.

```text
of _last_city {
  string last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number 
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10603"></a>
## FND-10603: chesscom.user_properties.v1.PIIProperty.last_latitude = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double last_latitude = 11;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1177.

```text
last_city = 9;
  }
  oneof _last_region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_i
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10604"></a>
## FND-10604: oneof declaration: chesscom.user_properties.v1.PIIProperty._last_longitude

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_longitude {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1210.

```text
region {
  string last_region = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10605"></a>
## FND-10605: chesscom.user_properties.v1.PIIProperty.last_longitude = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double last_longitude = 12;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1236.

```text
ion = 10;
  }
  oneof _last_latitude {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 f
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10606"></a>
## FND-10606: oneof declaration: chesscom.user_properties.v1.PIIProperty._payment_country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _payment_country {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1270.

```text
de {
  double last_latitude = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10607"></a>
## FND-10607: chesscom.user_properties.v1.PIIProperty.payment_country = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string payment_country = 14;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1297.

```text
 = 11;
  }
  oneof _last_longitude {
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  re
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10608"></a>
## FND-10608: oneof declaration: chesscom.user_properties.v1.PIIProperty._payment_country_confidence_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _payment_country_confidence_level {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1332.

```text
{
  double last_longitude = 12;
  }
  oneof _payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
 
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10609"></a>
## FND-10609: chesscom.user_properties.v1.PIIProperty.payment_country_confidence_level = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string payment_country_confidence_level = 15;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1376.

```text
_payment_country {
  string payment_country = 14;
  }
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10610"></a>
## FND-10610: oneof declaration: chesscom.user_properties.v1.PIIProperty._phone_number

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _phone_number {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1428.

```text
}
  oneof _payment_country_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10611"></a>
## FND-10611: chesscom.user_properties.v1.PIIProperty.phone_number = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string phone_number = 17;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1452.

```text
ry_confidence_level {
  string payment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10612"></a>
## FND-10612: oneof declaration: chesscom.user_properties.v1.PIIProperty._uscf_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _uscf_id {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1484.

```text
ayment_country_confidence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10613"></a>
## FND-10613: chesscom.user_properties.v1.PIIProperty.uscf_id = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string uscf_id = 19;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1503.

```text
idence_level = 15;
  }
  oneof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10614"></a>
## FND-10614: oneof declaration: chesscom.user_properties.v1.PIIProperty._fide_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fide_id {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1530.

```text
eof _phone_number {
  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10615"></a>
## FND-10615: chesscom.user_properties.v1.PIIProperty.fide_id = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 fide_id = 20;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1549.

```text

  string phone_number = 17;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10616"></a>
## FND-10616: chesscom.user_properties.v1.PIIProperty.previous_emails = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string previous_emails = 13;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1575.

```text
7;
  }
  oneof _uscf_id {
  string uscf_id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10617"></a>
## FND-10617: chesscom.user_properties.v1.PIIProperty.paypal_emails = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string paypal_emails = 16;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1615.

```text
id = 19;
  }
  oneof _fide_id {
  int64 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10618"></a>
## FND-10618: chesscom.user_properties.v1.PIIProperty.previous_phone_numbers = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string previous_phone_numbers = 18;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 1653.

```text
4 fide_id = 20;
  }
  repeated string previous_emails = 13;
  repeated string paypal_emails = 16;
  repeated string previous_phone_numbers = 18;
}

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10619"></a>
## FND-10619: enum declaration: chesscom.user_properties.v1.PlayStatsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayStatsPropertyDefinition {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 124.

```text
_properties/v1/properties_play_stats.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PlayStatsPropertyDefinition {
  PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WI
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10620"></a>
## FND-10620: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 161.

```text
proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PlayStatsPropertyDefinition {
  PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEF
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10621"></a>
## FND-10621: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 211.

```text
perties.v1;

enum PlayStatsPropertyDefinition {
  PLAY_STATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP 
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10622"></a>
## FND-10622: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 268.

```text
ATS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10623"></a>
## FND-10623: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 326.

```text
ERTY_DEFINITION_AVG_MOVES_PER_GAME = 1;
  PLAY_STATS_PROPERTY_DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10624"></a>
## FND-10624: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 388.

```text
DEFINITION_AVG_OPPONENT_RATING = 2;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10625"></a>
## FND-10625: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 458.

```text
IGHEST_OPPONENT_RATING = 3;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10626"></a>
## FND-10626: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 538.

```text
ENT_WIN_GAME = 4;
  PLAY_STATS_PROPERTY_DEFINITION_HIGHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITIO
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10627"></a>
## FND-10627: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 591.

```text
GHEST_RATED_OPPONENT_WIN_GAME_TIMESTAMP = 5;
  PLAY_STATS_PROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINI
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10628"></a>
## FND-10628: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 650.

```text
ROPERTY_DEFINITION_LAST_GAME_DATE = 6;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10629"></a>
## FND-10629: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 711.

```text
DEFINITION_TOTAL_GAME_COUNT_ALL = 7;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10630"></a>
## FND-10630: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 774.

```text
NITION_TOTAL_GAME_COUNT_RATED = 8;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rati
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10631"></a>
## FND-10631: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 829.

```text
Y_DEFINITION_TOTAL_GAME_COUNT_UNRATED = 9;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10632"></a>
## FND-10632: chesscom.user_properties.v1.PlayStatsPropertyDefinition.PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 885.

```text
PROPERTY_DEFINITION_TOTAL_WIN_COUNT = 10;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10633"></a>
## FND-10633: message declaration: chesscom.user_properties.v1.PlayStatsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayStatsProperty {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 942.

```text
OPERTY_DEFINITION_TOTAL_DRAW_COUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_g
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10634"></a>
## FND-10634: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._avg_moves_per_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avg_moves_per_game {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 972.

```text
OUNT = 11;
  PLAY_STATS_PROPERTY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10635"></a>
## FND-10635: chesscom.user_properties.v1.PlayStatsProperty.avg_moves_per_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double avg_moves_per_game = 1;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1002.

```text
TY_DEFINITION_TOTAL_LOSS_COUNT = 12;
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timest
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10636"></a>
## FND-10636: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._avg_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avg_opponent_rating {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1039.

```text
}

message PlayStatsProperty {
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp hi
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10637"></a>
## FND-10637: chesscom.user_properties.v1.PlayStatsProperty.avg_opponent_rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double avg_opponent_rating = 2;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1070.

```text
  oneof _avg_moves_per_game {
  double avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_t
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10638"></a>
## FND-10638: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._highest_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_opponent_rating {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1108.

```text
 avg_moves_per_game = 1;
  }
  oneof _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_d
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10639"></a>
## FND-10639: chesscom.user_properties.v1.PlayStatsProperty.highest_opponent_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 highest_opponent_rating = 3;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1143.

```text
f _avg_opponent_rating {
  double avg_opponent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10640"></a>
## FND-10640: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._highest_rated_opponent_win_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rated_opponent_win_game {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1184.

```text
onent_rating = 2;
  }
  oneof _highest_opponent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_ga
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10641"></a>
## FND-10641: chesscom.user_properties.v1.PlayStatsProperty.highest_rated_opponent_win_game = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string highest_rated_opponent_win_game = 4;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1227.

```text
nent_rating {
  int32 highest_opponent_rating = 3;
  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10642"></a>
## FND-10642: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._highest_rated_opponent_win_game_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highest_rated_opponent_win_game_timestamp {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1277.

```text

  }
  oneof _highest_rated_opponent_win_game {
  string highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int3
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10643"></a>
## FND-10643: chesscom.user_properties.v1.PlayStatsProperty.highest_rated_opponent_win_game_timestamp = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1330.

```text
ing highest_rated_opponent_win_game = 4;
  }
  oneof _highest_rated_opponent_win_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10644"></a>
## FND-10644: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._last_game_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_game_date {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1410.

```text
_game_timestamp {
  .google.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_co
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10645"></a>
## FND-10645: chesscom.user_properties.v1.PlayStatsProperty.last_game_date = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_game_date = 6;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1436.

```text
e.protobuf.Timestamp highest_rated_opponent_win_game_timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_co
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10646"></a>
## FND-10646: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_game_count_all

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_game_count_all {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1489.

```text
timestamp = 5;
  }
  oneof _last_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 tot
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10647"></a>
## FND-10647: chesscom.user_properties.v1.PlayStatsProperty.total_game_count_all = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_game_count_all = 7;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1521.

```text
_game_date {
  .google.protobuf.Timestamp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof 
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10648"></a>
## FND-10648: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_game_count_rated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_game_count_rated {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1559.

```text
amp last_game_date = 6;
  }
  oneof _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss
```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10649"></a>
## FND-10649: chesscom.user_properties.v1.PlayStatsProperty.total_game_count_rated = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_game_count_rated = 8;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1593.

```text
f _total_game_count_all {
  int32 total_game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10650"></a>
## FND-10650: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_game_count_unrated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_game_count_unrated {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1633.

```text
game_count_all = 7;
  }
  oneof _total_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10651"></a>
## FND-10651: chesscom.user_properties.v1.PlayStatsProperty.total_game_count_unrated = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_game_count_unrated = 9;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1669.

```text
al_game_count_rated {
  int32 total_game_count_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10652"></a>
## FND-10652: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_win_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_win_count {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1711.

```text
ount_rated = 8;
  }
  oneof _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10653"></a>
## FND-10653: chesscom.user_properties.v1.PlayStatsProperty.total_win_count = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_win_count = 10;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1738.

```text
 _total_game_count_unrated {
  int32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10654"></a>
## FND-10654: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_draw_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_draw_count {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1772.

```text
32 total_game_count_unrated = 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10655"></a>
## FND-10655: chesscom.user_properties.v1.PlayStatsProperty.total_draw_count = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_draw_count = 11;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1800.

```text
= 9;
  }
  oneof _total_win_count {
  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10656"></a>
## FND-10656: oneof declaration: chesscom.user_properties.v1.PlayStatsProperty._total_loss_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_loss_count {

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1835.

```text

  int32 total_win_count = 10;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10657"></a>
## FND-10657: chesscom.user_properties.v1.PlayStatsProperty.total_loss_count = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_loss_count = 12;

### Evidence

- **SRC-0619** `research/proto/chesscom/user_properties/v1/properties_play_stats.proto` — [preserved redacted evidence](../evidence/text/d26cda1e66259603b16dff5fda97c25b1be04cacf794ee465caf7c39049159ef.proto)
  Character offset 1863.

```text
0;
  }
  oneof _total_draw_count {
  int32 total_draw_count = 11;
  }
  oneof _total_loss_count {
  int32 total_loss_count = 12;
  }
}

```

**Source references:** SRC-0619, SRC-1590  
**URL references:** None independently associated  
**Related findings:** FND-10619, FND-10620, FND-10621

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10658"></a>
## FND-10658: enum declaration: chesscom.user_properties.v1.PredictivePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PredictivePropertyDefinition {

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 124.

```text
_properties/v1/properties_predictive.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PredictivePropertyDefinition {
  PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;
  PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSI
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10659"></a>
## FND-10659: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 162.

```text
roto
// syntax: proto3

package chesscom.user_properties.v1;

enum PredictivePropertyDefinition {
  PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;
  PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITI
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10660"></a>
## FND-10660: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 212.

```text
erties.v1;

enum PredictivePropertyDefinition {
  PREDICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;
  PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINI
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10661"></a>
## FND-10661: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 265.

```text
DICTIVE_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;
  PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFIN
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10662"></a>
## FND-10662: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 321.

```text
E_PROPERTY_DEFINITION_CHURN_RISK_30D = 1;
  PREDICTIVE_PROPERTY_DEFINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10663"></a>
## FND-10663: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 387.

```text
FINITION_SCORES_UPDATED_AT = 2;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10664"></a>
## FND-10664: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 454.

```text
URN_RISK_30D_GENERATED_AT = 3;
  PREDICTIVE_PROPERTY_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 1
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10665"></a>
## FND-10665: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 506.

```text
_DEFINITION_CHURN_RISK_30D_MODEL_VERSION = 4;
  PREDICTIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10666"></a>
## FND-10666: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 560.

```text
TIVE_PROPERTY_DEFINITION_ACTIVATION_7D = 5;
  PREDICTIVE_PROPERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTI
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10667"></a>
## FND-10667: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 621.

```text
ERTY_DEFINITION_PUZZLE_SLUMP_7D = 6;
  PREDICTIVE_PROPERTY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNU
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10668"></a>
## FND-10668: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 677.

```text
TY_DEFINITION_LESSONS_PROGRESSION_7D = 7;
  PREDICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_N
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10669"></a>
## FND-10669: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 725.

```text
ICTIVE_PROPERTY_DEFINITION_REVIEW_UPSELL_30D = 8;
  PREDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CU
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10670"></a>
## FND-10670: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 779.

```text
EDICTIVE_PROPERTY_DEFINITION_RETURN_7D = 9;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_A
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10671"></a>
## FND-10671: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 839.

```text
PERTY_DEFINITION_TRIAL_START_7D = 10;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVAT
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10672"></a>
## FND-10672: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 906.

```text
ION_TRIAL_CONVERSION_30D = 11;
  PREDICTIVE_PROPERTY_DEFINITION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCOR
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10673"></a>
## FND-10673: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 965.

```text
TION_SUBSCRIPTION_CONVERSION_30D = 12;
  PREDICTIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10674"></a>
## FND-10674: chesscom.user_properties.v1.PredictivePropertyDefinition.PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;

### Evidence

- **SRC-0620** `research/proto/chesscom/user_properties/v1/properties_predictive.proto` — [preserved redacted evidence](../evidence/text/a9aa99ee077d773dbb4856396c8997448c31ce75d85ceeabfc617f88b13328a2.proto)
  Character offset 1012.

```text
TIVE_PROPERTY_DEFINITION_ANNUAL_RENEWAL_365D = 13;
  PREDICTIVE_PROPERTY_DEFINITION_NURR_7D = 14;
  PREDICTIVE_PROPERTY_DEFINITION_CURR_14D = 15;
  PREDICTIVE_PROPERTY_DEFINITION_LESSON_ADOPTION_30D = 16;
  PREDICTIVE_PROPERTY_DEFINITION_REACTIVATION_7D = 17;
  PREDICTIVE_PROPERTY_DEFINITION_TRIAL_PROPENSITY_SCORE = 18;
}

message PredictiveProperty {
  oneof _churn_risk_30d {
  double churn_risk_30d = 1;
  }
  oneof
```

**Source references:** SRC-0620, SRC-1591  
**URL references:** None independently associated  
**Related findings:** FND-10658, FND-10659, FND-10660

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
