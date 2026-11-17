# authoritative_frontend_descriptors — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17415"></a>
## FND-17415: Full frontend descriptor: google/protobuf/timestamp.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/timestamp.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "Timestamp",
      "field": [
        {
          "name": "seconds",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "nanos",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "TimestampProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/timestamppb",
    "cc_enable_arenas": true,
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 335.

```text
per).
// Personal-use reverse engineering artifact. Not redistributed.
export const DESCRIPTORS = {"google/protobuf/timestamp.proto":"Ch9nb29nbGUvcHJvdG9idWYvdGltZXN0YW1wLnByb3RvEg9nb29nbGUucHJvdG9idWYiKwoJVGltZXN0YW1wEg8KB3NlY29uZHMYASABKAMSDQoFbmFub3MYAiABKAVChQEKE2NvbS5nb29nbGUucHJvdG9idWZCDlRpbWVzdGFtcFByb3RvUAFaMmdvb2dsZS5nb2xhbmcub3JnL3Byb3RvYnVmL3R5cGVzL2tub3duL3RpbWVzdGFtcHBi+AEBogIDR1BCqgIeR29vZ2xlLlByb3RvYn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17416"></a>
## FND-17416: Full frontend descriptor: google/protobuf/any.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/any.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "Any",
      "field": [
        {
          "name": "type_url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES"
        }
      ]
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "AnyProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/anypb",
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 691.

```text
R5cGVzL2tub3duL3RpbWVzdGFtcHBi+AEBogIDR1BCqgIeR29vZ2xlLlByb3RvYnVmLldlbGxLbm93blR5cGVzYgZwcm90bzM","google/protobuf/any.proto":"Chlnb29nbGUvcHJvdG9idWYvYW55LnByb3RvEg9nb29nbGUucHJvdG9idWYiJgoDQW55EhAKCHR5cGVfdXJsGAEgASgJEg0KBXZhbHVlGAIgASgMQnYKE2NvbS5nb29nbGUucHJvdG9idWZCCEFueVByb3RvUAFaLGdvb2dsZS5nb2xhbmcub3JnL3Byb3RvYnVmL3R5cGVzL2tub3duL2FueXBiogIDR1BCqgIeR29vZ2xlLlByb3RvYnVmLldlbGxLbm93blR5cGVzYgZwcm90bzM","google
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17417"></a>
## FND-17417: Full frontend descriptor: google/protobuf/duration.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/duration.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "Duration",
      "field": [
        {
          "name": "seconds",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "nanos",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "DurationProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/durationpb",
    "cc_enable_arenas": true,
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 1005.

```text
Byb3RvYnVmL3R5cGVzL2tub3duL2FueXBiogIDR1BCqgIeR29vZ2xlLlByb3RvYnVmLldlbGxLbm93blR5cGVzYgZwcm90bzM","google/protobuf/duration.proto":"Ch5nb29nbGUvcHJvdG9idWYvZHVyYXRpb24ucHJvdG8SD2dvb2dsZS5wcm90b2J1ZiIqCghEdXJhdGlvbhIPCgdzZWNvbmRzGAEgASgDEg0KBW5hbm9zGAIgASgFQoMBChNjb20uZ29vZ2xlLnByb3RvYnVmQg1EdXJhdGlvblByb3RvUAFaMWdvb2dsZS5nb2xhbmcub3JnL3Byb3RvYnVmL3R5cGVzL2tub3duL2R1cmF0aW9ucGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2V
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17418"></a>
## FND-17418: Full frontend descriptor: google/protobuf/empty.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/empty.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "Empty"
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "EmptyProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/emptypb",
    "cc_enable_arenas": true,
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 1355.

```text
3R5cGVzL2tub3duL2R1cmF0aW9ucGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2VsbEtub3duVHlwZXNiBnByb3RvMw","google/protobuf/empty.proto":"Chtnb29nbGUvcHJvdG9idWYvZW1wdHkucHJvdG8SD2dvb2dsZS5wcm90b2J1ZiIHCgVFbXB0eUJ9ChNjb20uZ29vZ2xlLnByb3RvYnVmQgpFbXB0eVByb3RvUAFaLmdvb2dsZS5nb2xhbmcub3JnL3Byb3RvYnVmL3R5cGVzL2tub3duL2VtcHR5cGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2VsbEtub3duVHlwZXNiBnByb3RvMw","google/protobuf/field_mask.proto"
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17419"></a>
## FND-17419: Full frontend descriptor: google/protobuf/field_mask.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/field_mask.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "FieldMask",
      "field": [
        {
          "name": "paths",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "FieldMaskProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/fieldmaskpb",
    "cc_enable_arenas": true,
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 1642.

```text
nVmL3R5cGVzL2tub3duL2VtcHR5cGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2VsbEtub3duVHlwZXNiBnByb3RvMw","google/protobuf/field_mask.proto":"CiBnb29nbGUvcHJvdG9idWYvZmllbGRfbWFzay5wcm90bxIPZ29vZ2xlLnByb3RvYnVmIhoKCUZpZWxkTWFzaxINCgVwYXRocxgBIAMoCUKFAQoTY29tLmdvb2dsZS5wcm90b2J1ZkIORmllbGRNYXNrUHJvdG9QAVoyZ29vZ2xlLmdvbGFuZy5vcmcvcHJvdG9idWYvdHlwZXMva25vd24vZmllbGRtYXNrcGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2VsbEtub3duVHlwZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17420"></a>
## FND-17420: Full frontend descriptor: google/protobuf/struct.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "google/protobuf/struct.proto",
  "package": "google.protobuf",
  "message_type": [
    {
      "name": "Struct",
      "field": [
        {
          "name": "fields",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Struct.FieldsEntry"
        }
      ],
      "nested_type": [
        {
          "name": "FieldsEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    },
    {
      "name": "Value",
      "field": [
        {
          "name": "null_value",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".google.protobuf.NullValue",
          "oneof_index": 0
        },
        {
          "name": "number_value",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE",
          "oneof_index": 0
        },
        {
          "name": "string_value",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "bool_value",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0
        },
        {
          "name": "struct_value",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Struct",
          "oneof_index": 0
        },
        {
          "name": "list_value",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.ListValue",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "kind"
        }
      ]
    },
    {
      "name": "ListValue",
      "field": [
        {
          "name": "values",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Value"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "NullValue",
      "value": [
        {
          "name": "NULL_VALUE",
          "number": 0
        }
      ]
    }
  ],
  "options": {
    "java_package": "com.google.protobuf",
    "java_outer_classname": "StructProto",
    "java_multiple_files": true,
    "go_package": "google.golang.org/protobuf/types/known/structpb",
    "cc_enable_arenas": true,
    "objc_class_prefix": "GPB",
    "csharp_namespace": "Google.Protobuf.WellKnownTypes"
  },
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 1978.

```text
HlwZXMva25vd24vZmllbGRtYXNrcGL4AQGiAgNHUEKqAh5Hb29nbGUuUHJvdG9idWYuV2VsbEtub3duVHlwZXNiBnByb3RvMw","google/protobuf/struct.proto":"Chxnb29nbGUvcHJvdG9idWYvc3RydWN0LnByb3RvEg9nb29nbGUucHJvdG9idWYihAEKBlN0cnVjdBIzCgZmaWVsZHMYASADKAsyIy5nb29nbGUucHJvdG9idWYuU3RydWN0LkZpZWxkc0VudHJ5GkUKC0ZpZWxkc0VudHJ5EgsKA2tleRgBIAEoCRIlCgV2YWx1ZRgCIAEoCzIWLmdvb2dsZS5wcm90b2J1Zi5WYWx1ZToCOAEi6gEKBVZhbHVlEjAKCm51bGxfdmFsdWUYASABKA4yGi5nb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17421"></a>
## FND-17421: Full frontend descriptor: chesscom/proto_options/annotations/v1/annotations.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/annotations/v1/annotations.proto",
  "package": "chesscom.proto_options.annotations.v1",
  "message_type": [
    {
      "name": "Usage",
      "field": [
        {
          "name": "platform",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.annotations.v1.Platform"
        },
        {
          "name": "project",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.annotations.v1.Project"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "Platform",
      "value": [
        {
          "name": "PLATFORM_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLATFORM_MOBILE",
          "number": 1
        },
        {
          "name": "PLATFORM_WEB",
          "number": 2
        },
        {
          "name": "PLATFORM_BACKEND",
          "number": 3
        }
      ]
    },
    {
      "name": "Project",
      "value": [
        {
          "name": "PROJECT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PROJECT_CHESSCOM",
          "number": 1
        },
        {
          "name": "PROJECT_CHESSKID",
          "number": 2
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "message_used_by",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 60000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.annotations.v1.Usage",
      "json_name": "messageUsedBy",
      "proto3_optional": true
    },
    {
      "name": "enum_used_by",
      "extendee": ".google.protobuf.EnumOptions",
      "number": 60001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.annotations.v1.Usage",
      "json_name": "enumUsedBy",
      "proto3_optional": true
    },
    {
      "name": "service_used_by",
      "extendee": ".google.protobuf.ServiceOptions",
      "number": 60002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.annotations.v1.Usage",
      "json_name": "serviceUsedBy",
      "proto3_optional": true
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 2863.

```text
VmL3R5cGVzL2tub3duL3N0cnVjdHBi+AEBogIDR1BCqgIeR29vZ2xlLlByb3RvYnVmLldlbGxLbm93blR5cGVzYgZwcm90bzM","chesscom/proto_options/annotations/v1/annotations.proto":"CjdjaGVzc2NvbS9wcm90b19vcHRpb25zL2Fubm90YXRpb25zL3YxL2Fubm90YXRpb25zLnByb3RvEiVjaGVzc2NvbS5wcm90b19vcHRpb25zLmFubm90YXRpb25zLnYxIosBCgVVc2FnZRJBCghwbGF0Zm9ybRgBIAMoDjIvLmNoZXNzY29tLnByb3RvX29wdGlvbnMuYW5ub3RhdGlvbnMudjEuUGxhdGZvcm0SPwoHcHJvamVjdBgCIAMoDjIuLmNoZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17422"></a>
## FND-17422: Full frontend descriptor: chesscom/engine/v1/engine.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/engine/v1/engine.proto",
  "package": "chesscom.engine.v1",
  "enum_type": [
    {
      "name": "Engine",
      "value": [
        {
          "name": "ENGINE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ENGINE_SF12",
          "number": 1
        },
        {
          "name": "ENGINE_SF15",
          "number": 2
        },
        {
          "name": "ENGINE_SF15_NNUE",
          "number": 3
        },
        {
          "name": "ENGINE_SF15_1",
          "number": 4
        },
        {
          "name": "ENGINE_SF15_1_NNUE",
          "number": 5
        },
        {
          "name": "ENGINE_SF16_NNUE",
          "number": 6
        },
        {
          "name": "ENGINE_SF9_FAIRPLAY_V1",
          "number": 7
        },
        {
          "name": "ENGINE_DRAGON_3_3",
          "number": 8
        },
        {
          "name": "ENGINE_KOMODO_3_3",
          "number": 9
        },
        {
          "name": "ENGINE_SF16_1_NNUE",
          "number": 10
        },
        {
          "name": "ENGINE_TORCH_3",
          "number": 11
        },
        {
          "name": "ENGINE_TORCH_HUMAN",
          "number": 12
        },
        {
          "name": "ENGINE_SF18_NNUE",
          "number": 13
        },
        {
          "name": "ENGINE_SF19_NNUE",
          "number": 14
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 3975.

```text
syLC5jaGVzc2NvbS5wcm90b19vcHRpb25zLmFubm90YXRpb25zLnYxLlVzYWdlUg1zZXJ2aWNlVXNlZEJ5iAEBYgZwcm90bzM","chesscom/engine/v1/engine.proto":"Ch9jaGVzc2NvbS9lbmdpbmUvdjEvZW5naW5lLnByb3RvEhJjaGVzc2NvbS5lbmdpbmUudjEq3AIKBkVuZ2luZRIWChJFTkdJTkVfVU5TUEVDSUZJRUQQABIPCgtFTkdJTkVfU0YxMhABEg8KC0VOR0lORV9TRjE1EAISFAoQRU5HSU5FX1NGMTVfTk5VRRADEhEKDUVOR0lORV9TRjE1XzEQBBIWChJFTkdJTkVfU0YxNV8xX05OVUUQBRIUChBFTkdJTkVfU0YxNl9OTlVFEAYSGgoWRU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17423"></a>
## FND-17423: Full frontend descriptor: chesscom/engine/v1/strength.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/engine/v1/strength.proto",
  "package": "chesscom.engine.v1",
  "enum_type": [
    {
      "name": "Strength",
      "value": [
        {
          "name": "STRENGTH_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STRENGTH_FAST",
          "number": 1
        },
        {
          "name": "STRENGTH_STANDARD",
          "number": 2
        },
        {
          "name": "STRENGTH_DEEP",
          "number": 3
        },
        {
          "name": "STRENGTH_MAXIMUM",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 4562.

```text
1JDSF9IVU1BThAMEhQKEEVOR0lORV9TRjE4X05OVUUQDRIUChBFTkdJTkVfU0YxOV9OTlVFEA4aB4qmHQMKAQFiBnByb3RvMw","chesscom/engine/v1/strength.proto":"CiFjaGVzc2NvbS9lbmdpbmUvdjEvc3RyZW5ndGgucHJvdG8SEmNoZXNzY29tLmVuZ2luZS52MSqAAQoIU3RyZW5ndGgSGAoUU1RSRU5HVEhfVU5TUEVDSUZJRUQQABIRCg1TVFJFTkdUSF9GQVNUEAESFQoRU1RSRU5HVEhfU1RBTkRBUkQQAhIRCg1TVFJFTkdUSF9ERUVQEAMSFAoQU1RSRU5HVEhfTUFYSU1VTRAEGgeKph0DCgEBYgZwcm90bzM","chesscom/chess/v1/time
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17424"></a>
## FND-17424: Full frontend descriptor: chesscom/chess/v1/time.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/time.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "TimeControl",
      "field": [
        {
          "name": "base",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.BaseTimeControl",
          "oneof_index": 0
        },
        {
          "name": "daily",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.DailyTimeControl",
          "oneof_index": 0
        },
        {
          "name": "multi_stage",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.MultiStageTimeControl",
          "oneof_index": 0
        },
        {
          "name": "armageddon",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArmageddonTimeControl",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "control"
        }
      ]
    },
    {
      "name": "BaseTimeControl",
      "field": [
        {
          "name": "base_ms",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "increment_ms",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        }
      ],
      "options": {}
    },
    {
      "name": "DailyTimeControl",
      "field": [
        {
          "name": "days_per_turn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    },
    {
      "name": "MultiStageTimeControl",
      "field": [
        {
          "name": "stages",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.TimeControlStage"
        }
      ],
      "options": {}
    },
    {
      "name": "TimeControlStage",
      "field": [
        {
          "name": "time_control",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.BaseTimeControl"
        },
        {
          "name": "move_limit",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_move_limit"
        }
      ]
    },
    {
      "name": "ArmageddonTimeControl",
      "field": [
        {
          "name": "white_base_ms",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "black_base_ms",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "increment_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "increment_after_move",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "TimeClass",
      "value": [
        {
          "name": "TIME_CLASS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TIME_CLASS_HYPERBULLET",
          "number": 1
        },
        {
          "name": "TIME_CLASS_BULLET",
          "number": 2
        },
        {
          "name": "TIME_CLASS_BLITZ",
          "number": 3
        },
        {
          "name": "TIME_CLASS_RAPID",
          "number": 4
        },
        {
          "name": "TIME_CLASS_CLASSICAL",
          "number": 5
        },
        {
          "name": "TIME_CLASS_DAILY",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 4860.

```text
5HVEhfU1RBTkRBUkQQAhIRCg1TVFJFTkdUSF9ERUVQEAMSFAoQU1RSRU5HVEhfTUFYSU1VTRAEGgeKph0DCgEBYgZwcm90bzM","chesscom/chess/v1/time.proto":"ChxjaGVzc2NvbS9jaGVzcy92MS90aW1lLnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSKNAgoLVGltZUNvbnRyb2wSMgoEYmFzZRgBIAEoCzIiLmNoZXNzY29tLmNoZXNzLnYxLkJhc2VUaW1lQ29udHJvbEgAEjQKBWRhaWx5GAIgASgLMiMuY2hlc3Njb20uY2hlc3MudjEuRGFpbHlUaW1lQ29udHJvbEgAEj8KC211bHRpX3N0YWdlGAMgASgLMiguY2hlc3Njb20uY2hlc3MudjEuTXVsd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17425"></a>
## FND-17425: Full frontend descriptor: chesscom/chess/v1/variant.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/variant.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "Variant",
      "value": [
        {
          "name": "VARIANT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "VARIANT_CHESS",
          "number": 1
        },
        {
          "name": "VARIANT_CHESS_960",
          "number": 2
        },
        {
          "name": "VARIANT_BUGHOUSE",
          "number": 4
        },
        {
          "name": "VARIANT_THREE_CHECK",
          "number": 5
        },
        {
          "name": "VARIANT_CRAZYHOUSE",
          "number": 6
        },
        {
          "name": "VARIANT_KING_OF_THE_HILL",
          "number": 7
        },
        {
          "name": "VARIANT_ODDS_CHESS",
          "number": 8
        },
        {
          "name": "VARIANT_HELP_CHESS",
          "number": 9
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 6221.

```text
JBUElEEAQSGAoUVElNRV9DTEFTU19DTEFTU0lDQUwQBRIUChBUSU1FX0NMQVNTX0RBSUxZEAYaCIqmHQQKAgECYgZwcm90bzM","chesscom/chess/v1/variant.proto":"Ch9jaGVzc2NvbS9jaGVzcy92MS92YXJpYW50LnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSrrAQoHVmFyaWFudBIXChNWQVJJQU5UX1VOU1BFQ0lGSUVEEAASEQoNVkFSSUFOVF9DSEVTUxABEhUKEVZBUklBTlRfQ0hFU1NfOTYwEAISFAoQVkFSSUFOVF9CVUdIT1VTRRAEEhcKE1ZBUklBTlRfVEhSRUVfQ0hFQ0sQBRIWChJWQVJJQU5UX0NSQVpZSE9VU0UQBhIcChhWQVJJQU5UX0
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17426"></a>
## FND-17426: Full frontend descriptor: chesscom/chess/v1/result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/result.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "Result",
      "value": [
        {
          "name": "RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RESULT_WHITE_WIN",
          "number": 1
        },
        {
          "name": "RESULT_BLACK_WIN",
          "number": 2
        },
        {
          "name": "RESULT_DRAW",
          "number": 3
        },
        {
          "name": "RESULT_ABORT",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "ResultType",
      "value": [
        {
          "name": "RESULT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RESULT_TYPE_CHECKMATE",
          "number": 1
        },
        {
          "name": "RESULT_TYPE_STALEMATE",
          "number": 2
        },
        {
          "name": "RESULT_TYPE_INSUFFICIENT_MATERIAL",
          "number": 3
        },
        {
          "name": "RESULT_TYPE_RESIGNATION",
          "number": 4
        },
        {
          "name": "RESULT_TYPE_DRAW_OFFER",
          "number": 5
        },
        {
          "name": "RESULT_TYPE_TIMEOUT",
          "number": 6
        },
        {
          "name": "RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL",
          "number": 7
        },
        {
          "name": "RESULT_TYPE_ABANDONMENT",
          "number": 8
        },
        {
          "name": "RESULT_TYPE_50_MOVE_RULE",
          "number": 9
        },
        {
          "name": "RESULT_TYPE_THREEFOLD",
          "number": 10
        },
        {
          "name": "RESULT_TYPE_BUGHOUSE_PARTNER_LOSE",
          "number": 11
        },
        {
          "name": "RESULT_TYPE_THREE_CHECK",
          "number": 12
        },
        {
          "name": "RESULT_TYPE_KING_OF_THE_HILL",
          "number": 13
        },
        {
          "name": "RESULT_TYPE_DOUBLE_FORFEIT",
          "number": 14
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 6656.

```text
0hJTEwQBxIWChJWQVJJQU5UX09ERFNfQ0hFU1MQCBIWChJWQVJJQU5UX0hFTFBfQ0hFU1MQCRoIiqYdBAoCAQJiBnByb3RvMw","chesscom/chess/v1/result.proto":"Ch5jaGVzc2NvbS9jaGVzcy92MS9yZXN1bHQucHJvdG8SEWNoZXNzY29tLmNoZXNzLnYxKnkKBlJlc3VsdBIWChJSRVNVTFRfVU5TUEVDSUZJRUQQABIUChBSRVNVTFRfV0hJVEVfV0lOEAESFAoQUkVTVUxUX0JMQUNLX1dJThACEg8KC1JFU1VMVF9EUkFXEAMSEAoMUkVTVUxUX0FCT1JUEAQaCIqmHQQKAgECKvADCgpSZXN1bHRUeXBlEhsKF1JFU1VMVF9UWVBFX1VOU1BFQ0lGSUV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17427"></a>
## FND-17427: Full frontend descriptor: chesscom/chess/v1/color.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/color.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "Color",
      "value": [
        {
          "name": "COLOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COLOR_WHITE",
          "number": 1
        },
        {
          "name": "COLOR_BLACK",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 7600.

```text
UWVBFX0tJTkdfT0ZfVEhFX0hJTEwQDRIeChpSRVNVTFRfVFlQRV9ET1VCTEVfRk9SRkVJVBAOGgiKph0ECgIBAmIGcHJvdG8z","chesscom/chess/v1/color.proto":"Ch1jaGVzc2NvbS9jaGVzcy92MS9jb2xvci5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEqSgoFQ29sb3ISFQoRQ09MT1JfVU5TUEVDSUZJRUQQABIPCgtDT0xPUl9XSElURRABEg8KC0NPTE9SX0JMQUNLEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/chess/v1/piece.proto":"Ch1jaGVzc2NvbS9jaGVzcy92MS9waWVjZS5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEiZQoFUG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17428"></a>
## FND-17428: Full frontend descriptor: chesscom/chess/v1/piece.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/piece.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "Piece",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PieceType"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "PieceType",
      "value": [
        {
          "name": "PIECE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PIECE_TYPE_PAWN",
          "number": 1
        },
        {
          "name": "PIECE_TYPE_KNIGHT",
          "number": 2
        },
        {
          "name": "PIECE_TYPE_BISHOP",
          "number": 3
        },
        {
          "name": "PIECE_TYPE_ROOK",
          "number": 4
        },
        {
          "name": "PIECE_TYPE_QUEEN",
          "number": 5
        },
        {
          "name": "PIECE_TYPE_KING",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 7814.

```text
oRQ09MT1JfVU5TUEVDSUZJRUQQABIPCgtDT0xPUl9XSElURRABEg8KC0NPTE9SX0JMQUNLEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/chess/v1/piece.proto":"Ch1jaGVzc2NvbS9jaGVzcy92MS9waWVjZS5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEiZQoFUGllY2USJwoFY29sb3IYASABKA4yGC5jaGVzc2NvbS5jaGVzcy52MS5Db2xvchIqCgR0eXBlGAIgASgOMhwuY2hlc3Njb20uY2hlc3MudjEuUGllY2VUeXBlOgeCph0DCgEBKrMBCglQaWVjZVR5cGUSGgoWUElFQ0VfVFlQRV9VTlNQRUNJRklFRBAAEhMKD1BJRUNFX1RZUEVfUEFXThAB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17429"></a>
## FND-17429: Full frontend descriptor: chesscom/chess/v1/square.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/square.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "Square",
      "value": [
        {
          "name": "SQUARE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SQUARE_A1",
          "number": 1
        },
        {
          "name": "SQUARE_B1",
          "number": 2
        },
        {
          "name": "SQUARE_C1",
          "number": 3
        },
        {
          "name": "SQUARE_D1",
          "number": 4
        },
        {
          "name": "SQUARE_E1",
          "number": 5
        },
        {
          "name": "SQUARE_F1",
          "number": 6
        },
        {
          "name": "SQUARE_G1",
          "number": 7
        },
        {
          "name": "SQUARE_H1",
          "number": 8
        },
        {
          "name": "SQUARE_A2",
          "number": 9
        },
        {
          "name": "SQUARE_B2",
          "number": 10
        },
        {
          "name": "SQUARE_C2",
          "number": 11
        },
        {
          "name": "SQUARE_D2",
          "number": 12
        },
        {
          "name": "SQUARE_E2",
          "number": 13
        },
        {
          "name": "SQUARE_F2",
          "number": 14
        },
        {
          "name": "SQUARE_G2",
          "number": 15
        },
        {
          "name": "SQUARE_H2",
          "number": 16
        },
        {
          "name": "SQUARE_A3",
          "number": 17
        },
        {
          "name": "SQUARE_B3",
          "number": 18
        },
        {
          "name": "SQUARE_C3",
          "number": 19
        },
        {
          "name": "SQUARE_D3",
          "number": 20
        },
        {
          "name": "SQUARE_E3",
          "number": 21
        },
        {
          "name": "SQUARE_F3",
          "number": 22
        },
        {
          "name": "SQUARE_G3",
          "number": 23
        },
        {
          "name": "SQUARE_H3",
          "number": 24
        },
        {
          "name": "SQUARE_A4",
          "number": 25
        },
        {
          "name": "SQUARE_B4",
          "number": 26
        },
        {
          "name": "SQUARE_C4",
          "number": 27
        },
        {
          "name": "SQUARE_D4",
          "number": 28
        },
        {
          "name": "SQUARE_E4",
          "number": 29
        },
        {
          "name": "SQUARE_F4",
          "number": 30
        },
        {
          "name": "SQUARE_G4",
          "number": 31
        },
        {
          "name": "SQUARE_H4",
          "number": 32
        },
        {
          "name": "SQUARE_A5",
          "number": 33
        },
        {
          "name": "SQUARE_B5",
          "number": 34
        },
        {
          "name": "SQUARE_C5",
          "number": 35
        },
        {
          "name": "SQUARE_D5",
          "number": 36
        },
        {
          "name": "SQUARE_E5",
          "number": 37
        },
        {
          "name": "SQUARE_F5",
          "number": 38
        },
        {
          "name": "SQUARE_G5",
          "number": 39
        },
        {
          "name": "SQUARE_H5",
          "number": 40
        },
        {
          "name": "SQUARE_A6",
          "number": 41
        },
        {
          "name": "SQUARE_B6",
          "number": 42
        },
        {
          "name": "SQUARE_C6",
          "number": 43
        },
        {
          "name": "SQUARE_D6",
          "number": 44
        },
        {
          "name": "SQUARE_E6",
          "number": 45
        },
        {
          "name": "SQUARE_F6",
          "number": 46
        },
        {
          "name": "SQUARE_G6",
          "number": 47
        },
        {
          "name": "SQUARE_H6",
          "number": 48
        },
        {
          "name": "SQUARE_A7",
          "number": 49
        },
        {
          "name": "SQUARE_B7",
          "number": 50
        },
        {
          "name": "SQUARE_C7",
          "number": 51
        },
        {
          "name": "SQUARE_D7",
          "number": 52
        },
        {
          "name": "SQUARE_E7",
          "number": 53
        },
        {
          "name": "SQUARE_F7",
          "number": 54
        },
        {
          "name": "SQUARE_G7",
          "number": 55
        },
        {
          "name": "SQUARE_H7",
          "number": 56
        },
        {
          "name": "SQUARE_A8",
          "number": 57
        },
        {
          "name": "SQUARE_B8",
          "number": 58
        },
        {
          "name": "SQUARE_C8",
          "number": 59
        },
        {
          "name": "SQUARE_D8",
          "number": 60
        },
        {
          "name": "SQUARE_E8",
          "number": 61
        },
        {
          "name": "SQUARE_F8",
          "number": 62
        },
        {
          "name": "SQUARE_G8",
          "number": 63
        },
        {
          "name": "SQUARE_H8",
          "number": 64
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 8307.

```text
V9UWVBFX1JPT0sQBBIUChBQSUVDRV9UWVBFX1FVRUVOEAUSEwoPUElFQ0VfVFlQRV9LSU5HEAYaB4qmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/square.proto":"Ch5jaGVzc2NvbS9jaGVzcy92MS9zcXVhcmUucHJvdG8SEWNoZXNzY29tLmNoZXNzLnYxKukHCgZTcXVhcmUSFgoSU1FVQVJFX1VOU1BFQ0lGSUVEEAASDQoJU1FVQVJFX0ExEAESDQoJU1FVQVJFX0IxEAISDQoJU1FVQVJFX0MxEAMSDQoJU1FVQVJFX0QxEAQSDQoJU1FVQVJFX0UxEAUSDQoJU1FVQVJFX0YxEAYSDQoJU1FVQVJFX0cxEAcSDQoJU1FVQVJFX0gxEAgSDQoJU1FVQVJ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17430"></a>
## FND-17430: Full frontend descriptor: chesscom/chess/v1/move.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/move.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "CastlingDetails",
      "field": [
        {
          "name": "king_from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "king_to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "rook_from",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "rook_to",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ],
      "options": {}
    },
    {
      "name": "Move",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "promotion_piece_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PromotionPieceType",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "time_taken_ms",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "castling_details",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.CastlingDetails",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "remaining_clock_ms",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "drop_piece_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PieceType",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "time_taken_duration",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Duration",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_promotion_piece_type"
        },
        {
          "name": "_time_taken_ms"
        },
        {
          "name": "_castling_details"
        },
        {
          "name": "_remaining_clock_ms"
        },
        {
          "name": "_drop_piece_type"
        },
        {
          "name": "_time_taken_duration"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "PromotionPieceType",
      "value": [
        {
          "name": "PROMOTION_PIECE_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PROMOTION_PIECE_TYPE_KNIGHT",
          "number": 1
        },
        {
          "name": "PROMOTION_PIECE_TYPE_BISHOP",
          "number": 2
        },
        {
          "name": "PROMOTION_PIECE_TYPE_ROOK",
          "number": 3
        },
        {
          "name": "PROMOTION_PIECE_TYPE_QUEEN",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 9761.

```text
1FVQVJFX0U4ED0SDQoJU1FVQVJFX0Y4ED4SDQoJU1FVQVJFX0c4ED8SDQoJU1FVQVJFX0g4EEAaB4qmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/move.proto":"ChxjaGVzc2NvbS9jaGVzcy92MS9tb3ZlLnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSLOAQoPQ2FzdGxpbmdEZXRhaWxzEiwKCWtpbmdfZnJvbRgBIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlNxdWFyZRIqCgdraW5nX3RvGAIgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEiwKCXJvb2tfZnJvbRgDIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlNxdWFyZRIqCgdyb29rX3RvG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17431"></a>
## FND-17431: Full frontend descriptor: chesscom/chess/v1/chesscom_game_source.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/chesscom_game_source.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "ChesscomGameSource",
      "value": [
        {
          "name": "CHESSCOM_GAME_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_DAILY",
          "number": 1
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_LIVE",
          "number": 2
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_MASTER",
          "number": 3
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_PGN",
          "number": 4
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_VS_COMPUTER",
          "number": 5
        },
        {
          "name": "CHESSCOM_GAME_SOURCE_VS_COACH",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 11157.

```text
U9USU9OX1BJRUNFX1RZUEVfUk9PSxADEh4KGlBST01PVElPTl9QSUVDRV9UWVBFX1FVRUVOEAQaB4qmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/chesscom_game_source.proto":"CixjaGVzc2NvbS9jaGVzcy92MS9jaGVzc2NvbV9nYW1lX3NvdXJjZS5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEqigIKEkNoZXNzY29tR2FtZVNvdXJjZRIkCiBDSEVTU0NPTV9HQU1FX1NPVVJDRV9VTlNQRUNJRklFRBAAEh4KGkNIRVNTQ09NX0dBTUVfU09VUkNFX0RBSUxZEAESHQoZQ0hFU1NDT01fR0FNRV9TT1VSQ0VfTElWRRACEh8KG0NIRVNTQ09NX0dBT
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17432"></a>
## FND-17432: Full frontend descriptor: chesscom/chess/v1/score.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/score.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "Score",
      "field": [
        {
          "name": "score_centipawns_white",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_SINT32",
          "oneof_index": 0
        },
        {
          "name": "mate_in_white",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "mate_in_black",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "stalemate",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Stalemate",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "score"
        }
      ]
    },
    {
      "name": "Stalemate",
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 11663.

```text
fU09VUkNFX1ZTX0NPTVBVVEVSEAUSIQodQ0hFU1NDT01fR0FNRV9TT1VSQ0VfVlNfQ09BQ0gQBhoHiqYdAwoBAWIGcHJvdG8z","chesscom/chess/v1/score.proto":"Ch1jaGVzc2NvbS9jaGVzcy92MS9zY29yZS5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEioAEKBVNjb3JlEiAKFnNjb3JlX2NlbnRpcGF3bnNfd2hpdGUYASABKBFIABIXCg1tYXRlX2luX3doaXRlGAIgASgFSAASFwoNbWF0ZV9pbl9ibGFjaxgDIAEoBUgAEjEKCXN0YWxlbWF0ZRgEIAEoCzIcLmNoZXNzY29tLmNoZXNzLnYxLlN0YWxlbWF0ZUgAOgeCph0DCgEBQgcKBXNjb3JlIhQK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17433"></a>
## FND-17433: Full frontend descriptor: chesscom/chess/v1/arrow.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/arrow.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "Arrow",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ],
      "options": {}
    },
    {
      "name": "ArrowsAndSquares",
      "field": [
        {
          "name": "arrows",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Arrow"
        },
        {
          "name": "squares",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 12022.

```text
zY29tLmNoZXNzLnYxLlN0YWxlbWF0ZUgAOgeCph0DCgEBQgcKBXNjb3JlIhQKCVN0YWxlbWF0ZToHgqYdAwoBAWIGcHJvdG8z","chesscom/chess/v1/arrow.proto":"Ch1jaGVzc2NvbS9jaGVzcy92MS9hcnJvdy5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEiYAoFQXJyb3cSJwoEZnJvbRgBIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlNxdWFyZRIlCgJ0bxgCIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlNxdWFyZToHgqYdAwoBASJxChBBcnJvd3NBbmRTcXVhcmVzEigKBmFycm93cxgBIAMoCzIYLmNoZXNzY29tLmNoZXNzLnYxLkFycm93EioKB3Nx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17434"></a>
## FND-17434: Full frontend descriptor: chesscom/chess/v1/board_markings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/board_markings.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "ArrowMarking",
      "field": [
        {
          "name": "arrow",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Arrow"
        },
        {
          "name": "color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.MarkingColor"
        }
      ],
      "options": {}
    },
    {
      "name": "SquareMarking",
      "field": [
        {
          "name": "square",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.MarkingColor"
        }
      ],
      "options": {}
    },
    {
      "name": "BoardMarkings",
      "field": [
        {
          "name": "arrows",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArrowMarking"
        },
        {
          "name": "squares",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.SquareMarking"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "MarkingColor",
      "value": [
        {
          "name": "MARKING_COLOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MARKING_COLOR_RED",
          "number": 1
        },
        {
          "name": "MARKING_COLOR_BLUE",
          "number": 2
        },
        {
          "name": "MARKING_COLOR_GREEN",
          "number": 3
        },
        {
          "name": "MARKING_COLOR_ORANGE",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 12419.

```text
XNzLnYxLkFycm93EioKB3NxdWFyZXMYAiADKA4yGS5jaGVzc2NvbS5jaGVzcy52MS5TcXVhcmU6B4KmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/board_markings.proto":"CiZjaGVzc2NvbS9jaGVzcy92MS9ib2FyZF9tYXJraW5ncy5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEicAoMQXJyb3dNYXJraW5nEicKBWFycm93GAEgASgLMhguY2hlc3Njb20uY2hlc3MudjEuQXJyb3cSLgoFY29sb3IYAiABKA4yHy5jaGVzc2NvbS5jaGVzcy52MS5NYXJraW5nQ29sb3I6B4KmHQMKAQEicwoNU3F1YXJlTWFya2luZxIpCgZzcXVhcmUYASABKA4yGS5
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17435"></a>
## FND-17435: Full frontend descriptor: chesscom/chess/v1/file.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/file.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "File",
      "value": [
        {
          "name": "FILE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FILE_A",
          "number": 1
        },
        {
          "name": "FILE_B",
          "number": 2
        },
        {
          "name": "FILE_C",
          "number": 3
        },
        {
          "name": "FILE_D",
          "number": 4
        },
        {
          "name": "FILE_E",
          "number": 5
        },
        {
          "name": "FILE_F",
          "number": 6
        },
        {
          "name": "FILE_G",
          "number": 7
        },
        {
          "name": "FILE_H",
          "number": 8
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 13235.

```text
MVUUQAhIXChNNQVJLSU5HX0NPTE9SX0dSRUVOEAMSGAoUTUFSS0lOR19DT0xPUl9PUkFOR0UQBBoHiqYdAwoBAWIGcHJvdG8z","chesscom/chess/v1/file.proto":"ChxjaGVzc2NvbS9jaGVzcy92MS9maWxlLnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSqFAQoERmlsZRIUChBGSUxFX1VOU1BFQ0lGSUVEEAASCgoGRklMRV9BEAESCgoGRklMRV9CEAISCgoGRklMRV9DEAMSCgoGRklMRV9EEAQSCgoGRklMRV9FEAUSCgoGRklMRV9GEAYSCgoGRklMRV9HEAcSCgoGRklMRV9IEAgaB4qmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/position.p
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17436"></a>
## FND-17436: Full frontend descriptor: chesscom/chess/v1/position.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/position.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "Position",
      "field": [
        {
          "name": "pieces",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Placement"
        },
        {
          "name": "active_color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "castling_rights",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.CastlingRight"
        },
        {
          "name": "en_passant_square",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "halfmove_clock",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "fullmove_number",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "in_check",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_en_passant_square"
        },
        {
          "name": "_in_check"
        }
      ]
    },
    {
      "name": "Placement",
      "field": [
        {
          "name": "piece",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Piece"
        },
        {
          "name": "square",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        }
      ],
      "options": {}
    },
    {
      "name": "CastlingRight",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "rook_file",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.File"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 13527.

```text
klMRV9EEAQSCgoGRklMRV9FEAUSCgoGRklMRV9GEAYSCgoGRklMRV9HEAcSCgoGRklMRV9IEAgaB4qmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/position.proto":"CiBjaGVzc2NvbS9jaGVzcy92MS9wb3NpdGlvbi5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEi0gIKCFBvc2l0aW9uEiwKBnBpZWNlcxgBIAMoCzIcLmNoZXNzY29tLmNoZXNzLnYxLlBsYWNlbWVudBIuCgxhY3RpdmVfY29sb3IYAiABKA4yGC5jaGVzc2NvbS5jaGVzcy52MS5Db2xvchI5Cg9jYXN0bGluZ19yaWdodHMYAyADKAsyIC5jaGVzc2NvbS5jaGVzcy52MS5DYXN0bGluZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17437"></a>
## FND-17437: Full frontend descriptor: chesscom/chess/v1/game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/game.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "GameResult",
      "field": [
        {
          "name": "result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Result"
        },
        {
          "name": "result_type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.ResultType"
        }
      ],
      "options": {}
    },
    {
      "name": "Game",
      "field": [
        {
          "name": "starting_position",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Position"
        },
        {
          "name": "moves",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMove"
        },
        {
          "name": "metadata",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata"
        }
      ],
      "options": {}
    },
    {
      "name": "GameMove",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "metadata",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMoveMetadata",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "variations",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.MoveVariation"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_metadata"
        }
      ]
    },
    {
      "name": "GameMoveMetadata",
      "field": [
        {
          "name": "score",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Score",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "time_remaining_ms",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "comment_before",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "comments_after",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "nags",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_score"
        },
        {
          "name": "_time_remaining_ms"
        },
        {
          "name": "_comment_before"
        }
      ]
    },
    {
      "name": "MoveVariation",
      "field": [
        {
          "name": "moves",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMove"
        }
      ],
      "options": {}
    },
    {
      "name": "Rules",
      "field": [
        {
          "name": "is_chess960",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_is_chess960"
        }
      ]
    },
    {
      "name": "GameMetadata",
      "field": [
        {
          "name": "players",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.PlayerMetadata"
        },
        {
          "name": "time_control",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.TimeControl",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "timestamps",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Timestamps",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "result",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "rules",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Rules",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "chesscom_metadata",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ChesscomGameMetadata",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "pgn_headers",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata.PgnHeadersEntry"
        },
        {
          "name": "link",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "time_class",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "is_rated",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "PgnHeadersEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_time_control"
        },
        {
          "name": "_timestamps"
        },
        {
          "name": "_result"
        },
        {
          "name": "_rules"
        },
        {
          "name": "_chesscom_metadata"
        },
        {
          "name": "_link"
        },
        {
          "name": "_time_class"
        },
        {
          "name": "_is_rated"
        }
      ]
    },
    {
      "name": "Timestamps",
      "field": [
        {
          "name": "started_at",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "finished_at",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_started_at"
        },
        {
          "name": "_finished_at"
        }
      ]
    },
    {
      "name": "ChesscomGameMetadata",
      "field": [
        {
          "name": "game_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "legacy_game_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "eco_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "game_source",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.ChesscomGameSource",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_game_id"
        },
        {
          "name": "_legacy_game_id"
        },
        {
          "name": "_eco_id"
        },
        {
          "name": "_game_source"
        }
      ]
    },
    {
      "name": "PlayerMetadata",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "ratings",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Rating"
        },
        {
          "name": "name",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "chesscom_metadata",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ChesscomPlayerMetadata",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_name"
        },
        {
          "name": "_chesscom_metadata"
        }
      ]
    },
    {
      "name": "Rating",
      "field": [
        {
          "name": "rating",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_rating"
        }
      ]
    },
    {
      "name": "ChesscomPlayerMetadata",
      "field": [
        {
          "name": "user_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "legacy_user_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_user_id"
        },
        {
          "name": "_legacy_user_id"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 14391.

```text
XNzLnYxLkNvbG9yEioKCXJvb2tfZmlsZRgCIAEoDjIXLmNoZXNzY29tLmNoZXNzLnYxLkZpbGU6B4KmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/game.proto":"ChxjaGVzc2NvbS9jaGVzcy92MS9nYW1lLnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSJ1CgpHYW1lUmVzdWx0EikKBnJlc3VsdBgBIAEoDjIZLmNoZXNzY29tLmNoZXNzLnYxLlJlc3VsdBIyCgtyZXN1bHRfdHlwZRgCIAEoDjIdLmNoZXNzY29tLmNoZXNzLnYxLlJlc3VsdFR5cGU6CIKmHQQKAgECIqYBCgRHYW1lEjYKEXN0YXJ0aW5nX3Bvc2l0aW9uGAEgASgLMhsuY2hlc3Njb20uY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17438"></a>
## FND-17438: Full frontend descriptor: chesscom/chess/v1/game_phase.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/game_phase.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "GamePhase",
      "value": [
        {
          "name": "GAME_PHASE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PHASE_OPENING",
          "number": 1
        },
        {
          "name": "GAME_PHASE_MIDDLEGAME",
          "number": 2
        },
        {
          "name": "GAME_PHASE_ENDGAME",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 17523.

```text
GVnYWN5X3VzZXJfaWQYAiABKANIAYgBAToHgqYdAwoBAUIKCghfdXNlcl9pZEIRCg9fbGVnYWN5X3VzZXJfaWRiBnByb3RvMw","chesscom/chess/v1/game_phase.proto":"CiJjaGVzc2NvbS9jaGVzcy92MS9nYW1lX3BoYXNlLnByb3RvEhFjaGVzc2NvbS5jaGVzcy52MSp7CglHYW1lUGhhc2USGgoWR0FNRV9QSEFTRV9VTlNQRUNJRklFRBAAEhYKEkdBTUVfUEhBU0VfT1BFTklORxABEhkKFUdBTUVfUEhBU0VfTUlERExFR0FNRRACEhYKEkdBTUVfUEhBU0VfRU5ER0FNRRADGgeKph0DCgEBYgZwcm90bzM","chesscom/chess/v1/eco.proto":
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17439"></a>
## FND-17439: Full frontend descriptor: chesscom/chess/v1/eco.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/eco.proto",
  "package": "chesscom.chess.v1",
  "message_type": [
    {
      "name": "EcoFamily",
      "field": [
        {
          "name": "eco_family_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 17814.

```text
lORxABEhkKFUdBTUVfUEhBU0VfTUlERExFR0FNRRACEhYKEkdBTUVfUEhBU0VfRU5ER0FNRRADGgeKph0DCgEBYgZwcm90bzM","chesscom/chess/v1/eco.proto":"ChtjaGVzc2NvbS9jaGVzcy92MS9lY28ucHJvdG8SEWNoZXNzY29tLmNoZXNzLnYxIjkKCUVjb0ZhbWlseRIVCg1lY29fZmFtaWx5X2lkGAEgASgNEgwKBG5hbWUYAiABKAk6B4KmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/notation.proto":"CiBjaGVzc2NvbS9jaGVzcy92MS9ub3RhdGlvbi5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEqfwoMTW92ZU5vdGF0aW9uEh0KGU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17440"></a>
## FND-17440: Full frontend descriptor: chesscom/chess/v1/notation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/chess/v1/notation.proto",
  "package": "chesscom.chess.v1",
  "enum_type": [
    {
      "name": "MoveNotation",
      "value": [
        {
          "name": "MOVE_NOTATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_NOTATION_TCN",
          "number": 1
        },
        {
          "name": "MOVE_NOTATION_SAN",
          "number": 2
        },
        {
          "name": "MOVE_NOTATION_UCI_LAN",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 18001.

```text
XNzLnYxIjkKCUVjb0ZhbWlseRIVCg1lY29fZmFtaWx5X2lkGAEgASgNEgwKBG5hbWUYAiABKAk6B4KmHQMKAQFiBnByb3RvMw","chesscom/chess/v1/notation.proto":"CiBjaGVzc2NvbS9jaGVzcy92MS9ub3RhdGlvbi5wcm90bxIRY2hlc3Njb20uY2hlc3MudjEqfwoMTW92ZU5vdGF0aW9uEh0KGU1PVkVfTk9UQVRJT05fVU5TUEVDSUZJRUQQABIVChFNT1ZFX05PVEFUSU9OX1RDThABEhUKEU1PVkVfTk9UQVRJT05fU0FOEAISGQoVTU9WRV9OT1RBVElPTl9VQ0lfTEFOEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/engine/v1/score.pro
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17441"></a>
## FND-17441: Full frontend descriptor: chesscom/engine/v1/score.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/engine/v1/score.proto",
  "package": "chesscom.engine.v1",
  "message_type": [
    {
      "name": "Score",
      "field": [
        {
          "name": "score",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Score"
        },
        {
          "name": "depth",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "nodes",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "engine",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Engine"
        },
        {
          "name": "variation",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "strength",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Strength",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_strength"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 18293.

```text
1RDThABEhUKEU1PVkVfTk9UQVRJT05fU0FOEAISGQoVTU9WRV9OT1RBVElPTl9VQ0lfTEFOEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/engine/v1/score.proto":"Ch5jaGVzc2NvbS9lbmdpbmUvdjEvc2NvcmUucHJvdG8SEmNoZXNzY29tLmVuZ2luZS52MSLYAQoFU2NvcmUSJwoFc2NvcmUYASABKAsyGC5jaGVzc2NvbS5jaGVzcy52MS5TY29yZRINCgVkZXB0aBgCIAEoBRINCgVub2RlcxgGIAEoAxIqCgZlbmdpbmUYAyABKA4yGi5jaGVzc2NvbS5lbmdpbmUudjEuRW5naW5lEhEKCXZhcmlhdGlvbhgEIAEoBRIzCghzdHJlbmd0aBgFIAEoDjI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17442"></a>
## FND-17442: Full frontend descriptor: chesscom/engine/v1/evaluation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/engine/v1/evaluation.proto",
  "package": "chesscom.engine.v1",
  "message_type": [
    {
      "name": "Evaluation",
      "field": [
        {
          "name": "score",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score"
        },
        {
          "name": "variation",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 18701.

```text
0aBgFIAEoDjIcLmNoZXNzY29tLmVuZ2luZS52MS5TdHJlbmd0aEgAiAEBOgeCph0DCgEBQgsKCV9zdHJlbmd0aGIGcHJvdG8z","chesscom/engine/v1/evaluation.proto":"CiNjaGVzc2NvbS9lbmdpbmUvdjEvZXZhbHVhdGlvbi5wcm90bxISY2hlc3Njb20uZW5naW5lLnYxImsKCkV2YWx1YXRpb24SKAoFc2NvcmUYASABKAsyGS5jaGVzc2NvbS5lbmdpbmUudjEuU2NvcmUSKgoJdmFyaWF0aW9uGAIgAygLMhcuY2hlc3Njb20uY2hlc3MudjEuTW92ZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/move_classificat
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17443"></a>
## FND-17443: Full frontend descriptor: chesscom/explanation_engine/v1/move_classification.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/move_classification.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "EvalClassification",
      "field": [
        {
          "name": "move_classification",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "evaluation",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Evaluation"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "MoveClassification",
      "value": [
        {
          "name": "MOVE_CLASSIFICATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_CLASSIFICATION_BOOK",
          "number": 1
        },
        {
          "name": "MOVE_CLASSIFICATION_BRILLIANT",
          "number": 2
        },
        {
          "name": "MOVE_CLASSIFICATION_GREAT_FIND",
          "number": 3
        },
        {
          "name": "MOVE_CLASSIFICATION_BEST",
          "number": 4
        },
        {
          "name": "MOVE_CLASSIFICATION_EXCELLENT",
          "number": 5
        },
        {
          "name": "MOVE_CLASSIFICATION_GOOD",
          "number": 6
        },
        {
          "name": "MOVE_CLASSIFICATION_INACCURACY",
          "number": 7
        },
        {
          "name": "MOVE_CLASSIFICATION_MISTAKE",
          "number": 8
        },
        {
          "name": "MOVE_CLASSIFICATION_BLUNDER",
          "number": 9
        },
        {
          "name": "MOVE_CLASSIFICATION_MISSED",
          "number": 10
        },
        {
          "name": "MOVE_CLASSIFICATION_FORCED",
          "number": 11
        },
        {
          "name": "MOVE_CLASSIFICATION_TRICKY",
          "number": 20
        }
      ],
      "options": {},
      "reserved_range": [
        {
          "start": 12,
          "end": 19
        }
      ]
    },
    {
      "name": "MoveClassificationVersion",
      "value": [
        {
          "name": "MOVE_CLASSIFICATION_VERSION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MOVE_CLASSIFICATION_VERSION_V2",
          "number": 1
        },
        {
          "name": "MOVE_CLASSIFICATION_VERSION_V3",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 18974.

```text
pbmUudjEuU2NvcmUSKgoJdmFyaWF0aW9uGAIgAygLMhcuY2hlc3Njb20uY2hlc3MudjEuTW92ZToHgqYdAwoBAWIGcHJvdG8z","chesscom/explanation_engine/v1/move_classification.proto":"CjhjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbW92ZV9jbGFzc2lmaWNhdGlvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIqIBChJFdmFsQ2xhc3NpZmljYXRpb24STwoTbW92ZV9jbGFzc2lmaWNhdGlvbhgBIAEoDjIyLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Nb3ZlQ2xhc3NpZmljYXRpb24SM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17444"></a>
## FND-17444: Full frontend descriptor: chesscom/explanation_engine/v1/language.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/language.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "Locale",
      "value": [
        {
          "name": "LOCALE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "LOCALE_DE_DE",
          "number": 1
        },
        {
          "name": "LOCALE_EN_US",
          "number": 2
        },
        {
          "name": "LOCALE_ES_ES",
          "number": 3
        },
        {
          "name": "LOCALE_FR_FR",
          "number": 4
        },
        {
          "name": "LOCALE_IT_IT",
          "number": 5
        },
        {
          "name": "LOCALE_PL_PL",
          "number": 6
        },
        {
          "name": "LOCALE_PT_PT",
          "number": 7
        },
        {
          "name": "LOCALE_RU_RU",
          "number": 8
        },
        {
          "name": "LOCALE_TR_TR",
          "number": 9
        },
        {
          "name": "LOCALE_AR_SA",
          "number": 10
        },
        {
          "name": "LOCALE_ID_ID",
          "number": 11
        },
        {
          "name": "LOCALE_KO_KR",
          "number": 12
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 20222.

```text
UNBVElPTl9WRVJTSU9OX1YyEAESIgoeTU9WRV9DTEFTU0lGSUNBVElPTl9WRVJTSU9OX1YzEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/language.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbGFuZ3VhZ2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSqBAgoGTG9jYWxlEhYKEkxPQ0FMRV9VTlNQRUNJRklFRBAAEhAKDExPQ0FMRV9ERV9ERRABEhAKDExPQ0FMRV9FTl9VUxACEhAKDExPQ0FMRV9FU19FUxADEhAKDExPQ0FMRV9GUl9GUhAEEhAKDExPQ0FMRV9JVF9JVBAF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17445"></a>
## FND-17445: Full frontend descriptor: chesscom/explanation_engine/v1/speech.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/speech.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SentenceFragment",
      "field": [
        {
          "name": "fragment",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "arrows_and_squares",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.ArrowsAndSquares"
        }
      ],
      "options": {}
    },
    {
      "name": "Sentence",
      "field": [
        {
          "name": "sentence_fragments",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SentenceFragment"
        },
        {
          "name": "audio_url_hash",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "Speech",
      "field": [
        {
          "name": "sentences",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Sentence"
        }
      ],
      "options": {}
    },
    {
      "name": "SpeechForLocale",
      "field": [
        {
          "name": "locale",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Locale"
        },
        {
          "name": "speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 20736.

```text
AJEhAKDExPQ0FMRV9BUl9TQRAKEhAKDExPQ0FMRV9JRF9JRBALEhAKDExPQ0FMRV9LT19LUhAMGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/speech.proto":"CitjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc3BlZWNoLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEibgoQU2VudGVuY2VGcmFnbWVudBIQCghmcmFnbWVudBgBIAEoCRI/ChJhcnJvd3NfYW5kX3NxdWFyZXMYAiABKAsyIy5jaGVzc2NvbS5jaGVzcy52MS5BcnJvd3NBbmRTcXVhcmVzOgeCph0DCgEBInkKCFNlbnRlbmNlEkwKEn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17446"></a>
## FND-17446: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_non_chess_text.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_non_chess_text.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetNonChessTextRequest",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.NonChessTextType"
        }
      ],
      "options": {}
    },
    {
      "name": "GetNonChessTextResponse",
      "field": [
        {
          "name": "speech",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "NonChessTextType",
      "value": [
        {
          "name": "NON_CHESS_TEXT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL",
          "number": 1
        },
        {
          "name": "NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL",
          "number": 2
        },
        {
          "name": "NON_CHESS_TEXT_TYPE_RESUME_GAME",
          "number": 3
        },
        {
          "name": "NON_CHESS_TEXT_TYPE_SWITCHED_COACH",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 21507.

```text
jYKBnNwZWVjaBgCIAEoCzImLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5TcGVlY2g6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/feature_get_non_chess_text.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfbm9uX2NoZXNzX3RleHQucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJhChZHZXROb25DaGVzc1RleHRSZXF1ZXN0Ej4KBHR5cGUYASABKA4yMC5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuTm9uQ2hlc3NUZXh0VHlwZToHgq
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17447"></a>
## FND-17447: Full frontend descriptor: chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GetIllegalMoveExplanationRequest",
      "field": [
        {
          "name": "attempted_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        }
      ],
      "options": {}
    },
    {
      "name": "GetIllegalMoveExplanationResponse",
      "field": [
        {
          "name": "illegal_move_case",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.IllegalMoveCase",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        },
        {
          "name": "board_markings",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.BoardMarkings"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_illegal_move_case"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "IllegalMoveCase",
      "value": [
        {
          "name": "ILLEGAL_MOVE_CASE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ILLEGAL_MOVE_CASE_IN_CHECK",
          "number": 1
        },
        {
          "name": "ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING",
          "number": 2
        },
        {
          "name": "ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES",
          "number": 3
        },
        {
          "name": "ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES",
          "number": 4
        },
        {
          "name": "ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE",
          "number": 5
        },
        {
          "name": "ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES",
          "number": 6
        },
        {
          "name": "ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED",
          "number": 7
        },
        {
          "name": "ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK",
          "number": 8
        },
        {
          "name": "ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK",
          "number": 9
        }
      ],
      "options": {}
    },
    {
      "name": "IllegalMoveExplanationMode",
      "value": [
        {
          "name": "ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ILLEGAL_MOVE_EXPLANATION_MODE_ALL",
          "number": 1
        },
        {
          "name": "ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 22275.

```text
BFX1JFU1VNRV9HQU1FEAMSJgoiTk9OX0NIRVNTX1RFWFRfVFlQRV9TV0lUQ0hFRF9DT0FDSBAEGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto":"CkljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9nZXRfaWxsZWdhbF9tb3ZlX2V4cGxhbmF0aW9uLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiXAogR2V0SWxsZWdhbE1vdmVFeHBsYW5hdGlvblJlcXVlc3QSLwoOYXR0ZW1wdGVkX21vdmUYASABKAsyFy5jaGVzc2NvbS5jaGVz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17448"></a>
## FND-17448: Full frontend descriptor: chesscom/explanation_engine/v1/charm_inference_code.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/charm_inference_code.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CharmInferenceCode",
      "field": [
        {
          "name": "model_key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ratings",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "engine_line_move_indexes",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "coded_values",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES"
        }
      ],
      "options": {}
    },
    {
      "name": "NodeCharmInferenceCodes",
      "field": [
        {
          "name": "inferences",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCode"
        }
      ],
      "options": {}
    },
    {
      "name": "CharmInferenceCodes",
      "field": [
        {
          "name": "codebook_version",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "nodes",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry"
        }
      ],
      "nested_type": [
        {
          "name": "NodesEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.NodeCharmInferenceCodes"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 23856.

```text
0VYUExBTkFUSU9OX01PREVfU1VQUFJFU1NfUElFQ0VfSEFTX09USEVSX0xFR0FMX01PVkVTEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/charm_inference_code.proto":"CjljaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY2hhcm1faW5mZXJlbmNlX2NvZGUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJ5ChJDaGFybUluZmVyZW5jZUNvZGUSEQoJbW9kZWxfa2V5GAEgASgJEg8KB3JhdGluZ3MYAiADKAUSIAoYZW5naW5lX2xpbmVfbW92ZV9pbmRleGVzGAMgAygNEhQKDGNvZGVkX3Zh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17449"></a>
## FND-17449: Full frontend descriptor: chesscom/explanation_engine/v1/coach_state.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/coach_state.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CoachState",
      "field": [
        {
          "name": "ply_since_retry_offered",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "ply_since_flip_board_offered",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_ply_since_retry_offered"
        },
        {
          "name": "_ply_since_flip_board_offered"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 24681.

```text
XNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ob2RlQ2hhcm1JbmZlcmVuY2VDb2RlczoCOAE6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/coach_state.proto":"CjBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY29hY2hfc3RhdGUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKjAQoKQ29hY2hTdGF0ZRIkChdwbHlfc2luY2VfcmV0cnlfb2ZmZXJlZBgBIAEoDUgAiAEBEikKHHBseV9zaW5jZV9mbGlwX2JvYXJkX29mZmVyZWQYAiABKA1IAYgBAToHgqYdAwoBAUIaChhfcGx5X3NpbmNlX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17450"></a>
## FND-17450: Full frontend descriptor: chesscom/explanation_engine/v1/compact_charm_inference.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/compact_charm_inference.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "CompactCharmInference",
      "field": [
        {
          "name": "model_key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ratings",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "uci_moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "move_probabilities",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "expected_points",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "rank_probabilities",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "strength_probabilities",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "time_taken_probabilities",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "ldw_probabilities",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "strength_rating_sensitive_probabilities",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "engine_line_move_indexes",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "move_indexes",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    },
    {
      "name": "CompactCharmInferences",
      "field": [
        {
          "name": "inferences",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CompactCharmInference"
        },
        {
          "name": "quantization_bits",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 25077.

```text
woBAUIaChhfcGx5X3NpbmNlX3JldHJ5X29mZmVyZWRCHwodX3BseV9zaW5jZV9mbGlwX2JvYXJkX29mZmVyZWRiBnByb3RvMw","chesscom/explanation_engine/v1/compact_charm_inference.proto":"CjxjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY29tcGFjdF9jaGFybV9pbmZlcmVuY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSLyAgoVQ29tcGFjdENoYXJtSW5mZXJlbmNlEhEKCW1vZGVsX2tleRgBIAEoCRIPCgdyYXRpbmdzGAIgAygFEhUKCXVjaV9tb3ZlcxgDIAMoCUICGAESGgoSbW92ZV9wcm9iY
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17451"></a>
## FND-17451: Full frontend descriptor: chesscom/explanation_engine/v1/game_point_info.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_point_info.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GamePointInfo",
      "field": [
        {
          "name": "game_point",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "score",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "parent_game_point",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "child_game_points",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "null_move_child_game_point",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "played_child_game_point",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "is_played",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_move"
        },
        {
          "name": "_score"
        },
        {
          "name": "_parent_game_point"
        },
        {
          "name": "_null_move_child_game_point"
        },
        {
          "name": "_played_child_game_point"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 25961.

```text
2luZS52MS5Db21wYWN0Q2hhcm1JbmZlcmVuY2USGQoRcXVhbnRpemF0aW9uX2JpdHMYAiABKAU6B4KmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/game_point_info.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9wb2ludF9pbmZvLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiiAMKDUdhbWVQb2ludEluZm8SEgoKZ2FtZV9wb2ludBgBIAEoBRIqCgRtb3ZlGAIgASgLMhcuY2hlc3Njb20uY2hlc3MudjEuTW92ZUgAiAEBEi0KBXNjb3JlGAMgASgLMhkuY2hlc3Njb20uZW5na
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17452"></a>
## FND-17452: Full frontend descriptor: chesscom/explanation_engine/v1/game_phase.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_phase.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GamePhaseTransitions",
      "field": [
        {
          "name": "middlegame_starting_game_point",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "endgame_starting_game_point",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_middlegame_starting_game_point"
        },
        {
          "name": "_endgame_starting_game_point"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GamePhaseVersion",
      "value": [
        {
          "name": "GAME_PHASE_VERSION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PHASE_VERSION_1",
          "number": 1
        },
        {
          "name": "GAME_PHASE_VERSION_2",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 26671.

```text
fcG9pbnRCHQobX251bGxfbW92ZV9jaGlsZF9nYW1lX3BvaW50QhoKGF9wbGF5ZWRfY2hpbGRfZ2FtZV9wb2ludGIGcHJvdG8z","chesscom/explanation_engine/v1/game_phase.proto":"Ci9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9waGFzZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIo4CChRHYW1lUGhhc2VUcmFuc2l0aW9ucxJaCh5taWRkbGVnYW1lX3N0YXJ0aW5nX2dhbWVfcG9pbnQYASABKAsyLS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVBvaW50SW5mb0gAiAEBElcKG2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17453"></a>
## FND-17453: Full frontend descriptor: chesscom/explanation_engine/v1/game_arc.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_arc.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "GameArc",
      "value": [
        {
          "name": "GAME_ARC_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_ARC_BALANCED",
          "number": 1
        },
        {
          "name": "GAME_ARC_SUDDEN",
          "number": 2
        },
        {
          "name": "GAME_ARC_SMOOTH",
          "number": 3
        },
        {
          "name": "GAME_ARC_ROUGH",
          "number": 4
        },
        {
          "name": "GAME_ARC_THROWAWAY",
          "number": 5
        },
        {
          "name": "GAME_ARC_WILD",
          "number": 6
        },
        {
          "name": "GAME_ARC_SHARP",
          "number": 7
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 27363.

```text
VEEAASGAoUR0FNRV9QSEFTRV9WRVJTSU9OXzEQARIYChRHQU1FX1BIQVNFX1ZFUlNJT05fMhACGgeKph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/game_arc.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9hcmMucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSq3AQoHR2FtZUFyYxIYChRHQU1FX0FSQ19VTlNQRUNJRklFRBAAEhUKEUdBTUVfQVJDX0JBTEFOQ0VEEAESEwoPR0FNRV9BUkNfU1VEREVOEAISEwoPR0FNRV9BUkNfU01PT1RIEAMSEgoOR0FNRV9BUkNfUk9VR0gQBBIW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17454"></a>
## FND-17454: Full frontend descriptor: chesscom/explanation_engine/v1/accuracy.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/accuracy.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "PieceTypeAccuracy",
      "field": [
        {
          "name": "piece_type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.PieceType"
        },
        {
          "name": "accuracy_score",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ]
    },
    {
      "name": "GamePhaseAccuracy",
      "field": [
        {
          "name": "game_phase",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.GamePhase"
        },
        {
          "name": "accuracy_score",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ]
    },
    {
      "name": "ColorAccuracy",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "accuracy_by_piece_type",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PieceTypeAccuracy"
        },
        {
          "name": "accuracy_by_game_phase",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseAccuracy"
        },
        {
          "name": "accuracy_overall",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        },
        {
          "name": "avg_centipawn_loss",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_DOUBLE"
        }
      ]
    },
    {
      "name": "VariationAccuracy",
      "field": [
        {
          "name": "accuracy_by_color",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ColorAccuracy"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "AccuracyAlgorithm",
      "value": [
        {
          "name": "ACCURACY_ALGORITHM_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ACCURACY_ALGORITHM_CAPS2",
          "number": 1
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 27778.

```text
QBBIWChJHQU1FX0FSQ19USFJPV0FXQVkQBRIRCg1HQU1FX0FSQ19XSUxEEAYSEgoOR0FNRV9BUkNfU0hBUlAQB2IGcHJvdG8z","chesscom/explanation_engine/v1/accuracy.proto":"Ci1jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvYWNjdXJhY3kucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSJdChFQaWVjZVR5cGVBY2N1cmFjeRIwCgpwaWVjZV90eXBlGAEgASgOMhwuY2hlc3Njb20uY2hlc3MudjEuUGllY2VUeXBlEhYKDmFjY3VyYWN5X3Njb3JlGAIgASgBIl0KEUdhbWVQaGFzZUFjY3VyYWN5EjAKCmdhbWVf
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17455"></a>
## FND-17455: Full frontend descriptor: chesscom/explanation_engine/v1/report_card.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/report_card.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GamePhaseGlyph",
      "field": [
        {
          "name": "game_phase",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.GamePhase"
        },
        {
          "name": "glyph",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        }
      ]
    },
    {
      "name": "PlayerReportCard",
      "field": [
        {
          "name": "color",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color"
        },
        {
          "name": "glyph_by_phase",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseGlyph"
        },
        {
          "name": "effective_rating",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    },
    {
      "name": "ReportCard",
      "field": [
        {
          "name": "report_card_by_color",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PlayerReportCard"
        },
        {
          "name": "speech",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 28813.

```text
iCh5BQ0NVUkFDWV9BTEdPUklUSE1fVU5TUEVDSUZJRUQQABIcChhBQ0NVUkFDWV9BTEdPUklUSE1fQ0FQUzIQAWIGcHJvdG8z","chesscom/explanation_engine/v1/report_card.proto":"CjBjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvcmVwb3J0X2NhcmQucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSKFAQoOR2FtZVBoYXNlR2x5cGgSMAoKZ2FtZV9waGFzZRgBIAEoDjIcLmNoZXNzY29tLmNoZXNzLnYxLkdhbWVQaGFzZRJBCgVnbHlwaBgCIAEoDjIyLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Nb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17456"></a>
## FND-17456: Full frontend descriptor: chesscom/api/v1/pagination.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/pagination.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "RequestPagination",
      "field": [
        {
          "name": "page_size",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "page_token",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_page_size"
        },
        {
          "name": "_page_token"
        }
      ]
    },
    {
      "name": "ResponsePagination",
      "field": [
        {
          "name": "next_page_token",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "total_size",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_next_page_token"
        },
        {
          "name": "_total_size"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 29529.

```text
C5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuUGxheWVyUmVwb3J0Q2FyZBIOCgZzcGVlY2gYAiABKAliBnByb3RvMw","chesscom/api/v1/pagination.proto":"CiBjaGVzc2NvbS9hcGkvdjEvcGFnaW5hdGlvbi5wcm90bxIPY2hlc3Njb20uYXBpLnYxImoKEVJlcXVlc3RQYWdpbmF0aW9uEhYKCXBhZ2Vfc2l6ZRgBIAEoBUgAiAEBEhcKCnBhZ2VfdG9rZW4YAiABKAlIAYgBAToHgqYdAwoBAUIMCgpfcGFnZV9zaXplQg0KC19wYWdlX3Rva2VuIncKElJlc3BvbnNlUGFnaW5hdGlvbhIcCg9uZXh0X3BhZ2VfdG9rZW4YASABKAlIAIgBARIXC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17457"></a>
## FND-17457: Full frontend descriptor: chesscom/api/v1/location.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/location.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Location",
      "field": [
        {
          "name": "country_code",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "city",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "region",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "continent_code",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "postal_code",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "latitude",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "longitude",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "timezone",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "asn",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_city"
        },
        {
          "name": "_region"
        },
        {
          "name": "_continent_code"
        },
        {
          "name": "_postal_code"
        },
        {
          "name": "_latitude"
        },
        {
          "name": "_longitude"
        },
        {
          "name": "_timezone"
        },
        {
          "name": "_asn"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 29951.

```text
0b3RhbF9zaXplGAIgASgFSAGIAQE6B4KmHQMKAQFCEgoQX25leHRfcGFnZV90b2tlbkINCgtfdG90YWxfc2l6ZWIGcHJvdG8z","chesscom/api/v1/location.proto":"Ch5jaGVzc2NvbS9hcGkvdjEvbG9jYXRpb24ucHJvdG8SD2NoZXNzY29tLmFwaS52MSLIAgoITG9jYXRpb24SFAoMY291bnRyeV9jb2RlGAEgASgJEhEKBGNpdHkYAiABKAlIAIgBARITCgZyZWdpb24YAyABKAlIAYgBARIbCg5jb250aW5lbnRfY29kZRgEIAEoCUgCiAEBEhgKC3Bvc3RhbF9jb2RlGAUgASgJSAOIAQESFQoIbGF0aXR1ZGUYBiABKAJIBIgBARIWCglsb25naXR1ZGU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17458"></a>
## FND-17458: Full frontend descriptor: chesscom/api/v1/platform.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/platform.proto",
  "package": "chesscom.api.v1",
  "enum_type": [
    {
      "name": "Platform",
      "value": [
        {
          "name": "PLATFORM_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLATFORM_IOS",
          "number": 1
        },
        {
          "name": "PLATFORM_ANDROID",
          "number": 2
        },
        {
          "name": "PLATFORM_WEB",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 30505.

```text
UIOCgxfcG9zdGFsX2NvZGVCCwoJX2xhdGl0dWRlQgwKCl9sb25naXR1ZGVCCwoJX3RpbWV6b25lQgYKBF9hc25iBnByb3RvMw","chesscom/api/v1/platform.proto":"Ch5jaGVzc2NvbS9hcGkvdjEvcGxhdGZvcm0ucHJvdG8SD2NoZXNzY29tLmFwaS52MSpnCghQbGF0Zm9ybRIYChRQTEFURk9STV9VTlNQRUNJRklFRBAAEhAKDFBMQVRGT1JNX0lPUxABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhIQCgxQTEFURk9STV9XRUIQAxoHiqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/asset.proto":"ChtjaGVzc2NvbS9hcGkvdjEvYXNzZXQucHJvdG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17459"></a>
## FND-17459: Full frontend descriptor: chesscom/api/v1/asset.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/asset.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Asset",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "key",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "content_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "url",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "alt_text",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_content_type"
        },
        {
          "name": "_url"
        },
        {
          "name": "_alt_text"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 30757.

```text
KDFBMQVRGT1JNX0lPUxABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhIQCgxQTEFURk9STV9XRUIQAxoHiqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/asset.proto":"ChtjaGVzc2NvbS9hcGkvdjEvYXNzZXQucHJvdG8SD2NoZXNzY29tLmFwaS52MSKWAQoFQXNzZXQSDAoEbmFtZRgBIAEoCRILCgNrZXkYAiABKAkSGQoMY29udGVudF90eXBlGAMgASgJSACIAQESEAoDdXJsGAQgASgJSAGIAQESFQoIYWx0X3RleHQYBSABKAlIAogBAToIgqYdBAoCAQJCDwoNX2NvbnRlbnRfdHlwZUIGCgRfdXJsQgsKCV9hbHRfdGV4dGIGcHJvdG8z","chesscom/ap
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17460"></a>
## FND-17460: Full frontend descriptor: chesscom/api/v1/date.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/date.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Date",
      "field": [
        {
          "name": "year",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "month",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "day",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 31066.

```text
0X3RleHQYBSABKAlIAogBAToIgqYdBAoCAQJCDwoNX2NvbnRlbnRfdHlwZUIGCgRfdXJsQgsKCV9hbHRfdGV4dGIGcHJvdG8z","chesscom/api/v1/date.proto":"ChpjaGVzc2NvbS9hcGkvdjEvZGF0ZS5wcm90bxIPY2hlc3Njb20uYXBpLnYxIjoKBERhdGUSDAoEeWVhchgBIAEoBRINCgVtb250aBgCIAEoBRILCgNkYXkYAyABKAU6CIKmHQQKAgECYgZwcm90bzM","chesscom/api/v1/semantic_version.proto":"CiZjaGVzc2NvbS9hcGkvdjEvc2VtYW50aWNfdmVyc2lvbi5wcm90bxIPY2hlc3Njb20uYXBpLnYxIkcKD1NlbWFudGljVmVy
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17461"></a>
## FND-17461: Full frontend descriptor: chesscom/api/v1/semantic_version.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/semantic_version.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "SemanticVersion",
      "field": [
        {
          "name": "major",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "minor",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "patch",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 31249.

```text
BpLnYxIjoKBERhdGUSDAoEeWVhchgBIAEoBRINCgVtb250aBgCIAEoBRILCgNkYXkYAyABKAU6CIKmHQQKAgECYgZwcm90bzM","chesscom/api/v1/semantic_version.proto":"CiZjaGVzc2NvbS9hcGkvdjEvc2VtYW50aWNfdmVyc2lvbi5wcm90bxIPY2hlc3Njb20uYXBpLnYxIkcKD1NlbWFudGljVmVyc2lvbhINCgVtYWpvchgBIAEoBRINCgVtaW5vchgCIAEoBRINCgVwYXRjaBgDIAEoBToHgqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/decimal.proto":"Ch1jaGVzc2NvbS9hcGkvdjEvZGVjaW1hbC5wcm90bxIPY2hlc3Njb20uYXBp
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17462"></a>
## FND-17462: Full frontend descriptor: chesscom/api/v1/decimal.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/decimal.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Decimal",
      "field": [
        {
          "name": "value",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT64"
        },
        {
          "name": "scale",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 31477.

```text
udGljVmVyc2lvbhINCgVtYWpvchgBIAEoBRINCgVtaW5vchgCIAEoBRINCgVwYXRjaBgDIAEoBToHgqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/decimal.proto":"Ch1jaGVzc2NvbS9hcGkvdjEvZGVjaW1hbC5wcm90bxIPY2hlc3Njb20uYXBpLnYxIjAKB0RlY2ltYWwSDQoFdmFsdWUYASABKAMSDQoFc2NhbGUYAiABKAU6B4KmHQMKAQFiBnByb3RvMw","chesscom/api/v1/country.proto":"Ch1jaGVzc2NvbS9hcGkvdjEvY291bnRyeS5wcm90bxIPY2hlc3Njb20uYXBpLnYxIlMKB0NvdW50cnkSCgoCaWQYASABKAUSDAoEbmFtZRgCIAE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17463"></a>
## FND-17463: Full frontend descriptor: chesscom/api/v1/country.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/country.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Country",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name_localized",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "code",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 31654.

```text
2hlc3Njb20uYXBpLnYxIjAKB0RlY2ltYWwSDQoFdmFsdWUYASABKAMSDQoFc2NhbGUYAiABKAU6B4KmHQMKAQFiBnByb3RvMw","chesscom/api/v1/country.proto":"Ch1jaGVzc2NvbS9hcGkvdjEvY291bnRyeS5wcm90bxIPY2hlc3Njb20uYXBpLnYxIlMKB0NvdW50cnkSCgoCaWQYASABKAUSDAoEbmFtZRgCIAEoCRIWCg5uYW1lX2xvY2FsaXplZBgDIAEoCRIMCgRjb2RlGAQgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/api/v1/money.proto":"ChtjaGVzc2NvbS9hcGkvdjEvbW9uZXkucHJvdG8SD2NoZXNzY29tLmFwaS52MSI3CgV
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17464"></a>
## FND-17464: Full frontend descriptor: chesscom/api/v1/money.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/money.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Money",
      "field": [
        {
          "name": "amount",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "currency_code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 31877.

```text
BKAUSDAoEbmFtZRgCIAEoCRIWCg5uYW1lX2xvY2FsaXplZBgDIAEoCRIMCgRjb2RlGAQgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/api/v1/money.proto":"ChtjaGVzc2NvbS9hcGkvdjEvbW9uZXkucHJvdG8SD2NoZXNzY29tLmFwaS52MSI3CgVNb25leRIOCgZhbW91bnQYASABKAkSFQoNY3VycmVuY3lfY29kZRgCIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/i18n.proto":"ChpjaGVzc2NvbS9hcGkvdjEvaTE4bi5wcm90bxIPY2hlc3Njb20uYXBpLnYxIk0KCExhbmd1YWdlEg4KBmxvY2FsZRgBIAEoCRIYCgtuYXRpdm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17465"></a>
## FND-17465: Full frontend descriptor: chesscom/api/v1/i18n.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/i18n.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Language",
      "field": [
        {
          "name": "locale",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "native_name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_native_name"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 32058.

```text
tLmFwaS52MSI3CgVNb25leRIOCgZhbW91bnQYASABKAkSFQoNY3VycmVuY3lfY29kZRgCIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/api/v1/i18n.proto":"ChpjaGVzc2NvbS9hcGkvdjEvaTE4bi5wcm90bxIPY2hlc3Njb20uYXBpLnYxIk0KCExhbmd1YWdlEg4KBmxvY2FsZRgBIAEoCRIYCgtuYXRpdmVfbmFtZRgCIAEoCUgAiAEBOgeCph0DCgEBQg4KDF9uYXRpdmVfbmFtZWIGcHJvdG8z","chesscom/api/v1/speech.proto":"ChxjaGVzc2NvbS9hcGkvdjEvc3BlZWNoLnByb3RvEg9jaGVzc2NvbS5hcGkudjEiOAoGU3BlZWNoEgwKB
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17466"></a>
## FND-17466: Full frontend descriptor: chesscom/api/v1/speech.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/speech.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "Speech",
      "field": [
        {
          "name": "text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "audio_url_hash",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 32266.

```text
KBmxvY2FsZRgBIAEoCRIYCgtuYXRpdmVfbmFtZRgCIAEoCUgAiAEBOgeCph0DCgEBQg4KDF9uYXRpdmVfbmFtZWIGcHJvdG8z","chesscom/api/v1/speech.proto":"ChxjaGVzc2NvbS9hcGkvdjEvc3BlZWNoLnByb3RvEg9jaGVzc2NvbS5hcGkudjEiOAoGU3BlZWNoEgwKBHRleHQYASABKAkSFgoOYXVkaW9fdXJsX2hhc2gYAiABKAk6CIKmHQQKAgECYgZwcm90bzM","chesscom/proto_options/configurator/v1/configurator_options.proto":"CkFjaGVzc2NvbS9wcm90b19vcHRpb25zL2NvbmZpZ3VyYXRvci92MS9jb25maWd1cmF
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17467"></a>
## FND-17467: Full frontend descriptor: chesscom/proto_options/configurator/v1/configurator_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/configurator/v1/configurator_options.proto",
  "package": "chesscom.proto_options.configurator.v1",
  "message_type": [
    {
      "name": "ConfiguratorMessageOptions",
      "field": [
        {
          "name": "configurable",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "configurator",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 91000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.configurator.v1.ConfiguratorMessageOptions",
      "json_name": "configurator",
      "proto3_optional": true
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 32451.

```text
5hcGkudjEiOAoGU3BlZWNoEgwKBHRleHQYASABKAkSFgoOYXVkaW9fdXJsX2hhc2gYAiABKAk6CIKmHQQKAgECYgZwcm90bzM","chesscom/proto_options/configurator/v1/configurator_options.proto":"CkFjaGVzc2NvbS9wcm90b19vcHRpb25zL2NvbmZpZ3VyYXRvci92MS9jb25maWd1cmF0b3Jfb3B0aW9ucy5wcm90bxImY2hlc3Njb20ucHJvdG9fb3B0aW9ucy5jb25maWd1cmF0b3IudjEiMgoaQ29uZmlndXJhdG9yTWVzc2FnZU9wdGlvbnMSFAoMY29uZmlndXJhYmxlGAEgASgIOowBCgxjb25maWd1cmF0b3ISHy5nb29nbGUucHJv
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17468"></a>
## FND-17468: Full frontend descriptor: chesscom/api/v1/error.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/error.proto",
  "package": "chesscom.api.v1",
  "message_type": [
    {
      "name": "TwirpError",
      "field": [
        {
          "name": "msg",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "code",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "meta",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.TwirpError.MetaEntry"
        }
      ],
      "nested_type": [
        {
          "name": "MetaEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 32936.

```text
GlvbnMuY29uZmlndXJhdG9yLnYxLkNvbmZpZ3VyYXRvck1lc3NhZ2VPcHRpb25zUgxjb25maWd1cmF0b3KIAQFiBnByb3RvMw","chesscom/api/v1/error.proto":"ChtjaGVzc2NvbS9hcGkvdjEvZXJyb3IucHJvdG8SD2NoZXNzY29tLmFwaS52MSKJAQoKVHdpcnBFcnJvchILCgNtc2cYASABKAkSDAoEY29kZRgCIAEoCRIzCgRtZXRhGAMgAygLMiUuY2hlc3Njb20uYXBpLnYxLlR3aXJwRXJyb3IuTWV0YUVudHJ5GisKCU1ldGFFbnRyeRILCgNrZXkYASABKAkSDQoFdmFsdWUYAiABKAk6AjgBYgZwcm90bzM","chesscom/api/v1/error_reason
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17469"></a>
## FND-17469: Full frontend descriptor: chesscom/api/v1/error_reason.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/api/v1/error_reason.proto",
  "package": "chesscom.api.v1",
  "enum_type": [
    {
      "name": "ErrorReason",
      "value": [
        {
          "name": "ERROR_REASON_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ERROR_REASON_INVALID_INPUT",
          "number": 1
        },
        {
          "name": "ERROR_REASON_INVALID_CAPTCHA",
          "number": 12
        },
        {
          "name": "ERROR_REASON_USER_DISABLED",
          "number": 2
        },
        {
          "name": "ERROR_REASON_USER_NOT_FOUND",
          "number": 3
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_INVALID_CHALLENGE",
          "number": 4
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_INVALID_VERIFICATION_CODE",
          "number": 5
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_INVALID_NEW_DEVICE_VERIFICATION_CODE",
          "number": 54
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_INVALID_OLD_DEVICE_VERIFICATION_CODE",
          "number": 55
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_VERIFICATION_FAILED",
          "number": 6
        },
        {
          "name": "ERROR_REASON_AUTHENTICATION_VERIFICATION_BLOCKED",
          "number": 47
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_UPDATE_LIMIT_REACHED",
          "number": 7
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_UPDATE_MUST_BE_DIFFERENT",
          "number": 8
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_ALREADY_IN_USE",
          "number": 9
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_REMOVE_NO_LOGIN_OPTIONS",
          "number": 10
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_ACCOUNT_RECOVERY_LIMIT_REACHED",
          "number": 11
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_INVALID_TYPE",
          "number": 13
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_INVALID",
          "number": 21
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_UNSUPPORTED_COUNTRY",
          "number": 22
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_MISSING",
          "number": 25
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_VERIFICATION_LIMIT_REACHED",
          "number": 45
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_FRAUDULENT_ACTIVITY",
          "number": 48
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_ACCOUNT_VERIFICATION_LIMIT_REACHED",
          "number": 61
        },
        {
          "name": "ERROR_REASON_PHONE_NUMBER_UNSUBSCRIBED_RECIPIENT",
          "number": 62
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALREADY_PREMIUM",
          "number": 14
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_CROSS_BORDER_RESTRICTION",
          "number": 15
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_TYPE",
          "number": 16
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_ALL_SEATS_TAKEN",
          "number": 17
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVITATION_EXPIRED",
          "number": 18
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_JOIN_INVALID_INVITATION",
          "number": 19
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_NOT_FOUND",
          "number": 20
        },
        {
          "name": "ERROR_REASON_GROUP_MEMBERSHIP_USER_NOT_FOUND",
          "number": 23
        },
        {
          "name": "ERROR_REASON_SIGNUP_ISSUE_CHALLENGE_LIMIT_REACHED",
          "number": 24
        },
        {
          "name": "ERROR_REASON_SIGNUP_UNSUPPORTED_CHALLENGE_METHOD",
          "number": 63
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_NOT_SUPPORTED_TYPE",
          "number": 26
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_STATE_VALIDATION_FAILED",
          "number": 27
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_NO_AUTH_CODE",
          "number": 28
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_ACCOUNT_DOES_NOT_EXIST",
          "number": 29
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_PROVIDER_EXCEPTION",
          "number": 30
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_NO_PERMISSIONS_PROVIDED",
          "number": 31
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_SAME_ACCOUNT",
          "number": 32
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_ANOTHER_ACCOUNT",
          "number": 33
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_ALREADY_CONNECTED_TO_ANOTHER_USER",
          "number": 34
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_ONLY_AVAILABLE_LOGIN_OPTION",
          "number": 35
        },
        {
          "name": "ERROR_REASON_EXTERNAL_ACCOUNTS_CANNOT_DISCONNECT_ACCOUNT_ONLY_AVAILABLE_OPTION",
          "number": 60
        },
        {
          "name": "ERROR_REASON_ACCOUNT_CURRENT_PASSWORD_INVALID",
          "number": 36
        },
        {
          "name": "ERROR_REASON_ACCOUNT_NEW_PASSWORD_INVALID",
          "number": 37
        },
        {
          "name": "ERROR_REASON_ACCOUNT_PASSWORD_UPDATE_LIMIT_REACHED",
          "number": 38
        },
        {
          "name": "ERROR_REASON_ACCOUNT_NEW_EMAIL_INVALID",
          "number": 39
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_UPDATE_LIMIT_REACHED",
          "number": 40
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_UPDATE_FILLER_PASSWORD",
          "number": 41
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_UPDATE_EQUALS_CURRENT",
          "number": 42
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_UPDATE_ALREADY_IN_USE",
          "number": 43
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_ALREADY_ACTIVATED",
          "number": 57
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_NOT_FOUND",
          "number": 58
        },
        {
          "name": "ERROR_REASON_ACCOUNT_EMAIL_RESEND_LIMIT_REACHED",
          "number": 59
        },
        {
          "name": "ERROR_REASON_ACCOUNT_INVALID_DATA_PROVIDED",
          "number": 44
        },
        {
          "name": "ERROR_REASON_ACCOUNT_OLD_PASSWORD_EXIST",
          "number": 46
        },
        {
          "name": "ERROR_REASON_ACCOUNT_SKILL_CANNOT_BE_UPDATED_ANYMORE",
          "number": 49
        },
        {
          "name": "ERROR_REASON_ACCOUNT_INVALID_SELF_ASSESSED_SKILL_LEVEL",
          "number": 56
        },
        {
          "name": "ERROR_REASON_OTVC_CHALLENGE_TRY_AGAIN_LATER",
          "number": 50
        },
        {
          "name": "ERROR_REASON_OTVC_CHALLENGE_CHALLENGE_NOT_EXISTS",
          "number": 51
        },
        {
          "name": "ERROR_REASON_OTVC_CHALLENGE_USER_NOT_EXISTS",
          "number": 52
        },
        {
          "name": "ERROR_REASON_SURVEY_NO_ANSWERS",
          "number": 53
        },
        {
          "name": "ERROR_REASON_CONTACTS_ACCOUNT_NOT_VERIFIED",
          "number": 64
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 33228.

```text
R3aXJwRXJyb3IuTWV0YUVudHJ5GisKCU1ldGFFbnRyeRILCgNrZXkYASABKAkSDQoFdmFsdWUYAiABKAk6AjgBYgZwcm90bzM","chesscom/api/v1/error_reason.proto":"CiJjaGVzc2NvbS9hcGkvdjEvZXJyb3JfcmVhc29uLnByb3RvEg9jaGVzc2NvbS5hcGkudjEq/xoKC0Vycm9yUmVhc29uEhwKGEVSUk9SX1JFQVNPTl9VTlNQRUNJRklFRBAAEh4KGkVSUk9SX1JFQVNPTl9JTlZBTElEX0lOUFVUEAESIAocRVJST1JfUkVBU09OX0lOVkFMSURfQ0FQVENIQRAMEh4KGkVSUk9SX1JFQVNPTl9VU0VSX0RJU0FCTEVEEAISHwobRVJST1JfUkVBU09
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17470"></a>
## FND-17470: Full frontend descriptor: chesscom/explanation_engine/v1/game_analysis.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_analysis.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "VariationAnalysis",
      "field": [
        {
          "name": "variation_game_points",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        },
        {
          "name": "game_phase_transitions",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseTransitions"
        },
        {
          "name": "result",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameResult",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "variation_cutoffs",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        }
      ],
      "oneof_decl": [
        {
          "name": "_result"
        }
      ]
    },
    {
      "name": "EngineVariationAnalysis",
      "field": [
        {
          "name": "variation_analysis",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.VariationAnalysis"
        },
        {
          "name": "engine_score",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Score"
        },
        {
          "name": "variation_theme_prompt",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "PositionAnalysis",
      "field": [
        {
          "name": "move_classification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "null_move_variations",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EngineVariationAnalysis"
        },
        {
          "name": "best_move_variations",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.EngineVariationAnalysis"
        },
        {
          "name": "position_speech",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Speech"
        }
      ]
    },
    {
      "name": "GameAnalysisMetadata",
      "field": [
        {
          "name": "cee_version",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        }
      ]
    },
    {
      "name": "GameAnalysis",
      "field": [
        {
          "name": "main_line",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.VariationAnalysis"
        },
        {
          "name": "game_position_analysis_collection",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameAnalysis.GamePositionAnalysisCollectionEntry"
        },
        {
          "name": "accuracy_by_color",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.VariationAccuracy"
        },
        {
          "name": "report_card",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.ReportCard"
        },
        {
          "name": "game_arc",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.GameArc"
        },
        {
          "name": "key_moments_game_points",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GamePointInfo"
        },
        {
          "name": "annotated_pgn",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_summary",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "metadata",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameAnalysisMetadata"
        }
      ],
      "nested_type": [
        {
          "name": "GamePositionAnalysisCollectionEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.PositionAnalysis"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "reserved_range": [
        {
          "start": 1,
          "end": 2
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GameAnalysisSpeechVersion",
      "value": [
        {
          "name": "GAME_ANALYSIS_SPEECH_VERSION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_ANALYSIS_SPEECH_VERSION_2",
          "number": 2
        },
        {
          "name": "GAME_ANALYSIS_SPEECH_VERSION_3",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 37960.

```text
SVkVZX05PX0FOU1dFUlMQNRIuCipFUlJPUl9SRUFTT05fQ09OVEFDVFNfQUNDT1VOVF9OT1RfVkVSSUZJRUQQQGIGcHJvdG8z","chesscom/explanation_engine/v1/game_analysis.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9hbmFseXNpcy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIsACChFWYXJpYXRpb25BbmFseXNpcxJMChV2YXJpYXRpb25fZ2FtZV9wb2ludHMYASADKAsyLS5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuR2FtZVBvaW50SW5mbxJUChZnYW1lX3BoYXNlX3R
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17471"></a>
## FND-17471: Full frontend descriptor: chesscom/explanation_engine/v1/search.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/search.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SearchParameters",
      "field": [
        {
          "name": "depth_limit",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "nodes_limit",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "time_limit_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "num_lines",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "multi_line_strategy",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MultiLineStrategy",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "num_threads",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_depth_limit"
        },
        {
          "name": "_nodes_limit"
        },
        {
          "name": "_time_limit_ms"
        },
        {
          "name": "_num_lines"
        },
        {
          "name": "_multi_line_strategy"
        },
        {
          "name": "_num_threads"
        }
      ]
    },
    {
      "name": "GameReviewSearchSettings",
      "field": [
        {
          "name": "strength",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Strength"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "SearchPreset",
      "value": [
        {
          "name": "SEARCH_PRESET_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SEARCH_PRESET_PLAY_BOT_STANDARD",
          "number": 1
        },
        {
          "name": "SEARCH_PRESET_PLAY_BOT_FAST",
          "number": 2
        },
        {
          "name": "SEARCH_PRESET_GAME_REVIEW_FAST",
          "number": 3
        },
        {
          "name": "SEARCH_PRESET_GAME_REVIEW_STANDARD",
          "number": 4
        },
        {
          "name": "SEARCH_PRESET_GAME_REVIEW_DEEP",
          "number": 5
        },
        {
          "name": "SEARCH_PRESET_GAME_REVIEW_MAXIMUM",
          "number": 6
        }
      ],
      "options": {}
    },
    {
      "name": "MultiLineStrategy",
      "value": [
        {
          "name": "MULTI_LINE_STRATEGY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "MULTI_LINE_STRATEGY_UCI",
          "number": 1
        },
        {
          "name": "MULTI_LINE_STRATEGY_MULTISEARCH",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 40574.

```text
19TUEVFQ0hfVkVSU0lPTl8yEAISIgoeR0FNRV9BTkFMWVNJU19TUEVFQ0hfVkVSU0lPTl8zEAMaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/search.proto":"CitjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc2VhcmNoLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEi2gIKEFNlYXJjaFBhcmFtZXRlcnMSGAoLZGVwdGhfbGltaXQYASABKAVIAIgBARIYCgtub2Rlc19saW1pdBgCIAEoBUgBiAEBEhoKDXRpbWVfbGltaXRfbXMYAyABKAVIAogBARIWCgludW1fbGluZXMYBCABKAVIA4gBARJTCh
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17472"></a>
## FND-17472: Full frontend descriptor: chesscom/explanation_engine/v1/game_settings.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_settings.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GameSettings",
      "field": [
        {
          "name": "search_settings",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SearchSettings",
          "oneof_index": 0
        },
        {
          "name": "game_review_search_settings",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
          "oneof_index": 0
        },
        {
          "name": "preset",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.SearchPreset",
          "oneof_index": 0
        },
        {
          "name": "user_color",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Color",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "locale",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.Locale",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "game_phase_version",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.GamePhaseVersion",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "game_analysis_speech_version",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.GameAnalysisSpeechVersion",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "move_classification_version",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassificationVersion",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "force_disable_internal_engine_searches",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "enable_skills",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 7,
          "proto3_optional": true
        },
        {
          "name": "enabled_feature_flags",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "feature_flag_config",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry"
        }
      ],
      "nested_type": [
        {
          "name": "FeatureFlagConfigEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "search"
        },
        {
          "name": "_user_color"
        },
        {
          "name": "_locale"
        },
        {
          "name": "_game_phase_version"
        },
        {
          "name": "_game_analysis_speech_version"
        },
        {
          "name": "_move_classification_version"
        },
        {
          "name": "_force_disable_internal_engine_searches"
        },
        {
          "name": "_enable_skills"
        }
      ],
      "reserved_range": [
        {
          "start": 1,
          "end": 2
        },
        {
          "start": 2,
          "end": 3
        }
      ]
    },
    {
      "name": "SearchSettings",
      "field": [
        {
          "name": "search_parameters",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SearchParameters"
        },
        {
          "name": "null_move_search_parameters",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SearchParameters"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 41865.

```text
ElORV9TVFJBVEVHWV9VQ0kQARIjCh9NVUxUSV9MSU5FX1NUUkFURUdZX01VTFRJU0VBUkNIEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/game_settings.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9zZXR0aW5ncy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIuIICgxHYW1lU2V0dGluZ3MSSQoPc2VhcmNoX3NldHRpbmdzGAggASgLMi4uY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlNlYXJjaFNldHRpbmdzSAASXwobZ2FtZV9yZXZpZXdfc2VhcmNoX3N
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17473"></a>
## FND-17473: Full frontend descriptor: chesscom/explanation_engine/v1/move_annotation.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/move_annotation.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "AnnotationArrow",
      "field": [
        {
          "name": "from",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "to",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "color",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.AnnotationColor"
        }
      ],
      "options": {}
    },
    {
      "name": "AnnotationSquare",
      "field": [
        {
          "name": "square",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Square"
        },
        {
          "name": "color",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.AnnotationColor"
        }
      ],
      "options": {}
    },
    {
      "name": "MoveAnnotation",
      "field": [
        {
          "name": "comments",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "before_comment",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "nags",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_INT32"
        },
        {
          "name": "arrows",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AnnotationArrow"
        },
        {
          "name": "highlighted_squares",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.AnnotationSquare"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_before_comment"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "AnnotationColor",
      "value": [
        {
          "name": "ANNOTATION_COLOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ANNOTATION_COLOR_GREEN",
          "number": 1
        },
        {
          "name": "ANNOTATION_COLOR_RED",
          "number": 2
        },
        {
          "name": "ANNOTATION_COLOR_YELLOW",
          "number": 3
        },
        {
          "name": "ANNOTATION_COLOR_BLUE",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 43800.

```text
gCIAEoCzIwLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5TZWFyY2hQYXJhbWV0ZXJzOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/move_annotation.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvbW92ZV9hbm5vdGF0aW9uLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiqgEKD0Fubm90YXRpb25BcnJvdxInCgRmcm9tGAEgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEiUKAnRvGAIgASgOMhkuY2hlc3Njb20uY2hlc3MudjEuU3F1YXJlEj4KBWNvbG9yGAMgA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17474"></a>
## FND-17474: Full frontend descriptor: chesscom/explanation_engine/v1/simple_charm_inference.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/simple_charm_inference.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "SimpleCharmMovePrediction",
      "field": [
        {
          "name": "uci_move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "probability",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {}
    },
    {
      "name": "SimpleCharmInference",
      "field": [
        {
          "name": "model_key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SimpleCharmMovePrediction"
        },
        {
          "name": "expected_points",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "rank_probabilities",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "strength_probabilities",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "time_taken_probabilities",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "ldw_probabilities",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "strength_rating_sensitive_probabilities",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_rating"
        },
        {
          "name": "_expected_points"
        }
      ]
    },
    {
      "name": "SimpleCharmInferences",
      "field": [
        {
          "name": "inferences",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SimpleCharmInference"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 44964.

```text
hsKF0FOTk9UQVRJT05fQ09MT1JfWUVMTE9XEAMSGQoVQU5OT1RBVElPTl9DT0xPUl9CTFVFEAQaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/simple_charm_inference.proto":"CjtjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvc2ltcGxlX2NoYXJtX2luZmVyZW5jZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIksKGVNpbXBsZUNoYXJtTW92ZVByZWRpY3Rpb24SEAoIdWNpX21vdmUYASABKAkSEwoLcHJvYmFiaWxpdHkYAiABKAI6B4KmHQMKAQEi+AIKFFNpbXBsZUNoYXJtSW5mZXJlbm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17475"></a>
## FND-17475: Full frontend descriptor: chesscom/explanation_engine/v1/game_state.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/game_state.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "GameState",
      "field": [
        {
          "name": "game_state_version",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        },
        {
          "name": "game_tree",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameTree",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "game_settings",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameSettings"
        },
        {
          "name": "game_metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata"
        },
        {
          "name": "default_eval_source_engine",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Engine"
        },
        {
          "name": "coach_state",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CoachState"
        },
        {
          "name": "charm_inferences",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState.CharmInferencesEntry",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "annotations",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState.AnnotationsEntry"
        },
        {
          "name": "compact_charm_inferences",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "compact_game_tree",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CompactGameTree"
        },
        {
          "name": "quantized_charm_inferences",
          "number": 11,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "charm_inference_codes",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.CharmInferenceCodes"
        }
      ],
      "nested_type": [
        {
          "name": "CharmInferencesEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.SimpleCharmInferences"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "AnnotationsEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.MoveAnnotation"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "CompactCharmInferencesEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
            }
          ],
          "options": {
            "map_entry": true
          }
        },
        {
          "name": "QuantizedCharmInferencesEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_INT32"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".chesscom.explanation_engine.v1.CompactCharmInferences"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {}
    },
    {
      "name": "GameTree",
      "field": [
        {
          "name": "nodes",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameTreeNode"
        }
      ],
      "options": {}
    },
    {
      "name": "GameTreeNode",
      "field": [
        {
          "name": "initial_fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0
        },
        {
          "name": "legal_move_index",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0
        },
        {
          "name": "is_played",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_explicitly_unscored",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "score",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_SINT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "depth",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_SINT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "additional_children",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_SINT32"
        },
        {
          "name": "time_on_clock_deciseconds",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "score_is_weak",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "manually_added",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "board_state"
        },
        {
          "name": "_score"
        },
        {
          "name": "_depth"
        },
        {
          "name": "_time_on_clock_deciseconds"
        }
      ]
    },
    {
      "name": "CompactGameTree",
      "field": [
        {
          "name": "initial_fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "legal_move_indexes",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "node_flags",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BYTES"
        },
        {
          "name": "additional_children",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_SINT32"
        },
        {
          "name": "scores",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_SINT32"
        },
        {
          "name": "depths",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_SINT32"
        },
        {
          "name": "clocks_deciseconds",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "NodeFlag",
      "value": [
        {
          "name": "NODE_FLAG_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "NODE_FLAG_PLAYED",
          "number": 1
        },
        {
          "name": "NODE_FLAG_EXPLICITLY_UNSCORED",
          "number": 2
        },
        {
          "name": "NODE_FLAG_SCORE_IS_WEAK",
          "number": 4
        },
        {
          "name": "NODE_FLAG_MANUALLY_ADDED",
          "number": 8
        },
        {
          "name": "NODE_FLAG_HAS_SCORE",
          "number": 16
        },
        {
          "name": "NODE_FLAG_HAS_DEPTH",
          "number": 32
        },
        {
          "name": "NODE_FLAG_HAS_ADDITIONAL_CHILDREN",
          "number": 64
        },
        {
          "name": "NODE_FLAG_HAS_CLOCK",
          "number": 128
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 45916.

```text
gLMjQuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlNpbXBsZUNoYXJtSW5mZXJlbmNlOgeCph0DCgEBYgZwcm90bzM","chesscom/explanation_engine/v1/game_state.proto":"Ci9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZ2FtZV9zdGF0ZS5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIoELCglHYW1lU3RhdGUSPAoSZ2FtZV9zdGF0ZV92ZXJzaW9uGAEgASgLMiAuY2hlc3Njb20uYXBpLnYxLlNlbWFudGljVmVyc2lvbhI/CglnYW1lX3RyZWUYAiABKAsyKC5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17476"></a>
## FND-17476: Full frontend descriptor: chesscom/explanation_engine/v1/puzzle_gen.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/puzzle_gen.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "PuzzleGen",
      "field": [
        {
          "name": "puzzle",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.Puzzle",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "puzzle_game_state",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameState"
        },
        {
          "name": "mode",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGenMode"
        },
        {
          "name": "cee_version",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.SemanticVersion"
        },
        {
          "name": "puzzle_quality_score",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ],
      "oneof_decl": [
        {
          "name": "_puzzle"
        }
      ]
    },
    {
      "name": "Puzzle",
      "field": [
        {
          "name": "annotated_puzzle_pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "initial_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "puzzle_moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleMove"
        },
        {
          "name": "puzzle_themes",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleTheme"
        },
        {
          "name": "puzzle_goal",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleGoal",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "game_phase",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.GamePhase"
        },
        {
          "name": "origin_game_metadata",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.GameMetadata",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "puzzle_goal_speech",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SpeechForLocale"
        },
        {
          "name": "initial_position",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Position"
        },
        {
          "name": "puzzle_result",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleResult"
        },
        {
          "name": "origin_game_ply",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_puzzle_goal"
        },
        {
          "name": "_origin_game_metadata"
        },
        {
          "name": "_origin_game_ply"
        }
      ]
    },
    {
      "name": "PuzzleMove",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "classification",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.MoveClassification"
        },
        {
          "name": "puzzle_hint_speech",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SpeechForLocale"
        },
        {
          "name": "legal_alternate_moves",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        }
      ]
    },
    {
      "name": "PuzzleResult",
      "field": [
        {
          "name": "winning_result",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleWinningResult",
          "oneof_index": 0
        }
      ],
      "oneof_decl": [
        {
          "name": "result"
        }
      ]
    },
    {
      "name": "PuzzleGoal",
      "field": [
        {
          "name": "tactical_goal",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoal",
          "oneof_index": 0
        },
        {
          "name": "strategic_goal",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.StrategicGoal",
          "oneof_index": 0
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "goal_type"
        }
      ]
    },
    {
      "name": "PuzzleTheme",
      "field": [
        {
          "name": "mate_in_1",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn1",
          "oneof_index": 0
        },
        {
          "name": "mate_in_2",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn2",
          "oneof_index": 0
        },
        {
          "name": "scholars_mate",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeScholarsMate",
          "oneof_index": 0
        },
        {
          "name": "endgame_tactics",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics",
          "oneof_index": 0
        },
        {
          "name": "trapped_piece",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece",
          "oneof_index": 0
        },
        {
          "name": "fork",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeFork",
          "oneof_index": 0
        },
        {
          "name": "skewer",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeSkewer",
          "oneof_index": 0
        },
        {
          "name": "hanging_piece",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeHangingPiece",
          "oneof_index": 0
        },
        {
          "name": "discovery",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeDiscovery",
          "oneof_index": 0
        },
        {
          "name": "queen_sacrifice",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice",
          "oneof_index": 0
        },
        {
          "name": "opposition",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeOpposition",
          "oneof_index": 0
        },
        {
          "name": "mate_in_3_plus",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus",
          "oneof_index": 0
        },
        {
          "name": "mating_net",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeMatingNet",
          "oneof_index": 0
        },
        {
          "name": "pawn_endgame",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePawnEndgame",
          "oneof_index": 0
        },
        {
          "name": "promotion",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePromotion",
          "oneof_index": 0
        },
        {
          "name": "under_promotion",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion",
          "oneof_index": 0
        },
        {
          "name": "sacrifice",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeSacrifice",
          "oneof_index": 0
        },
        {
          "name": "back_rank_mate",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeBackRankMate",
          "oneof_index": 0
        },
        {
          "name": "pin",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePin",
          "oneof_index": 0
        },
        {
          "name": "king_safety",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeKingSafety",
          "oneof_index": 0
        },
        {
          "name": "piece_play",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePiecePlay",
          "oneof_index": 0
        },
        {
          "name": "pawn_structure",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemePawnStructure",
          "oneof_index": 0
        },
        {
          "name": "ladder_mate",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeLadderMate",
          "oneof_index": 0
        },
        {
          "name": "theme_type",
          "number": 255,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleThemeType"
        }
      ],
      "oneof_decl": [
        {
          "name": "theme"
        }
      ]
    },
    {
      "name": "TacticalGoal",
      "field": [
        {
          "name": "checkmate",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalCheckmate",
          "oneof_index": 0
        },
        {
          "name": "promotion",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalPromotion",
          "oneof_index": 0
        },
        {
          "name": "attack_the_king",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalAttackTheKing",
          "oneof_index": 0
        },
        {
          "name": "win_material",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalWinMaterial",
          "oneof_index": 0
        },
        {
          "name": "defense",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalDefense",
          "oneof_index": 0
        },
        {
          "name": "promotion_position",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalPromotionPosition",
          "oneof_index": 0
        },
        {
          "name": "distant_checkmate",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate",
          "oneof_index": 0
        },
        {
          "name": "goal_type",
          "number": 255,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.TacticalGoalType"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "goal"
        }
      ]
    },
    {
      "name": "StrategicGoal",
      "field": [
        {
          "name": "goal_type",
          "number": 255,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.explanation_engine.v1.StrategicGoalType"
        }
      ],
      "options": {}
    },
    {
      "name": "TacticalGoalCheckmate",
      "options": {}
    },
    {
      "name": "TacticalGoalPromotion",
      "options": {}
    },
    {
      "name": "TacticalGoalAttackTheKing",
      "options": {}
    },
    {
      "name": "TacticalGoalDefense",
      "options": {}
    },
    {
      "name": "TacticalGoalWinMaterial",
      "field": [
        {
          "name": "won_piece",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Piece",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_won_piece"
        }
      ]
    },
    {
      "name": "TacticalGoalPromotionPosition",
      "options": {}
    },
    {
      "name": "TacticalGoalDistantCheckmate",
      "options": {}
    },
    {
      "name": "PuzzleThemeMateIn1"
    },
    {
      "name": "PuzzleThemeMateIn2"
    },
    {
      "name": "PuzzleThemeMateIn3Plus"
    },
    {
      "name": "PuzzleThemeScholarsMate"
    },
    {
      "name": "PuzzleThemeEndgameTactics"
    },
    {
      "name": "PuzzleThemeTrappedPiece"
    },
    {
      "name": "PuzzleThemeFork"
    },
    {
      "name": "PuzzleThemeSkewer"
    },
    {
      "name": "PuzzleThemeHangingPiece"
    },
    {
      "name": "PuzzleThemeDiscovery"
    },
    {
      "name": "PuzzleThemeQueenSacrifice"
    },
    {
      "name": "PuzzleThemeOpposition"
    },
    {
      "name": "PuzzleThemeMatingNet"
    },
    {
      "name": "PuzzleThemePawnEndgame"
    },
    {
      "name": "PuzzleThemePromotion"
    },
    {
      "name": "PuzzleThemeUnderPromotion"
    },
    {
      "name": "PuzzleThemeSacrifice"
    },
    {
      "name": "PuzzleThemeBackRankMate"
    },
    {
      "name": "PuzzleThemePin"
    },
    {
      "name": "PuzzleThemeKingSafety",
      "field": [
        {
          "name": "subtheme_weaken",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "subtheme_attack",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "subtheme_defend",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_subtheme_weaken"
        },
        {
          "name": "_subtheme_attack"
        },
        {
          "name": "_subtheme_defend"
        }
      ]
    },
    {
      "name": "PuzzleSubthemeKingSafetyWeaken"
    },
    {
      "name": "PuzzleSubthemeKingSafetyAttack"
    },
    {
      "name": "PuzzleSubthemeKingSafetyDefend"
    },
    {
      "name": "PuzzleThemePiecePlay",
      "field": [
        {
          "name": "subtheme_activity",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "subtheme_prevention",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "subtheme_trades",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_subtheme_activity"
        },
        {
          "name": "_subtheme_prevention"
        },
        {
          "name": "_subtheme_trades"
        }
      ]
    },
    {
      "name": "PuzzleSubthemePiecePlayActivity"
    },
    {
      "name": "PuzzleSubthemePiecePlayPrevention"
    },
    {
      "name": "PuzzleSubthemePiecePlayTrades"
    },
    {
      "name": "PuzzleThemePawnStructure",
      "field": [
        {
          "name": "subtheme_healthy",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "subtheme_creates_weaknesses",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_subtheme_healthy"
        },
        {
          "name": "_subtheme_creates_weaknesses"
        }
      ]
    },
    {
      "name": "PuzzleSubthemePawnStructureHealthy"
    },
    {
      "name": "PuzzleSubthemePawnStructureCreatesWeaknesses"
    },
    {
      "name": "PuzzleThemeLadderMate"
    }
  ],
  "enum_type": [
    {
      "name": "PuzzleGenMode",
      "value": [
        {
          "name": "PUZZLE_GEN_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_GEN_MODE_TACTICAL",
          "number": 1
        },
        {
          "name": "PUZZLE_GEN_MODE_STRATEGIC",
          "number": 2
        }
      ]
    },
    {
      "name": "PuzzleWinningResult",
      "value": [
        {
          "name": "PUZZLE_WINNING_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD",
          "number": 1
        }
      ]
    },
    {
      "name": "TacticalGoalType",
      "value": [
        {
          "name": "TACTICAL_GOAL_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TACTICAL_GOAL_TYPE_CHECKMATE",
          "number": 1
        },
        {
          "name": "TACTICAL_GOAL_TYPE_PROMOTION",
          "number": 2
        },
        {
          "name": "TACTICAL_GOAL_TYPE_ATTACK_THE_KING",
          "number": 3
        },
        {
          "name": "TACTICAL_GOAL_TYPE_WIN_MATERIAL",
          "number": 4
        },
        {
          "name": "TACTICAL_GOAL_TYPE_DEFENSE",
          "number": 5
        },
        {
          "name": "TACTICAL_GOAL_TYPE_PROMOTION_POSITION",
          "number": 6
        },
        {
          "name": "TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE",
          "number": 7
        }
      ],
      "options": {}
    },
    {
      "name": "StrategicGoalType",
      "value": [
        {
          "name": "STRATEGIC_GOAL_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS",
          "number": 1
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS",
          "number": 2
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES",
          "number": 3
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_RESTRICT_PIECES",
          "number": 4
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_TRADE_PIECES",
          "number": 5
        },
        {
          "name": "STRATEGIC_GOAL_TYPE_ATTACK_THE_KING",
          "number": 6
        }
      ],
      "options": {}
    },
    {
      "name": "PuzzleThemeType",
      "value": [
        {
          "name": "PUZZLE_THEME_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PUZZLE_THEME_TYPE_MATE_IN_1",
          "number": 1
        },
        {
          "name": "PUZZLE_THEME_TYPE_MATE_IN_2",
          "number": 2
        },
        {
          "name": "PUZZLE_THEME_TYPE_SCHOLARS_MATE",
          "number": 3
        },
        {
          "name": "PUZZLE_THEME_TYPE_ENDGAME_TACTICS",
          "number": 4
        },
        {
          "name": "PUZZLE_THEME_TYPE_TRAPPED_PIECE",
          "number": 5
        },
        {
          "name": "PUZZLE_THEME_TYPE_FORK",
          "number": 6
        },
        {
          "name": "PUZZLE_THEME_TYPE_SKEWER",
          "number": 7
        },
        {
          "name": "PUZZLE_THEME_TYPE_HANGING_PIECE",
          "number": 8
        },
        {
          "name": "PUZZLE_THEME_TYPE_DISCOVERY",
          "number": 9
        },
        {
          "name": "PUZZLE_THEME_TYPE_QUEEN_SACRIFICE",
          "number": 10
        },
        {
          "name": "PUZZLE_THEME_TYPE_OPPOSITION",
          "number": 11
        },
        {
          "name": "PUZZLE_THEME_TYPE_MATE_IN_3_PLUS",
          "number": 12
        },
        {
          "name": "PUZZLE_THEME_TYPE_MATING_NET",
          "number": 13
        },
        {
          "name": "PUZZLE_THEME_TYPE_PAWN_ENDGAME",
          "number": 14
        },
        {
          "name": "PUZZLE_THEME_TYPE_PROMOTION",
          "number": 15
        },
        {
          "name": "PUZZLE_THEME_TYPE_UNDER_PROMOTION",
          "number": 16
        },
        {
          "name": "PUZZLE_THEME_TYPE_SACRIFICE",
          "number": 17
        },
        {
          "name": "PUZZLE_THEME_TYPE_BACK_RANK_MATE",
          "number": 18
        },
        {
          "name": "PUZZLE_THEME_TYPE_PIN",
          "number": 19
        },
        {
          "name": "PUZZLE_THEME_TYPE_KING_SAFETY",
          "number": 20
        },
        {
          "name": "PUZZLE_THEME_TYPE_PIECE_PLAY",
          "number": 21
        },
        {
          "name": "PUZZLE_THEME_TYPE_PAWN_STRUCTURE",
          "number": 22
        },
        {
          "name": "PUZZLE_THEME_TYPE_LADDER_MATE",
          "number": 23
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 49156.

```text
IlCiFOT0RFX0ZMQUdfSEFTX0FERElUSU9OQUxfQ0hJTERSRU4QQBIYChNOT0RFX0ZMQUdfSEFTX0NMT0NLEIABYgZwcm90bzM","chesscom/explanation_engine/v1/puzzle_gen.proto":"Ci9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvcHV6emxlX2dlbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIqsCCglQdXp6bGVHZW4SOwoGcHV6emxlGAEgASgLMiYuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlB1enpsZUgAiAEBEkQKEXB1enpsZV9nYW1lX3N0YXRlGAIgASgLMikuY2hlc3Njb20uZXhwbGFuYX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17477"></a>
## FND-17477: Full frontend descriptor: chesscom/explanation_engine/v1/charm_inference.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/charm_inference.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "MovePrediction",
      "field": [
        {
          "name": "move",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "uci_move",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "probability",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        }
      ]
    },
    {
      "name": "CharmInferenceResult",
      "field": [
        {
          "name": "model_key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "elo",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "moves",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.MovePrediction"
        },
        {
          "name": "expected_points",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "rank_probabilities",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "strength_probabilities",
          "number": 6,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "time_taken_probabilities",
          "number": 7,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "ldw_probabilities",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "strength_rating_sensitive_probabilities",
          "number": 9,
          "label": "LABEL_REPEATED",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "engine_line_uci_moves",
          "number": 10,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "engine",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.engine.v1.Engine",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_engine"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 60043.

```text
FlQRV9QQVdOX1NUUlVDVFVSRRAWEiEKHVBVWlpMRV9USEVNRV9UWVBFX0xBRERFUl9NQVRFEBcaB4qmHQMKAQFiBnByb3RvMw","chesscom/explanation_engine/v1/charm_inference.proto":"CjRjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY2hhcm1faW5mZXJlbmNlLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiXgoOTW92ZVByZWRpY3Rpb24SJQoEbW92ZRgBIAEoCzIXLmNoZXNzY29tLmNoZXNzLnYxLk1vdmUSEAoIdWNpX21vdmUYAiABKAkSEwoLcHJvYmFiaWxpdHkYAyABKAIikwMKFENoYXJtSW5mZXJlb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17478"></a>
## FND-17478: Full frontend descriptor: chesscom/explanation_engine/v1/torch_search_mode.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/torch_search_mode.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "TorchSearchMode",
      "field": [
        {
          "name": "human",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode.Human",
          "oneof_index": 0
        },
        {
          "name": "multisearch",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode.Multisearch",
          "oneof_index": 0
        }
      ],
      "nested_type": [
        {
          "name": "Human",
          "field": [
            {
              "name": "disable_maia",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL",
              "oneof_index": 0,
              "proto3_optional": true
            }
          ],
          "options": {},
          "oneof_decl": [
            {
              "name": "_disable_maia"
            }
          ]
        },
        {
          "name": "Multisearch",
          "field": [
            {
              "name": "reduce_nodes_on_successive_searches",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_BOOL",
              "oneof_index": 0,
              "proto3_optional": true
            }
          ],
          "options": {},
          "oneof_decl": [
            {
              "name": "_reduce_nodes_on_successive_searches"
            }
          ]
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "mode"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 60896.

```text
ogAygJEi8KBmVuZ2luZRgLIAEoDjIaLmNoZXNzY29tLmVuZ2luZS52MS5FbmdpbmVIAIgBAUIJCgdfZW5naW5lYgZwcm90bzM","chesscom/explanation_engine/v1/torch_search_mode.proto":"CjZjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvdG9yY2hfc2VhcmNoX21vZGUucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MSLuAgoPVG9yY2hTZWFyY2hNb2RlEkYKBWh1bWFuGAEgASgLMjUuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLlRvcmNoU2VhcmNoTW9kZS5IdW1hbkgAElIKC211bHRpc2VhcmNoGAI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17479"></a>
## FND-17479: Full frontend descriptor: chesscom/explanation_engine/v1/feature_run_search.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/feature_run_search.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "RunSearchRequest",
      "field": [
        {
          "name": "search_parameters",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SearchParameters",
          "oneof_index": 0
        },
        {
          "name": "null_move_search_parameters",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.SearchParameters",
          "oneof_index": 0
        },
        {
          "name": "game_review_search_settings",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.GameReviewSearchSettings",
          "oneof_index": 0
        },
        {
          "name": "search_moves",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.Move"
        },
        {
          "name": "stream_results",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "engine_id",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "heartbeat_interval_seconds",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "guarantee_nodes",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "guarantee_nodes_null_move",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "disable_maia",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "torch_search_mode",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.explanation_engine.v1.TorchSearchMode",
          "oneof_index": 5,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "search"
        },
        {
          "name": "_engine_id"
        },
        {
          "name": "_guarantee_nodes"
        },
        {
          "name": "_guarantee_nodes_null_move"
        },
        {
          "name": "_disable_maia"
        },
        {
          "name": "_torch_search_mode"
        }
      ]
    },
    {
      "name": "RunSearchResponse",
      "field": [
        {
          "name": "evaluations",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.engine.v1.Evaluation"
        },
        {
          "name": "progress",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT"
        },
        {
          "name": "aborted",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "log",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "is_heartbeat",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "SearchLimits",
      "field": [
        {
          "name": "depth",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "nodes",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "time_ms",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32",
          "oneof_index": 2,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_depth"
        },
        {
          "name": "_nodes"
        },
        {
          "name": "_time_ms"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 61576.

```text
HgqYdAwoBAUImCiRfcmVkdWNlX25vZGVzX29uX3N1Y2Nlc3NpdmVfc2VhcmNoZXM6B4KmHQMKAQFCBgoEbW9kZWIGcHJvdG8z","chesscom/explanation_engine/v1/feature_run_search.proto":"CjdjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZmVhdHVyZV9ydW5fc2VhcmNoLnByb3RvEh5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEiygUKEFJ1blNlYXJjaFJlcXVlc3QSTQoRc2VhcmNoX3BhcmFtZXRlcnMYASABKAsyMC5jaGVzc2NvbS5leHBsYW5hdGlvbl9lbmdpbmUudjEuU2VhcmNoUGFyYW1ldGVyc0gAElcKG251bG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17480"></a>
## FND-17480: Full frontend descriptor: chesscom/explanation_engine/v1/opening.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/opening.proto",
  "package": "chesscom.explanation_engine.v1",
  "message_type": [
    {
      "name": "Opening",
      "field": [
        {
          "name": "opening_name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "tcn_moves",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "eco_code",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "url",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_opening_name"
        },
        {
          "name": "_tcn_moves"
        },
        {
          "name": "_eco_code"
        },
        {
          "name": "_url"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 63087.

```text
QESFAoHdGltZV9tcxgDIAEoBUgCiAEBOgeCph0DCgEBQggKBl9kZXB0aEIICgZfbm9kZXNCCgoIX3RpbWVfbXNiBnByb3RvMw","chesscom/explanation_engine/v1/opening.proto":"CixjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvb3BlbmluZy5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxIqIBCgdPcGVuaW5nEhkKDG9wZW5pbmdfbmFtZRgBIAEoCUgAiAEBEhYKCXRjbl9tb3ZlcxgCIAEoCUgBiAEBEhUKCGVjb19jb2RlGAMgASgJSAKIAQESEAoDdXJsGAQgASgJSAOIAQE6B4KmHQMKAQFCDwoNX29wZW5pbmdfb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17481"></a>
## FND-17481: Full frontend descriptor: chesscom/explanation_engine/v1/coach_emotion.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/explanation_engine/v1/coach_emotion.proto",
  "package": "chesscom.explanation_engine.v1",
  "enum_type": [
    {
      "name": "CoachEmotion",
      "value": [
        {
          "name": "COACH_EMOTION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_EMOTION_IDLE",
          "number": 1
        },
        {
          "name": "COACH_EMOTION_SURPRISED",
          "number": 2
        },
        {
          "name": "COACH_EMOTION_HAPPY",
          "number": 3
        },
        {
          "name": "COACH_EMOTION_IMPRESSED",
          "number": 4
        },
        {
          "name": "COACH_EMOTION_SHOCKED",
          "number": 5
        },
        {
          "name": "COACH_EMOTION_THINKING",
          "number": 6
        },
        {
          "name": "COACH_EMOTION_CONCERNED",
          "number": 7
        },
        {
          "name": "COACH_EMOTION_SAD",
          "number": 8
        }
      ],
      "options": {
        "deprecated": true
      }
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 63472.

```text
OIAQE6B4KmHQMKAQFCDwoNX29wZW5pbmdfbmFtZUIMCgpfdGNuX21vdmVzQgsKCV9lY29fY29kZUIGCgRfdXJsYgZwcm90bzM","chesscom/explanation_engine/v1/coach_emotion.proto":"CjJjaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvY29hY2hfZW1vdGlvbi5wcm90bxIeY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxKo4CCgxDb2FjaEVtb3Rpb24SHQoZQ09BQ0hfRU1PVElPTl9VTlNQRUNJRklFRBAAEhYKEkNPQUNIX0VNT1RJT05fSURMRRABEhsKF0NPQUNIX0VNT1RJT05fU1VSUFJJU0VEEAISFwoTQ09BQ0hfRU1PVEl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17482"></a>
## FND-17482: Full frontend descriptor: chesscom/stats/v1/advanced_stat_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/stats/v1/advanced_stat_type.proto",
  "package": "chesscom.stats.v1",
  "enum_type": [
    {
      "name": "AdvancedStatType",
      "value": [
        {
          "name": "ADVANCED_STAT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPENING_ACCURACY",
          "number": 1
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPENING_MISTAKES",
          "number": 2
        },
        {
          "name": "ADVANCED_STAT_TYPE_BOOK_MOVES",
          "number": 3
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_CHECKMATE",
          "number": 4
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_FREE_PIECES",
          "number": 5
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_ALL_TACTICS",
          "number": 6
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_UNTHEMED_TACTICS",
          "number": 7
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_FORKS",
          "number": 8
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_PINS",
          "number": 9
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_DISCOVERIES",
          "number": 10
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_REMOVES_DEFENDERS",
          "number": 11
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_TRAPPED_PIECES",
          "number": 12
        },
        {
          "name": "ADVANCED_STAT_TYPE_FOUND_SACRIFICES",
          "number": 13
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_CHECKMATE",
          "number": 14
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_FREE_PIECES",
          "number": 15
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_ALL_TACTICS",
          "number": 16
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_UNTHEMED_TACTICS",
          "number": 17
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_FORKS",
          "number": 18
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_PINS",
          "number": 19
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_DISCOVERIES",
          "number": 20
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_REMOVES_DEFENDERS",
          "number": 21
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_TRAPPED_PIECES",
          "number": 22
        },
        {
          "name": "ADVANCED_STAT_TYPE_ALLOWED_SACRIFICES",
          "number": 23
        },
        {
          "name": "ADVANCED_STAT_TYPE_STRATEGIC_ACCURACY",
          "number": 24
        },
        {
          "name": "ADVANCED_STAT_TYPE_ATTACKING_ACCURACY",
          "number": 25
        },
        {
          "name": "ADVANCED_STAT_TYPE_DEFENDING_ACCURACY",
          "number": 26
        },
        {
          "name": "ADVANCED_STAT_TYPE_SPACE_ADVANTAGE_ACCURACY",
          "number": 27
        },
        {
          "name": "ADVANCED_STAT_TYPE_PIECE_ACTIVITY_ADVANTAGE_ACCURACY",
          "number": 28
        },
        {
          "name": "ADVANCED_STAT_TYPE_PAWN_STRUCTURE_ADVANTAGE_ACCURACY",
          "number": 29
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_ACCURACY",
          "number": 30
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_ATTACKING_ACCURACY",
          "number": 31
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_DEFENDING_ACCURACY",
          "number": 32
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_SPACE_ADVANTAGE_ACCURACY",
          "number": 33
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY",
          "number": 34
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY",
          "number": 35
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_ACCURACY",
          "number": 36
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_ATTACKING_ACCURACY",
          "number": 37
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_DEFENDING_ACCURACY",
          "number": 38
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_SPACE_ADVANTAGE_ACCURACY",
          "number": 39
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_PIECE_ACTIVITY_ADVANTAGE_ACCURACY",
          "number": 40
        },
        {
          "name": "ADVANCED_STAT_TYPE_SEMI_OPEN_PAWN_STRUCTURE_ADVANTAGE_ACCURACY",
          "number": 41
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_ACCURACY",
          "number": 42
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_ATTACKING_ACCURACY",
          "number": 43
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_DEFENDING_ACCURACY",
          "number": 44
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_SPACE_ADVANTAGE_ACCURACY",
          "number": 45
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_PIECE_ACTIVITY_ADVANTAGE_ACCURACY",
          "number": 46
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOSED_PAWN_STRUCTURE_ADVANTAGE_ACCURACY",
          "number": 47
        },
        {
          "name": "ADVANCED_STAT_TYPE_ENDGAME_ACCURACY",
          "number": 48
        },
        {
          "name": "ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_BETTER",
          "number": 49
        },
        {
          "name": "ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_EQUAL",
          "number": 50
        },
        {
          "name": "ADVANCED_STAT_TYPE_ENDGAME_WIN_PERCENTAGE_WORSE",
          "number": 51
        },
        {
          "name": "ADVANCED_STAT_TYPE_KING_PAWN_ACCURACY",
          "number": 52
        },
        {
          "name": "ADVANCED_STAT_TYPE_ROOK_PAWN_ACCURACY",
          "number": 53
        },
        {
          "name": "ADVANCED_STAT_TYPE_QUEEN_ACCURACY",
          "number": 54
        },
        {
          "name": "ADVANCED_STAT_TYPE_OTHER_ACCURACY",
          "number": 55
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_KING_SAFETY_AND_CASTLING",
          "number": 56
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_DEVELOPMENT",
          "number": 57
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_CENTER_CONTROL",
          "number": 58
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_KING_SAFETY_AND_CASTLING",
          "number": 59
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_DEVELOPMENT",
          "number": 60
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_CENTER_CONTROL",
          "number": 61
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_BACKWARD_PAWNS",
          "number": 62
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_ISOLATED_PAWNS",
          "number": 63
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_DOUBLED_PAWNS",
          "number": 64
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_PAWN_CHAINS",
          "number": 65
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_PASSED_PAWNS",
          "number": 66
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_OUTPOSTS",
          "number": 67
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_OPEN_FILES",
          "number": 68
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_PIECE_ACTIVITY",
          "number": 69
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_BLOCKADES",
          "number": 70
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_TRADES",
          "number": 71
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_SPACE",
          "number": 72
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_OCCUPYING_CENTER",
          "number": 73
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_CENTRAL_BREAKS",
          "number": 74
        },
        {
          "name": "ADVANCED_STAT_TYPE_GOOD_KING_SAFETY",
          "number": 75
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_BACKWARD_PAWNS",
          "number": 76
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_ISOLATED_PAWNS",
          "number": 77
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_DOUBLED_PAWNS",
          "number": 78
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_PAWN_CHAINS",
          "number": 79
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_PASSED_PAWNS",
          "number": 80
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_OUTPOSTS",
          "number": 81
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_OPEN_FILES",
          "number": 82
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_PIECE_ACTIVITY",
          "number": 83
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_BLOCKADES",
          "number": 84
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_TRADES",
          "number": 85
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_SPACE",
          "number": 86
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_OCCUPYING_CENTER",
          "number": 87
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_CENTRAL_BREAKS",
          "number": 88
        },
        {
          "name": "ADVANCED_STAT_TYPE_BAD_KING_SAFETY",
          "number": 89
        },
        {
          "name": "ADVANCED_STAT_TYPE_TIME_BLUNDERS",
          "number": 90
        },
        {
          "name": "ADVANCED_STAT_TYPE_TIME_DISCERNMENT",
          "number": 91
        },
        {
          "name": "ADVANCED_STAT_TYPE_TIME_PRESSURE_ACCURACY",
          "number": 92
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOCK_ADVANTAGE",
          "number": 93
        },
        {
          "name": "ADVANCED_STAT_TYPE_FLAG_RATE",
          "number": 94
        },
        {
          "name": "ADVANCED_STAT_TYPE_SWINDLE_RATE",
          "number": 95
        },
        {
          "name": "ADVANCED_STAT_TYPE_RUSHED_GAME_RATE",
          "number": 96
        },
        {
          "name": "ADVANCED_STAT_TYPE_OPENING_CATEGORY",
          "number": 100
        },
        {
          "name": "ADVANCED_STAT_TYPE_TACTICS_CATEGORY",
          "number": 101
        },
        {
          "name": "ADVANCED_STAT_TYPE_STRATEGY_CATEGORY",
          "number": 102
        },
        {
          "name": "ADVANCED_STAT_TYPE_ENDGAME_CATEGORY",
          "number": 103
        },
        {
          "name": "ADVANCED_STAT_TYPE_CLOCK_CATEGORY",
          "number": 104
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 64015.

```text
AGEhsKF0NPQUNIX0VNT1RJT05fQ09OQ0VSTkVEEAcSFQoRQ09BQ0hfRU1PVElPTl9TQUQQCBoJGAGKph0DCgEBYgZwcm90bzM","chesscom/stats/v1/advanced_stat_type.proto":"CipjaGVzc2NvbS9zdGF0cy92MS9hZHZhbmNlZF9zdGF0X3R5cGUucHJvdG8SEWNoZXNzY29tLnN0YXRzLnYxKuAjChBBZHZhbmNlZFN0YXRUeXBlEiIKHkFEVkFOQ0VEX1NUQVRfVFlQRV9VTlNQRUNJRklFRBAAEicKI0FEVkFOQ0VEX1NUQVRfVFlQRV9PUEVOSU5HX0FDQ1VSQUNZEAESJwojQURWQU5DRURfU1RBVF9UWVBFX09QRU5JTkdfTUlTVEFLRVMQAhIhCh1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17483"></a>
## FND-17483: Full frontend descriptor: chesscom/stats/v1/advanced_stat_example.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/stats/v1/advanced_stat_example.proto",
  "package": "chesscom.stats.v1",
  "message_type": [
    {
      "name": "AdvancedStatExample",
      "field": [
        {
          "name": "stat",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatType"
        },
        {
          "name": "outcome",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.stats.v1.AdvancedStatExampleOutcome"
        },
        {
          "name": "ply",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "san",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "AdvancedStatExampleOutcome",
      "value": [
        {
          "name": "ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD",
          "number": 1
        },
        {
          "name": "ADVANCED_STAT_EXAMPLE_OUTCOME_BAD",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 70263.

```text
OREdBTUVfQ0FURUdPUlkQZxIlCiFBRFZBTkNFRF9TVEFUX1RZUEVfQ0xPQ0tfQ0FURUdPUlkQaBoHiqYdAwoBAWIGcHJvdG8z","chesscom/stats/v1/advanced_stat_example.proto":"Ci1jaGVzc2NvbS9zdGF0cy92MS9hZHZhbmNlZF9zdGF0X2V4YW1wbGUucHJvdG8SEWNoZXNzY29tLnN0YXRzLnYxIqsBChNBZHZhbmNlZFN0YXRFeGFtcGxlEjEKBHN0YXQYASABKA4yIy5jaGVzc2NvbS5zdGF0cy52MS5BZHZhbmNlZFN0YXRUeXBlEj4KB291dGNvbWUYAiABKA4yLS5jaGVzc2NvbS5zdGF0cy52MS5BZHZhbmNlZFN0YXRFeGFtcGxlT3V0Y29t
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17484"></a>
## FND-17484: Full frontend descriptor: chesscom/proto_options/kafka/v1/kafka_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/kafka/v1/kafka_options.proto",
  "package": "chesscom.proto_options.kafka.v1",
  "message_type": [
    {
      "name": "KafkaOptions",
      "field": [
        {
          "name": "default_config",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        },
        {
          "name": "config",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaOptions.ConfigEntry"
        },
        {
          "name": "chesskid",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "environment_config",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaEnvironments"
        },
        {
          "name": "skip_schema_registry",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "nested_type": [
        {
          "name": "ConfigEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    },
    {
      "name": "KafkaEnvironments",
      "field": [
        {
          "name": "prod",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        },
        {
          "name": "sandbox",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        },
        {
          "name": "staging",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        },
        {
          "name": "chesskid_staging",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        },
        {
          "name": "chesskid_prod",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs"
        }
      ]
    },
    {
      "name": "KafkaConfigs",
      "field": [
        {
          "name": "retention_ms",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "cleanup_policy",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "num_partitions",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_INT32"
        },
        {
          "name": "additional_config",
          "number": 4,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.kafka.v1.KafkaConfigs.AdditionalConfigEntry"
        },
        {
          "name": "retention_duration",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.kafka.v1.Duration"
        }
      ],
      "nested_type": [
        {
          "name": "AdditionalConfigEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "Duration",
      "value": [
        {
          "name": "DURATION_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "DURATION_ONE_HOUR",
          "number": 3600000
        },
        {
          "name": "DURATION_TWO_HOURS",
          "number": 7200000
        },
        {
          "name": "DURATION_ONE_DAY",
          "number": 86400000
        },
        {
          "name": "DURATION_THREE_DAYS",
          "number": 259200000
        },
        {
          "name": "DURATION_ONE_WEEK",
          "number": 604800000
        },
        {
          "name": "DURATION_TWO_WEEKS",
          "number": 1209600000
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "kafka",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 90000,
      "label": "LABEL_REPEATED",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.kafka.v1.KafkaOptions",
      "json_name": "kafka"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 70866.

```text
MRV9PVVRDT01FX0dPT0QQARIlCiFBRFZBTkNFRF9TVEFUX0VYQU1QTEVfT1VUQ09NRV9CQUQQAhoHiqYdAwoBAWIGcHJvdG8z","chesscom/proto_options/kafka/v1/kafka_options.proto":"CjNjaGVzc2NvbS9wcm90b19vcHRpb25zL2thZmthL3YxL2thZmthX29wdGlvbnMucHJvdG8SH2NoZXNzY29tLnByb3RvX29wdGlvbnMua2Fma2EudjEizwIKDEthZmthT3B0aW9ucxJFCg5kZWZhdWx0X2NvbmZpZxgBIAEoCzItLmNoZXNzY29tLnByb3RvX29wdGlvbnMua2Fma2EudjEuS2Fma2FDb25maWdzEkkKBmNvbmZpZxgCIAMoCzI5LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17485"></a>
## FND-17485: Full frontend descriptor: chesscom/game_storage/v2/player_title.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/player_title.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "PlayerTitle",
      "value": [
        {
          "name": "PLAYER_TITLE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_TITLE_WGM",
          "number": 1
        },
        {
          "name": "PLAYER_TITLE_GM",
          "number": 2
        },
        {
          "name": "PLAYER_TITLE_WIM",
          "number": 3
        },
        {
          "name": "PLAYER_TITLE_IM",
          "number": 4
        },
        {
          "name": "PLAYER_TITLE_WFM",
          "number": 5
        },
        {
          "name": "PLAYER_TITLE_FM",
          "number": 6
        },
        {
          "name": "PLAYER_TITLE_WNM",
          "number": 7
        },
        {
          "name": "PLAYER_TITLE_NM",
          "number": 8
        },
        {
          "name": "PLAYER_TITLE_M",
          "number": 9
        },
        {
          "name": "PLAYER_TITLE_CM",
          "number": 10
        },
        {
          "name": "PLAYER_TITLE_WCM",
          "number": 11
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 72791.

```text
vbnMYkL8FIAMoCzItLmNoZXNzY29tLnByb3RvX29wdGlvbnMua2Fma2EudjEuS2Fma2FPcHRpb25zUgVrYWZrYWIGcHJvdG8z","chesscom/game_storage/v2/player_title.proto":"CitjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcGxheWVyX3RpdGxlLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIqoAIKC1BsYXllclRpdGxlEhwKGFBMQVlFUl9USVRMRV9VTlNQRUNJRklFRBAAEhQKEFBMQVlFUl9USVRMRV9XR00QARITCg9QTEFZRVJfVElUTEVfR00QAhIUChBQTEFZRVJfVElUTEVfV0lNEAMSEwoPUExBWUVSX1RJVExFX0lNEAQSFA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17486"></a>
## FND-17486: Full frontend descriptor: chesscom/game_storage/v2/game_origin.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/game_origin.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "GameOrigin",
      "value": [
        {
          "name": "GAME_ORIGIN_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_ORIGIN_DIRECT_CHALLENGE",
          "number": 1
        },
        {
          "name": "GAME_ORIGIN_SEEK",
          "number": 2
        },
        {
          "name": "GAME_ORIGIN_POOL_SEEK",
          "number": 3
        },
        {
          "name": "GAME_ORIGIN_START_GAME",
          "number": 4
        },
        {
          "name": "GAME_ORIGIN_MATCH",
          "number": 5
        },
        {
          "name": "GAME_ORIGIN_ARENA",
          "number": 6
        },
        {
          "name": "GAME_ORIGIN_TOURNAMENT",
          "number": 7
        },
        {
          "name": "GAME_ORIGIN_TEAM_MATCH",
          "number": 8
        },
        {
          "name": "GAME_ORIGIN_COMPETITION",
          "number": 9
        },
        {
          "name": "GAME_ORIGIN_RECOMMENDED_MATCH",
          "number": 10
        },
        {
          "name": "GAME_ORIGIN_LEAGUE",
          "number": 11
        },
        {
          "name": "GAME_ORIGIN_SIMUL",
          "number": 12
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 73334.

```text
VJfVElUTEVfTRAJEhMKD1BMQVlFUl9USVRMRV9DTRAKEhQKEFBMQVlFUl9USVRMRV9XQ00QCxoIiqYdBAoCAQJiBnByb3RvMw","chesscom/game_storage/v2/game_origin.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9vcmlnaW4ucHJvdG8SGGNoZXNzY29tLmdhbWVfc3RvcmFnZS52Mir3AgoKR2FtZU9yaWdpbhIbChdHQU1FX09SSUdJTl9VTlNQRUNJRklFRBAAEiAKHEdBTUVfT1JJR0lOX0RJUkVDVF9DSEFMTEVOR0UQARIUChBHQU1FX09SSUdJTl9TRUVLEAISGQoVR0FNRV9PUklHSU5fUE9PTF9TRUVLEAMSGgoWR0FNRV9
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17487"></a>
## FND-17487: Full frontend descriptor: chesscom/game_storage/v2/player_result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/player_result.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "PlayerResult",
      "value": [
        {
          "name": "PLAYER_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_RESULT_WIN",
          "number": 1
        },
        {
          "name": "PLAYER_RESULT_DRAW",
          "number": 2
        },
        {
          "name": "PLAYER_RESULT_LOSE",
          "number": 3
        },
        {
          "name": "PLAYER_RESULT_ABORT",
          "number": 4
        },
        {
          "name": "PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE",
          "number": 5
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 73990.

```text
fTUFUQ0gQChIWChJHQU1FX09SSUdJTl9MRUFHVUUQCxIVChFHQU1FX09SSUdJTl9TSU1VTBAMGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/player_result.proto":"CixjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcGxheWVyX3Jlc3VsdC5wcm90bxIYY2hlc3Njb20uZ2FtZV9zdG9yYWdlLnYyKsABCgxQbGF5ZXJSZXN1bHQSHQoZUExBWUVSX1JFU1VMVF9VTlNQRUNJRklFRBAAEhUKEVBMQVlFUl9SRVNVTFRfV0lOEAESFgoSUExBWUVSX1JFU1VMVF9EUkFXEAISFgoSUExBWUVSX1JFU1VMVF9MT1NFEAMSFwoTUExBWUVSX1JFU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17488"></a>
## FND-17488: Full frontend descriptor: chesscom/game_storage/v2/game_provider.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/game_provider.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "GameProvider",
      "value": [
        {
          "name": "GAME_PROVIDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PROVIDER_CHESS_COM",
          "number": 1
        },
        {
          "name": "GAME_PROVIDER_CHESS_KID",
          "number": 2
        },
        {
          "name": "GAME_PROVIDER_FIDE",
          "number": 3
        },
        {
          "name": "GAME_PROVIDER_LICHESS",
          "number": 4
        },
        {
          "name": "GAME_PROVIDER_CHESSBASE",
          "number": 5
        },
        {
          "name": "GAME_PROVIDER_OFFLINE",
          "number": 6
        },
        {
          "name": "GAME_PROVIDER_CHESS_COM_MASTER_GAMES",
          "number": 7
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 74407.

```text
JFU1VMVF9BQk9SVBAEEicKI1BMQVlFUl9SRVNVTFRfQlVHSE9VU0VfUEFSVE5FUl9MT1NFEAUaCIqmHQQKAgECYgZwcm90bzM","chesscom/game_storage/v2/game_provider.proto":"CixjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9wcm92aWRlci5wcm90bxIYY2hlc3Njb20uZ2FtZV9zdG9yYWdlLnYyKoYCCgxHYW1lUHJvdmlkZXISHQoZR0FNRV9QUk9WSURFUl9VTlNQRUNJRklFRBAAEhsKF0dBTUVfUFJPVklERVJfQ0hFU1NfQ09NEAESGwoXR0FNRV9QUk9WSURFUl9DSEVTU19LSUQQAhIWChJHQU1FX1BST1ZJREVSX0ZJREUQAxIZC
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17489"></a>
## FND-17489: Full frontend descriptor: chesscom/game_storage/v2/rating_class.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/rating_class.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "RatingClass",
      "value": [
        {
          "name": "RATING_CLASS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RATING_CLASS_UNRATED",
          "number": 1
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_BULLET",
          "number": 2
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_BLITZ",
          "number": 3
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_RAPID",
          "number": 4
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_DAILY",
          "number": 5
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS960",
          "number": 6
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS960_DAILY",
          "number": 7
        },
        {
          "name": "RATING_CLASS_CHESS_COM_BUGHOUSE",
          "number": 8
        },
        {
          "name": "RATING_CLASS_CHESS_COM_KINGOFTHEHILL",
          "number": 9
        },
        {
          "name": "RATING_CLASS_CHESS_COM_THREECHECK",
          "number": 10
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CRAZYHOUSE",
          "number": 11
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_STANDARD",
          "number": 12
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_RAPID",
          "number": 13
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_BLITZ",
          "number": 14
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS",
          "number": 15
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 74917.

```text
ERVJfT0ZGTElORRAGEigKJEdBTUVfUFJPVklERVJfQ0hFU1NfQ09NX01BU1RFUl9HQU1FUxAHGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/rating_class.proto":"CitjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcmF0aW5nX2NsYXNzLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIq9gQKC1JhdGluZ0NsYXNzEhwKGFJBVElOR19DTEFTU19VTlNQRUNJRklFRBAAEhgKFFJBVElOR19DTEFTU19VTlJBVEVEEAESJwojUkFUSU5HX0NMQVNTX0NIRVNTX0NPTV9DSEVTU19CVUxMRVQQAhImCiJSQVRJTkdfQ0xBU1NfQ0hFU1
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17490"></a>
## FND-17490: Full frontend descriptor: chesscom/game_storage/v2/game_result.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/game_result.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "GameResult",
      "value": [
        {
          "name": "GAME_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_TIMEOUT",
          "number": 1
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_CHECKMATE",
          "number": 2
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_RESIGNATION",
          "number": 3
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_ABANDONMENT",
          "number": 4
        },
        {
          "name": "GAME_RESULT_DRAW_BY_AGREEMENT",
          "number": 5
        },
        {
          "name": "GAME_RESULT_DRAW_BY_REPETITION",
          "number": 6
        },
        {
          "name": "GAME_RESULT_DRAW_BY_STALEMATE",
          "number": 7
        },
        {
          "name": "GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL",
          "number": 8
        },
        {
          "name": "GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL",
          "number": 9
        },
        {
          "name": "GAME_RESULT_DRAW_BY_50_MOVE_RULE",
          "number": 10
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE",
          "number": 11
        },
        {
          "name": "GAME_RESULT_ABORTED",
          "number": 12
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_THREE_CHECK",
          "number": 13
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL",
          "number": 14
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT",
          "number": 15
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 75916.

```text
1NfQkxJVFoQDhIrCidSQVRJTkdfQ0xBU1NfQ0hFU1NfQ09NX0NIRVNTX09ERFNfQ0hFU1MQDxoIiqYdBAoCAQJiBnByb3RvMw","chesscom/game_storage/v2/game_result.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9yZXN1bHQucHJvdG8SGGNoZXNzY29tLmdhbWVfc3RvcmFnZS52MiqZBQoKR2FtZVJlc3VsdBIbChdHQU1FX1JFU1VMVF9VTlNQRUNJRklFRBAAEiMKH0dBTUVfUkVTVUxUX1dJTl9MT1NFX0JZX1RJTUVPVVQQARIlCiFHQU1FX1JFU1VMVF9XSU5fTE9TRV9CWV9DSEVDS01BVEUQAhInCiNHQU1FX1JFU1VMVF9
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17491"></a>
## FND-17491: Full frontend descriptor: chesscom/game_storage/v2/game_privacy.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/game_privacy.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "GamePrivacy",
      "value": [
        {
          "name": "GAME_PRIVACY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PRIVACY_PUBLIC",
          "number": 1
        },
        {
          "name": "GAME_PRIVACY_PRIVATE",
          "number": 2
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 76959.

```text
9USEVfSElMTBAOEioKJkdBTUVfUkVTVUxUX1dJTl9MT1NFX0JZX0RPVUJMRV9GT1JGRUlUEA8aCIqmHQQKAgECYgZwcm90bzM","chesscom/game_storage/v2/game_privacy.proto":"CitjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9wcml2YWN5LnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIqaAoLR2FtZVByaXZhY3kSHAoYR0FNRV9QUklWQUNZX1VOU1BFQ0lGSUVEEAASFwoTR0FNRV9QUklWQUNZX1BVQkxJQxABEhgKFEdBTUVfUFJJVkFDWV9QUklWQVRFEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/computer/v2/ass
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17492"></a>
## FND-17492: Full frontend descriptor: chesscom/computer/v2/assisted_game_feature.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/computer/v2/assisted_game_feature.proto",
  "package": "chesscom.computer.v2",
  "enum_type": [
    {
      "name": "AssistedGameFeature",
      "value": [
        {
          "name": "ASSISTED_GAME_FEATURE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "ASSISTED_GAME_FEATURE_CHAT",
          "number": 1
        },
        {
          "name": "ASSISTED_GAME_FEATURE_ANALYSIS",
          "number": 2
        },
        {
          "name": "ASSISTED_GAME_FEATURE_HINTS",
          "number": 3
        },
        {
          "name": "ASSISTED_GAME_FEATURE_THREATS",
          "number": 4
        },
        {
          "name": "ASSISTED_GAME_FEATURE_EVALUATION",
          "number": 5
        },
        {
          "name": "ASSISTED_GAME_FEATURE_ENGINE",
          "number": 6
        },
        {
          "name": "ASSISTED_GAME_FEATURE_SUGGESTIONS",
          "number": 7
        },
        {
          "name": "ASSISTED_GAME_FEATURE_TAKEBACKS",
          "number": 8
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 77255.

```text
VEEAASFwoTR0FNRV9QUklWQUNZX1BVQkxJQxABEhgKFEdBTUVfUFJJVkFDWV9QUklWQVRFEAIaCIqmHQQKAgECYgZwcm90bzM","chesscom/computer/v2/assisted_game_feature.proto":"CjBjaGVzc2NvbS9jb21wdXRlci92Mi9hc3Npc3RlZF9nYW1lX2ZlYXR1cmUucHJvdG8SFGNoZXNzY29tLmNvbXB1dGVyLnYyKuICChNBc3Npc3RlZEdhbWVGZWF0dXJlEiUKIUFTU0lTVEVEX0dBTUVfRkVBVFVSRV9VTlNQRUNJRklFRBAAEh4KGkFTU0lTVEVEX0dBTUVfRkVBVFVSRV9DSEFUEAESIgoeQVNTSVNURURfR0FNRV9GRUFUVVJFX0FOQUxZU0lTE
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17493"></a>
## FND-17493: Full frontend descriptor: chesscom/computer/v2/game_mode.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/computer/v2/game_mode.proto",
  "package": "chesscom.computer.v2",
  "enum_type": [
    {
      "name": "GameMode",
      "value": [
        {
          "name": "GAME_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_MODE_CHALLENGE",
          "number": 1
        },
        {
          "name": "GAME_MODE_FRIENDLY",
          "number": 2
        },
        {
          "name": "GAME_MODE_ASSISTED",
          "number": 3
        },
        {
          "name": "GAME_MODE_CUSTOM",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 77892.

```text
RVUkVfU1VHR0VTVElPTlMQBxIjCh9BU1NJU1RFRF9HQU1FX0ZFQVRVUkVfVEFLRUJBQ0tTEAgaCIqmHQQKAgECYgZwcm90bzM","chesscom/computer/v2/game_mode.proto":"CiRjaGVzc2NvbS9jb21wdXRlci92Mi9nYW1lX21vZGUucHJvdG8SFGNoZXNzY29tLmNvbXB1dGVyLnYyKo4BCghHYW1lTW9kZRIZChVHQU1FX01PREVfVU5TUEVDSUZJRUQQABIXChNHQU1FX01PREVfQ0hBTExFTkdFEAESFgoSR0FNRV9NT0RFX0ZSSUVORExZEAISFgoSR0FNRV9NT0RFX0FTU0lTVEVEEAMSFAoQR0FNRV9NT0RFX0NVU1RPTRAEGgiKph0ECgIBAmIGcHJvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17494"></a>
## FND-17494: Full frontend descriptor: chesscom/game_storage/v2/vs_computer_game_data.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/vs_computer_game_data.proto",
  "package": "chesscom.game_storage.v2",
  "message_type": [
    {
      "name": "VsComputerGameData",
      "field": [
        {
          "name": "assisted_game_features",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.computer.v2.AssistedGameFeature"
        },
        {
          "name": "crowns_earned",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "bot_personality_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "game_mode",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.computer.v2.GameMode"
        },
        {
          "name": "event_config_key",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_crowns_earned"
        },
        {
          "name": "_event_config_key"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 78218.

```text
SSUVORExZEAISFgoSR0FNRV9NT0RFX0FTU0lTVEVEEAMSFAoQR0FNRV9NT0RFX0NVU1RPTRAEGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/vs_computer_game_data.proto":"CjRjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvdnNfY29tcHV0ZXJfZ2FtZV9kYXRhLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIimgIKElZzQ29tcHV0ZXJHYW1lRGF0YRJJChZhc3Npc3RlZF9nYW1lX2ZlYXR1cmVzGAEgAygOMikuY2hlc3Njb20uY29tcHV0ZXIudjIuQXNzaXN0ZWRHYW1lRmVhdHVyZRIaCg1jcm93bnNfZWFybmVkGAIgA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17495"></a>
## FND-17495: Full frontend descriptor: chesscom/game_storage/v2/vs_coach_game_data.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/vs_coach_game_data.proto",
  "package": "chesscom.game_storage.v2",
  "message_type": [
    {
      "name": "VsCoachGameData",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 78774.

```text
19rZXkYBSABKAlIAYgBAToIgqYdBAoCAQJCEAoOX2Nyb3duc19lYXJuZWRCEwoRX2V2ZW50X2NvbmZpZ19rZXliBnByb3RvMw","chesscom/game_storage/v2/vs_coach_game_data.proto":"CjFjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvdnNfY29hY2hfZ2FtZV9kYXRhLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIiLQoPVnNDb2FjaEdhbWVEYXRhEhAKCGNvYWNoX2lkGAEgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/game_server.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9z
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17496"></a>
## FND-17496: Full frontend descriptor: chesscom/game_storage/v2/game_server.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/game_server.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "GameServer",
      "value": [
        {
          "name": "GAME_SERVER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_SERVER_RCN",
          "number": 1
        },
        {
          "name": "GAME_SERVER_LIVE_CHESS",
          "number": 2
        },
        {
          "name": "GAME_SERVER_WEB",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 79005.

```text
vbS5nYW1lX3N0b3JhZ2UudjIiLQoPVnNDb2FjaEdhbWVEYXRhEhAKCGNvYWNoX2lkGAEgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/game_server.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvZ2FtZV9zZXJ2ZXIucHJvdG8SGGNoZXNzY29tLmdhbWVfc3RvcmFnZS52Mip5CgpHYW1lU2VydmVyEhsKF0dBTUVfU0VSVkVSX1VOU1BFQ0lGSUVEEAASEwoPR0FNRV9TRVJWRVJfUkNOEAESGgoWR0FNRV9TRVJWRVJfTElWRV9DSEVTUxACEhMKD0dBTUVfU0VSVkVSX1dFQhADGgiKph0ECgIBAmIGcHJvdG8z","ches
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17497"></a>
## FND-17497: Full frontend descriptor: chesscom/game_storage/v2/player_type.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/player_type.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "PlayerType",
      "value": [
        {
          "name": "PLAYER_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_TYPE_HUMAN",
          "number": 1
        },
        {
          "name": "PLAYER_TYPE_COMPUTER",
          "number": 2
        },
        {
          "name": "PLAYER_TYPE_CYBORG",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 79321.

```text
fUkNOEAESGgoWR0FNRV9TRVJWRVJfTElWRV9DSEVTUxACEhMKD0dBTUVfU0VSVkVSX1dFQhADGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/player_type.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcGxheWVyX3R5cGUucHJvdG8SGGNoZXNzY29tLmdhbWVfc3RvcmFnZS52Mip8CgpQbGF5ZXJUeXBlEhsKF1BMQVlFUl9UWVBFX1VOU1BFQ0lGSUVEEAASFQoRUExBWUVSX1RZUEVfSFVNQU4QARIYChRQTEFZRVJfVFlQRV9DT01QVVRFUhACEhYKElBMQVlFUl9UWVBFX0NZQk9SRxADGgiKph0ECgIBAmIGcHJvdG8z","
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17498"></a>
## FND-17498: Full frontend descriptor: chesscom/game_storage/v2/player_provider.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/player_provider.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "PlayerProvider",
      "value": [
        {
          "name": "PLAYER_PROVIDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_COM",
          "number": 1
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_KID",
          "number": 2
        },
        {
          "name": "PLAYER_PROVIDER_FIDE",
          "number": 3
        },
        {
          "name": "PLAYER_PROVIDER_LICHESS_ORG",
          "number": 4
        },
        {
          "name": "PLAYER_PROVIDER_CHESSBASE",
          "number": 5
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_COM_MASTER",
          "number": 6
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 79641.

```text
NQU4QARIYChRQTEFZRVJfVFlQRV9DT01QVVRFUhACEhYKElBMQVlFUl9UWVBFX0NZQk9SRxADGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/player_provider.proto":"Ci5jaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcGxheWVyX3Byb3ZpZGVyLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIq+QEKDlBsYXllclByb3ZpZGVyEh8KG1BMQVlFUl9QUk9WSURFUl9VTlNQRUNJRklFRBAAEh0KGVBMQVlFUl9QUk9WSURFUl9DSEVTU19DT00QARIdChlQTEFZRVJfUFJPVklERVJfQ0hFU1NfS0lEEAISGAoUUExBWUVSX1BST1Z
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17499"></a>
## FND-17499: Full frontend descriptor: chesscom/game_storage/v2/player_bad_sport_behavior.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/player_bad_sport_behavior.proto",
  "package": "chesscom.game_storage.v2",
  "enum_type": [
    {
      "name": "PlayerBadSportBehavior",
      "value": [
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_NONE",
          "number": 1
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED",
          "number": 2
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_ABORT",
          "number": 3
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT",
          "number": 4
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT",
          "number": 5
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED",
          "number": 6
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED",
          "number": 7
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 80139.

```text
klERVJfQ0hFU1NCQVNFEAUSJAogUExBWUVSX1BST1ZJREVSX0NIRVNTX0NPTV9NQVNURVIQBhoIiqYdBAoCAQJiBnByb3RvMw","chesscom/game_storage/v2/player_bad_sport_behavior.proto":"CjhjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvcGxheWVyX2JhZF9zcG9ydF9iZWhhdmlvci5wcm90bxIYY2hlc3Njb20uZ2FtZV9zdG9yYWdlLnYyKoYDChZQbGF5ZXJCYWRTcG9ydEJlaGF2aW9yEikKJVBMQVlFUl9CQURfU1BPUlRfQkVIQVZJT1JfVU5TUEVDSUZJRUQQABIiCh5QTEFZRVJfQkFEX1NQT1JUX0JFSEFWSU9SX05PTkUQARIzCi9QT
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17500"></a>
## FND-17500: Full frontend descriptor: chesscom/game_storage/v2/opening_data.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/opening_data.proto",
  "package": "chesscom.game_storage.v2",
  "message_type": [
    {
      "name": "OpeningData",
      "field": [
        {
          "name": "last_book_eco_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "last_book_ply",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "last_notable_eco_id",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "last_notable_ply",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "eco_family_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "eco_code",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_last_book_eco_id"
        },
        {
          "name": "_last_book_ply"
        },
        {
          "name": "_last_notable_eco_id"
        },
        {
          "name": "_last_notable_ply"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 80848.

```text
ozUExBWUVSX0JBRF9TUE9SVF9CRUhBVklPUl9CT1RIX1BMQVlFUlNfRElTQ09OTkVDVEVEEAcaCIqmHQQKAgECYgZwcm90bzM","chesscom/game_storage/v2/opening_data.proto":"CitjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvb3BlbmluZ19kYXRhLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIikAIKC09wZW5pbmdEYXRhEh0KEGxhc3RfYm9va19lY29faWQYASABKA1IAIgBARIaCg1sYXN0X2Jvb2tfcGx5GAIgASgNSAGIAQESIAoTbGFzdF9ub3RhYmxlX2Vjb19pZBgDIAEoDUgCiAEBEh0KEGxhc3Rfbm90YWJsZV9wbHkYBCABKA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17501"></a>
## FND-17501: Full frontend descriptor: chesscom/tdtools/v1/identifiers.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/tdtools/v1/identifiers.proto",
  "package": "chesscom.tdtools.v1",
  "message_type": [
    {
      "name": "ChessComTournamentIdentifier",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.tdtools.v1.ChessComTournamentType"
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "ChessComTournamentType",
      "value": [
        {
          "name": "CHESS_COM_TOURNAMENT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TOURNAMENT",
          "number": 1
        },
        {
          "name": "ARENA",
          "number": 2
        },
        {
          "name": "TEAM_MATCH",
          "number": 3
        },
        {
          "name": "SIMUL",
          "number": 4
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 81369.

```text
pZEIQCg5fbGFzdF9ib29rX3BseUIWChRfbGFzdF9ub3RhYmxlX2Vjb19pZEITChFfbGFzdF9ub3RhYmxlX3BseWIGcHJvdG8z","chesscom/tdtools/v1/identifiers.proto":"CiVjaGVzc2NvbS90ZHRvb2xzL3YxL2lkZW50aWZpZXJzLnByb3RvEhNjaGVzc2NvbS50ZHRvb2xzLnYxIm8KHENoZXNzQ29tVG91cm5hbWVudElkZW50aWZpZXISCgoCaWQYASABKA0SOQoEdHlwZRgCIAEoDjIrLmNoZXNzY29tLnRkdG9vbHMudjEuQ2hlc3NDb21Ub3VybmFtZW50VHlwZToIgqYdBAoCAQIqgwEKFkNoZXNzQ29tVG91cm5hbWVudFR5cGUSKQolQ0hFU1Nf
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17502"></a>
## FND-17502: Full frontend descriptor: chesscom/game_storage/v2/tournament_data.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/tournament_data.proto",
  "package": "chesscom.game_storage.v2",
  "message_type": [
    {
      "name": "TournamentData",
      "field": [
        {
          "name": "chess_com_tournament_identifier",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.tdtools.v1.ChessComTournamentIdentifier"
        },
        {
          "name": "round",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 81832.

```text
AEg4KClRPVVJOQU1FTlQQARIJCgVBUkVOQRACEg4KClRFQU1fTUFUQ0gQAxIJCgVTSU1VTBAEGgiKph0ECgIBAmIGcHJvdG8z","chesscom/game_storage/v2/tournament_data.proto":"Ci5jaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvdG91cm5hbWVudF9kYXRhLnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIihQEKDlRvdXJuYW1lbnREYXRhEloKH2NoZXNzX2NvbV90b3VybmFtZW50X2lkZW50aWZpZXIYASABKAsyMS5jaGVzc2NvbS50ZHRvb2xzLnYxLkNoZXNzQ29tVG91cm5hbWVudElkZW50aWZpZXISDQoFcm91bmQYAiABKA06CIK
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17503"></a>
## FND-17503: Full frontend descriptor: chesscom/game_storage/v2/special_game_event.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v2/special_game_event.proto",
  "package": "chesscom.game_storage.v2",
  "message_type": [
    {
      "name": "SpecialGameEvent",
      "field": [
        {
          "name": "is_featured",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_pcl",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 82175.

```text
50ZHRvb2xzLnYxLkNoZXNzQ29tVG91cm5hbWVudElkZW50aWZpZXISDQoFcm91bmQYAiABKA06CIKmHQQKAgECYgZwcm90bzM","chesscom/game_storage/v2/special_game_event.proto":"CjFjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjIvc3BlY2lhbF9nYW1lX2V2ZW50LnByb3RvEhhjaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIiQQoQU3BlY2lhbEdhbWVFdmVudBITCgtpc19mZWF0dXJlZBgBIAEoCBIOCgZpc19wY2wYAiABKAg6CIKmHQQKAgECYgZwcm90bzM","chesscom/proto_options/oauth/v1/scope_options.proto":"CjNjaGVz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17504"></a>
## FND-17504: Full frontend descriptor: chesscom/proto_options/oauth/v1/scope_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/oauth/v1/scope_options.proto",
  "package": "chesscom.proto_options.oauth.v1",
  "enum_type": [
    {
      "name": "ScopeVisibility",
      "value": [
        {
          "name": "SCOPE_VISIBILITY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SCOPE_VISIBILITY_INTERNAL",
          "number": 1
        },
        {
          "name": "SCOPE_VISIBILITY_PUBLIC",
          "number": 2
        },
        {
          "name": "SCOPE_VISIBILITY_PRIVILEGED",
          "number": 3
        }
      ]
    },
    {
      "name": "ScopeConsent",
      "value": [
        {
          "name": "SCOPE_CONSENT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SCOPE_CONSENT_OPTIONAL",
          "number": 1
        },
        {
          "name": "SCOPE_CONSENT_REQUIRED",
          "number": 2
        },
        {
          "name": "SCOPE_CONSENT_IMPLICIT",
          "number": 3
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "scope_name",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 91100,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "scopeName",
      "proto3_optional": true
    },
    {
      "name": "scope_description",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 91101,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "scopeDescription",
      "proto3_optional": true
    },
    {
      "name": "scope_visibility",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 91102,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.proto_options.oauth.v1.ScopeVisibility",
      "json_name": "scopeVisibility",
      "proto3_optional": true
    },
    {
      "name": "scope_consent",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 91103,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.proto_options.oauth.v1.ScopeConsent",
      "json_name": "scopeConsent",
      "proto3_optional": true
    },
    {
      "name": "scope_legacy_names",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 91104,
      "label": "LABEL_REPEATED",
      "type": "TYPE_STRING",
      "json_name": "scopeLegacyNames"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 82433.

```text
oQU3BlY2lhbEdhbWVFdmVudBITCgtpc19mZWF0dXJlZBgBIAEoCBIOCgZpc19wY2wYAiABKAg6CIKmHQQKAgECYgZwcm90bzM","chesscom/proto_options/oauth/v1/scope_options.proto":"CjNjaGVzc2NvbS9wcm90b19vcHRpb25zL29hdXRoL3YxL3Njb3BlX29wdGlvbnMucHJvdG8SH2NoZXNzY29tLnByb3RvX29wdGlvbnMub2F1dGgudjEqkAEKD1Njb3BlVmlzaWJpbGl0eRIgChxTQ09QRV9WSVNJQklMSVRZX1VOU1BFQ0lGSUVEEAASHQoZU0NPUEVfVklTSUJJTElUWV9JTlRFUk5BTBABEhsKF1NDT1BFX1ZJU0lCSUxJVFlfUFVCTElDEA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17505"></a>
## FND-17505: Full frontend descriptor: chesscom/oauth/v1/scope.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/oauth/v1/scope.proto",
  "package": "chesscom.oauth.v1",
  "enum_type": [
    {
      "name": "Scope",
      "value": [
        {
          "name": "SCOPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "SCOPE_PUBLIC",
          "number": 1,
          "options": {}
        },
        {
          "name": "SCOPE_NONE",
          "number": 2,
          "options": {}
        },
        {
          "name": "SCOPE_CHESS",
          "number": 100,
          "options": {}
        },
        {
          "name": "SCOPE_ADDRESS",
          "number": 200,
          "options": {}
        },
        {
          "name": "SCOPE_EMAIL",
          "number": 201,
          "options": {}
        },
        {
          "name": "SCOPE_OPENID",
          "number": 202,
          "options": {}
        },
        {
          "name": "SCOPE_PROFILE",
          "number": 203,
          "options": {}
        },
        {
          "name": "SCOPE_EBOARD",
          "number": 204,
          "options": {}
        },
        {
          "name": "SCOPE_NOADS",
          "number": 205,
          "options": {}
        },
        {
          "name": "SCOPE_PROLONGED_TOKEN",
          "number": 206,
          "options": {}
        },
        {
          "name": "SCOPE_ANALYSIS",
          "number": 300,
          "options": {}
        },
        {
          "name": "SCOPE_ARTICLES_READ",
          "number": 301,
          "options": {}
        },
        {
          "name": "SCOPE_ATTRIBUTION_WRITE",
          "number": 302,
          "options": {}
        },
        {
          "name": "SCOPE_COMMENTS_WRITE",
          "number": 303,
          "options": {}
        },
        {
          "name": "SCOPE_COMPUTER_GAMES_MANAGE",
          "number": 304,
          "options": {}
        },
        {
          "name": "SCOPE_COMPUTER_GAMES_PLAY",
          "number": 305,
          "options": {}
        },
        {
          "name": "SCOPE_CONTACTS_READ",
          "number": 306,
          "options": {}
        },
        {
          "name": "SCOPE_CONTACTS_WRITE",
          "number": 307,
          "options": {}
        },
        {
          "name": "SCOPE_ENDGAMES",
          "number": 308,
          "options": {}
        },
        {
          "name": "SCOPE_EXPLORER",
          "number": 347,
          "options": {}
        },
        {
          "name": "SCOPE_FAIRPLAY_READ",
          "number": 349,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SCOPE_FAIRPLAY_WRITE",
          "number": 350,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "SCOPE_FCM",
          "number": 309,
          "options": {}
        },
        {
          "name": "SCOPE_FORUMS_WRITE",
          "number": 310,
          "options": {}
        },
        {
          "name": "SCOPE_FRIENDS_READ",
          "number": 311,
          "options": {}
        },
        {
          "name": "SCOPE_FRIENDS_WRITE",
          "number": 312,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES",
          "number": 600,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES_SEEKS_READ",
          "number": 313,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES_SEEKS_WRITE",
          "number": 314,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES_MANAGE",
          "number": 315,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES_PLAY",
          "number": 316,
          "options": {}
        },
        {
          "name": "SCOPE_GAMES_READ",
          "number": 317,
          "options": {}
        },
        {
          "name": "SCOPE_LEAGUES",
          "number": 318,
          "options": {}
        },
        {
          "name": "SCOPE_LESSONS",
          "number": 319,
          "options": {}
        },
        {
          "name": "SCOPE_MARKETING",
          "number": 320,
          "options": {}
        },
        {
          "name": "SCOPE_MEMBERSHIP",
          "number": 321,
          "options": {}
        },
        {
          "name": "SCOPE_MESSAGES_READ",
          "number": 322,
          "options": {}
        },
        {
          "name": "SCOPE_MESSAGES_WRITE",
          "number": 323,
          "options": {}
        },
        {
          "name": "SCOPE_NOTIFICATIONS",
          "number": 324,
          "options": {}
        },
        {
          "name": "SCOPE_ORDERS_READ",
          "number": 325,
          "options": {}
        },
        {
          "name": "SCOPE_PAGE_CONTEXT_READ",
          "number": 351,
          "options": {}
        },
        {
          "name": "SCOPE_PEACEKEEPER",
          "number": 326,
          "options": {}
        },
        {
          "name": "SCOPE_PRACTICE",
          "number": 327,
          "options": {}
        },
        {
          "name": "SCOPE_PUZZLES_MANAGE",
          "number": 328,
          "options": {}
        },
        {
          "name": "SCOPE_PUZZLES_READ",
          "number": 329,
          "options": {}
        },
        {
          "name": "SCOPE_SESSION",
          "number": 330,
          "options": {}
        },
        {
          "name": "SCOPE_GATEWAY_THEMES",
          "number": 900,
          "options": {}
        },
        {
          "name": "SCOPE_STATS_READ",
          "number": 331,
          "options": {}
        },
        {
          "name": "SCOPE_STREAKS_ADMIN_READ",
          "number": 348,
          "options": {}
        },
        {
          "name": "SCOPE_SUPPORT",
          "number": 10000,
          "options": {}
        },
        {
          "name": "SCOPE_SUPPORT_INTERCOM",
          "number": 10010,
          "options": {}
        },
        {
          "name": "SCOPE_THEMES",
          "number": 332,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_ACKNOWLEDGEMENTS_MANAGE",
          "number": 333,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_AGE_ASSURANCE_MANAGE",
          "number": 346,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_CONSENT_MANAGE",
          "number": 334,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_MEMBERSHIP_READ",
          "number": 335,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_PROFILE_MANAGE",
          "number": 336,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_SETTINGS_READ",
          "number": 337,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_SETTINGS_WRITE",
          "number": 338,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_TRACKING_READ",
          "number": 339,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_TRACKING_WRITE",
          "number": 340,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_READ",
          "number": 341,
          "options": {}
        },
        {
          "name": "SCOPE_USERS_SEARCH",
          "number": 342,
          "options": {}
        },
        {
          "name": "SCOPE_VIDEOS_WRITE",
          "number": 343,
          "options": {}
        },
        {
          "name": "SCOPE_VISION",
          "number": 344,
          "options": {}
        },
        {
          "name": "SCOPE_WORKFLOWS_INCENTIVES_READ",
          "number": 345,
          "options": {}
        },
        {
          "name": "SCOPE_ADMIN_FAIRPLAY",
          "number": 20000,
          "options": {}
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 83650.

```text
hbWVzEiEuZ29vZ2xlLnByb3RvYnVmLkVudW1WYWx1ZU9wdGlvbnMY4McFIAMoCVIQc2NvcGVMZWdhY3lOYW1lc2IGcHJvdG8z","chesscom/oauth/v1/scope.proto":"Ch1jaGVzc2NvbS9vYXV0aC92MS9zY29wZS5wcm90bxIRY2hlc3Njb20ub2F1dGgudjEqhSMKBVNjb3BlEhUKEVNDT1BFX1VOU1BFQ0lGSUVEEAASPQoMU0NPUEVfUFVCTElDEAEaK+K9LAZwdWJsaWPqvSwdQWNjZXNzIHdpdGhvdXQgYXV0aGVudGljYXRpb24SGAoKU0NPUEVfTk9ORRACGgjivSwEbm9uZRI5CgtTQ09QRV9DSEVTUxBkGijivSwGY2hlc3Mu6r0sGlVzZSBhbGwgQ2hl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17506"></a>
## FND-17506: Full frontend descriptor: chesscom/proto_options/api/v1/api_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/api/v1/api_options.proto",
  "package": "chesscom.proto_options.api.v1",
  "message_type": [
    {
      "name": "ApiNoAuth"
    },
    {
      "name": "ApiSecurityBasicAuth"
    },
    {
      "name": "ApiSecurityBearerAuth"
    },
    {
      "name": "ApiSecurityApiKeyAuth",
      "field": [
        {
          "name": "header",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "cookie",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "oneof_decl": [
        {
          "name": "_header"
        },
        {
          "name": "_cookie"
        }
      ]
    },
    {
      "name": "ApiAuthenticationDefinition",
      "field": [
        {
          "name": "no_auth",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiNoAuth",
          "oneof_index": 0
        },
        {
          "name": "basic_auth",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiSecurityBasicAuth",
          "oneof_index": 0
        },
        {
          "name": "bearer_auth",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiSecurityBearerAuth",
          "oneof_index": 0
        },
        {
          "name": "api_key_auth",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiSecurityApiKeyAuth",
          "oneof_index": 0
        },
        {
          "name": "description",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "oneof_decl": [
        {
          "name": "auth"
        }
      ]
    },
    {
      "name": "ApiAuthenticationOption",
      "field": [
        {
          "name": "definition",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiAuthenticationDefinition"
        },
        {
          "name": "reference",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "ApiServerDefinition",
      "field": [
        {
          "name": "url",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "description",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "authentication",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiAuthenticationOption"
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "_description"
        }
      ]
    },
    {
      "name": "ApiServerOption",
      "field": [
        {
          "name": "definition",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiServerDefinition",
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "reference",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING",
          "options": {
            "deprecated": true
          }
        }
      ],
      "options": {
        "deprecated": true
      }
    },
    {
      "name": "ApiServiceMetadata",
      "field": [
        {
          "name": "is_platform_service",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "is_mcp_service",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ]
    },
    {
      "name": "ApiOptions",
      "field": [
        {
          "name": "prefix",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "server",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiServerOption",
          "options": {
            "deprecated": true
          },
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "authentication",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiAuthenticationOption"
        },
        {
          "name": "metadata",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.api.v1.ApiServiceMetadata",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "scope",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.oauth.v1.Scope"
        },
        {
          "name": "protocol",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.api.v1.RpcProtocol"
        }
      ],
      "oneof_decl": [
        {
          "name": "_prefix"
        },
        {
          "name": "_server"
        },
        {
          "name": "_metadata"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "RpcProtocol",
      "value": [
        {
          "name": "RPC_PROTOCOL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RPC_PROTOCOL_TWIRP",
          "number": 1
        },
        {
          "name": "RPC_PROTOCOL_CONNECT",
          "number": 2
        }
      ]
    }
  ],
  "extension": [
    {
      "name": "service_options",
      "extendee": ".google.protobuf.ServiceOptions",
      "number": 91000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.api.v1.ApiOptions",
      "json_name": "serviceOptions",
      "proto3_optional": true
    },
    {
      "name": "file_options",
      "extendee": ".google.protobuf.FileOptions",
      "number": 91001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.api.v1.ApiOptions",
      "json_name": "fileOptions",
      "proto3_optional": true
    },
    {
      "name": "package_options",
      "extendee": ".google.protobuf.FileOptions",
      "number": 91002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.api.v1.ApiOptions",
      "json_name": "packageOptions",
      "proto3_optional": true
    },
    {
      "name": "scope",
      "extendee": ".google.protobuf.MethodOptions",
      "number": 91003,
      "label": "LABEL_REPEATED",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.oauth.v1.Scope",
      "json_name": "scope"
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 89747.

```text
Sw2TWFuYWdlIEZhaXJQbGF5IHNjcmVlbmVyIGNvbmZpZ3MgYW5kIGluZ2VzdGlvbiBzb3VyY2Vz8L0sA/i9LAJiBnByb3RvMw","chesscom/proto_options/api/v1/api_options.proto":"Ci9jaGVzc2NvbS9wcm90b19vcHRpb25zL2FwaS92MS9hcGlfb3B0aW9ucy5wcm90bxIdY2hlc3Njb20ucHJvdG9fb3B0aW9ucy5hcGkudjEiCwoJQXBpTm9BdXRoIhYKFEFwaVNlY3VyaXR5QmFzaWNBdXRoIhcKFUFwaVNlY3VyaXR5QmVhcmVyQXV0aCJXChVBcGlTZWN1cml0eUFwaUtleUF1dGgSEwoGaGVhZGVyGAEgASgJSACIAQESEwoGY29va2llGAIgAS
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17507"></a>
## FND-17507: Full frontend descriptor: chesscom/game_gateway/v2/player.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/player.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "Player",
      "field": [
        {
          "name": "type",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerType"
        },
        {
          "name": "provider",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerProvider"
        },
        {
          "name": "key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "final_rating",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "result",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerResult"
        },
        {
          "name": "client",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "rating_diff",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "dw_incident_logged",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "bad_sport_behavior",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerBadSportBehavior",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "display_name",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "title",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.PlayerTitle"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_client"
        },
        {
          "name": "_rating_diff"
        },
        {
          "name": "_dw_incident_logged"
        },
        {
          "name": "_bad_sport_behavior"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 92479.

```text
UucHJvdG9idWYuTWV0aG9kT3B0aW9ucxj7xgUgAygOMhguY2hlc3Njb20ub2F1dGgudjEuU2NvcGVSBXNjb3BlYgZwcm90bzM","chesscom/game_gateway/v2/player.proto":"CiVjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvcGxheWVyLnByb3RvEhhjaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIilQQKBlBsYXllchIyCgR0eXBlGAEgASgOMiQuY2hlc3Njb20uZ2FtZV9zdG9yYWdlLnYyLlBsYXllclR5cGUSOgoIcHJvdmlkZXIYAiABKA4yKC5jaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIuUGxheWVyUHJvdmlkZXISCwoDa2V5GAMgASgJEhQKDGZpbmFs
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17508"></a>
## FND-17508: Full frontend descriptor: chesscom/game_gateway/v2/chess_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/chess_game.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "ChessGame",
      "field": [
        {
          "name": "initial_fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "final_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ply_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "move_text",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_timestamps",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "white_player",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.Player"
        },
        {
          "name": "black_player",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.Player"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_initial_fen"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 93334.

```text
lbnRCDgoMX3JhdGluZ19kaWZmQhUKE19kd19pbmNpZGVudF9sb2dnZWRCFQoTX2JhZF9zcG9ydF9iZWhhdmlvcmIGcHJvdG8z","chesscom/game_gateway/v2/chess_game.proto":"CiljaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvY2hlc3NfZ2FtZS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYyIoECCglDaGVzc0dhbWUSGAoLaW5pdGlhbF9mZW4YASABKAlIAIgBARIRCglmaW5hbF9mZW4YAiABKAkSEQoJcGx5X2NvdW50GAMgASgNEhEKCW1vdmVfdGV4dBgEIAEoCRIXCg9tb3ZlX3RpbWVzdGFtcHMYBSADKA0SNgoMd2hpdGVfcGxheWVy
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17509"></a>
## FND-17509: Full frontend descriptor: chesscom/game_gateway/v2/bughouse_game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/bughouse_game.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "BughouseGame",
      "field": [
        {
          "name": "first_board",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.ChessGame"
        },
        {
          "name": "second_game_key",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 93831.

```text
yABKAsyIC5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuUGxheWVyOgiCph0ECgIBAkIOCgxfaW5pdGlhbF9mZW5iBnByb3RvMw","chesscom/game_gateway/v2/bughouse_game.proto":"CixjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvYnVnaG91c2VfZ2FtZS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYyImsKDEJ1Z2hvdXNlR2FtZRI4CgtmaXJzdF9ib2FyZBgBIAEoCzIjLmNoZXNzY29tLmdhbWVfZ2F0ZXdheS52Mi5DaGVzc0dhbWUSFwoPc2Vjb25kX2dhbWVfa2V5GAIgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_gate
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17510"></a>
## FND-17510: Full frontend descriptor: chesscom/game_gateway/v2/game.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_gateway/v2/game.proto",
  "package": "chesscom.game_gateway.v2",
  "message_type": [
    {
      "name": "Game",
      "field": [
        {
          "name": "key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "provider",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameProvider"
        },
        {
          "name": "created_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "started_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "ended_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "time_control",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.chess.v1.TimeControl"
        },
        {
          "name": "time_class",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.TimeClass"
        },
        {
          "name": "rating_class",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.RatingClass"
        },
        {
          "name": "variant",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.chess.v1.Variant"
        },
        {
          "name": "result",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameResult"
        },
        {
          "name": "privacy",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GamePrivacy"
        },
        {
          "name": "origin",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameOrigin"
        },
        {
          "name": "game_server",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v2.GameServer"
        },
        {
          "name": "special_game_event",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v2.SpecialGameEvent",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "tournament_data",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v2.TournamentData"
        },
        {
          "name": "chess_game",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.ChessGame",
          "oneof_index": 0
        },
        {
          "name": "bughouse_game",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_gateway.v2.BughouseGame",
          "oneof_index": 0
        },
        {
          "name": "legacy_id",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "vs_computer_game_data",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v2.VsComputerGameData",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "rematch_of",
          "number": 21,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "opening_data",
          "number": 22,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v2.OpeningData"
        },
        {
          "name": "vs_coach_game_data",
          "number": 23,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v2.VsCoachGameData",
          "oneof_index": 6,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "game"
        },
        {
          "name": "_name"
        },
        {
          "name": "_special_game_event"
        },
        {
          "name": "_legacy_id"
        },
        {
          "name": "_vs_computer_game_data"
        },
        {
          "name": "_rematch_of"
        },
        {
          "name": "_vs_coach_game_data"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 94133.

```text
zY29tLmdhbWVfZ2F0ZXdheS52Mi5DaGVzc0dhbWUSFwoPc2Vjb25kX2dhbWVfa2V5GAIgASgJOgiCph0ECgIBAmIGcHJvdG8z","chesscom/game_gateway/v2/game.proto":"CiNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZS5wcm90bxIYY2hlc3Njb20uZ2FtZV9nYXRld2F5LnYyIrcKCgRHYW1lEgsKA2tleRgBIAEoCRIRCgRuYW1lGAIgASgJSAGIAQESOAoIcHJvdmlkZXIYAyABKA4yJi5jaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjIuR2FtZVByb3ZpZGVyEi4KCmNyZWF0ZWRfYXQYBCABKAsyGi5nb29nbGUucHJvdG9idWYuVGltZXN0YW1wEi
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17511"></a>
## FND-17511: Full frontend descriptor: chesscom/proto_options/events/v1/event_options.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/proto_options/events/v1/event_options.proto",
  "package": "chesscom.proto_options.events.v1",
  "message_type": [
    {
      "name": "EventDefinition",
      "field": [
        {
          "name": "name",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "category",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.EventCategory",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.EventType",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "funnel",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.proto_options.events.v1.Funnel",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "interface_name",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "element_name",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "v1_event_name",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "static_properties",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.proto_options.events.v1.EventDefinition.StaticPropertiesEntry"
        },
        {
          "name": "experiment_key_field",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "nested_type": [
        {
          "name": "StaticPropertiesEntry",
          "field": [
            {
              "name": "key",
              "number": 1,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_STRING"
            },
            {
              "name": "value",
              "number": 2,
              "label": "LABEL_OPTIONAL",
              "type": "TYPE_MESSAGE",
              "type_name": ".google.protobuf.Value"
            }
          ],
          "options": {
            "map_entry": true
          }
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_name"
        },
        {
          "name": "_category"
        },
        {
          "name": "_type"
        },
        {
          "name": "_funnel"
        },
        {
          "name": "_interface_name"
        },
        {
          "name": "_element_name"
        },
        {
          "name": "_v1_event_name"
        },
        {
          "name": "_experiment_key_field"
        }
      ]
    },
    {
      "name": "ContextExtensionDefinition",
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "EventCategory",
      "value": [
        {
          "name": "EVENT_CATEGORY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EVENT_CATEGORY_IMPRESSION",
          "number": 1
        },
        {
          "name": "EVENT_CATEGORY_USER_ACTION",
          "number": 2
        },
        {
          "name": "EVENT_CATEGORY_SERVER_ACTION",
          "number": 3
        },
        {
          "name": "EVENT_CATEGORY_LOG",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "EventType",
      "value": [
        {
          "name": "EVENT_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "EVENT_TYPE_IMPRESSION",
          "number": 1
        },
        {
          "name": "EVENT_TYPE_INTERFACE_OPENED",
          "number": 2
        },
        {
          "name": "EVENT_TYPE_INTERFACE_CLOSED",
          "number": 3
        },
        {
          "name": "EVENT_TYPE_BUTTON_CLICK",
          "number": 4
        },
        {
          "name": "EVENT_TYPE_TEXT_ENTRY",
          "number": 5
        },
        {
          "name": "EVENT_TYPE_MODAL_OPENED",
          "number": 6
        },
        {
          "name": "EVENT_TYPE_NOTIFICATION_SENT",
          "number": 7
        },
        {
          "name": "EVENT_TYPE_LINK_CLICKED",
          "number": 8
        },
        {
          "name": "EVENT_TYPE_NOTIFICATION_OPENED",
          "number": 9
        },
        {
          "name": "EVENT_TYPE_GAME_ACTION",
          "number": 10
        },
        {
          "name": "EVENT_TYPE_USER_STATUS_SYSTEM_ACTION",
          "number": 11
        },
        {
          "name": "EVENT_TYPE_MODAL_CLOSED",
          "number": 12
        },
        {
          "name": "EVENT_TYPE_SOCIAL_ACTION",
          "number": 13
        },
        {
          "name": "EVENT_TYPE_NOTIFICATION_CLICKED",
          "number": 14
        },
        {
          "name": "EVENT_TYPE_UNSUBSCRIBED",
          "number": 15
        },
        {
          "name": "EVENT_TYPE_NOTIFICATION_DELIVERED",
          "number": 16
        }
      ],
      "options": {}
    },
    {
      "name": "Funnel",
      "value": [
        {
          "name": "FUNNEL_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FUNNEL_RECOMMENDED_MATCH",
          "number": 1
        },
        {
          "name": "FUNNEL_SIGNUP",
          "number": 2
        },
        {
          "name": "FUNNEL_GAME_CREATE",
          "number": 3
        },
        {
          "name": "FUNNEL_GAME_REVIEW",
          "number": 4
        },
        {
          "name": "FUNNEL_PUZZLES",
          "number": 5
        },
        {
          "name": "FUNNEL_FRIENDS",
          "number": 6
        },
        {
          "name": "FUNNEL_HOME",
          "number": 7
        },
        {
          "name": "FUNNEL_GAME_ARCHIVE",
          "number": 8
        },
        {
          "name": "FUNNEL_PROFILE",
          "number": 9
        },
        {
          "name": "FUNNEL_GAMEPLAY",
          "number": 10
        },
        {
          "name": "FUNNEL_CRM",
          "number": 11
        },
        {
          "name": "FUNNEL_PLAY_COACH",
          "number": 12
        },
        {
          "name": "FUNNEL_CONTACTS",
          "number": 13
        },
        {
          "name": "FUNNEL_LESSONS",
          "number": 14
        },
        {
          "name": "FUNNEL_COURSES",
          "number": 15
        },
        {
          "name": "FUNNEL_LOGIN",
          "number": 16
        },
        {
          "name": "FUNNEL_BOTS",
          "number": 17
        },
        {
          "name": "FUNNEL_PAYMENTS",
          "number": 18
        },
        {
          "name": "FUNNEL_CHALLENGES",
          "number": 19
        },
        {
          "name": "FUNNEL_USER",
          "number": 20
        },
        {
          "name": "FUNNEL_ADD_PHONE_NUMBER",
          "number": 21
        },
        {
          "name": "FUNNEL_SETTINGS",
          "number": 22
        },
        {
          "name": "FUNNEL_DOWNLOAD_MOBILE_APP",
          "number": 23
        },
        {
          "name": "FUNNEL_MESSAGE",
          "number": 24
        },
        {
          "name": "FUNNEL_SOCIAL",
          "number": 25
        },
        {
          "name": "FUNNEL_STREAKS",
          "number": 26
        },
        {
          "name": "FUNNEL_ONBOARDING",
          "number": 27
        },
        {
          "name": "FUNNEL_MONETIZATION",
          "number": 28
        },
        {
          "name": "FUNNEL_INDEX",
          "number": 29
        },
        {
          "name": "FUNNEL_CHAT",
          "number": 30
        },
        {
          "name": "FUNNEL_COACH",
          "number": 31
        },
        {
          "name": "FUNNEL_SHARE",
          "number": 32
        },
        {
          "name": "FUNNEL_DAILY_PUZZLE",
          "number": 33
        },
        {
          "name": "FUNNEL_NOTIFICATIONS",
          "number": 34
        },
        {
          "name": "FUNNEL_CLUBS",
          "number": 35
        },
        {
          "name": "FUNNEL_PUZZLE_RUSH",
          "number": 36
        },
        {
          "name": "FUNNEL_PUZZLE_BATTLE",
          "number": 37
        },
        {
          "name": "FUNNEL_CUSTOM_PUZZLES",
          "number": 38
        },
        {
          "name": "FUNNEL_AWARDS",
          "number": 39
        },
        {
          "name": "FUNNEL_UNOCKABLES",
          "number": 40,
          "options": {
            "deprecated": true
          }
        },
        {
          "name": "FUNNEL_EVENTS",
          "number": 41
        },
        {
          "name": "FUNNEL_STATS",
          "number": 42
        },
        {
          "name": "FUNNEL_ACTIVITY_FEED",
          "number": 43
        },
        {
          "name": "FUNNEL_TRAINABLE",
          "number": 44
        },
        {
          "name": "FUNNEL_ANALYSIS",
          "number": 45
        },
        {
          "name": "FUNNEL_YEAR_IN_CHESS",
          "number": 46
        },
        {
          "name": "FUNNEL_UNLOCKABLES",
          "number": 47
        },
        {
          "name": "FUNNEL_SOCIAL_PLATFORMS",
          "number": 48
        },
        {
          "name": "FUNNEL_TRAIN",
          "number": 49
        }
      ],
      "options": {}
    }
  ],
  "extension": [
    {
      "name": "event_definition",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 51000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.events.v1.EventDefinition",
      "json_name": "eventDefinition",
      "proto3_optional": true
    },
    {
      "name": "context_extension",
      "extendee": ".google.protobuf.MessageOptions",
      "number": 51002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_MESSAGE",
      "type_name": ".chesscom.proto_options.events.v1.ContextExtensionDefinition",
      "json_name": "contextExtension",
      "proto3_optional": true
    },
    {
      "name": "funnel",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 51000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_ENUM",
      "type_name": ".chesscom.proto_options.events.v1.Funnel",
      "json_name": "funnel",
      "proto3_optional": true
    },
    {
      "name": "rename",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 51001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "rename",
      "proto3_optional": true
    },
    {
      "name": "amplitude_value",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 51002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "options": {
        "deprecated": true
      },
      "json_name": "amplitudeValue",
      "proto3_optional": true
    },
    {
      "name": "value",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 51003,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "value",
      "proto3_optional": true
    },
    {
      "name": "v1_enum_value",
      "extendee": ".google.protobuf.EnumValueOptions",
      "number": 51004,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_INT32",
      "json_name": "v1EnumValue",
      "proto3_optional": true
    },
    {
      "name": "interface",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 51000,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "json_name": "interface",
      "proto3_optional": true
    },
    {
      "name": "element",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 51001,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "json_name": "element",
      "proto3_optional": true
    },
    {
      "name": "name",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 51002,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "name",
      "proto3_optional": true
    },
    {
      "name": "set_user_property",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 51003,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_BOOL",
      "json_name": "setUserProperty",
      "proto3_optional": true
    },
    {
      "name": "user_property_name",
      "extendee": ".google.protobuf.FieldOptions",
      "number": 51004,
      "label": "LABEL_OPTIONAL",
      "type": "TYPE_STRING",
      "json_name": "userPropertyName",
      "proto3_optional": true
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 96053.

```text
RCGAoWX3ZzX2NvbXB1dGVyX2dhbWVfZGF0YUINCgtfcmVtYXRjaF9vZkIVChNfdnNfY29hY2hfZ2FtZV9kYXRhYgZwcm90bzM","chesscom/proto_options/events/v1/event_options.proto":"CjRjaGVzc2NvbS9wcm90b19vcHRpb25zL2V2ZW50cy92MS9ldmVudF9vcHRpb25zLnByb3RvEiBjaGVzc2NvbS5wcm90b19vcHRpb25zLmV2ZW50cy52MSKZBQoPRXZlbnREZWZpbml0aW9uEhEKBG5hbWUYASABKAlIAIgBARJGCghjYXRlZ29yeRgCIAEoDjIvLmNoZXNzY29tLnByb3RvX29wdGlvbnMuZXZlbnRzLnYxLkV2ZW50Q2F0ZWdvcnlIAYgBA
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17512"></a>
## FND-17512: Full frontend descriptor: chesscom/bots/v1/bot_metadata.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/bots/v1/bot_metadata.proto",
  "package": "chesscom.bots.v1",
  "message_type": [
    {
      "name": "BotMetadata",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "rating_text",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "theme_uuid",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "image_url",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_theme_uuid"
        }
      ]
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 101045.

```text
25hbWUSHS5nb29nbGUucHJvdG9idWYuRmllbGRPcHRpb25zGLyOAyABKAlSEHVzZXJQcm9wZXJ0eU5hbWWIAQFiBnByb3RvMw","chesscom/bots/v1/bot_metadata.proto":"CiNjaGVzc2NvbS9ib3RzL3YxL2JvdF9tZXRhZGF0YS5wcm90bxIQY2hlc3Njb20uYm90cy52MSKBAQoLQm90TWV0YWRhdGESCgoCaWQYASABKAkSDAoEbmFtZRgCIAEoCRITCgtyYXRpbmdfdGV4dBgDIAEoCRIXCgp0aGVtZV91dWlkGAQgASgJSACIAQESEQoJaW1hZ2VfdXJsGAUgASgJOgiCph0ECgIBAkINCgtfdGhlbWVfdXVpZGIGcHJvdG8z","chesscom/coaches/v2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17513"></a>
## FND-17513: Full frontend descriptor: chesscom/coaches/v2/model.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/coaches/v2/model.proto",
  "package": "chesscom.coaches.v2",
  "message_type": [
    {
      "name": "Coach",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "titled_name",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "image_url",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "voice_id",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "description",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "country",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Country"
        },
        {
          "name": "locale",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "text_id",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "analytics_id",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "icon_url",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "taglines",
          "number": 12,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.api.v1.Speech"
        },
        {
          "name": "i18n_meta",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.CoachI18nMetadata"
        },
        {
          "name": "is_celebrity",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "rive_animation_url",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "greeting_rive_animation_url",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "has_visemes",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_voice_id"
        },
        {
          "name": "_rive_animation_url"
        },
        {
          "name": "_greeting_rive_animation_url"
        },
        {
          "name": "_has_visemes"
        }
      ]
    },
    {
      "name": "CoachI18nMetadata",
      "field": [
        {
          "name": "language_indicator",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_language_indicator"
        }
      ]
    },
    {
      "name": "CoachCategory",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "name",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "coaches",
          "number": 3,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.coaches.v2.Coach"
        }
      ],
      "options": {}
    },
    {
      "name": "SpeechString",
      "field": [
        {
          "name": "text",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "audio_hash",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {}
    },
    {
      "name": "PlayCoachAssistanceSettingsSnapshot",
      "field": [
        {
          "name": "suggestion_arrows",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "threat_arrows",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "evaluation_bar",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "move_feedback",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        },
        {
          "name": "auto_hints",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_BOOL"
        }
      ],
      "options": {}
    },
    {
      "name": "FinishVsCoachContext",
      "field": [
        {
          "name": "source",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.coaches.v2.FinishVsCoachSource",
          "options": {}
        },
        {
          "name": "original_game_id",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        },
        {
          "name": "original_game_type",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "options": {}
        }
      ],
      "options": {}
    }
  ],
  "enum_type": [
    {
      "name": "CoachVoiceSpeed",
      "value": [
        {
          "name": "COACH_VOICE_SPEED_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_VOICE_SPEED_NORMAL",
          "number": 1
        },
        {
          "name": "COACH_VOICE_SPEED_1_25_TIMES",
          "number": 2
        },
        {
          "name": "COACH_VOICE_SPEED_1_50_TIMES",
          "number": 3
        },
        {
          "name": "COACH_VOICE_SPEED_2_TIMES",
          "number": 4
        }
      ],
      "options": {}
    },
    {
      "name": "CoachContext",
      "value": [
        {
          "name": "COACH_CONTEXT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_CONTEXT_HOME",
          "number": 1
        },
        {
          "name": "COACH_CONTEXT_LEARN",
          "number": 2
        }
      ],
      "options": {}
    },
    {
      "name": "CoachSpeechType",
      "value": [
        {
          "name": "COACH_SPEECH_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "COACH_SPEECH_TYPE_WELCOME",
          "number": 1
        },
        {
          "name": "COACH_SPEECH_TYPE_MOTIVATIONAL",
          "number": 2
        }
      ]
    },
    {
      "name": "FinishVsCoachSource",
      "value": [
        {
          "name": "FINISH_VS_COACH_SOURCE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "FINISH_VS_COACH_SOURCE_GAME",
          "number": 1
        },
        {
          "name": "FINISH_VS_COACH_SOURCE_ANALYSIS",
          "number": 2
        },
        {
          "name": "FINISH_VS_COACH_SOURCE_GAME_REVIEW",
          "number": 3
        }
      ],
      "options": {}
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 101346.

```text
0aGVtZV91dWlkGAQgASgJSACIAQESEQoJaW1hZ2VfdXJsGAUgASgJOgiCph0ECgIBAkINCgtfdGhlbWVfdXVpZGIGcHJvdG8z","chesscom/coaches/v2/model.proto":"Ch9jaGVzc2NvbS9jb2FjaGVzL3YyL21vZGVsLnByb3RvEhNjaGVzc2NvbS5jb2FjaGVzLnYyIqgECgVDb2FjaBIKCgJpZBgBIAEoCRIMCgRuYW1lGAIgASgJEhMKC3RpdGxlZF9uYW1lGAMgASgJEhEKCWltYWdlX3VybBgEIAEoCRIVCgh2b2ljZV9pZBgFIAEoCUgAiAEBEhMKC2Rlc2NyaXB0aW9uGAYgASgJEikKB2NvdW50cnkYByABKAsyGC5jaGVzc2NvbS5hcGkudjEuQ291bn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.

<a id="FND-17514"></a>
## FND-17514: Full frontend descriptor: chesscom/game_storage/v1/game_stored.proto

**Category:** authoritative_frontend_descriptors  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "name": "chesscom/game_storage/v1/game_stored.proto",
  "package": "chesscom.game_storage.v1",
  "message_type": [
    {
      "name": "GameStored",
      "field": [
        {
          "name": "internal_key",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "provider",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.GameProvider"
        },
        {
          "name": "key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "created_at",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "started_at",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "ended_at",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".google.protobuf.Timestamp"
        },
        {
          "name": "time_control",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "per_player_time_controls",
          "number": 8,
          "label": "LABEL_REPEATED",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.PerPlayerTimeControl"
        },
        {
          "name": "time_class",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.TimeClass"
        },
        {
          "name": "rating_class",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.RatingClass"
        },
        {
          "name": "variant",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.Variant"
        },
        {
          "name": "result",
          "number": 12,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.GameResult"
        },
        {
          "name": "privacy",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.GamePrivacy"
        },
        {
          "name": "origin",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.GameOrigin"
        },
        {
          "name": "chess_com_tournament_identifier",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.tdtools.v1.ChessComTournamentIdentifier"
        },
        {
          "name": "tags",
          "number": 16,
          "label": "LABEL_REPEATED",
          "type": "TYPE_STRING"
        },
        {
          "name": "chess_game",
          "number": 30,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.ChessGame",
          "oneof_index": 0
        },
        {
          "name": "bughouse_game",
          "number": 31,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.BughouseGame",
          "oneof_index": 0
        },
        {
          "name": "variant_game",
          "number": 32,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.VariantGame",
          "oneof_index": 0
        },
        {
          "name": "legacy_id",
          "number": 33,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "vs_computer_game_mode",
          "number": 34,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.VsComputerGameMode",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "vs_coach_game_data",
          "number": 35,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.VsCoachGameData",
          "oneof_index": 3,
          "proto3_optional": true
        }
      ],
      "options": {
        "deprecated": true
      },
      "oneof_decl": [
        {
          "name": "game"
        },
        {
          "name": "_legacy_id"
        },
        {
          "name": "_vs_computer_game_mode"
        },
        {
          "name": "_vs_coach_game_data"
        }
      ],
      "reserved_range": [
        {
          "start": 17,
          "end": 30
        }
      ]
    },
    {
      "name": "ChessGame",
      "field": [
        {
          "name": "initial_fen",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "final_fen",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ply_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "move_text",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_timestamps",
          "number": 5,
          "label": "LABEL_REPEATED",
          "type": "TYPE_UINT32"
        },
        {
          "name": "white_player",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        },
        {
          "name": "black_player",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        },
        {
          "name": "master_chess_game_data",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.MasterChessGameData",
          "oneof_index": 1,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_initial_fen"
        },
        {
          "name": "_master_chess_game_data"
        }
      ]
    },
    {
      "name": "BughouseGame",
      "field": [
        {
          "name": "first_board",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.ChessGame"
        },
        {
          "name": "second_game_key",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "reserved_range": [
        {
          "start": 2,
          "end": 3
        }
      ]
    },
    {
      "name": "VariantGame",
      "field": [
        {
          "name": "initial_fen4",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "end_fen4",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "ply_count",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "pgn4",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "board_dimension",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.VariantGame.VariantType"
        },
        {
          "name": "rating_type",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "player_1",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        },
        {
          "name": "player_2",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        },
        {
          "name": "player_3",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        },
        {
          "name": "player_4",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.Player"
        }
      ],
      "enum_type": [
        {
          "name": "VariantType",
          "value": [
            {
              "name": "VARIANT_TYPE_UNSPECIFIED",
              "number": 0
            },
            {
              "name": "VARIANT_TYPE_FREE_FOR_ALL",
              "number": 1
            },
            {
              "name": "VARIANT_TYPE_TEAMS",
              "number": 2
            },
            {
              "name": "VARIANT_TYPE_SOLO",
              "number": 3
            }
          ]
        }
      ]
    },
    {
      "name": "PerPlayerTimeControl",
      "field": [
        {
          "name": "player_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "time_control",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    },
    {
      "name": "Player",
      "field": [
        {
          "name": "id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "type",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.PlayerType"
        },
        {
          "name": "provider",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.PlayerProvider"
        },
        {
          "name": "key",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_handle",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "display_name",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "title",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.PlayerTitle"
        },
        {
          "name": "country",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "final_rating",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "result",
          "number": 10,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.PlayerResult"
        },
        {
          "name": "place",
          "number": 11,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32"
        },
        {
          "name": "client",
          "number": 13,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "points",
          "number": 14,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "initial_rating",
          "number": 15,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 2,
          "proto3_optional": true
        },
        {
          "name": "rating_diff",
          "number": 16,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_FLOAT",
          "oneof_index": 3,
          "proto3_optional": true
        },
        {
          "name": "fide_id",
          "number": 17,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT64",
          "oneof_index": 4,
          "proto3_optional": true
        },
        {
          "name": "min_rating",
          "number": 18,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 5,
          "proto3_optional": true
        },
        {
          "name": "dw_incident_logged",
          "number": 19,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_UINT32",
          "oneof_index": 6,
          "proto3_optional": true
        },
        {
          "name": "bad_sport_behavior",
          "number": 20,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.PlayerBadSportBehavior",
          "oneof_index": 7,
          "proto3_optional": true
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_client"
        },
        {
          "name": "_points"
        },
        {
          "name": "_initial_rating"
        },
        {
          "name": "_rating_diff"
        },
        {
          "name": "_fide_id"
        },
        {
          "name": "_min_rating"
        },
        {
          "name": "_dw_incident_logged"
        },
        {
          "name": "_bad_sport_behavior"
        }
      ],
      "reserved_range": [
        {
          "start": 12,
          "end": 13
        }
      ]
    },
    {
      "name": "MasterChessGameData",
      "field": [
        {
          "name": "pgn",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "event",
          "number": 2,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "site",
          "number": 3,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "date",
          "number": 4,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "round",
          "number": 5,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "move_text",
          "number": 6,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        },
        {
          "name": "final_fen3",
          "number": 7,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 0,
          "proto3_optional": true
        },
        {
          "name": "final_fen6",
          "number": 8,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING",
          "oneof_index": 1,
          "proto3_optional": true
        },
        {
          "name": "time_control",
          "number": 9,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ],
      "options": {},
      "oneof_decl": [
        {
          "name": "_final_fen3"
        },
        {
          "name": "_final_fen6"
        }
      ]
    },
    {
      "name": "PlayModeGrouping",
      "field": [
        {
          "name": "variants",
          "number": 1,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.Variant"
        },
        {
          "name": "time_classes",
          "number": 2,
          "label": "LABEL_REPEATED",
          "type": "TYPE_ENUM",
          "type_name": ".chesscom.game_storage.v1.TimeClass"
        }
      ]
    },
    {
      "name": "PlayModeGroupingOptions",
      "extension": [
        {
          "name": "grouping",
          "extendee": ".google.protobuf.EnumValueOptions",
          "number": 1001,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_MESSAGE",
          "type_name": ".chesscom.game_storage.v1.PlayModeGrouping",
          "json_name": "grouping"
        }
      ]
    },
    {
      "name": "VsCoachGameData",
      "field": [
        {
          "name": "coach_id",
          "number": 1,
          "label": "LABEL_OPTIONAL",
          "type": "TYPE_STRING"
        }
      ]
    }
  ],
  "enum_type": [
    {
      "name": "GameProvider",
      "value": [
        {
          "name": "GAME_PROVIDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PROVIDER_CHESS_COM",
          "number": 1
        },
        {
          "name": "GAME_PROVIDER_CHESS_KID",
          "number": 2
        },
        {
          "name": "GAME_PROVIDER_FIDE",
          "number": 3
        },
        {
          "name": "GAME_PROVIDER_LICHESS",
          "number": 4
        },
        {
          "name": "GAME_PROVIDER_CHESSBASE",
          "number": 5
        },
        {
          "name": "GAME_PROVIDER_OFFLINE",
          "number": 6
        },
        {
          "name": "GAME_PROVIDER_CHESS_COM_MASTER_GAMES",
          "number": 7
        }
      ]
    },
    {
      "name": "GameOrigin",
      "value": [
        {
          "name": "GAME_ORIGIN_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_ORIGIN_DIRECT_CHALLENGE",
          "number": 1
        },
        {
          "name": "GAME_ORIGIN_SEEK",
          "number": 2
        },
        {
          "name": "GAME_ORIGIN_POOL_SEEK",
          "number": 3
        },
        {
          "name": "GAME_ORIGIN_START_GAME",
          "number": 4
        },
        {
          "name": "GAME_ORIGIN_MATCH",
          "number": 5
        },
        {
          "name": "GAME_ORIGIN_ARENA",
          "number": 6
        },
        {
          "name": "GAME_ORIGIN_TOURNAMENT",
          "number": 7
        },
        {
          "name": "GAME_ORIGIN_TEAM_MATCH",
          "number": 8
        },
        {
          "name": "GAME_ORIGIN_COMPETITION",
          "number": 9
        },
        {
          "name": "GAME_ORIGIN_RECOMMENDED_MATCH",
          "number": 10
        },
        {
          "name": "GAME_ORIGIN_LEAGUE",
          "number": 11
        },
        {
          "name": "GAME_ORIGIN_SIMUL",
          "number": 12
        }
      ]
    },
    {
      "name": "TimeClass",
      "value": [
        {
          "name": "TIME_CLASS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "TIME_CLASS_BULLET",
          "number": 1
        },
        {
          "name": "TIME_CLASS_BLITZ",
          "number": 2
        },
        {
          "name": "TIME_CLASS_RAPID",
          "number": 3
        },
        {
          "name": "TIME_CLASS_DAILY",
          "number": 4
        },
        {
          "name": "TIME_CLASS_HYPER",
          "number": 5
        },
        {
          "name": "TIME_CLASS_CLASSICAL",
          "number": 6
        }
      ],
      "options": {}
    },
    {
      "name": "RatingClass",
      "value": [
        {
          "name": "RATING_CLASS_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "RATING_CLASS_UNRATED",
          "number": 1
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_BULLET",
          "number": 2
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_BLITZ",
          "number": 3
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_RAPID",
          "number": 4
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_DAILY",
          "number": 5
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS960",
          "number": 6
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS960_DAILY",
          "number": 7
        },
        {
          "name": "RATING_CLASS_CHESS_COM_BUGHOUSE",
          "number": 8
        },
        {
          "name": "RATING_CLASS_CHESS_COM_KINGOFTHEHILL",
          "number": 9
        },
        {
          "name": "RATING_CLASS_CHESS_COM_THREECHECK",
          "number": 10
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CRAZYHOUSE",
          "number": 11
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_STANDARD",
          "number": 12
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_RAPID",
          "number": 13
        },
        {
          "name": "RATING_CLASS_FIDE_CHESS_BLITZ",
          "number": 14
        },
        {
          "name": "RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS",
          "number": 15
        }
      ]
    },
    {
      "name": "Variant",
      "value": [
        {
          "name": "VARIANT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "VARIANT_CHESS",
          "number": 1
        },
        {
          "name": "VARIANT_CHESS_960",
          "number": 2
        },
        {
          "name": "VARIANT_BUGHOUSE",
          "number": 4
        },
        {
          "name": "VARIANT_THREE_CHECK",
          "number": 5
        },
        {
          "name": "VARIANT_CRAZYHOUSE",
          "number": 6
        },
        {
          "name": "VARIANT_KING_OF_THE_HILL",
          "number": 7
        },
        {
          "name": "VARIANT_ODDS_CHESS",
          "number": 8
        },
        {
          "name": "VARIANT_HELP_CHESS",
          "number": 9
        }
      ],
      "options": {}
    },
    {
      "name": "GamePrivacy",
      "value": [
        {
          "name": "GAME_PRIVACY_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_PRIVACY_PUBLIC",
          "number": 1
        },
        {
          "name": "GAME_PRIVACY_PRIVATE",
          "number": 2
        }
      ]
    },
    {
      "name": "PlayerResult",
      "value": [
        {
          "name": "PLAYER_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_RESULT_WIN",
          "number": 1
        },
        {
          "name": "PLAYER_RESULT_DRAW",
          "number": 2
        },
        {
          "name": "PLAYER_RESULT_LOSE",
          "number": 3
        },
        {
          "name": "PLAYER_RESULT_ABORT",
          "number": 4
        },
        {
          "name": "PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE",
          "number": 5
        }
      ],
      "options": {}
    },
    {
      "name": "GameResult",
      "value": [
        {
          "name": "GAME_RESULT_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_TIMEOUT",
          "number": 1
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_CHECKMATE",
          "number": 2
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_RESIGNATION",
          "number": 3
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_ABANDONMENT",
          "number": 4
        },
        {
          "name": "GAME_RESULT_DRAW_BY_AGREEMENT",
          "number": 5
        },
        {
          "name": "GAME_RESULT_DRAW_BY_REPETITION",
          "number": 6
        },
        {
          "name": "GAME_RESULT_DRAW_BY_STALEMATE",
          "number": 7
        },
        {
          "name": "GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL",
          "number": 8
        },
        {
          "name": "GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL",
          "number": 9
        },
        {
          "name": "GAME_RESULT_DRAW_BY_50_MOVE_RULE",
          "number": 10
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE",
          "number": 11
        },
        {
          "name": "GAME_RESULT_ABORTED",
          "number": 12
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_THREE_CHECK",
          "number": 13
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL",
          "number": 14
        },
        {
          "name": "GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT",
          "number": 15
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerProvider",
      "value": [
        {
          "name": "PLAYER_PROVIDER_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_COM",
          "number": 1
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_KID",
          "number": 2
        },
        {
          "name": "PLAYER_PROVIDER_FIDE",
          "number": 3
        },
        {
          "name": "PLAYER_PROVIDER_LICHESS_ORG",
          "number": 4
        },
        {
          "name": "PLAYER_PROVIDER_CHESSBASE",
          "number": 5
        },
        {
          "name": "PLAYER_PROVIDER_CHESS_COM_MASTER",
          "number": 6
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerTitle",
      "value": [
        {
          "name": "PLAYER_TITLE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_TITLE_WGM",
          "number": 1
        },
        {
          "name": "PLAYER_TITLE_GM",
          "number": 2
        },
        {
          "name": "PLAYER_TITLE_WIM",
          "number": 3
        },
        {
          "name": "PLAYER_TITLE_IM",
          "number": 4
        },
        {
          "name": "PLAYER_TITLE_WFM",
          "number": 5
        },
        {
          "name": "PLAYER_TITLE_FM",
          "number": 6
        },
        {
          "name": "PLAYER_TITLE_WNM",
          "number": 7
        },
        {
          "name": "PLAYER_TITLE_NM",
          "number": 8
        },
        {
          "name": "PLAYER_TITLE_M",
          "number": 9
        },
        {
          "name": "PLAYER_TITLE_CM",
          "number": 10
        },
        {
          "name": "PLAYER_TITLE_WCM",
          "number": 11
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerType",
      "value": [
        {
          "name": "PLAYER_TYPE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_TYPE_HUMAN",
          "number": 1
        },
        {
          "name": "PLAYER_TYPE_COMPUTER",
          "number": 2
        },
        {
          "name": "PLAYER_TYPE_CYBORG",
          "number": 3
        }
      ],
      "options": {}
    },
    {
      "name": "PlayerBadSportBehavior",
      "value": [
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_NONE",
          "number": 1
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED",
          "number": 2
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_ABORT",
          "number": 3
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT",
          "number": 4
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT",
          "number": 5
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED",
          "number": 6
        },
        {
          "name": "PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED",
          "number": 7
        }
      ],
      "options": {}
    },
    {
      "name": "VsComputerGameMode",
      "value": [
        {
          "name": "VS_COMPUTER_GAME_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "VS_COMPUTER_GAME_MODE_CHALLENGE",
          "number": 1
        },
        {
          "name": "VS_COMPUTER_GAME_MODE_FRIENDLY",
          "number": 2
        },
        {
          "name": "VS_COMPUTER_GAME_MODE_ASSISTED",
          "number": 3
        },
        {
          "name": "VS_COMPUTER_GAME_MODE_CUSTOM",
          "number": 4
        }
      ]
    },
    {
      "name": "PlayMode",
      "value": [
        {
          "name": "PLAY_MODE_UNSPECIFIED",
          "number": 0
        },
        {
          "name": "PLAY_MODE_LIVE",
          "number": 1,
          "options": {}
        },
        {
          "name": "PLAY_MODE_DAILY",
          "number": 2,
          "options": {}
        },
        {
          "name": "PLAY_MODE_VS_COMPUTER",
          "number": 3,
          "options": {}
        }
      ],
      "options": {
        "deprecated": true
      }
    }
  ],
  "syntax": "proto3"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 103850.

```text
VSQ0VfQU5BTFlTSVMQAhImCiJGSU5JU0hfVlNfQ09BQ0hfU09VUkNFX0dBTUVfUkVWSUVXEAMaCIqmHQQKAgECYgZwcm90bzM","chesscom/game_storage/v1/game_stored.proto":"CipjaGVzc2NvbS9nYW1lX3N0b3JhZ2UvdjEvZ2FtZV9zdG9yZWQucHJvdG8SGGNoZXNzY29tLmdhbWVfc3RvcmFnZS52MSLZCQoKR2FtZVN0b3JlZBIUCgxpbnRlcm5hbF9rZXkYASABKAkSOAoIcHJvdmlkZXIYAiABKA4yJi5jaGVzc2NvbS5nYW1lX3N0b3JhZ2UudjEuR2FtZVByb3ZpZGVyEgsKA2tleRgDIAEoCRIuCgpjcmVhdGVkX2F0GAQgASgLMhouZ29vZ2x
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** New offline recovery from an existing source, not a new website observation. This preserves service definitions, options and exact proto3 presence beyond the older lossy rendered schema. Raw base64 remains in the redacted original registry evidence.
