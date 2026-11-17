# api_schema_services — findings 201–241

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18048"></a>
## FND-18048: Frontend-declared RPC chesscom.payments.v1.ProductService/GetUserActiveMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.ProductService",
  "method": "GetUserActiveMembership",
  "input_type": ".chesscom.payments.v1.GetUserActiveMembershipRequest",
  "output_type": ".chesscom.payments.v1.GetUserActiveMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 827574.

```text
NISVBfVFlQRV9QUklNQVJZEAESIwofR1JPVVBfTUVNQkVSU0hJUF9UWVBFX1NFQ09OREFSWRACGgeKph0DCgEBYgZwcm90bzM","chesscom/payments/v1/product_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIikKHkdldFVzZXJBY3RpdmVNZW1iZXJzaGlwUmVxdWVzdDoHgqYdAwoBASLxBwofR2V0VXNlckFjdGl2ZU1lbWJlcnNoaXBSZXNwb25zZRI/ChBtZW1iZXJzaGlwX2xldmVsGAEgASgOMiUuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcEx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18049"></a>
## FND-18049: Frontend-declared RPC chesscom.payments.v1.ProductService/GetUserIsEligibleToRestartMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.ProductService",
  "method": "GetUserIsEligibleToRestartMembership",
  "input_type": ".chesscom.payments.v1.GetUserIsEligibleToRestartMembershipRequest",
  "output_type": ".chesscom.payments.v1.GetUserIsEligibleToRestartMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 827574.

```text
NISVBfVFlQRV9QUklNQVJZEAESIwofR1JPVVBfTUVNQkVSU0hJUF9UWVBFX1NFQ09OREFSWRACGgeKph0DCgEBYgZwcm90bzM","chesscom/payments/v1/product_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIikKHkdldFVzZXJBY3RpdmVNZW1iZXJzaGlwUmVxdWVzdDoHgqYdAwoBASLxBwofR2V0VXNlckFjdGl2ZU1lbWJlcnNoaXBSZXNwb25zZRI/ChBtZW1iZXJzaGlwX2xldmVsGAEgASgOMiUuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcEx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18050"></a>
## FND-18050: Frontend-declared RPC chesscom.payments.v1.ProductService/RestartMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.ProductService",
  "method": "RestartMembership",
  "input_type": ".chesscom.payments.v1.RestartMembershipRequest",
  "output_type": ".chesscom.payments.v1.RestartMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 827574.

```text
NISVBfVFlQRV9QUklNQVJZEAESIwofR1JPVVBfTUVNQkVSU0hJUF9UWVBFX1NFQ09OREFSWRACGgeKph0DCgEBYgZwcm90bzM","chesscom/payments/v1/product_service.proto":"CipjaGVzc2NvbS9wYXltZW50cy92MS9wcm9kdWN0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIikKHkdldFVzZXJBY3RpdmVNZW1iZXJzaGlwUmVxdWVzdDoHgqYdAwoBASLxBwofR2V0VXNlckFjdGl2ZU1lbWJlcnNoaXBSZXNwb25zZRI/ChBtZW1iZXJzaGlwX2xldmVsGAEgASgOMiUuY2hlc3Njb20ucGF5bWVudHMudjEuTWVtYmVyc2hpcEx
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18053"></a>
## FND-18053: Frontend-declared RPC chesscom.payments.v1.MembershipService/CancelMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.MembershipService",
  "method": "CancelMembership",
  "input_type": ".chesscom.payments.v1.CancelMembershipRequest",
  "output_type": ".chesscom.payments.v1.CancelMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 832105.

```text
mVyGAIgASgJSACIAQESFwoKb3duZXJfbmFtZRgDIAEoCUgBiAEBQgkKB19udW1iZXJCDQoLX293bmVyX25hbWViBnByb3RvMw","chesscom/payments/v1/membership_service.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIhkKF0NhbmNlbE1lbWJlcnNoaXBSZXF1ZXN0IhoKGENhbmNlbE1lbWJlcnNoaXBSZXNwb25zZSJ/Ch9TdWJtaXRDYW5jZWxsYXRpb25TdXJ2ZXlSZXF1ZXN0EjgKBnJlYXNvbhgBIAEoDjIoLmNoZXNzY29tLnBheW1lbnRzLnYxLkNhbmNl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18054"></a>
## FND-18054: Frontend-declared RPC chesscom.payments.v1.MembershipService/SubmitCancellationSurvey

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.MembershipService",
  "method": "SubmitCancellationSurvey",
  "input_type": ".chesscom.payments.v1.SubmitCancellationSurveyRequest",
  "output_type": ".chesscom.payments.v1.SubmitCancellationSurveyResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 832105.

