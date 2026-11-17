# url_references — findings 1701–1800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-20832"></a>
## FND-20832: https://www.chess.com/bundles/app/js/engine/books/eco.json

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/books/eco.json",
  "type": "asset",
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
  "id": "URL-01701",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/books/eco.json",
      "http_status": 200,
      "size_download": 30873759,
      "content_type_and_optional_elapsed": "application/json 0.199615",
      "source_id": "SRC-0202",
      "line": 21,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2801.

```text
e.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1521.

```text
s/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bu
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2801.

```text
e.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1521.

```text
s/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bu
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/books/eco.json>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20833

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20833"></a>
## FND-20833: https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue",
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
  "id": "URL-01702",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/plain 0.171573",
      "source_id": "SRC-0202",
      "line": 23,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3068.

```text
engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analy
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1580.

```text
/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/an
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3068.

```text
engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analy
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1580.

```text
/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/an
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20834"></a>
## FND-20834: https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue",
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
  "id": "URL-01703",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/plain 0.138668",
      "source_id": "SRC-0202",
      "line": 22,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2941.

```text
eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundl
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1645.

```text
js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2941.

```text
eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundl
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1645.

```text
js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20835"></a>
## FND-20835: https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js",
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
  "id": "URL-01704",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js",
      "http_status": 404,
      "size_download": 548,
      "content_type_and_optional_elapsed": "text/html 0.163742",
      "source_id": "SRC-0202",
      "line": 12,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1557.

```text
-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/ass
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 980.

```text
ysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bu
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1557.

```text
-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/ass
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 980.

```text
ysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bu
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20836"></a>
## FND-20836: https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js",
  "type": "asset",
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
  "id": "URL-01705",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js",
      "http_status": 200,
      "size_download": 40876,
      "content_type_and_optional_elapsed": "application/javascript 0.138553",
      "source_id": "SRC-0202",
      "line": 11,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1414.

```text
2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1047.

```text
.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1414.

```text
2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1047.

```text
.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20837"></a>
## FND-20837: https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm",
  "type": "asset",
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
  "id": "URL-01706",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm",
      "http_status": 200,
      "size_download": 707847,
      "content_type_and_optional_elapsed": "application/wasm 0.205290",
      "source_id": "SRC-0202",
      "line": 17,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2232.

```text
kfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1112.

```text
e/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/ap
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2232.

```text
kfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1112.

```text
e/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/ap
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20838"></a>
## FND-20838: https://www.chess.com/bundles/app/js/engine/stockfish.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/stockfish.js",
  "type": "asset",
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
  "id": "URL-01707",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/stockfish.js",
      "http_status": 200,
      "size_download": 93567,
      "content_type_and_optional_elapsed": "application/javascript 0.147183",
      "source_id": "SRC-0202",
      "line": 14,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1818.

```text
e/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
htt
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1179.

```text
e/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1818.

```text
e/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
htt
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1179.

```text
e/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20839"></a>
## FND-20839: https://www.chess.com/bundles/app/js/engine/stockfish.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/stockfish.wasm",
  "type": "asset",
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
  "id": "URL-01708",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/stockfish.wasm",
      "http_status": 200,
      "size_download": 385560,
      "content_type_and_optional_elapsed": "application/wasm 0.181921",
      "source_id": "SRC-0202",
      "line": 16,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2094.

```text
e/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://ww
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1236.

```text
js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2094.

```text
e/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://ww
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1236.

```text
js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20840"></a>
## FND-20840: https://www.chess.com/bundles/app/js/engine/torch-lite.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/torch-lite.js",
  "type": "asset",
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
  "id": "URL-01709",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/torch-lite.js",
      "http_status": 200,
      "size_download": 35368,
      "content_type_and_optional_elapsed": "application/javascript 0.160463",
      "source_id": "SRC-0202",
      "line": 20,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2658.

```text
                                              200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
http
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1403.

```text
com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2658.

```text
                                              200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
http
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1403.

```text
com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch-lite.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20841"></a>
## FND-20841: https://www.chess.com/bundles/app/js/engine/torch-lite.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/torch-lite.wasm",
  "type": "asset",
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
  "id": "URL-01710",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/torch-lite.wasm",
      "http_status": 200,
      "size_download": 6840976,
      "content_type_and_optional_elapsed": "application/wasm 1.076223",
      "source_id": "SRC-0202",
      "line": 26,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3481.

```text
wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1461.

```text
undles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3481.

```text
wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1461.

```text
undles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch-lite.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20842"></a>
## FND-20842: https://www.chess.com/bundles/app/js/engine/torch.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/torch.js",
  "type": "asset",
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
  "id": "URL-01711",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/torch.js",
      "http_status": 200,
      "size_download": 35359,
      "content_type_and_optional_elapsed": "application/javascript 0.139400",
      "source_id": "SRC-0202",
      "line": 18,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2370.

```text
kfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1295.

```text
les/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2370.

```text
kfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1295.

```text
les/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20843"></a>
## FND-20843: https://www.chess.com/bundles/app/js/engine/torch.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/app/js/engine/torch.wasm",
  "type": "asset",
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
  "id": "URL-01712",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/bundles/app/js/engine/torch.wasm",
      "http_status": 200,
      "size_download": 47327363,
      "content_type_and_optional_elapsed": "application/wasm 0.731200",
      "source_id": "SRC-0202",
      "line": 25,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3341.

```text
                                             200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
http
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1348.

```text
bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/a
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3341.

```text
                                             200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
http
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 1348.

```text
bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/a
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20844"></a>
## FND-20844: https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png",
  "type": "asset",
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
  "id": "URL-01713"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10843.

```text
ess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png",
          "width": 1100,
          "height": 1100
        },
        "description": "Ch
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5807.

```text
ess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png",
          "width": 1100,
          "height": 1100
        },
        "description": "Ch
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10843.

```text
ess.com",
        "logo": {
          "@type": "ImageObject",
                    "url": "https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png",
          "width": 1100,
          "height": 1100
        },
        "description": "Ch
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20845"></a>
## FND-20845: https://www.chess.com/bundles/web/images/color-icons/commerce-adfree.b6edf890.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/color-icons/commerce-adfree.b6edf890.svg",
  "type": "asset",
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
  "id": "URL-01714"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 81730.

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 80986.

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 81730.

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/color-icons/commerce-adfree.b6edf890.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20846"></a>
## FND-20846: https://www.chess.com/bundles/web/images/color-icons/commerce-diamond.79625166.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/color-icons/commerce-diamond.79625166.svg",
  "type": "asset",
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
  "id": "URL-01715"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 79497.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 80220.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 78753.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 79476.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 79497.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 80220.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/color-icons/commerce-diamond.79625166.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20847"></a>
## FND-20847: https://www.chess.com/bundles/web/images/color-icons/commerce-gold.24e164aa.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/color-icons/commerce-gold.24e164aa.svg",
  "type": "asset",
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
  "id": "URL-01716"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 76456.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 77030.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 75712.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 76286.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 76456.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 77030.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/color-icons/commerce-gold.24e164aa.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20848"></a>
## FND-20848: https://www.chess.com/bundles/web/images/color-icons/commerce-platinum.a2bfab84.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/color-icons/commerce-platinum.a2bfab84.svg",
  "type": "asset",
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
  "id": "URL-01717"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 77615.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 78246.

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 78871.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 76871.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 77502.

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 78127.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 77615.

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 78246.

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 78871.

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/color-icons/commerce-platinum.a2bfab84.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20849"></a>
## FND-20849: https://www.chess.com/bundles/web/images/color-icons/heart-green.b65098b1.svg

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/color-icons/heart-green.b65098b1.svg",
  "type": "asset",
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
  "id": "URL-01718"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 81000.

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 80256.

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 81000.

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/color-icons/heart-green.b65098b1.svg>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20850"></a>
## FND-20850: https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png",
  "type": "asset",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01719"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 4373.

```text
eta property="og:type" content="website" />

          <meta property="og:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

          <meta property="og:site_name" content="Chess.com" />

  
    
          <m
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5013.

