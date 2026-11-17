# Infrastructure and deployment

[Master index](00_MASTER_INDEX.md)

Historical asset probes preserve exact URLs/status/content type/download size. Range206/onebyte must not be confused with a complete engine file. Versioned/hash package paths and production/staging/sandbox endpoints are exposed deployment evidence; provider,DNS/TLSdetails,cacheheaderpolicyanddatabasehostingwere not established.


## Detailed findings

- [FND-18975](findings/infrastructure-001.md#FND-18975) — Asset probe status206was a deliberate byte-range request
- [FND-18976](findings/infrastructure-001.md#FND-18976) — Torch multipart loader explains some guessed-path404s
- [FND-18977](findings/infrastructure-001.md#FND-18977) — Dependency delivery is versioned and hashed
- [FND-18978](findings/infrastructure-001.md#FND-18978) — Frontend libraries do not identify the backend
