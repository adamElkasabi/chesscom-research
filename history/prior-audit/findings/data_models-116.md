# data_models — findings 11501–11600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11775"></a>
## FND-11775: chesscom.user_properties.v1.UserDetailsProperty.is_content_hidden = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_content_hidden = 10;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2093.

```text
}
  oneof _referred_by_method {
  string referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_ope
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11776"></a>
## FND-11776: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_verified

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_verified {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2128.

```text
tring referred_by_method = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _las
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11777"></a>
## FND-11777: chesscom.user_properties.v1.UserDetailsProperty.is_verified = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_verified = 11;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2151.

```text
d = 9;
  }
  oneof _is_content_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11778"></a>
## FND-11778: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_sendgrid_invalid_email

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_sendgrid_invalid_email {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2180.

```text
t_hidden {
  bool is_content_hidden = 10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11779"></a>
## FND-11779: chesscom.user_properties.v1.UserDetailsProperty.has_sendgrid_invalid_email = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_sendgrid_invalid_email = 12;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2218.

```text
10;
  }
  oneof _is_verified {
  bool is_verified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  on
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11780"></a>
## FND-11780: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._last_bounce_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_bounce_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2262.

```text
ified = 11;
  }
  oneof _has_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.proto
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11781"></a>
## FND-11781: chesscom.user_properties.v1.UserDetailsProperty.last_bounce_date = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_bounce_date = 13;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2290.

```text
_sendgrid_invalid_email {
  bool has_sendgrid_invalid_email = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_repo
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11782"></a>
## FND-11782: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._last_open_email_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_open_email_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2346.

```text
ail = 12;
  }
  oneof _last_bounce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_p
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11783"></a>
## FND-11783: chesscom.user_properties.v1.UserDetailsProperty.last_open_email_date = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_open_email_date = 14;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2378.

