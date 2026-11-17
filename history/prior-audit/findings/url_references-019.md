# url_references — findings 1801–1900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-20932"></a>
## FND-20932: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01801",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "application/wasm 0.431104",
      "source_id": "SRC-0202",
      "line": 15,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1961.

```text
.js                                             200 93567 application/javascript 0.147183
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 583.

```text
e-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https:/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1961.

```text
.js                                             200 93567 application/javascript 0.147183
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 583.

```text
e-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https:/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20933"></a>
## FND-20933: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01802",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/javascript; charset=utf-8 0.176903",
      "source_id": "SRC-0202",
      "line": 9,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1120.

```text
puter/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 660.

```text
e-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1120.

```text
puter/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 660.

```text
e-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20934"></a>
## FND-20934: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01803",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "application/wasm 0.264840",
      "source_id": "SRC-0202",
      "line": 13,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1685.

```text
ngine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/eng
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 742.

```text
0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1685.

```text
ngine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/eng
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 742.

```text
0c.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20935"></a>
## FND-20935: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01804",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/javascript; charset=utf-8 0.186076",
      "source_id": "SRC-0202",
      "line": 5,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 548.

```text
gine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.c
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 352.

```text
orch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://ww
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 548.

```text
gine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.c
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 352.

```text
orch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://ww
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20936"></a>
## FND-20936: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 404; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01805",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm",
      "http_status": 404,
      "size_download": 27150,
      "content_type_and_optional_elapsed": "text/html 0.150929",
      "source_id": "SRC-0202",
      "line": 3,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 288.

```text
ine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 429.

```text
85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.ch
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 288.

```text
ine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 429.

```text
85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.ch
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20937"></a>
## FND-20937: https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01806",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/javascript; charset=utf-8 0.112791",
      "source_id": "SRC-0202",
      "line": 2,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 138.

```text
lanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engin
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 0.

```text
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explana
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 138.

```text
lanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engin
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 0.

```text
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explana
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20938"></a>
## FND-20938: https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01807",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "application/wasm 0.076822",
      "source_id": "SRC-0202",
      "line": 1,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 0.

```text
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 104.

```text
ess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.c
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 0.

```text
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 104.

```text
ess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.c
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20939"></a>
## FND-20939: https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01808",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "application/javascript 0.044203",
      "source_id": "SRC-0202",
      "line": 6,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 695.

```text
2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 826.

```text
6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https:/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 695.

```text
2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 826.

```text
6e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https:/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20940"></a>
## FND-20940: https://www.chess.com/r2/client-packages/analysis/2026.11.7/shared.eager.BOGLllgUUR.chunk.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/client-packages/analysis/2026.11.7/shared.eager.BOGLllgUUR.chunk.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0045"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01809"
}

### Evidence

- **SRC-0045** `extension/lib/descriptors.js` — [preserved redacted evidence](../evidence/text/28b92c2eb005f7d6c2823c0012ebf9832b97a79615b3e5b10be0bbd67e6beada.js)
  Character offset 68.

```text
// Chess.com protobuf FileDescriptorSet, extracted verbatim from
// https://www.chess.com/r2/client-packages/analysis/2026.11.7/shared.eager.BOGLllgUUR.chunk.js
// (base64 FileDescriptorProto blobs registered via the bundle's `J()` helper).
// Person
```

**Source references:** SRC-0045  
**URL references:** <https://www.chess.com/r2/client-packages/analysis/2026.11.7/shared.eager.BOGLllgUUR.chunk.js>  
**Related findings:** FND-17415, FND-17416, FND-17417

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20941"></a>
## FND-20941: https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 206; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01810",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "application/javascript 0.046749",
      "source_id": "SRC-0202",
      "line": 8,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 981.

```text
2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 898.

```text
ngle-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 981.

```text
2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 898.

```text
ngle-a809e6e.wasm
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20942"></a>
## FND-20942: https://www.chess.com/ratings

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ratings",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01811"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19143.

