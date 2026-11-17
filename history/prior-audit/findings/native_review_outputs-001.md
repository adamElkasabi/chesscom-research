# native_review_outputs — findings 1–18

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18427"></a>
## FND-18427: Stored native review payload: research/doting-cee-baseline.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 56.760494232177734
          }
        ],
        "effectiveRating": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 95.23474884033203
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0109** `research/doting-cee-baseline.json` — [preserved redacted evidence](../evidence/text/f20a1fa1142b6cf57a0920249bd12b40a94624dcc57ac221168e9a8d120fd205.json)

**Source references:** SRC-0109  
**URL references:** None independently associated  
**Related findings:** FND-18428, FND-18429

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18448"></a>
## FND-18448: Stored native review payload: research/doting-extension-cee.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 56.760494232177734
          }
        ],
        "effectiveRating": 300,
        "gameRatingV2": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 95.23474884033203
          }
        ],
        "effectiveRating": 1000,
        "gameRatingV2": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0110** `research/doting-extension-cee.json` — [preserved redacted evidence](../evidence/text/98c92d4d47cc949131e02108c90e35c4478402be3ab50ae222e57a9a8170a293.json)

**Source references:** SRC-0110  
**URL references:** None independently associated  
**Related findings:** FND-18449, FND-18450

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18469"></a>
## FND-18469: Stored native review payload: research/doting-preeval.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.01492691040039,
      "black": 95.37910461425781
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 6
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 59.81550216674805
          }
        ],
        "effectiveRating": 400
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 94.89874267578125
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0112** `research/doting-preeval.json` — [preserved redacted evidence](../evidence/text/72fc86ef8bf714d2ae2b2202b71512886cff008a111eb05f9f479da4d1ae279a.json)

**Source references:** SRC-0112  
**URL references:** None independently associated  
**Related findings:** FND-18470, FND-18471

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18490"></a>
## FND-18490: Stored native review payload: research/doting-state12.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 56.760494232177734
          }
        ],
        "effectiveRating": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 95.23474884033203
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0116** `research/doting-state12.json` — [preserved redacted evidence](../evidence/text/38829c3ad3d10dcef5a7f97f81b557f764321cc7fdb763baf5ef3281f806af55.json)

**Source references:** SRC-0116  
**URL references:** None independently associated  
**Related findings:** FND-18491, FND-18492

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18511"></a>
## FND-18511: Stored native review payload: research/doting-v3.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 56.760494232177734
          }
        ],
        "effectiveRating": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 95.23474884033203
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0120** `research/doting-v3.json` — [preserved redacted evidence](../evidence/text/82dc06310df44cd8bafd4796ddc61f5410b555ce039f9759e57ee22301c68cd9.json)

