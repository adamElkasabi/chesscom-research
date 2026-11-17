# data_models — findings 901–1000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01175"></a>
## FND-01175: message declaration: chesscom.chess.v1.Stalemate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Stalemate {

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 264.

```text
 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01170, FND-01171

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01176"></a>
## FND-01176: enum declaration: chesscom.chess.v1.Square

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Square {

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 89.

```text
// source: chesscom/chess/v1/square.proto
// syntax: proto3

package chesscom.chess.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
 
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01177"></a>
## FND-01177: chesscom.chess.v1.Square.SQUARE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_UNSPECIFIED = 0;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 105.

```text
urce: chesscom/chess/v1/square.proto
// syntax: proto3

package chesscom.chess.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01178"></a>
## FND-01178: chesscom.chess.v1.Square.SQUARE_A1 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A1 = 1;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 131.

```text
uare.proto
// syntax: proto3

package chesscom.chess.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUAR
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01179"></a>
## FND-01179: chesscom.chess.v1.Square.SQUARE_B1 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B1 = 2;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 148.

```text
tax: proto3

package chesscom.chess.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUA
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01180"></a>
## FND-01180: chesscom.chess.v1.Square.SQUARE_C1 = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C1 = 3;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 165.

```text
age chesscom.chess.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQU
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01181"></a>
## FND-01181: chesscom.chess.v1.Square.SQUARE_D1 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D1 = 4;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 182.

