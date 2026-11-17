# api_schema_services — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-17755"></a>
## FND-17755: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/UpdateSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "UpdateSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardSessionResponse",
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

<a id="FND-17756"></a>
## FND-17756: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/UpdateSharedBoardClock

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "UpdateSharedBoardClock",
  "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardClockRequest",
  "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardClockResponse",
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

<a id="FND-17757"></a>
## FND-17757: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/CreateSharedBoard

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "CreateSharedBoard",
  "input_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardRequest",
  "output_type": ".chesscom.shared_board.v1alpha.CreateSharedBoardResponse",
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

<a id="FND-17758"></a>
## FND-17758: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/DeleteSharedBoard

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "DeleteSharedBoard",
  "input_type": ".chesscom.shared_board.v1alpha.DeleteSharedBoardRequest",
  "output_type": ".chesscom.shared_board.v1alpha.DeleteSharedBoardResponse",
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

<a id="FND-17759"></a>
## FND-17759: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/UpdateSharedBoard

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "UpdateSharedBoard",
  "input_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardRequest",
  "output_type": ".chesscom.shared_board.v1alpha.UpdateSharedBoardResponse",
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

<a id="FND-17760"></a>
## FND-17760: Frontend-declared RPC chesscom.shared_board.v1alpha.SharedBoardService/EndSharedBoardSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.shared_board.v1alpha.SharedBoardService",
  "method": "EndSharedBoardSession",
  "input_type": ".chesscom.shared_board.v1alpha.EndSharedBoardSessionRequest",
  "output_type": ".chesscom.shared_board.v1alpha.EndSharedBoardSessionResponse",
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

<a id="FND-17766"></a>
## FND-17766: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListAllThemeElements

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListAllThemeElements",
  "input_type": ".chesscom.themes.v2.ListAllThemeElementsRequest",
  "output_type": ".chesscom.themes.v2.ListAllThemeElementsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17767"></a>
## FND-17767: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListThemesSelection

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListThemesSelection",
  "input_type": ".chesscom.themes.v2.ListThemesSelectionRequest",
  "output_type": ".chesscom.themes.v2.ListThemesSelectionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17768"></a>
## FND-17768: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListThemes

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListThemes",
  "input_type": ".chesscom.themes.v2.ListThemesRequest",
  "output_type": ".chesscom.themes.v2.ListThemesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17769"></a>
## FND-17769: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListBackgrounds

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListBackgrounds",
  "input_type": ".chesscom.themes.v2.ListBackgroundsRequest",
  "output_type": ".chesscom.themes.v2.ListBackgroundsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17770"></a>
## FND-17770: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListBoardStyles

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListBoardStyles",
  "input_type": ".chesscom.themes.v2.ListBoardStylesRequest",
  "output_type": ".chesscom.themes.v2.ListBoardStylesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17771"></a>
## FND-17771: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListPieceSets

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListPieceSets",
  "input_type": ".chesscom.themes.v2.ListPieceSetsRequest",
  "output_type": ".chesscom.themes.v2.ListPieceSetsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17772"></a>
## FND-17772: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListSoundSets

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListSoundSets",
  "input_type": ".chesscom.themes.v2.ListSoundSetsRequest",
  "output_type": ".chesscom.themes.v2.ListSoundSetsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17773"></a>
## FND-17773: Frontend-declared RPC chesscom.themes.v2.ThemesService/ListOnboardingThemes

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "ListOnboardingThemes",
  "input_type": ".chesscom.themes.v2.ListOnboardingThemesRequest",
  "output_type": ".chesscom.themes.v2.ListOnboardingThemesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17774"></a>
## FND-17774: Frontend-declared RPC chesscom.themes.v2.ThemesService/GetTheme

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "GetTheme",
  "input_type": ".chesscom.themes.v2.GetThemeRequest",
  "output_type": ".chesscom.themes.v2.GetThemeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17775"></a>
## FND-17775: Frontend-declared RPC chesscom.themes.v2.ThemesService/GetCustomTheme

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "GetCustomTheme",
  "input_type": ".chesscom.themes.v2.GetCustomThemeRequest",
  "output_type": ".chesscom.themes.v2.GetCustomThemeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17776"></a>
## FND-17776: Frontend-declared RPC chesscom.themes.v2.ThemesService/SelectTheme

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "SelectTheme",
  "input_type": ".chesscom.themes.v2.SelectThemeRequest",
  "output_type": ".chesscom.themes.v2.SelectThemeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17777"></a>
## FND-17777: Frontend-declared RPC chesscom.themes.v2.ThemesService/SelectCustomTheme

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "SelectCustomTheme",
  "input_type": ".chesscom.themes.v2.SelectCustomThemeRequest",
  "output_type": ".chesscom.themes.v2.SelectCustomThemeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17778"></a>
## FND-17778: Frontend-declared RPC chesscom.themes.v2.ThemesService/GetActiveTheme

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.themes.v2.ThemesService",
  "method": "GetActiveTheme",
  "input_type": ".chesscom.themes.v2.GetActiveThemeRequest",
  "output_type": ".chesscom.themes.v2.GetActiveThemeResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 318134.

```text
RGT1JNX1dFQhABEhQKEFBMQVRGT1JNX0FORFJPSUQQAhITCg9QTEFURk9STV9JUEhPTkUQAxoJGAGKph0DCgEBYgZwcm90bzM","chesscom/themes/v2/themes_service.proto":"CidjaGVzc2NvbS90aGVtZXMvdjIvdGhlbWVzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnRoZW1lcy52MiJPChtMaXN0QWxsVGhlbWVFbGVtZW50c1JlcXVlc3QSEgoKYm9hcmRfc2l6ZRgBIAEoBRITCgtwaWVjZXNfc2l6ZRgCIAEoBToHgqYdAwoBASKnAgocTGlzdEFsbFRoZW1lRWxlbWVudHNSZXNwb25zZRIvCgZ0aGVtZXMYASADKAsyHy5jaGVzc2NvbS50aGVtZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17787"></a>
## FND-17787: Frontend-declared RPC chesscom.bots.v1.BotGroupService/ListBotGroups

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.bots.v1.BotGroupService",
  "method": "ListBotGroups",
  "input_type": ".chesscom.bots.v1.ListBotGroupsRequest",
  "output_type": ".chesscom.bots.v1.ListBotGroupsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 342506.

```text
QCg5fc3RhZmZfZW5hYmxlZEoECAQQBUoECAUQBkoECAYQB0oECAcQCEoECAgQCUoECAoQC0oECAsQDEoECA0QDmIGcHJvdG8z","chesscom/bots/v1/bot_group_service.proto":"CihjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cF9zZXJ2aWNlLnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIpIBChRMaXN0Qm90R3JvdXBzUmVxdWVzdBIbCg5ib3RfZ3JvdXBfdXVpZBgBIAEoCUgAiAEBEhYKCXdpdGhfYm90cxgFIAEoCEgBiAEBEhsKE3N1cHBvcnRlZF9sYW5ndWFnZXMYBiADKAk6B4KmHQMKAQFCEQoPX2JvdF9ncm91cF91dWlkQgwKCl93aXRoX2Jvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17788"></a>
## FND-17788: Frontend-declared RPC chesscom.bots.v1.BotGroupService/ListAllBotsInGroup

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.bots.v1.BotGroupService",
  "method": "ListAllBotsInGroup",
  "input_type": ".chesscom.bots.v1.ListAllBotsInGroupRequest",
  "output_type": ".chesscom.bots.v1.ListAllBotsInGroupResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 342506.