```text
:[],"badge":null},{"id":"community.rankings","type":"link","label":"Chess Ratings","url":"https:\/\/www.chess.com\/ratings","icon":{"name":"rating-rankings","variant":"color"},"sub":[],"badge":null},{"id":"commun
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 14107.

```text
:[],"badge":null},{"id":"community.rankings","type":"link","label":"Chess Ratings","url":"https:\/\/www.chess.com\/ratings","icon":{"name":"rating-rankings","variant":"color"},"sub":[],"badge":null},{"id":"commun
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19143.

```text
:[],"badge":null},{"id":"community.rankings","type":"link","label":"Chess Ratings","url":"https:\/\/www.chess.com\/ratings","icon":{"name":"rating-rankings","variant":"color"},"sub":[],"badge":null},{"id":"commun
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/ratings>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20943"></a>
## FND-20943: https://www.chess.com/register?returnUrl=https://www.chess.com/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/register?returnUrl=https://www.chess.com/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01812"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 40000.

```text
        <div class="mobile-toolbar-menu-area-auth">
          
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-small
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 62614.

```text

      
    <div class="sidebar-footer-auth-buttons">
        
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-mediu
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 40000.

```text
        <div class="mobile-toolbar-menu-area-auth">
          
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-small
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 62614.

```text

      
    <div class="sidebar-footer-auth-buttons">
        
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-mediu
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/register?returnUrl=https://www.chess.com/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20944"></a>
## FND-20944: https://www.chess.com/register?returnUrl=https://www.chess.com/game/live/187158515860

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/register?returnUrl=https://www.chess.com/game/live/187158515860",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01813"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 35136.

```text
        <div class="mobile-toolbar-menu-area-auth">
          
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/game/live/187158515860"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-small
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 57778.

```text

      
    <div class="sidebar-footer-auth-buttons">
        
  
  
      <a
      href="https://www.chess.com/register?returnUrl=https://www.chess.com/game/live/187158515860"
        
  
  class="cc-button-component cc-button-primary cc-bg-primary cc-button-mediu
```

**Source references:** SRC-0777  
**URL references:** <https://www.chess.com/register?returnUrl=https://www.chess.com/game/live/187158515860>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20945"></a>
## FND-20945: https://www.chess.com/resources

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/resources",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01814"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22226.

```text
:"color"},"sub":[],"badge":null},{"id":"other.tools","type":"link","label":"Tools","url":"https:\/\/www.chess.com\/resources","icon":{"name":"time-clock","variant":"color"},"sub":[],"badge":null},{"id":"other.visio
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17190.

```text
:"color"},"sub":[],"badge":null},{"id":"other.tools","type":"link","label":"Tools","url":"https:\/\/www.chess.com\/resources","icon":{"name":"time-clock","variant":"color"},"sub":[],"badge":null},{"id":"other.visio
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22226.

```text
:"color"},"sub":[],"badge":null},{"id":"other.tools","type":"link","label":"Tools","url":"https:\/\/www.chess.com\/resources","icon":{"name":"time-clock","variant":"color"},"sub":[],"badge":null},{"id":"other.visio
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/resources>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20946"></a>
## FND-20946: https://www.chess.com/ro/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ro/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01815"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7329.

```text
s://www.chess.com/no/analysis" hreflang="no" />
              <link rel="alternate" href="https://www.chess.com/ro/analysis" hreflang="ro" />
              <link rel="alternate" href="https://www.chess.com/sk/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7329.

```text
s://www.chess.com/no/analysis" hreflang="no" />
              <link rel="alternate" href="https://www.chess.com/ro/analysis" hreflang="ro" />
              <link rel="alternate" href="https://www.chess.com/sk/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ro/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20947"></a>
## FND-20947: https://www.chess.com/robots.txt

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/robots.txt",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0202",
    "SRC-1147",
    "SRC-1162",
    "SRC-1174"
  ],
  "directly_visited": "Historical GET probe recorded; see source and byte-range caveat.",
  "verification_status": "Historical HTTP status 200; not re-fetched in this audit.",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01816",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/robots.txt",
      "http_status": 200,
      "size_download": 4197,
      "content_type_and_optional_elapsed": "text/plain; charset=UTF-8 0.052364",
      "source_id": "SRC-0202",
      "line": 19,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2513.

```text
                                                200 35359 application/javascript 0.139400
https://www.chess.com/robots.txt                                                                     200 4197 text/plain; 
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1741.

```text
//www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2513.

```text
                                                200 35359 application/javascript 0.139400
https://www.chess.com/robots.txt                                                                     200 4197 text/plain; 
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1741.

```text
//www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/robots.txt>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20948"></a>
## FND-20948: https://www.chess.com/ru/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ru/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01817"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5637.

```text
s://www.chess.com/pl/analysis" hreflang="pl" />
              <link rel="alternate" href="https://www.chess.com/ru/analysis" hreflang="ru" />
              <link rel="alternate" href="https://www.chess.com/sv/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5637.

```text
s://www.chess.com/pl/analysis" hreflang="pl" />
              <link rel="alternate" href="https://www.chess.com/ru/analysis" hreflang="ru" />
              <link rel="alternate" href="https://www.chess.com/sv/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ru/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20949"></a>
## FND-20949: https://www.chess.com/share/game/live/default/187158515860

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/share/game/live/default/187158515860",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01818"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 4496.

```text
 <meta property="og:type" content="game" />

          <meta property="og:image" content="https://www.chess.com/share/game/live/default/187158515860" />

          <meta property="og:image:secure_url" content="https://www.chess.com/share/
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 4616.

```text
me/live/default/187158515860" />

          <meta property="og:image:secure_url" content="https://www.chess.com/share/game/live/default/187158515860" />

          <meta property="og:site_name" content="Chess.com" />

  
    
          <m
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5206.

```text
lick to review the game, move by move." />

          <meta name="twitter:image" content="https://www.chess.com/share/game/live/default/187158515860" />

  
  
          
        <link rel="canonical" href="https://www.chess.com/game/live
```

**Source references:** SRC-0777  
**URL references:** <https://www.chess.com/share/game/live/default/187158515860>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20950"></a>
## FND-20950: https://www.chess.com/sk/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sk/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01819"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7423.

```text
s://www.chess.com/ro/analysis" hreflang="ro" />
              <link rel="alternate" href="https://www.chess.com/sk/analysis" hreflang="sk" />
              <link rel="alternate" href="https://www.chess.com/sl/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7423.

```text
s://www.chess.com/ro/analysis" hreflang="ro" />
              <link rel="alternate" href="https://www.chess.com/sk/analysis" hreflang="sk" />
              <link rel="alternate" href="https://www.chess.com/sl/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/sk/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20951"></a>
## FND-20951: https://www.chess.com/sl/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sl/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01820"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7517.

```text
s://www.chess.com/sk/analysis" hreflang="sk" />
              <link rel="alternate" href="https://www.chess.com/sl/analysis" hreflang="sl" />
              <link rel="alternate" href="https://www.chess.com/tr/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7517.

```text
s://www.chess.com/sk/analysis" hreflang="sk" />
              <link rel="alternate" href="https://www.chess.com/sl/analysis" hreflang="sl" />
              <link rel="alternate" href="https://www.chess.com/tr/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/sl/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20952"></a>
## FND-20952: https://www.chess.com/solo-chess

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/solo-chess",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01821"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21676.

```text
"sub":[],"badge":null},{"id":"other.solo_chess","type":"link","label":"Solo Chess","url":"https:\/\/www.chess.com\/solo-chess","icon":{"name":"pawn-solo","variant":"color"},"sub":[],"badge":null},{"id":"other.comput
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 16640.

```text
"sub":[],"badge":null},{"id":"other.solo_chess","type":"link","label":"Solo Chess","url":"https:\/\/www.chess.com\/solo-chess","icon":{"name":"pawn-solo","variant":"color"},"sub":[],"badge":null},{"id":"other.comput
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21676.

```text
"sub":[],"badge":null},{"id":"other.solo_chess","type":"link","label":"Solo Chess","url":"https:\/\/www.chess.com\/solo-chess","icon":{"name":"pawn-solo","variant":"color"},"sub":[],"badge":null},{"id":"other.comput
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/solo-chess>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20953"></a>
## FND-20953: https://www.chess.com/sounds/_MP3_/default/capture.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/capture.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01822"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255422.

```text
nd:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568828.

```text
nd:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568828.

```text
nd:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/capture.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20954"></a>
## FND-20954: https://www.chess.com/sounds/_MP3_/default/castle.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/castle.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01823"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255677.

```text
capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/s
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569083.

```text
capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/s
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569083.

```text
capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/s
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/castle.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20955"></a>
## FND-20955: https://www.chess.com/sounds/_MP3_/default/game-end.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/game-end.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01824"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255932.

```text
stle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569338.

```text
stle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569338.

```text
stle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/game-end.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20956"></a>
## FND-20956: https://www.chess.com/sounds/_MP3_/default/game-start.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/game-start.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01825"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256197.

```text
.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569603.

```text
.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569603.

```text
.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/game-start.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20957"></a>
## FND-20957: https://www.chess.com/sounds/_MP3_/default/illegal.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/illegal.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01826"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256463.

```text
start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569869.

```text
start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569869.

```text
start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/illegal.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20958"></a>
## FND-20958: https://www.chess.com/sounds/_MP3_/default/move-check.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/move-check.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01827"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256725.

```text
.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570131.

```text
.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570131.

```text
.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/move-check.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20959"></a>
## FND-20959: https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01828"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257002.

```text
,moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.ches
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570408.

```text
,moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.ches
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570408.

```text
,moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.ches
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20960"></a>
## FND-20960: https://www.chess.com/sounds/_MP3_/default/move-self.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/move-self.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01829"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257280.

```text
nt.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.co
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570686.

```text
nt.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.co
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570686.

```text
nt.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.co
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/move-self.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20961"></a>
## FND-20961: https://www.chess.com/sounds/_MP3_/default/notify.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/notify.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01830"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257541.

```text
ve-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/s
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570947.

```text
ve-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/s
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570947.

```text
ve-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/s
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/notify.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20962"></a>
## FND-20962: https://www.chess.com/sounds/_MP3_/default/premove.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/premove.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01831"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257795.

```text
otify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571201.

```text
otify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571201.

```text
otify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/premove.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20963"></a>
## FND-20963: https://www.chess.com/sounds/_MP3_/default/promote.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/promote.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01832"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258052.

```text
emove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571458.

```text
emove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571458.

```text
emove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/promote.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20964"></a>
## FND-20964: https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01833"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258315.

```text
wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571721.

```text
wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571721.

```text
wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20965"></a>
## FND-20965: https://www.chess.com/sounds/_OGG_/default/capture.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/capture.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01834"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255483.

```text
_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568889.

```text
_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568889.

```text
_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/capture.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20966"></a>
## FND-20966: https://www.chess.com/sounds/_OGG_/default/castle.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/castle.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01835"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255737.

```text
BM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569143.

```text
BM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569143.

```text
BM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/castle.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20967"></a>
## FND-20967: https://www.chess.com/sounds/_OGG_/default/game-end.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/game-end.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01836"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255994.

```text
default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569400.

```text
default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569400.

```text
default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/game-end.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20968"></a>
## FND-20968: https://www.chess.com/sounds/_OGG_/default/game-start.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/game-start.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01837"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256261.

```text
ult/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569667.

```text
ult/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569667.

```text
ult/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/game-start.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20969"></a>
## FND-20969: https://www.chess.com/sounds/_OGG_/default/illegal.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/illegal.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01838"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256524.

```text
_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://w
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569930.

```text
_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569930.

```text
_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://w
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/illegal.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20970"></a>
## FND-20970: https://www.chess.com/sounds/_OGG_/default/move-check.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/move-check.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01839"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256789.

```text
ult/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`htt
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570195.

```text
ult/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`htt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570195.

```text
ult/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`htt
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/move-check.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20971"></a>
## FND-20971: https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01840"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257069.

```text
ve-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`http
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570475.

```text
ve-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`http
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570475.

```text
ve-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`http
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20972"></a>
## FND-20972: https://www.chess.com/sounds/_OGG_/default/move-self.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/move-self.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01841"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257343.

```text
fault/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://ww
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570749.

```text
fault/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://ww
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570749.

```text
fault/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://ww
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/move-self.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20973"></a>
## FND-20973: https://www.chess.com/sounds/_OGG_/default/notify.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/notify.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01842"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257601.

```text
BM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571007.

```text
BM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571007.

```text
BM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/notify.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20974"></a>
## FND-20974: https://www.chess.com/sounds/_OGG_/default/premove.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/premove.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01843"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257856.

```text
_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571262.

```text
_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571262.

```text
_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/premove.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20975"></a>
## FND-20975: https://www.chess.com/sounds/_OGG_/default/promote.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/promote.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01844"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258113.

```text
_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571519.

```text
_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571519.

```text
_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/promote.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20976"></a>
## FND-20976: https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01845"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258379.

```text
ult/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function gze(e){r
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571785.

```text
ult/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function W_e(e){r
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571785.

```text
ult/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function W_e(e){r
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20977"></a>
## FND-20977: https://www.chess.com/sounds/_WAV_/default/capture.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/capture.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01846"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255544.

```text
3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568950.

```text
3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568950.

```text
3_/default/capture.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/capture.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20978"></a>
## FND-20978: https://www.chess.com/sounds/_WAV_/default/castle.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/castle.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01847"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255797.

```text
MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569203.

```text
MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569203.

```text
MP3_/default/castle.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/castle.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20979"></a>
## FND-20979: https://www.chess.com/sounds/_WAV_/default/game-end.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/game-end.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01848"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256056.

```text
/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`http
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569462.

```text
/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`http
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569462.

```text
/default/game-end.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`http
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/game-end.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20980"></a>
## FND-20980: https://www.chess.com/sounds/_WAV_/default/game-start.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/game-start.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01849"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256325.

```text
ault/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://w
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569731.

```text
ault/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569731.

```text
ault/game-start.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/game-start.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://w
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/game-start.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20981"></a>
## FND-20981: https://www.chess.com/sounds/_WAV_/default/illegal.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/illegal.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01850"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256585.

```text
3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`http
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569991.

```text
3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`http
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569991.

```text
3_/default/illegal.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/illegal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`http
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/illegal.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20982"></a>
## FND-20982: https://www.chess.com/sounds/_WAV_/default/move-check.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/move-check.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01851"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256853.

```text
ault/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570259.

```text
ault/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570259.

```text
ault/move-check.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-check.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/move-check.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20983"></a>
## FND-20983: https://www.chess.com/sounds/_WAV_/default/move-opponent.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/move-opponent.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01852"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257136.

```text
ove-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https:
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570542.

```text
ove-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https:
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570542.

```text
ove-opponent.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-opponent.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https:
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/move-opponent.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20984"></a>
## FND-20984: https://www.chess.com/sounds/_WAV_/default/move-self.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/move-self.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01853"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257406.

```text
efault/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570812.

```text
efault/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570812.

```text
efault/move-self.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/move-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/move-self.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20985"></a>
## FND-20985: https://www.chess.com/sounds/_WAV_/default/notify.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/notify.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01854"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257661.

```text
MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://w
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571067.

```text
MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571067.

```text
MP3_/default/notify.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://w
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/notify.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20986"></a>
## FND-20986: https://www.chess.com/sounds/_WAV_/default/premove.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/premove.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01855"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257917.

```text
3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://w
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571323.

```text
3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://w
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571323.

```text
3_/default/premove.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://w
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/premove.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20987"></a>
## FND-20987: https://www.chess.com/sounds/_WAV_/default/promote.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/promote.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01856"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258174.

```text
3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`htt
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571580.

```text
3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`htt
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571580.

```text
3_/default/promote.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/promote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`htt
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/promote.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20988"></a>
## FND-20988: https://www.chess.com/sounds/_WAV_/default/tenseconds.wav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WAV_/default/tenseconds.wav",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01857"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258443.

```text
ault/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function gze(e){return{...e,board:{assets:{background:br.board},config:{highlight
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571849.

```text
ault/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function W_e(e){return{...e,board:{assets:{background:Qn.board},config:{highlight
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571849.

```text
ault/tenseconds.mp3`,ogg:`https://www.chess.com/sounds/_OGG_/default/tenseconds.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/tenseconds.wav`}}}}}));function W_e(e){return{...e,board:{assets:{background:Qn.board},config:{highlight
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WAV_/default/tenseconds.wav>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20989"></a>
## FND-20989: https://www.chess.com/sounds/_WEBM_/default/capture.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/capture.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01858"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255359.

```text
d1`,lightSquareCoordinateHex:`#779952`}},pieces:{assets:Qr},sound:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568765.

```text
d1`,lightSquareCoordinateHex:`#779952`}},pieces:{assets:Er},sound:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 568765.

