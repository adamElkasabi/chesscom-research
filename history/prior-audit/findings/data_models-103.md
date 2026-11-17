# data_models — findings 10201–10300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10475"></a>
## FND-10475: chesscom.user_properties.v1.IpqsProperty.ipqs_abuse_velocity = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string ipqs_abuse_velocity = 7;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 945.

```text
f _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recent
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10476"></a>
## FND-10476: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_has_abused_recently

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_has_abused_recently {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 983.

```text
s_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recentl
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10477"></a>
## FND-10477: chesscom.user_properties.v1.IpqsProperty.ipqs_has_abused_recently = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_has_abused_recently = 8;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1019.

```text
 _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10478"></a>
## FND-10478: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_vpn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_vpn {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1060.

```text
se_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10479"></a>
## FND-10479: chesscom.user_properties.v1.IpqsProperty.ipqs_is_vpn = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_vpn = 9;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1083.

```text
oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10480"></a>
## FND-10480: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_tor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_tor {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1111.

```text
tly {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10481"></a>
## FND-10481: chesscom.user_properties.v1.IpqsProperty.ipqs_is_tor = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_tor = 10;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1134.

```text
bused_recently = 8;
  }
  oneof _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10482"></a>
## FND-10482: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_ip_fraud_score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_ip_fraud_score {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1163.

```text
of _ipqs_is_vpn {
  bool ipqs_is_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10483"></a>
## FND-10483: chesscom.user_properties.v1.IpqsProperty.ipqs_ip_fraud_score = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double ipqs_ip_fraud_score = 11;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1194.

```text
s_vpn = 9;
  }
  oneof _ipqs_is_tor {
  bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10484"></a>
## FND-10484: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_ip_has_abused_recently

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_ip_has_abused_recently {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1233.

```text
 bool ipqs_is_tor = 10;
  }
  oneof _ipqs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10485"></a>
## FND-10485: chesscom.user_properties.v1.IpqsProperty.ipqs_ip_has_abused_recently = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_ip_has_abused_recently = 12;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 1272.

```text
qs_ip_fraud_score {
  double ipqs_ip_fraud_score = 11;
  }
  oneof _ipqs_ip_has_abused_recently {
  bool ipqs_ip_has_abused_recently = 12;
  }
}

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10486"></a>
## FND-10486: enum declaration: chesscom.user_properties.v1.LeaguePropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum LeaguePropertyDefinition {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 120.

```text
user_properties/v1/properties_league.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum LeaguePropertyDefinition {
  LEAGUE_UNSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10487"></a>
## FND-10487: chesscom.user_properties.v1.LeaguePropertyDefinition.LEAGUE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LEAGUE_UNSPECIFIED = 0;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 154.

```text
ue.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum LeaguePropertyDefinition {
  LEAGUE_UNSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10488"></a>
## FND-10488: chesscom.user_properties.v1.LeaguePropertyDefinition.LEAGUE_NAME = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LEAGUE_NAME = 1;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 180.

```text


package chesscom.user_properties.v1;

enum LeaguePropertyDefinition {
  LEAGUE_UNSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promoti
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10489"></a>
## FND-10489: chesscom.user_properties.v1.LeaguePropertyDefinition.LEAGUE_IMAGE_URL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LEAGUE_IMAGE_URL = 2;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 199.

```text
user_properties.v1;

enum LeaguePropertyDefinition {
  LEAGUE_UNSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool le
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10490"></a>
## FND-10490: chesscom.user_properties.v1.LeaguePropertyDefinition.LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 223.

```text
m LeaguePropertyDefinition {
  LEAGUE_UNSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10491"></a>
## FND-10491: chesscom.user_properties.v1.LeaguePropertyDefinition.PROMOTION_LEAGUE_NAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_LEAGUE_NAME = 4;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 262.

```text
NSPECIFIED = 0;
  LEAGUE_NAME = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_leagu
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10492"></a>
## FND-10492: chesscom.user_properties.v1.LeaguePropertyDefinition.PROMOTION_LEAGUE_IMAGE_URL = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_LEAGUE_IMAGE_URL = 5;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 291.

```text
 = 1;
  LEAGUE_IMAGE_URL = 2;
  LEAGUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_l
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10493"></a>
## FND-10493: message declaration: chesscom.user_properties.v1.LeagueProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LeagueProperty {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 326.

```text
GUE_IS_IN_THE_PROMOTION_ZONE = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promot
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10494"></a>
## FND-10494: oneof declaration: chesscom.user_properties.v1.LeagueProperty._league_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _league_name {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 353.

```text
E = 3;
  PROMOTION_LEAGUE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  st
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10495"></a>
## FND-10495: chesscom.user_properties.v1.LeagueProperty.league_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string league_name = 1;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 376.

```text
UE_NAME = 4;
  PROMOTION_LEAGUE_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_i
```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10496"></a>
## FND-10496: oneof declaration: chesscom.user_properties.v1.LeagueProperty._league_image_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _league_image_url {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 406.

```text
E_IMAGE_URL = 5;
}

message LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10497"></a>
## FND-10497: chesscom.user_properties.v1.LeagueProperty.league_image_url = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string league_image_url = 2;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 434.

```text
LeagueProperty {
  oneof _league_name {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10498"></a>
## FND-10498: oneof declaration: chesscom.user_properties.v1.LeagueProperty._league_is_in_the_promotion_zone

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _league_is_in_the_promotion_zone {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 469.

```text
me {
  string league_name = 1;
  }
  oneof _league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10499"></a>
## FND-10499: chesscom.user_properties.v1.LeagueProperty.league_is_in_the_promotion_zone = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool league_is_in_the_promotion_zone = 3;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 512.

```text
_league_image_url {
  string league_image_url = 2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10500"></a>
## FND-10500: oneof declaration: chesscom.user_properties.v1.LeagueProperty._promotion_league_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _promotion_league_name {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 560.

```text
2;
  }
  oneof _league_is_in_the_promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10501"></a>
## FND-10501: chesscom.user_properties.v1.LeagueProperty.promotion_league_name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string promotion_league_name = 4;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 593.

```text
promotion_zone {
  bool league_is_in_the_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10502"></a>
## FND-10502: oneof declaration: chesscom.user_properties.v1.LeagueProperty._promotion_league_image_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _promotion_league_image_url {

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 633.

```text
_promotion_zone = 3;
  }
  oneof _promotion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10503"></a>
## FND-10503: chesscom.user_properties.v1.LeagueProperty.promotion_league_image_url = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string promotion_league_image_url = 5;

### Evidence

- **SRC-0614** `research/proto/chesscom/user_properties/v1/properties_league.proto` — [preserved redacted evidence](../evidence/text/c3318ac879e265ce5895bbd2d80682ed9cf3cb94edb971e324f92ed375c9a5ca.proto)
  Character offset 671.

```text
otion_league_name {
  string promotion_league_name = 4;
  }
  oneof _promotion_league_image_url {
  string promotion_league_image_url = 5;
  }
}

```

**Source references:** SRC-0614, SRC-1585  
**URL references:** None independently associated  
**Related findings:** FND-10486, FND-10487, FND-10488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10504"></a>
## FND-10504: enum declaration: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MonthlyBotEventPropertyDefinition {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 131.

```text
ties/v1/properties_monthly_bot_event.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum MonthlyBotEventPropertyDefinition {
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10505"></a>
## FND-10505: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition.MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 174.

```text
// syntax: proto3

package chesscom.user_properties.v1;

enum MonthlyBotEventPropertyDefinition {
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10506"></a>
## FND-10506: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition.MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 231.

```text
enum MonthlyBotEventPropertyDefinition {
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10507"></a>
## FND-10507: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition.MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 280.

```text
Y_BOT_EVENT_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achi
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10508"></a>
## FND-10508: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition.MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 332.

```text
ONTHLY_BOT_EVENT_PROPERTY_DEFINITION_KEY = 1;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof 
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10509"></a>
## FND-10509: chesscom.user_properties.v1.MonthlyBotEventPropertyDefinition.MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 397.

```text
_PROPERTY_DEFINITION_POINTS = 2;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progress
```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10510"></a>
## FND-10510: message declaration: chesscom.user_properties.v1.MonthlyBotEventProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MonthlyBotEventProperty {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 463.

```text
NITION_MILESTONES_ACHIEVED = 3;
  MONTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10511"></a>
## FND-10511: oneof declaration: chesscom.user_properties.v1.MonthlyBotEventProperty._key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _key {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 499.

```text
NTHLY_BOT_EVENT_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10512"></a>
## FND-10512: chesscom.user_properties.v1.MonthlyBotEventProperty.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string key = 1;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 514.

```text
_PROPERTY_DEFINITION_LAST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10513"></a>
## FND-10513: oneof declaration: chesscom.user_properties.v1.MonthlyBotEventProperty._points

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _points {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 536.

```text
AST_PROGRESSION_AT = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10514"></a>
## FND-10514: chesscom.user_properties.v1.MonthlyBotEventProperty.points = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 points = 2;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 554.

```text
 = 4;
}

message MonthlyBotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10515"></a>
## FND-10515: oneof declaration: chesscom.user_properties.v1.MonthlyBotEventProperty._milestones_achieved

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _milestones_achieved {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 578.

```text
BotEventProperty {
  oneof _key {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10516"></a>
## FND-10516: chesscom.user_properties.v1.MonthlyBotEventProperty.milestones_achieved = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 milestones_achieved = 3;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 609.

```text
 {
  string key = 1;
  }
  oneof _points {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10517"></a>
## FND-10517: oneof declaration: chesscom.user_properties.v1.MonthlyBotEventProperty._last_progression_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_progression_at {

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 646.

```text
nts {
  int32 points = 2;
  }
  oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10518"></a>
## FND-10518: chesscom.user_properties.v1.MonthlyBotEventProperty.last_progression_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_progression_at = 4;

### Evidence

- **SRC-0615** `research/proto/chesscom/user_properties/v1/properties_monthly_bot_event.proto` — [preserved redacted evidence](../evidence/text/7c41f0756f727b80276b7f5f319ff22a2e106b071d296c05830f8d09d1eb7db6.proto)
  Character offset 677.

```text
 oneof _milestones_achieved {
  int32 milestones_achieved = 3;
  }
  oneof _last_progression_at {
  .google.protobuf.Timestamp last_progression_at = 4;
  }
}

```

**Source references:** SRC-0615, SRC-1586  
**URL references:** None independently associated  
**Related findings:** FND-10504, FND-10505, FND-10506

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10519"></a>
## FND-10519: enum declaration: chesscom.user_properties.v1.NavbarPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum NavbarPropertyDefinition {

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 120.

```text
user_properties/v1/properties_navbar.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum NavbarPropertyDefinition {
  NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  NAVBAR_PROPERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10520, FND-10521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10520"></a>
## FND-10520: chesscom.user_properties.v1.NavbarPropertyDefinition.NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 154.

```text
ar.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum NavbarPropertyDefinition {
  NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  NAVBAR_PROPERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10521"></a>
## FND-10521: chesscom.user_properties.v1.NavbarPropertyDefinition.NAVBAR_PROPERTY_DEFINITION_PINS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NAVBAR_PROPERTY_DEFINITION_PINS = 1;

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 200.

```text
ser_properties.v1;

enum NavbarPropertyDefinition {
  NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  NAVBAR_PROPERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10520

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10522"></a>
## FND-10522: chesscom.user_properties.v1.NavbarPropertyDefinition.NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 239.

```text
Definition {
  NAVBAR_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  NAVBAR_PROPERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10520, FND-10521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10523"></a>
## FND-10523: message declaration: chesscom.user_properties.v1.NavbarProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NavbarProperty {

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 284.

```text
PECIFIED = 0;
  NAVBAR_PROPERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10520, FND-10521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10524"></a>
## FND-10524: chesscom.user_properties.v1.NavbarProperty.pins = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string pins = 1;

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 311.

```text
ERTY_DEFINITION_PINS = 1;
  NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10520, FND-10521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10525"></a>
## FND-10525: chesscom.user_properties.v1.NavbarProperty.favorites = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string favorites = 2;

### Evidence

- **SRC-0616** `research/proto/chesscom/user_properties/v1/properties_navbar.proto` — [preserved redacted evidence](../evidence/text/9d1b69156e82a8f9b951c07ffd0aec097563e79fd4370e12289245069a9465ae.proto)
  Character offset 339.

```text
NAVBAR_PROPERTY_DEFINITION_FAVORITES = 2;
}

message NavbarProperty {
  repeated string pins = 1;
  repeated string favorites = 2;
}

```

**Source references:** SRC-0616, SRC-1587  
**URL references:** None independently associated  
**Related findings:** FND-10519, FND-10520, FND-10521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10526"></a>
## FND-10526: enum declaration: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum OpeningCoursesPropertyDefinition {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 129.

```text
erties/v1/properties_opening_courses.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum OpeningCoursesPropertyDefinition {
  OPENING_COURSES_PROPERTY_UNSPECIFIED = 0;
  FIRST_OPENING_COURSES_SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10527"></a>
## FND-10527: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.OPENING_COURSES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OPENING_COURSES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 171.

```text

// syntax: proto3

package chesscom.user_properties.v1;

enum OpeningCoursesPropertyDefinition {
  OPENING_COURSES_PROPERTY_UNSPECIFIED = 0;
  FIRST_OPENING_COURSES_SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10528"></a>
## FND-10528: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.FIRST_OPENING_COURSES_SESSION_DATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIRST_OPENING_COURSES_SESSION_DATE = 1;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 215.

```text
operties.v1;

enum OpeningCoursesPropertyDefinition {
  OPENING_COURSES_PROPERTY_UNSPECIFIED = 0;
  FIRST_OPENING_COURSES_SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUM
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10529"></a>
## FND-10529: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.LAST_OPENING_COURSES_SESSION_DATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPENING_COURSES_SESSION_DATE = 2;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 257.

```text
efinition {
  OPENING_COURSES_PROPERTY_UNSPECIFIED = 0;
  FIRST_OPENING_COURSES_SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NU
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10530"></a>
## FND-10530: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.LAST_OPENING_COURSES_STUDY_DATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_OPENING_COURSES_STUDY_DATE = 3;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 298.

```text
SPECIFIED = 0;
  FIRST_OPENING_COURSES_SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HIT
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10531"></a>
## FND-10531: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 337.

```text
SESSION_DATE = 1;
  LAST_OPENING_COURSES_SESSION_DATE = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREV
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10532"></a>
## FND-10532: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 389.

```text
E = 2;
  LAST_OPENING_COURSES_STUDY_DATE = 3;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10533"></a>
## FND-10533: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 442.

```text
R_OF_OPENING_COURSES_VARIATIONS_LEARNED = 4;
  NUMBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .g
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10534"></a>
## FND-10534: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_STARTED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_STARTED = 7;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 491.

```text
MBER_OF_OPENING_COURSES_VARIATIONS_REVIEWED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_se
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10535"></a>
## FND-10535: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_COMPLETED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_COMPLETED = 8;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 532.

```text
ED = 5;
  NUMBER_OF_OPENING_COURSES_REVIEWS_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10536"></a>
## FND-10536: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 575.

```text
_PENDING = 6;
  NUMBER_OF_OPENING_COURSES_STARTED = 7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10537"></a>
## FND-10537: chesscom.user_properties.v1.OpeningCoursesPropertyDefinition.NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 627.

```text
7;
  NUMBER_OF_OPENING_COURSES_COMPLETED = 8;
  NUMBER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10538"></a>
## FND-10538: message declaration: chesscom.user_properties.v1.OpeningCoursesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OpeningCoursesProperty {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 679.

```text
ER_OF_OPENING_COURSES_FEATURE_LIMIT_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .googl
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10539"></a>
## FND-10539: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._first_opening_courses_session_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_opening_courses_session_date {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 714.

```text
_HITS = 9;
  NUMBER_OF_OPENING_COURSES_PREVIEWS_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_c
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10540"></a>
## FND-10540: chesscom.user_properties.v1.OpeningCoursesProperty.first_opening_courses_session_date = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp first_opening_courses_session_date = 1;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 760.

```text
S_CLAIMED = 10;
}

message OpeningCoursesProperty {
  oneof _first_opening_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10541"></a>
## FND-10541: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._last_opening_courses_session_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_opening_courses_session_date {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 833.

```text
g_courses_session_date {
  .google.protobuf.Timestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_va
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10542"></a>
## FND-10542: chesscom.user_properties.v1.OpeningCoursesProperty.last_opening_courses_session_date = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_opening_courses_session_date = 2;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 878.

```text
imestamp first_opening_courses_session_date = 1;
  }
  oneof _last_opening_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10543"></a>
## FND-10543: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._last_opening_courses_study_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_opening_courses_study_date {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 950.

```text
ng_courses_session_date {
  .google.protobuf.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10544"></a>
## FND-10544: chesscom.user_properties.v1.OpeningCoursesProperty.last_opening_courses_study_date = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_opening_courses_study_date = 3;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 993.

```text
f.Timestamp last_opening_courses_session_date = 2;
  }
  oneof _last_opening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _numbe
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10545"></a>
## FND-10545: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_variations_learned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_variations_learned {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1063.

```text
pening_courses_study_date {
  .google.protobuf.Timestamp last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_cours
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10546"></a>
## FND-10546: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_variations_learned = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_variations_learned = 4;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1119.

```text
 last_opening_courses_study_date = 3;
  }
  oneof _number_of_opening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_c
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10547"></a>
## FND-10547: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_variations_reviewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_variations_reviewed {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1181.

```text
pening_courses_variations_learned {
  int32 number_of_opening_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10548"></a>
## FND-10548: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_variations_reviewed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_variations_reviewed = 5;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1238.

```text
ning_courses_variations_learned = 4;
  }
  oneof _number_of_opening_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  in
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10549"></a>
## FND-10549: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_reviews_pending

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_reviews_pending {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1301.

```text
ning_courses_variations_reviewed {
  int32 number_of_opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _numbe
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10550"></a>
## FND-10550: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_reviews_pending = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_reviews_pending = 6;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1354.

```text
opening_courses_variations_reviewed = 5;
  }
  oneof _number_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 num
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10551"></a>
## FND-10551: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_started

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_started {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1413.

```text
r_of_opening_courses_reviews_pending {
  int32 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof 
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10552"></a>
## FND-10552: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_started = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_started = 7;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1458.

```text
2 number_of_opening_courses_reviews_pending = 6;
  }
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10553"></a>
## FND-10553: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_completed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_completed {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1509.

```text
}
  oneof _number_of_opening_courses_started {
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed
```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10554"></a>
## FND-10554: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_completed = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_completed = 8;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1556.

```text
  int32 number_of_opening_courses_started = 7;
  }
  oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed = 10;
  }
}

```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10555"></a>
## FND-10555: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_feature_limit_hits

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_feature_limit_hits {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1609.

```text
oneof _number_of_opening_courses_completed {
  int32 number_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed = 10;
  }
}

```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10556"></a>
## FND-10556: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_feature_limit_hits = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_feature_limit_hits = 9;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1665.

```text
ber_of_opening_courses_completed = 8;
  }
  oneof _number_of_opening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed = 10;
  }
}

```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10557"></a>
## FND-10557: oneof declaration: chesscom.user_properties.v1.OpeningCoursesProperty._number_of_opening_courses_previews_claimed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _number_of_opening_courses_previews_claimed {

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1727.

```text
pening_courses_feature_limit_hits {
  int32 number_of_opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed = 10;
  }
}

```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10558"></a>
## FND-10558: chesscom.user_properties.v1.OpeningCoursesProperty.number_of_opening_courses_previews_claimed = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 number_of_opening_courses_previews_claimed = 10;

### Evidence

- **SRC-0617** `research/proto/chesscom/user_properties/v1/properties_opening_courses.proto` — [preserved redacted evidence](../evidence/text/dc1c7c667a1474f3e818dcd133c83fadb80a559a5ff7c48ff99c66b5eb839d16.proto)
  Character offset 1781.

```text
opening_courses_feature_limit_hits = 9;
  }
  oneof _number_of_opening_courses_previews_claimed {
  int32 number_of_opening_courses_previews_claimed = 10;
  }
}

```

**Source references:** SRC-0617, SRC-1588  
**URL references:** None independently associated  
**Related findings:** FND-10526, FND-10527, FND-10528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10559"></a>
## FND-10559: enum declaration: chesscom.user_properties.v1.PIIPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PIIPropertyDefinition {

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 117.

```text
om/user_properties/v1/properties_pii.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PIIPropertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PA
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10560"></a>
## FND-10560: chesscom.user_properties.v1.PIIPropertyDefinition.PII_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PII_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 148.

```text
s_pii.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum PIIPropertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_C
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10561"></a>
## FND-10561: chesscom.user_properties.v1.PIIPropertyDefinition.EMAIL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EMAIL = 1;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 180.

```text
ackage chesscom.user_properties.v1;

enum PIIPropertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10562"></a>
## FND-10562: chesscom.user_properties.v1.PIIPropertyDefinition.FIRST_NAME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FIRST_NAME = 2;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 193.

```text
om.user_properties.v1;

enum PIIPropertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10563"></a>
## FND-10563: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_NAME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_NAME = 3;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 211.

```text
.v1;

enum PIIPropertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUM
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10564"></a>
## FND-10564: chesscom.user_properties.v1.PIIPropertyDefinition.COUNTRY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COUNTRY = 4;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 228.

```text
pertyDefinition {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVI
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10565"></a>
## FND-10565: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_COUNTRY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_COUNTRY = 5;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 243.

```text
 {
  PII_PROPERTY_UNSPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBE
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10566"></a>
## FND-10566: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_IP_ADDRESS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_IP_ADDRESS = 6;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 263.

```text
SPECIFIED = 0;
  EMAIL = 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
  LAST_LATITUDE = 11;
  LAST_LONGITUDE = 12;
  PREVIOUS_EMAILS = 13;
  PAYMENT_COUNTRY = 14;
  PAYMENT_COUNTRY_CONFIDENCE_LEVEL = 15;
  PAYPAL_EMAILS = 16;
  PHONE_NUMBER = 17;
  PREVIOUS_PHONE_NUMBERS = 18;
  USCF_ID =
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10567"></a>
## FND-10567: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_TIMEZONE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_TIMEZONE = 7;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 286.

```text
= 1;
  FIRST_NAME = 2;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10568"></a>
## FND-10568: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_CONTINENT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CONTINENT = 8;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 307.

```text
;
  LAST_NAME = 3;
  COUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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

message PIIProperty 
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10569"></a>
## FND-10569: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_CITY = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CITY = 9;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 329.

```text
OUNTRY = 4;
  LAST_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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
  s
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10570"></a>
## FND-10570: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_REGION = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_REGION = 10;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 346.

```text
T_COUNTRY = 5;
  LAST_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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

```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10571"></a>
## FND-10571: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_LATITUDE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_LATITUDE = 11;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 366.

```text
T_IP_ADDRESS = 6;
  LAST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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
  oneof _first_n
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10572"></a>
## FND-10572: chesscom.user_properties.v1.PIIPropertyDefinition.LAST_LONGITUDE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_LONGITUDE = 12;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 388.

```text
ST_TIMEZONE = 7;
  LAST_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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
  string first_n
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10573"></a>
## FND-10573: chesscom.user_properties.v1.PIIPropertyDefinition.PREVIOUS_EMAILS = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREVIOUS_EMAILS = 13;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 411.

```text
_CONTINENT = 8;
  LAST_CITY = 9;
  LAST_REGION = 10;
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
  oneof _l
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10574"></a>
## FND-10574: chesscom.user_properties.v1.PIIPropertyDefinition.PAYMENT_COUNTRY = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PAYMENT_COUNTRY = 14;

### Evidence

- **SRC-0618** `research/proto/chesscom/user_properties/v1/properties_pii.proto` — [preserved redacted evidence](../evidence/text/35904cd7f60fbab3b13f4978c55fd30506809652bb6b0fc8435153863f837e58.proto)
  Character offset 435.

```text
ITY = 9;
  LAST_REGION = 10;
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
  string last
```

**Source references:** SRC-0618, SRC-1589  
**URL references:** None independently associated  
**Related findings:** FND-10559, FND-10560, FND-10561

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