```text
QCg5fc3RhZmZfZW5hYmxlZEoECAQQBUoECAUQBkoECAYQB0oECAcQCEoECAgQCUoECAoQC0oECAsQDEoECA0QDmIGcHJvdG8z","chesscom/bots/v1/bot_group_service.proto":"CihjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cF9zZXJ2aWNlLnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIpIBChRMaXN0Qm90R3JvdXBzUmVxdWVzdBIbCg5ib3RfZ3JvdXBfdXVpZBgBIAEoCUgAiAEBEhYKCXdpdGhfYm90cxgFIAEoCEgBiAEBEhsKE3N1cHBvcnRlZF9sYW5ndWFnZXMYBiADKAk6B4KmHQMKAQFCEQoPX2JvdF9ncm91cF91dWlkQgwKCl93aXRoX2Jvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17789"></a>
## FND-17789: Frontend-declared RPC chesscom.bots.v1.BotGroupService/ListAllBotsForClub

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.bots.v1.BotGroupService",
  "method": "ListAllBotsForClub",
  "input_type": ".chesscom.bots.v1.ListAllBotsForClubRequest",
  "output_type": ".chesscom.bots.v1.ListAllBotsForClubResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 342506.

```text
QCg5fc3RhZmZfZW5hYmxlZEoECAQQBUoECAUQBkoECAYQB0oECAcQCEoECAgQCUoECAoQC0oECAsQDEoECA0QDmIGcHJvdG8z","chesscom/bots/v1/bot_group_service.proto":"CihjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cF9zZXJ2aWNlLnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIpIBChRMaXN0Qm90R3JvdXBzUmVxdWVzdBIbCg5ib3RfZ3JvdXBfdXVpZBgBIAEoCUgAiAEBEhYKCXdpdGhfYm90cxgFIAEoCEgBiAEBEhsKE3N1cHBvcnRlZF9sYW5ndWFnZXMYBiADKAk6B4KmHQMKAQFCEQoPX2JvdF9ncm91cF91dWlkQgwKCl93aXRoX2Jvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17790"></a>
## FND-17790: Frontend-declared RPC chesscom.bots.v1.BotGroupService/ListAllBotNames

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.bots.v1.BotGroupService",
  "method": "ListAllBotNames",
  "input_type": ".chesscom.bots.v1.ListAllBotNamesRequest",
  "output_type": ".chesscom.bots.v1.ListAllBotNamesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 342506.

```text
QCg5fc3RhZmZfZW5hYmxlZEoECAQQBUoECAUQBkoECAYQB0oECAcQCEoECAgQCUoECAoQC0oECAsQDEoECA0QDmIGcHJvdG8z","chesscom/bots/v1/bot_group_service.proto":"CihjaGVzc2NvbS9ib3RzL3YxL2JvdF9ncm91cF9zZXJ2aWNlLnByb3RvEhBjaGVzc2NvbS5ib3RzLnYxIpIBChRMaXN0Qm90R3JvdXBzUmVxdWVzdBIbCg5ib3RfZ3JvdXBfdXVpZBgBIAEoCUgAiAEBEhYKCXdpdGhfYm90cxgFIAEoCEgBiAEBEhsKE3N1cHBvcnRlZF9sYW5ndWFnZXMYBiADKAk6B4KmHQMKAQFCEQoPX2JvdF9ncm91cF91dWlkQgwKCl93aXRoX2Jvd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17861"></a>
## FND-17861: Frontend-declared RPC chesscom.user_properties.v1.AuthenticatedPropertiesService/GetPropertiesForAuthenticatedUser

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_properties.v1.AuthenticatedPropertiesService",
  "method": "GetPropertiesForAuthenticatedUser",
  "input_type": ".chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserRequest",
  "output_type": ".chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 649239.

```text
nbGUucHJvdG9idWYuVGltZXN0YW1wUg9kZXByZWNhdGlvbkRhdGWIAQE6B4KmHQMKAQFCDAoKZGVmaW5pdGlvbmIGcHJvdG8z","chesscom/user_properties/v1/authenticated_properties_service.proto":"CkJjaGVzc2NvbS91c2VyX3Byb3BlcnRpZXMvdjEvYXV0aGVudGljYXRlZF9wcm9wZXJ0aWVzX3NlcnZpY2UucHJvdG8SG2NoZXNzY29tLnVzZXJfcHJvcGVydGllcy52MSJxCihHZXRQcm9wZXJ0aWVzRm9yQXV0aGVudGljYXRlZFVzZXJSZXF1ZXN0EjwKCnByb3BlcnRpZXMYASADKAsyKC5jaGVzc2NvbS51c2VyX3Byb3BlcnRpZXM
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17866"></a>
## FND-17866: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/GetUserData

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "GetUserData",
  "input_type": ".chesscom.user_gateway.v1.GetUserDataRequest",
  "output_type": ".chesscom.user_gateway.v1.GetUserDataResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17867"></a>
## FND-17867: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/GetUserDataByUsername

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "GetUserDataByUsername",
  "input_type": ".chesscom.user_gateway.v1.GetUserDataByUsernameRequest",
  "output_type": ".chesscom.user_gateway.v1.GetUserDataByUsernameResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17868"></a>
## FND-17868: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/GetUserDataMany

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "GetUserDataMany",
  "input_type": ".chesscom.user_gateway.v1.GetUserDataManyRequest",
  "output_type": ".chesscom.user_gateway.v1.GetUserDataManyResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17869"></a>
## FND-17869: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/ListRelatedUsersData

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "ListRelatedUsersData",
  "input_type": ".chesscom.user_gateway.v1.ListRelatedUsersDataRequest",
  "output_type": ".chesscom.user_gateway.v1.ListRelatedUsersDataResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17870"></a>
## FND-17870: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/GetUserDataWithOtherUsernames

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "GetUserDataWithOtherUsernames",
  "input_type": ".chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesRequest",
  "output_type": ".chesscom.user_gateway.v1.GetUserDataWithOtherUsernamesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17871"></a>
## FND-17871: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/ListUsers

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "ListUsers",
  "input_type": ".chesscom.user_gateway.v1.ListUsersRequest",
  "output_type": ".chesscom.user_gateway.v1.ListUsersResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17872"></a>
## FND-17872: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/SendFriendRequest

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "SendFriendRequest",
  "input_type": ".chesscom.user_gateway.v1.SendFriendRequestRequest",
  "output_type": ".chesscom.user_gateway.v1.SendFriendRequestResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17873"></a>
## FND-17873: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/AcceptFriendRequest

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "AcceptFriendRequest",
  "input_type": ".chesscom.user_gateway.v1.AcceptFriendRequestRequest",
  "output_type": ".chesscom.user_gateway.v1.AcceptFriendRequestResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17874"></a>
## FND-17874: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/DeclineFriendRequest

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "DeclineFriendRequest",
  "input_type": ".chesscom.user_gateway.v1.DeclineFriendRequestRequest",
  "output_type": ".chesscom.user_gateway.v1.DeclineFriendRequestResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17875"></a>
## FND-17875: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/CancelFriendRequest

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "CancelFriendRequest",
  "input_type": ".chesscom.user_gateway.v1.CancelFriendRequestRequest",
  "output_type": ".chesscom.user_gateway.v1.CancelFriendRequestResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17876"></a>
## FND-17876: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/RemoveFriend

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "RemoveFriend",
  "input_type": ".chesscom.user_gateway.v1.RemoveFriendRequest",
  "output_type": ".chesscom.user_gateway.v1.RemoveFriendResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17877"></a>
## FND-17877: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/BlockUser

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "BlockUser",
  "input_type": ".chesscom.user_gateway.v1.BlockUserRequest",
  "output_type": ".chesscom.user_gateway.v1.BlockUserResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17878"></a>