```text
mVyGAIgASgJSACIAQESFwoKb3duZXJfbmFtZRgDIAEoCUgBiAEBQgkKB19udW1iZXJCDQoLX293bmVyX25hbWViBnByb3RvMw","chesscom/payments/v1/membership_service.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIhkKF0NhbmNlbE1lbWJlcnNoaXBSZXF1ZXN0IhoKGENhbmNlbE1lbWJlcnNoaXBSZXNwb25zZSJ/Ch9TdWJtaXRDYW5jZWxsYXRpb25TdXJ2ZXlSZXF1ZXN0EjgKBnJlYXNvbhgBIAEoDjIoLmNoZXNzY29tLnBheW1lbnRzLnYxLkNhbmNl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18055"></a>
## FND-18055: Frontend-declared RPC chesscom.payments.v1.MembershipService/ExtendMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.MembershipService",
  "method": "ExtendMembership",
  "input_type": ".chesscom.payments.v1.ExtendMembershipRequest",
  "output_type": ".chesscom.payments.v1.ExtendMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 832105.

```text
mVyGAIgASgJSACIAQESFwoKb3duZXJfbmFtZRgDIAEoCUgBiAEBQgkKB19udW1iZXJCDQoLX293bmVyX25hbWViBnByb3RvMw","chesscom/payments/v1/membership_service.proto":"Ci1jaGVzc2NvbS9wYXltZW50cy92MS9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIhkKF0NhbmNlbE1lbWJlcnNoaXBSZXF1ZXN0IhoKGENhbmNlbE1lbWJlcnNoaXBSZXNwb25zZSJ/Ch9TdWJtaXRDYW5jZWxsYXRpb25TdXJ2ZXlSZXF1ZXN0EjgKBnJlYXNvbhgBIAEoDjIoLmNoZXNzY29tLnBheW1lbnRzLnYxLkNhbmNl
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18059"></a>
## FND-18059: Frontend-declared RPC chesscom.payments.v1.SupportPromotionService/CheckMemberPromotions

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SupportPromotionService",
  "method": "CheckMemberPromotions",
  "input_type": ".chesscom.payments.v1.CheckMemberPromotionsRequest",
  "output_type": ".chesscom.payments.v1.CheckMemberPromotionsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 835735.

