# api_schema_services — findings 1–100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17517"></a>
## FND-17517: Frontend-declared RPC chesscom.coaches.v2.CoachesService/ListCoaches

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "ListCoaches",
  "input_type": ".chesscom.coaches.v2.ListCoachesRequest",
  "output_type": ".chesscom.coaches.v2.ListCoachesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17518"></a>
## FND-17518: Frontend-declared RPC chesscom.coaches.v2.CoachesService/ListOnboardingCoaches

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "ListOnboardingCoaches",
  "input_type": ".chesscom.coaches.v2.ListOnboardingCoachesRequest",
  "output_type": ".chesscom.coaches.v2.ListOnboardingCoachesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17519"></a>
## FND-17519: Frontend-declared RPC chesscom.coaches.v2.CoachesService/SetCurrentCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "SetCurrentCoach",
  "input_type": ".chesscom.coaches.v2.SetCurrentCoachRequest",
  "output_type": ".chesscom.coaches.v2.SetCurrentCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17520"></a>
## FND-17520: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetCurrentCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetCurrentCoach",
  "input_type": ".chesscom.coaches.v2.GetCurrentCoachRequest",
  "output_type": ".chesscom.coaches.v2.GetCurrentCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17521"></a>
## FND-17521: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetCoach",
  "input_type": ".chesscom.coaches.v2.GetCoachRequest",
  "output_type": ".chesscom.coaches.v2.GetCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17522"></a>
## FND-17522: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetCoaches

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetCoaches",
  "input_type": ".chesscom.coaches.v2.GetCoachesRequest",
  "output_type": ".chesscom.coaches.v2.GetCoachesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17523"></a>
## FND-17523: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetCoachQuota

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetCoachQuota",
  "input_type": ".chesscom.coaches.v2.GetCoachQuotaRequest",
  "output_type": ".chesscom.coaches.v2.GetCoachQuotaResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17524"></a>
## FND-17524: Frontend-declared RPC chesscom.coaches.v2.CoachesService/StartedGameAgainstCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "StartedGameAgainstCoach",
  "input_type": ".chesscom.coaches.v2.StartedGameAgainstCoachRequest",
  "output_type": ".chesscom.coaches.v2.StartedGameAgainstCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17525"></a>
## FND-17525: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetSettings

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetSettings",
  "input_type": ".chesscom.coaches.v2.GetSettingsRequest",
  "output_type": ".chesscom.coaches.v2.GetSettingsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17526"></a>
## FND-17526: Frontend-declared RPC chesscom.coaches.v2.CoachesService/SetSettings

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "SetSettings",
  "input_type": ".chesscom.coaches.v2.SetSettingsRequest",
  "output_type": ".chesscom.coaches.v2.SetSettingsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17527"></a>
## FND-17527: Frontend-declared RPC chesscom.coaches.v2.CoachesService/SaveCoachGame

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "SaveCoachGame",
  "input_type": ".chesscom.coaches.v2.SaveCoachGameRequest",
  "output_type": ".chesscom.coaches.v2.SaveCoachGameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17528"></a>
## FND-17528: Frontend-declared RPC chesscom.coaches.v2.CoachesService/GetCoachSpeech

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "GetCoachSpeech",
  "input_type": ".chesscom.coaches.v2.GetCoachSpeechRequest",
  "output_type": ".chesscom.coaches.v2.GetCoachSpeechResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17529"></a>
## FND-17529: Frontend-declared RPC chesscom.coaches.v2.CoachesService/HideCoachGame

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.coaches.v2.CoachesService",
  "method": "HideCoachGame",
  "input_type": ".chesscom.coaches.v2.HideCoachGameRequest",
  "output_type": ".chesscom.coaches.v2.HideCoachGameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 115551.

