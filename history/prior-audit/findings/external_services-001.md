# external_services — findings 1–1

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18979"></a>
## FND-18979: Third-party integrations are declared in saved public page assets

**Category:** external_services  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved HTML/code references Cloudflare Turnstile,cookie-consent scripts,analytics/ads/Sentry and chess static asset hosts. URL registry retains each literal and its provenance. Script inclusion is not a full runtime network capture or proof every service executes for every user.

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 21842.

```text
lessons_extend_user_activity_with_parent_and_configuration', 'library_redirect_to_analysis', 'login_turnstile', 'onetrust_cookie_consent', 'otvc_suspicious_login_protection', 'payments_apple_pay_trial_billing_details', 'payments_bulgaria_dual_prices', 'payments_california_consent', 'payments_new_local_payment_component', 'payments_onboarding_offered_products', 'payments_web_onboarding_monetization_step_from_configura
```
- **SRC-0780** `research/refinement/live-play.js` — [preserved redacted evidence](../evidence/text/bb2b575a71305d6b24316f8a494a4cb38bb38c6a5d3fd5995f33e4bce8f0fb35.js)

**Source references:** SRC-0777, SRC-0780  
**URL references:** None independently associated  
**Related findings:** FND-18977, FND-19909, FND-18139, FND-18142, FND-18205

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
