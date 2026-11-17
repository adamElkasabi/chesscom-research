# 07 — Focused architecture diagrams

[Start](00_START_HERE.md)

## Bot move generation — recovered static ordering

```mermaid
flowchart TD
    M[Bot metadata: style / skills / book / config key] --> G{New-bot gate AND config available?}
    G -->|yes| C[Feature61 BotMoveFromConfig]
    C --> CM[Configured move or empty/error: no fallthrough in Z5]
    G -->|no| B{Valid browser book move?}
    B -->|yes| BM[Use book move]
    B -->|no| K[Feature9 GetBotMove: KOMODO]
    M --> P[Npt explicit personality enum translation]
    M --> S[Mpt skill-derived rating + adaptive flag]
    P --> K
    S --> K
    M --> SP[Separate speech assets / LoadBot / GetBotChat]
```

## Configured path setup — static plus selected native confirmation

```mermaid
flowchart LR
    U[Literal Topaz model URL] --> F[Public model bytes]
    F --> L[CEE_LoadCharmModel: m-topaz-jackdaw]
    K[Bot config key] --> Q[Configurator v3/v4 wrapper]
    Q --> J[storedJson to BotMoveConfiguration]
    J --> R[Feature70 resource discovery]
    L --> R
    R --> B[Fetch returned book then AddArtifact]
    J --> D[Feature61 configured move decision]
    L --> D
    B --> D
```

Feature70's NN requirement was present without the model and absent after it loaded in the native diagnostic. Frontend setup consumes book resources at this callsite; production config values were not retrieved.

## Human review: two related but non-identical execution paths

```mermaid
flowchart TD
    W[Website full analysis option + Human feature flag] --> E[A4e engine selection: TORCH_HUMAN or SF16_1]
    E --> Q[W4e CEAC review request]
    Q --> S[Remote /v2/game-review WebSocket]
    S --> X[Private server implementation/settings unknown]
    L[Local CEE game points] --> H[Feature79 Human evaluation preload]
    H --> A[Feature1 AddEvaluations]
    A --> R[Feature42 local GameReview]
    R --> N[Completed historical review; not website parity]
```

Diagrams explain evidenced interfaces, not undisclosed server topology. There is deliberately no arrow equating BotPersonality.HUMAN, TorchSearchMode.human, Maia and the recovered Charm-small model.
