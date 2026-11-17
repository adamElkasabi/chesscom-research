# data_models — findings 9101–9200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09375"></a>
## FND-09375: chesscom.user_activity.v1.Client.Name.USER_PROPERTIES = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_PROPERTIES = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7140.

```text
 = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09376"></a>
## FND-09376: chesscom.user_activity.v1.Client.Name.ON_PLATFORM_MESSAGING = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ON_PLATFORM_MESSAGING = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7165.

```text
LIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_na
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09377"></a>
## FND-09377: chesscom.user_activity.v1.Client.Name.WORKFLOWS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WORKFLOWS = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7196.

```text
 WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09378"></a>
## FND-09378: chesscom.user_activity.v1.Client.Name.COURSES = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSES = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7215.

```text
 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09379"></a>
## FND-09379: chesscom.user_activity.v1.Client.Name.RCN_SERVICE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RCN_SERVICE = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7232.

```text
 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _s
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09380"></a>
## FND-09380: chesscom.user_activity.v1.Client.Name.PROGRESSION_SERVICE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROGRESSION_SERVICE = 9;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7253.

```text
ES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chess
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09381"></a>
## FND-09381: chesscom.user_activity.v1.Client.Name.ITERABLE_CONNECTOR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ITERABLE_CONNECTOR = 10;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7282.

```text
GING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09382"></a>
## FND-09382: chesscom.user_activity.v1.Client.Name.SENDGRID_WEBHOOKS = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SENDGRID_WEBHOOKS = 11;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7311.

```text
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09383"></a>
## FND-09383: chesscom.user_activity.v1.Client.Name.EMAIL_SENDER = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EMAIL_SENDER = 12;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7339.

```text
VICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09384"></a>
## FND-09384: chesscom.user_activity.v1.Client.Name.PUSH_SENDER = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUSH_SENDER = 13;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7362.

```text
ON_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09385"></a>
## FND-09385: message declaration: chesscom.user_activity.v1.UserProperties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserProperties {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7387.

```text
BLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09386"></a>
## FND-09386: oneof declaration: chesscom.user_activity.v1.UserProperties._client_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _client_name {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7414.

```text
DGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09387"></a>
## FND-09387: chesscom.user_activity.v1.UserProperties.client_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Client.Name client_name = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7437.

