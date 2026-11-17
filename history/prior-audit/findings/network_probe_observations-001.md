# network_probe_observations — findings 1–44

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18986"></a>
## FND-18986: Historical GET probe https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 0.

```text
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.wasm>  
**Related findings:** FND-18975, FND-18976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18987"></a>
## FND-18987: Historical GET probe https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 138.

```text
engine/explanation-engine/1.130.212/default/explanation-engine.wasm 206 1 application/wasm 0.076822
https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-en
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/explanation-engine/1.130.212/default/explanation-engine.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18988"></a>
## FND-18988: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 288.

```text
nation-engine/1.130.212/default/explanation-engine.js 206 1 text/javascript; charset=utf-8 0.112791
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-s
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18989"></a>
## FND-18989: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 418.

```text
s-chess-engine/Torch/torch-2-single-697050e.wasm                       404 27150 text/html 0.150929
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.com/r2/client-packages/an
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18990"></a>
## FND-18990: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 548.

```text
s-chess-engine/Torch/torch-2-85193a7.wasm                              404 27150 text/html 0.151944
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/r2/assets-ch
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-single-697050e.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18991"></a>
## FND-18991: Historical GET probe https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 695.

```text
rch/torch-2-single-697050e.js                         206 1 text/javascript; charset=utf-8 0.186076
https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.chess.com/r2/client-pa
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/client-packages/analysis/2026.11.7/analysis.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18992"></a>
## FND-18992: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 834.

```text
s/analysis/2026.11.7/analysis.js                              206 1 application/javascript 0.044203
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-ch
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-85193a7.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18993"></a>
## FND-18993: Historical GET probe https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 981.

```text
rch/torch-2-85193a7.js                                206 1 text/javascript; charset=utf-8 0.229019
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2/assets-ch
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18994"></a>
## FND-18994: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1120.

```text
s/play-computer/2026.11.5/play-computer.js                    206 1 application/javascript 0.046749
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bund
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18995"></a>
## FND-18995: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1267.

```text
rch/torch-2-lite-single-a809e6e.js                    206 1 text/javascript; charset=utf-8 0.176903
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18996"></a>
## FND-18996: Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1414.

```text
rch/torch-2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/assets-chess-engine/Torc
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18997"></a>
## FND-18997: Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1557.

```text
/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js   
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18998"></a>
## FND-18998: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1685.

```text
s/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
https://www.chess.com/r2/assets-chess-engine
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-single-a809e6e.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18999"></a>
## FND-18999: Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1818.

```text
hess-engine/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19000"></a>
## FND-19000: Historical GET probe https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 1961.

```text
/stockfish.js                                             200 93567 application/javascript 0.147183
https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stock
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/r2/assets-chess-engine/Torch/torch-2-lite-aff3c0c.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19001"></a>
## FND-19001: Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2094.

```text
hess-engine/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19002"></a>
## FND-19002: Historical GET probe https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2232.

```text
ngine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
https://www.chess.com/robots.txt       
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19003"></a>
## FND-19003: Historical GET probe https://www.chess.com/bundles/app/js/engine/torch.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2370.

```text
ngine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
https://www.chess.com/robots.txt                                                                     200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/ap
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19004"></a>
## FND-19004: Historical GET probe https://www.chess.com/robots.txt

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2513.

```text
/torch.js                                                 200 35359 application/javascript 0.139400
https://www.chess.com/robots.txt                                                                     200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/ap
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/robots.txt>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19005"></a>
## FND-19005: Historical GET probe https://www.chess.com/bundles/app/js/engine/torch-lite.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2658.

```text
                                                        200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch-lite.js>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19006"></a>
## FND-19006: Historical GET probe https://www.chess.com/bundles/app/js/engine/books/eco.json

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2801.

```text
/torch-lite.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af115
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/books/eco.json>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19007"></a>
## FND-19007: Historical GET probe https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 2941.

```text
ine/books/eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analysis                                    
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19008"></a>
## FND-19008: Historical GET probe https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3068.

```text
es/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analysis                                                                       200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/tor
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19009"></a>
## FND-19009: Historical GET probe https://www.chess.com/analysis

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "https://www.chess.com/analysis",
  "http_status": 200,
  "size_download": 113132,
  "content_type_and_optional_elapsed": "text/html; charset=UTF-8 0.252476",
  "source_id": "SRC-0202",
  "line": 24,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3195.

```text
es/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analysis                                                                       200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/
```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/analysis>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19010"></a>
## FND-19010: Historical GET probe https://www.chess.com/bundles/app/js/engine/torch.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3341.

```text
                                                       200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19011"></a>
