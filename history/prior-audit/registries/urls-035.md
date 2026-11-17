# URL and reference inventory

[Master index](../00_MASTER_INDEX.md)

## URL-01701

<https://www.chess.com/bundles/app/js/engine/books/eco.json>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20832](../findings/url_references-018.md#FND-20832), [FND-19006](../findings/network_probe_observations-001.md#FND-19006).

### SRC-0202 at character 2801

```text
e.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://
```

### SRC-1147 at character 1521

```text
s/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bu
```

### SRC-1162 at character 2801

```text
e.js                                            200 35368 application/javascript 0.160463
https://www.chess.com/bundles/app/js/engine/books/eco.json                                           200 30873759 application/json 0.199615
https://
```

### SRC-1174 at character 1521

```text
s/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bu
```

## URL-01702

<https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 206; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20833](../findings/url_references-018.md#FND-20833), [FND-19008](../findings/network_probe_observations-001.md#FND-19008).

### SRC-0202 at character 3068

```text
engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analy
```

### SRC-1147 at character 1580

```text
/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/an
```

### SRC-1162 at character 3068

```text
engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue                                     206 1 text/plain 0.171573
https://www.chess.com/analy
```

### SRC-1174 at character 1580

```text
/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/an
```

## URL-01703

<https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 206; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20834](../findings/url_references-018.md#FND-20834), [FND-19007](../findings/network_probe_observations-001.md#FND-19007).

### SRC-0202 at character 2941

```text
eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundl
```

### SRC-1147 at character 1645

```text
js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```

### SRC-1162 at character 2941

```text
eco.json                                           200 30873759 application/json 0.199615
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue                                     206 1 text/plain 0.138668
https://www.chess.com/bundl
```

### SRC-1174 at character 1645

```text
js/engine/books/eco.json
https://www.chess.com/bundles/app/js/engine/nn-5af11540bbfe.nnue
https://www.chess.com/bundles/app/js/engine/nn-ad9b42354671.nnue
https://www.chess.com/analysis
https://www.chess.com/robots.txt

```

## URL-01704

<https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 404; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20835](../findings/url_references-018.md#FND-20835), [FND-18997](../findings/network_probe_observations-001.md#FND-18997).

### SRC-0202 at character 1557

```text
-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/ass
```

### SRC-1147 at character 980

```text
ysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bu
```

### SRC-1162 at character 1557

```text
-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js                                   404 548 text/html 0.163742
https://www.chess.com/r2/ass
```

### SRC-1174 at character 980

```text
ysis.js
https://www.chess.com/r2/client-packages/play-computer/2026.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bu
```

## URL-01705

<https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20836](../findings/url_references-018.md#FND-20836), [FND-18996](../findings/network_probe_observations-001.md#FND-18996).

### SRC-0202 at character 1414

```text
2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www
```

### SRC-1147 at character 1047

```text
.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/
```

### SRC-1162 at character 1414

```text
2-lite-aff3c0c.js                           206 1 text/javascript; charset=utf-8 0.305896
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js                                     200 40876 application/javascript 0.138553
https://www
```

### SRC-1174 at character 1047

```text
.11.5/play-computer.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/
```

## URL-01706

<https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20837](../findings/url_references-018.md#FND-20837), [FND-19002](../findings/network_probe_observations-001.md#FND-19002).

### SRC-0202 at character 2232

```text
kfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.
```

### SRC-1147 at character 1112

```text
e/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/ap
```

### SRC-1162 at character 2232

```text
kfish.wasm                                           200 385560 application/wasm 0.181921
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.
```

### SRC-1174 at character 1112

```text
e/stockfish-nnue-16.1.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/ap
```

## URL-01707

<https://www.chess.com/bundles/app/js/engine/stockfish.js>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20838](../findings/url_references-018.md#FND-20838), [FND-18999](../findings/network_probe_observations-001.md#FND-18999).

### SRC-0202 at character 1818

```text
e/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
htt
```

### SRC-1147 at character 1179

```text
e/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/
```

### SRC-1162 at character 1818

```text
e/Torch/torch-2-lite-single-a809e6e.wasm                  206 1 application/wasm 0.264840
https://www.chess.com/bundles/app/js/engine/stockfish.js                                             200 93567 application/javascript 0.147183
htt
```

### SRC-1174 at character 1179

```text
e/stockfish-nnue-16.js
https://www.chess.com/bundles/app/js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/
```

## URL-01708

<https://www.chess.com/bundles/app/js/engine/stockfish.wasm>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20839](../findings/url_references-018.md#FND-20839), [FND-19001](../findings/network_probe_observations-001.md#FND-19001).

### SRC-0202 at character 2094

```text
e/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://ww
```

### SRC-1147 at character 1236

```text
js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js
```

### SRC-1162 at character 2094

```text
e/Torch/torch-2-lite-aff3c0c.wasm                         206 1 application/wasm 0.431104
https://www.chess.com/bundles/app/js/engine/stockfish.wasm                                           200 385560 application/wasm 0.181921
https://ww
```

### SRC-1174 at character 1236

```text
js/engine/stockfish-nnue-16.wasm
https://www.chess.com/bundles/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js
```

## URL-01709

<https://www.chess.com/bundles/app/js/engine/torch-lite.js>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20840](../findings/url_references-018.md#FND-20840), [FND-19005](../findings/network_probe_observations-001.md#FND-19005).

### SRC-0202 at character 2658

```text
                                              200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
http
```

### SRC-1147 at character 1403

```text
com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles
```

### SRC-1162 at character 2658

```text
                                              200 4197 text/plain; charset=UTF-8 0.052364
https://www.chess.com/bundles/app/js/engine/torch-lite.js                                            200 35368 application/javascript 0.160463
http
```

### SRC-1174 at character 1403

```text
com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles
```

## URL-01710

<https://www.chess.com/bundles/app/js/engine/torch-lite.wasm>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20841](../findings/url_references-018.md#FND-20841), [FND-19011](../findings/network_probe_observations-001.md#FND-19011).

### SRC-0202 at character 3481

```text
wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```

### SRC-1147 at character 1461

```text
undles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/
```

### SRC-1162 at character 3481

```text
wasm                                               200 47327363 application/wasm 0.731200
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm                                          200 6840976 application/wasm 1.076223

```

### SRC-1174 at character 1461

```text
undles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/app/js/engine/torch-lite.wasm
https://www.chess.com/bundles/app/js/engine/books/eco.json
https://www.chess.com/bundles/
```

## URL-01711

<https://www.chess.com/bundles/app/js/engine/torch.js>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20842](../findings/url_references-018.md#FND-20842), [FND-19003](../findings/network_probe_observations-001.md#FND-19003).

### SRC-0202 at character 2370

```text
kfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
```

### SRC-1147 at character 1295

```text
les/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/
```

### SRC-1162 at character 2370

```text
kfish-nnue-16.wasm                                   200 707847 application/wasm 0.205290
https://www.chess.com/bundles/app/js/engine/torch.js                                                 200 35359 application/javascript 0.139400
```

### SRC-1174 at character 1295

```text
les/app/js/engine/stockfish.js
https://www.chess.com/bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/
```

## URL-01712

<https://www.chess.com/bundles/app/js/engine/torch.wasm>

- Type: asset; form: absolute.
- Visited: Historical GET probe recorded; see source and byte-range caveat..
- Verified: Historical HTTP status 200; not re-fetched in this audit..
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20843](../findings/url_references-018.md#FND-20843), [FND-19010](../findings/network_probe_observations-001.md#FND-19010).

### SRC-0202 at character 3341

```text
                                             200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
http
```

### SRC-1147 at character 1348

```text
bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/a
```

### SRC-1162 at character 3341

```text
                                             200 113132 text/html; charset=UTF-8 0.252476
https://www.chess.com/bundles/app/js/engine/torch.wasm                                               200 47327363 application/wasm 0.731200
http
```

### SRC-1174 at character 1348

```text
bundles/app/js/engine/stockfish.wasm
https://www.chess.com/bundles/app/js/engine/torch.js
https://www.chess.com/bundles/app/js/engine/torch.wasm
https://www.chess.com/bundles/app/js/engine/torch-lite.js
https://www.chess.com/bundles/a
```

## URL-01713

<https://www.chess.com/bundles/web/images/brand/chesscom_pawn.5dfdea51.png>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20844](../findings/url_references-018.md#FND-20844).

### SRC-0065 at character 10843

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

### SRC-0777 at character 5807

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

### SRC-1150 at character 10843

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

## URL-01714

<https://www.chess.com/bundles/web/images/color-icons/commerce-adfree.b6edf890.svg>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20845](../findings/url_references-018.md#FND-20845).

### SRC-0065 at character 81730

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```

### SRC-0777 at character 80986

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```

### SRC-1150 at character 81730

```text
25","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-adfree.b6edf890.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"no_ads","mem
```

## URL-01715

<https://www.chess.com/bundles/web/images/color-icons/commerce-diamond.79625166.svg>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20846](../findings/url_references-018.md#FND-20846).

### SRC-0065 at character 79497

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

### SRC-0065 at character 80220

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

### SRC-0777 at character 78753

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

### SRC-0777 at character 79476

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

### SRC-1150 at character 79497

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

### SRC-1150 at character 80220

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-diamond.79625166.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"diamond","me
```

## URL-01716

<https://www.chess.com/bundles/web/images/color-icons/commerce-gold.24e164aa.svg>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20847](../findings/url_references-018.md#FND-20847).

### SRC-0065 at character 76456

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

### SRC-0065 at character 77030

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

### SRC-0777 at character 75712

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

### SRC-0777 at character 76286

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

### SRC-1150 at character 76456

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

### SRC-1150 at character 77030

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-gold.24e164aa.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"gold","membe
```

## URL-01717

<https://www.chess.com/bundles/web/images/color-icons/commerce-platinum.a2bfab84.svg>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20848](../findings/url_references-018.md#FND-20848).

### SRC-0065 at character 77615

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-0065 at character 78246

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-0065 at character 78871

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-0777 at character 76871

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-0777 at character 77502

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-0777 at character 78127

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-1150 at character 77615

```text
2","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_MONTH"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-1150 at character 78246

```text
024","subscription":{"length":7,"unit":"SUBSCRIPTION_UNIT_DAY"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

### SRC-1150 at character 78871

```text
22","subscription":{"length":1,"unit":"SUBSCRIPTION_UNIT_YEAR"},"description":"","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/commerce-platinum.a2bfab84.svg","productType":"PRODUCT_TYPE_MEMBERSHIP","membershipProductDetails":{"code":"platinum","m
```

## URL-01718

<https://www.chess.com/bundles/web/images/color-icons/heart-green.b65098b1.svg>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20849](../findings/url_references-018.md#FND-20849).

### SRC-0065 at character 81000

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```

### SRC-0777 at character 80256

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```

### SRC-1150 at character 81000

```text
CRIPTION_UNIT_YEAR"},"description":"Unlimited access to all Chess.com features!","image":"https:\/\/www.chess.com\/bundles\/web\/images\/color-icons\/heart-green.b65098b1.svg","productType":"PRODUCT_TYPE_GROUP_MEMBERSHIP","membershipProductDetails":{"code":"diamon
```

## URL-01719

<https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20850](../findings/url_references-018.md#FND-20850).

### SRC-0065 at character 4373

```text
eta property="og:type" content="website" />

          <meta property="og:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

          <meta property="og:site_name" content="Chess.com" />

  
    
          <m
```

### SRC-0065 at character 5013

```text
ersonalized insights from Game Review." />

          <meta name="twitter:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analys
```

### SRC-1150 at character 4373

```text
eta property="og:type" content="website" />

          <meta property="og:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

          <meta property="og:site_name" content="Chess.com" />

  
    
          <m
```

### SRC-1150 at character 5013

```text
ersonalized insights from Game Review." />

          <meta name="twitter:image" content="https://www.chess.com/bundles/web/images/social/share-analysis-board.4b839d53.png" />

  
  
        
  
          <link rel="alternate" href="https://www.chess.com/analys
```

## URL-01720

<https://www.chess.com/bundles/web/images/webgl_data>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20851](../findings/url_references-018.md#FND-20851).

### SRC-0781 at character 180188

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function ene(e,t){return!t.api.boardImages.isIni
```

### SRC-1137 at character 195845

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function Ite(e,t){return!t.api.boardImages.isIni
```

### SRC-1165 at character 195845

```text
.com/chess-themes/sounds/`,webglAssetPaths:`__CHESSCOM_WEBGL_ASSET_PATHS__`,webglDataUrl:`https://www.chess.com/bundles/web/images/webgl_data`,webglDataUrlDev:`static/webgl_data`}}));function Ite(e,t){return!t.api.boardImages.isIni
```

## URL-01721

<https://www.chess.com/bundles/web/sounds>

- Type: asset; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20852](../findings/url_references-018.md#FND-20852).

### SRC-0781 at character 180015

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```

### SRC-1137 at character 195672

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```

### SRC-1165 at character 195672

```text
={enPassant:`https://www.chess.com/article/view/how-to-capture-en-passant`,soundsDefault:`https://www.chess.com/bundles/web/sounds`,soundsTheme:`https://images.chesscomfiles.com/chess-themes/sounds/`,webglAssetPaths:`__C
```

## URL-01722

<https://www.chess.com/ca/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20853](../findings/url_references-018.md#FND-20853).

### SRC-0065 at character 10175

```text
s://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/anal
```

### SRC-1150 at character 10175

```text
s://www.chess.com/tk/analysis" hreflang="tk" />
              <link rel="alternate" href="https://www.chess.com/ca/analysis" hreflang="ca" />
              <link rel="alternate" href="https://www.chess.com/ur/anal
```

## URL-01723

<https://www.chess.com/calculator>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20854](../findings/url_references-018.md#FND-20854).

### SRC-0065 at character 22913

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```

### SRC-0777 at character 17877

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```

### SRC-1150 at character 22913

```text
"sub":[],"badge":null},{"id":"other.calculator","type":"link","label":"Calculator","url":"https:\/\/www.chess.com\/calculator","icon":{"name":"board-2x2-calculated","variant":"color"},"sub":[],"badge":null}],"badge"
```

## URL-01724

<https://www.chess.com/classroom>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20855](../findings/url_references-018.md#FND-20855).

### SRC-0065 at character 16444

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```

### SRC-0777 at character 11408

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```

### SRC-1150 at character 16444

```text
},"sub":[],"badge":null},{"id":"train.classroom","type":"link","label":"Classroom","url":"https:\/\/www.chess.com\/classroom","icon":{"name":"classroom","variant":"color"},"sub":[],"badge":null},{"id":"train.endgam
```

## URL-01725

<https://www.chess.com/clubs>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20856](../findings/url_references-018.md#FND-20856).

### SRC-0065 at character 18364

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```

### SRC-0777 at character 13328

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```

### SRC-1150 at character 18364

```text
lor"},"sub":[],"badge":null},{"id":"community.clubs","type":"link","label":"Clubs","url":"https:\/\/www.chess.com\/clubs","icon":{"name":"clubs","variant":"color"},"sub":[],"badge":null},{"id":"community.member
```

## URL-01726

<https://www.chess.com/coaches>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20857](../findings/url_references-018.md#FND-20857).

### SRC-0065 at character 18690

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```

### SRC-0777 at character 13654

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```

### SRC-1150 at character 18690

```text
},"sub":[],"badge":null},{"id":"community.coaches","type":"link","label":"Coaches","url":"https:\/\/www.chess.com\/coaches","icon":{"name":"coaches","variant":"color"},"sub":[],"badge":null}],"badge":null},{"id":
```

## URL-01727

<https://www.chess.com/community>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20858](../findings/url_references-018.md#FND-20858).

### SRC-0065 at character 17965

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```

### SRC-0065 at character 53684

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```

### SRC-0065 at character 54760

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

### SRC-0777 at character 12929

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```

### SRC-0777 at character 48848

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```

### SRC-0777 at character 49924

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

### SRC-1150 at character 17965

```text
adge":null}],"badge":null},{"id":"community","type":"dropdown","label":"Community","url":"https:\/\/www.chess.com\/community","icon":{"name":"friends","variant":"color"},"sub":[{"id":"community.social","type":"sect
```

### SRC-1150 at character 53684

```text
op-wrapper sidebar-mobile-hidden"
    data-interaction="community">
    


  <a
    href="https://www.chess.com/community"
      
  
  class="cc-button-component cc-button-ghost cc-bg-ghost cc-button-medium     
```

### SRC-1150 at character 54760

```text
 sidebar-desktop-hidden"
    data-interaction="mobile-community"
    data-primary-action="https://www.chess.com/community">
    


  <button
    type="button"
      
  
  class="cc-button-component cc-button-gho
```

## URL-01728

<https://www.chess.com/computer-chess-championship>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20859](../findings/url_references-018.md#FND-20859).

### SRC-0065 at character 21871

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```

### SRC-0777 at character 16835

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```

### SRC-1150 at character 21871

```text
,{"id":"other.computer_championship","type":"link","label":"Computer Championship","url":"https:\/\/www.chess.com\/computer-chess-championship","icon":{"name":"device-chip-champion","variant":"color"},"sub":[],"badge":null},{"id":"o
```

## URL-01729

<https://www.chess.com/courses>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20860](../findings/url_references-018.md#FND-20860).

### SRC-0065 at character 15926

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```

### SRC-0777 at character 10890

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```

### SRC-1150 at character 15926

```text
g","variant":"color"},"sub":[{"id":"train.courses","type":"link","label":"Courses","url":"https:\/\/www.chess.com\/courses","icon":{"name":"book-open-aqua","variant":"color"},"sub":[],"badge":null},{"id":"train.a
```

## URL-01730

<https://www.chess.com/cs/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20861](../findings/url_references-018.md#FND-20861).

### SRC-0065 at character 6765

```text
s://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/anal
```

### SRC-1150 at character 6765

```text
s://www.chess.com/hr/analysis" hreflang="hr" />
              <link rel="alternate" href="https://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/anal
```

## URL-01731

<https://www.chess.com/da/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20862](../findings/url_references-018.md#FND-20862).

### SRC-0065 at character 6859

```text
s://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/anal
```

### SRC-1150 at character 6859

```text
s://www.chess.com/cs/analysis" hreflang="cs" />
              <link rel="alternate" href="https://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/anal
```

## URL-01732

<https://www.chess.com/daily>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20863](../findings/url_references-018.md#FND-20863).

### SRC-0065 at character 14371

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```

### SRC-0777 at character 9335

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```

### SRC-1150 at character 14371

```text
,"sub":[],"badge":null},{"id":"puzzles.daily","type":"link","label":"Daily Puzzle","url":"https:\/\/www.chess.com\/daily","icon":{"name":"calendar-dailypuzzle","variant":"color"},"sub":[],"badge":null},{"id":"p
```

## URL-01733

<https://www.chess.com/de/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20864](../findings/url_references-018.md#FND-20864).

### SRC-0065 at character 5449

```text
s://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/anal
```

### SRC-1150 at character 5449

```text
s://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/analysis" hreflang="de" />
              <link rel="alternate" href="https://www.chess.com/pl/anal
```

## URL-01734

<https://www.chess.com/el/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20865](../findings/url_references-018.md#FND-20865).

### SRC-0065 at character 5825

```text
s://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/anal
```

### SRC-1150 at character 5825

```text
s://www.chess.com/sv/analysis" hreflang="sv" />
              <link rel="alternate" href="https://www.chess.com/el/analysis" hreflang="el" />
              <link rel="alternate" href="https://www.chess.com/pt/anal
```

## URL-01735

<https://www.chess.com/endgames>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20866](../findings/url_references-018.md#FND-20866).

### SRC-0065 at character 16612

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```

### SRC-0777 at character 11576

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```

### SRC-1150 at character 16612

```text
r"},"sub":[],"badge":null},{"id":"train.endgames","type":"link","label":"Endgames","url":"https:\/\/www.chess.com\/endgames","icon":{"name":"game-endgames","variant":"color"},"sub":[],"badge":null},{"id":"train.pr
```

## URL-01736

<https://www.chess.com/es/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20867](../findings/url_references-018.md#FND-20867).

### SRC-0065 at character 5261

```text
ss.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/anal
```

### SRC-1150 at character 5261

```text
ss.com/analysis" hreflang="en" />

            
              <link rel="alternate" href="https://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/anal
```

## URL-01737

<https://www.chess.com/et/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20868](../findings/url_references-018.md#FND-20868).

### SRC-0065 at character 8269

```text
s://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/anal
```

### SRC-1150 at character 8269

```text
s://www.chess.com/bs/analysis" hreflang="bs" />
              <link rel="alternate" href="https://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/anal
```

## URL-01738

<https://www.chess.com/events>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20869](../findings/url_references-018.md#FND-20869).

### SRC-0065 at character 17271

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```

### SRC-0777 at character 12235

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```

### SRC-1150 at character 17271

```text
ars","variant":"color"},"sub":[{"id":"watch.events","type":"link","label":"Events","url":"https:\/\/www.chess.com\/events","icon":{"name":"trophies","variant":"color"},"sub":[],"badge":null},{"id":"watch.chess_t
```

## URL-01739

<https://www.chess.com/explorer>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20870](../findings/url_references-018.md#FND-20870).

### SRC-0065 at character 21329

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```

### SRC-0777 at character 16293

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```

### SRC-1150 at character 21329

```text
r"},"sub":[],"badge":null},{"id":"other.explorer","type":"link","label":"Explorer","url":"https:\/\/www.chess.com\/explorer","icon":{"name":"explorer","variant":"color"},"sub":[],"badge":null},{"id":"other.vote_ch
```

## URL-01740

<https://www.chess.com/fa/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20871](../findings/url_references-018.md#FND-20871).

### SRC-0065 at character 8363

```text
s://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/anal
```

### SRC-1150 at character 8363

```text
s://www.chess.com/et/analysis" hreflang="et" />
              <link rel="alternate" href="https://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/anal
```

## URL-01741

<https://www.chess.com/fi/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20872](../findings/url_references-018.md#FND-20872).

### SRC-0065 at character 6953

```text
s://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/anal
```

### SRC-1150 at character 6953

```text
s://www.chess.com/da/analysis" hreflang="da" />
              <link rel="alternate" href="https://www.chess.com/fi/analysis" hreflang="fi" />
              <link rel="alternate" href="https://www.chess.com/hu/anal
```

## URL-01742

<https://www.chess.com/fil/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20873](../findings/url_references-018.md#FND-20873).

### SRC-0065 at character 9791

```text
w.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/
```

### SRC-1150 at character 9791

```text
w.chess.com/zh-TW/analysis" hreflang="zh-TW" />
              <link rel="alternate" href="https://www.chess.com/fil/analysis" hreflang="fil" />
              <link rel="alternate" href="https://www.chess.com/nl-BE/
```

## URL-01743

<https://www.chess.com/forum>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20874](../findings/url_references-018.md#FND-20874).

### SRC-0065 at character 20264

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```

### SRC-0777 at character 15228

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```

### SRC-1150 at character 20264

```text
r"},"sub":[],"badge":null},{"id":"community.forums","type":"link","label":"Forums","url":"https:\/\/www.chess.com\/forum","icon":{"name":"communication-bubbles","variant":"color"},"sub":[],"badge":null}],"badge
```

## URL-01744

<https://www.chess.com/fr/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20875](../findings/url_references-018.md#FND-20875).

### SRC-0065 at character 5355

```text
s://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/anal
```

### SRC-1150 at character 5355

```text
s://www.chess.com/es/analysis" hreflang="es" />
              <link rel="alternate" href="https://www.chess.com/fr/analysis" hreflang="fr" />
              <link rel="alternate" href="https://www.chess.com/de/anal
```

## URL-01745

<https://www.chess.com/friends>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20876](../findings/url_references-018.md#FND-20876).

### SRC-0065 at character 18202

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```

### SRC-0777 at character 13166

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```

### SRC-1150 at character 18202

```text
:null,"icon":null,"sub":[{"id":"community.friends","type":"link","label":"Friends","url":"https:\/\/www.chess.com\/friends","icon":{"name":"friends","variant":"color"},"sub":[],"badge":null},{"id":"community.club
```

## URL-01746

<https://www.chess.com/game/computer/2613044014?move=0>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20877](../findings/url_references-018.md#FND-20877).

### SRC-0126 at character 269

```text
1300"]
[Termination "[PUBLIC_PLAYER_HANDLE_REDACTED] won by checkmate"]
[ECO "A00"]
[EndDate "2026.11.11"]
[Link "https://www.chess.com/game/computer/2613044014?move=0"]

1. e3 e6 2. d4 d5 3. c4 Nf6 4. Nc3 Bb4 5. Bd2 O-O 6. a3 Be7 7. Nf3 c5 8. cxd5 exd5 9. 
```

### SRC-2046 at character 269

```text
1300"]
[Termination "[PUBLIC_PLAYER_HANDLE_REDACTED] won by checkmate"]
[ECO "A00"]
[EndDate "2026.11.11"]
[Link "https://www.chess.com/game/computer/2613044014?move=0"]

1. e3 e6 2. d4 d5 3. c4 Nf6 4. Nc3 Bb4 5. Bd2 O-O 6. a3 Be7 7. Nf3 c5 8. cxd5 exd5 9. 
```

## URL-01747

<https://www.chess.com/game/live/187158515860>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20878](../findings/url_references-018.md#FND-20878).

### SRC-0777 at character 4094

```text
ntent="Chess: [PUBLIC_PLAYER_HANDLE_REDACTED] vs [PUBLIC_PLAYER_HANDLE_REDACTED]" />

          <meta property="og:url" content="https://www.chess.com/game/live/187158515860" />

          <meta property="fb:app_id" content="2427617054" />

          <meta proper
```

### SRC-0777 at character 5323

```text
/game/live/default/187158515860" />

  
  
          
        <link rel="canonical" href="https://www.chess.com/game/live/187158515860">
  
    
              
    
    <link rel="manifest" href="/manifest.json" crossorigin=
```

### SRC-2049 at character 3245

```text
omatically be treated as contradictory.

Visible follow-up investigation:
- User supplied https://www.chess.com/game/live/187158515860 as an example of a page loading explanation-engine.js/.wasm. A fetch_page result displaye
```

## URL-01748

<https://www.chess.com/games>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20879](../findings/url_references-018.md#FND-20879).

### SRC-0065 at character 20811

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```

### SRC-0777 at character 15775

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```

### SRC-1150 at character 20811

```text
,"badge":null},{"id":"other.games_database","type":"link","label":"Games Database","url":"https:\/\/www.chess.com\/games","icon":{"name":"board-4x4-brown","variant":"color"},"sub":[],"badge":null},{"id":"other.
```

## URL-01749

<https://www.chess.com/games/archive>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20880](../findings/url_references-018.md#FND-20880).

### SRC-0065 at character 13838

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```

### SRC-0777 at character 8802

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```

### SRC-1150 at character 13838

```text
b":[],"badge":null},{"id":"play.game_history","type":"link","label":"Game History","url":"https:\/\/www.chess.com\/games\/archive","icon":{"name":"board-archive","variant":"color"},"sub":[],"badge":null}],"badge":null}]
```

## URL-01750

<https://www.chess.com/gl/analysis>

- Type: page_or_route_candidate; form: absolute.
- Visited: not established from literal alone.
- Verified: observed literal only; not re-fetched during this audit.
- Date: source-embedded date if present; filesystem time is not a verification date.
- Related findings: [FND-20881](../findings/url_references-018.md#FND-20881).

### SRC-0065 at character 8457

```text
s://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/anal
```

### SRC-1150 at character 8457

```text
s://www.chess.com/fa/analysis" hreflang="fa" />
              <link rel="alternate" href="https://www.chess.com/gl/analysis" hreflang="gl" />
              <link rel="alternate" href="https://www.chess.com/he/anal
```