```text
s.v1;

enum Square {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQ
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01182"></a>
## FND-01182: chesscom.chess.v1.Square.SQUARE_E1 = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E1 = 5;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 199.

```text
e {
  SQUARE_UNSPECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  S
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01183"></a>
## FND-01183: chesscom.chess.v1.Square.SQUARE_F1 = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F1 = 6;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 216.

```text
ECIFIED = 0;
  SQUARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01184"></a>
## FND-01184: chesscom.chess.v1.Square.SQUARE_G1 = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G1 = 7;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 233.

```text
UARE_A1 = 1;
  SQUARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
 
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01185"></a>
## FND-01185: chesscom.chess.v1.Square.SQUARE_H1 = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H1 = 8;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 250.

```text
UARE_B1 = 2;
  SQUARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01186"></a>
## FND-01186: chesscom.chess.v1.Square.SQUARE_A2 = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A2 = 9;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 267.

```text
UARE_C1 = 3;
  SQUARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01187"></a>
## FND-01187: chesscom.chess.v1.Square.SQUARE_B2 = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B2 = 10;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 284.

```text
UARE_D1 = 4;
  SQUARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01188"></a>
## FND-01188: chesscom.chess.v1.Square.SQUARE_C2 = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C2 = 11;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 302.

```text
ARE_E1 = 5;
  SQUARE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01189"></a>
## FND-01189: chesscom.chess.v1.Square.SQUARE_D2 = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D2 = 12;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 320.

```text
RE_F1 = 6;
  SQUARE_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01190"></a>
## FND-01190: chesscom.chess.v1.Square.SQUARE_E2 = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E2 = 13;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 338.

```text
E_G1 = 7;
  SQUARE_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01191"></a>
## FND-01191: chesscom.chess.v1.Square.SQUARE_F2 = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F2 = 14;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 356.

```text
_H1 = 8;
  SQUARE_A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01192"></a>
## FND-01192: chesscom.chess.v1.Square.SQUARE_G2 = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G2 = 15;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 374.

```text
A2 = 9;
  SQUARE_B2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01193"></a>
## FND-01193: chesscom.chess.v1.Square.SQUARE_H2 = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H2 = 16;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 392.

```text
2 = 10;
  SQUARE_C2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01194"></a>
## FND-01194: chesscom.chess.v1.Square.SQUARE_A3 = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A3 = 17;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 410.

```text
2 = 11;
  SQUARE_D2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01195"></a>
## FND-01195: chesscom.chess.v1.Square.SQUARE_B3 = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B3 = 18;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 428.

```text
2 = 12;
  SQUARE_E2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01196"></a>
## FND-01196: chesscom.chess.v1.Square.SQUARE_C3 = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C3 = 19;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 446.

```text
2 = 13;
  SQUARE_F2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01197"></a>
## FND-01197: chesscom.chess.v1.Square.SQUARE_D3 = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D3 = 20;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 464.

```text
2 = 14;
  SQUARE_G2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01198"></a>
## FND-01198: chesscom.chess.v1.Square.SQUARE_E3 = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E3 = 21;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 482.

```text
2 = 15;
  SQUARE_H2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01199"></a>
## FND-01199: chesscom.chess.v1.Square.SQUARE_F3 = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F3 = 22;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 500.

```text
2 = 16;
  SQUARE_A3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01200"></a>
## FND-01200: chesscom.chess.v1.Square.SQUARE_G3 = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G3 = 23;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 518.

```text
3 = 17;
  SQUARE_B3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01201"></a>
## FND-01201: chesscom.chess.v1.Square.SQUARE_H3 = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H3 = 24;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 536.

```text
3 = 18;
  SQUARE_C3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01202"></a>
## FND-01202: chesscom.chess.v1.Square.SQUARE_A4 = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A4 = 25;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 554.

```text
3 = 19;
  SQUARE_D3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01203"></a>
## FND-01203: chesscom.chess.v1.Square.SQUARE_B4 = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B4 = 26;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 572.

```text
3 = 20;
  SQUARE_E3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01204"></a>
## FND-01204: chesscom.chess.v1.Square.SQUARE_C4 = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C4 = 27;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 590.

```text
3 = 21;
  SQUARE_F3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01205"></a>
## FND-01205: chesscom.chess.v1.Square.SQUARE_D4 = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D4 = 28;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 608.

```text
3 = 22;
  SQUARE_G3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01206"></a>
## FND-01206: chesscom.chess.v1.Square.SQUARE_E4 = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E4 = 29;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 626.

```text
3 = 23;
  SQUARE_H3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01207"></a>
## FND-01207: chesscom.chess.v1.Square.SQUARE_F4 = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F4 = 30;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 644.

```text
3 = 24;
  SQUARE_A4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01208"></a>
## FND-01208: chesscom.chess.v1.Square.SQUARE_G4 = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G4 = 31;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 662.

```text
4 = 25;
  SQUARE_B4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01209"></a>
## FND-01209: chesscom.chess.v1.Square.SQUARE_H4 = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H4 = 32;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 680.

```text
4 = 26;
  SQUARE_C4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01210"></a>
## FND-01210: chesscom.chess.v1.Square.SQUARE_A5 = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A5 = 33;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 698.

```text
4 = 27;
  SQUARE_D4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01211"></a>
## FND-01211: chesscom.chess.v1.Square.SQUARE_B5 = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B5 = 34;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 716.

```text
4 = 28;
  SQUARE_E4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01212"></a>
## FND-01212: chesscom.chess.v1.Square.SQUARE_C5 = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C5 = 35;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 734.

```text
4 = 29;
  SQUARE_F4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01213"></a>
## FND-01213: chesscom.chess.v1.Square.SQUARE_D5 = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D5 = 36;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 752.

```text
4 = 30;
  SQUARE_G4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01214"></a>
## FND-01214: chesscom.chess.v1.Square.SQUARE_E5 = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E5 = 37;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 770.

```text
4 = 31;
  SQUARE_H4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01215"></a>
## FND-01215: chesscom.chess.v1.Square.SQUARE_F5 = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F5 = 38;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 788.

```text
4 = 32;
  SQUARE_A5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01216"></a>
## FND-01216: chesscom.chess.v1.Square.SQUARE_G5 = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G5 = 39;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 806.

```text
5 = 33;
  SQUARE_B5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01217"></a>
## FND-01217: chesscom.chess.v1.Square.SQUARE_H5 = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H5 = 40;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 824.

```text
5 = 34;
  SQUARE_C5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01218"></a>
## FND-01218: chesscom.chess.v1.Square.SQUARE_A6 = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A6 = 41;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 842.

```text
5 = 35;
  SQUARE_D5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01219"></a>
## FND-01219: chesscom.chess.v1.Square.SQUARE_B6 = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B6 = 42;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 860.

```text
5 = 36;
  SQUARE_E5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01220"></a>
## FND-01220: chesscom.chess.v1.Square.SQUARE_C6 = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C6 = 43;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 878.

```text
5 = 37;
  SQUARE_F5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01221"></a>
## FND-01221: chesscom.chess.v1.Square.SQUARE_D6 = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D6 = 44;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 896.

```text
5 = 38;
  SQUARE_G5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01222"></a>
## FND-01222: chesscom.chess.v1.Square.SQUARE_E6 = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E6 = 45;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 914.

```text
5 = 39;
  SQUARE_H5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01223"></a>
## FND-01223: chesscom.chess.v1.Square.SQUARE_F6 = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F6 = 46;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 932.

```text
5 = 40;
  SQUARE_A6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01224"></a>
## FND-01224: chesscom.chess.v1.Square.SQUARE_G6 = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G6 = 47;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 950.

```text
6 = 41;
  SQUARE_B6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64
```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01225"></a>
## FND-01225: chesscom.chess.v1.Square.SQUARE_H6 = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H6 = 48;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 968.

```text
6 = 42;
  SQUARE_C6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01226"></a>
## FND-01226: chesscom.chess.v1.Square.SQUARE_A7 = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A7 = 49;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 986.

```text
6 = 43;
  SQUARE_D6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01227"></a>
## FND-01227: chesscom.chess.v1.Square.SQUARE_B7 = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B7 = 50;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1004.

```text
6 = 44;
  SQUARE_E6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01228"></a>
## FND-01228: chesscom.chess.v1.Square.SQUARE_C7 = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C7 = 51;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1022.

```text
6 = 45;
  SQUARE_F6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01229"></a>
## FND-01229: chesscom.chess.v1.Square.SQUARE_D7 = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D7 = 52;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1040.

```text
6 = 46;
  SQUARE_G6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01230"></a>
## FND-01230: chesscom.chess.v1.Square.SQUARE_E7 = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E7 = 53;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1058.

```text
6 = 47;
  SQUARE_H6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01231"></a>
## FND-01231: chesscom.chess.v1.Square.SQUARE_F7 = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F7 = 54;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1076.

```text
6 = 48;
  SQUARE_A7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01232"></a>
## FND-01232: chesscom.chess.v1.Square.SQUARE_G7 = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G7 = 55;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1094.

```text
7 = 49;
  SQUARE_B7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01233"></a>
## FND-01233: chesscom.chess.v1.Square.SQUARE_H7 = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H7 = 56;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1112.

```text
7 = 50;
  SQUARE_C7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01234"></a>
## FND-01234: chesscom.chess.v1.Square.SQUARE_A8 = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_A8 = 57;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1130.

```text
7 = 51;
  SQUARE_D7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01235"></a>
## FND-01235: chesscom.chess.v1.Square.SQUARE_B8 = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_B8 = 58;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1148.

```text
7 = 52;
  SQUARE_E7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01236"></a>
## FND-01236: chesscom.chess.v1.Square.SQUARE_C8 = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_C8 = 59;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1166.

```text
7 = 53;
  SQUARE_F7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01237"></a>
## FND-01237: chesscom.chess.v1.Square.SQUARE_D8 = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_D8 = 60;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1184.

```text
7 = 54;
  SQUARE_G7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01238"></a>
## FND-01238: chesscom.chess.v1.Square.SQUARE_E8 = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_E8 = 61;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1202.

```text
7 = 55;
  SQUARE_H7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01239"></a>
## FND-01239: chesscom.chess.v1.Square.SQUARE_F8 = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_F8 = 62;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1220.

```text
7 = 56;
  SQUARE_A8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01240"></a>
## FND-01240: chesscom.chess.v1.Square.SQUARE_G8 = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_G8 = 63;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1238.

```text
8 = 57;
  SQUARE_B8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01241"></a>
## FND-01241: chesscom.chess.v1.Square.SQUARE_H8 = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SQUARE_H8 = 64;

### Evidence

- **SRC-0254** `research/proto/chesscom/chess/v1/square.proto` — [preserved redacted evidence](../evidence/text/657b93bae139105ad6178aedf4790841a7499732f4977ebb01b6fda522b6e7a3.proto)
  Character offset 1256.

```text
8 = 58;
  SQUARE_C8 = 59;
  SQUARE_D8 = 60;
  SQUARE_E8 = 61;
  SQUARE_F8 = 62;
  SQUARE_G8 = 63;
  SQUARE_H8 = 64;
}