```text
BVFVSRV9TVUdHRVNUSU9OUxAHEiMKH0FTU0lTVEVEX0dBTUVfRkVBVFVSRV9UQUtFQkFDS1MQCBoHiqYdAwoBAWIGcHJvdG8z","chesscom/coaches/v2/service.proto":"CiFjaGVzc2NvbS9jb2FjaGVzL3YyL3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvYWNoZXMudjIikwEKEkxpc3RDb2FjaGVzUmVxdWVzdBIgCg9sb2NhbGVfb3ZlcnJpZGUYASABKAlCAhgBSACIAQESIwoWd2l0aF9jZWxlYnJpdHlfY29hY2hlcxgCIAEoCEgBiAEBOgeCph0DCgEBQhIKEF9sb2NhbGVfb3ZlcnJpZGVCGQoXX3dpdGhfY2VsZWJyaXR5X2NvYWNoZXMiXAoTTGlz
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17544"></a>
## FND-17544: Frontend-declared RPC chesscom.flair.v1.FlairInternalService/ListFlairInternal

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairInternalService",
  "method": "ListFlairInternal",
  "input_type": ".chesscom.flair.v1.ListFlairInternalRequest",
  "output_type": ".chesscom.flair.v1.ListFlairInternalResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 139509.

```text
mbGFpchgCIAEoCzIcLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyVmlld0gAiAEBOgeCph0DCgEBQggKBl9mbGFpcmIGcHJvdG8z","chesscom/flair/v1/flair_internal_service.proto":"Ci5jaGVzc2NvbS9mbGFpci92MS9mbGFpcl9pbnRlcm5hbF9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIaChhMaXN0RmxhaXJJbnRlcm5hbFJlcXVlc3QiRAoZTGlzdEZsYWlySW50ZXJuYWxSZXNwb25zZRInCgVmbGFpchgBIAMoCzIYLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyIjIKHUxpc3RGbGFpckJ5SWRzSW50ZXJuYWxSZXF1ZXN0EhEKCWZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17545"></a>
## FND-17545: Frontend-declared RPC chesscom.flair.v1.FlairInternalService/ListFlairByIdsInternal

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairInternalService",
  "method": "ListFlairByIdsInternal",
  "input_type": ".chesscom.flair.v1.ListFlairByIdsInternalRequest",
  "output_type": ".chesscom.flair.v1.ListFlairByIdsInternalResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 139509.

```text
mbGFpchgCIAEoCzIcLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyVmlld0gAiAEBOgeCph0DCgEBQggKBl9mbGFpcmIGcHJvdG8z","chesscom/flair/v1/flair_internal_service.proto":"Ci5jaGVzc2NvbS9mbGFpci92MS9mbGFpcl9pbnRlcm5hbF9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIaChhMaXN0RmxhaXJJbnRlcm5hbFJlcXVlc3QiRAoZTGlzdEZsYWlySW50ZXJuYWxSZXNwb25zZRInCgVmbGFpchgBIAMoCzIYLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyIjIKHUxpc3RGbGFpckJ5SWRzSW50ZXJuYWxSZXF1ZXN0EhEKCWZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17546"></a>
## FND-17546: Frontend-declared RPC chesscom.flair.v1.FlairInternalService/SetUserFlairInternal

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairInternalService",
  "method": "SetUserFlairInternal",
  "input_type": ".chesscom.flair.v1.SetUserFlairInternalRequest",
  "output_type": ".chesscom.flair.v1.SetUserFlairInternalResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 139509.

```text
mbGFpchgCIAEoCzIcLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyVmlld0gAiAEBOgeCph0DCgEBQggKBl9mbGFpcmIGcHJvdG8z","chesscom/flair/v1/flair_internal_service.proto":"Ci5jaGVzc2NvbS9mbGFpci92MS9mbGFpcl9pbnRlcm5hbF9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIaChhMaXN0RmxhaXJJbnRlcm5hbFJlcXVlc3QiRAoZTGlzdEZsYWlySW50ZXJuYWxSZXNwb25zZRInCgVmbGFpchgBIAMoCzIYLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyIjIKHUxpc3RGbGFpckJ5SWRzSW50ZXJuYWxSZXF1ZXN0EhEKCWZ
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17549"></a>
## FND-17549: Frontend-declared RPC chesscom.flair.v1.FlairAdminService/ListFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairAdminService",
  "method": "ListFlair",
  "input_type": ".chesscom.flair.v1.ListFlairRequest",
  "output_type": ".chesscom.flair.v1.ListFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 142295.

