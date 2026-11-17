# security — findings 1–2

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18980"></a>
## FND-18980: Local entitlement changes do not prove a production authorization vulnerability

**Category:** security  
**Classification:** inference  
**Verification:** partially verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The working extension replaces the remote review transport with local output and adjusts local client gates. No authorized authenticated cloud entitlement bypass or account-state mutation was demonstrated. Keep local patch behavior separate from server authorization claims.

### Evidence

- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
  Character offset 5786.

```text
ion
  // store at module initialization. In particular, its pre-socket gate is:
  //   !permissions.canCreate && permissions.uiLocked
  // where uiLocked comes from analysis.locked. hasUnlimitedReview alone only
  // affects report-card/upgrade UI; it does NOT let a new review start.
  // Change only local analysis permissions, never account membership or cloud
  // save/library rights. Getters also survive ordinary 
```
- **SRC-0003** `QUOTA-FIX-INSTALL.txt` — [preserved redacted evidence](../evidence/text/f4743bdea513c51e8409333bf289915a738ede9623295bc57bf8a6c50aa02999.txt)
  Character offset 723.

```text
ed.

WHAT CHANGED
The old hook patched hasUnlimitedReview, but the page's actual launch gate
checks canCreate and locked before opening a review socket. Those local
analysis permissions are now patched before the page snapshots them.
Existing page configuration/PGN is preserved. Later normal quota assignments
and replacement analysis configurations are handled as well.

This does not change account membership, server
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)

**Source references:** SRC-0053, SRC-0003, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-18891, FND-18943, FND-18944, FND-18955

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18981"></a>
## FND-18981: Passive source metadata is not a security-header assessment

**Category:** security  
**Classification:** unknown  
**Verification:** unverified  
**Confidence:** high — No direct security test or relevant full header/cookie artifact was accessed.

No preserved complete response-header/cookie/CORS/CSP trace of authenticated website pages was found. Extension CSP and isolated tests cannot fill that gap. Native schema fieldvalidation_hash is an interface,not independently verified anti-tamper strength.

### Evidence

- **SRC-0050** `extension/manifest.json` — [preserved redacted evidence](../evidence/text/ba33bb40ad68e7f612945a04967c1cb1f02306d7d8d765e27e093de09741a3f6.json)
- **SRC-2047** `uploads/PREMIUM-ANALYSIS.md` — [preserved redacted evidence](../evidence/text/1eecd070e0afdb43b61a19aeb6acf5e7cf37e32dc1c5aa6e22ca64f836d4a6ba.md)
  Character offset 28598.

```text
llsPosition {
  int32  ply             = 1;
  repeated Skill skills  = 2;     // 73 values
  string validation_hash = 3;     // signed by CEE
}
```

73 skills, e.g. `SKILL_FORK=21`, `SKILL_ROYAL_FORK=31`,
`SKILL_BRILLIANT_SACRIFICE=37`, `SKILL_OPPOSITION=65`,
`SKILL_ROOK_BEHIND_OWN_PASSED_PAWN=64`. These are what the step-by-step
explanation shows ("this move develops a piece with tempo") and they feed
puzzles.

`val
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)

**Source references:** SRC-0050, SRC-2047, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-18943, FND-18954, FND-18956, FND-00085, FND-00086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