## FND-17878: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/UnblockUser

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "UnblockUser",
  "input_type": ".chesscom.user_gateway.v1.UnblockUserRequest",
  "output_type": ".chesscom.user_gateway.v1.UnblockUserResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17879"></a>
## FND-17879: Frontend-declared RPC chesscom.user_gateway.v1.UserGatewayService/AcceptFriendLink

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_gateway.v1.UserGatewayService",
  "method": "AcceptFriendLink",
  "input_type": ".chesscom.user_gateway.v1.AcceptFriendLinkRequest",
  "output_type": ".chesscom.user_gateway.v1.AcceptFriendLinkResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 657472.

```text
W50aWZpZXISEwoJdXNlcl91dWlkGAEgASgJSAASEgoIdXNlcm5hbWUYAiABKAlIADoIgqYdBAoCAQJCBAoCaWRiBnByb3RvMw","chesscom/user_gateway/v1/user_gateway_service.proto":"CjNjaGVzc2NvbS91c2VyX2dhdGV3YXkvdjEvdXNlcl9nYXRld2F5X3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfZ2F0ZXdheS52MSLXAQoSR2V0VXNlckRhdGFSZXF1ZXN0EhEKCXVzZXJfdXVpZBgBIAEoCRIYChBvdGhlcl91c2VyX3V1aWRzGAIgAygJElsKEnVzZXJfcmVsYXRpb25zaGlwcxgDIAMoCzI/LmNoZXNzY29tLnVzZXJfcmVsYXRpb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17882"></a>
## FND-17882: Frontend-declared RPC chesscom.friends_search.v1.FriendsNavigationService/ListRecentFriends

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsNavigationService",
  "method": "ListRecentFriends",
  "input_type": ".chesscom.friends_search.v1.ListRecentFriendsRequest",
  "output_type": ".chesscom.friends_search.v1.ListRecentFriendsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 676259.

```text
EFSEAESMQotRlJJRU5EU19TRUFSQ0hfUkVUUklFVkFCTEVfRklFTERfQ09VTlRSWV9DT0RFEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/friends_search/v1/friends_navigation_service.proto":"CjtjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX25hdmlnYXRpb25fc2VydmljZS5wcm90bxIaY2hlc3Njb20uZnJpZW5kc19zZWFyY2gudjEiIwoYTGlzdFJlY2VudEZyaWVuZHNSZXF1ZXN0OgeCph0DCgEBImwKGUxpc3RSZWNlbnRGcmllbmRzUmVzcG9uc2USRgoHZnJpZW5kcxgBIAMoCzI1LmNoZXNzY29tLmZyaWVuZHNfc2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17883"></a>
## FND-17883: Frontend-declared RPC chesscom.friends_search.v1.FriendsNavigationService/ListRecentPendingFriends

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsNavigationService",
  "method": "ListRecentPendingFriends",
  "input_type": ".chesscom.friends_search.v1.ListRecentPendingFriendsRequest",
  "output_type": ".chesscom.friends_search.v1.ListRecentPendingFriendsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 676259.

```text
EFSEAESMQotRlJJRU5EU19TRUFSQ0hfUkVUUklFVkFCTEVfRklFTERfQ09VTlRSWV9DT0RFEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/friends_search/v1/friends_navigation_service.proto":"CjtjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX25hdmlnYXRpb25fc2VydmljZS5wcm90bxIaY2hlc3Njb20uZnJpZW5kc19zZWFyY2gudjEiIwoYTGlzdFJlY2VudEZyaWVuZHNSZXF1ZXN0OgeCph0DCgEBImwKGUxpc3RSZWNlbnRGcmllbmRzUmVzcG9uc2USRgoHZnJpZW5kcxgBIAMoCzI1LmNoZXNzY29tLmZyaWVuZHNfc2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17884"></a>
## FND-17884: Frontend-declared RPC chesscom.friends_search.v1.FriendsNavigationService/SocialAutocomplete

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsNavigationService",
  "method": "SocialAutocomplete",
  "input_type": ".chesscom.friends_search.v1.SocialAutocompleteRequest",
  "output_type": ".chesscom.friends_search.v1.SocialAutocompleteResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 676259.

```text
EFSEAESMQotRlJJRU5EU19TRUFSQ0hfUkVUUklFVkFCTEVfRklFTERfQ09VTlRSWV9DT0RFEAIaB4qmHQMKAQFiBnByb3RvMw","chesscom/friends_search/v1/friends_navigation_service.proto":"CjtjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX25hdmlnYXRpb25fc2VydmljZS5wcm90bxIaY2hlc3Njb20uZnJpZW5kc19zZWFyY2gudjEiIwoYTGlzdFJlY2VudEZyaWVuZHNSZXF1ZXN0OgeCph0DCgEBImwKGUxpc3RSZWNlbnRGcmllbmRzUmVzcG9uc2USRgoHZnJpZW5kcxgBIAMoCzI1LmNoZXNzY29tLmZyaWVuZHNfc2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17886"></a>
## FND-17886: Frontend-declared RPC chesscom.friends_search.v1.FriendsSearchService/QueryFriends

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsSearchService",
  "method": "QueryFriends",
  "input_type": ".chesscom.friends_search.v1.QueryFriendsRequest",
  "output_type": ".chesscom.friends_search.v1.QueryFriendsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17887"></a>
## FND-17887: Frontend-declared RPC chesscom.friends_search.v1.FriendsSearchService/Autocomplete

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsSearchService",
  "method": "Autocomplete",
  "input_type": ".chesscom.friends_search.v1.AutocompleteRequest",
  "output_type": ".chesscom.friends_search.v1.AutocompleteResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17888"></a>
## FND-17888: Frontend-declared RPC chesscom.friends_search.v1.FriendsSearchService/GetBlockersOf

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsSearchService",
  "method": "GetBlockersOf",
  "input_type": ".chesscom.friends_search.v1.GetBlockersOfRequest",
  "output_type": ".chesscom.friends_search.v1.GetBlockersOfResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17889"></a>
## FND-17889: Frontend-declared RPC chesscom.friends_search.v1.FriendsSearchService/GetUsersBlockedBy

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsSearchService",
  "method": "GetUsersBlockedBy",
  "input_type": ".chesscom.friends_search.v1.GetUsersBlockedByRequest",
  "output_type": ".chesscom.friends_search.v1.GetUsersBlockedByResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17890"></a>
## FND-17890: Frontend-declared RPC chesscom.friends_search.v1.FriendsSearchService/GetFriendsCount

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.friends_search.v1.FriendsSearchService",
  "method": "GetFriendsCount",
  "input_type": ".chesscom.friends_search.v1.GetFriendsCountRequest",
  "output_type": ".chesscom.friends_search.v1.GetFriendsCountResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 678739.

