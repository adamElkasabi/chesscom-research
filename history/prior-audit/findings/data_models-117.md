# data_models — findings 11601–11700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11875"></a>
## FND-11875: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_bounce_date_sendgrid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_bounce_date_sendgrid {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 751.

```text
AINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11876"></a>
## FND-11876: chesscom.user_properties.v1.UserEngagementProperty.last_bounce_date_sendgrid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_bounce_date_sendgrid = 1;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 788.

```text
L_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11877"></a>
## FND-11877: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_open_email_date_sendgrid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_open_email_date_sendgrid {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 852.

```text
neof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11878"></a>
## FND-11878: chesscom.user_properties.v1.UserEngagementProperty.last_open_email_date_sendgrid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_open_email_date_sendgrid = 2;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 893.

```text
le.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11879"></a>
## FND-11879: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_click_email_date_sendgrid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_click_email_date_sendgrid {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 961.

```text
st_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11880"></a>
## FND-11880: chesscom.user_properties.v1.UserEngagementProperty.last_click_email_date_sendgrid = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_click_email_date_sendgrid = 3;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1003.

```text
otobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11881"></a>
## FND-11881: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_bounce_date_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_bounce_date_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1072.

```text
_click_email_date_sendgrid {
  .google.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
 
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11882"></a>
## FND-11882: chesscom.user_properties.v1.UserEngagementProperty.last_bounce_date_iterable = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_bounce_date_iterable = 4;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1109.

```text
e.protobuf.Timestamp last_click_email_date_sendgrid = 3;
  }
  oneof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendg
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11883"></a>
## FND-11883: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_open_email_date_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_open_email_date_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1173.

```text
neof _last_bounce_date_iterable {
  .google.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendg
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11884"></a>
## FND-11884: chesscom.user_properties.v1.UserEngagementProperty.last_open_email_date_iterable = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_open_email_date_iterable = 5;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1214.

```text
le.protobuf.Timestamp last_bounce_date_iterable = 4;
  }
  oneof _last_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_da
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11885"></a>
## FND-11885: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_click_email_date_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_click_email_date_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1282.

```text
st_open_email_date_iterable {
  .google.protobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sen
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11886"></a>
## FND-11886: chesscom.user_properties.v1.UserEngagementProperty.last_click_email_date_iterable = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_click_email_date_iterable = 6;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1324.

```text
otobuf.Timestamp last_open_email_date_iterable = 5;
  }
  oneof _last_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_n
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11887"></a>
## FND-11887: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_dropped_email_date_sendgrid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_dropped_email_date_sendgrid {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1393.

```text
_click_email_date_iterable {
  .google.protobuf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11888"></a>
## FND-11888: chesscom.user_properties.v1.UserEngagementProperty.last_dropped_email_date_sendgrid = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1437.

```text
buf.Timestamp last_click_email_date_iterable = 6;
  }
  oneof _last_dropped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  o
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11889"></a>
## FND-11889: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_spam_report_date_sendgrid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_spam_report_date_sendgrid {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1508.

```text
pped_email_date_sendgrid {
  .google.protobuf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11890"></a>
## FND-11890: chesscom.user_properties.v1.UserEngagementProperty.last_spam_report_date_sendgrid = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1550.

```text
buf.Timestamp last_dropped_email_date_sendgrid = 7;
  }
  oneof _last_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneo
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11891"></a>
## FND-11891: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_opened_push_notification_date_firebase

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_opened_push_notification_date_firebase {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1619.

```text
_spam_report_date_sendgrid {
  .google.protobuf.Timestamp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_p
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11892"></a>
## FND-11892: chesscom.user_properties.v1.UserEngagementProperty.last_opened_push_notification_date_firebase = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1674.

```text
mp last_spam_report_date_sendgrid = 8;
  }
  oneof _last_opened_push_notification_date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_co
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11893"></a>
## FND-11893: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_viewed_payment_page_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_viewed_payment_page_date {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1756.