```text
AsyMy5jaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxLkduc0ZpZWxkT3B0aW9uc1IIZ25zRmllbGRiBnByb3RvMw","chesscom/flair/v1/flair_admin_service.proto":"CitjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9hZG1pbl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSISChBMaXN0RmxhaXJSZXF1ZXN0IjwKEUxpc3RGbGFpclJlc3BvbnNlEicKBWZsYWlyGAEgAygLMhguY2hlc3Njb20uZmxhaXIudjEuRmxhaXIiKgoVTGlzdEZsYWlyQnlJZHNSZXF1ZXN0EhEKCWZsYWlyX2lkcxgBIAMoCSJBChZMaXN0RmxhaXJCeU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17550"></a>
## FND-17550: Frontend-declared RPC chesscom.flair.v1.FlairAdminService/ListFlairByIds

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairAdminService",
  "method": "ListFlairByIds",
  "input_type": ".chesscom.flair.v1.ListFlairByIdsRequest",
  "output_type": ".chesscom.flair.v1.ListFlairByIdsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 142295.

```text
AsyMy5jaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxLkduc0ZpZWxkT3B0aW9uc1IIZ25zRmllbGRiBnByb3RvMw","chesscom/flair/v1/flair_admin_service.proto":"CitjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9hZG1pbl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSISChBMaXN0RmxhaXJSZXF1ZXN0IjwKEUxpc3RGbGFpclJlc3BvbnNlEicKBWZsYWlyGAEgAygLMhguY2hlc3Njb20uZmxhaXIudjEuRmxhaXIiKgoVTGlzdEZsYWlyQnlJZHNSZXF1ZXN0EhEKCWZsYWlyX2lkcxgBIAMoCSJBChZMaXN0RmxhaXJCeU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17551"></a>
## FND-17551: Frontend-declared RPC chesscom.flair.v1.FlairAdminService/ListFlairByNamePrefix

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairAdminService",
  "method": "ListFlairByNamePrefix",
  "input_type": ".chesscom.flair.v1.ListFlairByNamePrefixRequest",
  "output_type": ".chesscom.flair.v1.ListFlairByNamePrefixResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 142295.

```text
AsyMy5jaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxLkduc0ZpZWxkT3B0aW9uc1IIZ25zRmllbGRiBnByb3RvMw","chesscom/flair/v1/flair_admin_service.proto":"CitjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9hZG1pbl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSISChBMaXN0RmxhaXJSZXF1ZXN0IjwKEUxpc3RGbGFpclJlc3BvbnNlEicKBWZsYWlyGAEgAygLMhguY2hlc3Njb20uZmxhaXIudjEuRmxhaXIiKgoVTGlzdEZsYWlyQnlJZHNSZXF1ZXN0EhEKCWZsYWlyX2lkcxgBIAMoCSJBChZMaXN0RmxhaXJCeU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17552"></a>
## FND-17552: Frontend-declared RPC chesscom.flair.v1.FlairAdminService/SetUserFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairAdminService",
  "method": "SetUserFlair",
  "input_type": ".chesscom.flair.v1.SetUserFlairRequest",
  "output_type": ".chesscom.flair.v1.SetUserFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 142295.

```text
AsyMy5jaGVzc2NvbS5wcm90b19vcHRpb25zLm1hbmlmZXN0LnYxLkduc0ZpZWxkT3B0aW9uc1IIZ25zRmllbGRiBnByb3RvMw","chesscom/flair/v1/flair_admin_service.proto":"CitjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9hZG1pbl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSISChBMaXN0RmxhaXJSZXF1ZXN0IjwKEUxpc3RGbGFpclJlc3BvbnNlEicKBWZsYWlyGAEgAygLMhguY2hlc3Njb20uZmxhaXIudjEuRmxhaXIiKgoVTGlzdEZsYWlyQnlJZHNSZXF1ZXN0EhEKCWZsYWlyX2lkcxgBIAMoCSJBChZMaXN0RmxhaXJCeU
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17554"></a>
## FND-17554: Frontend-declared RPC chesscom.flair.v1.FlairService/ListFlairSelection

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairService",
  "method": "ListFlairSelection",
  "input_type": ".chesscom.flair.v1.ListFlairSelectionRequest",
  "output_type": ".chesscom.flair.v1.ListFlairSelectionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17555"></a>
## FND-17555: Frontend-declared RPC chesscom.flair.v1.FlairService/SelectFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairService",
  "method": "SelectFlair",
  "input_type": ".chesscom.flair.v1.SelectFlairRequest",
  "output_type": ".chesscom.flair.v1.SelectFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17556"></a>
## FND-17556: Frontend-declared RPC chesscom.flair.v1.FlairService/RemoveFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairService",
  "method": "RemoveFlair",
  "input_type": ".chesscom.flair.v1.RemoveFlairRequest",
  "output_type": ".chesscom.flair.v1.RemoveFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17557"></a>