```text
dpbmcuY2hlc3MtcGxhdGZvcm0uY29tEhdwcm9kLmNoZXNzLXBsYXRmb3JtLmNvbRoLEglwaHBzZXNzaWQiAggBYgZwcm90bzM","chesscom/friends_search/v1/friends_search_service.proto":"CjdjaGVzc2NvbS9mcmllbmRzX3NlYXJjaC92MS9mcmllbmRzX3NlYXJjaF9zZXJ2aWNlLnByb3RvEhpjaGVzc2NvbS5mcmllbmRzX3NlYXJjaC52MSKLAgoTUXVlcnlGcmllbmRzUmVxdWVzdBIRCgR1dWlkGAEgASgJSACIAQESJAoXaW5jbHVkZV9wcmVzZW5jZV9zdGF0dXMYAiABKAhIAYgBARI7CgpwYWdpbmF0aW9uGAMgASgLMiIuY2hlc3Njb2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17919"></a>
## FND-17919: Frontend-declared RPC chesscom.courses.v1.CourseRecommendationService/GetCourseRecommendationForPosition

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseRecommendationService",
  "method": "GetCourseRecommendationForPosition",
  "input_type": ".chesscom.courses.v1.GetCourseRecommendationForPositionRequest",
  "output_type": ".chesscom.courses.v1.GetCourseRecommendationForPositionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 721459.

```text
DT01NRU5EQVRJT05fU0lHTkFMX0FDVElWSVRZEAMSIQodUkVDT01NRU5EQVRJT05fU0lHTkFMX1FVQUxJVFkQBGIGcHJvdG8z","chesscom/courses/v1/course_recommendation_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbl9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoACCilHZXRDb3Vyc2VSZWNvbW1lbmRhdGlvbkZvclBvc2l0aW9uUmVxdWVzdBITCgZyYXRpbmcYASABKAVIAIgBARIsCgVjb2xvchgCIAEoDjIYLmNoZXNzY29tLmNoZXNzLnYxLkNvbG9ySAGIAQESCwoDZm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17920"></a>
## FND-17920: Frontend-declared RPC chesscom.courses.v1.CourseRecommendationService/GetCoursesForPosition

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseRecommendationService",
  "method": "GetCoursesForPosition",
  "input_type": ".chesscom.courses.v1.GetCoursesForPositionRequest",
  "output_type": ".chesscom.courses.v1.GetCoursesForPositionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 721459.

```text
DT01NRU5EQVRJT05fU0lHTkFMX0FDVElWSVRZEAMSIQodUkVDT01NRU5EQVRJT05fU0lHTkFMX1FVQUxJVFkQBGIGcHJvdG8z","chesscom/courses/v1/course_recommendation_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbl9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoACCilHZXRDb3Vyc2VSZWNvbW1lbmRhdGlvbkZvclBvc2l0aW9uUmVxdWVzdBITCgZyYXRpbmcYASABKAVIAIgBARIsCgVjb2xvchgCIAEoDjIYLmNoZXNzY29tLmNoZXNzLnYxLkNvbG9ySAGIAQESCwoDZm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17921"></a>
## FND-17921: Frontend-declared RPC chesscom.courses.v1.CourseRecommendationService/GetUserCourseRecommendations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseRecommendationService",
  "method": "GetUserCourseRecommendations",
  "input_type": ".chesscom.courses.v1.GetUserCourseRecommendationsRequest",
  "output_type": ".chesscom.courses.v1.GetUserCourseRecommendationsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 721459.

```text
DT01NRU5EQVRJT05fU0lHTkFMX0FDVElWSVRZEAMSIQodUkVDT01NRU5EQVRJT05fU0lHTkFMX1FVQUxJVFkQBGIGcHJvdG8z","chesscom/courses/v1/course_recommendation_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbl9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoACCilHZXRDb3Vyc2VSZWNvbW1lbmRhdGlvbkZvclBvc2l0aW9uUmVxdWVzdBITCgZyYXRpbmcYASABKAVIAIgBARIsCgVjb2xvchgCIAEoDjIYLmNoZXNzY29tLmNoZXNzLnYxLkNvbG9ySAGIAQESCwoDZm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17922"></a>
## FND-17922: Frontend-declared RPC chesscom.courses.v1.CourseRecommendationService/ReportRecommendationImpression

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseRecommendationService",
  "method": "ReportRecommendationImpression",
  "input_type": ".chesscom.courses.v1.ReportRecommendationImpressionRequest",
  "output_type": ".chesscom.courses.v1.ReportRecommendationImpressionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 721459.

```text
DT01NRU5EQVRJT05fU0lHTkFMX0FDVElWSVRZEAMSIQodUkVDT01NRU5EQVRJT05fU0lHTkFMX1FVQUxJVFkQBGIGcHJvdG8z","chesscom/courses/v1/course_recommendation_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9yZWNvbW1lbmRhdGlvbl9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIoACCilHZXRDb3Vyc2VSZWNvbW1lbmRhdGlvbkZvclBvc2l0aW9uUmVxdWVzdBITCgZyYXRpbmcYASABKAVIAIgBARIsCgVjb2xvchgCIAEoDjIYLmNoZXNzY29tLmNoZXNzLnYxLkNvbG9ySAGIAQESCwoDZm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17926"></a>
## FND-17926: Frontend-declared RPC chesscom.courses.v1.UserGoalService/SetUserGoal

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.UserGoalService",
  "method": "SetUserGoal",
  "input_type": ".chesscom.courses.v1.SetUserGoalRequest",
  "output_type": ".chesscom.courses.v1.SetUserGoalResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 724702.

```text
SIgoeUkVXQVJEX1RZUEVfQU5ZX0RJQU1PTkRfQ09VUlNFEAESGwoXUkVXQVJEX1RZUEVfUEFJRF9DT1VSU0UQAmIGcHJvdG8z","chesscom/courses/v1/user_goal_service.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZ29hbF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIkYKElNldFVzZXJHb2FsUmVxdWVzdBIwCglnb2FsX3R5cGUYASABKA4yHS5jaGVzc2NvbS5jb3Vyc2VzLnYxLkdvYWxUeXBlIhUKE1NldFVzZXJHb2FsUmVzcG9uc2UicwoSQ2xhaW1SZXdhcmRSZXF1ZXN0EjAKCWdvYWxfdHlwZRgBIAEoDjIdLm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17927"></a>
## FND-17927: Frontend-declared RPC chesscom.courses.v1.UserGoalService/ClaimReward

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.UserGoalService",
  "method": "ClaimReward",
  "input_type": ".chesscom.courses.v1.ClaimRewardRequest",
  "output_type": ".chesscom.courses.v1.ClaimRewardResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 724702.