```text
date_firebase {
  .google.protobuf.Timestamp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_ite
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11894"></a>
## FND-11894: chesscom.user_properties.v1.UserEngagementProperty.last_viewed_payment_page_date = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_viewed_payment_page_date = 10;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1797.

```text
amp last_opened_push_notification_date_firebase = 9;
  }
  oneof _last_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_boun
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11895"></a>
## FND-11895: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_push_open_date_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_push_open_date_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1866.

```text
t_viewed_payment_page_date {
  .google.protobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11896"></a>
## FND-11896: chesscom.user_properties.v1.UserEngagementProperty.last_push_open_date_iterable = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_push_open_date_iterable = 11;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1906.

```text
rotobuf.Timestamp last_viewed_payment_page_date = 10;
  }
  oneof _last_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11897"></a>
## FND-11897: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._last_email_complaint_date_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_email_complaint_date_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 1974.

```text
ast_push_open_date_iterable {
  .google.protobuf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11898"></a>
## FND-11898: chesscom.user_properties.v1.UserEngagementProperty.last_email_complaint_date_iterable = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_email_complaint_date_iterable = 12;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 2020.

```text
uf.Timestamp last_push_open_date_iterable = 11;
  }
  oneof _last_email_complaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11899"></a>
## FND-11899: oneof declaration: chesscom.user_properties.v1.UserEngagementProperty._total_email_bounces_iterable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_email_bounces_iterable {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 2094.

```text
mplaint_date_iterable {
  .google.protobuf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11900"></a>
## FND-11900: chesscom.user_properties.v1.UserEngagementProperty.total_email_bounces_iterable = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double total_email_bounces_iterable = 13;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 2134.

```text
uf.Timestamp last_email_complaint_date_iterable = 12;
  }
  oneof _total_email_bounces_iterable {
  double total_email_bounces_iterable = 13;
  }
}

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11901"></a>
## FND-11901: enum declaration: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserPuzzleStatsPropertyDefinition {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 131.

```text
ties/v1/properties_user_puzzle_stats.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserPuzzleStatsPropertyDefinition {
  USER_PUZZLE_STATS_UNSPECIFIED = 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 poi
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11902"></a>
## FND-11902: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_UNSPECIFIED = 0;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 174.

```text
// syntax: proto3

package chesscom.user_properties.v1;