```text
  EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09388"></a>
## FND-09388: oneof declaration: chesscom.user_activity.v1.UserProperties._country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7499.

```text
Properties {
  oneof _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09389"></a>
## FND-09389: chesscom.user_activity.v1.UserProperties.country = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string country = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7518.

```text
f _client_name {
  .chesscom.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09390"></a>
## FND-09390: oneof declaration: chesscom.user_activity.v1.UserProperties._skill_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _skill_level {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7544.

```text
om.user_activity.v1.Client.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09391"></a>
## FND-09391: chesscom.user_activity.v1.UserProperties.skill_level = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user.v1.SkillLevel skill_level = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7567.

```text
ent.Name client_name = 1;
  }
  oneof _country {
  string country = 2;
  }
  oneof _skill_level {
  .chesscom.user.v1.SkillLevel skill_level = 3;
  }
}

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09392"></a>
## FND-09392: message declaration: chesscom.user_gateway.v1.GatewayUserView

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GatewayUserView {

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 109.

```text
: chesscom/user_gateway/v1/user_gateway.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GatewayUserView {
  oneof _user_properties {
  .chesscom.user_properties.v1.PropertiesByUser user_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4
```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09393, FND-09394

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09393"></a>
## FND-09393: oneof declaration: chesscom.user_gateway.v1.GatewayUserView._user_properties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_properties {

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 137.

```text
ser_gateway.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GatewayUserView {
  oneof _user_properties {
  .chesscom.user_properties.v1.PropertiesByUser user_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_
```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09394

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09394"></a>
## FND-09394: chesscom.user_gateway.v1.GatewayUserView.user_properties = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PropertiesByUser user_properties = 2;

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 164.

```text
: proto3

package chesscom.user_gateway.v1;

message GatewayUserView {
  oneof _user_properties {
  .chesscom.user_properties.v1.PropertiesByUser user_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUs
```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09395"></a>
## FND-09395: oneof declaration: chesscom.user_gateway.v1.GatewayUserView._presence

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _presence {

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 237.

```text
oneof _user_properties {
  .chesscom.user_properties.v1.PropertiesByUser user_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;
}

```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393, FND-09394

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09396"></a>
## FND-09396: chesscom.user_gateway.v1.GatewayUserView.presence = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.presence.v1.UserPresence presence = 3;

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 257.

```text
es {
  .chesscom.user_properties.v1.PropertiesByUser user_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;
}

```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393, FND-09394

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09397"></a>
## FND-09397: chesscom.user_gateway.v1.GatewayUserView.user = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user.v1.UserView user = 1;

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 312.

```text
er_properties = 2;
  }
  oneof _presence {
  .chesscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;
}

```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393, FND-09394

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09398"></a>
## FND-09398: chesscom.user_gateway.v1.GatewayUserView.ratings = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 360.

```text
esscom.presence.v1.UserPresence presence = 3;
  }
  optional .chesscom.user.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;
}

```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393, FND-09394

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09399"></a>
## FND-09399: chesscom.user_gateway.v1.GatewayUserView.relationships = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;

### Evidence

- **SRC-0593** `research/proto/chesscom/user_gateway/v1/user_gateway.proto` — [preserved redacted evidence](../evidence/text/b3fc270b52a109fcef32098c132e2e3745452886dabf64a3f0328c973e546183.proto)
  Character offset 433.

```text
er.v1.UserView user = 1;
  repeated .chesscom.ratings.v2.VariantTimeClassRatingGroup ratings = 4;
  repeated .chesscom.user_relationships.v2.ListableUserRelationship relationships = 5;
}

```

**Source references:** SRC-0593, SRC-1564  
**URL references:** None independently associated  
**Related findings:** FND-09392, FND-09393, FND-09394

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09400"></a>
## FND-09400: message declaration: chesscom.user_gateway.v1.GetUserDataRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 117.

```text
om/user_gateway/v1/user_gateway_service.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gatewa
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09401"></a>
## FND-09401: chesscom.user_gateway.v1.GetUserDataRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 148.

```text
_service.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09402"></a>
## FND-09402: chesscom.user_gateway.v1.GetUserDataRequest.other_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string other_user_uuids = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 181.

```text

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09403"></a>
## FND-09403: chesscom.user_gateway.v1.GetUserDataRequest.user_relationships = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 221.

```text
age GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09404"></a>
## FND-09404: chesscom.user_gateway.v1.GetUserDataRequest.field_mask = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 4;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 320.

```text
 repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelati
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09405"></a>
## FND-09405: message declaration: chesscom.user_gateway.v1.GetUserDataResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 375.

```text
hipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optiona
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09406"></a>
## FND-09406: chesscom.user_gateway.v1.GetUserDataResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 407.

```text
ships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09407"></a>
## FND-09407: message declaration: chesscom.user_gateway.v1.GetUserDataByUsernameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataByUsernameRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 476.

```text
essage GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09408"></a>
## FND-09408: chesscom.user_gateway.v1.GetUserDataByUsernameRequest.username = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 517.

```text
chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataByUsernameResponse {
  optional .ches
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09409"></a>
## FND-09409: chesscom.user_gateway.v1.GetUserDataByUsernameRequest.other_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string other_user_uuids = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 181.

```text

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09410"></a>
## FND-09410: chesscom.user_gateway.v1.GetUserDataByUsernameRequest.user_relationships = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 221.

```text
age GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09411"></a>
## FND-09411: chesscom.user_gateway.v1.GetUserDataByUsernameRequest.field_mask = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 4;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 320.

```text
 repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelati
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09412"></a>
## FND-09412: chesscom.user_gateway.v1.GetUserDataByUsernameRequest.include_disabled = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool include_disabled = 5;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 742.

```text
shipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataByUsernameResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataManyRequest {
  repeated string user_uuids = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequ
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09413"></a>
## FND-09413: message declaration: chesscom.user_gateway.v1.GetUserDataByUsernameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataByUsernameResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 781.

```text
= 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataByUsernameResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataManyRequest {
  repeated string user_uuids = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  o
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09414"></a>
## FND-09414: chesscom.user_gateway.v1.GetUserDataByUsernameResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 407.

```text
ships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09415"></a>
## FND-09415: message declaration: chesscom.user_gateway.v1.GetUserDataManyRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataManyRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 892.

```text
UserDataByUsernameResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataManyRequest {
  repeated string user_uuids = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.us
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09416"></a>
## FND-09416: chesscom.user_gateway.v1.GetUserDataManyRequest.user_uuids = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string user_uuids = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 927.

```text
onal .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataManyRequest {
  repeated string user_uuids = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09417"></a>
## FND-09417: chesscom.user_gateway.v1.GetUserDataManyRequest.other_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string other_user_uuids = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 181.

```text

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09418"></a>
## FND-09418: chesscom.user_gateway.v1.GetUserDataManyRequest.user_relationships = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 221.

```text
age GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09419"></a>
## FND-09419: chesscom.user_gateway.v1.GetUserDataManyRequest.field_mask = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 4;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 320.

```text
 repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelati
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09420"></a>
## FND-09420: message declaration: chesscom.user_gateway.v1.GetUserDataManyResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataManyResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1155.

```text
hipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListRelatedUsersDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  opt
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09421"></a>
## FND-09421: chesscom.user_gateway.v1.GetUserDataManyResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1191.

```text
s = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListRelatedUsersDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09422"></a>
## FND-09422: message declaration: chesscom.user_gateway.v1.ListRelatedUsersDataRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRelatedUsersDataRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1260.

```text
ge GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListRelatedUsersDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message ListRelatedUsersDataResponse {
  repeated .ch
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09423"></a>
## FND-09423: chesscom.user_gateway.v1.ListRelatedUsersDataRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 148.

```text
_service.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09424"></a>
## FND-09424: chesscom.user_gateway.v1.ListRelatedUsersDataRequest.other_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string other_user_uuids = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 181.

```text

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09425"></a>
## FND-09425: chesscom.user_gateway.v1.ListRelatedUsersDataRequest.user_relationships = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 221.

```text
age GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09426"></a>
## FND-09426: chesscom.user_gateway.v1.ListRelatedUsersDataRequest.field_mask = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 4;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 320.

```text
 repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelati
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09427"></a>
## FND-09427: message declaration: chesscom.user_gateway.v1.ListRelatedUsersDataResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListRelatedUsersDataResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1527.

```text
hipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message ListRelatedUsersDataResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataWithOtherUsernamesRequest {
  optional string user_uuid = 1;
  repeated string other_usernames = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationshi
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09428"></a>
## FND-09428: chesscom.user_gateway.v1.ListRelatedUsersDataResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1191.

```text
s = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListRelatedUsersDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09429"></a>
## FND-09429: message declaration: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataWithOtherUsernamesRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1637.

```text
stRelatedUsersDataResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataWithOtherUsernamesRequest {
  optional string user_uuid = 1;
  repeated string other_usernames = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09430"></a>
## FND-09430: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 148.

```text
_service.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09431"></a>
## FND-09431: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest.other_usernames = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string other_usernames = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1719.

```text
user_data = 1;
}

message GetUserDataWithOtherUsernamesRequest {
  optional string user_uuid = 1;
  repeated string other_usernames = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataWithOtherUsernamesResponse {
  optional .chesscom.user_gateway.v1.Gate
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09432"></a>
## FND-09432: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest.user_relationships = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 221.

```text
age GetUserDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09433"></a>
## FND-09433: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest.field_mask = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 4;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 320.

```text
 repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelati
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09434"></a>
## FND-09434: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest.include_disabled = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool include_disabled = 5;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 742.

```text
shipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataByUsernameResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataManyRequest {
  repeated string user_uuids = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequ
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09435"></a>
## FND-09435: message declaration: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserDataWithOtherUsernamesResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1950.

```text
= 3;
  optional .google.protobuf.FieldMask field_mask = 4;
  optional bool include_disabled = 5;
}

message GetUserDataWithOtherUsernamesResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.Fiel
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09436"></a>
## FND-09436: chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 407.

```text
ships = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message GetUserDataByUsernameRequest {
  optional string username = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09437"></a>
## FND-09437: message declaration: chesscom.user_gateway.v1.ListUsersRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListUsersRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2069.

```text
WithOtherUsernamesResponse {
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09438"></a>
## FND-09438: oneof declaration: chesscom.user_gateway.v1.ListUsersRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2098.

```text
  optional .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09439"></a>
## FND-09439: chesscom.user_gateway.v1.ListUsersRequest.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2120.

```text
ser_gateway.v1.GatewayUserView user_data = 1;
}

message ListUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pa
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09440"></a>
## FND-09440: chesscom.user_gateway.v1.ListUsersRequest.criteria = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_targeting.v1.Criterion criteria = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2177.

```text
ListUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
  one
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09441"></a>
## FND-09441: chesscom.user_gateway.v1.ListUsersRequest.field_mask = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.FieldMask field_mask = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2240.

```text
uestPagination pagination = 1;
  }
  repeated .chesscom.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
  oneof _source {
  string source = 2;
  }
  oneof _method {
  strin
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09442"></a>
## FND-09442: message declaration: chesscom.user_gateway.v1.ListUsersResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListUsersResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2295.

```text
.user_targeting.v1.Criterion criteria = 2;
  optional .google.protobuf.FieldMask field_mask = 3;
}

message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
  oneof _source {
  string source = 2;
  }
  oneof _method {
  string method = 3;
  }
  optional .chesscom.user_gateway.v1.
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09443"></a>
## FND-09443: chesscom.user_gateway.v1.ListUsersResponse.user_data = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 1191.

```text
s = 3;
  optional .google.protobuf.FieldMask field_mask = 4;
}

message GetUserDataManyResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
}

message ListRelatedUsersDataRequest {
  optional string user_uuid = 1;
  repeated string other_user_uuids = 2;
  repeated .chesscom.user_relationships.v2.UserRelationshipRequestCriteria user_relationships = 3;
  optional .google.protobuf.FieldMask fie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09444"></a>
## FND-09444: chesscom.user_gateway.v1.ListUsersResponse.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2393.

```text


message ListUsersResponse {
  repeated .chesscom.user_gateway.v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
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
  .che
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09445"></a>
## FND-09445: message declaration: chesscom.user_gateway.v1.SendFriendRequestRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SendFriendRequestRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2457.

```text
v1.GatewayUserView user_data = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
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
  .c
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09446"></a>
## FND-09446: oneof declaration: chesscom.user_gateway.v1.SendFriendRequestRequest._source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _source {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2494.

```text
ptional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
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
  .chesscom.user_gateway.v1.SendFriendReq
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09447"></a>
## FND-09447: chesscom.user_gateway.v1.SendFriendRequestRequest.source = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string source = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2512.

```text
api.v1.ResponsePagination pagination = 2;
}

message SendFriendRequestRequest {
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
  .chesscom.user_gateway.v1.SendFriendRequestFailure failur
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09448"></a>
## FND-09448: oneof declaration: chesscom.user_gateway.v1.SendFriendRequestRequest._method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _method {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2537.

```text
 pagination = 2;
}

message SendFriendRequestRequest {
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

message Acc
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09449"></a>
## FND-09449: chesscom.user_gateway.v1.SendFriendRequestRequest.method = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string method = 3;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2555.

```text


message SendFriendRequestRequest {
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

message AcceptFriendRequestRe
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09450"></a>
## FND-09450: chesscom.user_gateway.v1.SendFriendRequestRequest.user_identifier = 1

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

<a id="FND-09451"></a>
## FND-09451: message declaration: chesscom.user_gateway.v1.SendFriendRequestResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SendFriendRequestResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2654.

```text
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
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptF
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09452"></a>
## FND-09452: oneof declaration: chesscom.user_gateway.v1.SendFriendRequestResponse.result

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

<a id="FND-09453"></a>
## FND-09453: chesscom.user_gateway.v1.SendFriendRequestResponse.success = 1

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

<a id="FND-09454"></a>
## FND-09454: chesscom.user_gateway.v1.SendFriendRequestResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2775.

```text
uestResponse {
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
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.use
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09455"></a>
## FND-09455: message declaration: chesscom.user_gateway.v1.AcceptFriendRequestRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendRequestRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2846.

```text
pWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendRequestFailure failure = 2;
  }
}

message Dec
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09456"></a>
## FND-09456: chesscom.user_gateway.v1.AcceptFriendRequestRequest.user_identifier = 1

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

<a id="FND-09457"></a>
## FND-09457: message declaration: chesscom.user_gateway.v1.AcceptFriendRequestResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendRequestResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2959.

```text
tFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendRequestFailure failure = 2;
  }
}

message DeclineFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message De
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09458"></a>
## FND-09458: oneof declaration: chesscom.user_gateway.v1.AcceptFriendRequestResponse.result

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

<a id="FND-09459"></a>
## FND-09459: chesscom.user_gateway.v1.AcceptFriendRequestResponse.success = 1

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

<a id="FND-09460"></a>
## FND-09460: chesscom.user_gateway.v1.AcceptFriendRequestResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.AcceptFriendRequestFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3082.

```text
uestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendRequestFailure failure = 2;
  }
}

message DeclineFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message DeclineFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09461"></a>
## FND-09461: message declaration: chesscom.user_gateway.v1.DeclineFriendRequestRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeclineFriendRequestRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3155.

```text
riteSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendRequestFailure failure = 2;
  }
}

message DeclineFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message DeclineFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.DeclineFriendRequestFailure failure = 2;
  }
}

message 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09462"></a>
## FND-09462: chesscom.user_gateway.v1.DeclineFriendRequestRequest.user_identifier = 1

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

<a id="FND-09463"></a>
## FND-09463: message declaration: chesscom.user_gateway.v1.DeclineFriendRequestResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeclineFriendRequestResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3269.

```text
eFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message DeclineFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.DeclineFriendRequestFailure failure = 2;
  }
}

message CancelFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message C
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09464"></a>
## FND-09464: oneof declaration: chesscom.user_gateway.v1.DeclineFriendRequestResponse.result

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

<a id="FND-09465"></a>
## FND-09465: chesscom.user_gateway.v1.DeclineFriendRequestResponse.success = 1

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

<a id="FND-09466"></a>
## FND-09466: chesscom.user_gateway.v1.DeclineFriendRequestResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.DeclineFriendRequestFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3393.

```text
uestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.DeclineFriendRequestFailure failure = 2;
  }
}

message CancelFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message CancelFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09467"></a>
## FND-09467: message declaration: chesscom.user_gateway.v1.CancelFriendRequestRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelFriendRequestRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3467.

```text
iteSuccess success = 1;
  .chesscom.user_gateway.v1.DeclineFriendRequestFailure failure = 2;
  }
}

message CancelFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message CancelFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.CancelFriendRequestFailure failure = 2;
  }
}

