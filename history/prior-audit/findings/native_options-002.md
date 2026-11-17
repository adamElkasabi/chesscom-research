# native_options — findings 101–102

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-19130"></a>
## FND-19130: Advertised UCI UCI_Chess960

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UCI_Chess960 type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4581.

```text
yzygyProbeLimit type spin default 7 min 1 max 7
option name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default false
uciok
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19131"></a>
## FND-19131: Advertised UCI UseSoftNodes

**Category:** native_options  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

option name UseSoftNodes type check default false

### Evidence

- **SRC-0874** `research/refinement/uci-options.txt` — [preserved redacted evidence](../evidence/text/5ca5c962f85b9a0ad1ec6e7b9bc762bda3b88fb17d92d49df9bd87ca25e9b613.txt)
  Character offset 4631.

```text
tion name Threads type spin default 1 min 1 max 1
option name UCI_Chess960 type check default false
option name UseSoftNodes type check default false
uciok
```

**Source references:** SRC-0874  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-19030, FND-19031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