```

**Source references:** SRC-0254, SRC-1225  
**URL references:** None independently associated  
**Related findings:** FND-01176, FND-01177, FND-01178

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01242"></a>
## FND-01242: enum declaration: chesscom.chess.v1.TimeClass

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TimeClass {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 87.

```text
// source: chesscom/chess/v1/time.proto
// syntax: proto3

package chesscom.chess.v1;

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTi
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01243"></a>
## FND-01243: chesscom.chess.v1.TimeClass.TIME_CLASS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_UNSPECIFIED = 0;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 106.

```text
rce: chesscom/chess/v1/time.proto
// syntax: proto3

package chesscom.chess.v1;

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01244"></a>
## FND-01244: chesscom.chess.v1.TimeClass.TIME_CLASS_HYPERBULLET = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_HYPERBULLET = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 136.

```text
oto
// syntax: proto3

package chesscom.chess.v1;

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiSt
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01245"></a>
## FND-01245: chesscom.chess.v1.TimeClass.TIME_CLASS_BULLET = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_BULLET = 2;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 166.

```text
 chesscom.chess.v1;

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01246"></a>
## FND-01246: chesscom.chess.v1.TimeClass.TIME_CLASS_BLITZ = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_BLITZ = 3;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 191.

```text
 TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.Ar
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01247"></a>
## FND-01247: chesscom.chess.v1.TimeClass.TIME_CLASS_RAPID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_RAPID = 4;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 215.