## FND-17557: Frontend-declared RPC chesscom.flair.v1.FlairService/GetUserFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairService",
  "method": "GetUserFlair",
  "input_type": ".chesscom.flair.v1.GetUserFlairRequest",
  "output_type": ".chesscom.flair.v1.GetUserFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17558"></a>
## FND-17558: Frontend-declared RPC chesscom.flair.v1.FlairService/ListUserFlair

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.flair.v1.FlairService",
  "method": "ListUserFlair",
  "input_type": ".chesscom.flair.v1.ListUserFlairRequest",
  "output_type": ".chesscom.flair.v1.ListUserFlairResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 145830.

```text
iBuYW1lIHByZWZpeDIIY2hlc3Njb21CKMq3LCQKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoLEgl4LWFwaS1rZXliBnByb3RvMw","chesscom/flair/v1/flair_service.proto":"CiVjaGVzc2NvbS9mbGFpci92MS9mbGFpcl9zZXJ2aWNlLnByb3RvEhFjaGVzc2NvbS5mbGFpci52MSIkChlMaXN0RmxhaXJTZWxlY3Rpb25SZXF1ZXN0OgeCph0DCgEBImUKGkxpc3RGbGFpclNlbGVjdGlvblJlc3BvbnNlEj4KD2ZsYWlyX3NlbGVjdGlvbhgBIAMoCzIlLmNoZXNzY29tLmZsYWlyLnYxLkZsYWlyU2VsZWN0aW9uSXRlbToHgqYdAwoBASIvChJTZWxlY3RG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17568"></a>
## FND-17568: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/HydrateGamesByCriteria

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "HydrateGamesByCriteria",
  "input_type": ".chesscom.game_gateway.v2.HydrateGamesByCriteriaRequest",
  "output_type": ".chesscom.game_gateway.v2.HydrateGamesByCriteriaResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17569"></a>
## FND-17569: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/CountGamesByCriteria

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "CountGamesByCriteria",
  "input_type": ".chesscom.game_gateway.v2.CountGamesByCriteriaRequest",
  "output_type": ".chesscom.game_gateway.v2.CountGamesByCriteriaResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17570"></a>
## FND-17570: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/DeleteGame

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "DeleteGame",
  "input_type": ".chesscom.game_gateway.v2.DeleteGameRequest",
  "output_type": ".chesscom.game_gateway.v2.DeleteGameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17571"></a>
## FND-17571: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/AggregateGameResultsByPlayerAndCriteria

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "AggregateGameResultsByPlayerAndCriteria",
  "input_type": ".chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaRequest",
  "output_type": ".chesscom.game_gateway.v2.AggregateGameResultsByPlayerAndCriteriaResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17572"></a>
## FND-17572: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/HydrateGameByLegacyId

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "HydrateGameByLegacyId",
  "input_type": ".chesscom.game_gateway.v2.HydrateGameByLegacyIdRequest",
  "output_type": ".chesscom.game_gateway.v2.HydrateGameByLegacyIdResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17573"></a>
## FND-17573: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/PlayerOverviewStats

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "PlayerOverviewStats",
  "input_type": ".chesscom.game_gateway.v2.PlayerOverviewStatsRequest",
  "output_type": ".chesscom.game_gateway.v2.PlayerOverviewStatsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17574"></a>
## FND-17574: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/CountTournamentsByPlayer

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "CountTournamentsByPlayer",
  "input_type": ".chesscom.game_gateway.v2.CountTournamentsByPlayerRequest",
  "output_type": ".chesscom.game_gateway.v2.CountTournamentsByPlayerResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17575"></a>
## FND-17575: Frontend-declared RPC chesscom.game_gateway.v2.GameGatewayService/PlayerOverviewAllStats

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.game_gateway.v2.GameGatewayService",
  "method": "PlayerOverviewAllStats",
  "input_type": ".chesscom.game_gateway.v2.PlayerOverviewAllStatsRequest",
  "output_type": ".chesscom.game_gateway.v2.PlayerOverviewAllStatsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 154232.

```text
5fbWV0YWRhdGEYCiABKAsyJS5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjEuUGduTWV0YWRhdGE6CIKmHQQKAgECYgZwcm90bzM","chesscom/game_gateway/v2/game_gateway_service.proto":"CjNjaGVzc2NvbS9nYW1lX2dhdGV3YXkvdjIvZ2FtZV9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLmdhbWVfZ2F0ZXdheS52MiLaAQodSHlkcmF0ZUdhbWVzQnlDcml0ZXJpYVJlcXVlc3QSNAoIY3JpdGVyaWEYASABKAsyIi5jaGVzc2NvbS5nYW1lX2dhdGV3YXkudjIuQ3JpdGVyaWESLgoKZmllbGRfbWFzaxgCIAEoCzIaLmdvb2dsZS5wcm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17667"></a>
## FND-17667: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetCeeVersion

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetCeeVersion",
  "input_type": ".chesscom.explanation_engine.v1.CeeVersionRequest",
  "output_type": ".chesscom.explanation_engine.v1.CeeVersionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17668"></a>