```text
Vwb25fY29kZV91c2VkGAQgASgIEisKCHBsYXRmb3JtGAUgASgOMhkuY2hlc3Njb20uYXBpLnYxLlBsYXRmb3JtYgZwcm90bzM","chesscom/payments/v1/support_promotion_service.proto":"CjRjaGVzc2NvbS9wYXltZW50cy92MS9zdXBwb3J0X3Byb21vdGlvbl9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLMAQocQ2hlY2tNZW1iZXJQcm9tb3Rpb25zUmVxdWVzdBIRCgl1c2VyX3V1aWQYASABKAkSFwoEY29kZRgCIAEoCUIJgAEByrsYAggDEjoKB2NvbnRleHQYAyABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvc
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18063"></a>
## FND-18063: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/CancelSubscription

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "CancelSubscription",
  "input_type": ".chesscom.payments.v1.CancelSubscriptionRequest",
  "output_type": ".chesscom.payments.v1.CancelSubscriptionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18064"></a>
## FND-18064: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/StopRenewalByCardMatch

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "StopRenewalByCardMatch",
  "input_type": ".chesscom.payments.v1.StopRenewalByCardMatchRequest",
  "output_type": ".chesscom.payments.v1.StopRenewalByCardMatchResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18065"></a>
## FND-18065: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/ExtendSubscription

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "ExtendSubscription",
  "input_type": ".chesscom.payments.v1.ExtendSubscriptionRequest",
  "output_type": ".chesscom.payments.v1.ExtendSubscriptionResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18066"></a>
## FND-18066: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/GrantGoodwillDiamond

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "GrantGoodwillDiamond",
  "input_type": ".chesscom.payments.v1.GrantGoodwillDiamondRequest",
  "output_type": ".chesscom.payments.v1.GrantGoodwillDiamondResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18067"></a>
## FND-18067: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/GrantNoAdsOffer

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "GrantNoAdsOffer",
  "input_type": ".chesscom.payments.v1.GrantNoAdsOfferRequest",
  "output_type": ".chesscom.payments.v1.GrantNoAdsOfferResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18068"></a>
## FND-18068: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/TransferMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "TransferMembership",
  "input_type": ".chesscom.payments.v1.TransferMembershipRequest",
  "output_type": ".chesscom.payments.v1.TransferMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18069"></a>
## FND-18069: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/GrantMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "GrantMembership",
  "input_type": ".chesscom.payments.v1.GrantMembershipRequest",
  "output_type": ".chesscom.payments.v1.GrantMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18070"></a>
## FND-18070: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/SwitchToMonthly

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "SwitchToMonthly",
  "input_type": ".chesscom.payments.v1.SwitchToMonthlyRequest",
  "output_type": ".chesscom.payments.v1.SwitchToMonthlyResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18071"></a>
## FND-18071: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/GetFamilyPlanInvitations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "GetFamilyPlanInvitations",
  "input_type": ".chesscom.payments.v1.GetFamilyPlanInvitationsRequest",
  "output_type": ".chesscom.payments.v1.GetFamilyPlanInvitationsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18072"></a>
## FND-18072: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/RevokeFamilyPlanInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "RevokeFamilyPlanInvitation",
  "input_type": ".chesscom.payments.v1.RevokeFamilyPlanInvitationRequest",
  "output_type": ".chesscom.payments.v1.RevokeFamilyPlanInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18073"></a>
## FND-18073: Frontend-declared RPC chesscom.payments.v1.SubscriptionAdminService/ClearFamilyPlanTrialCooldown

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.SubscriptionAdminService",
  "method": "ClearFamilyPlanTrialCooldown",
  "input_type": ".chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest",
  "output_type": ".chesscom.payments.v1.ClearFamilyPlanTrialCooldownResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 841881.

```text
F9ESUFNT05EX1NUQVJURUQQARIsCihHUkFOVF9HT09EV0lMTF9ESUFNT05EX1JFU1VMVF9EQVlTX0FEREVEEAJiBnByb3RvMw","chesscom/payments/v1/subscription_admin_service.proto":"CjVjaGVzc2NvbS9wYXltZW50cy92MS9zdWJzY3JpcHRpb25fYWRtaW5fc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEigwEKGUNhbmNlbFN1YnNjcmlwdGlvblJlcXVlc3QSEQoJdXNlcl91dWlkGAEgASgJEjoKB2NvbnRleHQYAiABKAsyKS5jaGVzc2NvbS5zdXBwb3J0LnYxLlN1cHBvcnRBY3Rpb25Db250ZXh0EhcKD3N1YnNjcmlw
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18075"></a>
## FND-18075: Frontend-declared RPC chesscom.payments.v1.PricesService/GetPriceForAllCountries

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.PricesService",
  "method": "GetPriceForAllCountries",
  "input_type": ".chesscom.payments.v1.GetPriceForAllCountriesRequest",
  "output_type": ".chesscom.payments.v1.GetPriceForAllCountriesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 897016.