```text
ersonalized insights from Game Review." />

          <meta name="twitter:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analys
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 4373.

```text
eta property="og:type" content="website" />

          <meta property="og:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

          <meta property="og:site_name" content="Chess.com" />

  
    
          <m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5013.

```text
ersonalized insights from Game Review." />

          <meta name="twitter:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analys
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20851"></a>
## FND-20851: https://www.chess.com/bundles/web/images/webgl_data

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/images/webgl_data",
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
  "id": "URL-01720"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 180188.

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function ene(e,t){return!t.api.boardImages.isIni
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195845.

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function Ite(e,t){return!t.api.boardImages.isIni
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195845.

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function Ite(e,t){return!t.api.boardImages.isIni
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/bundles/web/images/webgl_data>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20852"></a>
## FND-20852: https://www.chess.com/bundles/web/sounds

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/bundles/web/sounds",
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
  "id": "URL-01721"
}

### Evidence

- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 180015.

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195672.

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 195672.

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```

**Source references:** SRC-0781, SRC-1137, SRC-1165  
**URL references:** <https://www.chess.com/bundles/web/sounds>  
**Related findings:** FND-18117, FND-18118, FND-18125, FND-18108, FND-18109

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20853"></a>
## FND-20853: https://www.chess.com/ca/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ca/analysis",
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
  "id": "URL-01722"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10175.

```text
s://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 10175.

```text
s://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ca/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20854"></a>
## FND-20854: https://www.chess.com/calculator

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/calculator",
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
  "id": "URL-01723"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22913.

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17877.

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22913.

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/calculator>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20855"></a>
## FND-20855: https://www.chess.com/classroom

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/classroom",
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
  "id": "URL-01724"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16444.

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11408.

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16444.

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/classroom>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20856"></a>
## FND-20856: https://www.chess.com/clubs

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/clubs",
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
  "id": "URL-01725"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18364.

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 13328.

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18364.

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/clubs>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20857"></a>
## FND-20857: https://www.chess.com/coaches

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/coaches",
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
  "id": "URL-01726"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18690.

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 13654.

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18690.

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/coaches>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20858"></a>
## FND-20858: https://www.chess.com/community

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/community",
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
  "id": "URL-01727"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17965.

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 53684.

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 54760.

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12929.

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 48848.

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 49924.

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17965.

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 53684.

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 54760.

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/community>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20859"></a>
## FND-20859: https://www.chess.com/computer-chess-championship

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/computer-chess-championship",
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
  "id": "URL-01728"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21871.

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 16835.

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21871.

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/computer-chess-championship>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20860"></a>
## FND-20860: https://www.chess.com/courses

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/courses",
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
  "id": "URL-01729"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15926.

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10890.

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15926.

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/courses>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20861"></a>
## FND-20861: https://www.chess.com/cs/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/cs/analysis",
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
  "id": "URL-01730"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6765.

```text
s://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6765.

```text
s://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/cs/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20862"></a>
## FND-20862: https://www.chess.com/da/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/da/analysis",
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
  "id": "URL-01731"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6859.

```text
s://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6859.

```text
s://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/da/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20863"></a>
## FND-20863: https://www.chess.com/daily

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/daily",
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
  "id": "URL-01732"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14371.

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9335.

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14371.

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/daily>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20864"></a>
## FND-20864: https://www.chess.com/de/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/de/analysis",
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
  "id": "URL-01733"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5449.

```text
s://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5449.

```text
s://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/de/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20865"></a>
## FND-20865: https://www.chess.com/el/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/el/analysis",
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
  "id": "URL-01734"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5825.

```text
s://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5825.

```text
s://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/el/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20866"></a>
## FND-20866: https://www.chess.com/endgames

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/endgames",
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
  "id": "URL-01735"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16612.

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11576.

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16612.

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/endgames>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20867"></a>
## FND-20867: https://www.chess.com/es/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/es/analysis",
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
  "id": "URL-01736"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5261.

```text
ss.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5261.

```text
ss.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/es/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20868"></a>
## FND-20868: https://www.chess.com/et/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/et/analysis",
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
  "id": "URL-01737"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8269.

```text
s://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8269.

```text
s://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/et/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20869"></a>
## FND-20869: https://www.chess.com/events

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/events",
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
  "id": "URL-01738"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17271.

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12235.

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17271.

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/events>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20870"></a>
## FND-20870: https://www.chess.com/explorer

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/explorer",
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
  "id": "URL-01739"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21329.

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 16293.

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21329.

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/explorer>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20871"></a>
## FND-20871: https://www.chess.com/fa/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/fa/analysis",
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
  "id": "URL-01740"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8363.

```text
s://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8363.

```text
s://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/fa/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20872"></a>
## FND-20872: https://www.chess.com/fi/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/fi/analysis",
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
  "id": "URL-01741"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6953.

```text
s://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6953.

```text
s://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/fi/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20873"></a>
## FND-20873: https://www.chess.com/fil/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/fil/analysis",
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
  "id": "URL-01742"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9791.

```text
w.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9791.

```text
w.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/fil/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20874"></a>
## FND-20874: https://www.chess.com/forum

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/forum",
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
  "id": "URL-01743"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20264.

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15228.

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20264.

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/forum>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20875"></a>
## FND-20875: https://www.chess.com/fr/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/fr/analysis",
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
  "id": "URL-01744"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5355.

```text
s://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5355.

```text
s://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/fr/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20876"></a>
## FND-20876: https://www.chess.com/friends

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/friends",
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
  "id": "URL-01745"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18202.

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 13166.

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18202.

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/friends>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20877"></a>
## FND-20877: https://www.chess.com/game/computer/2613044014?move=0

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/game/computer/2613044014?move=0",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0126",
    "SRC-2046"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01746"
}

### Evidence

- **SRC-0126** `research/fixtures/example-game.pgn` — [preserved redacted evidence](../evidence/text/a81e0dd69c853178d81f7b7bb470318e30f5aa2f08fcc0a792307b390be667ca.pgn)
  Character offset 269.

```text
1300"]
[Termination "[PUBLIC_PLAYER_HANDLE_REDACTED] won by checkmate"]
[ECO "A00"]
[EndDate "2026.11.11"]
[Link "https://www.chess.com/game/computer/2613044014?move=0"]

1. e3 e6 2. d4 d5 3. c4 Nf6 4. Nc3 Bb4 5. Bd2 O-O 6. a3 Be7 7. Nf3 c5 8. cxd5 exd5 9. 
```
- **SRC-2046** `torch-refinement-research.zip!/research/fixtures/example-game.pgn` — [preserved redacted evidence](../evidence/text/a81e0dd69c853178d81f7b7bb470318e30f5aa2f08fcc0a792307b390be667ca.pgn)
  Character offset 269.

```text
1300"]
[Termination "[PUBLIC_PLAYER_HANDLE_REDACTED] won by checkmate"]
[ECO "A00"]
[EndDate "2026.11.11"]
[Link "https://www.chess.com/game/computer/2613044014?move=0"]

1. e3 e6 2. d4 d5 3. c4 Nf6 4. Nc3 Bb4 5. Bd2 O-O 6. a3 Be7 7. Nf3 c5 8. cxd5 exd5 9. 
```