**Source references:** SRC-0120  
**URL references:** None independently associated  
**Related findings:** FND-18512, FND-18513

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18546"></a>
## FND-18546: Stored native review payload: research/refinement/results/baseline.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.95828628540039,
      "black": 95.46183013916016
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 56.760494232177734
          }
        ],
        "effectiveRating": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 95.23474884033203
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18547

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18568"></a>
## FND-18568: Stored native review payload: research/refinement/results/comparison-control.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 60.15205383300781,
      "black": 96.07951354980469
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 2
        },
        {
          "moveClassification": 7,
          "tally": 2
        },
        {
          "moveClassification": 8,
          "tally": 3
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 3
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 57.02191925048828
          }
        ],
        "effectiveRating": 300
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 96.15827941894531
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18569

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18590"></a>
## FND-18590: Stored native review payload: research/refinement/results/comparison-human.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "You had a nice tactical find in this game. Let's review!",
    "accuracy": {
      "white": 59.01492691040039,
      "black": 95.37910461425781
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 6
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6,
          "tally": 1
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 6,
            "phase": 1,
            "accuracy": 59.81550216674805
          }
        ],
        "effectiveRating": 400
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 94.89874267578125
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "You won with a nice tactic! Let's look at it together."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18591

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18617"></a>
## FND-18617: Stored native review payload: research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 65.15036010742188,
      "black": 99.21577453613281
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 1
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 6
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 3
        },
        {
          "moveClassification": 5,
          "tally": 4
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 38.936546325683594
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 99.21786499023438
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18618

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18639"></a>
## FND-18639: Stored native review payload: research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 65.3160629272461,
      "black": 99.38276672363281
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 3
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 38.60036087036133
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 99.3322525024414
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18640

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18661"></a>
## FND-18661: Stored native review payload: research/refinement/results/followup-hash32-softfalse.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 66.01242065429688,
      "black": 99.10324096679688
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 1
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 3
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 41.81056213378906
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 99.33668518066406
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0807** `research/refinement/results/followup-hash32-softfalse.json` — [preserved redacted evidence](../evidence/text/e3642c41e53040ebeff4327a13b709591bcb9891d7ca970398a8ade32c9366f3.json)

**Source references:** SRC-0807  
**URL references:** None independently associated  
**Related findings:** FND-18660, FND-18662

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18683"></a>
## FND-18683: Stored native review payload: research/refinement/results/followup-hash32-softtrue.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 65.15916442871094,
      "black": 98.37834930419922
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 3
        },
        {
          "moveClassification": 5,
          "tally": 4
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 38.38899612426758
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 98.24657440185547
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0808** `research/refinement/results/followup-hash32-softtrue.json` — [preserved redacted evidence](../evidence/text/9e0a126148a8592961161a6a38e743fcbcf3e7c9fef2d3095cade8211ffdfe60.json)

**Source references:** SRC-0808  
**URL references:** None independently associated  
**Related findings:** FND-18682, FND-18684

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18705"></a>
## FND-18705: Stored native review payload: research/refinement/results/followup-hash64-repeat.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 2
        },
        {
          "moveClassification": 5,
          "tally": 5
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 39.17156219482422
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 98.97355651855469
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0809** `research/refinement/results/followup-hash64-repeat.json` — [preserved redacted evidence](../evidence/text/447c9263aa911e0e3185ddde0917fed04fdd826f9884b35299e764e56b0f7dea.json)

**Source references:** SRC-0809  
**URL references:** None independently associated  
**Related findings:** FND-18704, FND-18706

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18727"></a>
## FND-18727: Stored native review payload: research/refinement/results/followup-hash64-softfalse.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 64.79644775390625,
      "black": 98.8089599609375
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 2
        },
        {
          "moveClassification": 5,
          "tally": 5
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 39.17156219482422
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 98.97355651855469
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0810** `research/refinement/results/followup-hash64-softfalse.json` — [preserved redacted evidence](../evidence/text/8c9fb429b5e804dec6f04a316102e62a9b8629962a865562b3f1d917c2b16308.json)

**Source references:** SRC-0810  
**URL references:** None independently associated  
**Related findings:** FND-18726, FND-18728

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18749"></a>
## FND-18749: Stored native review payload: research/refinement/results/followup-hash64-softtrue.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 65.71549987792969,
      "black": 99.19789123535156
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8,
          "tally": 5
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 3
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 39.500370025634766
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 99.16720581054688
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0811** `research/refinement/results/followup-hash64-softtrue.json` — [preserved redacted evidence](../evidence/text/ec0ecf507b8cf076f00a89104e7fd749c47cff406f61f06c61185435d35138d3.json)

**Source references:** SRC-0811  
**URL references:** None independently associated  
**Related findings:** FND-18748, FND-18750

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18771"></a>
## FND-18771: Stored native review payload: research/refinement/results/followup-soft-factor200.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 66.39828491210938,
      "black": 98.71414947509766
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 3
        },
        {
          "moveClassification": 5,
          "tally": 4
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 41.16399002075195
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 98.7276611328125
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0812** `research/refinement/results/followup-soft-factor200.json` — [preserved redacted evidence](../evidence/text/5dedac464481da11ade84d756924369b0139baf180932d907b719847d96dc1d6.json)

**Source references:** SRC-0812  
**URL references:** None independently associated  
**Related findings:** FND-18770, FND-18772

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18793"></a>
## FND-18793: Stored native review payload: research/refinement/results/followup-soft-factor50.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 66.39828491210938,
      "black": 98.71414947509766
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 3
        },
        {
          "moveClassification": 5,
          "tally": 4
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 41.16399002075195
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 98.7276611328125
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0813** `research/refinement/results/followup-soft-factor50.json` — [preserved redacted evidence](../evidence/text/567a3a363ab87a4e3bda11fb4f3110062ca5375dbfe6019b7f15ae5eaa113186.json)

**Source references:** SRC-0813  
**URL references:** None independently associated  
**Related findings:** FND-18792, FND-18794

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.

<a id="FND-18835"></a>
## FND-18835: Stored native review payload: research/refinement/results/normalized-repeat-1.json

**Category:** native_review_outputs  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "highlights": {
    "gameSummary": "Good job grabbing a big advantage in the opening and converting the win.",
    "accuracy": {
      "white": 65.7431640625,
      "black": 99.13605499267578
    },
    "classificationTallies": {
      "white": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3
        },
        {
          "moveClassification": 4
        },
        {
          "moveClassification": 5,
          "tally": 2
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7,
          "tally": 1
        },
        {
          "moveClassification": 8,
          "tally": 4
        },
        {
          "moveClassification": 9,
          "tally": 1
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ],
      "black": [
        {
          "moveClassification": 1,
          "tally": 2
        },
        {
          "moveClassification": 2
        },
        {
          "moveClassification": 3,
          "tally": 1
        },
        {
          "moveClassification": 4,
          "tally": 4
        },
        {
          "moveClassification": 5,
          "tally": 3
        },
        {
          "moveClassification": 6
        },
        {
          "moveClassification": 7
        },
        {
          "moveClassification": 8
        },
        {
          "moveClassification": 9
        },
        {
          "moveClassification": 10
        },
        {
          "moveClassification": 11
        },
        {
          "moveClassification": 20
        }
      ]
    },
    "reportCard": {
      "white": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 7,
            "phase": 1,
            "accuracy": 40.499080657958984
          }
        ],
        "effectiveRating": 100
      },
      "black": {
        "reportsByPhase": [
          {
            "accuracyGlyph": 3,
            "phase": 1,
            "accuracy": 99.1512451171875
          }
        ],
        "effectiveRating": 1000
      },
      "speech": "You really outplayed your opponent in that one."
    },
    "takeaways": {},
    "gameSummaryCoachEmotion": 3,
    "gameSummaryPlay": "That game was yours from the opening! Let's check out the highlights."
  },
  "result": {
    "result": 2,
    "resultType": 1
  },
  "opening": {
    "openingName": "Queen's Pawn Opening: Blackmar Gambit",
    "tcnMoves": "lBZJmCJC",
    "ecoCode": "D00",
    "url": "Queens-Pawn-Opening-Blackmar-Gambit-2...dxe4"
  },
  "metadata": {
    "ceeVersion": {
      "major": 1,
      "minor": 211,
      "patch": 5
    },
    "annotatedPgn": "\n1. d4 d5 2. e4 dxe4 3. Be2 Nf6 4. Qd3 exd3 5. cxd3 Nc6 6. Bh5 Nxd4 7. Bd2 Nc2+ 8. Kf1 Nxa1 9. Bc1 Qxd3+ 10. Ke1 Nc2# 0-1"
  }
}

### Evidence

- **SRC-0834** `research/refinement/results/normalized-repeat-1.json` — [preserved redacted evidence](../evidence/text/5b06faa553321a13a78397901efcbfcc94d003f9401f84bbd8e6dd6864c5ea43.json)

**Source references:** SRC-0834  
**URL references:** None independently associated  
**Related findings:** FND-18834, FND-18836

**Additional notes:** Per-move records are separately extracted. These are local outputs unless source explicitly says otherwise, not cloud targets.
