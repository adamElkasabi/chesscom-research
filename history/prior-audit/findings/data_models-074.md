# data_models — findings 7301–7400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07575"></a>
## FND-07575: chesscom.proto_options.events.v1.Funnel.FUNNEL_ACTIVITY_FEED = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_ACTIVITY_FEED = 43;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 1973.

```text
 = 38;
  FUNNEL_AWARDS = 39;
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCatego
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07576"></a>
## FND-07576: chesscom.proto_options.events.v1.Funnel.FUNNEL_TRAINABLE = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_TRAINABLE = 44;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2002.

```text
  FUNNEL_UNOCKABLES = 40;
  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07577"></a>
## FND-07577: chesscom.proto_options.events.v1.Funnel.FUNNEL_ANALYSIS = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_ANALYSIS = 45;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2027.

```text

  FUNNEL_EVENTS = 41;
  FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07578"></a>
## FND-07578: chesscom.proto_options.events.v1.Funnel.FUNNEL_YEAR_IN_CHESS = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_YEAR_IN_CHESS = 46;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2051.

```text
 FUNNEL_STATS = 42;
  FUNNEL_ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.Event
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07579"></a>
## FND-07579: chesscom.proto_options.events.v1.Funnel.FUNNEL_UNLOCKABLES = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_UNLOCKABLES = 47;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2080.

```text
ACTIVITY_FEED = 43;
  FUNNEL_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _f
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07580"></a>
## FND-07580: chesscom.proto_options.events.v1.Funnel.FUNNEL_SOCIAL_PLATFORMS = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_SOCIAL_PLATFORMS = 48;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2107.

```text
L_TRAINABLE = 44;
  FUNNEL_ANALYSIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_o
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07581"></a>
## FND-07581: chesscom.proto_options.events.v1.Funnel.FUNNEL_TRAIN = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FUNNEL_TRAIN = 49;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2139.

```text
SIS = 45;
  FUNNEL_YEAR_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel =
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07582"></a>
## FND-07582: message declaration: chesscom.proto_options.events.v1.EventDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventDefinition {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2161.

```text
R_IN_CHESS = 46;
  FUNNEL_UNLOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _inter
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07583"></a>
## FND-07583: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _name {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2189.

```text
LOCKABLES = 47;
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interfa
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07584"></a>
## FND-07584: chesscom.proto_options.events.v1.EventDefinition.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string name = 1;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2205.

```text
  FUNNEL_SOCIAL_PLATFORMS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07585"></a>
## FND-07585: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._category

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _category {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2228.

```text
MS = 48;
  FUNNEL_TRAIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name 
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07586"></a>
## FND-07586: chesscom.proto_options.events.v1.EventDefinition.category = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.EventCategory category = 2;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2248.

```text
AIN = 49;
}

message EventDefinition {
  oneof _name {
  string name = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_n
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07587"></a>
## FND-07587: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _type {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2316.

```text
 = 1;
  }
  oneof _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07588"></a>
## FND-07588: chesscom.proto_options.events.v1.EventDefinition.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.EventType type = 3;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2332.

```text
f _category {
  .chesscom.proto_options.events.v1.EventCategory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _exper
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07589"></a>
## FND-07589: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2392.

```text
ory category = 2;
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  r
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07590"></a>
## FND-07590: chesscom.proto_options.events.v1.EventDefinition.funnel = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 4;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2410.

```text
  }
  oneof _type {
  .chesscom.proto_options.events.v1.EventType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07591"></a>
## FND-07591: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._interface_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _interface_name {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2469.

```text
ntType type = 3;
  }
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEnt
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07592"></a>
## FND-07592: chesscom.proto_options.events.v1.EventDefinition.interface_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string interface_name = 5;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2495.

```text
of _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07593"></a>
## FND-07593: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._element_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _element_name {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2528.

```text
tions.events.v1.Funnel funnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07594"></a>
## FND-07594: chesscom.proto_options.events.v1.EventDefinition.element_name = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string element_name = 6;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2552.

```text
unnel = 4;
  }
  oneof _interface_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key =
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07595"></a>
## FND-07595: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._v1_event_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _v1_event_name {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2583.

```text
ce_name {
  string interface_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07596"></a>
## FND-07596: chesscom.proto_options.events.v1.EventDefinition.v1_event_name = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string v1_event_name = 7;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2608.

```text
ace_name = 5;
  }
  oneof _element_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}