**Source references:** SRC-0126, SRC-2046  
**URL references:** <https://www.chess.com/game/computer/2613044014?move=0>  
**Related findings:** None assigned

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20878"></a>
## FND-20878: https://www.chess.com/game/live/187158515860

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/game/live/187158515860",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777",
    "SRC-2049"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01747"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 4094.

```text
ntent="Chess: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED]" />

          <meta property="og:url" content="https://www.chess.com/game/live/187158515860" />

          <meta property="fb:app_id" content="2427617054" />

          <meta proper
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 5323.

```text
/game/live/default/187158515860" />

  
  
          
        <link rel="canonical" href="https://www.chess.com/game/live/187158515860">
  
    
              
    
    <link rel="manifest" href="/manifest.json" crossorigin=
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 3245.

```text
omatically be treated as contradictory.

Visible follow-up investigation:
- User supplied https://www.chess.com/game/live/187158515860 as an example of a page loading explanation-engine.js/.wasm. A fetch_page result displaye
```

**Source references:** SRC-0777, SRC-2049  
**URL references:** <https://www.chess.com/game/live/187158515860>  
**Related findings:** FND-18977, FND-18979, FND-19909, FND-18916, FND-18924

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20879"></a>
## FND-20879: https://www.chess.com/games

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/games",
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
  "id": "URL-01748"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20811.

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15775.

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20811.

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/games>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20880"></a>
## FND-20880: https://www.chess.com/games/archive

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/games/archive",
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
  "id": "URL-01749"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13838.

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 8802.

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13838.

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/games/archive>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20881"></a>
## FND-20881: https://www.chess.com/gl/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/gl/analysis",
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
  "id": "URL-01750"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8457.

```text
s://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8457.

```text
s://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/gl/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20882"></a>
## FND-20882: https://www.chess.com/he/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/he/analysis",
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
  "id": "URL-01751"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8551.

```text
s://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/analysis" hreflang="he" />
              <link rel="alternate" href="https://www.chess.com/hi/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8551.

```text
s://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/analysis" hreflang="he" />
              <link rel="alternate" href="https://www.chess.com/hi/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/he/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20883"></a>
## FND-20883: https://www.chess.com/hi/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/hi/analysis",
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
  "id": "URL-01752"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8645.

```text
s://www.chess.com/he/analysis" hreflang="he" />
              <link rel="alternate" href="https://www.chess.com/hi/analysis" hreflang="hi" />
              <link rel="alternate" href="https://www.chess.com/id/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8645.

```text
s://www.chess.com/he/analysis" hreflang="he" />
              <link rel="alternate" href="https://www.chess.com/hi/analysis" hreflang="hi" />
              <link rel="alternate" href="https://www.chess.com/id/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/hi/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20884"></a>
## FND-20884: https://www.chess.com/hr/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/hr/analysis",
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
  "id": "URL-01753"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6671.

```text
s://www.chess.com/bg/analysis" hreflang="bg" />
              <link rel="alternate" href="https://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6671.

```text
s://www.chess.com/bg/analysis" hreflang="bg" />
              <link rel="alternate" href="https://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/hr/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20885"></a>
## FND-20885: https://www.chess.com/hu/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/hu/analysis",
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
  "id": "URL-01754"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7047.

```text
s://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/analysis" hreflang="hu" />
              <link rel="alternate" href="https://www.chess.com/lt/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7047.

```text
s://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/analysis" hreflang="hu" />
              <link rel="alternate" href="https://www.chess.com/lt/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/hu/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20886"></a>
## FND-20886: https://www.chess.com/hy/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/hy/analysis",
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
  "id": "URL-01755"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6483.

```text
s://www.chess.com/nl/analysis" hreflang="nl" />
              <link rel="alternate" href="https://www.chess.com/hy/analysis" hreflang="hy" />
              <link rel="alternate" href="https://www.chess.com/bg/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6483.

```text
s://www.chess.com/nl/analysis" hreflang="nl" />
              <link rel="alternate" href="https://www.chess.com/hy/analysis" hreflang="hy" />
              <link rel="alternate" href="https://www.chess.com/bg/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/hy/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20887"></a>
## FND-20887: https://www.chess.com/id/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/id/analysis",
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
  "id": "URL-01756"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8739.

```text
s://www.chess.com/hi/analysis" hreflang="hi" />
              <link rel="alternate" href="https://www.chess.com/id/analysis" hreflang="id" />
              <link rel="alternate" href="https://www.chess.com/is/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8739.

```text
s://www.chess.com/hi/analysis" hreflang="hi" />
              <link rel="alternate" href="https://www.chess.com/id/analysis" hreflang="id" />
              <link rel="alternate" href="https://www.chess.com/is/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/id/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20888"></a>
## FND-20888: https://www.chess.com/insights

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/insights",
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
  "id": "URL-01757"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16273.

```text
r"},"sub":[],"badge":null},{"id":"train.insights","type":"link","label":"Insights","url":"https:\/\/www.chess.com\/insights","icon":{"name":"puzzle-hint","variant":"color"},"sub":[],"badge":null},{"id":"train.clas
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11237.

```text
r"},"sub":[],"badge":null},{"id":"train.insights","type":"link","label":"Insights","url":"https:\/\/www.chess.com\/insights","icon":{"name":"puzzle-hint","variant":"color"},"sub":[],"badge":null},{"id":"train.clas
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16273.

```text
r"},"sub":[],"badge":null},{"id":"train.insights","type":"link","label":"Insights","url":"https:\/\/www.chess.com\/insights","icon":{"name":"puzzle-hint","variant":"color"},"sub":[],"badge":null},{"id":"train.clas
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/insights>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20889"></a>
## FND-20889: https://www.chess.com/is/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/is/analysis",
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
  "id": "URL-01758"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8833.

```text
s://www.chess.com/id/analysis" hreflang="id" />
              <link rel="alternate" href="https://www.chess.com/is/analysis" hreflang="is" />
              <link rel="alternate" href="https://www.chess.com/ka/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8833.

```text
s://www.chess.com/id/analysis" hreflang="id" />
              <link rel="alternate" href="https://www.chess.com/is/analysis" hreflang="is" />
              <link rel="alternate" href="https://www.chess.com/ka/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/is/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20890"></a>
## FND-20890: https://www.chess.com/it/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/it/analysis",
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
  "id": "URL-01759"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6013.

```text
s://www.chess.com/pt/analysis" hreflang="pt" />
              <link rel="alternate" href="https://www.chess.com/it/analysis" hreflang="it" />
              <link rel="alternate" href="https://www.chess.com/zh/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6013.

```text
s://www.chess.com/pt/analysis" hreflang="pt" />
              <link rel="alternate" href="https://www.chess.com/it/analysis" hreflang="it" />
              <link rel="alternate" href="https://www.chess.com/zh/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/it/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20891"></a>
## FND-20891: https://www.chess.com/ja/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ja/analysis",
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
  "id": "URL-01760"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6201.

```text
s://www.chess.com/zh/analysis" hreflang="zh" />
              <link rel="alternate" href="https://www.chess.com/ja/analysis" hreflang="ja" />
              <link rel="alternate" href="https://www.chess.com/ko/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6201.

```text
s://www.chess.com/zh/analysis" hreflang="zh" />
              <link rel="alternate" href="https://www.chess.com/ja/analysis" hreflang="ja" />
              <link rel="alternate" href="https://www.chess.com/ko/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ja/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20892"></a>
## FND-20892: https://www.chess.com/ka/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ka/analysis",
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
  "id": "URL-01761"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8927.

```text
s://www.chess.com/is/analysis" hreflang="is" />
              <link rel="alternate" href="https://www.chess.com/ka/analysis" hreflang="ka" />
              <link rel="alternate" href="https://www.chess.com/lv/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 8927.

