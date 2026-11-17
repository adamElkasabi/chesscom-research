# data_models — findings 10101–10200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10375"></a>
## FND-10375: chesscom.user_properties.v1.PropertyPermissionLevel.PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 298.

```text
NGE = 1;
  RANGE_MODIFIER_CEIL = 2;
  RANGE_MODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10376"></a>
## FND-10376: chesscom.user_properties.v1.PropertyPermissionLevel.PROPERTY_PERMISSION_LEVEL_PRIVATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 343.

```text
ODIFIER_FLOOR = 3;
}

enum PropertyPermissionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10377"></a>
## FND-10377: chesscom.user_properties.v1.PropertyPermissionLevel.PROPERTY_PERMISSION_LEVEL_SELF = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROPERTY_PERMISSION_LEVEL_SELF = 2;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 384.

```text
sionLevel {
  PROPERTY_PERMISSION_LEVEL_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransform
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10378"></a>
## FND-10378: chesscom.user_properties.v1.PropertyPermissionLevel.PROPERTY_PERMISSION_LEVEL_FRIENDS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 422.

```text
L_UNSPECIFIED = 0;
  PROPERTY_PERMISSION_LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10379"></a>
## FND-10379: chesscom.user_properties.v1.PropertyPermissionLevel.PROPERTY_PERMISSION_LEVEL_PUBLIC = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 463.

```text
LEVEL_PRIVATE = 1;
  PROPERTY_PERMISSION_LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name =
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10380"></a>
## FND-10380: message declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertyDefinitionMetadata {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 504.

```text
LEVEL_SELF = 2;
  PROPERTY_PERMISSION_LEVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10381"></a>
## FND-10381: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata.user_activity_enrichment_transformer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof user_activity_enrichment_transformer {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 543.

```text
EVEL_FRIENDS = 3;
  PROPERTY_PERMISSION_LEVEL_PUBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10382"></a>
## FND-10382: chesscom.user_properties.v1.PropertyDefinitionMetadata.range_transformer = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RangeTransformer range_transformer = 11;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 590.

```text
UBLIC = 4;
}