```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07597"></a>
## FND-07597: oneof declaration: chesscom.proto_options.events.v1.EventDefinition._experiment_key_field

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _experiment_key_field {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2640.

```text
nt_name {
  string element_name = 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefiniti
```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07598"></a>
## FND-07598: chesscom.proto_options.events.v1.EventDefinition.experiment_key_field = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string experiment_key_field = 9;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2672.

```text
= 6;
  }
  oneof _v1_event_name {
  string v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07599"></a>
## FND-07599: chesscom.proto_options.events.v1.EventDefinition.static_properties = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2711.

```text
ing v1_event_name = 7;
  }
  oneof _experiment_key_field {
  string experiment_key_field = 9;
  }
  repeated .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07600"></a>
## FND-07600: message declaration: chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StaticPropertiesEntry {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2817.

```text
ed .chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07601"></a>
## FND-07601: chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2851.

```text
v1.EventDefinition.StaticPropertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07602"></a>
## FND-07602: chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2878.

```text
opertiesEntry static_properties = 8;
  message StaticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07603"></a>
## FND-07603: message declaration: chesscom.proto_options.events.v1.ContextExtensionDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ContextExtensionDefinition {

### Evidence

- **SRC-0523** `research/proto/chesscom/proto_options/events/v1/event_options.proto` — [preserved redacted evidence](../evidence/text/816135feea94792f90ec955158bd037a6e102a670511f3ed160e367b164c4111.proto)
  Character offset 2928.

```text
ticPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ContextExtensionDefinition {
}

```

**Source references:** SRC-0523, SRC-1494  
**URL references:** None independently associated  
**Related findings:** FND-07507, FND-07508, FND-07509

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07604"></a>
## FND-07604: enum declaration: chesscom.proto_options.kafka.v1.Duration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Duration {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 124.

```text
o_options/kafka/v1/kafka_options.proto
// syntax: proto3

package chesscom.proto_options.kafka.v1;

enum Duration {
  DURATION_UNSPECIFIED = 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConf
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07605"></a>
## FND-07605: chesscom.proto_options.kafka.v1.Duration.DURATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 142.

```text
/kafka_options.proto
// syntax: proto3

package chesscom.proto_options.kafka.v1;

enum Duration {
  DURATION_UNSPECIFIED = 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07606"></a>
## FND-07606: chesscom.proto_options.kafka.v1.Duration.DURATION_ONE_HOUR = 3600000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_ONE_HOUR = 3600000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 170.

```text
ax: proto3

package chesscom.proto_options.kafka.v1;

enum Duration {
  DURATION_UNSPECIFIED = 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.p
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07607"></a>
## FND-07607: chesscom.proto_options.kafka.v1.Duration.DURATION_TWO_HOURS = 7200000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_TWO_HOURS = 7200000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 201.

```text
oto_options.kafka.v1;

enum Duration {
  DURATION_UNSPECIFIED = 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOpti
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07608"></a>
## FND-07608: chesscom.proto_options.kafka.v1.Duration.DURATION_ONE_DAY = 86400000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_ONE_DAY = 86400000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 233.

```text
tion {
  DURATION_UNSPECIFIED = 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  op
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07609"></a>
## FND-07609: chesscom.proto_options.kafka.v1.Duration.DURATION_THREE_DAYS = 259200000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_THREE_DAYS = 259200000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 264.

```text
 0;
  DURATION_ONE_HOUR = 3600000;
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  opt
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07610"></a>
## FND-07610: chesscom.proto_options.kafka.v1.Duration.DURATION_ONE_WEEK = 604800000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_ONE_WEEK = 604800000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 299.

```text
  DURATION_TWO_HOURS = 7200000;
  DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07611"></a>
## FND-07611: chesscom.proto_options.kafka.v1.Duration.DURATION_TWO_WEEKS = 1209600000

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DURATION_TWO_WEEKS = 1209600000;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 332.

```text
 DURATION_ONE_DAY = 86400000;
  DURATION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07612"></a>
## FND-07612: message declaration: chesscom.proto_options.kafka.v1.KafkaOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message KafkaOptions {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 368.

```text
TION_THREE_DAYS = 259200000;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_sc
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07613"></a>
## FND-07613: chesscom.proto_options.kafka.v1.KafkaOptions.default_config = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 393.

```text
00;
  DURATION_ONE_WEEK = 604800000;
  DURATION_TWO_WEEKS = 1209600000;
}

message KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  mess
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07614"></a>
## FND-07614: chesscom.proto_options.kafka.v1.KafkaOptions.config = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 470.

```text
ssage KafkaOptions {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs default_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07615"></a>
## FND-07615: chesscom.proto_options.kafka.v1.KafkaOptions.chesskid = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool chesskid = 3;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 551.

```text
ault_config = 1;
  repeated .chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.Kafka
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07616"></a>
## FND-07616: chesscom.proto_options.kafka.v1.KafkaOptions.environment_config = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 581.

```text
hesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry config = 2;
  optional bool chesskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07617"></a>
## FND-07617: chesscom.proto_options.kafka.v1.KafkaOptions.skip_schema_registry = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool skip_schema_registry = 5;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 667.

```text
esskid = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_o
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07618"></a>
## FND-07618: message declaration: chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ConfigEntry {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 709.

```text
ions.kafka.v1.KafkaEnvironments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;

```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07619"></a>
## FND-07619: chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 733.

```text
onments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.pro
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07620"></a>
## FND-07620: chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 760.

```text
= 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaCo
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07621"></a>
## FND-07621: message declaration: chesscom.proto_options.kafka.v1.KafkaEnvironments

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message KafkaEnvironments {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 794.

```text
egistry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  opti
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07622"></a>
## FND-07622: chesscom.proto_options.kafka.v1.KafkaEnvironments.prod = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 824.

```text
ntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  optional .chesscom.proto_options.k
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07623"></a>
## FND-07623: chesscom.proto_options.kafka.v1.KafkaEnvironments.sandbox = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 891.

```text
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
 
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07624"></a>
## FND-07624: chesscom.proto_options.kafka.v1.KafkaEnvironments.staging = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 961.

```text
a.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07625"></a>
## FND-07625: chesscom.proto_options.kafka.v1.KafkaEnvironments.chesskid_staging = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1031.

```text
1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_opti
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07626"></a>
## FND-07626: chesscom.proto_options.kafka.v1.KafkaEnvironments.chesskid_prod = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1110.

```text
nfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_staging = 5;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  option
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07627"></a>
## FND-07627: message declaration: chesscom.proto_options.kafka.v1.KafkaConfigs

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message KafkaConfigs {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1187.

```text
hesskid_staging = 5;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  messag
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07628"></a>
## FND-07628: chesscom.proto_options.kafka.v1.KafkaConfigs.retention_ms = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 retention_ms = 1;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1212.

```text
tional .chesscom.proto_options.kafka.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07629"></a>
## FND-07629: chesscom.proto_options.kafka.v1.KafkaConfigs.cleanup_policy = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cleanup_policy = 2;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1247.

```text
a.v1.KafkaConfigs chesskid_prod = 6;
}

message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
  optional string key = 1;
  optio
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07630"></a>
## FND-07630: chesscom.proto_options.kafka.v1.KafkaConfigs.num_partitions = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 num_partitions = 3;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1285.

```text


message KafkaConfigs {
  optional int32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07631"></a>
## FND-07631: chesscom.proto_options.kafka.v1.KafkaConfigs.additional_config = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1322.

```text
nt32 retention_ms = 1;
  optional string cleanup_policy = 2;
  optional int32 num_partitions = 3;
  repeated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07632"></a>
## FND-07632: chesscom.proto_options.kafka.v1.KafkaConfigs.retention_duration = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1424.

```text
peated .chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry additional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07633"></a>
## FND-07633: message declaration: chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdditionalConfigEntry {

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 1501.

```text
ditional_config = 4;
  optional .chesscom.proto_options.kafka.v1.Duration retention_duration = 5;
  message AdditionalConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07634"></a>
## FND-07634: chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 733.

```text
onments environment_config = 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.pro
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07635"></a>
## FND-07635: chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0524** `research/proto/chesscom/proto_options/kafka/v1/kafka_options.proto` — [preserved redacted evidence](../evidence/text/01c5e8cc9ab202545bcf893dd0f7fe5ab1f5621a1d68eb18663cdce76490c1c7.proto)
  Character offset 760.

```text
= 4;
  optional bool skip_schema_registry = 5;
  message ConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message KafkaEnvironments {
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs prod = 1;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs sandbox = 2;
  optional .chesscom.proto_options.kafka.v1.KafkaConfigs staging = 3;
  optional .chesscom.proto_options.kafka.v1.KafkaCo
```

**Source references:** SRC-0524, SRC-1495  
**URL references:** None independently associated  
**Related findings:** FND-07604, FND-07605, FND-07606

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07636"></a>
## FND-07636: enum declaration: chesscom.proto_options.manifest.v1.ClientHash

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ClientHash {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 128.

```text
tions/manifest/v1/annotations.proto
// syntax: proto3

package chesscom.proto_options.manifest.v1;

enum ClientHash {
  CLIENT_HASH_UNSPECIFIED = 0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cl
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07637"></a>
## FND-07637: chesscom.proto_options.manifest.v1.ClientHash.CLIENT_HASH_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_HASH_UNSPECIFIED = 0;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 148.

```text
notations.proto
// syntax: proto3

package chesscom.proto_options.manifest.v1;

enum ClientHash {
  CLIENT_HASH_UNSPECIFIED = 0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optio
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07638"></a>
## FND-07638: chesscom.proto_options.manifest.v1.ClientHash.CLIENT_HASH_EMAIL_SHA256 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_HASH_EMAIL_SHA256 = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 179.

```text
o3

package chesscom.proto_options.manifest.v1;

enum ClientHash {
  CLIENT_HASH_UNSPECIFIED = 0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.man
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07639"></a>
## FND-07639: chesscom.proto_options.manifest.v1.ClientHash.CLIENT_HASH_PHONE_SHA256 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_HASH_PHONE_SHA256 = 2;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 211.

```text
ns.manifest.v1;

enum ClientHash {
  CLIENT_HASH_UNSPECIFIED = 0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_acces
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07640"></a>
## FND-07640: message declaration: chesscom.proto_options.manifest.v1.GnsServiceOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GnsServiceOptions {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 244.

```text
{
  CLIENT_HASH_UNSPECIFIED = 0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOption
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07641"></a>
## FND-07641: chesscom.proto_options.manifest.v1.GnsServiceOptions.providers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string providers = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 274.

```text
0;
  CLIENT_HASH_EMAIL_SHA256 = 1;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07642"></a>
## FND-07642: chesscom.proto_options.manifest.v1.GnsServiceOptions.cli_group = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cli_group = 2;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 307.

```text
;
  CLIENT_HASH_PHONE_SHA256 = 2;
}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07643"></a>
## FND-07643: chesscom.proto_options.manifest.v1.GnsServiceOptions.scope = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string scope = 3;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 340.

```text

}

message GnsServiceOptions {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description =
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07644"></a>
## FND-07644: chesscom.proto_options.manifest.v1.GnsServiceOptions.description = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 4;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 369.

```text
 {
  repeated string providers = 1;
  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string example
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07645"></a>
## FND-07645: chesscom.proto_options.manifest.v1.GnsServiceOptions.skip = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool skip = 5;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 404.

```text

  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07646"></a>
## FND-07646: chesscom.proto_options.manifest.v1.GnsServiceOptions.cli_alias = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cli_alias = 6;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 430.

```text
up = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_o
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07647"></a>
## FND-07647: chesscom.proto_options.manifest.v1.GnsServiceOptions.default_access = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 463.

```text
 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool a
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07648"></a>
## FND-07648: message declaration: chesscom.proto_options.manifest.v1.GnsMethodOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GnsMethodOptions {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 541.

```text
ring cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07649"></a>
## FND-07649: chesscom.proto_options.manifest.v1.GnsMethodOptions.cli_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cli_name = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 570.

```text
l .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07650"></a>
## FND-07650: chesscom.proto_options.manifest.v1.GnsMethodOptions.scope = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string scope = 2;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 602.

```text
st.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
 
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07651"></a>
## FND-07651: chesscom.proto_options.manifest.v1.GnsMethodOptions.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 3;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 631.

```text
s = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description 
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07652"></a>
## FND-07652: chesscom.proto_options.manifest.v1.GnsMethodOptions.examples = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string examples = 4;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 666.

```text
{
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optio
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07653"></a>
## FND-07653: chesscom.proto_options.manifest.v1.GnsMethodOptions.skip = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool skip = 5;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 404.

```text

  optional string cli_group = 2;
  optional string scope = 3;
  optional string description = 4;
  optional bool skip = 5;
  optional string cli_alias = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess default_access = 7;
}

message GnsMethodOptions {
  optional string cli_name = 1;
  optional string scope = 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07654"></a>
## FND-07654: chesscom.proto_options.manifest.v1.GnsMethodOptions.agent_tool = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 724.

```text
= 2;
  optional string description = 3;
  optional string examples = 4;
  optional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  op
```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07655"></a>
## FND-07655: chesscom.proto_options.manifest.v1.GnsMethodOptions.access = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 800.

```text
tional bool skip = 5;
  optional .chesscom.proto_options.manifest.v1.GnsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07656"></a>
## FND-07656: message declaration: chesscom.proto_options.manifest.v1.GnsAgentTool

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GnsAgentTool {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 870.

```text
nsAgentTool agent_tool = 6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07657"></a>
## FND-07657: chesscom.proto_options.manifest.v1.GnsAgentTool.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 895.

```text
6;
  optional .chesscom.proto_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07658"></a>
## FND-07658: chesscom.proto_options.manifest.v1.GnsAgentTool.description = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 2;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 923.

```text
o_options.manifest.v1.GnsAccess access = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07659"></a>
## FND-07659: message declaration: chesscom.proto_options.manifest.v1.GnsAccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GnsAccess {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 959.

```text
ss = 7;
}

message GnsAgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07660"></a>
## FND-07660: chesscom.proto_options.manifest.v1.GnsAccess.requires = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string requires = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 981.

```text
AgentTool {
  optional string name = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07661"></a>
## FND-07661: message declaration: chesscom.proto_options.manifest.v1.GnsFieldOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GnsFieldOptions {

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 1014.

```text
e = 1;
  optional string description = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07662"></a>
## FND-07662: chesscom.proto_options.manifest.v1.GnsFieldOptions.client_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;

### Evidence

- **SRC-0525** `research/proto/chesscom/proto_options/manifest/v1/annotations.proto` — [preserved redacted evidence](../evidence/text/80d6f22434167adc4f0df5f906ab1859a24689afd25dbf3a1d6e3eb4129a2c33.proto)
  Character offset 1042.

```text
cription = 2;
}

message GnsAccess {
  optional string requires = 1;
}

message GnsFieldOptions {
  optional .chesscom.proto_options.manifest.v1.ClientHash client_hash = 1;
}

```

**Source references:** SRC-0525, SRC-1496  
**URL references:** None independently associated  
**Related findings:** FND-07636, FND-07637, FND-07638

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07663"></a>
## FND-07663: enum declaration: chesscom.proto_options.oauth.v1.ScopeVisibility

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ScopeVisibility {

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 124.

```text
o_options/oauth/v1/scope_options.proto
// syntax: proto3

package chesscom.proto_options.oauth.v1;

enum ScopeVisibility {
  SCOPE_VISIBILITY_UNSPECIFIED = 0;
  SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07664"></a>
## FND-07664: chesscom.proto_options.oauth.v1.ScopeVisibility.SCOPE_VISIBILITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VISIBILITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 149.

```text
options.proto
// syntax: proto3

package chesscom.proto_options.oauth.v1;

enum ScopeVisibility {
  SCOPE_VISIBILITY_UNSPECIFIED = 0;
  SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07665"></a>
## FND-07665: chesscom.proto_options.oauth.v1.ScopeVisibility.SCOPE_VISIBILITY_INTERNAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VISIBILITY_INTERNAL = 1;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 185.

```text
kage chesscom.proto_options.oauth.v1;

enum ScopeVisibility {
  SCOPE_VISIBILITY_UNSPECIFIED = 0;
  SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07666"></a>
## FND-07666: chesscom.proto_options.oauth.v1.ScopeVisibility.SCOPE_VISIBILITY_PUBLIC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VISIBILITY_PUBLIC = 2;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 218.

```text
.v1;

enum ScopeVisibility {
  SCOPE_VISIBILITY_UNSPECIFIED = 0;
  SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07667"></a>
## FND-07667: chesscom.proto_options.oauth.v1.ScopeVisibility.SCOPE_VISIBILITY_PRIVILEGED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_VISIBILITY_PRIVILEGED = 3;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 249.

```text
SCOPE_VISIBILITY_UNSPECIFIED = 0;
  SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07668"></a>
## FND-07668: enum declaration: chesscom.proto_options.oauth.v1.ScopeConsent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ScopeConsent {

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 285.

```text
SCOPE_VISIBILITY_INTERNAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07669"></a>
## FND-07669: chesscom.proto_options.oauth.v1.ScopeConsent.SCOPE_CONSENT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONSENT_UNSPECIFIED = 0;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 307.

```text
NAL = 1;
  SCOPE_VISIBILITY_PUBLIC = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07670"></a>
## FND-07670: chesscom.proto_options.oauth.v1.ScopeConsent.SCOPE_CONSENT_OPTIONAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONSENT_OPTIONAL = 1;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 340.

```text
C = 2;
  SCOPE_VISIBILITY_PRIVILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07671"></a>
## FND-07671: chesscom.proto_options.oauth.v1.ScopeConsent.SCOPE_CONSENT_REQUIRED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONSENT_REQUIRED = 2;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 370.

```text
ILEGED = 3;
}

enum ScopeConsent {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07672"></a>
## FND-07672: chesscom.proto_options.oauth.v1.ScopeConsent.SCOPE_CONSENT_IMPLICIT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CONSENT_IMPLICIT = 3;

### Evidence

- **SRC-0526** `research/proto/chesscom/proto_options/oauth/v1/scope_options.proto` — [preserved redacted evidence](../evidence/text/17a220c8a3cd0de3141008ef512e970414aa36ec073ad410ea573e7a5a9cec42.proto)
  Character offset 400.

```text
nt {
  SCOPE_CONSENT_UNSPECIFIED = 0;
  SCOPE_CONSENT_OPTIONAL = 1;
  SCOPE_CONSENT_REQUIRED = 2;
  SCOPE_CONSENT_IMPLICIT = 3;
}

```

**Source references:** SRC-0526, SRC-1497  
**URL references:** None independently associated  
**Related findings:** FND-07663, FND-07664, FND-07665

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07673"></a>
## FND-07673: message declaration: chesscom.proto_options.user_activity_connector.v1.UserActivityConnectorDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserActivityConnectorDefinition {

### Evidence

- **SRC-0527** `research/proto/chesscom/proto_options/user_activity_connector/v1/options.proto` — [preserved redacted evidence](../evidence/text/7d362cee585dad5e7ddfb2d900d5408a26f008accb3eaa4921e620966ea442b3.proto)
  Character offset 154.

```text
tor/v1/options.proto
// syntax: proto3

package chesscom.proto_options.user_activity_connector.v1;

message UserActivityConnectorDefinition {
}

```

**Source references:** SRC-0527, SRC-1498  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07674"></a>
## FND-07674: message declaration: chesscom.ratings.v2.Rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Rating {

### Evidence

- **SRC-0528** `research/proto/chesscom/ratings/v2/rating.proto` — [preserved redacted evidence](../evidence/text/5378162ec605ecace49fcb88bc32b5a5f03cb0e8b78fc1cf4e10abf7043ff213.proto)
  Character offset 93.

```text
// source: chesscom/ratings/v2/rating.proto
// syntax: proto3

package chesscom.ratings.v2;

message Rating {
  oneof _timestamp {
  .google.protobuf.Timestamp timestamp = 3;
  }
  optional uint32 value = 1;
  optional .chesscom.api.v1.Decimal deviation = 2;
}

```

**Source references:** SRC-0528, SRC-1499  
**URL references:** None independently associated  
**Related findings:** FND-07675, FND-07676

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