```text
gcmVmdW5kMghjaGVzc2NvbUIuyrcsKgoEL3JwYxIPEg1hcGkuY2hlc3MuY29tGg0SC2JlYXJlcl9hdXRoKgKQTmIGcHJvdG8z","chesscom/payments/v1/prices_service.proto":"CiljaGVzc2NvbS9wYXltZW50cy92MS9wcmljZXNfc2VydmljZS5wcm90bxIUY2hlc3Njb20ucGF5bWVudHMudjEiLQoeR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXF1ZXN0EgsKA3NrdRgBIAMoCSJfCh9HZXRQcmljZUZvckFsbENvdW50cmllc1Jlc3BvbnNlEjwKD3Byb2R1Y3RzX3ByaWNlcxgBIAMoCzIjLmNoZXNzY29tLnBheW1lbnRzLnYxLlByb2R1Y3RQcmlj
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18077"></a>
## FND-18077: Frontend-declared RPC chesscom.payments.v1.CheckoutService/GetTotalBySku

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.CheckoutService",
  "method": "GetTotalBySku",
  "input_type": ".chesscom.payments.v1.GetTotalBySkuRequest",
  "output_type": ".chesscom.payments.v1.GetTotalBySkuResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 897603.

```text
uR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXNwb25zZSIAQh3KtywZCgQvcnBjEg8SDXd3dy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/checkout_service.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLgAgoUR2V0VG90YWxCeVNrdVJlcXVlc3QSCwoDc2t1GAEgASgJEhgKC2NvdXBvbl9jb2RlGAIgASgJSACIAQESRAoQcmVxdWVzdF9sb2NhdGlvbhgDIAEoCzIlLmNoZXNzY29tLnBheW1lbnRzLnYxLlJlcXVlc3RMb2NhdGlvbkgBiAEBEkAKDn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18078"></a>
## FND-18078: Frontend-declared RPC chesscom.payments.v1.CheckoutService/GetTotalBySkuList

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.CheckoutService",
  "method": "GetTotalBySkuList",
  "input_type": ".chesscom.payments.v1.GetTotalBySkuListRequest",
  "output_type": ".chesscom.payments.v1.GetTotalBySkuListResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 897603.

```text
uR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXNwb25zZSIAQh3KtywZCgQvcnBjEg8SDXd3dy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/checkout_service.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLgAgoUR2V0VG90YWxCeVNrdVJlcXVlc3QSCwoDc2t1GAEgASgJEhgKC2NvdXBvbl9jb2RlGAIgASgJSACIAQESRAoQcmVxdWVzdF9sb2NhdGlvbhgDIAEoCzIlLmNoZXNzY29tLnBheW1lbnRzLnYxLlJlcXVlc3RMb2NhdGlvbkgBiAEBEkAKDn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18079"></a>
## FND-18079: Frontend-declared RPC chesscom.payments.v1.CheckoutService/GetStorefrontDetails

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.CheckoutService",
  "method": "GetStorefrontDetails",
  "input_type": ".chesscom.payments.v1.GetStorefrontDetailsRequest",
  "output_type": ".chesscom.payments.v1.GetStorefrontDetailsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 897603.

```text
uR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXNwb25zZSIAQh3KtywZCgQvcnBjEg8SDXd3dy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/checkout_service.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLgAgoUR2V0VG90YWxCeVNrdVJlcXVlc3QSCwoDc2t1GAEgASgJEhgKC2NvdXBvbl9jb2RlGAIgASgJSACIAQESRAoQcmVxdWVzdF9sb2NhdGlvbhgDIAEoCzIlLmNoZXNzY29tLnBheW1lbnRzLnYxLlJlcXVlc3RMb2NhdGlvbkgBiAEBEkAKDn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18080"></a>
## FND-18080: Frontend-declared RPC chesscom.payments.v1.CheckoutService/GetAvailablePaymentMethods

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.CheckoutService",
  "method": "GetAvailablePaymentMethods",
  "input_type": ".chesscom.payments.v1.GetAvailablePaymentMethodsRequest",
  "output_type": ".chesscom.payments.v1.GetAvailablePaymentMethodsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 897603.