message PropertyDefinitionMetadata {
  oneof user_activity_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10383"></a>
## FND-10383: chesscom.user_properties.v1.PropertyDefinitionMetadata.year_transformer = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.YearTransformer year_transformer = 12;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 662.

```text
_enrichment_transformer {
  .chesscom.user_properties.v1.RangeTransformer range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _rep
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10384"></a>
## FND-10384: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._property_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _property_name {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 736.

```text
range_transformer = 11;
  .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10385"></a>
## FND-10385: chesscom.user_properties.v1.PropertyDefinitionMetadata.property_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string property_name = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 761.

```text
 .chesscom.user_properties.v1.YearTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timest
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10386"></a>
## FND-10386: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._property_name_suffix

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _property_name_suffix {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 793.

```text
arTransformer year_transformer = 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10387"></a>
## FND-10387: chesscom.user_properties.v1.PropertyDefinitionMetadata.property_name_suffix = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string property_name_suffix = 2;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 825.

```text
 12;
  }
  oneof _property_name {
  string property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_pr
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10388"></a>
## FND-10388: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._description

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _description {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 864.

```text
ing property_name = 1;
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_leve
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10389"></a>
## FND-10389: chesscom.user_properties.v1.PropertyDefinitionMetadata.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string description = 3;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 887.

```text
  }
  oneof _property_name_suffix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_pr
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10390"></a>
## FND-10390: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._is_backfilled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_backfilled {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 917.

```text
fix {
  string property_name_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermission
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10391"></a>
## FND-10391: chesscom.user_properties.v1.PropertyDefinitionMetadata.is_backfilled = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_backfilled = 4;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 942.

```text
ame_suffix = 2;
  }
  oneof _description {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10392"></a>
## FND-10392: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._repeated_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _repeated_limit {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 972.

```text
escription {
  string description = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10393"></a>
## FND-10393: chesscom.user_properties.v1.PropertyDefinitionMetadata.repeated_limit = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 repeated_limit = 5;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 998.

```text
ription = 3;
  }
  oneof _is_backfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10394"></a>
## FND-10394: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._deprecation_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _deprecation_date {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1030.

```text
kfilled {
  bool is_backfilled = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10395"></a>
## FND-10395: chesscom.user_properties.v1.PropertyDefinitionMetadata.deprecation_date = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp deprecation_date = 7;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1058.

```text
ed = 4;
  }
  oneof _repeated_limit {
  int32 repeated_limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repea
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10396"></a>
## FND-10396: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._is_private

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_private {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1113.

```text
limit = 5;
  }
  oneof _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10397"></a>
## FND-10397: chesscom.user_properties.v1.PropertyDefinitionMetadata.is_private = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_private = 8;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1135.

```text
 _deprecation_date {
  .google.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10398"></a>
## FND-10398: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._permission_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _permission_level {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1162.

```text
gle.protobuf.Timestamp deprecation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10399"></a>
## FND-10399: chesscom.user_properties.v1.PropertyDefinitionMetadata.permission_level = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1190.

```text
cation_date = 7;
  }
  oneof _is_private {
  bool is_private = 8;
  }
  oneof _permission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_p
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10400"></a>
## FND-10400: oneof declaration: chesscom.user_properties.v1.PropertyDefinitionMetadata._user_activity_enrichment_field_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_activity_enrichment_field_name {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1271.

```text
rmission_level {
  .chesscom.user_properties.v1.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

messa
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10401"></a>
## FND-10401: chesscom.user_properties.v1.PropertyDefinitionMetadata.user_activity_enrichment_field_name = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_activity_enrichment_field_name = 10;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1318.

```text
.PropertyPermissionLevel permission_level = 9;
  }
  oneof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransfo
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10402"></a>
## FND-10402: chesscom.user_properties.v1.PropertyDefinitionMetadata.destination = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.Destination destination = 6;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1373.

```text
eof _user_activity_enrichment_field_name {
  string user_activity_enrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_prope
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10403"></a>
## FND-10403: chesscom.user_properties.v1.PropertyDefinitionMetadata.event_name_allowlist = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string event_name_allowlist = 13;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1440.

```text
nrichment_field_name = 10;
  }
  repeated .chesscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 ra
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10404"></a>
## FND-10404: chesscom.user_properties.v1.PropertyDefinitionMetadata.customizable_views = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1485.

```text
esscom.user_activity.v1.Destination destination = 6;
  repeated string event_name_allowlist = 13;
  repeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

mess
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10405"></a>
## FND-10405: message declaration: chesscom.user_properties.v1.PropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertyDefinition {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1586.

```text
epeated .chesscom.user_properties.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.Allow
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10406"></a>
## FND-10406: message declaration: chesscom.user_properties.v1.RangeTransformer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RangeTransformer {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1618.

```text
s.v1.PropertyPermissionCustomizableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist 
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10407"></a>
## FND-10407: oneof declaration: chesscom.user_properties.v1.RangeTransformer._range_modifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _range_modifier {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1647.

```text
izableView customizable_views = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10408"></a>
## FND-10408: chesscom.user_properties.v1.RangeTransformer.range_modifier = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RangeModifier range_modifier = 2;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1673.

```text
ews = 14;
}

message PropertyDefinition {
}

message RangeTransformer {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.Proper
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10409"></a>
## FND-10409: chesscom.user_properties.v1.RangeTransformer.range = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 range = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1742.

```text
 {
  oneof _range_modifier {
  .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10410"></a>
## FND-10410: message declaration: chesscom.user_properties.v1.YearTransformer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message YearTransformer {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1772.

```text
 .chesscom.user_properties.v1.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10411"></a>
## FND-10411: message declaration: chesscom.user_properties.v1.PropertyPermissionCustomizableView

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertyPermissionCustomizableView {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1801.

```text
.RangeModifier range_modifier = 2;
  }
  optional uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10412"></a>
## FND-10412: oneof declaration: chesscom.user_properties.v1.PropertyPermissionCustomizableView.customization

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof customization {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1848.

```text
al uint32 range = 1;
}

message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10413"></a>
## FND-10413: chesscom.user_properties.v1.PropertyPermissionCustomizableView.allowlist = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1872.

```text
message YearTransformer {
}

message PropertyPermissionCustomizableView {
  oneof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10414"></a>
## FND-10414: chesscom.user_properties.v1.PropertyPermissionCustomizableView.levels = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 1949.

```text
neof customization {
  .chesscom.user_properties.v1.AllowlistViewCustomization allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10415"></a>
## FND-10415: message declaration: chesscom.user_properties.v1.AllowlistViewCustomization

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AllowlistViewCustomization {

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 2026.

```text
n allowlist = 2;
  }
  repeated .chesscom.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10416"></a>
## FND-10416: chesscom.user_properties.v1.AllowlistViewCustomization.values = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string values = 1;

### Evidence

- **SRC-0610** `research/proto/chesscom/user_properties/v1/properties_definition.proto` — [preserved redacted evidence](../evidence/text/fba0afc3256333df299791501314971528c970d04278eb6663e8c09965e580b4.proto)
  Character offset 2065.

```text
om.user_properties.v1.PropertyPermissionLevel levels = 1;
}

message AllowlistViewCustomization {
  repeated string values = 1;
}

```

**Source references:** SRC-0610, SRC-1581  
**URL references:** None independently associated  
**Related findings:** FND-10369, FND-10370, FND-10371

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10417"></a>
## FND-10417: enum declaration: chesscom.user_properties.v1.FairPlayPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FairPlayPropertyDefinition {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 123.

```text
r_properties/v1/properties_fair_play.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum FairPlayPropertyDefinition {
  FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10418"></a>
## FND-10418: chesscom.user_properties.v1.FairPlayPropertyDefinition.FAIR_PLAY_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 159.

```text
.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum FairPlayPropertyDefinition {
  FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Ti
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10419"></a>
## FND-10419: chesscom.user_properties.v1.FairPlayPropertyDefinition.CHEAT_REPORT_COUNT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHEAT_REPORT_COUNT = 1;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 197.

```text
scom.user_properties.v1;

enum FairPlayPropertyDefinition {
  FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10420"></a>
## FND-10420: chesscom.user_properties.v1.FairPlayPropertyDefinition.LAST_CHEAT_REPORT_DATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST_CHEAT_REPORT_DATE = 2;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 223.

```text
enum FairPlayPropertyDefinition {
  FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10421"></a>
## FND-10421: chesscom.user_properties.v1.FairPlayPropertyDefinition.PREVIOUS_CHANCE_USER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREVIOUS_CHANCE_USER = 3;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 253.

```text
n {
  FAIR_PLAY_PROPERTY_UNSPECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chan
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10422"></a>
## FND-10422: chesscom.user_properties.v1.FairPlayPropertyDefinition.NEXT_CHANCE_USER = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NEXT_CHANCE_USER = 4;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 281.

```text
PECIFIED = 0;
  CHEAT_REPORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _ne
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10423"></a>
## FND-10423: chesscom.user_properties.v1.FairPlayPropertyDefinition.SECOND_CHANCE_TAG = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SECOND_CHANCE_TAG = 5;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 305.

```text
PORT_COUNT = 1;
  LAST_CHEAT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  strin
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10424"></a>
## FND-10424: message declaration: chesscom.user_properties.v1.FairPlayProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FairPlayProperty {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 331.

```text
AT_REPORT_DATE = 2;
  PREVIOUS_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10425"></a>
## FND-10425: oneof declaration: chesscom.user_properties.v1.FairPlayProperty._cheat_report_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _cheat_report_count {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 360.

```text
S_CHANCE_USER = 3;
  NEXT_CHANCE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag 
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10426"></a>
## FND-10426: chesscom.user_properties.v1.FairPlayProperty.cheat_report_count = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 cheat_report_count = 1;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 390.

```text
CE_USER = 4;
  SECOND_CHANCE_TAG = 5;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag =
```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10427"></a>
## FND-10427: oneof declaration: chesscom.user_properties.v1.FairPlayProperty._last_cheat_report_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_cheat_report_date {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 426.

```text
;
}

message FairPlayProperty {
  oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10428"></a>
## FND-10428: chesscom.user_properties.v1.FairPlayProperty.last_cheat_report_date = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_cheat_report_date = 2;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 460.

```text
oneof _cheat_report_count {
  int32 cheat_report_count = 1;
  }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10429"></a>
## FND-10429: oneof declaration: chesscom.user_properties.v1.FairPlayProperty._previous_chance_user

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _previous_chance_user {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 521.

```text
 }
  oneof _last_cheat_report_date {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10430"></a>
## FND-10430: chesscom.user_properties.v1.FairPlayProperty.previous_chance_user = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string previous_chance_user = 3;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 553.

```text
te {
  .google.protobuf.Timestamp last_cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10431"></a>
## FND-10431: oneof declaration: chesscom.user_properties.v1.FairPlayProperty._next_chance_user

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _next_chance_user {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 592.

```text
cheat_report_date = 2;
  }
  oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10432"></a>
## FND-10432: chesscom.user_properties.v1.FairPlayProperty.next_chance_user = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string next_chance_user = 4;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 620.

```text
 oneof _previous_chance_user {
  string previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10433"></a>
## FND-10433: oneof declaration: chesscom.user_properties.v1.FairPlayProperty._second_chance_tag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _second_chance_tag {

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 655.

```text
ring previous_chance_user = 3;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10434"></a>
## FND-10434: chesscom.user_properties.v1.FairPlayProperty.second_chance_tag = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string second_chance_tag = 5;

### Evidence

- **SRC-0611** `research/proto/chesscom/user_properties/v1/properties_fair_play.proto` — [preserved redacted evidence](../evidence/text/9e17f92c773b4b1bc7cdcdd87e7025a8e5b2b12178b86765af3ea07312780637.proto)
  Character offset 684.

```text
;
  }
  oneof _next_chance_user {
  string next_chance_user = 4;
  }
  oneof _second_chance_tag {
  string second_chance_tag = 5;
  }
}

```

**Source references:** SRC-0611, SRC-1582  
**URL references:** None independently associated  
**Related findings:** FND-10417, FND-10418, FND-10419

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10435"></a>
## FND-10435: enum declaration: chesscom.user_properties.v1.GrowthPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GrowthPropertyDefinition {

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 120.

```text
user_properties/v1/properties_growth.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum GrowthPropertyDefinition {
  GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10436"></a>
## FND-10436: chesscom.user_properties.v1.GrowthPropertyDefinition.GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 154.

```text
th.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum GrowthPropertyDefinition {
  GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state 
```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10437"></a>
## FND-10437: chesscom.user_properties.v1.GrowthPropertyDefinition.GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 200.

```text
ser_properties.v1;

enum GrowthPropertyDefinition {
  GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  one
```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10438"></a>
## FND-10438: chesscom.user_properties.v1.GrowthPropertyDefinition.GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 249.

```text
 {
  GROWTH_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Tim
```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10439"></a>
## FND-10439: chesscom.user_properties.v1.GrowthPropertyDefinition.GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 304.

```text
TH_PROPERTY_DEFINITION_MOMENTUM_STATE = 1;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10440"></a>
## FND-10440: message declaration: chesscom.user_properties.v1.GrowthProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GrowthProperty {

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 360.

```text
ERTY_DEFINITION_MOMENTUM_PRIOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10441"></a>
## FND-10441: oneof declaration: chesscom.user_properties.v1.GrowthProperty._momentum_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _momentum_state {

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 387.

```text
IOR_STATE = 2;
  GROWTH_PROPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10442"></a>
## FND-10442: chesscom.user_properties.v1.GrowthProperty.momentum_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string momentum_state = 1;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 413.

```text
OPERTY_DEFINITION_MOMENTUM_COMPUTED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10443"></a>
## FND-10443: oneof declaration: chesscom.user_properties.v1.GrowthProperty._momentum_prior_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _momentum_prior_state {

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 446.

```text
ED_AT = 3;
}

message GrowthProperty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10444"></a>
## FND-10444: chesscom.user_properties.v1.GrowthProperty.momentum_prior_state = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string momentum_prior_state = 2;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 478.

```text
erty {
  oneof _momentum_state {
  string momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10445"></a>
## FND-10445: oneof declaration: chesscom.user_properties.v1.GrowthProperty._momentum_computed_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _momentum_computed_at {

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 517.

```text
ng momentum_state = 1;
  }
  oneof _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10446"></a>
## FND-10446: chesscom.user_properties.v1.GrowthProperty.momentum_computed_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp momentum_computed_at = 3;

### Evidence

- **SRC-0612** `research/proto/chesscom/user_properties/v1/properties_growth.proto` — [preserved redacted evidence](../evidence/text/e2c2fa3e2c8133dfc7827827d41504b9b0a5b52f3aff1fc96fe62d8d342d4e22.proto)
  Character offset 549.

```text
of _momentum_prior_state {
  string momentum_prior_state = 2;
  }
  oneof _momentum_computed_at {
  .google.protobuf.Timestamp momentum_computed_at = 3;
  }
}

```

**Source references:** SRC-0612, SRC-1583  
**URL references:** None independently associated  
**Related findings:** FND-10435, FND-10436, FND-10437

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10447"></a>
## FND-10447: enum declaration: chesscom.user_properties.v1.IpqsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IpqsPropertyDefinition {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 118.

```text
m/user_properties/v1/properties_ipqs.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum IpqsPropertyDefinition {
  IPQS_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SC
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10448"></a>
## FND-10448: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_UNSPECIFIED = 0;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 150.

```text
ipqs.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum IpqsPropertyDefinition {
  IPQS_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_R
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10449"></a>
## FND-10449: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_FRAUD_SCORE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_FRAUD_SCORE = 1;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 174.

```text
oto3

package chesscom.user_properties.v1;

enum IpqsPropertyDefinition {
  IPQS_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10450"></a>
## FND-10450: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_LOW_QUALITY_EMAIL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_LOW_QUALITY_EMAIL = 2;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 198.

```text
ser_properties.v1;

enum IpqsPropertyDefinition {
  IPQS_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10451"></a>
## FND-10451: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_FIRST_SEEN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_FIRST_SEEN = 3;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 231.

```text
ertyDefinition {
  IPQS_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10452"></a>
## FND-10452: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_BOT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_BOT = 4;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 254.

```text
_UNSPECIFIED = 0;
  IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10453"></a>
## FND-10453: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_PROXY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_PROXY = 5;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 273.

```text
 IPQS_FRAUD_SCORE = 1;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10454"></a>
## FND-10454: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_KNOWN_ATTACKER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_KNOWN_ATTACKER = 6;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 294.

```text
;
  IPQS_IS_LOW_QUALITY_EMAIL = 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bo
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10455"></a>
## FND-10455: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_ABUSE_VELOCITY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_ABUSE_VELOCITY = 7;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 324.

```text
= 2;
  IPQS_FIRST_SEEN = 3;
  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email =
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10456"></a>
## FND-10456: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_HAS_ABUSED_RECENTLY = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_HAS_ABUSED_RECENTLY = 8;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 351.

```text

  IPQS_IS_BOT = 4;
  IPQS_IS_PROXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10457"></a>
## FND-10457: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_VPN = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_VPN = 9;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 383.

```text
OXY = 5;
  IPQS_IS_KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Times
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10458"></a>
## FND-10458: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IS_TOR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IS_TOR = 10;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 402.

```text
KNOWN_ATTACKER = 6;
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_see
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10459"></a>
## FND-10459: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IP_FRAUD_SCORE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IP_FRAUD_SCORE = 11;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 422.

```text
  IPQS_ABUSE_VELOCITY = 7;
  IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10460"></a>
## FND-10460: chesscom.user_properties.v1.IpqsPropertyDefinition.IPQS_IP_HAS_ABUSED_RECENTLY = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IPQS_IP_HAS_ABUSED_RECENTLY = 12;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 450.

```text
 IPQS_HAS_ABUSED_RECENTLY = 8;
  IPQS_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10461"></a>
## FND-10461: message declaration: chesscom.user_properties.v1.IpqsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IpqsProperty {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 487.

```text
_IS_VPN = 9;
  IPQS_IS_TOR = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10462"></a>
## FND-10462: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_fraud_score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_fraud_score {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 512.

```text
R = 10;
  IPQS_IP_FRAUD_SCORE = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10463"></a>
## FND-10463: chesscom.user_properties.v1.IpqsProperty.ipqs_fraud_score = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double ipqs_fraud_score = 1;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 540.

```text
E = 11;
  IPQS_IP_HAS_ABUSED_RECENTLY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_know
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10464"></a>
## FND-10464: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_low_quality_email

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_low_quality_email {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 575.

```text
LY = 12;
}

message IpqsProperty {
  oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_a
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10465"></a>
## FND-10465: chesscom.user_properties.v1.IpqsProperty.ipqs_is_low_quality_email = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_low_quality_email = 2;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 612.

```text
oneof _ipqs_fraud_score {
  double ipqs_fraud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10466"></a>
## FND-10466: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_first_seen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_first_seen {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 654.

```text
aud_score = 1;
  }
  oneof _ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10467"></a>
## FND-10467: chesscom.user_properties.v1.IpqsProperty.ipqs_first_seen = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp ipqs_first_seen = 3;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 681.

```text
_ipqs_is_low_quality_email {
  bool ipqs_is_low_quality_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_ab
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10468"></a>
## FND-10468: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_bot

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_bot {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 735.

```text
y_email = 2;
  }
  oneof _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10469"></a>
## FND-10469: chesscom.user_properties.v1.IpqsProperty.ipqs_is_bot = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_bot = 4;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 758.

```text
f _ipqs_first_seen {
  .google.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
  bool ipqs_is_known_attacker = 6;
  }
  oneof _ipqs_abuse_velocity {
  string ipqs_abuse_velocity = 7;
  }
  oneof _ipqs_has_abused_recently {
  bool ipqs_has_abused_recently = 8;
  }
  oneof _ipqs_is_vpn
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10470"></a>
## FND-10470: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_proxy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_proxy {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 786.

```text
le.protobuf.Timestamp ipqs_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
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
 
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10471"></a>
## FND-10471: chesscom.user_properties.v1.IpqsProperty.ipqs_is_proxy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_proxy = 5;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 811.

```text
s_first_seen = 3;
  }
  oneof _ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
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
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10472"></a>
## FND-10472: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_is_known_attacker

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_is_known_attacker {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 841.

```text
_ipqs_is_bot {
  bool ipqs_is_bot = 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
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

```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10473"></a>
## FND-10473: chesscom.user_properties.v1.IpqsProperty.ipqs_is_known_attacker = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ipqs_is_known_attacker = 6;

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 875.

```text
= 4;
  }
  oneof _ipqs_is_proxy {
  bool ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
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
  d
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10474"></a>
## FND-10474: oneof declaration: chesscom.user_properties.v1.IpqsProperty._ipqs_abuse_velocity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ipqs_abuse_velocity {

### Evidence

- **SRC-0613** `research/proto/chesscom/user_properties/v1/properties_ipqs.proto` — [preserved redacted evidence](../evidence/text/e210fab06becc3e06e78e1a002526c2dbe425341afd3829363b4ebc6e90c86d0.proto)
  Character offset 914.

```text
l ipqs_is_proxy = 5;
  }
  oneof _ipqs_is_known_attacker {
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
  o
```

**Source references:** SRC-0613, SRC-1584  
**URL references:** None independently associated  
**Related findings:** FND-10447, FND-10448, FND-10449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