```text
SIgoeUkVXQVJEX1RZUEVfQU5ZX0RJQU1PTkRfQ09VUlNFEAESGwoXUkVXQVJEX1RZUEVfUEFJRF9DT1VSU0UQAmIGcHJvdG8z","chesscom/courses/v1/user_goal_service.proto":"CitjaGVzc2NvbS9jb3Vyc2VzL3YxL3VzZXJfZ29hbF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIkYKElNldFVzZXJHb2FsUmVxdWVzdBIwCglnb2FsX3R5cGUYASABKA4yHS5jaGVzc2NvbS5jb3Vyc2VzLnYxLkdvYWxUeXBlIhUKE1NldFVzZXJHb2FsUmVzcG9uc2UicwoSQ2xhaW1SZXdhcmRSZXF1ZXN0EjAKCWdvYWxfdHlwZRgBIAEoDjIdLm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17933"></a>
## FND-17933: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/GetCourseList

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "GetCourseList",
  "input_type": ".chesscom.courses.v1.GetCourseListRequest",
  "output_type": ".chesscom.courses.v1.GetCourseListResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17934"></a>
## FND-17934: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/SetCourseInactive

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "SetCourseInactive",
  "input_type": ".chesscom.courses.v1.SetCourseInactiveRequest",
  "output_type": ".chesscom.courses.v1.SetCourseInactiveResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17935"></a>
## FND-17935: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/SetCoursePaused

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "SetCoursePaused",
  "input_type": ".chesscom.courses.v1.SetCoursePausedRequest",
  "output_type": ".chesscom.courses.v1.SetCoursePausedResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17936"></a>
## FND-17936: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/SetCourseUnpaused

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "SetCourseUnpaused",
  "input_type": ".chesscom.courses.v1.SetCourseUnpausedRequest",
  "output_type": ".chesscom.courses.v1.SetCourseUnpausedResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17937"></a>
## FND-17937: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/AssignTutorial

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "AssignTutorial",
  "input_type": ".chesscom.courses.v1.AssignTutorialRequest",
  "output_type": ".chesscom.courses.v1.AssignTutorialResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17938"></a>
## FND-17938: Frontend-declared RPC chesscom.courses.v1.CoursesDashboardService/GetAvailableTutorials

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesDashboardService",
  "method": "GetAvailableTutorials",
  "input_type": ".chesscom.courses.v1.GetAvailableTutorialsRequest",
  "output_type": ".chesscom.courses.v1.GetAvailableTutorialsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 727900.

```text
QAhIeChpUVVRPUklBTF9DQVRFR09SWV9TVFJBVEVHWRADEh0KGVRVVE9SSUFMX0NBVEVHT1JZX0VOREdBTUUQBGIGcHJvdG8z","chesscom/courses/v1/courses_dashboard_service.proto":"CjNjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfZGFzaGJvYXJkX3NlcnZpY2UucHJvdG8SE2NoZXNzY29tLmNvdXJzZXMudjEiFgoUR2V0Q291cnNlTGlzdFJlcXVlc3QiSQoVR2V0Q291cnNlTGlzdFJlc3BvbnNlEjAKC2NvdXJzZV9saXN0GAEgAygLMhsuY2hlc3Njb20uY291cnNlcy52MS5Db3Vyc2UiLQoYU2V0Q291cnNlSW5hY3RpdmVSZXF1ZX
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17942"></a>
## FND-17942: Frontend-declared RPC chesscom.courses.v1.CourseProductDetailsService/GetCourseProductBySlug

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseProductDetailsService",
  "method": "GetCourseProductBySlug",
  "input_type": ".chesscom.courses.v1.GetCourseProductBySlugRequest",
  "output_type": ".chesscom.courses.v1.GetCourseProductBySlugResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 731058.

```text
VzX2NvbW1vbi52MS5Db3Vyc2VQcm9kdWN0UmV2aWV3Eh8KF2RlZmF1bHRfbW92ZV90cmFpbmVyX2lkGAQgASgJYgZwcm90bzM","chesscom/courses/v1/course_product_details_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHNfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJDCh1HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVxdWVzdBIMCgRzbHVnGAEgASgJEhQKDGNvdW50cnlfY29kZRgCIAEoCSJcCh5HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVzcG9uc2USOgoHZGV0YWlscxgBI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17943"></a>
## FND-17943: Frontend-declared RPC chesscom.courses.v1.CourseProductDetailsService/ClaimCourseProduct

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseProductDetailsService",
  "method": "ClaimCourseProduct",
  "input_type": ".chesscom.courses.v1.ClaimCourseProductRequest",
  "output_type": ".chesscom.courses.v1.ClaimCourseProductResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 731058.

```text
VzX2NvbW1vbi52MS5Db3Vyc2VQcm9kdWN0UmV2aWV3Eh8KF2RlZmF1bHRfbW92ZV90cmFpbmVyX2lkGAQgASgJYgZwcm90bzM","chesscom/courses/v1/course_product_details_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHNfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJDCh1HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVxdWVzdBIMCgRzbHVnGAEgASgJEhQKDGNvdW50cnlfY29kZRgCIAEoCSJcCh5HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVzcG9uc2USOgoHZGV0YWlscxgBI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17944"></a>
## FND-17944: Frontend-declared RPC chesscom.courses.v1.CourseProductDetailsService/GetDefaultMoveTrainerIdByProductId

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseProductDetailsService",
  "method": "GetDefaultMoveTrainerIdByProductId",
  "input_type": ".chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdRequest",
  "output_type": ".chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 731058.

```text
VzX2NvbW1vbi52MS5Db3Vyc2VQcm9kdWN0UmV2aWV3Eh8KF2RlZmF1bHRfbW92ZV90cmFpbmVyX2lkGAQgASgJYgZwcm90bzM","chesscom/courses/v1/course_product_details_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHNfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJDCh1HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVxdWVzdBIMCgRzbHVnGAEgASgJEhQKDGNvdW50cnlfY29kZRgCIAEoCSJcCh5HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVzcG9uc2USOgoHZGV0YWlscxgBI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17945"></a>
## FND-17945: Frontend-declared RPC chesscom.courses.v1.CourseProductDetailsService/SetCourseActive

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CourseProductDetailsService",
  "method": "SetCourseActive",
  "input_type": ".chesscom.courses.v1.SetCourseActiveRequest",
  "output_type": ".chesscom.courses.v1.SetCourseActiveResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 731058.

```text
VzX2NvbW1vbi52MS5Db3Vyc2VQcm9kdWN0UmV2aWV3Eh8KF2RlZmF1bHRfbW92ZV90cmFpbmVyX2lkGAQgASgJYgZwcm90bzM","chesscom/courses/v1/course_product_details_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2RldGFpbHNfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJDCh1HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVxdWVzdBIMCgRzbHVnGAEgASgJEhQKDGNvdW50cnlfY29kZRgCIAEoCSJcCh5HZXRDb3Vyc2VQcm9kdWN0QnlTbHVnUmVzcG9uc2USOgoHZGV0YWlscxgBI
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17961"></a>
## FND-17961: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseLearningSession

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseLearningSession",
  "input_type": ".chesscom.courses.v1.GetCourseLearningSessionRequest",
  "output_type": ".chesscom.courses.v1.GetCourseLearningSessionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17962"></a>
## FND-17962: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseTrainingForLearning

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseTrainingForLearning",
  "input_type": ".chesscom.courses.v1.GetCourseTrainingForLearningRequest",
  "output_type": ".chesscom.courses.v1.GetCourseTrainingForLearningResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17963"></a>
## FND-17963: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseTrainingForReviewing

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseTrainingForReviewing",
  "input_type": ".chesscom.courses.v1.GetCourseTrainingForReviewingRequest",
  "output_type": ".chesscom.courses.v1.GetCourseTrainingForReviewingResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17964"></a>
## FND-17964: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/StoreCourseTrainingProgress

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "StoreCourseTrainingProgress",
  "input_type": ".chesscom.courses.v1.StoreCourseTrainingProgressRequest",
  "output_type": ".chesscom.courses.v1.StoreCourseTrainingProgressResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17965"></a>
## FND-17965: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/StoreCourseVideoProgress

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "StoreCourseVideoProgress",
  "input_type": ".chesscom.courses.v1.StoreCourseVideoProgressRequest",
  "output_type": ".chesscom.courses.v1.StoreCourseVideoProgressResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17966"></a>
## FND-17966: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseVideoPlayback

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseVideoPlayback",
  "input_type": ".chesscom.courses.v1.GetCourseVideoPlaybackRequest",
  "output_type": ".chesscom.courses.v1.GetCourseVideoPlaybackResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17967"></a>
## FND-17967: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/FinalizeCourseTraining

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "FinalizeCourseTraining",
  "input_type": ".chesscom.courses.v1.FinalizeCourseTrainingRequest",
  "output_type": ".chesscom.courses.v1.FinalizeCourseTrainingResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17968"></a>
## FND-17968: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseStats

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseStats",
  "input_type": ".chesscom.courses.v1.GetCourseStatsRequest",
  "output_type": ".chesscom.courses.v1.GetCourseStatsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17969"></a>
## FND-17969: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/GetCourseConfiguration

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "GetCourseConfiguration",
  "input_type": ".chesscom.courses.v1.GetCourseConfigurationRequest",
  "output_type": ".chesscom.courses.v1.GetCourseConfigurationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17970"></a>