```text
uR2V0UHJpY2VGb3JBbGxDb3VudHJpZXNSZXNwb25zZSIAQh3KtywZCgQvcnBjEg8SDXd3dy5jaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/checkout_service.proto":"CitjaGVzc2NvbS9wYXltZW50cy92MS9jaGVja291dF9zZXJ2aWNlLnByb3RvEhRjaGVzc2NvbS5wYXltZW50cy52MSLgAgoUR2V0VG90YWxCeVNrdVJlcXVlc3QSCwoDc2t1GAEgASgJEhgKC2NvdXBvbl9jb2RlGAIgASgJSACIAQESRAoQcmVxdWVzdF9sb2NhdGlvbhgDIAEoCzIlLmNoZXNzY29tLnBheW1lbnRzLnYxLlJlcXVlc3RMb2NhdGlvbkgBiAEBEkAKDn
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18082"></a>
## FND-18082: Frontend-declared RPC chesscom.payments.v1.GiftService/ListEligibleGiftRecipients

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GiftService",
  "method": "ListEligibleGiftRecipients",
  "input_type": ".chesscom.payments.v1.ListEligibleGiftRecipientsRequest",
  "output_type": ".chesscom.payments.v1.ListEligibleGiftRecipientsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900316.

```text
xLkdldEF2YWlsYWJsZVBheW1lbnRNZXRob2RzUmVzcG9uc2UiAEIZyrcsFQoEL3JwYxILEgljaGVzcy5jb20aAGIGcHJvdG8z","chesscom/payments/v1/gift_service.proto":"CidjaGVzc2NvbS9wYXltZW50cy92MS9naWZ0X3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIngKIUxpc3RFbGlnaWJsZUdpZnRSZWNpcGllbnRzUmVxdWVzdBISCgp1c2VyX3V1aWRzGAEgAygJEjMKB3Byb2R1Y3QYAiABKAsyHS5jaGVzc2NvbS5wYXltZW50cy52MS5Qcm9kdWN0SACIAQFCCgoIX3Byb2R1Y3QiQQoiTGlzdEVsaWdpYmxlR2lmdFJlY2
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18084"></a>
## FND-18084: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/GenerateInvitationLink

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "GenerateInvitationLink",
  "input_type": ".chesscom.payments.v1.GenerateInvitationLinkRequest",
  "output_type": ".chesscom.payments.v1.GenerateInvitationLinkResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18085"></a>
## FND-18085: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/CheckJoinEligibility

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "CheckJoinEligibility",
  "input_type": ".chesscom.payments.v1.CheckJoinEligibilityRequest",
  "output_type": ".chesscom.payments.v1.CheckJoinEligibilityResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18086"></a>
## FND-18086: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/InviteMember

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "InviteMember",
  "input_type": ".chesscom.payments.v1.InviteMemberRequest",
  "output_type": ".chesscom.payments.v1.InviteMemberResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18087"></a>
## FND-18087: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/RemoveMember

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "RemoveMember",
  "input_type": ".chesscom.payments.v1.RemoveMemberRequest",
  "output_type": ".chesscom.payments.v1.RemoveMemberResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18088"></a>
## FND-18088: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/GetMaxSecondaryMembers

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "GetMaxSecondaryMembers",
  "input_type": ".chesscom.payments.v1.GetMaxSecondaryMembersRequest",
  "output_type": ".chesscom.payments.v1.GetMaxSecondaryMembersResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18089"></a>
## FND-18089: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/GetSecondaryMembers

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "GetSecondaryMembers",
  "input_type": ".chesscom.payments.v1.GetSecondaryMembersRequest",
  "output_type": ".chesscom.payments.v1.GetSecondaryMembersResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18090"></a>
## FND-18090: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/LeaveGroupMembership

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "LeaveGroupMembership",
  "input_type": ".chesscom.payments.v1.LeaveGroupMembershipRequest",
  "output_type": ".chesscom.payments.v1.LeaveGroupMembershipResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18091"></a>
## FND-18091: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/PreviewInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "PreviewInvitation",
  "input_type": ".chesscom.payments.v1.PreviewInvitationRequest",
  "output_type": ".chesscom.payments.v1.PreviewInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18092"></a>
## FND-18092: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/JoinGroupFromInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "JoinGroupFromInvitation",
  "input_type": ".chesscom.payments.v1.JoinGroupFromInvitationRequest",
  "output_type": ".chesscom.payments.v1.JoinGroupFromInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18093"></a>
## FND-18093: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/ListPendingInvitations

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "ListPendingInvitations",
  "input_type": ".chesscom.payments.v1.ListPendingInvitationsRequest",
  "output_type": ".chesscom.payments.v1.ListPendingInvitationsResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18094"></a>
