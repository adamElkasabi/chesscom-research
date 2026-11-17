# experiments — findings 1–95

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18532"></a>
## FND-18532: Trial example-game-baseline — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "example-game-baseline",
    "fixture": "example-game",
    "settings": {
      "userColor": 1
    },
    "uciAfter": {
      "Normalize": true
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:21:10.051Z",
  "actual": {
    "accuracy": {
      "white": 87.72982025146484,
      "black": 79.54060363769531
    },
    "ratings": {
      "white": 1850,
      "black": 1700
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 4,
        "4": 27,
        "5": 19,
        "6": 4,
        "7": 1,
        "8": 0,
        "9": 1,
        "10": 1,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 16,
        "5": 26,
        "6": 5,
        "7": 4,
        "8": 4,
        "9": 0,
        "10": 1,
        "11": 1,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "f303b61796d06cb4d8c032bc61dc0def4aef8332b499ad3705dccff136a227e9",
  "actualSettings": {
    "userColor": 1,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 82.554,
  "speech": {
    "sentences": 124,
    "hashes": 124
  },
  "warnings": [],
  "source_id": "SRC-0734",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0734** `research/refinement/holdout/example-game-baseline.json` — [preserved redacted evidence](../evidence/text/ac0b65a37bd95b5db989e78110dde725725a0ea35423741ebd362e77aa1b395f.json)

**Source references:** SRC-0734, SRC-2041  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18533"></a>
## FND-18533: Trial example-game-normalize-off — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "example-game-normalize-off",
    "fixture": "example-game",
    "settings": {
      "userColor": 1
    },
    "uciAfter": {
      "Normalize": false
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:22:32.798Z",
  "actual": {
    "accuracy": {
      "white": 88.43988037109375,
      "black": 80.23229217529297
    },
    "ratings": {
      "white": 1850,
      "black": 1450
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 4,
        "4": 27,
        "5": 19,
        "6": 4,
        "7": 1,
        "8": 0,
        "9": 1,
        "10": 1,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 16,
        "5": 23,
        "6": 7,
        "7": 2,
        "8": 7,
        "9": 0,
        "10": 1,
        "11": 1,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "a877ccf3d74e3c3674400b77d15b7d98934e6fd828c9bd1abc04ef1813e1575a",
  "actualSettings": {
    "userColor": 1,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 77.184,
  "speech": {
    "sentences": 125,
    "hashes": 125
  },
  "warnings": [],
  "source_id": "SRC-0736",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0736** `research/refinement/holdout/example-game-normalize-off.json` — [preserved redacted evidence](../evidence/text/b9f7fc394433a0d850eae96e5ca8c2deb45a81a679ce10a91e05d823a42392eb.json)

**Source references:** SRC-0736, SRC-2043  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18534"></a>
## FND-18534: Trial example-game-refined-hash64 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "example-game-refined-hash64",
    "fixture": "example-game",
    "settings": {
      "userColor": 1
    },
    "uciAfter": {
      "Normalize": false,
      "Hash": 64
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:23:50.138Z",
  "actual": {
    "accuracy": {
      "white": 90.14149475097656,
      "black": 82.31620788574219
    },
    "ratings": {
      "white": 1900,
      "black": 1450
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 4,
        "4": 26,
        "5": 22,
        "6": 2,
        "7": 1,
        "8": 0,
        "9": 1,
        "10": 1,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 18,
        "5": 21,
        "6": 6,
        "7": 4,
        "8": 6,
        "9": 0,
        "10": 1,
        "11": 1,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "86243ff1809ef3e587f33436b803f9fa3fae61cda0209834e591f80a1b6d60e1",
  "actualSettings": {
    "userColor": 1,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 78.637,
  "speech": {
    "sentences": 126,
    "hashes": 126
  },
  "warnings": [],
  "source_id": "SRC-0738",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0738** `research/refinement/holdout/example-game-refined-hash64.json` — [preserved redacted evidence](../evidence/text/c572b8b96991dbca2acb40d599eb1aebf122bfca791083e055d1601b3db33b7d.json)

**Source references:** SRC-0738, SRC-2035  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18535"></a>
## FND-18535: Trial human-game-baseline — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "human-game-baseline",
    "fixture": "human-game",
    "settings": {
      "userColor": 2
    },
    "uciAfter": {
      "Normalize": true
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:18:05.837Z",
  "actual": {
    "accuracy": {
      "white": 74.10804748535156,
      "black": 62.9063606262207
    },
    "ratings": {
      "white": 1250,
      "black": 600
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 1,
        "4": 12,
        "5": 10,
        "6": 7,
        "7": 3,
        "8": 4,
        "9": 0,
        "10": 2,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 12,
        "5": 8,
        "6": 3,
        "7": 7,
        "8": 4,
        "9": 0,
        "10": 3,
        "11": 2,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "f11625d5ffb12e876251af16c6e059e237c986e90a1423f5f13372facd3d208e",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 60.079,
  "speech": {
    "sentences": 89,
    "hashes": 89
  },
  "warnings": [],
  "source_id": "SRC-0740",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0740** `research/refinement/holdout/human-game-baseline.json` — [preserved redacted evidence](../evidence/text/181753795a012578d7094f9ff47f530080bc113af786c83847029fc57bfe556d.json)

**Source references:** SRC-0740, SRC-2039  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18536"></a>
## FND-18536: Trial human-game-normalize-off — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "human-game-normalize-off",
    "fixture": "human-game",
    "settings": {
      "userColor": 2
    },
    "uciAfter": {
      "Normalize": false
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:19:06.103Z",
  "actual": {
    "accuracy": {
      "white": 69.12924194335938,
      "black": 62.28227615356445
    },
    "ratings": {
      "white": 1000,
      "black": 350
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 1,
        "4": 12,
        "5": 10,
        "6": 5,
        "7": 5,
        "8": 2,
        "9": 2,
        "10": 2,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 12,
        "5": 7,
        "6": 7,
        "7": 3,
        "8": 4,
        "9": 0,
        "10": 4,
        "11": 2,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "8dd30ec0a920ac627d40d062ffba0c1a582a0621169f12804ffd66f46332de80",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 62.758,
  "speech": {
    "sentences": 89,
    "hashes": 89
  },
  "warnings": [],
  "source_id": "SRC-0742",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0742** `research/refinement/holdout/human-game-normalize-off.json` — [preserved redacted evidence](../evidence/text/7125f2a4f8ba105c717f8542dde06917163f680dd6aa8e8a91a703f7b9e68544.json)

**Source references:** SRC-0742, SRC-2036  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18537"></a>
## FND-18537: Trial human-game-refined-hash64 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "human-game-refined-hash64",
    "fixture": "human-game",
    "settings": {
      "userColor": 2
    },
    "uciAfter": {
      "Normalize": false,
      "Hash": 64
    },
    "timeoutSeconds": 200
  },
  "started": "2026-11-14T19:20:09.014Z",
  "actual": {
    "accuracy": {
      "white": 66.73457336425781,
      "black": 60.90155792236328
    },
    "ratings": {
      "white": 850,
      "black": 300
    },
    "tallies": {
      "white": {
        "1": 4,
        "2": 0,
        "3": 2,
        "4": 11,
        "5": 9,
        "6": 6,
        "7": 4,
        "8": 4,
        "9": 2,
        "10": 1,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 3,
        "2": 0,
        "3": 0,
        "4": 8,
        "5": 11,
        "6": 5,
        "7": 4,
        "8": 5,
        "9": 0,
        "10": 4,
        "11": 2,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "5439b1cc6f3fba048014c634f8af95d23aeb9efe6502cdff800b62e30ba5a5fc",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 60.889,
  "speech": {
    "sentences": 90,
    "hashes": 90
  },
  "warnings": [],
  "source_id": "SRC-0744",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0744** `research/refinement/holdout/human-game-refined-hash64.json` — [preserved redacted evidence](../evidence/text/e8be0938a34ecd327c0603b8e0279688f806d1087927dbeb9daf6edf15547e56.json)

**Source references:** SRC-0744, SRC-2037  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18538"></a>
## FND-18538: Trial baseline — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "baseline",
    "saveReview": true
  },
  "error": "exit null ",
  "source_id": "SRC-0790",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0790** `research/refinement/resource-failed-attempts/baseline.json` — [preserved redacted evidence](../evidence/text/8a09b5139b3885c5670c9210088a717bb73d9ab32d72de744852433beb713777.json)

**Source references:** SRC-0790  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18539"></a>
## FND-18539: Trial strength-1-class-1 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-1-class-1",
    "strength": 1,
    "settings": {
      "moveClassificationVersion": 1
    }
  },
  "error": "exit null ",
  "source_id": "SRC-0791",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0791** `research/refinement/resource-failed-attempts/strength-1-class-1.json` — [preserved redacted evidence](../evidence/text/8cf855ada961379b36fa3a8bac53b2660dd5ebf19fc3cdd8cf30086044102cce.json)

**Source references:** SRC-0791  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18540"></a>
## FND-18540: Trial strength-1-class-2 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-1-class-2",
    "strength": 1,
    "settings": {
      "moveClassificationVersion": 2
    }
  },
  "error": "exit null ",
  "source_id": "SRC-0792",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0792** `research/refinement/resource-failed-attempts/strength-1-class-2.json` — [preserved redacted evidence](../evidence/text/6876204532f562e4cf411f8ae86cb488d6d0f82699a2d254dd1a94d37f9a9709.json)

**Source references:** SRC-0792  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18541"></a>
## FND-18541: Trial strength-2-class-0 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-0",
    "strength": 2,
    "settings": {}
  },
  "error": "exit null ",
  "source_id": "SRC-0793",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0793** `research/refinement/resource-failed-attempts/strength-2-class-0.json` — [preserved redacted evidence](../evidence/text/1d99186f3edd4b5f624beac7684695d1788db7fb5d29420aff284d9eedb0522b.json)

**Source references:** SRC-0793  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18542"></a>
## FND-18542: Trial strength-2-class-1 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-1",
    "strength": 2,
    "settings": {
      "moveClassificationVersion": 1
    }
  },
  "error": "exit null ",
  "source_id": "SRC-0794",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0794** `research/refinement/resource-failed-attempts/strength-2-class-1.json` — [preserved redacted evidence](../evidence/text/122c3ed97e20f7d834201ad62be3cde4f2fda24db8803482733e860ae67c4d33.json)

**Source references:** SRC-0794  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18543"></a>
## FND-18543: Trial strength-2-class-2 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-2",
    "strength": 2,
    "settings": {
      "moveClassificationVersion": 2
    }
  },
  "error": "exit null ",
  "source_id": "SRC-0795",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0795** `research/refinement/resource-failed-attempts/strength-2-class-2.json` — [preserved redacted evidence](../evidence/text/37626e2c147cd26b30fd607f8df2a286d85eba631395ace0df2bfec69f4d6ca9.json)

**Source references:** SRC-0795  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18544"></a>
## FND-18544: Trial strength-3-class-1 — invalid resource-pressure attempt; not a numerical result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-3-class-1",
    "strength": 3,
    "settings": {
      "moveClassificationVersion": 1
    }
  },
  "error": "exit null ",
  "source_id": "SRC-0796",
  "outcome": "invalid resource-pressure attempt; not a numerical result"
}

### Evidence

- **SRC-0796** `research/refinement/resource-failed-attempts/strength-3-class-1.json` — [preserved redacted evidence](../evidence/text/e2f2c25b92bf1c3fbf626258c1b52470d6b8fefd2160bcbabda1c93f93d83c74.json)

**Source references:** SRC-0796  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18545"></a>
## FND-18545: Trial baseline — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "baseline",
    "saveReview": true
  },
  "started": "2026-11-14T18:47:29.319Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.404,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0797",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797, SRC-2011  
**URL references:** None independently associated  
**Related findings:** FND-18546, FND-18547

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18567"></a>
## FND-18567: Trial comparison-control — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "comparison-control",
    "reviewEvaluations": true,
    "preSearch": {
      "gameReviewSearchSettings": {
        "strength": 1
      }
    },
    "addPreSearch": true,
    "saveReview": true,
    "timeoutSeconds": 90
  },
  "started": "2026-11-14T20:25:35.752Z",
  "actual": {
    "accuracy": {
      "white": 60.15205383300781,
      "black": 96.07951354980469
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 2,
        "8": 3,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "c2b28b8addf021e0b46fa0bd913876bd0e46df2b49ee95dd8dcb9e119ed53e6f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.524,
  "speech": {
    "sentences": 21,
    "hashes": 21
  },
  "warnings": [],
  "source_id": "SRC-0798",
  "outcome": "complete numeric result",
  "completed_presearch_points": 21,
  "presearch_progress_values": [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "searchAudit": {
    "beforeReview": [
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 c2c3 c2c4 d2d3 d2d4 e2e3 e2e4 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 c2c3 c2c4 d2d3 e2e3 e2e4 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 c7c5 c7c6 d7d5 d7d6 e7e5 e7e6 f7f5 f7f6 g7g5 g7g6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 d1d2 d1d3 e1d2 e2e3 e2e4 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 d1d2 d1d3 e1d2 e2e3 e2e4 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d5e4 d8d6 d8d7 e7e5 e7e6 e8d7 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d6 d8d7 e7e5 e7e6 e8d7 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 d1d2 d1d3 d1e2 d1f3 d1g4 d1h5 d4d5 e1d2 e1e2 f1a6 f1b5 f1c4 f1d3 f1e2 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 d1d2 d1d3 d1e2 d1f3 d1g4 d1h5 d4d5 e1d2 e1e2 f1a6 f1b5 f1c4 f1d3 f1e2 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e4e3 e7e5 e7e6 e8d7 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e4e3 e7e5 e8d7 f7f5 f7f6 g7g5 g7g6 g8f6 g8h6 h7h5 h7h6",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 d1d2 d1d3 d4d5 e1d2 e1f1 e2a6 e2b5 e2c4 e2d3 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 d1d2 d1d3 d4d5 e1d2 e1f1 e2a6 e2b5 e2c4 e2d3 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e4d3 e4e3 e7e5 e7e6 e8d7 f6d5 f6d7 f6g4 f6g8 f6h5 g7g5 g7g6 h7h5 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e4e3 e7e5 e7e6 e8d7 f6d5 f6d7 f6g4 f6g8 f6h5 g7g5 g7g6 h7h5 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 c2d3 d4d5 e1d1 e1d2 e1f1 e2d1 e2d3 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 c2c3 c2c4 c2d3 d4d5 e1d1 e1d2 e1f1 e2d1 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h5 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 b7b5 b7b6 b8a6 b8c6 b8d7 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h5 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 d4d5 e1d1 e1d2 e1f1 e2d1 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 d4d5 e1d1 e1d2 e1f1 e2d1 e2f1 e2f3 e2g4 e2h5 f2f3 f2f4 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c6a5 c6b4 c6b8 c6d4 c6e5 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c6a5 c6b4 c6b8 c6d4 c6e5 c8d7 c8e6 c8f5 c8g4 c8h3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 e1d1 e1d2 e1f1 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4 h5d1 h5e2 h5f3 h5f7 h5g4 h5g6",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b1d2 b2b3 b2b4 c1d2 c1e3 c1f4 c1g5 c1h6 e1d1 e1d2 e1f1 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4 h5e2 h5f3 h5f7 h5g4 h5g6",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d4b3 d4b5 d4c2 d4c6 d4e2 d4e6 d4f3 d4f5 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d4b3 d4b5 d4c2 d4c6 d4e2 d4e6 d4f3 d4f5 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves e1d1 e1e2 e1f1",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves e1e2 e1f1",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c2a1 c2a3 c2b4 c2d4 c2e1 c2e3 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a7a5 a7a6 a8b8 b7b5 b7b6 c2a1 c2a3 c2b4 c2d4 c2e1 c2e3 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 d2a5 d2b4 d2c1 d2c3 d2e1 d2e3 d2f4 d2g5 d2h6 d3d4 f1e1 f1e2 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4 h5d1 h5e2 h5f3 h5f7 h5g4 h5g6",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a2a3 a2a4 b1a3 b1c3 b2b3 b2b4 d2a5 d2b4 d2c1 d2c3 d2e1 d2e3 d2f4 d2g5 d2h6 d3d4 f1e1 f1e2 f2f3 f2f4 g1e2 g1f3 g1h3 g2g3 g2g4 h2h3 h2h4 h5d1 h5f3 h5f7 h5g4 h5g6",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a1b3 a1c2 a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a1b3 a1c2 a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d8d3 d8d4 d8d5 d8d6 d8d7 e7e5 e7e6 e8d7 f6d5 f6d7 f6e4 f6g4 f6g8 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves f1e1 g1e2",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves f1e1 g1e2 h5e2",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a1b3 a1c2 a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d3a3 d3a6 d3b1 d3b3 d3b5 d3c2 d3c3 d3c4 d3d1 d3d2 d3d4 d3d5 d3d6 d3d7 d3d8 d3e2 d3e3 d3e4 d3f1 d3f3 d3f5 d3g3 d3g6 d3h3 e7e5 e7e6 e8d7 e8d8 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8",
      "request engine TORCH",
      "request cmd go nodes 150000 searchmoves a1b3 a7a5 a7a6 a8b8 b7b5 b7b6 c7c5 c7c6 c8d7 c8e6 c8f5 c8g4 c8h3 d3a3 d3a6 d3b1 d3b3 d3b5 d3c2 d3c3 d3c4 d3d1 d3d2 d3d4 d3d5 d3d6 d3d7 d3d8 d3e2 d3e3 d3e4 d3f1 d3f3 d3f5 d3g3 d3g6 d3h3 e7e5 e7e6 e8d7 e8d8 f6d5 f6d7 f6e4 f6g4 f6g8 f6h5 g7g5 g7g6 h7h6 h8g8"
    ],
    "duringReview": []
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18568, FND-18569

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18589"></a>
## FND-18589: Trial comparison-human — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "comparison-human",
    "reviewEvaluations": true,
    "preSearch": {
      "gameReviewSearchSettings": {
        "strength": 1
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {}
        }
      }
    },
    "addPreSearch": true,
    "saveReview": true,
    "timeoutSeconds": 90
  },
  "started": "2026-11-14T20:25:13.271Z",
  "actual": {
    "accuracy": {
      "white": 59.01492691040039,
      "black": 95.37910461425781
    },
    "ratings": {
      "white": 400,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 1,
        "7": 1,
        "8": 6,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "f26ffb5773601a7ce614334121b8a0fa9ea76ee8c8596e82110213964a15d84d",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.59,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0799",
  "outcome": "complete numeric result",
  "completed_presearch_points": 21,
  "presearch_progress_values": [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "searchAudit": {
    "beforeReview": [
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02",
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_depth_limit 6 split_width_limit 2 allowed_excess_depth 0 allowed_excess_width 2 rating 2100 max_allowed_cp_margin 100 ep_loss_margin 0.02"
    ],
    "duringReview": []
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18590, FND-18591

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18611"></a>
## FND-18611: Trial depth-12 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "depth-12",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 12,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 12,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:00:21.624Z",
  "actual": {
    "accuracy": {
      "white": 58.20283126831055,
      "black": 95.31281280517578
    },
    "ratings": {
      "white": 450,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 1,
        "7": 1,
        "8": 5,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "36328e91004ecdb8c16bd47ca011c5b03beb1028ef024786c26487eac2824e4c",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 12,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 12,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 5.556,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0800",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0800** `research/refinement/results/depth-12.json` — [preserved redacted evidence](../evidence/text/9fe9993541c180e59f3f190a15bcf157418ff08940dc38f1b9f760691c828c73.json)

**Source references:** SRC-0800, SRC-1988  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18612"></a>
## FND-18612: Trial depth-16 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "depth-16",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 16,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 16,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:00:31.352Z",
  "actual": {
    "accuracy": {
      "white": 60.66204071044922,
      "black": 97.47888946533203
    },
    "ratings": {
      "white": 450,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "e843962fed9bf548ad660e9e7ad19f4f0c29f91b9c4d1e0d88a8758b700be109",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 16,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 16,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.833,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0801",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0801** `research/refinement/results/depth-16.json` — [preserved redacted evidence](../evidence/text/c064aeac3801297d2679d332b2133a9a93c220f6bdffbb0677777b31dcb65e8a.json)

**Source references:** SRC-0801, SRC-2000  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18613"></a>
## FND-18613: Trial depth-18 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "depth-18",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 18,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 18,
            "numLines": 1
          }
        }
      }
    },
    "timeoutSeconds": 60
  },
  "started": "2026-11-14T19:00:48.437Z",
  "actual": {
    "accuracy": {
      "white": 59.763641357421875,
      "black": 94.91861724853516
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 3,
        "7": 0,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "513b657aadaf257bd5803eeff518668dcd545abf1df0bda1be699076df546df2",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 18,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 18,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 35.807,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0802",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0802** `research/refinement/results/depth-18.json` — [preserved redacted evidence](../evidence/text/f7440ffaf1d10e556afff6c843d7821bc6b5126792748bb25ea393dc4cc04533.json)

**Source references:** SRC-0802, SRC-2027  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18614"></a>
## FND-18614: Trial depth-22 — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "depth-22",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 22,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 22,
            "numLines": 1
          }
        }
      }
    },
    "timeoutSeconds": 60
  },
  "started": "2026-11-14T19:01:24.419Z",
  "error": "trial timeout after 60s",
  "warnings": [],
  "source_id": "SRC-0803",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0803** `research/refinement/results/depth-22.json` — [preserved redacted evidence](../evidence/text/0dd67febd556b9c81c445b4bd9e60f3709535311811920cba5b76f38cbe09e16.json)

**Source references:** SRC-0803, SRC-1979  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18615"></a>
## FND-18615: Trial embedded-human-pvtrees — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "embedded-human-pvtrees",
    "pvtrees": {
      "request": {
        "search": {
          "case": "searchParameters",
          "value": {
            "nodesLimit": 300000,
            "numLines": 1
          }
        },
        "torchSearchMode": {
          "mode": {
            "case": "human",
            "value": {}
          }
        }
      },
      "pvtreeOptions": {
        "rating": 100
      }
    }
  },
  "started": "2026-11-14T19:05:01.514Z",
  "error": "trial timeout after 150s",
  "warnings": [],
  "source_id": "SRC-0804",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0804** `research/refinement/results/embedded-human-pvtrees.json` — [preserved redacted evidence](../evidence/text/63fc62590e886ea5dabb178de6d643e1013d3434660ed992a5bf3506891473a7.json)

**Source references:** SRC-0804, SRC-1997  
**URL references:** None independently associated  
**Related findings:** FND-18974

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18616"></a>
## FND-18616: Trial followup-hash128-softfalse — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash128-softfalse",
    "uciAfter": {
      "Normalize": false,
      "Hash": 128,
      "UseSoftNodes": false
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:16:18.042Z",
  "actual": {
    "accuracy": {
      "white": 65.15036010742188,
      "black": 99.21577453613281
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 0,
        "8": 6,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "755db5fe49b0247429804f2637422f2fe0a70854d591f59c9dfb4012c01181fb",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.847,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0805",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805, SRC-1975  
**URL references:** None independently associated  
**Related findings:** FND-18617, FND-18618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18638"></a>
## FND-18638: Trial followup-hash128-softtrue — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash128-softtrue",
    "uciAfter": {
      "Normalize": false,
      "Hash": 128,
      "UseSoftNodes": true
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:16:35.027Z",
  "actual": {
    "accuracy": {
      "white": 65.3160629272461,
      "black": 99.38276672363281
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "b5afea7213d6c15dba89cc33b181f57746005977cf9e9ae9253d08a71b7f8b76",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 23.455,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0806",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806, SRC-2024  
**URL references:** None independently associated  
**Related findings:** FND-18639, FND-18640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18660"></a>
## FND-18660: Trial followup-hash32-softfalse — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash32-softfalse",
    "uciAfter": {
      "Normalize": false,
      "Hash": 32,
      "UseSoftNodes": false
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:14:56.222Z",
  "actual": {
    "accuracy": {
      "white": 66.01242065429688,
      "black": 99.10324096679688
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 1,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "de75fbe5d8c0e6cb353b6d213e2c14df276723ad52234641dbb0546504b4465c",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.754,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0807",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0807** `research/refinement/results/followup-hash32-softfalse.json` — [preserved redacted evidence](../evidence/text/e3642c41e53040ebeff4327a13b709591bcb9891d7ca970398a8ade32c9366f3.json)

**Source references:** SRC-0807, SRC-2023  
**URL references:** None independently associated  
**Related findings:** FND-18661, FND-18662

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18682"></a>
## FND-18682: Trial followup-hash32-softtrue — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash32-softtrue",
    "uciAfter": {
      "Normalize": false,
      "Hash": 32,
      "UseSoftNodes": true
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:15:13.105Z",
  "actual": {
    "accuracy": {
      "white": 65.15916442871094,
      "black": 98.37834930419922
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "e88fb97571fd4560d27c598d84b9b6d6e4b3f3cf472bf92d27e464252e211ded",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 21.917,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0808",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0808** `research/refinement/results/followup-hash32-softtrue.json` — [preserved redacted evidence](../evidence/text/9e0a126148a8592961161a6a38e743fcbcf3e7c9fef2d3095cade8211ffdfe60.json)

**Source references:** SRC-0808, SRC-1980  
**URL references:** None independently associated  
**Related findings:** FND-18683, FND-18684

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18704"></a>
## FND-18704: Trial followup-hash64-repeat — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash64-repeat",
    "uciAfter": {
      "Normalize": false,
      "Hash": 64
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:14:38.773Z",
  "actual": {
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 5,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "09679555a521fb012bcbe462d1aac31797582c1ba0fa730248b8a973a1731477",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.278,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0809",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0809** `research/refinement/results/followup-hash64-repeat.json` — [preserved redacted evidence](../evidence/text/447c9263aa911e0e3185ddde0917fed04fdd826f9884b35299e764e56b0f7dea.json)

**Source references:** SRC-0809, SRC-2025  
**URL references:** None independently associated  
**Related findings:** FND-18705, FND-18706

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18726"></a>
## FND-18726: Trial followup-hash64-softfalse — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash64-softfalse",
    "uciAfter": {
      "Normalize": false,
      "Hash": 64,
      "UseSoftNodes": false
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:15:35.214Z",
  "actual": {
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 5,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "09679555a521fb012bcbe462d1aac31797582c1ba0fa730248b8a973a1731477",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.985,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0810",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0810** `research/refinement/results/followup-hash64-softfalse.json` — [preserved redacted evidence](../evidence/text/8c9fb429b5e804dec6f04a316102e62a9b8629962a865562b3f1d917c2b16308.json)

**Source references:** SRC-0810, SRC-2017  
**URL references:** None independently associated  
**Related findings:** FND-18727, FND-18728

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18748"></a>
## FND-18748: Trial followup-hash64-softtrue — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-hash64-softtrue",
    "uciAfter": {
      "Normalize": false,
      "Hash": 64,
      "UseSoftNodes": true
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:15:53.368Z",
  "actual": {
    "accuracy": {
      "white": 65.71549987792969,
      "black": 99.19789123535156
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "e6602352be300a95200364c79b9f6248967da3aecfc53fd5818323e19eef4d91",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 24.505,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0811",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0811** `research/refinement/results/followup-hash64-softtrue.json` — [preserved redacted evidence](../evidence/text/ec0ecf507b8cf076f00a89104e7fd749c47cff406f61f06c61185435d35138d3.json)

**Source references:** SRC-0811, SRC-1999  
**URL references:** None independently associated  
**Related findings:** FND-18749, FND-18750

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18770"></a>
## FND-18770: Trial followup-soft-factor200 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-soft-factor200",
    "uciAfter": {
      "Normalize": false,
      "UseSoftNodes": true,
      "HardSoftNodeFactor": 200
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:17:22.457Z",
  "actual": {
    "accuracy": {
      "white": 66.39828491210938,
      "black": 98.71414947509766
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "8b81e3ae0d2d2d84d550a876d34725cb62ab0d2c2e6b19233f8eb7f4877248af",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 22.635,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0812",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0812** `research/refinement/results/followup-soft-factor200.json` — [preserved redacted evidence](../evidence/text/5dedac464481da11ade84d756924369b0139baf180932d907b719847d96dc1d6.json)

**Source references:** SRC-0812, SRC-1987  
**URL references:** None independently associated  
**Related findings:** FND-18771, FND-18772

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18792"></a>
## FND-18792: Trial followup-soft-factor50 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "followup-soft-factor50",
    "uciAfter": {
      "Normalize": false,
      "UseSoftNodes": true,
      "HardSoftNodeFactor": 50
    },
    "saveReview": true
  },
  "started": "2026-11-14T19:16:58.659Z",
  "actual": {
    "accuracy": {
      "white": 66.39828491210938,
      "black": 98.71414947509766
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "8b81e3ae0d2d2d84d550a876d34725cb62ab0d2c2e6b19233f8eb7f4877248af",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 23.65,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0813",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0813** `research/refinement/results/followup-soft-factor50.json` — [preserved redacted evidence](../evidence/text/567a3a363ab87a4e3bda11fb4f3110062ca5375dbfe6019b7f15ae5eaa113186.json)

**Source references:** SRC-0813, SRC-2026  
**URL references:** None independently associated  
**Related findings:** FND-18793, FND-18794

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18814"></a>
## FND-18814: Trial nodes-150000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "nodes-150000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "nodesLimit": 150000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "nodesLimit": 150000,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:02:34.828Z",
  "actual": {
    "accuracy": {
      "white": 59.45392608642578,
      "black": 94.97537994384766
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "dde3922db91eca1ffb52fa122e58a83caf7dc1a887f05870c4001b035d3e0fa8",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "nodesLimit": 150000
        },
        "nullMoveSearchParameters": {
          "nodesLimit": 150000
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 21.741,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0814",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0814** `research/refinement/results/nodes-150000.json` — [preserved redacted evidence](../evidence/text/f5c125ebd2746b70e7bb99b1601c82a1a6e5cfc8cf813543fdcc7d551090da73.json)

**Source references:** SRC-0814, SRC-1976  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18815"></a>
## FND-18815: Trial nodes-300000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "nodes-300000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "nodesLimit": 300000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "nodesLimit": 300000,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:02:56.729Z",
  "actual": {
    "accuracy": {
      "white": 58.44866943359375,
      "black": 93.21588134765625
    },
    "ratings": {
      "white": 350,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 3,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "e41344c7b34c99ffb295e6874acaf37575202a08a3c8d02b07b387a7d94bded8",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "nodesLimit": 300000
        },
        "nullMoveSearchParameters": {
          "nodesLimit": 300000
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 40.093,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0815",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0815** `research/refinement/results/nodes-300000.json` — [preserved redacted evidence](../evidence/text/a912fb4e94ae26a6163f9ca12eae4db2e726598d96e9d76e77e357c8001a1ee8.json)

**Source references:** SRC-0815, SRC-2014  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18816"></a>
## FND-18816: Trial nodes-40000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "nodes-40000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "nodesLimit": 40000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "nodesLimit": 40000,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:02:24.687Z",
  "actual": {
    "accuracy": {
      "white": 59.881385803222656,
      "black": 95.71517181396484
    },
    "ratings": {
      "white": 350,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 1,
        "8": 6,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "6431d42a5e692031253e8d686c122b1a16f340472692121006e5a9707d337d02",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "nodesLimit": 40000
        },
        "nullMoveSearchParameters": {
          "nodesLimit": 40000
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 9.994,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0816",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0816** `research/refinement/results/nodes-40000.json` — [preserved redacted evidence](../evidence/text/7d27e95c195d75c1f692fb917615a8438ab17b9294d626385053eb77680396b3.json)

**Source references:** SRC-0816, SRC-2007  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18817"></a>
## FND-18817: Trial nodes-600000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "nodes-600000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "nodesLimit": 600000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "nodesLimit": 600000,
            "numLines": 1
          }
        }
      }
    }
  },
  "started": "2026-11-14T19:03:36.945Z",
  "actual": {
    "accuracy": {
      "white": 61.58863830566406,
      "black": 96.10839080810547
    },
    "ratings": {
      "white": 350,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "82d173136693c0f039d2caf122cab40c6a7314016ae6c17cf2944014e7952f78",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "nodesLimit": 600000
        },
        "nullMoveSearchParameters": {
          "nodesLimit": 600000
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 84.415,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0817",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0817** `research/refinement/results/nodes-600000.json` — [preserved redacted evidence](../evidence/text/574b6787a717030cfcca0fb2b913abbeb4f26b7407292ed7c32fb51a39567445.json)

**Source references:** SRC-0817, SRC-2008  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18818"></a>
## FND-18818: Trial normalized-ClearBetweenSearches-true — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-ClearBetweenSearches-true",
    "uciAfter": {
      "Normalize": false,
      "ClearBetweenSearches": true
    }
  },
  "started": "2026-11-14T19:11:38.442Z",
  "actual": {
    "accuracy": {
      "white": 65.74172973632812,
      "black": 99.03148651123047
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 1,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "fcb7ef0847813bc2e3981d2da3d1376eb134b82db119871fba50a63b8779de10",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.101,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0818",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0818** `research/refinement/results/normalized-ClearBetweenSearches-true.json` — [preserved redacted evidence](../evidence/text/3e7912dd4339630e9f44f2b66ca2abadd9703206eda6558cbc140187bc0b9c78.json)

**Source references:** SRC-0818, SRC-1974  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18819"></a>
## FND-18819: Trial normalized-HardSoftNodeFactor-200 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-HardSoftNodeFactor-200",
    "uciAfter": {
      "Normalize": false,
      "HardSoftNodeFactor": 200
    }
  },
  "started": "2026-11-14T19:10:23.798Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.774,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0819",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0819** `research/refinement/results/normalized-HardSoftNodeFactor-200.json` — [preserved redacted evidence](../evidence/text/f48e4a62af3fa2cca0b02499f5b378f9d47a909c5f76fc1cc936211eb6a47d88.json)

**Source references:** SRC-0819, SRC-2010  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18820"></a>
## FND-18820: Trial normalized-HardSoftNodeFactor-50 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-HardSoftNodeFactor-50",
    "uciAfter": {
      "Normalize": false,
      "HardSoftNodeFactor": 50
    }
  },
  "started": "2026-11-14T19:10:06.993Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.63,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0820",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0820** `research/refinement/results/normalized-HardSoftNodeFactor-50.json` — [preserved redacted evidence](../evidence/text/908be2764c0f95208e21f240ac795ff37b3753a6ad2937f4d1c8d7e3d44e88fa.json)

**Source references:** SRC-0820, SRC-2016  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18821"></a>
## FND-18821: Trial normalized-Hash-64 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-Hash-64",
    "uciAfter": {
      "Normalize": false,
      "Hash": 64
    }
  },
  "started": "2026-11-14T19:11:19.571Z",
  "actual": {
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 5,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "09679555a521fb012bcbe462d1aac31797582c1ba0fa730248b8a973a1731477",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.741,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0821",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0821** `research/refinement/results/normalized-Hash-64.json` — [preserved redacted evidence](../evidence/text/124de40ebd9ea3b9a089eb88c0ce34f12b282acb6d90d181c1c598a09148b16b.json)

**Source references:** SRC-0821, SRC-2021  
**URL references:** None independently associated  
**Related findings:** FND-18966

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18822"></a>
## FND-18822: Trial normalized-Minimal-true — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-Minimal-true",
    "uciAfter": {
      "Normalize": false,
      "Minimal": true
    }
  },
  "started": "2026-11-14T19:11:54.686Z",
  "error": "Error: RuntimeError: Aborted(Assertion failed: n.has_score(), at: ../../src/features/game_review.cpp,144,build_move_from_node). Build with -sASSERTIONS for more info.\n    at globalThis.postMessage (file:///home/user/research/refinement/trial.mjs:25:53)\n    at Object.onmessage (file:///home/user/research/refinement/trial.mjs:35:19)\n    at Object.log (/home/user/extension/engines/cee/explanation-engine.js:1:128216)\n    at /home/user/extension/engines/cee/explanation-engine.js:1:128777",
  "warnings": [],
  "source_id": "SRC-0822",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0822** `research/refinement/results/normalized-Minimal-true.json` — [preserved redacted evidence](../evidence/text/4c72d5336ac42c7d7eee6c5de79e7d02b98ab1c2337fbc0b6e291ab358475471.json)

**Source references:** SRC-0822, SRC-2028  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18823"></a>
## FND-18823: Trial normalized-NodeFudging-100 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-NodeFudging-100",
    "uciAfter": {
      "Normalize": false,
      "NodeFudging": 100
    }
  },
  "started": "2026-11-14T19:10:40.749Z",
  "actual": {
    "accuracy": {
      "white": 65.36044311523438,
      "black": 98.88133239746094
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "479276bb68a899d114f04771da8f9254c3880144b3d69e2c4e89d50be6c01b22",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.601,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0823",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0823** `research/refinement/results/normalized-NodeFudging-100.json` — [preserved redacted evidence](../evidence/text/c46f8c6cf54039d88e7b1d73fbdf60ceba7a8ca24d3b2d03c67b3e93dac31268.json)

**Source references:** SRC-0823, SRC-1973  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18824"></a>
## FND-18824: Trial normalized-NodeFudging-1000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-NodeFudging-1000",
    "uciAfter": {
      "Normalize": false,
      "NodeFudging": 1000
    }
  },
  "started": "2026-11-14T19:10:58.478Z",
  "actual": {
    "accuracy": {
      "white": 64.94029235839844,
      "black": 99.02162170410156
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 0,
        "8": 6,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "c4051627ba7e3ac79365049dbda83504fb0746193b537004dadc5e1505b23e43",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 20.93,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0824",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0824** `research/refinement/results/normalized-NodeFudging-1000.json` — [preserved redacted evidence](../evidence/text/b5652d112ea99629095966f1d96bbfda887aaab56e16fbd1320433797cb3d3e7.json)

**Source references:** SRC-0824, SRC-1985  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18825"></a>
## FND-18825: Trial normalized-UseSoftNodes-true — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-UseSoftNodes-true",
    "uciAfter": {
      "Normalize": false,
      "UseSoftNodes": true
    }
  },
  "started": "2026-11-14T19:09:41.262Z",
  "actual": {
    "accuracy": {
      "white": 66.39828491210938,
      "black": 98.71414947509766
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "8b81e3ae0d2d2d84d550a876d34725cb62ab0d2c2e6b19233f8eb7f4877248af",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 25.577,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0825",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0825** `research/refinement/results/normalized-UseSoftNodes-true.json` — [preserved redacted evidence](../evidence/text/dce1414e7737d9704f2ab178673267d6b083cc3a1ee413b924efc8b1dbb3966e.json)

**Source references:** SRC-0825, SRC-1992  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18826"></a>
## FND-18826: Trial normalized-class-v2 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-class-v2",
    "settings": {
      "moveClassificationVersion": 1
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:09:22.628Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 1,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.489,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0826",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0826** `research/refinement/results/normalized-class-v2.json` — [preserved redacted evidence](../evidence/text/053167bf4f919f3167faab267eea238eba0333cd067d4855d4e045d5ce86e366.json)

**Source references:** SRC-0826, SRC-2002  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18827"></a>
## FND-18827: Trial normalized-evaluate-normal — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-evaluate-normal",
    "evaluateGame": {
      "search": {
        "case": "gameReviewSearchSettings",
        "value": {
          "strength": 1
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:08:23.407Z",
  "error": "Error: RuntimeError: Aborted(). Build with -sASSERTIONS for more info.\n    at globalThis.postMessage (file:///home/user/research/refinement/trial.mjs:24:53)\n    at Object.onmessage (file:///home/user/research/refinement/trial.mjs:34:19)\n    at Object.log (/home/user/extension/engines/cee/explanation-engine.js:1:128216)\n    at /home/user/extension/engines/cee/explanation-engine.js:1:128777",
  "warnings": [],
  "source_id": "SRC-0827",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0827** `research/refinement/results/normalized-evaluate-normal.json` — [preserved redacted evidence](../evidence/text/68a206e4b11c88aad3f4639678d58ff815320a2c8458afcc4f5ebb1dad4b87da.json)

**Source references:** SRC-0827, SRC-2019  
**URL references:** None independently associated  
**Related findings:** FND-18939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18828"></a>
## FND-18828: Trial normalized-human-no-maia — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-human-no-maia",
    "timeoutSeconds": 90,
    "evaluateGame": {
      "search": {
        "case": "gameReviewSearchSettings",
        "value": {
          "strength": 1
        }
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {
            "disableMaia": true
          }
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:13:54.503Z",
  "error": "Error: RuntimeError: Aborted(). Build with -sASSERTIONS for more info.\n    at globalThis.postMessage (file:///home/user/research/refinement/trial.mjs:25:53)\n    at Object.onmessage (file:///home/user/research/refinement/trial.mjs:35:19)\n    at Object.log (/home/user/extension/engines/cee/explanation-engine.js:1:128216)\n    at /home/user/extension/engines/cee/explanation-engine.js:1:128777",
  "warnings": [],
  "source_id": "SRC-0828",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0828** `research/refinement/results/normalized-human-no-maia.json` — [preserved redacted evidence](../evidence/text/5944404dd9a408703303a04e355431dc70706a9ab4babcbf35e973cf924b2792.json)

**Source references:** SRC-0828, SRC-1972  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18829"></a>
## FND-18829: Trial normalized-human — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-human",
    "timeoutSeconds": 90,
    "evaluateGame": {
      "search": {
        "case": "gameReviewSearchSettings",
        "value": {
          "strength": 1
        }
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {}
        }
      }
    },
    "saveReview": true,
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:13:48.617Z",
  "error": "Error: RuntimeError: Aborted(). Build with -sASSERTIONS for more info.\n    at globalThis.postMessage (file:///home/user/research/refinement/trial.mjs:25:53)\n    at Object.onmessage (file:///home/user/research/refinement/trial.mjs:35:19)\n    at Object.log (/home/user/extension/engines/cee/explanation-engine.js:1:128216)\n    at /home/user/extension/engines/cee/explanation-engine.js:1:128777",
  "warnings": [],
  "source_id": "SRC-0829",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0829** `research/refinement/results/normalized-human.json` — [preserved redacted evidence](../evidence/text/5f877d6dfce70086ccbb799b80ba1c6fa8d92cb20dce2162f57d024857df0dd3.json)

**Source references:** SRC-0829, SRC-1989  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18830"></a>
## FND-18830: Trial normalized-nodes-300000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-nodes-300000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 6,
            "nodesLimit": 300000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 6,
            "nodesLimit": 40000,
            "numLines": 1
          }
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:12:27.584Z",
  "actual": {
    "accuracy": {
      "white": 66.40452575683594,
      "black": 98.5245361328125
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "ba37354c31cd8d12a449a42926ad8fa4d6dcb3749a713ef55ab49423e0fe2abe",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 300000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 29.122,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0830",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0830** `research/refinement/results/normalized-nodes-300000.json` — [preserved redacted evidence](../evidence/text/27a4fa5fa4065f1d42822b1ae6ac3f6f0bff55a38f9112838f031d4dd7baea78.json)

**Source references:** SRC-0830, SRC-1971  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18831"></a>
## FND-18831: Trial normalized-nodes-40000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-nodes-40000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 6,
            "nodesLimit": 40000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 6,
            "nodesLimit": 40000,
            "numLines": 1
          }
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:12:08.360Z",
  "actual": {
    "accuracy": {
      "white": 64.62260437011719,
      "black": 99.14017486572266
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 0,
        "8": 6,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "37d2e79a10b72d1909b6d82fb45860b9d61028603415292441954bc29b7869c3",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 8.119,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0831",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0831** `research/refinement/results/normalized-nodes-40000.json` — [preserved redacted evidence](../evidence/text/47ebc3f68032e9237748ba787ab3e5a7a34e1421b05e48215c379de5260daf11.json)

**Source references:** SRC-0831, SRC-1998  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18832"></a>
## FND-18832: Trial normalized-nodes-600000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-nodes-600000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 6,
            "nodesLimit": 600000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 6,
            "nodesLimit": 40000,
            "numLines": 1
          }
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:12:56.862Z",
  "actual": {
    "accuracy": {
      "white": 66.5762939453125,
      "black": 99.24345397949219
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 1,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "3e6be1111801c717666b20e56828f8a3344133409aaa627285428698ecd9a573",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 600000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 51.6,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0832",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0832** `research/refinement/results/normalized-nodes-600000.json` — [preserved redacted evidence](../evidence/text/9e4ca92f92c2af0d6950967149a70148658bc8b1b8e5099bef4f9301fc9812ef.json)

**Source references:** SRC-0832, SRC-1991  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18833"></a>
## FND-18833: Trial normalized-nodes-75000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-nodes-75000",
    "settings": {
      "search": {
        "case": "searchSettings",
        "value": {
          "searchParameters": {
            "depthLimit": 6,
            "nodesLimit": 75000,
            "numLines": 2
          },
          "nullMoveSearchParameters": {
            "depthLimit": 6,
            "nodesLimit": 40000,
            "numLines": 1
          }
        }
      }
    },
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:12:16.610Z",
  "actual": {
    "accuracy": {
      "white": 64.58173370361328,
      "black": 99.13462829589844
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 0,
        "7": 0,
        "8": 6,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "ade09abf3167caeb0866750d350ccc8e3a4d9f30789dd8e6fcd6efb6d94812a7",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 75000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 10.692,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0833",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0833** `research/refinement/results/normalized-nodes-75000.json` — [preserved redacted evidence](../evidence/text/1dcb84bab6afc6d90bc15f132136f741343caba61ca7e4ff1ec9722ccf76c5f8.json)

**Source references:** SRC-0833, SRC-2004  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18834"></a>
## FND-18834: Trial normalized-repeat-1 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-repeat-1",
    "saveReview": true,
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:07:49.699Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.915,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0834",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0834** `research/refinement/results/normalized-repeat-1.json` — [preserved redacted evidence](../evidence/text/5b06faa553321a13a78397901efcbfcc94d003f9401f84bbd8e6dd6864c5ea43.json)

**Source references:** SRC-0834, SRC-2005  
**URL references:** None independently associated  
**Related findings:** FND-18835, FND-18836

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18856"></a>
## FND-18856: Trial normalized-repeat-2 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-repeat-2",
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:08:06.741Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.476,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0835",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0835** `research/refinement/results/normalized-repeat-2.json` — [preserved redacted evidence](../evidence/text/6680a6864b633db58d68fde1e0be8aa92832353383672b03a0765d4ab5d68b59.json)

**Source references:** SRC-0835, SRC-2009  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18857"></a>
## FND-18857: Trial normalized-standard — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "normalized-standard",
    "strength": 2,
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T19:08:30.016Z",
  "actual": {
    "accuracy": {
      "white": 66.5762939453125,
      "black": 99.24345397949219
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 1,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "3e6be1111801c717666b20e56828f8a3344133409aaa627285428698ecd9a573",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 600000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 52.443,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0836",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0836** `research/refinement/results/normalized-standard.json` — [preserved redacted evidence](../evidence/text/58fb9caff6297d6eefa79ec8f82fae70ae73f009b922b1ca10dfb2ad984cac27.json)

**Source references:** SRC-0836, SRC-2029  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18858"></a>
## FND-18858: Trial probe-human-no-maia — search-only result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "probe-human-no-maia",
    "preSearch": {
      "search": {
        "case": "searchParameters",
        "value": {
          "nodesLimit": 1000,
          "numLines": 1
        }
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {
            "disableMaia": true
          }
        }
      }
    },
    "rootOnly": true,
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:24.947Z",
  "elapsedSeconds": 1.301,
  "warnings": [],
  "source_id": "SRC-0837",
  "outcome": "search-only result",
  "completed_presearch_points": 1,
  "presearch_progress_values": [
    null
  ]
}

### Evidence

- **SRC-0837** `research/refinement/results/probe-human-no-maia.json` — [preserved redacted evidence](../evidence/text/381002d31f1df42f6d8d4168983819edb6243a0393e75858b6ab3b702a5c0b34.json)

**Source references:** SRC-0837  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18859"></a>
## FND-18859: Trial probe-human — search-only result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "probe-human",
    "preSearch": {
      "search": {
        "case": "searchParameters",
        "value": {
          "nodesLimit": 1000,
          "numLines": 1
        }
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {}
        }
      }
    },
    "rootOnly": true,
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:21:38.821Z",
  "elapsedSeconds": 1.541,
  "warnings": [],
  "source_id": "SRC-0838",
  "outcome": "search-only result",
  "completed_presearch_points": 1,
  "presearch_progress_values": [
    1
  ]
}

### Evidence

- **SRC-0838** `research/refinement/results/probe-human-offline.json` — [preserved redacted evidence](../evidence/text/0961e9ec73c34d2d6963726adddc0c9d8d4fe911421d9d594fc7a85b5682b683.json)

**Source references:** SRC-0838  
**URL references:** None independently associated  
**Related findings:** FND-18936, FND-18937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18860"></a>
## FND-18860: Trial probe-human — search-only result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "probe-human",
    "preSearch": {
      "search": {
        "case": "searchParameters",
        "value": {
          "nodesLimit": 1000,
          "numLines": 1
        }
      },
      "torchSearchMode": {
        "mode": {
          "case": "human",
          "value": {}
        }
      }
    },
    "rootOnly": true,
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:18.007Z",
  "elapsedSeconds": 1.254,
  "warnings": [],
  "source_id": "SRC-0839",
  "outcome": "search-only result",
  "completed_presearch_points": 1,
  "presearch_progress_values": [
    null
  ]
}

### Evidence

- **SRC-0839** `research/refinement/results/probe-human.json` — [preserved redacted evidence](../evidence/text/eca8680fa304ffbee854c03e0cd971dd4c0d1829149c58e4b6db51df20916348.json)

**Source references:** SRC-0839  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18861"></a>
## FND-18861: Trial probe-normal — search-only result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "probe-normal",
    "preSearch": {
      "search": {
        "case": "searchParameters",
        "value": {
          "nodesLimit": 1000,
          "numLines": 1
        }
      }
    },
    "rootOnly": true,
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:21:52.648Z",
  "elapsedSeconds": 1.5,
  "warnings": [],
  "source_id": "SRC-0840",
  "outcome": "search-only result",
  "completed_presearch_points": 1,
  "presearch_progress_values": [
    1
  ]
}

### Evidence

- **SRC-0840** `research/refinement/results/probe-normal-offline.json` — [preserved redacted evidence](../evidence/text/1fbe6d1ae3661e771905f598ec51fc6101fb3358a97884161c353b29b5ad6390.json)

**Source references:** SRC-0840  
**URL references:** None independently associated  
**Related findings:** FND-18937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18862"></a>
## FND-18862: Trial probe-normal — search-only result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "probe-normal",
    "preSearch": {
      "search": {
        "case": "searchParameters",
        "value": {
          "nodesLimit": 1000,
          "numLines": 1
        }
      }
    },
    "rootOnly": true,
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:10.671Z",
  "elapsedSeconds": 1.468,
  "warnings": [],
  "source_id": "SRC-0841",
  "outcome": "search-only result",
  "completed_presearch_points": 1,
  "presearch_progress_values": [
    null
  ]
}

### Evidence

- **SRC-0841** `research/refinement/results/probe-normal.json` — [preserved redacted evidence](../evidence/text/d6095c23dc36d73b306eb0798e0cfcf3e473b8c99ed46e172052f4ce2fa2d540.json)

**Source references:** SRC-0841  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18863"></a>
## FND-18863: Trial pvtree-human — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "pvtree-human",
    "pvtrees": {
      "request": {
        "search": {
          "case": "searchParameters",
          "value": {
            "nodesLimit": 1000,
            "numLines": 1
          }
        },
        "torchSearchMode": {
          "mode": {
            "case": "human",
            "value": {}
          }
        }
      },
      "pvtreeOptions": {
        "rating": 100
      }
    },
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:37.827Z",
  "error": "trial timeout after 20s",
  "warnings": [],
  "source_id": "SRC-0842",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0842** `research/refinement/results/probe-pvtree-human.json` — [preserved redacted evidence](../evidence/text/43fc0cef1993371775e1447ce3db95a71391464001ea7b5fa724fd24c151d6a6.json)

**Source references:** SRC-0842  
**URL references:** None independently associated  
**Related findings:** FND-18939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18864"></a>
## FND-18864: Trial pvtree-no-maia — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "pvtree-no-maia",
    "pvtrees": {
      "request": {
        "search": {
          "case": "searchParameters",
          "value": {
            "nodesLimit": 1000,
            "numLines": 1
          }
        },
        "torchSearchMode": {
          "mode": {
            "case": "human",
            "value": {
              "disableMaia": true
            }
          }
        }
      },
      "pvtreeOptions": {
        "rating": 100
      }
    },
    "searchOnly": true,
    "timeoutSeconds": 20
  },
  "started": "2026-11-14T20:20:58.183Z",
  "error": "trial timeout after 20s",
  "warnings": [],
  "source_id": "SRC-0843",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0843** `research/refinement/results/probe-pvtree-no-maia.json` — [preserved redacted evidence](../evidence/text/1765a2e583b05429253e898292483e945275ccf035b9536420d56f6c886094b9.json)

**Source references:** SRC-0843  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18865"></a>
## FND-18865: Trial strength-1-class-1 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-1-class-1",
    "strength": 1,
    "settings": {
      "moveClassificationVersion": 1
    }
  },
  "started": "2026-11-14T18:47:46.890Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 1,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.952,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0844",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0844** `research/refinement/results/strength-1-class-1.json` — [preserved redacted evidence](../evidence/text/624509e53807221986b1dd5ba84066e2a782d5defc99d32e1dab8bd9d3e05b18.json)

**Source references:** SRC-0844, SRC-2031  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18866"></a>
## FND-18866: Trial strength-1-class-2 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-1-class-2",
    "strength": 1,
    "settings": {
      "moveClassificationVersion": 2
    }
  },
  "started": "2026-11-14T18:48:05.983Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 20.203,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0845",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0845** `research/refinement/results/strength-1-class-2.json` — [preserved redacted evidence](../evidence/text/2c7c74acbbd6964592e6bcf5f8930022cfcab83a106ee6fd35587ba197d99ec6.json)

**Source references:** SRC-0845, SRC-1996  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18867"></a>
## FND-18867: Trial strength-2-class-0 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-0",
    "strength": 2,
    "settings": {}
  },
  "started": "2026-11-14T18:48:26.359Z",
  "actual": {
    "accuracy": {
      "white": 61.22994613647461,
      "black": 95.98047637939453
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 0,
        "6": 2,
        "7": 0,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "530ea27a732fd0d726dff5ad52368b9e7d8ad53812b7714edadc33c5467b8f4a",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 600000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 61.5,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0846",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0846** `research/refinement/results/strength-2-class-0.json` — [preserved redacted evidence](../evidence/text/d8f42aef6c0c1776da7181b17fc751fcec338b54656f76b26a4e4403510ee60a.json)

**Source references:** SRC-0846, SRC-2012  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18868"></a>
## FND-18868: Trial strength-2-class-1 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-1",
    "strength": 2,
    "settings": {
      "moveClassificationVersion": 1
    }
  },
  "started": "2026-11-14T18:49:27.994Z",
  "actual": {
    "accuracy": {
      "white": 61.22994613647461,
      "black": 95.98047637939453
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 0,
        "6": 2,
        "7": 0,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "530ea27a732fd0d726dff5ad52368b9e7d8ad53812b7714edadc33c5467b8f4a",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 1,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 600000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 57.027,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0847",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0847** `research/refinement/results/strength-2-class-1.json` — [preserved redacted evidence](../evidence/text/204c52634045b1e50c6aaef8b643067ad61b9778546fb27371503ef6e7385829.json)

**Source references:** SRC-0847, SRC-2015  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18869"></a>
## FND-18869: Trial strength-2-class-2 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-2-class-2",
    "strength": 2,
    "settings": {
      "moveClassificationVersion": 2
    }
  },
  "started": "2026-11-14T18:50:25.196Z",
  "actual": {
    "accuracy": {
      "white": 61.22994613647461,
      "black": 95.98047637939453
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 1,
        "5": 0,
        "6": 2,
        "7": 0,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "530ea27a732fd0d726dff5ad52368b9e7d8ad53812b7714edadc33c5467b8f4a",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 600000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 62.708,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0848",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0848** `research/refinement/results/strength-2-class-2.json` — [preserved redacted evidence](../evidence/text/0aae401583bda7b988cd268e02dd0e0e5904e8b4bee6e563c0fbb76c8990c401.json)

**Source references:** SRC-0848, SRC-2006  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18870"></a>
## FND-18870: Trial strength-3-class-0 — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-3-class-0",
    "strength": 3,
    "settings": {}
  },
  "started": "2026-11-14T18:51:28.064Z",
  "error": "trial timeout after 150s",
  "warnings": [],
  "source_id": "SRC-0849",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0849** `research/refinement/results/strength-3-class-0.json` — [preserved redacted evidence](../evidence/text/b3544719789b4afa11951e33c46780d08f13e2541af3bb1c190f4cbae1e5aa0f.json)

**Source references:** SRC-0849, SRC-1978  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18871"></a>
## FND-18871: Trial strength-4-class-0 — error/timeout

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "strength-4-class-0",
    "strength": 4,
    "settings": {},
    "timeoutSeconds": 60
  },
  "started": "2026-11-14T18:54:24.336Z",
  "error": "trial timeout after 60s",
  "warnings": [],
  "source_id": "SRC-0850",
  "outcome": "error/timeout"
}

### Evidence

- **SRC-0850** `research/refinement/results/strength-4-class-0.json` — [preserved redacted evidence](../evidence/text/9c494cfd43f29f0ad18958e4480684f5bef624e05bc27154dcbe970efcc6902d.json)

**Source references:** SRC-0850, SRC-1986  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18872"></a>
## FND-18872: Trial tricky-on — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "tricky-on",
    "experimental": {
      "allowTrickyClassification": true
    }
  },
  "started": "2026-11-14T19:00:02.937Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.531,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0851",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0851** `research/refinement/results/tricky-on.json` — [preserved redacted evidence](../evidence/text/b26f85718e64062cf79e5b8d2b2e85ff8152d210f2a747bc358fc423dd251bef.json)

**Source references:** SRC-0851, SRC-2020  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18873"></a>
## FND-18873: Trial uci-classification-combo — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-classification-combo",
    "uciAfter": {
      "EloSensitivePD": true,
      "ClassificationV3": true,
      "ForgivingClassificationsElo": 1000
    }
  },
  "started": "2026-11-14T18:59:45.115Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.683,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0852",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0852** `research/refinement/results/uci-classification-combo.json` — [preserved redacted evidence](../evidence/text/119f18b177e04174ae9975102094838bd295b66e691fda14dab0c56eec3e0cd6.json)

**Source references:** SRC-0852, SRC-1990  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18874"></a>
## FND-18874: Trial uci-classification-v3 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-classification-v3",
    "uciAfter": {
      "ClassificationV3": true
    }
  },
  "started": "2026-11-14T18:55:46.702Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.481,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0853",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0853** `research/refinement/results/uci-classification-v3.json` — [preserved redacted evidence](../evidence/text/a6e1e891c73202780cf511e99d53e6bb9c83b30509746bb33e95cfe27830a9e1.json)

**Source references:** SRC-0853, SRC-2030  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18875"></a>
## FND-18875: Trial uci-clear-between — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-clear-between",
    "uciAfter": {
      "ClearBetweenSearches": true
    }
  },
  "started": "2026-11-14T18:59:08.659Z",
  "actual": {
    "accuracy": {
      "white": 59.861366271972656,
      "black": 94.88895416259766
    },
    "ratings": {
      "white": 550,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 1,
        "6": 1,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 4,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "a4de6310be9a05e25119fb55c218face8707af6b0affc4d1ffea63d1cea12257",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.713,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0854",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0854** `research/refinement/results/uci-clear-between.json` — [preserved redacted evidence](../evidence/text/3572a05e5ab5694e3baadf70dbbc9f21ecfdcc0808b4f67e8777fb5660a95334.json)

**Source references:** SRC-0854, SRC-2013  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18876"></a>
## FND-18876: Trial uci-elo-sensitive — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-elo-sensitive",
    "uciAfter": {
      "EloSensitivePD": true
    }
  },
  "started": "2026-11-14T18:55:24.625Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 21.855,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0855",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0855** `research/refinement/results/uci-elo-sensitive.json` — [preserved redacted evidence](../evidence/text/fde6dfac5df5af71b4c013ec529c406354621b249a59efce403b8626a3bb7eda.json)

**Source references:** SRC-0855, SRC-1995  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18877"></a>
## FND-18877: Trial uci-forgiving-1000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-forgiving-1000",
    "uciAfter": {
      "ForgivingClassificationsElo": 1000
    }
  },
  "started": "2026-11-14T18:56:22.549Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.315,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0856",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0856** `research/refinement/results/uci-forgiving-1000.json` — [preserved redacted evidence](../evidence/text/364eb421dc8f4cc42cc5ff31638411043ea2e38d3318a03916d3996653905785.json)

**Source references:** SRC-0856, SRC-2001  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18878"></a>
## FND-18878: Trial uci-forgiving-2000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-forgiving-2000",
    "uciAfter": {
      "ForgivingClassificationsElo": 2000
    }
  },
  "started": "2026-11-14T18:56:38.994Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.142,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0857",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0857** `research/refinement/results/uci-forgiving-2000.json` — [preserved redacted evidence](../evidence/text/2e9eef34d7d0e56282c5af86705ce16ad8b26d11f9fb9d2db7256691d21aae06.json)

**Source references:** SRC-0857, SRC-1994  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18879"></a>
## FND-18879: Trial uci-forgiving-400 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-forgiving-400",
    "uciAfter": {
      "ForgivingClassificationsElo": 400
    }
  },
  "started": "2026-11-14T18:56:05.330Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.031,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0858",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0858** `research/refinement/results/uci-forgiving-400.json` — [preserved redacted evidence](../evidence/text/4f14edf879e2ec0af0779ffd5e7095ab2d7e862b10a9984a493bf3305c51b904.json)

**Source references:** SRC-0858, SRC-2003  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18880"></a>
## FND-18880: Trial uci-hard-soft-200 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-hard-soft-200",
    "uciAfter": {
      "HardSoftNodeFactor": 200
    }
  },
  "started": "2026-11-14T18:57:58.728Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.148,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0859",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0859** `research/refinement/results/uci-hard-soft-200.json` — [preserved redacted evidence](../evidence/text/8863f04415a1735f910f7a326a1358addb88e322b3ed61cfe653f6e788bc4df1.json)

**Source references:** SRC-0859, SRC-2022  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18881"></a>
## FND-18881: Trial uci-hard-soft-50 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-hard-soft-50",
    "uciAfter": {
      "HardSoftNodeFactor": 50
    }
  },
  "started": "2026-11-14T18:57:40.977Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.616,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0860",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0860** `research/refinement/results/uci-hard-soft-50.json` — [preserved redacted evidence](../evidence/text/83d0d1cbb6a6dd34afe5f8c4dd48cd631e5893d2f6628b14ad23a7da93643ea8.json)

**Source references:** SRC-0860, SRC-1982  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18882"></a>
## FND-18882: Trial uci-hash-64 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-hash-64",
    "uciAfter": {
      "Hash": 64
    }
  },
  "started": "2026-11-14T18:58:49.869Z",
  "actual": {
    "accuracy": {
      "white": 58.9421501159668,
      "black": 94.20455169677734
    },
    "ratings": {
      "white": 450,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 3,
        "7": 0,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 3,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "8ae296ec1f15e8b5db6816efc9bafc71babec25b6337d08c01f6ea99bb4d3ae4",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.649,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0861",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0861** `research/refinement/results/uci-hash-64.json` — [preserved redacted evidence](../evidence/text/fc2ca295b3b96d7f551385cca87836c8b536d4b929cde8e7de4f67ac8c687e53.json)

**Source references:** SRC-0861, SRC-1977  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18883"></a>
## FND-18883: Trial uci-multipv-2 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-multipv-2",
    "uciAfter": {
      "MultiPV": 2
    }
  },
  "started": "2026-11-14T18:59:26.524Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 2,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0d86bb169c688d4b77bf4dd7feb75c4972e4178a7d2bdcc7bb3337defc3fdf96",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.44,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0862",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0862** `research/refinement/results/uci-multipv-2.json` — [preserved redacted evidence](../evidence/text/2aad0e3f790939a63956b7a637d916c6c02be3f33af3aabfed09d5c854782a2b.json)

**Source references:** SRC-0862, SRC-1984  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18884"></a>
## FND-18884: Trial uci-node-fudging-100 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-node-fudging-100",
    "uciAfter": {
      "NodeFudging": 100
    }
  },
  "started": "2026-11-14T18:58:16.042Z",
  "actual": {
    "accuracy": {
      "white": 59.60816955566406,
      "black": 94.55702209472656
    },
    "ratings": {
      "white": 400,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 3,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "f90b603eede0643ad94719e6261eeaffdcf219fb0ab02f90be1a9853d03767d5",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 16.428,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0863",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0863** `research/refinement/results/uci-node-fudging-100.json` — [preserved redacted evidence](../evidence/text/8eb0444af960e0a26dab1ec3251bb1b2d8262feb54afc6095cc9b993de99b657.json)

**Source references:** SRC-0863, SRC-1993  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18885"></a>
## FND-18885: Trial uci-node-fudging-1000 — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-node-fudging-1000",
    "uciAfter": {
      "NodeFudging": 1000
    }
  },
  "started": "2026-11-14T18:58:32.621Z",
  "actual": {
    "accuracy": {
      "white": 60.43000411987305,
      "black": 97.84144592285156
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 5,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "0b38979352fe2d403906192a8fdfcf026517c98118e835525f9767de5b284c9a",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 17.086,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0864",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0864** `research/refinement/results/uci-node-fudging-1000.json` — [preserved redacted evidence](../evidence/text/524cdd83ddc1eac038131f74568fe803749d667728ebd1dfde4c5b474abc5852.json)

**Source references:** SRC-0864, SRC-1981  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18886"></a>
## FND-18886: Trial uci-normalize-off — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-normalize-off",
    "uciAfter": {
      "Normalize": false
    }
  },
  "started": "2026-11-14T18:56:56.262Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 4,
        "5": 3,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "50cc387d0425af86b93f185d2323ab53659191d7a89d0edfc033e34d4576af8f",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 18.054,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0865",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0865** `research/refinement/results/uci-normalize-off.json` — [preserved redacted evidence](../evidence/text/3921c32d6cc6ce94a71160a6a336f32b152ebc7727d8582a72ae4dd10e00422c.json)

**Source references:** SRC-0865, SRC-2018  
**URL references:** None independently associated  
**Related findings:** FND-18965

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18887"></a>
## FND-18887: Trial uci-soft-nodes — complete numeric result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "config": {
    "id": "uci-soft-nodes",
    "uciAfter": {
      "UseSoftNodes": true
    }
  },
  "started": "2026-11-14T18:57:14.458Z",
  "actual": {
    "accuracy": {
      "white": 60.25788497924805,
      "black": 95.0540771484375
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
        "11": 0,
        "20": 0
      },
      "black": {
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 3,
        "5": 3,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "20": 0
      }
    }
  },
  "engines": [
    11
  ],
  "numericHash": "d23d3b35b048e424d1ed46e82d33f4e3dd58519ae39582614ebfc4181c593544",
  "actualSettings": {
    "userColor": 2,
    "locale": 0,
    "gameAnalysisSpeechVersion": 3,
    "moveClassificationVersion": 2,
    "search": {
      "case": "searchSettings",
      "value": {
        "searchParameters": {
          "depthLimit": 6,
          "nodesLimit": 150000,
          "timeLimitMs": 0,
          "numLines": 2
        },
        "nullMoveSearchParameters": {
          "depthLimit": 6,
          "nodesLimit": 40000,
          "timeLimitMs": 0,
          "numLines": 1
        }
      }
    },
    "enableSkills": true
  },
  "elapsedSeconds": 26.362,
  "speech": {
    "sentences": 20,
    "hashes": 20
  },
  "warnings": [],
  "source_id": "SRC-0866",
  "outcome": "complete numeric result"
}

### Evidence

- **SRC-0866** `research/refinement/results/uci-soft-nodes.json` — [preserved redacted evidence](../evidence/text/d3c90fee459be774ac8f95bed9f24321104dd7eb2daecc653c760a4f6244acbd.json)

**Source references:** SRC-0866, SRC-1983  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18963"></a>
## FND-18963: Reference target is user-supplied, not a newly fetched cloud result

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Original20-ply reference has accuracy71.7/99.0,ratings100/1000,full tallies in target.json. Chess.com per-move labels were not provided. Newer game187158515860 was for source inspection, not a replacement numerical fixture.

### Evidence

- **SRC-0870** `research/refinement/target.json` — [preserved redacted evidence](../evidence/text/911a6715d45450b4a79ccd54b5796469ad01d9e6ccb9810bacc45a1a272cce11.json)
  Character offset 31.

```text
{
  "accuracy": {
    "white": 71.7,
    "black": 99
  },
  "ratings": {
    "white": 100,
    "black": 1000
  },
  "tallies": {
    "white": {
      "1": 2,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 4,
      "6": 1,
      "7": 0,
      "8": 2,
      "9": 1,
      "10": 0,
      "11": 0,
      "20": 0
    },
    "black": {
      "1": 2,
 
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 1697.

```text
2/review?move=0 ; 20 plies, result0-1, White Elo100/Black333, 600-second control. Reference accuracy71.7/99.0, ratings100/1000. Full targets remain in research/refinement/target.json.
- Earlier bot fixture target accuracy86.8/79.8, ratings1850/1500 supersedes older93.7/85.6,1800/1700. Earlier human fixture target76.8/70.2,1350/600. Individual per-move Chess.com labels for these references were not provided.
- Compact
```

**Source references:** SRC-0870, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18964"></a>
## FND-18964: Working baseline is59.95828628540039/95.46183013916016

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved direct native baseline has ratings300/1000. White:Book2,Good2,Inaccuracy1,Mistake4,Blunder1; Black:Book2,Great1,Best4,Excellent2,Good1. All other compact categories zero. Native output differs from cloud target.

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)
  Character offset 154.

```text
: true
  },
  "started": "2026-11-14T18:47:29.319Z",
  "actual": {
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
  
```

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18965"></a>
## FND-18965: Normalize=false is real engine tuning, not a formula

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved uci-normalize-off returns65.7431640625/99.13605499267578,ratings100/1000,improved aggregate tally distance. This changes actual Torch evaluations. Repeats reproduce its numbers; it was not globally promoted because holdouts regress.

### Evidence

- **SRC-0865** `research/refinement/results/uci-normalize-off.json` — [preserved redacted evidence](../evidence/text/3921c32d6cc6ce94a71160a6a336f32b152ebc7727d8582a72ae4dd10e00422c.json)
  Character offset 189.

```text

    }
  },
  "started": "2026-11-14T18:56:56.262Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
      
```
- **SRC-0834** `research/refinement/results/normalized-repeat-1.json` — [preserved redacted evidence](../evidence/text/5b06faa553321a13a78397901efcbfcc94d003f9401f84bbd8e6dd6864c5ea43.json)
  Character offset 215.

```text

    }
  },
  "started": "2026-11-14T19:07:49.699Z",
  "actual": {
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 1,
        "8": 4,
        "9": 1,
        "10": 0,
      
```
- **SRC-0745** `research/refinement/holdout-validation.json` — [preserved redacted evidence](../evidence/text/cbc41d78f43fd56ce256080d6cbdd1f3a5ef3949dfa413f562c108011ed4b4da.json)

**Source references:** SRC-0865, SRC-0834, SRC-0745  
**URL references:** None independently associated  
**Related findings:** FND-18886, FND-18834, FND-18835, FND-18836

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18966"></a>
## FND-18966: Normalize-off plus Hash64 matches Black tallies but not all metrics

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Saved candidate64.79644775390625/98.8089599609375,ratings100/1000; Black Book2,Great1,Best2,Excellent5 exactly matches target. White remainsBook2,Excellent2,Mistake5,Blunder1. Repeated hash64 trials reproduce result; this is not necessarily best accuracy.

### Evidence

- **SRC-0821** `research/refinement/results/normalized-Hash-64.json` — [preserved redacted evidence](../evidence/text/124de40ebd9ea3b9a089eb88c0ce34f12b282acb6d90d181c1c598a09148b16b.json)
  Character offset 208.

```text

    }
  },
  "started": "2026-11-14T19:11:19.571Z",
  "actual": {
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
   
```
- **SRC-0809** `research/refinement/results/followup-hash64-repeat.json` — [preserved redacted evidence](../evidence/text/447c9263aa911e0e3185ddde0917fed04fdd826f9884b35299e764e56b0f7dea.json)
  Character offset 236.

```text
: true
  },
  "started": "2026-11-14T19:14:38.773Z",
  "actual": {
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "ratings": {
      "white": 100,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 2,
        "6": 0,
        "7": 0,
        "8": 5,
        "9": 1,
        "10": 0,
   
```

**Source references:** SRC-0821, SRC-0809  
**URL references:** None independently associated  
**Related findings:** FND-18821, FND-18704, FND-18705, FND-18706

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18967"></a>
## FND-18967: Comparison loss ranks real outputs only

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

sweep objective accuracyAbs+2*tallyL1+ratingAbs/100 compares native output to a reference. It is NOT used by production to calculate accuracy/rating. Parameter search was bounded,not exhaustive over every setting/value, and includes repeated configurations.

### Evidence

- **SRC-0869** `research/refinement/sweep.mjs` — [preserved redacted evidence](../evidence/text/07d6432e87a9745880904485680ea6dbdbc545aca922f2c55ffc066941fbba9c.mjs)
  Character offset 5863.

```text
tringify(plan,null,2));
function metric(result){
 if(!result.actual)return null;
 let accuracyAbs=0,tallyL1=0,ratingAbs=0;
 for(const c of ['white','black']){
  accuracyAbs+=Math.abs(result.actual.accuracy[c]-target.accuracy[c]);
  ratingAbs+=Math.abs(result.actual.ratings[c]-target.ratings[c]);
  for(const[id,count]of Object.entries(target.tallies[c]))tallyL1+=Math.abs((result.actual.tallies[c][id]||0)-count);
 }
 r
```
- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)

**Source references:** SRC-0869, SRC-1629  
**URL references:** None independently associated  
**Related findings:** FND-18913, FND-18973, FND-00066, FND-00067, FND-00068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18968"></a>
## FND-18968: Holdout regression prevented one-game overfitting

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Human holdout baseline74.108/62.906,ratings1250/600; Normalize-off69.129/62.282,1000/350; plusHash6466.735/60.902,850/300. Bot holdout baseline87.730/79.541,1850/1700; Normalize-off88.440/80.232,1850/1450;Hash6490.141/82.316,1900/1450. Targets retained separately. No candidate universally matches all.

### Evidence

- **SRC-0745** `research/refinement/holdout-validation.json` — [preserved redacted evidence](../evidence/text/cbc41d78f43fd56ce256080d6cbdd1f3a5ef3949dfa413f562c108011ed4b4da.json)
  Character offset 566.

```text
 0,
          "10": 3
        }
      }
    },
    "actual": {
      "accuracy": {
        "white": 74.10804748535156,
        "black": 62.9063606262207
      },
      "ratings": {
        "white": 1250,
        "black": 600
      },
      "tallies": {
        "white": {
          "1": 4,
          "2": 0,
          "3": 1,
          "4": 12,
          "5": 10,
          "6": 7,
          "7": 3,
          "8": 4,
  
```

**Source references:** SRC-0745  
**URL references:** None independently associated  
**Related findings:** FND-18965

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18969"></a>
## FND-18969: Full local Human evaluation experiment completed21points

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

comparison-human uses GetGameReviewEvaluations79 with Fast/human at21gamepoints,AddEvaluations1,then GameReview42. Each call progress1; audit logs20PVtree searches plus auxiliary normals and zero new searches during review. Accuracy59.01492691040039/95.37910461425781,ratings400/1000. Underlying logsrating2100 are not established server settings.

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)
  Character offset 96816.

```text

    11
  ],
  "numericHash": "f26ffb5773601a7ce614334121b8a0fa9ea76ee8c8596e82110213964a15d84d",
  "searchAudit": {
    "beforeReview": [
      "request engine TORCH",
      "request cmd go nodes 40000",
      "request engine TORCH",
      "request cmd go nodes 300000 pvtrees use_split_depth_limit true use_split_width_limit true keep_equal_subtrees false show_only_optimal_mates true at_least_n_root_moves 2 split_dep
```
- **SRC-0661** `research/refinement/comparison-trial.mjs` — [preserved redacted evidence](../evidence/text/bdb6bf4b1463f5150da2084c0c861ed31474afe70bcea58bbb0bc33564073a70.mjs)

**Source references:** SRC-0799, SRC-0661  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18970"></a>
## FND-18970: Matched preload control differs from direct production baseline

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

comparison-control uses same explicit per-position preloading without human and gives60.15205383300781/96.07951354980469,ratings300/1000. Thus comparison-human versus production baseline is not a perfectly isolated one-setting experiment, although human also worsens accuracy versus this control.

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)
  Character offset 116975.

```text
aster-20260925-87ee25a"
        ]
      }
    }
  ],
  "actual": {
    "accuracy": {
      "white": 60.15205383300781,
      "black": 96.07951354980469
    },
    "ratings": {
      "white": 300,
      "black": 1000
    },
    "tallies": {
      "white": {
        "1": 2,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 2,
        "7": 2,
        "8": 3,
        "9": 1,
        "10": 0,
  
```
- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0798, SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569, FND-18589, FND-18590

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18971"></a>
## FND-18971: Only three per-move labels changed in local human comparison

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Preserved comparison table:3.Be2 Good->Inaccuracy;4.Qd3 Blunder->Mistake;7.Bd2 Inaccuracy->Mistake. Other17plies same. No Chess.com per-move label inferred from aggregate counts.

### Evidence

- **SRC-1628** `torch-human-comparison.md` — [preserved redacted evidence](../evidence/text/7634ec4631404aa657067f23169247d5fb8c0f6ea9a00050a0f0207731860af8.md)
  Character offset 3361.

```text
Book | Book |
| 1... | d5 | Book | Book |
| 2. | e4 | Book | Book |
| 2... | dxe4 | Book | Book |
| 3. | Be2 | Good | Inaccuracy |
| 3... | Nf6 | Best | Best |
| 4. | Qd3 | Blunder | Mistake |
| 4... | exd3 | Great | Great |
| 5. | cxd3 | Good | Good |
| 5... | Nc6 | Best | Best |
| 6. | Bh5 | Mistake | Mistake |
| 6... | Nxd4 | Good | Good |
| 7. | Bd2 | Inaccuracy | Mistake |
| 7... | Nc2+ | Best | Best |
| 8. | Kf
```

**Source references:** SRC-1628  
**URL references:** None independently associated  
**Related findings:** FND-00056, FND-00057, FND-00058

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18972"></a>
## FND-18972: 53/61 complete-result sweep count is a historical phase boundary

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

torch-refinement-findings reports61configurations,53complete8failed,plus6holdouts. Later offline probes and full comparisons add result files. Treat61 as the three-phase sweep snapshot, not the current total number of all experiment artifacts.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
  Character offset 350.

```text
elease is being claimed or substituted.

## What was tested
An automated, bounded search executed **61 trial configurations**, including repeat checks. 53 returned complete numeric results; 8 failed or timed out. Separate holdout validation tested the two earlier fixtures. This is not an exhaustive search of every possible parameter value.

Trials run the actual bundled CEE/Torch WASM and preserve its returned scores
```
- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 5852.

```text
rches and no new search commands during final review generation. Accuracy59.01492691040039/95.37910461425781, ratings400/1000. No Normalize/Hash tuning applied. Matched preload control60.15205383300781/96.07951354980469,ratings300/1000. Thus not a perfectly isolated comparison to the direct production baseline.
- Human experiment changed only three per-move local labels versus direct baseline:3.Be2 Good->Inaccuracy,4
```

**Source references:** SRC-1629, SRC-2049  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068, FND-18916, FND-18924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18973"></a>
## FND-18973: Parallel OOM attempts are not valid numerical trials

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Earlier concurrency3 caused child exits with null code/resource pressure. resource-failed-attempts is segregated; later sequential runs avoid that failure. A configured option in a resource-failed artifact does not establish an engine numerical behavior.

### Evidence

- **SRC-2049** `accessible-conversation/current-and-condensed-history` — [preserved redacted evidence](../evidence/text/b295bb5af6a3f9a3463e5be596f3ba2ea176d41d66915d311049a0980c38495a.txt)
  Character offset 2255.

```text
blish hidden categories are zero.
- Initial parallel WASM sweep with concurrency3 exhausted sandbox resources; children exited with null codes. Artifacts were separated as resource failures, not numerical results. Later sweeps ran sequentially.
- Repeated coach .bzp/charm-model probes returned404; their precise URLs are not preserved in the available condensed context. Do not reconstruct guessed URLs or re-probe them
```
- **SRC-0869** `research/refinement/sweep.mjs` — [preserved redacted evidence](../evidence/text/07d6432e87a9745880904485680ea6dbdbc545aca922f2c55ffc066941fbba9c.mjs)

**Source references:** SRC-2049, SRC-0869  
**URL references:** None independently associated  
**Related findings:** FND-18916, FND-18924, FND-18938, FND-18913, FND-18967

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-18974"></a>
## FND-18974: Timeouts do not establish unsupported modes

**Category:** experiments  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

Deep/Maximum/depth22 and native feature288 probes were bounded by explicit timeouts. Preserve timeouts as failed experiments; do not claim numerical outputs, no-op settings, or absent support from timeouts alone.

### Evidence

- **SRC-1629** `torch-refinement-findings.md` — [preserved redacted evidence](../evidence/text/45232eed52060fc33d35cb8b3c298f55f5dca7537730225245fbbe079b867a98.md)
- **SRC-0804** `research/refinement/results/embedded-human-pvtrees.json` — [preserved redacted evidence](../evidence/text/63fc62590e886ea5dabb178de6d643e1013d3434660ed992a5bf3506891473a7.json)
  Character offset 508.

```text
        "rating": 100
      }
    }
  },
  "started": "2026-11-14T19:05:01.514Z",
  "error": "trial timeout after 150s",
  "warnings": []
}
```

**Source references:** SRC-1629, SRC-0804  
**URL references:** None independently associated  
**Related findings:** FND-00066, FND-00067, FND-00068, FND-18615

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
