# architecture — findings 1–1

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18891"></a>
## FND-18891: Three different analysis pipelines must not be conflated

**Category:** architecture  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

The full website Game Review request builder sends CEAC over a remote WebSocket. Quick Analysis has binary and legacy local CEE routes. The extension intercepts the full-review socket and supplies local CEE output. Local worker loading therefore does not prove that native full Game Review runs locally.

### Evidence

- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
- **SRC-0752** `research/refinement/live-chunks/client.e0da4c65.BIjoPk3wAJ.chunk.js` — [preserved redacted evidence](../evidence/text/5919dccce274c55ef86cf454d90cf46ed1d0a18dcb86be4ccdb0c70f625d1dea.js)
- **SRC-0053** `extension/page-hook.js` — [preserved redacted evidence](../evidence/text/34e140d2e6dfe4e4bd5060054e97b302ea63adc06259706b495a836a9a1300f7.js)
- **SRC-0049** `extension/lib/review.js` — [preserved redacted evidence](../evidence/text/5f056d321e317d758a6d9882be84d2b32b60555244d92454645b7c2f3229f21d.js)
  Character offset 1109.

```text
t: { case: 'uciMoves', value: { moves: pageGame.uci || [] } },
    } } };
    else throw new Error('GameReviewRequest has no game');
  }
  // CEAC normally merges runSearchReq into NewGame settings on its server.
  // Do that merge locally, preserving player metadata and all source formats.
  const settings = { ...source.settings };
  const search = request.runSearchReq?.search;
  if (search?.case === 'gameReviewSear
```

**Source references:** SRC-1137, SRC-0752, SRC-0053, SRC-0049  
**URL references:** None independently associated  
**Related findings:** FND-18108, FND-18109, FND-18117, FND-18917, FND-18918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