## FND-17970: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/StoreCourseConfiguration

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "StoreCourseConfiguration",
  "input_type": ".chesscom.courses.v1.StoreCourseConfigurationRequest",
  "output_type": ".chesscom.courses.v1.StoreCourseConfigurationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17971"></a>
## FND-17971: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/DeleteCourseProgress

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "DeleteCourseProgress",
  "input_type": ".chesscom.courses.v1.DeleteCourseProgressRequest",
  "output_type": ".chesscom.courses.v1.DeleteCourseProgressResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17972"></a>
## FND-17972: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/ClaimPreview

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "ClaimPreview",
  "input_type": ".chesscom.courses.v1.ClaimPreviewRequest",
  "output_type": ".chesscom.courses.v1.ClaimPreviewResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17973"></a>
## FND-17973: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/SetVariationPaused

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "SetVariationPaused",
  "input_type": ".chesscom.courses.v1.SetVariationPausedRequest",
  "output_type": ".chesscom.courses.v1.SetVariationPausedResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17974"></a>
## FND-17974: Frontend-declared RPC chesscom.courses.v1.CoursesTrainingService/SetVariationUnpaused

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesTrainingService",
  "method": "SetVariationUnpaused",
  "input_type": ".chesscom.courses.v1.SetVariationUnpausedRequest",
  "output_type": ".chesscom.courses.v1.SetVariationUnpausedResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 744460.

```text
W5ndWFnZRgBIAEoCRISCgVsYWJlbBgCIAEoCUgAiAEBEgsKA3VybBgDIAEoCToHgqYdAwoBAUIICgZfbGFiZWxiBnByb3RvMw","chesscom/courses/v1/courses_training_service.proto":"CjJjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfdHJhaW5pbmdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSKvAQofR2V0Q291cnNlTGVhcm5pbmdTZXNzaW9uUmVxdWVzdBIUCgxjb250ZXh0X3R5cGUYASABKAkSEgoKY29udGV4dF9pZBgCIAEoCRIgChNsZWFybmluZ19zZXNzaW9uX2lkGAMgASgJSACIAQESGAoLY291cnNlX3NsdWc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17976"></a>
## FND-17976: Frontend-declared RPC chesscom.courses.v1.GetCourseProductBySKUService/GetCourseProductBySKU

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.GetCourseProductBySKUService",
  "method": "GetCourseProductBySKU",
  "input_type": ".chesscom.courses.v1.GetCourseProductBySKURequest",
  "output_type": ".chesscom.courses.v1.GetCourseProductBySKUResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 750411.

```text
EuU2V0VmFyaWF0aW9uVW5wYXVzZWRSZXNwb25zZUIhyrcsHQoEL3JwYxITEhFjb3Vyc2VzLmNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/courses/v1/course_product_by_sku_service.proto":"CjdjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZV9wcm9kdWN0X2J5X3NrdV9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIksKHEdldENvdXJzZVByb2R1Y3RCeVNLVVJlcXVlc3QSCwoDc2t1GAEgASgJEhMKBmxvY2FsZRgCIAEoCUgAiAEBQgkKB19sb2NhbGUiVAodR2V0Q291cnNlUHJvZHVjdEJ5U0tVUmVzcG9uc2USMwoHcHJvZH
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17979"></a>
## FND-17979: Frontend-declared RPC chesscom.courses.v1.CoursesConfigurableUserFlagService/SetConfigurableUserFlag

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesConfigurableUserFlagService",
  "method": "SetConfigurableUserFlag",
  "input_type": ".chesscom.courses.v1.SetConfigurableUserFlagRequest",
  "output_type": ".chesscom.courses.v1.SetConfigurableUserFlagResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 751813.

```text
kxBR19IQVNfU0tJUFBFRF9GVFVFX1NFTEVDVE9SEAoSHwobVVNFUl9GTEFHX0NPQUNIX0RFRkFVTFRfT0ZGEAtiBnByb3RvMw","chesscom/courses/v1/configurable_user_flag_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvbmZpZ3VyYWJsZV91c2VyX2ZsYWdfc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJSCh5TZXRDb25maWd1cmFibGVVc2VyRmxhZ1JlcXVlc3QSMAoJdXNlcl9mbGFnGAEgASgOMh0uY2hlc3Njb20uY291cnNlcy52MS5Vc2VyRmxhZyIhCh9TZXRDb25maWd1cmFibGVVc2VyRmxhZ1Jlc3Bvb
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17981"></a>
## FND-17981: Frontend-declared RPC chesscom.courses.v1.CoursesPreviewsInformationService/GetPreviewsInformation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesPreviewsInformationService",
  "method": "GetPreviewsInformation",
  "input_type": ".chesscom.courses.v1.GetPreviewsInformationRequest",
  "output_type": ".chesscom.courses.v1.GetPreviewsInformationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 752429.

```text
XRDb25maWd1cmFibGVVc2VyRmxhZ1Jlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/courses_previews_information_service.proto":"Cj5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfcHJldmlld3NfaW5mb3JtYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSIfCh1HZXRQcmV2aWV3c0luZm9ybWF0aW9uUmVxdWVzdCLkAQoeR2V0UHJldmlld3NJbmZvcm1hdGlvblJlc3BvbnNlEhMKC3VzZWRfYW1vdW50GAEgASgFEhkKDHRvdGFsX2Ftb3VudBg
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17985"></a>
## FND-17985: Frontend-declared RPC chesscom.courses.v1.CoursesAuthenticationService/AuthenticateForCoursesWithCookie

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesAuthenticationService",
  "method": "AuthenticateForCoursesWithCookie",
  "input_type": ".chesscom.courses.v1.AuthenticateForCoursesWithCookieRequest",
  "output_type": ".chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17986"></a>
## FND-17986: Frontend-declared RPC chesscom.courses.v1.CoursesAuthenticationService/GetOAuthURLForCourses

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesAuthenticationService",
  "method": "GetOAuthURLForCourses",
  "input_type": ".chesscom.courses.v1.GetOAuthURLForCoursesRequest",
  "output_type": ".chesscom.courses.v1.GetOAuthURLForCoursesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17987"></a>
## FND-17987: Frontend-declared RPC chesscom.courses.v1.CoursesAuthenticationService/AuthenticateForCourses

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesAuthenticationService",
  "method": "AuthenticateForCourses",
  "input_type": ".chesscom.courses.v1.AuthenticateForCoursesRequest",
  "output_type": ".chesscom.courses.v1.AuthenticateForCoursesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17988"></a>
## FND-17988: Frontend-declared RPC chesscom.courses.v1.CoursesAuthenticationService/RefreshTokenForCourses

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesAuthenticationService",
  "method": "RefreshTokenForCourses",
  "input_type": ".chesscom.courses.v1.RefreshTokenForCoursesRequest",
  "output_type": ".chesscom.courses.v1.RefreshTokenForCoursesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17989"></a>
## FND-17989: Frontend-declared RPC chesscom.courses.v1.CoursesAuthenticationService/GetUserInfoForCourses

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesAuthenticationService",
  "method": "GetUserInfoForCourses",
  "input_type": ".chesscom.courses.v1.GetUserInfoForCoursesRequest",
  "output_type": ".chesscom.courses.v1.GetUserInfoForCoursesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 753948.

