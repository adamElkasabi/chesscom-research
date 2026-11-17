# External services and dependencies

[Master index](00_MASTER_INDEX.md)

Every literal external URL is retained in the global registry with all source occurrences. Known source-level integrations include Turnstile,consent scripts,Sentry/analytics/ads,chess asset hosts,Vue/Pinia vendor bundles and npm/GitHub package metadata. Embedded metadata does not confer repository access or prove a service was contacted in a particular runtime session.

[Complete URL registry](16_URL_AND_REFERENCE_INDEX.md)

## Detailed findings

- [FND-18979](findings/external_services-001.md#FND-18979) — Third-party integrations are declared in saved public page assets