message Rem
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09468"></a>
## FND-09468: chesscom.user_gateway.v1.CancelFriendRequestRequest.user_identifier = 1

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

<a id="FND-09469"></a>
## FND-09469: message declaration: chesscom.user_gateway.v1.CancelFriendRequestResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelFriendRequestResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3580.

```text
lFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message CancelFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.CancelFriendRequestFailure failure = 2;
  }
}

message RemoveFriendRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message RemoveFrie
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09470"></a>
## FND-09470: oneof declaration: chesscom.user_gateway.v1.CancelFriendRequestResponse.result

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

<a id="FND-09471"></a>
## FND-09471: chesscom.user_gateway.v1.CancelFriendRequestResponse.success = 1

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

<a id="FND-09472"></a>
## FND-09472: chesscom.user_gateway.v1.CancelFriendRequestResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.CancelFriendRequestFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3703.

```text
uestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.CancelFriendRequestFailure failure = 2;
  }
}

message RemoveFriendRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message RemoveFriendResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09473"></a>
## FND-09473: message declaration: chesscom.user_gateway.v1.RemoveFriendRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveFriendRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3776.

```text
riteSuccess success = 1;
  .chesscom.user_gateway.v1.CancelFriendRequestFailure failure = 2;
  }
}

message RemoveFriendRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message RemoveFriendResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.RemoveFriendFailure failure = 2;
  }
}

message BlockUserRequest {
  opt
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09474"></a>
## FND-09474: chesscom.user_gateway.v1.RemoveFriendRequest.user_identifier = 1

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