```text
uVGltZXN0YW1wEjUKEXJld2FyZF9jbGFpbWVkX2F0GAUgASgLMhouZ29vZ2xlLnByb3RvYnVmLlRpbWVzdGFtcGIGcHJvdG8z","chesscom/courses/v1/courses_authentication_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfYXV0aGVudGljYXRpb25fc2VydmljZS5wcm90bxITY2hlc3Njb20uY291cnNlcy52MSJVCidBdXRoZW50aWNhdGVGb3JDb3Vyc2VzV2l0aENvb2tpZVJlcXVlc3QSFQoNcHJvdmlkZXJfbmFtZRgBIAEoCRITCgtjb29raWVfbmFtZRgCIAEoCSKjAQooQXV0aGVudGljYXRlRm9yQ291cnNlc1dpd
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17991"></a>
## FND-17991: Frontend-declared RPC chesscom.courses.v1.GetHasUserAccessToSkuService/GetHasUserAccessToSku

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.GetHasUserAccessToSkuService",
  "method": "GetHasUserAccessToSku",
  "input_type": ".chesscom.courses.v1.GetHasUserAccessToSkuRequest",
  "output_type": ".chesscom.courses.v1.GetHasUserAccessToSkuResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 756644.

```text
kdldFVzZXJJbmZvRm9yQ291cnNlc1Jlc3BvbnNlQiHKtywdCgQvcnBjEhMSEWNvdXJzZXMuY2hlc3MuY29tGgBiBnByb3RvMw","chesscom/courses/v1/courses_has_user_access_to_sku_service.proto":"CkBjaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfaGFzX3VzZXJfYWNjZXNzX3RvX3NrdV9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIkUKHEdldEhhc1VzZXJBY2Nlc3NUb1NrdVJlcXVlc3QSGAoQY2hlc3Njb21fdXNlcl9pZBgBIAEoCRILCgNza3UYAiABKAkiMwodR2V0SGFzVXNlckFjY2Vzc1RvU2t1UmVzcG9uc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17998"></a>
## FND-17998: Frontend-declared RPC chesscom.courses.v1.CoursesShopService/GetCourseProductList

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesShopService",
  "method": "GetCourseProductList",
  "input_type": ".chesscom.courses.v1.GetCourseProductListRequest",
  "output_type": ".chesscom.courses.v1.GetCourseProductListResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 758934.

```text
9PUFRJT05fVkFSSUFUSU9OU19ERVNDEAMSJgoiU0hPUF9TT1JUX09QVElPTl9SRUxFQVNFX0RBVEVfREVTQxAEYgZwcm90bzM","chesscom/courses/v1/courses_shop_service.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfc2hvcF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIu8HChtHZXRDb3Vyc2VQcm9kdWN0TGlzdFJlcXVlc3QSQwoKcGFnaW5hdGlvbhgBIAEoCzIqLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlc1Nob3BQYWdpbmF0aW9uSACIAQESGQoMc2VhcmNoX3F1ZXJ5GAIgASgJSAGIAQESRgoMZ2F
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-17999"></a>
## FND-17999: Frontend-declared RPC chesscom.courses.v1.CoursesShopService/GetShopMetadata

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1.CoursesShopService",
  "method": "GetShopMetadata",
  "input_type": ".chesscom.courses.v1.GetShopMetadataRequest",
  "output_type": ".chesscom.courses.v1.GetShopMetadataResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 758934.

```text
9PUFRJT05fVkFSSUFUSU9OU19ERVNDEAMSJgoiU0hPUF9TT1JUX09QVElPTl9SRUxFQVNFX0RBVEVfREVTQxAEYgZwcm90bzM","chesscom/courses/v1/courses_shop_service.proto":"Ci5jaGVzc2NvbS9jb3Vyc2VzL3YxL2NvdXJzZXNfc2hvcF9zZXJ2aWNlLnByb3RvEhNjaGVzc2NvbS5jb3Vyc2VzLnYxIu8HChtHZXRDb3Vyc2VQcm9kdWN0TGlzdFJlcXVlc3QSQwoKcGFnaW5hdGlvbhgBIAEoCzIqLmNoZXNzY29tLmNvdXJzZXMudjEuQ291cnNlc1Nob3BQYWdpbmF0aW9uSACIAQESGQoMc2VhcmNoX3F1ZXJ5GAIgASgJSAGIAQESRgoMZ2F
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18002"></a>
## FND-18002: Frontend-declared RPC chesscom.courses.v1alpha.CourseDeviationsService/GetCourseDeviations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.courses.v1alpha.CourseDeviationsService",
  "method": "GetCourseDeviations",
  "input_type": ".chesscom.courses.v1alpha.GetCourseDeviationsRequest",
  "output_type": ".chesscom.courses.v1alpha.GetCourseDeviationsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 761690.

```text
MKC2F1dGhvcl9uYW1lGAggASgJEhUKDWZlbl9pbl9jb3Vyc2UYCSABKAkSFAoMZmVuX2RldmlhdGVkGAogASgJYgZwcm90bzM","chesscom/courses/v1alpha/course_deviations_service.proto":"CjhjaGVzc2NvbS9jb3Vyc2VzL3YxYWxwaGEvY291cnNlX2RldmlhdGlvbnNfc2VydmljZS5wcm90bxIYY2hlc3Njb20uY291cnNlcy52MWFscGhhIlMKGkdldENvdXJzZURldmlhdGlvbnNSZXF1ZXN0EicKBWNvbG9yGAEgASgOMhguY2hlc3Njb20uY2hlc3MudjEuQ29sb3ISDAoEZmVucxgCIAMoCSJcChtHZXRDb3Vyc2VEZXZpYXRpb25zUmVzc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18009"></a>
## FND-18009: Frontend-declared RPC chesscom.skills.v1.SkillsService/GainSkillPoints

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.skills.v1.SkillsService",
  "method": "GainSkillPoints",
  "input_type": ".chesscom.skills.v1.GainSkillPointsRequest",
  "output_type": ".chesscom.skills.v1.GainSkillPointsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18010"></a>
## FND-18010: Frontend-declared RPC chesscom.skills.v1.SkillsService/GetSkills

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.skills.v1.SkillsService",
  "method": "GetSkills",
  "input_type": ".chesscom.skills.v1.GetSkillsRequest",
  "output_type": ".chesscom.skills.v1.GetSkillsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18011"></a>
## FND-18011: Frontend-declared RPC chesscom.skills.v1.SkillsService/GetSkillsPositions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.skills.v1.SkillsService",
  "method": "GetSkillsPositions",
  "input_type": ".chesscom.skills.v1.GetSkillsPositionsRequest",
  "output_type": ".chesscom.skills.v1.GetSkillsPositionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18012"></a>
## FND-18012: Frontend-declared RPC chesscom.skills.v1.SkillsService/GetConfig

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.skills.v1.SkillsService",
  "method": "GetConfig",
  "input_type": ".chesscom.skills.v1.GetConfigRequest",
  "output_type": ".chesscom.skills.v1.GetConfigResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18013"></a>
## FND-18013: Frontend-declared RPC chesscom.skills.v1.SkillsService/ResetSkills

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.skills.v1.SkillsService",
  "method": "ResetSkills",
  "input_type": ".chesscom.skills.v1.ResetSkillsRequest",
  "output_type": ".chesscom.skills.v1.ResetSkillsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 765586.

```text
pbGxDYXRlZ29yeRIrCgRuYW1lGAIgASgLMh0uY2hlc3Njb20uaTE4bi52MS5UcmFuc2xhdGlvbjoHgqYdAwoBAWIGcHJvdG8z","chesscom/skills/v1/skills_service.proto":"CidjaGVzc2NvbS9za2lsbHMvdjEvc2tpbGxzX3NlcnZpY2UucHJvdG8SEmNoZXNzY29tLnNraWxscy52MSL8AgoWR2FpblNraWxsUG9pbnRzUmVxdWVzdBIPCgdnYW1lX2lkGAEgASgJEkcKD3NraWxsX3Bvc2l0aW9ucxgCIAMoCzIuLmNoZXNzY29tLmV4cGxhbmF0aW9uX2VuZ2luZS52MS5Ta2lsbHNQb3NpdGlvbhJMCgtjb2FjaF9pbnB1dBgDIAEoCzI1LmNoZXNzY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18036"></a>
## FND-18036: Frontend-declared RPC chesscom.payments.v1.BillingService/GetUserBillingHistory

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.BillingService",
  "method": "GetUserBillingHistory",
  "input_type": ".chesscom.payments.v1.GetUserBillingHistoryRequest",
  "output_type": ".chesscom.payments.v1.GetUserBillingHistoryResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 806250.