## FND-18094: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/DeclineInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "DeclineInvitation",
  "input_type": ".chesscom.payments.v1.DeclineInvitationRequest",
  "output_type": ".chesscom.payments.v1.DeclineInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18095"></a>
## FND-18095: Frontend-declared RPC chesscom.payments.v1.GroupMembershipService/RevokeInvitation

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.payments.v1.GroupMembershipService",
  "method": "RevokeInvitation",
  "input_type": ".chesscom.payments.v1.RevokeInvitationRequest",
  "output_type": ".chesscom.payments.v1.RevokeInvitationResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 900960.

```text
52MS5MaXN0RWxpZ2libGVHaWZ0UmVjaXBpZW50c1Jlc3BvbnNlQhnKtywVCgQvcnBjEgsSCWNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/payments/v1/group_membership_service.proto":"CjNjaGVzc2NvbS9wYXltZW50cy92MS9ncm91cF9tZW1iZXJzaGlwX3NlcnZpY2UucHJvdG8SFGNoZXNzY29tLnBheW1lbnRzLnYxIigKHUdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXF1ZXN0OgeCph0DCgEBIkIKHkdlbmVyYXRlSW52aXRhdGlvbkxpbmtSZXNwb25zZRIXCg9pbnZpdGF0aW9uX2xpbmsYASABKAk6B4KmHQMKAQEiWgobQ2hlY2tKb2luRW
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18098"></a>
## FND-18098: Frontend-declared RPC chesscom.user_profile.v1.SocialService/ListFollowedUsers

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_profile.v1.SocialService",
  "method": "ListFollowedUsers",
  "input_type": ".chesscom.user_profile.v1.ListFollowedUsersRequest",
  "output_type": ".chesscom.user_profile.v1.ListFollowedUsersResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 905723.

```text
SEAoIdXNlcm5hbWUYAiABKAkSDgoGYXZhdGFyGAMgASgJEhQKDGNvdW50cnlfY29kZRgEIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/user_profile/v1/social_service.proto":"Ci1jaGVzc2NvbS91c2VyX3Byb2ZpbGUvdjEvc29jaWFsX3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfcHJvZmlsZS52MSKfAQoYTGlzdEZvbGxvd2VkVXNlcnNSZXF1ZXN0EjsKCnBhZ2luYXRpb24YASABKAsyIi5jaGVzc2NvbS5hcGkudjEuUmVxdWVzdFBhZ2luYXRpb25IAIgBARIbCg5yZXF1ZXN0ZXJfdXVpZBgCIAEoCUgBiAEBOgeCph0DCgEBQg0K
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18099"></a>
## FND-18099: Frontend-declared RPC chesscom.user_profile.v1.SocialService/DoesUserFollowOtherUsers

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.user_profile.v1.SocialService",
  "method": "DoesUserFollowOtherUsers",
  "input_type": ".chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest",
  "output_type": ".chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 905723.