## FND-17668: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/CreateNewGame

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "CreateNewGame",
  "input_type": ".chesscom.explanation_engine.v1.NewGameRequest",
  "output_type": ".chesscom.explanation_engine.v1.NewGameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17669"></a>
## FND-17669: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/LoadGameState

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "LoadGameState",
  "input_type": ".chesscom.explanation_engine.v1.LoadGameStateRequest",
  "output_type": ".chesscom.explanation_engine.v1.LoadGameStateResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17670"></a>
## FND-17670: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/AddEvaluations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "AddEvaluations",
  "input_type": ".chesscom.explanation_engine.v1.AddEvaluationsRequest",
  "output_type": ".chesscom.explanation_engine.v1.AddEvaluationsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17671"></a>
## FND-17671: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetExpectedPoints

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetExpectedPoints",
  "input_type": ".chesscom.explanation_engine.v1.ExpectedPointsRequest",
  "output_type": ".chesscom.explanation_engine.v1.ExpectedPointsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17672"></a>
## FND-17672: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/ValidateFen

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "ValidateFen",
  "input_type": ".chesscom.explanation_engine.v1.ValidateFenRequest",
  "output_type": ".chesscom.explanation_engine.v1.ValidateFenResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17673"></a>
## FND-17673: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/ValidatePgn

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "ValidatePgn",
  "input_type": ".chesscom.explanation_engine.v1.ValidatePgnRequest",
  "output_type": ".chesscom.explanation_engine.v1.ValidatePgnResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17674"></a>
## FND-17674: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetPgn

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetPgn",
  "input_type": ".chesscom.explanation_engine.v1.GetPgnRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetPgnResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17675"></a>
## FND-17675: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetFen

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetFen",
  "input_type": ".chesscom.explanation_engine.v1.GetFenRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetFenResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17676"></a>
## FND-17676: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetMoveDetails

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetMoveDetails",
  "input_type": ".chesscom.explanation_engine.v1.GetMoveDetailsRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetMoveDetailsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17677"></a>
## FND-17677: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetMoveClassification

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetMoveClassification",
  "input_type": ".chesscom.explanation_engine.v1.MoveClassificationRequest",
  "output_type": ".chesscom.explanation_engine.v1.MoveClassificationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17678"></a>
## FND-17678: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetAnalysisAnnotations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetAnalysisAnnotations",
  "input_type": ".chesscom.explanation_engine.v1.AnalysisAnnotationsRequest",
  "output_type": ".chesscom.explanation_engine.v1.AnalysisAnnotationsResponse",
  "client_streaming": false,
  "server_streaming": true,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17679"></a>
## FND-17679: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/MakeMoves

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "MakeMoves",
  "input_type": ".chesscom.explanation_engine.v1.MakeMovesRequest",
  "output_type": ".chesscom.explanation_engine.v1.MakeMovesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17680"></a>
## FND-17680: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/SetPlayedLine

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "SetPlayedLine",
  "input_type": ".chesscom.explanation_engine.v1.SetPlayedLineRequest",
  "output_type": ".chesscom.explanation_engine.v1.SetPlayedLineResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17681"></a>
## FND-17681: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGameReview

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGameReview",
  "input_type": ".chesscom.explanation_engine.v1.GameReviewRequest",
  "output_type": ".chesscom.explanation_engine.v1.GameReviewResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17682"></a>
## FND-17682: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGameState

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGameState",
  "input_type": ".chesscom.explanation_engine.v1.GetGameStateRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetGameStateResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17683"></a>
## FND-17683: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGamePointInfo

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGamePointInfo",
  "input_type": ".chesscom.explanation_engine.v1.GamePointInfoRequest",
  "output_type": ".chesscom.explanation_engine.v1.GamePointInfoResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17684"></a>