```text
ce_date {
  .google.protobuf.Timestamp last_bounce_date = 13;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _i
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11784"></a>
## FND-11784: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._last_dropped_email_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_dropped_email_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2438.

```text
;
  }
  oneof _last_open_email_date {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _ski
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11785"></a>
## FND-11785: chesscom.user_properties.v1.UserDetailsProperty.last_dropped_email_date = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_dropped_email_date = 15;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2473.

```text
 {
  .google.protobuf.Timestamp last_open_email_date = 14;
  }
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 1
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11786"></a>
## FND-11786: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._last_spam_report_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_spam_report_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2536.

```text
  oneof _last_dropped_email_date {
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Time
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11787"></a>
## FND-11787: chesscom.user_properties.v1.UserDetailsProperty.last_spam_report_date = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_spam_report_date = 16;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2569.

```text
{
  .google.protobuf.Timestamp last_dropped_email_date = 15;
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11788"></a>
## FND-11788: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_pawniversary

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_pawniversary {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2630.

```text
  }
  oneof _last_spam_report_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_e
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11789"></a>
## FND-11789: chesscom.user_properties.v1.UserDetailsProperty.is_pawniversary = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_pawniversary = 17;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2657.

```text
rt_date {
  .google.protobuf.Timestamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11790"></a>
## FND-11790: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_reactivated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_reactivated {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2690.

```text
stamp last_spam_report_date = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bo
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11791"></a>
## FND-11791: chesscom.user_properties.v1.UserDetailsProperty.is_reactivated = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_reactivated = 18;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2716.

```text
e = 16;
  }
  oneof _is_pawniversary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorro
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11792"></a>
## FND-11792: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._skill_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _skill_level {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2748.

```text
sary {
  bool is_pawniversary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11793"></a>
## FND-11793: chesscom.user_properties.v1.UserDetailsProperty.skill_level = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string skill_level = 19;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2771.

```text
ersary = 17;
  }
  oneof _is_reactivated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11794"></a>
## FND-11794: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._last_click_email_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_click_email_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2802.

```text
activated {
  bool is_reactivated = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_fo
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11795"></a>
## FND-11795: chesscom.user_properties.v1.UserDetailsProperty.last_click_email_date = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_click_email_date = 20;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2835.

```text
 = 18;
  }
  oneof _skill_level {
  string skill_level = 19;
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_ri
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11796"></a>
## FND-11796: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_on_do_not_email_list

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_on_do_not_email_list {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2896.

```text
  }
  oneof _last_click_email_date {
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversa
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11797"></a>
## FND-11797: chesscom.user_properties.v1.UserDetailsProperty.is_on_do_not_email_list = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_on_do_not_email_list = 21;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2931.

```text
{
  .google.protobuf.Timestamp last_click_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11798"></a>
## FND-11798: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_pawniversary_tomorrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_pawniversary_tomorrow {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 2972.

```text
_email_date = 20;
  }
  oneof _is_on_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11799"></a>
## FND-11799: chesscom.user_properties.v1.UserDetailsProperty.is_pawniversary_tomorrow = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_pawniversary_tomorrow = 22;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3008.

```text
_do_not_email_list {
  bool is_on_do_not_email_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  s
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11800"></a>
## FND-11800: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_guest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_guest {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3050.

```text
mail_list = 21;
  }
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _acc
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11801"></a>
## FND-11801: chesscom.user_properties.v1.UserDetailsProperty.is_guest = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_guest = 23;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3070.

```text
  oneof _is_pawniversary_tomorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  stri
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11802"></a>
## FND-11802: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._user_right_to_be_forgotten_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_right_to_be_forgotten_status {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3096.

```text
omorrow {
  bool is_pawniversary_tomorrow = 22;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11803"></a>
## FND-11803: chesscom.user_properties.v1.UserDetailsProperty.user_right_to_be_forgotten_status = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_right_to_be_forgotten_status = 25;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3141.

```text
2;
  }
  oneof _is_guest {
  bool is_guest = 23;
  }
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_ty
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11804"></a>
## FND-11804: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._next_pawniversary_start_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _next_pawniversary_start_date {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3194.

```text
  oneof _user_right_to_be_forgotten_status {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closu
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11805"></a>
## FND-11805: chesscom.user_properties.v1.UserDetailsProperty.next_pawniversary_start_date = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp next_pawniversary_start_date = 26;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3234.

```text
us {
  string user_right_to_be_forgotten_status = 25;
  }
  oneof _next_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11806"></a>
## FND-11806: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._opt_in_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opt_in_status {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3302.

```text
ext_pawniversary_start_date {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bo
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11807"></a>
## FND-11807: chesscom.user_properties.v1.UserDetailsProperty.opt_in_status = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opt_in_status = 28;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3327.

```text
te {
  .google.protobuf.Timestamp next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11808"></a>
## FND-11808: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._account_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _account_status {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3360.

```text
 next_pawniversary_start_date = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string langu
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11809"></a>
## FND-11809: chesscom.user_properties.v1.UserDetailsProperty.account_status = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string account_status = 29;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3386.

```text
ate = 26;
  }
  oneof _opt_in_status {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _lan
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11810"></a>
## FND-11810: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._closure_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _closure_type {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3420.

```text
us {
  string opt_in_status = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string langua
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11811"></a>
## FND-11811: chesscom.user_properties.v1.UserDetailsProperty.closure_type = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string closure_type = 30;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3444.

```text
tus = 28;
  }
  oneof _account_status {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11812"></a>
## FND-11812: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._closure_reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _closure_reason {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3476.

```text
tatus {
  string account_status = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11813"></a>
## FND-11813: chesscom.user_properties.v1.UserDetailsProperty.closure_reason = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string closure_reason = 31;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3502.

```text
tatus = 29;
  }
  oneof _closure_type {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11814"></a>
## FND-11814: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._activation_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _activation_type {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3536.

```text
ype {
  string closure_type = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11815"></a>
## FND-11815: chesscom.user_properties.v1.UserDetailsProperty.activation_type = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string activation_type = 32;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3563.

```text
 = 30;
  }
  oneof _closure_reason {
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11816"></a>
## FND-11816: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_avatar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_avatar {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3598.

```text
{
  string closure_reason = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11817"></a>
## FND-11817: chesscom.user_properties.v1.UserDetailsProperty.has_avatar = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_avatar = 33;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3620.

```text
son = 31;
  }
  oneof _activation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11818"></a>
## FND-11818: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._language

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _language {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3648.

```text
ation_type {
  string activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11819"></a>
## FND-11819: chesscom.user_properties.v1.UserDetailsProperty.language = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string language = 34;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3668.

```text
g activation_type = 32;
  }
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  b
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11820"></a>
## FND-11820: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._language_cloudflare

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _language_cloudflare {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3696.

```text
  oneof _has_avatar {
  bool has_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11821"></a>
## FND-11821: chesscom.user_properties.v1.UserDetailsProperty.language_cloudflare = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string language_cloudflare = 35;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3727.

```text
s_avatar = 33;
  }
  oneof _language {
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketi
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11822"></a>
## FND-11822: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_fcm_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_fcm_token {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3766.

```text
  string language = 34;
  }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_i
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11823"></a>
## FND-11823: chesscom.user_properties.v1.UserDetailsProperty.has_fcm_token = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_fcm_token = 36;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3791.

```text
 }
  oneof _language_cloudflare {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_b
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11824"></a>
## FND-11824: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_ios_fcm_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_ios_fcm_token {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3822.

```text
 {
  string language_cloudflare = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11825"></a>
## FND-11825: chesscom.user_properties.v1.UserDetailsProperty.has_ios_fcm_token = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_ios_fcm_token = 37;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3851.

```text
re = 35;
  }
  oneof _has_fcm_token {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11826"></a>
## FND-11826: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_android_fcm_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_android_fcm_token {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3886.

```text
 {
  bool has_fcm_token = 36;
  }
  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawn
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11827"></a>
## FND-11827: chesscom.user_properties.v1.UserDetailsProperty.has_android_fcm_token = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_android_fcm_token = 38;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3919.

```text

  oneof _has_ios_fcm_token {
  bool has_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniver
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11828"></a>
## FND-11828: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_web_fcm_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_web_fcm_token {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3958.

```text
s_ios_fcm_token = 37;
  }
  oneof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_r
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11829"></a>
## FND-11829: chesscom.user_properties.v1.UserDetailsProperty.has_web_fcm_token = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_web_fcm_token = 39;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 3987.

```text
neof _has_android_fcm_token {
  bool has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_ratin
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11830"></a>
## FND-11830: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._experiment_bucketing_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _experiment_bucketing_id {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4022.

```text
l has_android_fcm_token = 38;
  }
  oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11831"></a>
## FND-11831: chesscom.user_properties.v1.UserDetailsProperty.experiment_bucketing_id = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string experiment_bucketing_id = 40;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4057.

```text
 oneof _has_web_fcm_token {
  bool has_web_fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11832"></a>
## FND-11832: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_bot

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_bot {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4100.

```text
fcm_token = 39;
  }
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11833"></a>
## FND-11833: chesscom.user_properties.v1.UserDetailsProperty.is_bot = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_bot = 42;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4118.

```text
}
  oneof _experiment_bucketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11834"></a>
## FND-11834: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._trust_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trust_level {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4142.

```text
cketing_id {
  string experiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11835"></a>
## FND-11835: chesscom.user_properties.v1.UserDetailsProperty.trust_level = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 trust_level = 43;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4165.

```text
xperiment_bucketing_id = 40;
  }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11836"></a>
## FND-11836: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._pawniversary_years

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pawniversary_years {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4195.

```text
 }
  oneof _is_bot {
  bool is_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11837"></a>
## FND-11837: chesscom.user_properties.v1.UserDetailsProperty.pawniversary_years = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 pawniversary_years = 44;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4225.

```text
_bot = 42;
  }
  oneof _trust_level {
  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string bl
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11838"></a>
## FND-11838: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._initial_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_rating {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4262.

```text

  int32 trust_level = 43;
  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11839"></a>
## FND-11839: chesscom.user_properties.v1.UserDetailsProperty.initial_rating = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 initial_rating = 45;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4288.

```text

  }
  oneof _pawniversary_years {
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11840"></a>
## FND-11840: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_trusted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_trusted {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4321.

```text
{
  int32 pawniversary_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11841"></a>
## FND-11841: chesscom.user_properties.v1.UserDetailsProperty.is_trusted = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_trusted = 46;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4343.

```text
_years = 44;
  }
  oneof _initial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11842"></a>
## FND-11842: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_twitch_connection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_twitch_connection {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4371.

```text
itial_rating {
  int32 initial_rating = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11843"></a>
## FND-11843: chesscom.user_properties.v1.UserDetailsProperty.has_twitch_connection = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_twitch_connection = 47;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4404.

```text
ting = 45;
  }
  oneof _is_trusted {
  bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11844"></a>
## FND-11844: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_youtube_connection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_youtube_connection {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4443.

```text
bool is_trusted = 46;
  }
  oneof _has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11845"></a>
## FND-11845: chesscom.user_properties.v1.UserDetailsProperty.has_youtube_connection = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_youtube_connection = 48;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4477.

```text
_has_twitch_connection {
  bool has_twitch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  re
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11846"></a>
## FND-11846: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._blog_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _blog_id {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4517.

```text
ch_connection = 47;
  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_resul
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11847"></a>
## FND-11847: chesscom.user_properties.v1.UserDetailsProperty.blog_id = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string blog_id = 49;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4536.

```text

  }
  oneof _has_youtube_connection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11848"></a>
## FND-11848: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._stream_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stream_url {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4563.

```text
onnection {
  bool has_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 4
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11849"></a>
## FND-11849: chesscom.user_properties.v1.UserDetailsProperty.stream_url = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string stream_url = 50;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4585.

```text
_youtube_connection = 48;
  }
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string t
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11850"></a>
## FND-11850: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._closure_status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _closure_status {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4615.

```text
  oneof _blog_id {
  string blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 
```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11851"></a>
## FND-11851: chesscom.user_properties.v1.UserDetailsProperty.closure_status = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string closure_status = 51;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4641.

```text
g blog_id = 49;
  }
  oneof _stream_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11852"></a>
## FND-11852: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._is_beta

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_beta {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4675.

```text
m_url {
  string stream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11853"></a>
## FND-11853: chesscom.user_properties.v1.UserDetailsProperty.is_beta = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_beta = 53;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4694.

```text
ream_url = 50;
  }
  oneof _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11854"></a>
## FND-11854: oneof declaration: chesscom.user_properties.v1.UserDetailsProperty._has_linkedin_connection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _has_linkedin_connection {

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4719.

```text
f _closure_status {
  string closure_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11855"></a>
## FND-11855: chesscom.user_properties.v1.UserDetailsProperty.has_linkedin_connection = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool has_linkedin_connection = 54;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4754.

```text
e_status = 51;
  }
  oneof _is_beta {
  bool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11856"></a>
## FND-11856: chesscom.user_properties.v1.UserDetailsProperty.experiment_bucketing_results = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string experiment_bucketing_results = 27;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4795.

```text
ool is_beta = 53;
  }
  oneof _has_linkedin_connection {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11857"></a>
## FND-11857: chesscom.user_properties.v1.UserDetailsProperty.lists_member_of = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string lists_member_of = 41;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4848.

```text
n {
  bool has_linkedin_connection = 54;
  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11858"></a>
## FND-11858: chesscom.user_properties.v1.UserDetailsProperty.temporary_datasets_member_of = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string temporary_datasets_member_of = 52;

### Evidence

- **SRC-0640** `research/proto/chesscom/user_properties/v1/properties_user_details.proto` — [preserved redacted evidence](../evidence/text/6f5dae05668581067f398e13864c4d49e628ffd4e531d7e57415b6649f5d3360.proto)
  Character offset 4888.

```text

  }
  repeated string experiment_bucketing_results = 27;
  repeated string lists_member_of = 41;
  repeated string temporary_datasets_member_of = 52;
}

```

**Source references:** SRC-0640, SRC-1611  
**URL references:** None independently associated  
**Related findings:** FND-11706, FND-11707, FND-11708

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11859"></a>
## FND-11859: enum declaration: chesscom.user_properties.v1.UserEngagementPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserEngagementPropertyDefinition {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 129.

```text
erties/v1/properties_user_engagement.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum UserEngagementPropertyDefinition {
  USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0;
  LAST_BOUNCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11860"></a>
## FND-11860: chesscom.user_properties.v1.UserEngagementPropertyDefinition.USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 171.

```text

// syntax: proto3

package chesscom.user_properties.v1;

enum UserEngagementPropertyDefinition {
  USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0;
  LAST_BOUNCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DAT
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11861"></a>
## FND-11861: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_BOUNCE_DATE_SENDGRID = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_BOUNCE_DATE_SENDGRID = 1;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 215.

```text
operties.v1;

enum UserEngagementPropertyDefinition {
  USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0;
  LAST_BOUNCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICAT
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11862"></a>
## FND-11862: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_OPEN_EMAIL_DATE_SENDGRID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPEN_EMAIL_DATE_SENDGRID = 2;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 248.

```text
PropertyDefinition {
  USER_ENGAGEMENT_PROPERTY_UNSPECIFIED = 0;
  LAST_BOUNCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIE
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11863"></a>
## FND-11863: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_CLICK_EMAIL_DATE_SENDGRID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CLICK_EMAIL_DATE_SENDGRID = 3;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 285.

```text
T_PROPERTY_UNSPECIFIED = 0;
  LAST_BOUNCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PU
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11864"></a>
## FND-11864: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_BOUNCE_DATE_ITERABLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_BOUNCE_DATE_ITERABLE = 4;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 323.

```text
NCE_DATE_SENDGRID = 1;
  LAST_OPEN_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMA
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11865"></a>
## FND-11865: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_OPEN_EMAIL_DATE_ITERABLE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPEN_EMAIL_DATE_ITERABLE = 5;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 356.

```text
N_EMAIL_DATE_SENDGRID = 2;
  LAST_CLICK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11866"></a>
## FND-11866: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_CLICK_EMAIL_DATE_ITERABLE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CLICK_EMAIL_DATE_ITERABLE = 6;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 393.

```text
CK_EMAIL_DATE_SENDGRID = 3;
  LAST_BOUNCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11867"></a>
## FND-11867: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_DROPPED_EMAIL_DATE_SENDGRID = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 431.

```text
NCE_DATE_ITERABLE = 4;
  LAST_OPEN_EMAIL_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11868"></a>
## FND-11868: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_SPAM_REPORT_DATE_SENDGRID = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_SPAM_REPORT_DATE_SENDGRID = 8;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 471.

```text
_DATE_ITERABLE = 5;
  LAST_CLICK_EMAIL_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .go
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11869"></a>
## FND-11869: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 509.

```text
_DATE_ITERABLE = 6;
  LAST_DROPPED_EMAIL_DATE_SENDGRID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_da
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11870"></a>
## FND-11870: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_VIEWED_PAYMENT_PAGE_DATE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_VIEWED_PAYMENT_PAGE_DATE = 10;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 560.

```text
RID = 7;
  LAST_SPAM_REPORT_DATE_SENDGRID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11871"></a>
## FND-11871: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_PUSH_OPEN_DATE_ITERABLE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_PUSH_OPEN_DATE_ITERABLE = 11;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 598.

```text
RID = 8;
  LAST_OPENED_PUSH_NOTIFICATION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestam
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11872"></a>
## FND-11872: chesscom.user_properties.v1.UserEngagementPropertyDefinition.LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 635.

```text
ION_DATE_FIREBASE = 9;
  LAST_VIEWED_PAYMENT_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;

```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11873"></a>
## FND-11873: chesscom.user_properties.v1.UserEngagementPropertyDefinition.TOTAL_EMAIL_BOUNCES_ITERABLE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TOTAL_EMAIL_BOUNCES_ITERABLE = 13;

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 678.

```text
T_PAGE_DATE = 10;
  LAST_PUSH_OPEN_DATE_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
  TOTAL_EMAIL_BOUNCES_ITERABLE = 13;
}

message UserEngagementProperty {
  oneof _last_bounce_date_sendgrid {
  .google.protobuf.Timestamp last_bounce_date_sendgrid = 1;
  }
  oneof _last_open_email_date_sendgrid {
  .google.protobuf.Timestamp last_open_email_date_sendgrid = 2;
  }
  oneof _last_click_email_date_sendgrid
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11874"></a>
## FND-11874: message declaration: chesscom.user_properties.v1.UserEngagementProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserEngagementProperty {

### Evidence

- **SRC-0641** `research/proto/chesscom/user_properties/v1/properties_user_engagement.proto` — [preserved redacted evidence](../evidence/text/7f58c4edcf25d0e8d2478d3700c14fdd62865cecf5a159e3fd8c2bad96ff8dc3.proto)
  Character offset 716.

```text
E_ITERABLE = 11;
  LAST_EMAIL_COMPLAINT_DATE_ITERABLE = 12;
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
  .google.protobuf.Timestamp last_c
```

**Source references:** SRC-0641, SRC-1612  
**URL references:** None independently associated  
**Related findings:** FND-11859, FND-11860, FND-11861

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