```text
S_UNSPECIFIED = 0;
  TIME_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl arma
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01248"></a>
## FND-01248: chesscom.chess.v1.TimeClass.TIME_CLASS_CLASSICAL = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_CLASSICAL = 5;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 239.

```text
E_CLASS_HYPERBULLET = 1;
  TIME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

messa
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01249"></a>
## FND-01249: chesscom.chess.v1.TimeClass.TIME_CLASS_DAILY = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_DAILY = 6;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 267.

```text
IME_CLASS_BULLET = 2;
  TIME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optio
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01250"></a>
## FND-01250: message declaration: chesscom.chess.v1.TimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TimeControl {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 292.

```text
IME_CLASS_BLITZ = 3;
  TIME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01251"></a>
## FND-01251: oneof declaration: chesscom.chess.v1.TimeControl.control

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof control {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 316.

```text
IME_CLASS_RAPID = 4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01252"></a>
## FND-01252: chesscom.chess.v1.TimeControl.base = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.BaseTimeControl base = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 334.

```text
4;
  TIME_CLASS_CLASSICAL = 5;
  TIME_CLASS_DAILY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

messag
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01253"></a>
## FND-01253: chesscom.chess.v1.TimeControl.daily = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.DailyTimeControl daily = 2;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 381.

```text
LY = 6;
}

message TimeControl {
  oneof control {
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01254"></a>
## FND-01254: chesscom.chess.v1.TimeControl.multi_stage = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 430.

```text
{
  .chesscom.chess.v1.BaseTimeControl base = 1;
  .chesscom.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  re
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01255"></a>
## FND-01255: chesscom.chess.v1.TimeControl.armageddon = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 490.

```text
.chess.v1.DailyTimeControl daily = 2;
  .chesscom.chess.v1.MultiStageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

me
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01256"></a>
## FND-01256: message declaration: chesscom.chess.v1.BaseTimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BaseTimeControl {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 554.

```text
StageTimeControl multi_stage = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limi
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01257"></a>
## FND-01257: chesscom.chess.v1.BaseTimeControl.base_ms = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 base_ms = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 582.

```text
 = 3;
  .chesscom.chess.v1.ArmageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chess
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01258"></a>
## FND-01258: chesscom.chess.v1.BaseTimeControl.increment_ms = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 increment_ms = 2;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 612.

```text
ageddonTimeControl armageddon = 4;
  }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl t
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01259"></a>
## FND-01259: message declaration: chesscom.chess.v1.DailyTimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DailyTimeControl {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 648.

```text
 }
}

message BaseTimeControl {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message Armagedd
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01260"></a>
## FND-01260: chesscom.chess.v1.DailyTimeControl.days_per_turn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 days_per_turn = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 677.

```text
 {
  optional int64 base_ms = 1;
  optional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional in
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01261"></a>
## FND-01261: message declaration: chesscom.chess.v1.MultiStageTimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MultiStageTimeControl {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 714.

```text
tional int64 increment_ms = 2;
}

message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01262"></a>
## FND-01262: chesscom.chess.v1.MultiStageTimeControl.stages = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.TimeControlStage stages = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 748.

```text
message DailyTimeControl {
  optional int32 days_per_turn = 1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional i
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01263"></a>
## FND-01263: message declaration: chesscom.chess.v1.TimeControlStage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TimeControlStage {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 808.

```text
1;
}

message MultiStageTimeControl {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move
```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01264"></a>
## FND-01264: oneof declaration: chesscom.chess.v1.TimeControlStage._move_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_limit {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 837.

```text
ontrol {
  repeated .chesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01265"></a>
## FND-01265: chesscom.chess.v1.TimeControlStage.move_limit = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 move_limit = 2;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 859.

```text
hesscom.chess.v1.TimeControlStage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01266"></a>
## FND-01266: chesscom.chess.v1.TimeControlStage.time_control = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.BaseTimeControl time_control = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 887.

```text
Stage stages = 1;
}

message TimeControlStage {
  oneof _move_limit {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01267"></a>
## FND-01267: message declaration: chesscom.chess.v1.ArmageddonTimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ArmageddonTimeControl {

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 952.

```text
it {
  int32 move_limit = 2;
  }
  optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01268"></a>
## FND-01268: chesscom.chess.v1.ArmageddonTimeControl.white_base_ms = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 white_base_ms = 1;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 986.

```text
 optional .chesscom.chess.v1.BaseTimeControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01269"></a>
## FND-01269: chesscom.chess.v1.ArmageddonTimeControl.black_base_ms = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 black_base_ms = 2;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 1022.

```text
eControl time_control = 1;
}

message ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01270"></a>
## FND-01270: chesscom.chess.v1.ArmageddonTimeControl.increment_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 increment_ms = 3;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 1058.

```text
e ArmageddonTimeControl {
  optional int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01271"></a>
## FND-01271: chesscom.chess.v1.ArmageddonTimeControl.increment_after_move = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 increment_after_move = 4;

### Evidence

- **SRC-0255** `research/proto/chesscom/chess/v1/time.proto` — [preserved redacted evidence](../evidence/text/c5de7b9de5c6dc44165b86e6c7034fa3392682a887e4017dc4fcbae6473128d9.proto)
  Character offset 1093.

```text
l int32 white_base_ms = 1;
  optional int32 black_base_ms = 2;
  optional int32 increment_ms = 3;
  optional int32 increment_after_move = 4;
}

```

**Source references:** SRC-0255, SRC-1226  
**URL references:** None independently associated  
**Related findings:** FND-01242, FND-01243, FND-01244

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01272"></a>
## FND-01272: enum declaration: chesscom.chess.v1.Variant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Variant {

### Evidence

- **SRC-0256** `research/proto/chesscom/chess/v1/variant.proto` — [preserved redacted evidence](../evidence/text/0ab29acfd5916eb5814776fd89a9fa983aa9bda84fdbd32c59c5bebe0b18718f.proto)
  Character offset 90.

```text
// source: chesscom/chess/v1/variant.proto
// syntax: proto3

package chesscom.chess.v1;

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

```

**Source references:** SRC-0256, SRC-1227  
**URL references:** None independently associated  
**Related findings:** FND-01273, FND-01274

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01273"></a>
## FND-01273: chesscom.chess.v1.Variant.VARIANT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_UNSPECIFIED = 0;

### Evidence

- **SRC-0256** `research/proto/chesscom/chess/v1/variant.proto` — [preserved redacted evidence](../evidence/text/0ab29acfd5916eb5814776fd89a9fa983aa9bda84fdbd32c59c5bebe0b18718f.proto)
  Character offset 107.

```text
ce: chesscom/chess/v1/variant.proto
// syntax: proto3

package chesscom.chess.v1;

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

```

**Source references:** SRC-0256, SRC-1227  
**URL references:** None independently associated  
**Related findings:** FND-01272, FND-01274

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01274"></a>
## FND-01274: chesscom.chess.v1.Variant.VARIANT_CHESS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_CHESS = 1;

### Evidence

- **SRC-0256** `research/proto/chesscom/chess/v1/variant.proto` — [preserved redacted evidence](../evidence/text/0ab29acfd5916eb5814776fd89a9fa983aa9bda84fdbd32c59c5bebe0b18718f.proto)
  Character offset 134.

```text
nt.proto
// syntax: proto3

package chesscom.chess.v1;

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

```

**Source references:** SRC-0256, SRC-1227  
**URL references:** None independently associated  
**Related findings:** FND-01272, FND-01273

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