```text
s://www.chess.com/is/analysis" hreflang="is" />
              <link rel="alternate" href="https://www.chess.com/ka/analysis" hreflang="ka" />
              <link rel="alternate" href="https://www.chess.com/lv/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ka/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20893"></a>
## FND-20893: https://www.chess.com/ko/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ko/analysis",
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
  "id": "URL-01762"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6295.

```text
s://www.chess.com/ja/analysis" hreflang="ja" />
              <link rel="alternate" href="https://www.chess.com/ko/analysis" hreflang="ko" />
              <link rel="alternate" href="https://www.chess.com/nl/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6295.

```text
s://www.chess.com/ja/analysis" hreflang="ja" />
              <link rel="alternate" href="https://www.chess.com/ko/analysis" hreflang="ko" />
              <link rel="alternate" href="https://www.chess.com/nl/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ko/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20894"></a>
## FND-20894: https://www.chess.com/leaderboard

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/leaderboard",
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
  "id": "URL-01763"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19327.

```text
,"badge":null},{"id":"community.leaderboards","type":"link","label":"Leaderboards","url":"https:\/\/www.chess.com\/leaderboard","icon":{"name":"leaderboard","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 14291.

```text
,"badge":null},{"id":"community.leaderboards","type":"link","label":"Leaderboards","url":"https:\/\/www.chess.com\/leaderboard","icon":{"name":"leaderboard","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19327.

```text
,"badge":null},{"id":"community.leaderboards","type":"link","label":"Leaderboards","url":"https:\/\/www.chess.com\/leaderboard","icon":{"name":"leaderboard","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/leaderboard>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20895"></a>
## FND-20895: https://www.chess.com/learn

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/learn",
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
  "id": "URL-01764"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15093.

```text
b":[],"badge":null}],"badge":null},{"id":"learn","type":"dropdown","label":"Learn","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15237.

```text
s","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","label":"Lessons","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[],"badge":null},{"id":"learn.play_coa
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 46993.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="learn">
    


  <a
    href="https://www.chess.com/learn"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 48057.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-learn"
    data-primary-action="https://www.chess.com/learn">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10057.

```text
b":[],"badge":null}],"badge":null},{"id":"learn","type":"dropdown","label":"Learn","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10201.

```text
s","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","label":"Lessons","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[],"badge":null},{"id":"learn.play_coa
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 42157.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="learn">
    


  <a
    href="https://www.chess.com/learn"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 43221.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-learn"
    data-primary-action="https://www.chess.com/learn">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15093.

```text
b":[],"badge":null}],"badge":null},{"id":"learn","type":"dropdown","label":"Learn","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15237.

```text
s","variant":"color"},"sub":[{"id":"learn.lessons","type":"link","label":"Lessons","url":"https:\/\/www.chess.com\/learn","icon":{"name":"lessons","variant":"color"},"sub":[],"badge":null},{"id":"learn.play_coa
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 46993.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="learn">
    


  <a
    href="https://www.chess.com/learn"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 48057.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-learn"
    data-primary-action="https://www.chess.com/learn">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/learn>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20896"></a>
## FND-20896: https://www.chess.com/learn-how-to-play-chess

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/learn-how-to-play-chess",
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
  "id": "URL-01765"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21145.

```text
:"color"},"sub":[],"badge":null},{"id":"other.rules","type":"link","label":"Rules","url":"https:\/\/www.chess.com\/learn-how-to-play-chess","icon":{"name":"chess-rules","variant":"color"},"sub":[],"badge":null},{"id":"other.expl
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 16109.

```text
:"color"},"sub":[],"badge":null},{"id":"other.rules","type":"link","label":"Rules","url":"https:\/\/www.chess.com\/learn-how-to-play-chess","icon":{"name":"chess-rules","variant":"color"},"sub":[],"badge":null},{"id":"other.expl
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 21145.

```text
:"color"},"sub":[],"badge":null},{"id":"other.rules","type":"link","label":"Rules","url":"https:\/\/www.chess.com\/learn-how-to-play-chess","icon":{"name":"chess-rules","variant":"color"},"sub":[],"badge":null},{"id":"other.expl
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/learn-how-to-play-chess>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20897"></a>
## FND-20897: https://www.chess.com/legal/fair-play

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/legal/fair-play",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0066",
    "SRC-1137",
    "SRC-1151",
    "SRC-1165"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01766"
}

### Evidence

- **SRC-0066** `research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 88702.

```text
d for positions matching a current game - see our <a href=%link%>policy.</a>`,{"%link%":`"https://www.chess.com/legal/fair-play"`})}))},async initEvaluation(){vu()||CA(),I()===P.Tabs.Review?(await oi(),this.overrideSc
```
- **SRC-1137** `research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2685602.

```text
nfo`,message:z(`Chess engines are disabled while you are playing games - see our <a href="https://www.chess.com/legal/fair-play">policy.</a>`)})}var V2=r((()=>{dW(),lue(),Mg()}));function Gbt({wdlData:e,isBookMove:t})
```
- **SRC-1151** `research.zip!/research/analysis.js` — [preserved redacted evidence](../evidence/text/7ae71f1372a1a59a2be693c4042cad85a67fb872cd9d59b6029d3a6e4adeb58c.js)
  Character offset 88702.

```text
d for positions matching a current game - see our <a href=%link%>policy.</a>`,{"%link%":`"https://www.chess.com/legal/fair-play"`})}))},async initEvaluation(){vu()||CA(),I()===P.Tabs.Review?(await oi(),this.overrideSc
```
- **SRC-1165** `research.zip!/research/shared.eager.BOGLllgUUR.chunk.js` — [preserved redacted evidence](../evidence/text/1feeb7e108b578394c47e9ff4395d8ed31222e84e7b335f7f30867785b38415e.js)
  Character offset 2685602.

```text
nfo`,message:z(`Chess engines are disabled while you are playing games - see our <a href="https://www.chess.com/legal/fair-play">policy.</a>`)})}var V2=r((()=>{dW(),lue(),Mg()}));function Gbt({wdlData:e,isBookMove:t})
```

**Source references:** SRC-0066, SRC-1137, SRC-1151, SRC-1165  
**URL references:** <https://www.chess.com/legal/fair-play>  
**Related findings:** FND-18106, FND-18107, FND-18108, FND-18109, FND-18117

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20898"></a>
## FND-20898: https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis",
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
  "id": "URL-01767"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 40398.

```text
>Sign Up</span>
      

              
    </a>
  

          
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-s
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 64067.

```text
l">Sign Up</span>
      

              
    </a>
  

        
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-m
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 40398.

```text
>Sign Up</span>
      

              
    </a>
  

          
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-s
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 64067.

```text
l">Sign Up</span>
      

              
    </a>
  

        
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-m
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20899"></a>
## FND-20899: https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/187158515860

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/187158515860",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0777"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01768"
}

### Evidence

- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 35548.

```text
>Sign Up</span>
      

              
    </a>
  

          
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/187158515860"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-s
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 59245.

```text
l">Sign Up</span>
      

              
    </a>
  

        
  
  
      <a
      href="https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/187158515860"
        
  
  class="cc-button-component cc-button-secondary cc-bg-secondary cc-button-m
```