## FND-19011: Historical GET probe https://www.chess.com/bundles/app/js/engine/torch-lite.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

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

### Evidence

- **SRC-0202** `research/probe-results.txt` — [preserved redacted evidence](../evidence/text/c2d9ded354ef28c52fe4f639281eb57b246dda0121097b9e8b0224a4739bb8d7.txt)
  Character offset 3481.

```text
ine/torch.wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```

**Source references:** SRC-0202  
**URL references:** <https://www.chess.com/bundles/app/js/engine/torch-lite.wasm>  
**Related findings:** FND-18975, FND-18976, FND-18986

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19012"></a>
## FND-19012: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-Worker.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-no-Worker.js",
  "http_status": 200,
  "size_download": 42981,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 1,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 0.

```text
bundles/app/js/engine/stockfish-nnue-16-no-Worker.js                                            200 42981 application/javascript
bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm                                          200 693497 application/wasm
bundles/app/js/engine/stockfish-nnue-16-single.js                  
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19013"></a>
## FND-19013: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm",
  "http_status": 200,
  "size_download": 693497,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 2,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 129.

```text
sh-nnue-16-no-Worker.js                                            200 42981 application/javascript
bundles/app/js/engine/stockfish-nnue-16-no-Worker.wasm                                          200 693497 application/wasm
bundles/app/js/engine/stockfish-nnue-16-single.js                                               200 26003 application/javascript
bundles/app/js/engine/stockfish-nnue-16-single.wasm                
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19014"></a>
## FND-19014: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-single.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-single.js",
  "http_status": 200,
  "size_download": 26003,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 3,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 253.

```text
ockfish-nnue-16-no-Worker.wasm                                          200 693497 application/wasm
bundles/app/js/engine/stockfish-nnue-16-single.js                                               200 26003 application/javascript
bundles/app/js/engine/stockfish-nnue-16-single.wasm                                             200 574106 application/wasm
bundles/app/js/engine/stockfish-single.js                          
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19015"></a>
## FND-19015: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-single.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-single.wasm",
  "http_status": 200,
  "size_download": 574106,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 4,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 382.

```text
sh-nnue-16-single.js                                               200 26003 application/javascript
bundles/app/js/engine/stockfish-nnue-16-single.wasm                                             200 574106 application/wasm
bundles/app/js/engine/stockfish-single.js                                                       200 2234930 application/javascript
bundles/app/js/engine/stockfish-single.wasm                      
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19016"></a>
## FND-19016: Historical GET probe bundles/app/js/engine/stockfish-single.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-single.js",
  "http_status": 200,
  "size_download": 2234930,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 5,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 506.

```text
ockfish-nnue-16-single.wasm                                             200 574106 application/wasm
bundles/app/js/engine/stockfish-single.js                                                       200 2234930 application/javascript
bundles/app/js/engine/stockfish-single.wasm                                                     200 1381822 application/wasm
bundles/app/js/engine/stockfish-nnue-16-no-simd.js              
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19017"></a>
## FND-19017: Historical GET probe bundles/app/js/engine/stockfish-single.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-single.wasm",
  "http_status": 200,
  "size_download": 1381822,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 6,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 637.

```text
-single.js                                                       200 2234930 application/javascript
bundles/app/js/engine/stockfish-single.wasm                                                     200 1381822 application/wasm
bundles/app/js/engine/stockfish-nnue-16-no-simd.js                                              200 40939 application/javascript
bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm              
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19018"></a>
## FND-19018: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-simd.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-no-simd.js",
  "http_status": 200,
  "size_download": 40939,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 7,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 762.

```text
ckfish-single.wasm                                                     200 1381822 application/wasm
bundles/app/js/engine/stockfish-nnue-16-no-simd.js                                              200 40939 application/javascript
bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm                                            200 697387 application/wasm
bundles/app/js/engine/stockfish.asm.js                             
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19019"></a>
## FND-19019: Historical GET probe bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm",
  "http_status": 200,
  "size_download": 697387,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 8,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 891.

```text
sh-nnue-16-no-simd.js                                              200 40939 application/javascript
bundles/app/js/engine/stockfish-nnue-16-no-simd.wasm                                            200 697387 application/wasm
bundles/app/js/engine/stockfish.asm.js                                                          200 4820790 application/javascript
bundles/app/js/engine/book-small.json                            
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19020"></a>
## FND-19020: Historical GET probe bundles/app/js/engine/stockfish.asm.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/stockfish.asm.js",
  "http_status": 200,
  "size_download": 4820790,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 9,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1015.