## FND-17684: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGameTree

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGameTree",
  "input_type": ".chesscom.explanation_engine.v1.GameTreeRequest",
  "output_type": ".chesscom.explanation_engine.v1.GameTreeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17685"></a>
## FND-17685: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGameResult

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGameResult",
  "input_type": ".chesscom.explanation_engine.v1.GetGameResultRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetGameResultResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17686"></a>
## FND-17686: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/SetGameResult

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "SetGameResult",
  "input_type": ".chesscom.explanation_engine.v1.SetGameResultRequest",
  "output_type": ".chesscom.explanation_engine.v1.SetGameResultResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17687"></a>
## FND-17687: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetLegalMoves

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetLegalMoves",
  "input_type": ".chesscom.explanation_engine.v1.LegalMovesRequest",
  "output_type": ".chesscom.explanation_engine.v1.LegalMovesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17688"></a>
## FND-17688: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetLegalPremoves

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetLegalPremoves",
  "input_type": ".chesscom.explanation_engine.v1.LegalPremovesRequest",
  "output_type": ".chesscom.explanation_engine.v1.LegalPremovesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17689"></a>
## FND-17689: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetSanMoves

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetSanMoves",
  "input_type": ".chesscom.explanation_engine.v1.GetSanMovesRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetSanMovesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17690"></a>
## FND-17690: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetThreats

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetThreats",
  "input_type": ".chesscom.explanation_engine.v1.SimpleThreatsRequest",
  "output_type": ".chesscom.explanation_engine.v1.SimpleThreatsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17691"></a>
## FND-17691: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetGamePhaseTransitions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetGamePhaseTransitions",
  "input_type": ".chesscom.explanation_engine.v1.GamePhaseTransitionsRequest",
  "output_type": ".chesscom.explanation_engine.v1.GamePhaseTransitionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17692"></a>
## FND-17692: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetOpening

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetOpening",
  "input_type": ".chesscom.explanation_engine.v1.GetOpeningRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetOpeningResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17693"></a>
## FND-17693: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/LoadBot

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "LoadBot",
  "input_type": ".chesscom.explanation_engine.v1.LoadBotRequest",
  "output_type": ".chesscom.explanation_engine.v1.LoadBotResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17694"></a>
## FND-17694: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetBotMove

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetBotMove",
  "input_type": ".chesscom.explanation_engine.v1.GetBotMoveRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetBotMoveResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17695"></a>
## FND-17695: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetBotMoveFromConfig

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetBotMoveFromConfig",
  "input_type": ".chesscom.explanation_engine.v1.BotMoveFromConfigRequest",
  "output_type": ".chesscom.explanation_engine.v1.BotMoveFromConfigResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17696"></a>
## FND-17696: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetBotConfigResources

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetBotConfigResources",
  "input_type": ".chesscom.explanation_engine.v1.BotConfigResourcesRequest",
  "output_type": ".chesscom.explanation_engine.v1.BotConfigResourcesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17697"></a>
## FND-17697: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetBotChat

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetBotChat",
  "input_type": ".chesscom.explanation_engine.v1.GetBotChatRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetBotChatResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17698"></a>
## FND-17698: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetPunishMove

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetPunishMove",
  "input_type": ".chesscom.explanation_engine.v1.GetPunishMoveRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetPunishMoveResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17699"></a>
## FND-17699: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/LoadCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "LoadCoach",
  "input_type": ".chesscom.explanation_engine.v1.LoadCoachRequest",
  "output_type": ".chesscom.explanation_engine.v1.LoadCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17700"></a>
## FND-17700: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/SetCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "SetCoach",
  "input_type": ".chesscom.explanation_engine.v1.SetCoachRequest",
  "output_type": ".chesscom.explanation_engine.v1.SetCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17701"></a>
## FND-17701: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/LoadAndSetCoach

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "LoadAndSetCoach",
  "input_type": ".chesscom.explanation_engine.v1.LoadAndSetCoachRequest",
  "output_type": ".chesscom.explanation_engine.v1.LoadAndSetCoachResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17702"></a>
## FND-17702: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetCoachChat

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetCoachChat",
  "input_type": ".chesscom.explanation_engine.v1.GetCoachChatRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetCoachChatResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17703"></a>