**Source references:** SRC-0777  
**URL references:** <https://www.chess.com/login_and_go?returnUrl=https://www.chess.com/game/live/187158515860>  
**Related findings:** FND-18977, FND-18979, FND-19909

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20900"></a>
## FND-20900: https://www.chess.com/lt/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/lt/analysis",
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
  "id": "URL-01769"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7141.

```text
s://www.chess.com/hu/analysis" hreflang="hu" />
              <link rel="alternate" href="https://www.chess.com/lt/analysis" hreflang="lt" />
              <link rel="alternate" href="https://www.chess.com/no/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7141.

```text
s://www.chess.com/hu/analysis" hreflang="hu" />
              <link rel="alternate" href="https://www.chess.com/lt/analysis" hreflang="lt" />
              <link rel="alternate" href="https://www.chess.com/no/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/lt/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20901"></a>
## FND-20901: https://www.chess.com/lv/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/lv/analysis",
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
  "id": "URL-01770"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9021.

```text
s://www.chess.com/ka/analysis" hreflang="ka" />
              <link rel="alternate" href="https://www.chess.com/lv/analysis" hreflang="lv" />
              <link rel="alternate" href="https://www.chess.com/ms/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9021.

```text
s://www.chess.com/ka/analysis" hreflang="ka" />
              <link rel="alternate" href="https://www.chess.com/lv/analysis" hreflang="lv" />
              <link rel="alternate" href="https://www.chess.com/ms/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/lv/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20902"></a>
## FND-20902: https://www.chess.com/members

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/members",
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
  "id": "URL-01771"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18526.

```text
},"sub":[],"badge":null},{"id":"community.members","type":"link","label":"Members","url":"https:\/\/www.chess.com\/members","icon":{"name":"globe","variant":"color"},"sub":[],"badge":null},{"id":"community.coache
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 13490.

```text
},"sub":[],"badge":null},{"id":"community.members","type":"link","label":"Members","url":"https:\/\/www.chess.com\/members","icon":{"name":"globe","variant":"color"},"sub":[],"badge":null},{"id":"community.coache
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18526.

```text
},"sub":[],"badge":null},{"id":"community.members","type":"link","label":"Members","url":"https:\/\/www.chess.com\/members","icon":{"name":"globe","variant":"color"},"sub":[],"badge":null},{"id":"community.coache
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/members>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20903"></a>
## FND-20903: https://www.chess.com/membership/gift

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/membership/gift",
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
  "id": "URL-01772"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22730.

```text
t":"color"},"sub":[],"badge":null},{"id":"other.gift","type":"link","label":"Gift","url":"https:\/\/www.chess.com\/membership\/gift","icon":{"name":"commerce-gift","variant":"color"},"sub":[],"badge":null},{"id":"other.ca
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 17694.

```text
t":"color"},"sub":[],"badge":null},{"id":"other.gift","type":"link","label":"Gift","url":"https:\/\/www.chess.com\/membership\/gift","icon":{"name":"commerce-gift","variant":"color"},"sub":[],"badge":null},{"id":"other.ca
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 22730.

```text
t":"color"},"sub":[],"badge":null},{"id":"other.gift","type":"link","label":"Gift","url":"https:\/\/www.chess.com\/membership\/gift","icon":{"name":"commerce-gift","variant":"color"},"sub":[],"badge":null},{"id":"other.ca
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/membership/gift>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20904"></a>
## FND-20904: https://www.chess.com/ms/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/ms/analysis",
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
  "id": "URL-01773"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9115.

```text
s://www.chess.com/lv/analysis" hreflang="lv" />
              <link rel="alternate" href="https://www.chess.com/ms/analysis" hreflang="ms" />
              <link rel="alternate" href="https://www.chess.com/pt-BR/a
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9115.

```text
s://www.chess.com/lv/analysis" hreflang="lv" />
              <link rel="alternate" href="https://www.chess.com/ms/analysis" hreflang="ms" />
              <link rel="alternate" href="https://www.chess.com/pt-BR/a
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/ms/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20905"></a>
## FND-20905: https://www.chess.com/news

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/news",
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
  "id": "URL-01774"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19765.

```text
color"},"sub":[],"badge":null},{"id":"community.news","type":"link","label":"News","url":"https:\/\/www.chess.com\/news","icon":{"name":"page-news","variant":"color"},"sub":[],"badge":null},{"id":"community.ar
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 14729.

```text
color"},"sub":[],"badge":null},{"id":"community.news","type":"link","label":"News","url":"https:\/\/www.chess.com\/news","icon":{"name":"page-news","variant":"color"},"sub":[],"badge":null},{"id":"community.ar
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 19765.

```text
color"},"sub":[],"badge":null},{"id":"community.news","type":"link","label":"News","url":"https:\/\/www.chess.com\/news","icon":{"name":"page-news","variant":"color"},"sub":[],"badge":null},{"id":"community.ar
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/news>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20906"></a>
## FND-20906: https://www.chess.com/nl-BE/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/nl-BE/analysis",
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
  "id": "URL-01775"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9887.

```text
//www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/analysis" hreflang="nl-BE" />
              <link rel="alternate" href="https://www.chess.com/bn/a
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9887.

```text
//www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/analysis" hreflang="nl-BE" />
              <link rel="alternate" href="https://www.chess.com/bn/a
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/nl-BE/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20907"></a>
## FND-20907: https://www.chess.com/nl/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/nl/analysis",
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
  "id": "URL-01776"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6389.

```text
s://www.chess.com/ko/analysis" hreflang="ko" />
              <link rel="alternate" href="https://www.chess.com/nl/analysis" hreflang="nl" />
              <link rel="alternate" href="https://www.chess.com/hy/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 6389.

```text
s://www.chess.com/ko/analysis" hreflang="ko" />
              <link rel="alternate" href="https://www.chess.com/nl/analysis" hreflang="nl" />
              <link rel="alternate" href="https://www.chess.com/hy/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/nl/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20908"></a>
## FND-20908: https://www.chess.com/no/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/no/analysis",
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
  "id": "URL-01777"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7235.

```text
s://www.chess.com/lt/analysis" hreflang="lt" />
              <link rel="alternate" href="https://www.chess.com/no/analysis" hreflang="no" />
              <link rel="alternate" href="https://www.chess.com/ro/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 7235.

```text
s://www.chess.com/lt/analysis" hreflang="lt" />
              <link rel="alternate" href="https://www.chess.com/no/analysis" hreflang="no" />
              <link rel="alternate" href="https://www.chess.com/ro/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/no/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20909"></a>
## FND-20909: https://www.chess.com/openings

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/openings",
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
  "id": "URL-01778"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15591.

```text
r"},"sub":[],"badge":null},{"id":"learn.openings","type":"link","label":"Openings","url":"https:\/\/www.chess.com\/openings","icon":{"name":"book-stack-pawn","variant":"color"},"sub":[],"badge":null}],"badge":null
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10555.

```text
r"},"sub":[],"badge":null},{"id":"learn.openings","type":"link","label":"Openings","url":"https:\/\/www.chess.com\/openings","icon":{"name":"book-stack-pawn","variant":"color"},"sub":[],"badge":null}],"badge":null
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15591.

```text
r"},"sub":[],"badge":null},{"id":"learn.openings","type":"link","label":"Openings","url":"https:\/\/www.chess.com\/openings","icon":{"name":"book-stack-pawn","variant":"color"},"sub":[],"badge":null}],"badge":null
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/openings>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20910"></a>
## FND-20910: https://www.chess.com/openings/

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/openings/",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0067"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01779"
}

### Evidence

- **SRC-0067** `research/backups/review-v0.1.6.js` — [preserved redacted evidence](../evidence/text/db95e817f9f5c6df4271dbb73cab441c2310cfa0a26ca8fa2f1ed1794217fc3b.js)
  Character offset 21482.