```text
ockfish-nnue-16-no-simd.wasm                                            200 697387 application/wasm
bundles/app/js/engine/stockfish.asm.js                                                          200 4820790 application/javascript
bundles/app/js/engine/book-small.json                                                           200 2140353 application/json
bundles/app/js/vendor/explanation-engine/explanation-engine.js  
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19021"></a>
## FND-19021: Historical GET probe bundles/app/js/engine/book-small.json

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/engine/book-small.json",
  "http_status": 200,
  "size_download": 2140353,
  "content_type_and_optional_elapsed": "application/json",
  "source_id": "SRC-0204",
  "line": 10,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1146.

```text
.asm.js                                                          200 4820790 application/javascript
bundles/app/js/engine/book-small.json                                                           200 2140353 application/json
bundles/app/js/vendor/explanation-engine/explanation-engine.js                                  200 108056 application/javascript
bundles/app/js/vendor/explanation-engine/explanation-engine.wasm 
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19022"></a>
## FND-19022: Historical GET probe bundles/app/js/vendor/explanation-engine/explanation-engine.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/vendor/explanation-engine/explanation-engine.js",
  "http_status": 200,
  "size_download": 108056,
  "content_type_and_optional_elapsed": "application/javascript",
  "source_id": "SRC-0204",
  "line": 11,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1271.

```text
k-small.json                                                           200 2140353 application/json
bundles/app/js/vendor/explanation-engine/explanation-engine.js                                  200 108056 application/javascript
bundles/app/js/vendor/explanation-engine/explanation-engine.wasm                                200 32922478 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/default/expl
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19023"></a>
## FND-19023: Historical GET probe bundles/app/js/vendor/explanation-engine/explanation-engine.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "bundles/app/js/vendor/explanation-engine/explanation-engine.wasm",
  "http_status": 200,
  "size_download": 32922478,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 12,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1401.

```text
ion-engine/explanation-engine.js                                  200 108056 application/javascript
bundles/app/js/vendor/explanation-engine/explanation-engine.wasm                                200 32922478 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/default/e
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19024"></a>
## FND-19024: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "text/javascript; charset=utf-8",
  "source_id": "SRC-0204",
  "line": 13,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1527.

```text
anation-engine/explanation-engine.wasm                                200 32922478 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanat
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19025"></a>
## FND-19025: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 14,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1660.

```text
n-engine/1.130.285/default/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/default/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanat
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19026"></a>
## FND-19026: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "text/javascript; charset=utf-8",
  "source_id": "SRC-0204",
  "line": 15,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1779.

```text
ine/explanation-engine/1.130.285/default/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanat
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19027"></a>
## FND-19027: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 16,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 1912.

```text
n-engine/1.130.285/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanat
```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19028"></a>
## FND-19028: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.js

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.js",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "text/javascript; charset=utf-8",
  "source_id": "SRC-0204",
  "line": 17,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 2031.

```text
ine/explanation-engine/1.130.285/no-simd/explanation-engine.wasm             206 1 application/wasm
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm             206 1 application/wasm

```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-19029"></a>
## FND-19029: Historical GET probe r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm

**Category:** network_probe_observations  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "target_literal": "r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm",
  "http_status": 206,
  "size_download": 1,
  "content_type_and_optional_elapsed": "application/wasm",
  "source_id": "SRC-0204",
  "line": 18,
  "request_method": "GET",
  "range": "bytes=0-0 for probe-results per probe.sh; probe2 invocation not independently preserved"
}

### Evidence

- **SRC-0204** `research/probe2.txt` — [preserved redacted evidence](../evidence/text/4ac664979de9b0f7962f0ad3f6ac5119bedac8f5cff0470939c11781d021c790.txt)
  Character offset 2164.

```text
n-engine/1.130.212/no-simd/explanation-engine.js               206 1 text/javascript; charset=utf-8
r2/assets-chess-engine/explanation-engine/1.130.212/no-simd/explanation-engine.wasm             206 1 application/wasm

```

**Source references:** SRC-0204  
**URL references:** None independently associated  
**Related findings:** FND-19012, FND-19013, FND-19014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