## FND-17703: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetCoachHint

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetCoachHint",
  "input_type": ".chesscom.explanation_engine.v1.GetCoachHintRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetCoachHintResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17704"></a>
## FND-17704: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetErgonomicPosition

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetErgonomicPosition",
  "input_type": ".chesscom.explanation_engine.v1.GetErgonomicPositionRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetErgonomicPositionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17705"></a>
## FND-17705: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetErgonomicGame

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetErgonomicGame",
  "input_type": ".chesscom.explanation_engine.v1.GetErgonomicGameRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetErgonomicGameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17706"></a>
## FND-17706: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetCompressedPosition

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetCompressedPosition",
  "input_type": ".chesscom.explanation_engine.v1.GetCompressedPositionRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetCompressedPositionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17707"></a>
## FND-17707: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/ConvertToProtoMoves

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "ConvertToProtoMoves",
  "input_type": ".chesscom.explanation_engine.v1.ConvertToProtoMovesRequest",
  "output_type": ".chesscom.explanation_engine.v1.ConvertToProtoMovesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17708"></a>
## FND-17708: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetLuaCompletion

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetLuaCompletion",
  "input_type": ".chesscom.explanation_engine.v1.LuaCompletionRequest",
  "output_type": ".chesscom.explanation_engine.v1.LuaCompletionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17709"></a>
## FND-17709: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/RunLua

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "RunLua",
  "input_type": ".chesscom.explanation_engine.v1.RunLuaRequest",
  "output_type": ".chesscom.explanation_engine.v1.RunLuaResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17710"></a>
## FND-17710: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/UpdateExperimentalOptions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "UpdateExperimentalOptions",
  "input_type": ".chesscom.explanation_engine.v1.UpdateExperimentalOptionsRequest",
  "output_type": ".chesscom.explanation_engine.v1.UpdateExperimentalOptionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17711"></a>
## FND-17711: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetCeeInternalComponents

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetCeeInternalComponents",
  "input_type": ".chesscom.explanation_engine.v1.CeeInternalComponentsRequest",
  "output_type": ".chesscom.explanation_engine.v1.CeeInternalComponentsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17712"></a>
## FND-17712: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/InternalFeaturePuzzleGen

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "InternalFeaturePuzzleGen",
  "input_type": ".chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest",
  "output_type": ".chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17713"></a>
## FND-17713: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/InternalFeatureUpdateDeveloperOptions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "InternalFeatureUpdateDeveloperOptions",
  "input_type": ".chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest",
  "output_type": ".chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17714"></a>
## FND-17714: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/InternalFeatureMaiaBotMove

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "InternalFeatureMaiaBotMove",
  "input_type": ".chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest",
  "output_type": ".chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17715"></a>
## FND-17715: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/RunSearch

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "RunSearch",
  "input_type": ".chesscom.explanation_engine.v1.RunSearchRequest",
  "output_type": ".chesscom.explanation_engine.v1.RunSearchResponse",
  "client_streaming": false,
  "server_streaming": true,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17716"></a>
## FND-17716: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/DisposeGamePoint

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "DisposeGamePoint",
  "input_type": ".chesscom.explanation_engine.v1.DisposeGamePointRequest",
  "output_type": ".chesscom.explanation_engine.v1.DisposeGamePointResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17717"></a>
## FND-17717: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetNonChessText

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetNonChessText",
  "input_type": ".chesscom.explanation_engine.v1.GetNonChessTextRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetNonChessTextResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17718"></a>
## FND-17718: Frontend-declared RPC chesscom.explanation_engine.v1.ExplanationEngineService/GetIllegalMoveExplanation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.explanation_engine.v1.ExplanationEngineService",
  "method": "GetIllegalMoveExplanation",
  "input_type": ".chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest",
  "output_type": ".chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 267424.