```text
ing: opening ? {
      openingName: opening.name,
      ecoCode: opening.eco,
      url: 'https://www.chess.com/openings/' + opening.name.replace(/\s+/g, '-'),
      tcnMoves: opening.tcn,
    } : null,
  };

  
```

**Source references:** SRC-0067  
**URL references:** <https://www.chess.com/openings/>  
**Related findings:** FND-18888, FND-19170, FND-19178

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20911"></a>
## FND-20911: https://www.chess.com/openings/Queens-Gambit-Declined-Queens-Knight-Variation-3...dxc4-4.e4

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/openings/Queens-Gambit-Declined-Queens-Knight-Variation-3...dxc4-4.e4",
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
  "id": "URL-01780"
}

### Evidence

- **SRC-0127** `research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 301.

```text
ntPosition "8/8/1k6/p1r2nBp/8/8/PP6/K7 b - - 1 43"]
[Timezone "UTC"]
[ECO "D31"]
[ECOUrl "https://www.chess.com/openings/Queens-Gambit-Declined-Queens-Knight-Variation-3...dxc4-4.e4"]
[UTCDate "2026.11.13"]
[UTCTime "17:44:46"]
[WhiteElo "979"]
[BlackElo "1016"]
[TimeCon
```
- **SRC-2045** `torch-refinement-research.zip!/research/fixtures/human-game.pgn` — [preserved redacted evidence](../evidence/text/ce5eada5268e6670178f0cdb8a776408d483455467c98a4d5c2b5be4fb5ae174.pgn)
  Character offset 301.

```text
ntPosition "8/8/1k6/p1r2nBp/8/8/PP6/K7 b - - 1 43"]
[Timezone "UTC"]
[ECO "D31"]
[ECOUrl "https://www.chess.com/openings/Queens-Gambit-Declined-Queens-Knight-Variation-3...dxc4-4.e4"]
[UTCDate "2026.11.13"]
[UTCTime "17:44:46"]
[WhiteElo "979"]
[BlackElo "1016"]
[TimeCon
```

**Source references:** SRC-0127, SRC-2045  
**URL references:** <https://www.chess.com/openings/Queens-Gambit-Declined-Queens-Knight-Variation-3...dxc4-4.e4>  
**Related findings:** FND-20813, FND-21011

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20912"></a>
## FND-20912: https://www.chess.com/other

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/other",
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
  "id": "URL-01781"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20462.

```text
ull}],"badge":null}],"badge":null},{"id":"other","type":"dropdown","label":"Other","url":"https:\/\/www.chess.com\/other","icon":{"name":"ellipsis","variant":"color"},"sub":[{"id":"other.library","type":"link",
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 55880.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="other">
    


  <a
    href="https://www.chess.com/other"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 56946.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-other"
    data-primary-action="https://www.chess.com/other">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 15426.

```text
ull}],"badge":null}],"badge":null},{"id":"other","type":"dropdown","label":"Other","url":"https:\/\/www.chess.com\/other","icon":{"name":"ellipsis","variant":"color"},"sub":[{"id":"other.library","type":"link",
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 51044.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="other">
    


  <a
    href="https://www.chess.com/other"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 52110.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-other"
    data-primary-action="https://www.chess.com/other">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 20462.

```text
ull}],"badge":null}],"badge":null},{"id":"other","type":"dropdown","label":"Other","url":"https:\/\/www.chess.com\/other","icon":{"name":"ellipsis","variant":"color"},"sub":[{"id":"other.library","type":"link",
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 55880.

```text
esktop-wrapper sidebar-mobile-hidden"
    data-interaction="other">
    


  <a
    href="https://www.chess.com/other"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 56946.

```text
pper sidebar-desktop-hidden"
    data-interaction="mobile-other"
    data-primary-action="https://www.chess.com/other">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/other>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20913"></a>
## FND-20913: https://www.chess.com/pl/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/pl/analysis",
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
  "id": "URL-01782"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5543.

```text
s://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/analysis" hreflang="pl" />
              <link rel="alternate" href="https://www.chess.com/ru/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5543.

```text
s://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/analysis" hreflang="pl" />
              <link rel="alternate" href="https://www.chess.com/ru/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/pl/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20914"></a>
## FND-20914: https://www.chess.com/play

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play",
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
  "id": "URL-01783"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12463.

```text
userNavigationConfig = {"favorited":[{"id":"play","type":"dropdown","label":"Play","url":"https:\/\/www.chess.com\/play","icon":{"name":"play-white","variant":"color"},"sub":[{"id":"play.games","type":"section
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 42038.

```text
desktop-wrapper sidebar-mobile-hidden"
    data-interaction="play">
    


  <a
    href="https://www.chess.com/play"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 43390.

```text
apper sidebar-desktop-hidden"
    data-interaction="mobile-play"
    data-primary-action="https://www.chess.com/play">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 7427.

```text
userNavigationConfig = {"favorited":[{"id":"play","type":"dropdown","label":"Play","url":"https:\/\/www.chess.com\/play","icon":{"name":"play-white","variant":"color"},"sub":[{"id":"play.games","type":"section
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 37202.

```text
desktop-wrapper sidebar-mobile-hidden"
    data-interaction="play">
    


  <a
    href="https://www.chess.com/play"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 38554.

```text
apper sidebar-desktop-hidden"
    data-interaction="mobile-play"
    data-primary-action="https://www.chess.com/play">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12463.

```text
userNavigationConfig = {"favorited":[{"id":"play","type":"dropdown","label":"Play","url":"https:\/\/www.chess.com\/play","icon":{"name":"play-white","variant":"color"},"sub":[{"id":"play.games","type":"section
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 42038.

```text
desktop-wrapper sidebar-mobile-hidden"
    data-interaction="play">
    


  <a
    href="https://www.chess.com/play"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 43390.

```text
apper sidebar-desktop-hidden"
    data-interaction="mobile-play"
    data-primary-action="https://www.chess.com/play">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/play>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20915"></a>
## FND-20915: https://www.chess.com/play/coach?source=play_nav

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play/coach?source=play_nav",
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
  "id": "URL-01784"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13030.

```text
lor"},"sub":[],"badge":null},{"id":"play.coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15403.

```text
"sub":[],"badge":null},{"id":"learn.play_coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null},{"id":"learn.open
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 7994.

```text
lor"},"sub":[],"badge":null},{"id":"play.coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 10367.

```text
"sub":[],"badge":null},{"id":"learn.play_coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null},{"id":"learn.open
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13030.

```text
lor"},"sub":[],"badge":null},{"id":"play.coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null}],"badge":null},{"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 15403.

```text
"sub":[],"badge":null},{"id":"learn.play_coach","type":"link","label":"Play Coach","url":"https:\/\/www.chess.com\/play\/coach?source=play_nav","icon":{"name":"coach-david","variant":"color"},"sub":[],"badge":null},{"id":"learn.open
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/play/coach?source=play_nav>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20916"></a>
## FND-20916: https://www.chess.com/play/computer

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play/computer",
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
  "id": "URL-01785"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12858.

```text
color"},"sub":[],"badge":null},{"id":"play.bots","type":"link","label":"Play Bots","url":"https:\/\/www.chess.com\/play\/computer","icon":{"name":"device-bot","variant":"color"},"sub":[],"badge":null},{"id":"play.coach"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 7822.

```text
color"},"sub":[],"badge":null},{"id":"play.bots","type":"link","label":"Play Bots","url":"https:\/\/www.chess.com\/play\/computer","icon":{"name":"device-bot","variant":"color"},"sub":[],"badge":null},{"id":"play.coach"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12858.

```text
color"},"sub":[],"badge":null},{"id":"play.bots","type":"link","label":"Play Bots","url":"https:\/\/www.chess.com\/play\/computer","icon":{"name":"device-bot","variant":"color"},"sub":[],"badge":null},{"id":"play.coach"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/play/computer>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20917"></a>
## FND-20917: https://www.chess.com/play/online

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play/online",
  "type": "page_or_route_candidate",
  "reference_form": "absolute",
  "source_ids": [
    "SRC-0065",
    "SRC-0777",
    "SRC-0781",
    "SRC-1150"
  ],
  "directly_visited": "not established from literal alone",
  "verification_status": "observed literal only; not re-fetched during this audit",
  "date": "source-embedded date if present; filesystem time is not a verification date",
  "related_findings": [],
  "id": "URL-01786"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12690.

```text
l":null,"icon":null,"sub":[{"id":"play.online","type":"link","label":"Play Online","url":"https:\/\/www.chess.com\/play\/online","icon":{"name":"play-white","variant":"color"},"sub":[],"badge":null},{"id":"play.bots",
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 7654.

```text
l":null,"icon":null,"sub":[{"id":"play.online","type":"link","label":"Play Online","url":"https:\/\/www.chess.com\/play\/online","icon":{"name":"play-white","variant":"color"},"sub":[],"badge":null},{"id":"play.bots",
```
- **SRC-0781** `research/refinement/live-shared.eager.js` — [preserved redacted evidence](../evidence/text/9db47fa0bedaf16d5ca46c07aac80f2ff5eed2e0875d9c3584c03b6b1c92b91b.js)
  Character offset 344442.

```text
lease-history.md`],Iye={entries:[`play`],vendorBundleName:`play`,links:[{name:`Play`,url:`https://www.chess.com/play/online`}],featureFlags:[{name:`client_play_beta`,channel:`beta`}],sourceCodeUrl:`https://github.
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 12690.

```text
l":null,"icon":null,"sub":[{"id":"play.online","type":"link","label":"Play Online","url":"https:\/\/www.chess.com\/play\/online","icon":{"name":"play-white","variant":"color"},"sub":[],"badge":null},{"id":"play.bots",
```

**Source references:** SRC-0065, SRC-0777, SRC-0781, SRC-1150  
**URL references:** <https://www.chess.com/play/online>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20918"></a>
## FND-20918: https://www.chess.com/play/online/tournaments

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play/online/tournaments",
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
  "id": "URL-01787"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13476.

```text
sub":[],"badge":null},{"id":"play.tournaments","type":"link","label":"Tournaments","url":"https:\/\/www.chess.com\/play\/online\/tournaments","icon":{"name":"tournament-gold","variant":"color"},"sub":[],"badge":null},{"id":"play.v
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 8440.

```text
sub":[],"badge":null},{"id":"play.tournaments","type":"link","label":"Tournaments","url":"https:\/\/www.chess.com\/play\/online\/tournaments","icon":{"name":"tournament-gold","variant":"color"},"sub":[],"badge":null},{"id":"play.v
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 13476.

```text
sub":[],"badge":null},{"id":"play.tournaments","type":"link","label":"Tournaments","url":"https:\/\/www.chess.com\/play\/online\/tournaments","icon":{"name":"tournament-gold","variant":"color"},"sub":[],"badge":null},{"id":"play.v
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/play/online/tournaments>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20919"></a>
## FND-20919: https://www.chess.com/play/online/watch

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/play/online/watch",
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
  "id": "URL-01788"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17774.

```text
ub":[],"badge":null},{"id":"watch.playing_now","type":"link","label":"Playing Now","url":"https:\/\/www.chess.com\/play\/online\/watch","icon":{"name":"playing","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 12738.

```text
ub":[],"badge":null},{"id":"watch.playing_now","type":"link","label":"Playing Now","url":"https:\/\/www.chess.com\/play\/online\/watch","icon":{"name":"playing","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 17774.

```text
ub":[],"badge":null},{"id":"watch.playing_now","type":"link","label":"Playing Now","url":"https:\/\/www.chess.com\/play\/online\/watch","icon":{"name":"playing","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/play/online/watch>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20920"></a>
## FND-20920: https://www.chess.com/players

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/players",
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
  "id": "URL-01789"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18970.

```text
con":null,"sub":[{"id":"community.top_players","type":"link","label":"Top Players","url":"https:\/\/www.chess.com\/players","icon":{"name":"masters","variant":"color"},"sub":[],"badge":null},{"id":"community.rank
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 13934.

```text
con":null,"sub":[{"id":"community.top_players","type":"link","label":"Top Players","url":"https:\/\/www.chess.com\/players","icon":{"name":"masters","variant":"color"},"sub":[],"badge":null},{"id":"community.rank
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 18970.

```text
con":null,"sub":[{"id":"community.top_players","type":"link","label":"Top Players","url":"https:\/\/www.chess.com\/players","icon":{"name":"masters","variant":"color"},"sub":[],"badge":null},{"id":"community.rank
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/players>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20921"></a>
## FND-20921: https://www.chess.com/practice

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/practice",
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
  "id": "URL-01790"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16783.

```text
r"},"sub":[],"badge":null},{"id":"train.practice","type":"link","label":"Practice","url":"https:\/\/www.chess.com\/practice","icon":{"name":"game-practice","variant":"color"},"sub":[],"badge":null},{"id":"train.ai
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 11747.

```text
r"},"sub":[],"badge":null},{"id":"train.practice","type":"link","label":"Practice","url":"https:\/\/www.chess.com\/practice","icon":{"name":"game-practice","variant":"color"},"sub":[],"badge":null},{"id":"train.ai
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 16783.

```text
r"},"sub":[],"badge":null},{"id":"train.practice","type":"link","label":"Practice","url":"https:\/\/www.chess.com\/practice","icon":{"name":"game-practice","variant":"color"},"sub":[],"badge":null},{"id":"train.ai
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/practice>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20922"></a>
## FND-20922: https://www.chess.com/pt-BR/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/pt-BR/analysis",
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
  "id": "URL-01791"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9209.

```text
s://www.chess.com/ms/analysis" hreflang="ms" />
              <link rel="alternate" href="https://www.chess.com/pt-BR/analysis" hreflang="pt-BR" />
              <link rel="alternate" href="https://www.chess.com/sq/a
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 9209.

```text
s://www.chess.com/ms/analysis" hreflang="ms" />
              <link rel="alternate" href="https://www.chess.com/pt-BR/analysis" hreflang="pt-BR" />
              <link rel="alternate" href="https://www.chess.com/sq/a
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/pt-BR/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20923"></a>
## FND-20923: https://www.chess.com/pt/analysis

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/pt/analysis",
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
  "id": "URL-01792"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5919.

```text
s://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/analysis" hreflang="pt" />
              <link rel="alternate" href="https://www.chess.com/it/anal
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 5919.

```text
s://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/analysis" hreflang="pt" />
              <link rel="alternate" href="https://www.chess.com/it/anal
```

**Source references:** SRC-0065, SRC-1150  
**URL references:** <https://www.chess.com/pt/analysis>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-19911

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20924"></a>
## FND-20924: https://www.chess.com/puzzles

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/puzzles",
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
  "id": "URL-01793"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14041.

```text
],"badge":null}],"badge":null},{"id":"puzzles","type":"dropdown","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles","icon":{"name":"puzzle-piece","variant":"color"},"sub":[{"id":"puzzles.rated","type":"li
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 44791.

```text
ktop-wrapper sidebar-mobile-hidden"
    data-interaction="puzzles">
    


  <a
    href="https://www.chess.com/puzzles"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 45871.

```text
er sidebar-desktop-hidden"
    data-interaction="mobile-puzzles"
    data-primary-action="https://www.chess.com/puzzles">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9005.

```text
],"badge":null}],"badge":null},{"id":"puzzles","type":"dropdown","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles","icon":{"name":"puzzle-piece","variant":"color"},"sub":[{"id":"puzzles.rated","type":"li
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 39955.

```text
ktop-wrapper sidebar-mobile-hidden"
    data-interaction="puzzles">
    


  <a
    href="https://www.chess.com/puzzles"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 41035.

```text
er sidebar-desktop-hidden"
    data-interaction="mobile-puzzles"
    data-primary-action="https://www.chess.com/puzzles">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14041.

```text
],"badge":null}],"badge":null},{"id":"puzzles","type":"dropdown","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles","icon":{"name":"puzzle-piece","variant":"color"},"sub":[{"id":"puzzles.rated","type":"li
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 44791.

```text
ktop-wrapper sidebar-mobile-hidden"
    data-interaction="puzzles">
    


  <a
    href="https://www.chess.com/puzzles"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 45871.

```text
er sidebar-desktop-hidden"
    data-interaction="mobile-puzzles"
    data-primary-action="https://www.chess.com/puzzles">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/puzzles>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20925"></a>
## FND-20925: https://www.chess.com/puzzles/battle

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/puzzles/battle",
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
  "id": "URL-01794"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14726.

```text
sub":[],"badge":null},{"id":"puzzles.battle","type":"link","label":"Puzzle Battle","url":"https:\/\/www.chess.com\/puzzles\/battle","icon":{"name":"battle","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.custom"
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9690.

```text
sub":[],"badge":null},{"id":"puzzles.battle","type":"link","label":"Puzzle Battle","url":"https:\/\/www.chess.com\/puzzles\/battle","icon":{"name":"battle","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.custom"
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14726.

```text
sub":[],"badge":null},{"id":"puzzles.battle","type":"link","label":"Puzzle Battle","url":"https:\/\/www.chess.com\/puzzles\/battle","icon":{"name":"battle","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.custom"
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/puzzles/battle>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20926"></a>
## FND-20926: https://www.chess.com/puzzles/learning

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/puzzles/learning",
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
  "id": "URL-01795"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14903.

```text
ub":[],"badge":null},{"id":"puzzles.custom","type":"link","label":"Custom Puzzles","url":"https:\/\/www.chess.com\/puzzles\/learning","icon":{"name":"book-open-knight","variant":"color"},"sub":[],"badge":null}],"badge":nul
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9867.

```text
ub":[],"badge":null},{"id":"puzzles.custom","type":"link","label":"Custom Puzzles","url":"https:\/\/www.chess.com\/puzzles\/learning","icon":{"name":"book-open-knight","variant":"color"},"sub":[],"badge":null}],"badge":nul
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14903.

```text
ub":[],"badge":null},{"id":"puzzles.custom","type":"link","label":"Custom Puzzles","url":"https:\/\/www.chess.com\/puzzles\/learning","icon":{"name":"book-open-knight","variant":"color"},"sub":[],"badge":null}],"badge":nul
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/puzzles/learning>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20927"></a>
## FND-20927: https://www.chess.com/puzzles/rated

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/puzzles/rated",
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
  "id": "URL-01796"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14192.

```text
e","variant":"color"},"sub":[{"id":"puzzles.rated","type":"link","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles\/rated","icon":{"name":"puzzle-piece","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.d
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9156.

```text
e","variant":"color"},"sub":[{"id":"puzzles.rated","type":"link","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles\/rated","icon":{"name":"puzzle-piece","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.d
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14192.

```text
e","variant":"color"},"sub":[{"id":"puzzles.rated","type":"link","label":"Puzzles","url":"https:\/\/www.chess.com\/puzzles\/rated","icon":{"name":"puzzle-piece","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.d
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/puzzles/rated>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20928"></a>
## FND-20928: https://www.chess.com/puzzles/rush

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/puzzles/rush",
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
  "id": "URL-01797"
}

### Evidence

- **SRC-0065** `research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14547.

```text
"},"sub":[],"badge":null},{"id":"puzzles.rush","type":"link","label":"Puzzle Rush","url":"https:\/\/www.chess.com\/puzzles\/rush","icon":{"name":"puzzle-rush","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.ba
```
- **SRC-0777** `research/refinement/live-game-page.html` — [preserved redacted evidence](../evidence/text/c620bab98feeceb50732cb2e87f9ff7ec49340d83943841046cdba10d42afb7e.html)
  Character offset 9511.

```text
"},"sub":[],"badge":null},{"id":"puzzles.rush","type":"link","label":"Puzzle Rush","url":"https:\/\/www.chess.com\/puzzles\/rush","icon":{"name":"puzzle-rush","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.ba
```
- **SRC-1150** `research.zip!/research/analysis.html` — [preserved redacted evidence](../evidence/text/dd701ae48361bdb568b755b2a84bd76fe5a8fe1297957a55bf98d2388fce84c7.html)
  Character offset 14547.

```text
"},"sub":[],"badge":null},{"id":"puzzles.rush","type":"link","label":"Puzzle Rush","url":"https:\/\/www.chess.com\/puzzles\/rush","icon":{"name":"puzzle-rush","variant":"color"},"sub":[],"badge":null},{"id":"puzzles.ba
```

**Source references:** SRC-0065, SRC-0777, SRC-1150  
**URL references:** <https://www.chess.com/puzzles/rush>  
**Related findings:** FND-18977, FND-19909, FND-19910, FND-18979

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20929"></a>
## FND-20929: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js",
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
  "id": "URL-01798",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/javascript; charset=utf-8 0.229019",
      "source_id": "SRC-0202",
      "line": 7,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 834.

```text
/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 210.

```text
s.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 834.

```text
/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 210.

```text
s.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20930"></a>
## FND-20930: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm",
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
  "id": "URL-01799",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm",
      "http_status": 404,
      "size_download": 27150,
      "content_type_and_optional_elapsed": "text/html 0.151944",
      "source_id": "SRC-0202",
      "line": 4,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 418.

```text
gine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 280.

```text
anation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 418.

```text
gine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 280.

```text
anation-engine.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js
https://www.
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.

<a id="FND-20931"></a>
## FND-20931: https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js

**Category:** url_references  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "url": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js",
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
  "id": "URL-01800",
  "historical_http_observations": [
    {
      "target_literal": "https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js",
      "http_status": 206,
      "size_download": 1,
      "content_type_and_optional_elapsed": "text/javascript; charset=utf-8 0.305896",
      "source_id": "SRC-0202",
      "line": 10,
      "request_method": "GET",
      "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
    }
  ]
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1267.

```text
2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess
```
- **SRC-1147** `research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 508.

```text
697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.
```
- **SRC-1162** `research.zip!/research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1267.

```text
2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess
```
- **SRC-1174** `research.zip!/research/urls.txt` — [preserved redacted evidence](../evidence/text/df965571b48133552caefbb4b552ba4cafcde273f2be5357a7fc413da1e6a781.txt)
  Character offset 508.

```text
697050e.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm
https://www.
```

**Source references:** SRC-0202, SRC-1147, SRC-1162, SRC-1174  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js>  
**Related findings:** FND-18975, FND-18976, FND-18986, FND-20808, FND-20832

**Additional notes:** URL/reference extracted from source, not evidence that this URL is reachable. See urls.jsonl for every occurrence and context.