enum UserPuzzleStatsPropertyDefinition {
  USER_PUZZLE_STATS_UNSPECIFIED = 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11903"></a>
## FND-11903: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_POINTS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_POINTS = 1;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 211.

```text
ser_properties.v1;

enum UserPuzzleStatsPropertyDefinition {
  USER_PUZZLE_STATS_UNSPECIFIED = 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tie
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11904"></a>
## FND-11904: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_LEVEL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_LEVEL = 2;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 243.

```text
zleStatsPropertyDefinition {
  USER_PUZZLE_STATS_UNSPECIFIED = 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
 
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11905"></a>
## FND-11905: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_TIER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_TIER = 3;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 274.

```text
USER_PUZZLE_STATS_UNSPECIFIED = 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneo
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11906"></a>
## FND-11906: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_PRESTIGE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_PRESTIGE = 4;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 304.

```text
= 0;
  USER_PUZZLE_STATS_POINTS = 1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
 
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11907"></a>
## FND-11907: chesscom.user_properties.v1.UserPuzzleStatsPropertyDefinition.USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 338.

```text
1;
  USER_PUZZLE_STATS_LEVEL = 2;
  USER_PUZZLE_STATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5
```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11908"></a>
## FND-11908: message declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserPuzzleStatsProperty {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 388.

```text
ATS_TIER = 3;
  USER_PUZZLE_STATS_PRESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11909"></a>
## FND-11909: oneof declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty._points

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _points {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 424.

```text
ESTIGE = 4;
  USER_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11910"></a>
## FND-11910: chesscom.user_properties.v1.UserPuzzleStatsProperty.points = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 points = 1;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 442.

```text
_PUZZLE_STATS_TOTAL_TACTICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11911"></a>
## FND-11911: oneof declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty._level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _level {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 466.

```text
ICS_COMPLETED = 5;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11912"></a>
## FND-11912: chesscom.user_properties.v1.UserPuzzleStatsProperty.level = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 level = 2;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 483.

```text
;
}

message UserPuzzleStatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11913"></a>
## FND-11913: oneof declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty._tier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tier {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 506.

```text
StatsProperty {
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11914"></a>
## FND-11914: chesscom.user_properties.v1.UserPuzzleStatsProperty.tier = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 tier = 3;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 522.

```text
  oneof _points {
  int32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11915"></a>
## FND-11915: oneof declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty._prestige

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _prestige {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 544.

```text
t32 points = 1;
  }
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11916"></a>
## FND-11916: chesscom.user_properties.v1.UserPuzzleStatsProperty.prestige = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 prestige = 4;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 564.

```text
  oneof _level {
  int32 level = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11917"></a>
## FND-11917: oneof declaration: chesscom.user_properties.v1.UserPuzzleStatsProperty._total_tactics_completed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_tactics_completed {

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 590.

```text
evel = 2;
  }
  oneof _tier {
  int32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11918"></a>
## FND-11918: chesscom.user_properties.v1.UserPuzzleStatsProperty.total_tactics_completed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_tactics_completed = 5;

### Evidence

- **SRC-0642** `research/proto/chesscom/user_properties/v1/properties_user_puzzle_stats.proto` — [preserved redacted evidence](../evidence/text/5e84593a76e26ebb7d7df56b0f588d6d2ba2bd53a8710bb28affebfa1804cb04.proto)
  Character offset 625.

```text
32 tier = 3;
  }
  oneof _prestige {
  int32 prestige = 4;
  }
  oneof _total_tactics_completed {
  int32 total_tactics_completed = 5;
  }
}

```

**Source references:** SRC-0642, SRC-1613  
**URL references:** None independently associated  
**Related findings:** FND-11901, FND-11902, FND-11903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11919"></a>
## FND-11919: enum declaration: chesscom.user_properties.v1.UserSettingsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserSettingsPropertyDefinition {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 127.

```text
operties/v1/properties_user_settings.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserSettingsPropertyDefinition {
  USER_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  NOTIFICATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICAT
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11920"></a>
## FND-11920: chesscom.user_properties.v1.UserSettingsPropertyDefinition.USER_SETTINGS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_SETTINGS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 167.

```text
to
// syntax: proto3

package chesscom.user_properties.v1;

enum UserSettingsPropertyDefinition {
  USER_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  NOTIFICATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11921"></a>
## FND-11921: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_CHESS_TV = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_CHESS_TV = 1;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 209.

```text
r_properties.v1;

enum UserSettingsPropertyDefinition {
  USER_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  NOTIFICATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11922"></a>
## FND-11922: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_CHESS_TV = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_CHESS_TV = 2;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 245.

```text
ropertyDefinition {
  USER_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  NOTIFICATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11923"></a>
## FND-11923: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_CHALLENGE_MIN_RATING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_CHALLENGE_MIN_RATING = 3;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 278.

```text
GS_PROPERTY_UNSPECIFIED = 0;
  NOTIFICATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PR
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11924"></a>
## FND-11924: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_GAME_EVENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_GAME_EVENT = 4;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 315.

```text
CATION_MOBILE_CHESS_TV = 1;
  NOTIFICATION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11925"></a>
## FND-11925: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 353.

```text
TION_WEB_CHESS_TV = 2;
  GAMEPLAY_CHALLENGE_MIN_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 1
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11926"></a>
## FND-11926: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_NEW_CONTENT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_NEW_CONTENT = 6;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 399.

```text
N_RATING = 3;
  NOTIFICATION_MOBILE_GAME_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11927"></a>
## FND-11927: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 438.

```text
E_EVENT = 4;
  GAMEPLAY_LIVE_ALLOW_OFFLINE_CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOU
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11928"></a>
## FND-11928: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 481.

```text
CHALLENGES = 5;
  NOTIFICATION_MOBILE_NEW_CONTENT = 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AN
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11929"></a>
## FND-11929: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_CHALLENGE_MAX_RATING = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_CHALLENGE_MAX_RATING = 9;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 531.

```text
= 6;
  NOTIFICATION_MOBILE_MY_TURN_TO_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11930"></a>
## FND-11930: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 568.

```text
_MOVE = 7;
  NOTIFICATION_MOBILE_NEWS_AND_ANNOUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11931"></a>
## FND-11931: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_PLAY_SOUNDS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_PLAY_SOUNDS = 11;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 613.

```text
OUNCEMENTS = 8;
  GAMEPLAY_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMM
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11932"></a>
## FND-11932: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_NEW_CONTENT = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_NEW_CONTENT = 12;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 639.

```text
_CHALLENGE_MAX_RATING = 9;
  NOTIFICATION_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11933"></a>
## FND-11933: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 678.

```text
ON_WEB_LESSON_AND_PRACTICE = 10;
  BOARD_PLAY_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPL
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11934"></a>
## FND-11934: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_MOVE_METHOD = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_MOVE_METHOD = 14;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 723.

```text
_SOUNDS = 11;
  NOTIFICATION_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_M
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11935"></a>
## FND-11935: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_SOUND_THEME = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_SOUND_THEME = 15;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 749.

```text
ON_EMAIL_NEW_CONTENT = 12;
  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICA
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11936"></a>
## FND-11936: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 775.

```text

  NOTIFICATION_EMAIL_NEW_SOCIAL_TROPHY = 13;
  BOARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11937"></a>
## FND-11937: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 825.

```text
ARD_MOVE_METHOD = 14;
  BOARD_SOUND_THEME = 15;
  NOTIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SH
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11938"></a>
## FND-11938: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_MOVE_LIST_STYLE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_MOVE_LIST_STYLE = 18;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 877.

```text
TIFICATION_EMAIL_NEWS_AND_ANNOUNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11939"></a>
## FND-11939: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 907.

```text
UNCEMENTS = 16;
  NOTIFICATION_MOBILE_FRIEND_ACTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11940"></a>
## FND-11940: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_NEW_COMMENT = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_NEW_COMMENT = 20;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 953.

```text
CTIVITY_UPDATES = 17;
  BOARD_MOVE_LIST_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11941"></a>
## FND-11941: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_DAILY_CONFIRM_MOVE = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_DAILY_CONFIRM_MOVE = 21;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 992.

```text
_STYLE = 18;
  NOTIFICATION_MOBILE_RECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_L
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11942"></a>
## FND-11942: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_SEEK_MIN_RATING = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_SEEK_MIN_RATING = 22;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1028.

```text
ECOMMENDED_MATCH = 19;
  NOTIFICATION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11943"></a>
## FND-11943: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_NEW_USER_COMMENT = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_NEW_USER_COMMENT = 23;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1061.

```text
TION_EMAIL_NEW_COMMENT = 20;
  GAMEPLAY_DAILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  G
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11944"></a>
## FND-11944: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_SHOW_LEGAL_MOVES = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_SHOW_LEGAL_MOVES = 24;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1103.

```text
ILY_CONFIRM_MOVE = 21;
  GAMEPLAY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NO
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11945"></a>
## FND-11945: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_SHOW_TIMESTAMPS = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_SHOW_TIMESTAMPS = 25;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1134.

```text
AY_SEEK_MIN_RATING = 22;
  NOTIFICATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT =
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11946"></a>
## FND-11946: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_GAME_EVENT = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_GAME_EVENT = 26;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1167.

```text
CATION_WEB_NEW_USER_COMMENT = 23;
  BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PE
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11947"></a>
## FND-11947: chesscom.user_properties.v1.UserSettingsPropertyDefinition.PRIVACY_FRIENDS_LIST_PRIVACY = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRIVACY_FRIENDS_LIST_PRIVACY = 27;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1203.

```text
BOARD_SHOW_LEGAL_MOVES = 24;
  GAMEPLAY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11948"></a>
## FND-11948: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_VOTE_CHESS = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_VOTE_CHESS = 28;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1240.

```text
AY_SHOW_TIMESTAMPS = 25;
  NOTIFICATION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11949"></a>
## FND-11949: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_COORDINATES = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_COORDINATES = 29;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1276.

```text
ION_WEB_GAME_EVENT = 26;
  PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMA
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11950"></a>
## FND-11950: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1302.

```text
 PRIVACY_FRIENDS_LIST_PRIVACY = 27;
  NOTIFICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NO
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11951"></a>
## FND-11951: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_CHESS_TV = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_CHESS_TV = 31;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1344.

```text
FICATION_WEB_VOTE_CHESS = 28;
  BOARD_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11952"></a>
## FND-11952: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1380.

```text
D_COORDINATES = 29;
  GAMEPLAY_LIVE_PLAY_MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11953"></a>
## FND-11953: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_NEW_COMMENT = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_NEW_COMMENT = 33;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1421.

```text
MULTIPLE_GAMES = 30;
  NOTIFICATION_EMAIL_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11954"></a>
## FND-11954: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1461.

```text
L_CHESS_TV = 31;
  GAMEPLAY_LIVE_AUTO_PROMOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  P
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11955"></a>
## FND-11955: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_CONFIRM_RESIGN = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_CONFIRM_RESIGN = 35;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1502.

```text
MOTE_QUEEN = 32;
  NOTIFICATION_MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICAT
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11956"></a>
## FND-11956: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1534.

```text
MOBILE_NEW_COMMENT = 33;
  GAMEPLAY_DAILY_MAX_DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIV
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11957"></a>
## FND-11957: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_LESSON_QUOTA = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_LESSON_QUOTA = 37;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1580.

```text
DAYS_PER_MOVE = 34;
  GAMEPLAY_CONFIRM_RESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11958"></a>
## FND-11958: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1620.

```text
ESIGN = 35;
  GAMEPLAY_LIVE_SEEK_BASE_TIME_VARIANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11959"></a>
## FND-11959: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1667.

```text
ANTS = 36;
  NOTIFICATION_EMAIL_LESSON_QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MES
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11960"></a>
## FND-11960: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_WHITE_ALWAYS_ON_BOTTOM = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1706.

```text
QUOTA = 37;
  NOTIFICATION_EMAIL_LESSON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11961"></a>
## FND-11961: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_NEW_COMMENT = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_NEW_COMMENT = 41;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1743.

```text
ON_AND_PRACTICE = 38;
  GAMEPLAY_LIVE_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EM
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11962"></a>
## FND-11962: chesscom.user_properties.v1.UserSettingsPropertyDefinition.PRIVACY_INSIGHTS_PRIVACY = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRIVACY_INSIGHTS_PRIVACY = 42;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1780.

```text
_CHALLENGE_ALERTS = 39;
  BOARD_WHITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIV
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11963"></a>
## FND-11963: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_NEW_CONTENT = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_NEW_CONTENT = 43;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1813.

```text
HITE_ALWAYS_ON_BOTTOM = 40;
  NOTIFICATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICA
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11964"></a>
## FND-11964: chesscom.user_properties.v1.UserSettingsPropertyDefinition.PRIVACY_ALLOW_FRIEND_REQUESTS = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PRIVACY_ALLOW_FRIEND_REQUESTS = 44;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1850.

```text
ATION_WEB_NEW_COMMENT = 41;
  PRIVACY_INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11965"></a>
## FND-11965: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_LESSON_QUOTA = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_LESSON_QUOTA = 45;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1888.

```text
INSIGHTS_PRIVACY = 42;
  NOTIFICATION_WEB_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_H
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11966"></a>
## FND-11966: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_PREMOVES = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_PREMOVES = 46;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1929.

```text
_NEW_CONTENT = 43;
  PRIVACY_ALLOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11967"></a>
## FND-11967: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_NEW_MESSAGE = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_NEW_MESSAGE = 47;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 1960.

```text
LOW_FRIEND_REQUESTS = 44;
  NOTIFICATION_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSI
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11968"></a>
## FND-11968: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2000.

```text
_MOBILE_LESSON_QUOTA = 45;
  GAMEPLAY_LIVE_PREMOVES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS =
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11969"></a>
## FND-11969: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_EMAIL_HERO_PLAYING = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_EMAIL_HERO_PLAYING = 49;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2048.

```text
VES = 46;
  NOTIFICATION_MOBILE_NEW_MESSAGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11970"></a>
## FND-11970: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_LIVE_EVALUATION_BAR = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_LIVE_EVALUATION_BAR = 50;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2088.

```text
AGE = 47;
  NOTIFICATION_WEB_NEWS_AND_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_CHALLENGES_FROM = 57;
  GAMEPLAY_PLAY_ST
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11971"></a>
## FND-11971: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_MOBILE_VOTE_CHESS = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_MOBILE_VOTE_CHESS = 51;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2125.

```text
_ANNOUNCEMENTS = 48;
  NOTIFICATION_EMAIL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_CHALLENGES_FROM = 57;
  GAMEPLAY_PLAY_STREAKS = 58;
  PRIVACY_ALLOW_GLOBAL_CH
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11972"></a>
## FND-11972: chesscom.user_properties.v1.UserSettingsPropertyDefinition.NOTIFICATION_WEB_NEW_MESSAGE = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOTIFICATION_WEB_NEW_MESSAGE = 52;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2164.

```text
IL_HERO_PLAYING = 49;
  GAMEPLAY_LIVE_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_CHALLENGES_FROM = 57;
  GAMEPLAY_PLAY_STREAKS = 58;
  PRIVACY_ALLOW_GLOBAL_CHAT_REQUESTS_FROM = 59;
  PUZZLES_SHOW_D
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11973"></a>
## FND-11973: chesscom.user_properties.v1.UserSettingsPropertyDefinition.BOARD_HIGHLIGHT_MOVES = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOARD_HIGHLIGHT_MOVES = 53;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2201.

```text
_EVALUATION_BAR = 50;
  NOTIFICATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_CHALLENGES_FROM = 57;
  GAMEPLAY_PLAY_STREAKS = 58;
  PRIVACY_ALLOW_GLOBAL_CHAT_REQUESTS_FROM = 59;
  PUZZLES_SHOW_DETAILS = 60;
  NOTIFICATION_WEB_NEW_S
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11974"></a>
## FND-11974: chesscom.user_properties.v1.UserSettingsPropertyDefinition.GAMEPLAY_SEEK_MAX_RATING = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAMEPLAY_SEEK_MAX_RATING = 54;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 2231.

```text
CATION_MOBILE_VOTE_CHESS = 51;
  NOTIFICATION_WEB_NEW_MESSAGE = 52;
  BOARD_HIGHLIGHT_MOVES = 53;
  GAMEPLAY_SEEK_MAX_RATING = 54;
  GAMEPLAY_ANALYSIS_EVALUATION_BAR_MODE_WDL_FOR_OPENINGS = 55;
  BOARD_BOARD_STYLE = 56;
  GAMEPLAY_ALLOW_CHALLENGES_FROM = 57;
  GAMEPLAY_PLAY_STREAKS = 58;
  PRIVACY_ALLOW_GLOBAL_CHAT_REQUESTS_FROM = 59;
  PUZZLES_SHOW_DETAILS = 60;
  NOTIFICATION_WEB_NEW_SOCIAL_TROPHY = 61;
  PRIVACY_B
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