```text
d1`,lightSquareCoordinateHex:`#779952`}},pieces:{assets:Er},sound:{assets:{capture:{webm:`https://www.chess.com/sounds/_WEBM_/default/capture.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/capture.mp3`,ogg:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/capture.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20990"></a>
## FND-20990: https://www.chess.com/sounds/_WEBM_/default/castle.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/castle.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01859"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255615.

```text
/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/s
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569021.

```text
/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/s
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569021.

```text
/capture.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/capture.wav`},castle:{webm:`https://www.chess.com/sounds/_WEBM_/default/castle.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/castle.mp3`,ogg:`https://www.chess.com/s
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/castle.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20991"></a>
## FND-20991: https://www.chess.com/sounds/_WEBM_/default/game-end.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/game-end.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01860"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1255868.

```text
t/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569274.

```text
t/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569274.

```text
t/castle.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/castle.wav`},gameEnd:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-end.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-end.mp3`,ogg:`https://www.chess.com
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/game-end.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20992"></a>
## FND-20992: https://www.chess.com/sounds/_WEBM_/default/game-start.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/game-start.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01861"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256131.

```text
-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569537.

```text
-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569537.

```text
-end.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-end.wav`},gameStart:{webm:`https://www.chess.com/sounds/_WEBM_/default/game-start.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/game-start.mp3`,ogg:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/game-start.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20993"></a>
## FND-20993: https://www.chess.com/sounds/_WEBM_/default/illegal.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/illegal.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01862"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256400.

```text
tart.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569806.

```text
tart.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 569806.

```text
tart.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/game-start.wav`},illegal:{webm:`https://www.chess.com/sounds/_WEBM_/default/illegal.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/illegal.mp3`,ogg:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/illegal.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20994"></a>
## FND-20994: https://www.chess.com/sounds/_WEBM_/default/move-check.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/move-check.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01863"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256659.

```text
legal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570065.

```text
legal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570065.

```text
legal.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/illegal.wav`},moveCheck:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-check.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-check.mp3`,ogg:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/move-check.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20995"></a>
## FND-20995: https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01864"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1256933.

```text
ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.ches
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570339.

```text
ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.ches
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570339.

```text
ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-check.wav`},moveOpponent:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-opponent.mp3`,ogg:`https://www.ches
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/move-opponent.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20996"></a>
## FND-20996: https://www.chess.com/sounds/_WEBM_/default/move-self.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/move-self.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01865"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257215.

```text
.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.co
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570621.

```text
.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.co
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570621.

```text
.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-opponent.wav`},moveSelf:{webm:`https://www.chess.com/sounds/_WEBM_/default/move-self.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/move-self.mp3`,ogg:`https://www.chess.co
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/move-self.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20997"></a>
## FND-20997: https://www.chess.com/sounds/_WEBM_/default/notify.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/notify.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01866"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257479.

```text
e-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/s
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570885.

```text
e-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/s
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 570885.

```text
e-self.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/move-self.wav`},notify:{webm:`https://www.chess.com/sounds/_WEBM_/default/notify.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/notify.mp3`,ogg:`https://www.chess.com/s
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/notify.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20998"></a>
## FND-20998: https://www.chess.com/sounds/_WEBM_/default/premove.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/premove.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01867"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257732.

```text
t/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571138.

```text
t/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571138.

```text
t/notify.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/notify.wav`},premove:{webm:`https://www.chess.com/sounds/_WEBM_/default/premove.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/premove.mp3`,ogg:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/premove.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20999"></a>
## FND-20999: https://www.chess.com/sounds/_WEBM_/default/promote.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/promote.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01868"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1257989.

```text
premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571395.

```text
premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571395.

```text
premove.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/premove.wav`},promote:{webm:`https://www.chess.com/sounds/_WEBM_/default/promote.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/promote.mp3`,ogg:`https://www.chess.com/
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/promote.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21000"></a>
## FND-21000: https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0781",
    "SRC-1137",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01869"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 1258249.

```text
mote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.c
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571655.

```text
mote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.c
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 571655.

```text
mote.ogg`,wav:`https://www.chess.com/sounds/_WAV_/default/promote.wav`},tenSeconds:{webm:`https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm`,mp3:`https://www.chess.com/sounds/_MP3_/default/tenseconds.mp3`,ogg:`https://www.chess.c
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/sounds/_WEBM_/default/tenseconds.webm>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21001"></a>
## FND-21001: https://www.chess.com/sq/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sq/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01870"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9309.

```text
w.chess.com/pt-BR/analysis" hreflang="pt-BR" />
              <link rel="alternate" href="https://www.chess.com/sq/analysis" hreflang="sq" />
              <link rel="alternate" href="https://www.chess.com/sr/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9309.

```text
w.chess.com/pt-BR/analysis" hreflang="pt-BR" />
              <link rel="alternate" href="https://www.chess.com/sq/analysis" hreflang="sq" />
              <link rel="alternate" href="https://www.chess.com/sr/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/sq/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21002"></a>
## FND-21002: https://www.chess.com/sr/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sr/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01871"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9403.

```text
s://www.chess.com/sq/analysis" hreflang="sq" />
              <link rel="alternate" href="https://www.chess.com/sr/analysis" hreflang="sr" />
              <link rel="alternate" href="https://www.chess.com/vi/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9403.

```text
s://www.chess.com/sq/analysis" hreflang="sq" />
              <link rel="alternate" href="https://www.chess.com/sr/analysis" hreflang="sr" />
              <link rel="alternate" href="https://www.chess.com/vi/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/sr/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21003"></a>
## FND-21003: https://www.chess.com/stats

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/stats",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01872"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13304.

```text
ull,"url":null,"icon":null,"sub":[{"id":"play.stats","type":"link","label":"Stats","url":"https:\/\/www.chess.com\/stats","icon":{"name":"rating-stats","variant":"color"},"sub":[],"badge":null},{"id":"play.tour
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 8268.

```text
ull,"url":null,"icon":null,"sub":[{"id":"play.stats","type":"link","label":"Stats","url":"https:\/\/www.chess.com\/stats","icon":{"name":"rating-stats","variant":"color"},"sub":[],"badge":null},{"id":"play.tour
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13304.

```text
ull,"url":null,"icon":null,"sub":[{"id":"play.stats","type":"link","label":"Stats","url":"https:\/\/www.chess.com\/stats","icon":{"name":"rating-stats","variant":"color"},"sub":[],"badge":null},{"id":"play.tour
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/stats>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21004"></a>
## FND-21004: https://www.chess.com/streamers

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/streamers",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01873"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17603.

```text
},"sub":[],"badge":null},{"id":"watch.streamers","type":"link","label":"Streamers","url":"https:\/\/www.chess.com\/streamers","icon":{"name":"stream","variant":"color"},"sub":[],"badge":null},{"id":"watch.playing_n
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12567.

```text
},"sub":[],"badge":null},{"id":"watch.streamers","type":"link","label":"Streamers","url":"https:\/\/www.chess.com\/streamers","icon":{"name":"stream","variant":"color"},"sub":[],"badge":null},{"id":"watch.playing_n
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17603.

```text
},"sub":[],"badge":null},{"id":"watch.streamers","type":"link","label":"Streamers","url":"https:\/\/www.chess.com\/streamers","icon":{"name":"stream","variant":"color"},"sub":[],"badge":null},{"id":"watch.playing_n
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/streamers>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21005"></a>
## FND-21005: https://www.chess.com/support

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/support",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01874"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11294.

```text
  "@type": "ContactPoint",
          "contactType": "customer support",
          "url": "https://www.chess.com/support"
        },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
   
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6258.

```text
  "@type": "ContactPoint",
          "contactType": "customer support",
          "url": "https://www.chess.com/support"
        },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
   
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11294.

```text
  "@type": "ContactPoint",
          "contactType": "customer support",
          "url": "https://www.chess.com/support"
        },
        "sameAs": [
          "https://www.youtube.com/user/wwwChesscom",
   
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/support>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21006"></a>
## FND-21006: https://www.chess.com/sv/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/sv/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01875"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5731.

```text
s://www.chess.com/ru/analysis" hreflang="ru" />
              <link rel="alternate" href="https://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5731.

```text
s://www.chess.com/ru/analysis" hreflang="ru" />
              <link rel="alternate" href="https://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/sv/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21007"></a>
## FND-21007: https://www.chess.com/terms

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/terms",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01876"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20987.

```text
ub":[],"badge":null},{"id":"other.chess_terms","type":"link","label":"Chess Terms","url":"https:\/\/www.chess.com\/terms","icon":{"name":"pages-a-z","variant":"color"},"sub":[],"badge":null},{"id":"other.rules"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15951.

```text
ub":[],"badge":null},{"id":"other.chess_terms","type":"link","label":"Chess Terms","url":"https:\/\/www.chess.com\/terms","icon":{"name":"pages-a-z","variant":"color"},"sub":[],"badge":null},{"id":"other.rules"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20987.

```text
ub":[],"badge":null},{"id":"other.chess_terms","type":"link","label":"Chess Terms","url":"https:\/\/www.chess.com\/terms","icon":{"name":"pages-a-z","variant":"color"},"sub":[],"badge":null},{"id":"other.rules"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/terms>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21008"></a>
## FND-21008: https://www.chess.com/themes/css?board_size=200&pieces_size=150

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/themes/css?board_size=200&pieces_size=150",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01877"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 3538.

```text
"stylesheet" href="/bundles/app/vite/chessboard-layout.CoelVQAgfc.css">
  

  <link href="https://www.chess.com/themes/css?board_size=200&pieces_size=150" type="text/css" rel="stylesheet" id="active-theme-variables" />

  <meta name="theme-col
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 3693.

```text
stylesheet" href="/bundles/app/vite/chessboard-layout.CoelVQAgfc.css">
  


  <link href="https://www.chess.com/themes/css?board_size=200&pieces_size=150" type="text/css" rel="stylesheet" id="active-theme-variables" />

  <meta name="theme-col
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 3538.

```text
"stylesheet" href="/bundles/app/vite/chessboard-layout.CoelVQAgfc.css">
  

  <link href="https://www.chess.com/themes/css?board_size=200&pieces_size=150" type="text/css" rel="stylesheet" id="active-theme-variables" />

  <meta name="theme-col
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/themes/css?board_size=200&pieces_size=150>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21009"></a>
## FND-21009: https://www.chess.com/tk/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/tk/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01878"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10081.

```text
s://www.chess.com/bn/analysis" hreflang="bn" />
              <link rel="alternate" href="https://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10081.

```text
s://www.chess.com/bn/analysis" hreflang="bn" />
              <link rel="alternate" href="https://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/tk/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21010"></a>
## FND-21010: https://www.chess.com/today

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/today",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01879"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19609.

```text
ull,"icon":null,"sub":[{"id":"community.today","type":"link","label":"Chess Today","url":"https:\/\/www.chess.com\/today","icon":{"name":"today","variant":"color"},"sub":[],"badge":null},{"id":"community.news",
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 14573.

```text
ull,"icon":null,"sub":[{"id":"community.today","type":"link","label":"Chess Today","url":"https:\/\/www.chess.com\/today","icon":{"name":"today","variant":"color"},"sub":[],"badge":null},{"id":"community.news",
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19609.

```text
ull,"icon":null,"sub":[{"id":"community.today","type":"link","label":"Chess Today","url":"https:\/\/www.chess.com\/today","icon":{"name":"today","variant":"color"},"sub":[],"badge":null},{"id":"community.news",
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/today>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21011"></a>
## FND-21011: https://www.chess.com/tournament/live/arena/redirect-to/31184910

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/tournament/live/arena/redirect-to/31184910",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0127",
    "SRC-2045"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01880"
}

### Evidence

- **SRC-0127** `research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 138.

```text
026.11.13"]
[Round "-"]
[White "[PUBLIC_PLAYER_HANDLE_REDACTED]"]
[Black "[PUBLIC_PLAYER_HANDLE_REDACTED]"]
[Result "1-0"]
[Tournament "https://www.chess.com/tournament/live/arena/redirect-to/31184910"]
[CurrentPosition "8/8/1k6/p1r2nBp/8/8/PP6/K7 b - - 1 43"]
[Timezone "UTC"]
[ECO "D31"]

```
- **SRC-2045** `torch-refinement-research.zip!/research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 138.

```text
026.11.13"]
[Round "-"]
[White "[PUBLIC_PLAYER_HANDLE_REDACTED]"]
[Black "[PUBLIC_PLAYER_HANDLE_REDACTED]"]
[Result "1-0"]
[Tournament "https://www.chess.com/tournament/live/arena/redirect-to/31184910"]
[CurrentPosition "8/8/1k6/p1r2nBp/8/8/PP6/K7 b - - 1 43"]
[Timezone "UTC"]
[ECO "D31"]

```

**Source references:** SRC-0127, SRC-2045  
**URL references:** <https://www.chess.com/tournament/live/arena/redirect-to/31184910>  
**Related findings:** FND-20813, FND-20911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21012"></a>
## FND-21012: https://www.chess.com/tr/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/tr/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01881"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7611.

```text
s://www.chess.com/sl/analysis" hreflang="sl" />
              <link rel="alternate" href="https://www.chess.com/tr/analysis" hreflang="tr" />
              <link rel="alternate" href="https://www.chess.com/uk/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7611.

```text
s://www.chess.com/sl/analysis" hreflang="sl" />
              <link rel="alternate" href="https://www.chess.com/tr/analysis" hreflang="tr" />
              <link rel="alternate" href="https://www.chess.com/uk/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/tr/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21013"></a>
## FND-21013: https://www.chess.com/train

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/train",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01882"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15781.

```text
ge":null}],"badge":null}],"other":[{"id":"train","type":"dropdown","label":"Train","url":"https:\/\/www.chess.com\/train","icon":{"name":"training","variant":"color"},"sub":[{"id":"train.courses","type":"link",
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 49308.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="train">
    


  <a
    href="https://www.chess.com/train"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50374.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-train"
    data-primary-action="https://www.chess.com/train">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10745.

```text
ge":null}],"badge":null}],"other":[{"id":"train","type":"dropdown","label":"Train","url":"https:\/\/www.chess.com\/train","icon":{"name":"training","variant":"color"},"sub":[{"id":"train.courses","type":"link",
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 44472.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="train">
    


  <a
    href="https://www.chess.com/train"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 45538.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-train"
    data-primary-action="https://www.chess.com/train">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15781.

```text
ge":null}],"badge":null}],"other":[{"id":"train","type":"dropdown","label":"Train","url":"https:\/\/www.chess.com\/train","icon":{"name":"training","variant":"color"},"sub":[{"id":"train.courses","type":"link",
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 49308.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="train">
    


  <a
    href="https://www.chess.com/train"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 50374.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-train"
    data-primary-action="https://www.chess.com/train">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/train>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21014"></a>
## FND-21014: https://www.chess.com/tv

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/tv",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01883"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17434.

```text
or"},"sub":[],"badge":null},{"id":"watch.chess_tv","type":"link","label":"ChessTV","url":"https:\/\/www.chess.com\/tv","icon":{"name":"device-chess-tv","variant":"color"},"sub":[],"badge":null},{"id":"watch.
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12398.

```text
or"},"sub":[],"badge":null},{"id":"watch.chess_tv","type":"link","label":"ChessTV","url":"https:\/\/www.chess.com\/tv","icon":{"name":"device-chess-tv","variant":"color"},"sub":[],"badge":null},{"id":"watch.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17434.

```text
or"},"sub":[],"badge":null},{"id":"watch.chess_tv","type":"link","label":"ChessTV","url":"https:\/\/www.chess.com\/tv","icon":{"name":"device-chess-tv","variant":"color"},"sub":[],"badge":null},{"id":"watch.
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/tv>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21015"></a>
## FND-21015: https://www.chess.com/uk/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/uk/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01884"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7705.

```text
s://www.chess.com/tr/analysis" hreflang="tr" />
              <link rel="alternate" href="https://www.chess.com/uk/analysis" hreflang="uk" />
              <link rel="alternate" href="https://www.chess.com/af/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7705.

```text
s://www.chess.com/tr/analysis" hreflang="tr" />
              <link rel="alternate" href="https://www.chess.com/uk/analysis" hreflang="uk" />
              <link rel="alternate" href="https://www.chess.com/af/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/uk/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21016"></a>
## FND-21016: https://www.chess.com/ur/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ur/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01885"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10269.

```text
s://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/analysis" hreflang="ur" />
          
    
        <link rel="canonical" href="https://www.chess.c
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10269.

```text
s://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/analysis" hreflang="ur" />
          
    
        <link rel="canonical" href="https://www.chess.c
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ur/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21017"></a>
## FND-21017: https://www.chess.com/variants

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/variants",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01886"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13665.

```text
or"},"sub":[],"badge":null},{"id":"play.variants","type":"link","label":"Variants","url":"https:\/\/www.chess.com\/variants","icon":{"name":"variants","variant":"color"},"sub":[],"badge":null},{"id":"play.game_his
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 8629.

```text
or"},"sub":[],"badge":null},{"id":"play.variants","type":"link","label":"Variants","url":"https:\/\/www.chess.com\/variants","icon":{"name":"variants","variant":"color"},"sub":[],"badge":null},{"id":"play.game_his
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13665.

```text
or"},"sub":[],"badge":null},{"id":"play.variants","type":"link","label":"Variants","url":"https:\/\/www.chess.com\/variants","icon":{"name":"variants","variant":"color"},"sub":[],"badge":null},{"id":"play.game_his
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/variants>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21018"></a>
## FND-21018: https://www.chess.com/vi/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/vi/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01887"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9497.

```text
s://www.chess.com/sr/analysis" hreflang="sr" />
              <link rel="alternate" href="https://www.chess.com/vi/analysis" hreflang="vi" />
              <link rel="alternate" href="https://www.chess.com/zh-HK/a
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9497.

```text
s://www.chess.com/sr/analysis" hreflang="sr" />
              <link rel="alternate" href="https://www.chess.com/vi/analysis" hreflang="vi" />
              <link rel="alternate" href="https://www.chess.com/zh-HK/a
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/vi/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21019"></a>
## FND-21019: https://www.chess.com/vision

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/vision",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01888"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22391.

```text
color"},"sub":[],"badge":null},{"id":"other.vision","type":"link","label":"Vision","url":"https:\/\/www.chess.com\/vision","icon":{"name":"board-vision-coordinate","variant":"color"},"sub":[],"badge":null},{"id"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17355.

```text
color"},"sub":[],"badge":null},{"id":"other.vision","type":"link","label":"Vision","url":"https:\/\/www.chess.com\/vision","icon":{"name":"board-vision-coordinate","variant":"color"},"sub":[],"badge":null},{"id"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22391.

```text
color"},"sub":[],"badge":null},{"id":"other.vision","type":"link","label":"Vision","url":"https:\/\/www.chess.com\/vision","icon":{"name":"board-vision-coordinate","variant":"color"},"sub":[],"badge":null},{"id"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/vision>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21020"></a>
## FND-21020: https://www.chess.com/votechess

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/votechess",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01889"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21499.

```text
"sub":[],"badge":null},{"id":"other.vote_chess","type":"link","label":"Vote Chess","url":"https:\/\/www.chess.com\/votechess","icon":{"name":"clipboard-vote","variant":"color"},"sub":[],"badge":null},{"id":"other.s
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 16463.

```text
"sub":[],"badge":null},{"id":"other.vote_chess","type":"link","label":"Vote Chess","url":"https:\/\/www.chess.com\/votechess","icon":{"name":"clipboard-vote","variant":"color"},"sub":[],"badge":null},{"id":"other.s
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21499.

```text
"sub":[],"badge":null},{"id":"other.vote_chess","type":"link","label":"Vote Chess","url":"https:\/\/www.chess.com\/votechess","icon":{"name":"clipboard-vote","variant":"color"},"sub":[],"badge":null},{"id":"other.s
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/votechess>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21021"></a>
## FND-21021: https://www.chess.com/watch

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/watch",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01890"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17126.

```text
b":[],"badge":null}],"badge":null},{"id":"watch","type":"dropdown","label":"Watch","url":"https:\/\/www.chess.com\/watch","icon":{"name":"binoculars","variant":"color"},"sub":[{"id":"watch.events","type":"link"
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 51488.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="watch">
    


  <a
    href="https://www.chess.com/watch"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 52558.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-watch"
    data-primary-action="https://www.chess.com/watch">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12090.

```text
b":[],"badge":null}],"badge":null},{"id":"watch","type":"dropdown","label":"Watch","url":"https:\/\/www.chess.com\/watch","icon":{"name":"binoculars","variant":"color"},"sub":[{"id":"watch.events","type":"link"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 46652.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="watch">
    


  <a
    href="https://www.chess.com/watch"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 47722.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-watch"
    data-primary-action="https://www.chess.com/watch">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17126.

```text
b":[],"badge":null}],"badge":null},{"id":"watch","type":"dropdown","label":"Watch","url":"https:\/\/www.chess.com\/watch","icon":{"name":"binoculars","variant":"color"},"sub":[{"id":"watch.events","type":"link"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 51488.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="watch">
    


  <a
    href="https://www.chess.com/watch"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 52558.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-watch"
    data-primary-action="https://www.chess.com/watch">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/watch>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21022"></a>
## FND-21022: https://www.chess.com/zh-HK/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/zh-HK/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01891"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9591.

```text
s://www.chess.com/vi/analysis" hreflang="vi" />
              <link rel="alternate" href="https://www.chess.com/zh-HK/analysis" hreflang="zh-HK" />
              <link rel="alternate" href="https://www.chess.com/zh-T
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9591.

```text
s://www.chess.com/vi/analysis" hreflang="vi" />
              <link rel="alternate" href="https://www.chess.com/zh-HK/analysis" hreflang="zh-HK" />
              <link rel="alternate" href="https://www.chess.com/zh-T
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/zh-HK/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21023"></a>
## FND-21023: https://www.chess.com/zh-TW/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/zh-TW/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01892"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9691.

```text
w.chess.com/zh-HK/analysis" hreflang="zh-HK" />
              <link rel="alternate" href="https://www.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9691.

```text
w.chess.com/zh-HK/analysis" hreflang="zh-HK" />
              <link rel="alternate" href="https://www.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/zh-TW/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21024"></a>
## FND-21024: https://www.chess.com/zh/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/zh/analysis",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01893"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6107.

```text
s://www.chess.com/it/analysis" hreflang="it" />
              <link rel="alternate" href="https://www.chess.com/zh/analysis" hreflang="zh" />
              <link rel="alternate" href="https://www.chess.com/ja/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6107.

```text
s://www.chess.com/it/analysis" hreflang="it" />
              <link rel="alternate" href="https://www.chess.com/zh/analysis" hreflang="zh" />
              <link rel="alternate" href="https://www.chess.com/ja/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/zh/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21025"></a>
## FND-21025: https://www.chesscom.shop

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chesscom.shop",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01894"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22572.

```text
},"sub":[],"badge":null},{"id":"other.merch","type":"link","label":"Shop \/ Merch","url":"https:\/\/www.chesscom.shop","icon":{"name":"commerce-merch","variant":"color"},"sub":[],"badge":null},{"id":"other.g
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17536.

```text
},"sub":[],"badge":null},{"id":"other.merch","type":"link","label":"Shop \/ Merch","url":"https:\/\/www.chesscom.shop","icon":{"name":"commerce-merch","variant":"color"},"sub":[],"badge":null},{"id":"other.g
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22572.

```text
},"sub":[],"badge":null},{"id":"other.merch","type":"link","label":"Shop \/ Merch","url":"https:\/\/www.chesscom.shop","icon":{"name":"commerce-merch","variant":"color"},"sub":[],"badge":null},{"id":"other.g
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chesscom.shop>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21026"></a>
## FND-21026: https://www.chesskid.com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chesskid.com",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01895"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22068.

```text
r"},"sub":[],"badge":null},{"id":"other.chesskid","type":"link","label":"ChessKid","url":"https:\/\/www.chesskid.com","icon":{"name":"logo-chesskid","variant":"color"},"sub":[],"badge":null},{"id":"other.to
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17032.

```text
r"},"sub":[],"badge":null},{"id":"other.chesskid","type":"link","label":"ChessKid","url":"https:\/\/www.chesskid.com","icon":{"name":"logo-chesskid","variant":"color"},"sub":[],"badge":null},{"id":"other.to
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22068.

```text
r"},"sub":[],"badge":null},{"id":"other.chesskid","type":"link","label":"ChessKid","url":"https:\/\/www.chesskid.com","icon":{"name":"logo-chesskid","variant":"color"},"sub":[],"badge":null},{"id":"other.to
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chesskid.com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21027"></a>
## FND-21027: https://www.crunchbase.com/organization/chess-com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.crunchbase.com/organization/chess-com",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01896"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11805.

```text
edia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.h
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6769.

```text
edia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.h
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11805.

```text
edia.org/wiki/Chess.com",
          "https://www.wikidata.org/wiki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.h
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.crunchbase.com/organization/chess-com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21028"></a>
## FND-21028: https://www.facebook.com/chess

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.facebook.com/chess",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01897"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11515.

```text
s://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.c
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6479.

```text
s://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.c
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11515.

```text
s://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.c
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.facebook.com/chess>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21029"></a>
## FND-21029: https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01898"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11868.

```text
iki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm"
        ]
      }
    </script>
  
      
  
        
        
      <script>
      docu
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6832.

```text
iki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm"
        ]
      }
    </script>
  
      
  
        
        
      <script>
      docu
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11868.

```text
iki/Q16829376",
          "https://www.crunchbase.com/organization/chess-com",
          "https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm"
        ]
      }
    </script>
  
      
  
        
        
      <script>
      docu
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.glassdoor.com/Overview/Working-at-Chess-com-EI_IE2241778.11,20.htm>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21030"></a>
## FND-21030: https://www.instagram.com/wwwchesscom/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.instagram.com/wwwchesscom/",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01899"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11463.

```text
//www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6427.

```text
//www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11463.

```text
//www.youtube.com/user/wwwChesscom",
          "https://twitter.com/chesscom",
          "https://www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.instagram.com/wwwchesscom/>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-21031"></a>
## FND-21031: https://www.linkedin.com/company/chess-com

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.linkedin.com/company/chess-com",
  "type": "external_or_documentation",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01900"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11559.

```text
//www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
   
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 6523.

```text
//www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
   
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 11559.

```text
//www.instagram.com/wwwchesscom/",
          "https://www.facebook.com/chess",
          "https://www.linkedin.com/company/chess-com",
          "https://www.tiktok.com/@chess",
          "https://www.twitch.tv/chess",
   
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.linkedin.com/company/chess-com>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.