```text
0hpc3RvcnlFbnRyeVVzZXISEAoIdXNlcm5hbWUYASABKAkSEgoFZW1haWwYAiABKAlIAIgBAUIICgZfZW1haWxiBnByb3RvMw","chesscom/payments/v1/billing_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9iaWxsaW5nX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIh4KHEdldFVzZXJCaWxsaW5nSGlzdG9yeVJlcXVlc3QiYwodR2V0VXNlckJpbGxpbmdIaXN0b3J5UmVzcG9uc2USQgoPYmlsbGluZ19oaXN0b3J5GAEgAygLMikuY2hlc3Njb20ucGF5bWVudHMudjEuQmlsbGluZ0hpc3RvcnlFbnRyeSIiCiBHZXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18037"></a>
## FND-18037: Frontend-declared RPC chesscom.payments.v1.BillingService/GetUserBillingInformation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.BillingService",
  "method": "GetUserBillingInformation",
  "input_type": ".chesscom.payments.v1.GetUserBillingInformationRequest",
  "output_type": ".chesscom.payments.v1.GetUserBillingInformationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 806250.

```text
0hpc3RvcnlFbnRyeVVzZXISEAoIdXNlcm5hbWUYASABKAkSEgoFZW1haWwYAiABKAlIAIgBAUIICgZfZW1haWxiBnByb3RvMw","chesscom/payments/v1/billing_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9iaWxsaW5nX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIh4KHEdldFVzZXJCaWxsaW5nSGlzdG9yeVJlcXVlc3QiYwodR2V0VXNlckJpbGxpbmdIaXN0b3J5UmVzcG9uc2USQgoPYmlsbGluZ19oaXN0b3J5GAEgAygLMikuY2hlc3Njb20ucGF5bWVudHMudjEuQmlsbGluZ0hpc3RvcnlFbnRyeSIiCiBHZXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18038"></a>
## FND-18038: Frontend-declared RPC chesscom.payments.v1.BillingService/GetOrderInvoice

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.BillingService",
  "method": "GetOrderInvoice",
  "input_type": ".chesscom.payments.v1.GetOrderInvoiceRequest",
  "output_type": ".chesscom.payments.v1.GetOrderInvoiceResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 806250.

```text
0hpc3RvcnlFbnRyeVVzZXISEAoIdXNlcm5hbWUYASABKAkSEgoFZW1haWwYAiABKAlIAIgBAUIICgZfZW1haWxiBnByb3RvMw","chesscom/payments/v1/billing_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9iaWxsaW5nX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIh4KHEdldFVzZXJCaWxsaW5nSGlzdG9yeVJlcXVlc3QiYwodR2V0VXNlckJpbGxpbmdIaXN0b3J5UmVzcG9uc2USQgoPYmlsbGluZ19oaXN0b3J5GAEgAygLMikuY2hlc3Njb20ucGF5bWVudHMudjEuQmlsbGluZ0hpc3RvcnlFbnRyeSIiCiBHZXR
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18042"></a>
## FND-18042: Frontend-declared RPC chesscom.payments.v1.RefundService/IssueRefund

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.RefundService",
  "method": "IssueRefund",
  "input_type": ".chesscom.payments.v1.IssueRefundRequest",
  "output_type": ".chesscom.payments.v1.IssueRefundResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 811232.

```text
IvLmNoZXNzY29tLnBheW1lbnRzLnYxLlN1YnNjcmlwdGlvblBheW1lbnRTdGF0dXNCDgoMX3ByaWNlX2NlbnRzYgZwcm90bzM","chesscom/payments/v1/refund_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9yZWZ1bmRfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi/QEKEklzc3VlUmVmdW5kUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSEQoJY2hhcmdlX2lkGAIgASgJEhQKDGFtb3VudF9jZW50cxgEIAEoBRI6Cgdjb250ZXh0GAYgASgLMikuY2hlc3Njb20uc3VwcG9ydC52MS5TdXBwb3J0QWN0aW9uQ29udGV4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18043"></a>
## FND-18043: Frontend-declared RPC chesscom.payments.v1.RefundService/ListCharges

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.RefundService",
  "method": "ListCharges",
  "input_type": ".chesscom.payments.v1.ListChargesRequest",
  "output_type": ".chesscom.payments.v1.ListChargesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 811232.

```text
IvLmNoZXNzY29tLnBheW1lbnRzLnYxLlN1YnNjcmlwdGlvblBheW1lbnRTdGF0dXNCDgoMX3ByaWNlX2NlbnRzYgZwcm90bzM","chesscom/payments/v1/refund_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9yZWZ1bmRfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi/QEKEklzc3VlUmVmdW5kUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSEQoJY2hhcmdlX2lkGAIgASgJEhQKDGFtb3VudF9jZW50cxgEIAEoBRI6Cgdjb250ZXh0GAYgASgLMikuY2hlc3Njb20uc3VwcG9ydC52MS5TdXBwb3J0QWN0aW9uQ29udGV4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18044"></a>
## FND-18044: Frontend-declared RPC chesscom.payments.v1.RefundService/FindCharges

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.RefundService",
  "method": "FindCharges",
  "input_type": ".chesscom.payments.v1.FindChargesRequest",
  "output_type": ".chesscom.payments.v1.FindChargesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 811232.

```text
IvLmNoZXNzY29tLnBheW1lbnRzLnYxLlN1YnNjcmlwdGlvblBheW1lbnRTdGF0dXNCDgoMX3ByaWNlX2NlbnRzYgZwcm90bzM","chesscom/payments/v1/refund_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9yZWZ1bmRfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi/QEKEklzc3VlUmVmdW5kUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSEQoJY2hhcmdlX2lkGAIgASgJEhQKDGFtb3VudF9jZW50cxgEIAEoBRI6Cgdjb250ZXh0GAYgASgLMikuY2hlc3Njb20uc3VwcG9ydC52MS5TdXBwb3J0QWN0aW9uQ29udGV4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18045"></a>
## FND-18045: Frontend-declared RPC chesscom.payments.v1.RefundService/ListSubscriptions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.RefundService",
  "method": "ListSubscriptions",
  "input_type": ".chesscom.payments.v1.ListSubscriptionsRequest",
  "output_type": ".chesscom.payments.v1.ListSubscriptionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 811232.

```text
IvLmNoZXNzY29tLnBheW1lbnRzLnYxLlN1YnNjcmlwdGlvblBheW1lbnRTdGF0dXNCDgoMX3ByaWNlX2NlbnRzYgZwcm90bzM","chesscom/payments/v1/refund_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9yZWZ1bmRfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEi/QEKEklzc3VlUmVmdW5kUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSEQoJY2hhcmdlX2lkGAIgASgJEhQKDGFtb3VudF9jZW50cxgEIAEoBRI6Cgdjb250ZXh0GAYgASgLMikuY2hlc3Njb20uc3VwcG9ydC52MS5TdXBwb3J0QWN0aW9uQ29udGV4
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.