```text
PTUUQDxI6CjZQVVpaTEVfR0VOX0ZBSUxVUkVfVFlQRV9QSVRDSF9NT1ZFX0lOVkFMSURfQk9BUkRfRVZFTlQQEGIGcHJvdG8z","chesscom/explanation_engine/v1/explanation_engine_service.proto":"Cj9jaGVzc2NvbS9leHBsYW5hdGlvbl9lbmdpbmUvdjEvZXhwbGFuYXRpb25fZW5naW5lX3NlcnZpY2UucHJvdG8SHmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MTKkPAoYRXhwbGFuYXRpb25FbmdpbmVTZXJ2aWNlEpEBCg1HZXRDZWVWZXJzaW9uEjEuY2hlc3Njb20uZXhwbGFuYXRpb25fZW5naW5lLnYxLkNlZVZlcnNpb25SZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17739"></a>
## FND-17739: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/InviteSharedBoardParticipant

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "InviteSharedBoardParticipant",
  "input_type": ".chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest",
  "output_type": ".chesscom.shared_board.v1alpha.InviteSharedBoardParticipantResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17740"></a>
## FND-17740: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/RequestToJoinSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "RequestToJoinSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17741"></a>
## FND-17741: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/RespondToSharedBoardInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "RespondToSharedBoardInvitation",
  "input_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationRequest",
  "output_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17742"></a>
## FND-17742: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/RespondToSharedBoardJoinRequest

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "RespondToSharedBoardJoinRequest",
  "input_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest",
  "output_type": ".chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17743"></a>
## FND-17743: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/UpdateSharedBoardParticipantRole

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "UpdateSharedBoardParticipantRole",
  "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest",
  "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17744"></a>
## FND-17744: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/SetSharedBoardParticipantCapabilities

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "SetSharedBoardParticipantCapabilities",
  "input_type": ".chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest",
  "output_type": ".chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17745"></a>
## FND-17745: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/TransferSharedBoardHost

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "TransferSharedBoardHost",
  "input_type": ".chesscom.shared_board.v1alpha.TransferSharedBoardHostRequest",
  "output_type": ".chesscom.shared_board.v1alpha.TransferSharedBoardHostResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17746"></a>
## FND-17746: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/RemoveSharedBoardParticipant

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "RemoveSharedBoardParticipant",
  "input_type": ".chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantRequest",
  "output_type": ".chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17747"></a>
## FND-17747: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService/LeaveSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardSessionParticipantService",
  "method": "LeaveSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.LeaveSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.LeaveSharedBoardSessionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 298320.

```text
JkU2Vzc2lvbkVuZGVkTm90aWZpY2F0aW9uEhIKCnNlc3Npb25faWQYASABKAkSEQoJYXV0aG9yX2lkGAIgASgJYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_participant_service.proto":"CkRjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfcGFydGljaXBhbnRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEi1AEKI0ludml0ZVNoYXJlZEJvYXJkUGFydGljaXBhbnRSZXF1ZXN0EhIKCnNlc3Npb25faWQYASABKAkSDwoHdXNlcl9pZBgCIAEoCRI8CgRyb2xlG
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17749"></a>
## FND-17749: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/GetSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "GetSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.GetSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.GetSharedBoardSessionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17750"></a>
## FND-17750: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/FindSharedBoardSessionByResource

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "FindSharedBoardSessionByResource",
  "input_type": ".chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceRequest",
  "output_type": ".chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17751"></a>
## FND-17751: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/ListSharedBoardSessions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "ListSharedBoardSessions",
  "input_type": ".chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest",
  "output_type": ".chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17752"></a>
## FND-17752: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/CreateSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "CreateSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17753"></a>
## FND-17753: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/CreateSharedBoardSessionForResource

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "CreateSharedBoardSessionForResource",
  "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest",
  "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17754"></a>
## FND-17754: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/SyncCollectionRoster

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "SyncCollectionRoster",
  "input_type": ".chesscom.shared_board.v1alpha.SyncCollectionRosterRequest",
  "output_type": ".chesscom.shared_board.v1alpha.SyncCollectionRosterResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 303501.

```text
Jlc3BvbnNlQjfKtywzChkvc2VydmljZS9zaGFyZWQtYm9hcmQvcnBjEgAaEBIOeC1zZXNzaW9uLXVzZXIiAggBYgZwcm90bzM","chesscom/shared_board/v1alpha/shared_board_service.proto":"CjhjaGVzc2NvbS9zaGFyZWRfYm9hcmQvdjFhbHBoYS9zaGFyZWRfYm9hcmRfc2VydmljZS5wcm90bxIdY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEivwEKH0NyZWF0ZVNoYXJlZEJvYXJkU2Vzc2lvblJlcXVlc3QSOgoGYm9hcmRzGAEgAygLMiouY2hlc3Njb20uc2hhcmVkX2JvYXJkLnYxYWxwaGEuU2hhcmVkQm9hcmQSFwoPb3Blbl9lb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.