```text
SEAoIdXNlcm5hbWUYAiABKAkSDgoGYXZhdGFyGAMgASgJEhQKDGNvdW50cnlfY29kZRgEIAEoCToHgqYdAwoBAWIGcHJvdG8z","chesscom/user_profile/v1/social_service.proto":"Ci1jaGVzc2NvbS91c2VyX3Byb2ZpbGUvdjEvc29jaWFsX3NlcnZpY2UucHJvdG8SGGNoZXNzY29tLnVzZXJfcHJvZmlsZS52MSKfAQoYTGlzdEZvbGxvd2VkVXNlcnNSZXF1ZXN0EjsKCnBhZ2luYXRpb24YASABKAsyIi5jaGVzc2NvbS5hcGkudjEuUmVxdWVzdFBhZ2luYXRpb25IAIgBARIbCg5yZXF1ZXN0ZXJfdXVpZBgCIAEoCUgBiAEBOgeCph0DCgEBQg0K
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18102"></a>
## FND-18102: Frontend-declared RPC chesscom.inbox.v1.UserMessageService/BatchSendUserMessage

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.inbox.v1.UserMessageService",
  "method": "BatchSendUserMessage",
  "input_type": ".chesscom.inbox.v1.BatchSendUserMessageRequest",
  "output_type": ".chesscom.inbox.v1.BatchSendUserMessageResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 908149.

```text
ERVJfUFJJVkFDWRAIEjIKLk1FU1NBR0VfU0VORF9OT1RfQUxMT1dFRF9SRUFTT05fQ09OVEVOVF9ISURERU4QCWIGcHJvdG8z","chesscom/inbox/v1/user_message_service.proto":"CixjaGVzc2NvbS9pbmJveC92MS91c2VyX21lc3NhZ2Vfc2VydmljZS5wcm90bxIRY2hlc3Njb20uaW5ib3gudjEipAEKG0JhdGNoU2VuZFVzZXJNZXNzYWdlUmVxdWVzdBIYChBzZW5kZXJfdXNlcl91dWlkGAEgASgJEhwKFHJlY2lwaWVudF91c2VyX3V1aWRzGAIgAygJEhQKDG1lc3NhZ2VfdGV4dBgDIAEoCRI3Cgdjb250ZXh0GAQgASgOMiYuY2hlc3Njb20ua
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18103"></a>
## FND-18103: Frontend-declared RPC chesscom.inbox.v1.UserMessageService/CheckCanSendUserMessage

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.inbox.v1.UserMessageService",
  "method": "CheckCanSendUserMessage",
  "input_type": ".chesscom.inbox.v1.CheckCanSendUserMessageRequest",
  "output_type": ".chesscom.inbox.v1.CheckCanSendUserMessageResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 908149.

```text
ERVJfUFJJVkFDWRAIEjIKLk1FU1NBR0VfU0VORF9OT1RfQUxMT1dFRF9SRUFTT05fQ09OVEVOVF9ISURERU4QCWIGcHJvdG8z","chesscom/inbox/v1/user_message_service.proto":"CixjaGVzc2NvbS9pbmJveC92MS91c2VyX21lc3NhZ2Vfc2VydmljZS5wcm90bxIRY2hlc3Njb20uaW5ib3gudjEipAEKG0JhdGNoU2VuZFVzZXJNZXNzYWdlUmVxdWVzdBIYChBzZW5kZXJfdXNlcl91dWlkGAEgASgJEhwKFHJlY2lwaWVudF91c2VyX3V1aWRzGAIgAygJEhQKDG1lc3NhZ2VfdGV4dBgDIAEoCRI3Cgdjb250ZXh0GAQgASgOMiYuY2hlc3Njb20ua
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.

<a id="FND-18105"></a>
## FND-18105: Frontend-declared RPC chesscom.audiences.v1.AuthenticatedAudiencesService/IsAuthenticatedUserInAudiences

**Category:** api_schema_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "service": "chesscom.audiences.v1.AuthenticatedAudiencesService",
  "method": "IsAuthenticatedUserInAudiences",
  "input_type": ".chesscom.audiences.v1.IsAuthenticatedUserInAudiencesRequest",
  "output_type": ".chesscom.audiences.v1.IsAuthenticatedUserInAudiencesResponse",
  "client_streaming": false,
  "server_streaming": false,
  "source_id": "SRC-0045",
  "source_format": "frontend FileDescriptorProto"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 909478.

```text
Vja0NhblNlbmRVc2VyTWVzc2FnZVJlc3BvbnNlIgOQAgFCHcq3LBkKBC9ycGMSDxINd3d3LmNoZXNzLmNvbRoAYgZwcm90bzM","chesscom/audiences/v1/authenticated_audiences_service.proto":"CjtjaGVzc2NvbS9hdWRpZW5jZXMvdjEvYXV0aGVudGljYXRlZF9hdWRpZW5jZXNfc2VydmljZS5wcm90bxIVY2hlc3Njb20uYXVkaWVuY2VzLnYxIkcKJUlzQXV0aGVudGljYXRlZFVzZXJJbkF1ZGllbmNlc1JlcXVlc3QSFQoNYXVkaWVuY2Vfa2V5cxgBIAMoCToHgqYdAwoBASLIAQomSXNBdXRoZW50aWNhdGVkVXNlckluQXVkaWVuY2VzUm
```

**Source references:** SRC-0045  
**URL references:** None independently associated  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** Service method recovered offline from original descriptor; URL/auth/runtime invocation not established by this declaration alone.
