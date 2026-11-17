# native_review_moves — findings 101–200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-18547"></a>
## FND-18547: Ply 1 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 12,
      "to": 28
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 21
        }
      },
      "depth": 28,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Bringing out this pawn often leads to a closed, strategic game."
            }
          ],
          "audioUrlHash": "55f48c7c2124eef5ebb1629be3b247086937a9b4c2f36909c85d250810376d7b"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 28
          },
          {
            "from": 52,
            "to": 36
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 28
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 28,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, White will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 37
                      }
                    ],
                    "squares": [
                      37
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d575221e5c1c6344f85df924f675e080a38c1bdd864fd14fc97306c5f5d3f2bc"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 28
              },
              {
                "from": 52,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 37
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 37,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 27,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "7cbae0403100fe7c50106851a88b64f8affe69e6b76dfd4533534d27121c05f8"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 52,
                "to": 36
              },
              {
                "from": 11,
                "to": 27
              },
              {
                "from": 53,
                "to": 45
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 52,
    "to": 36
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18548"></a>
## FND-18548: Ply 2 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 52,
      "to": 36
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 21
        }
      },
      "depth": 27,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Keep it up. Many good openings come to mind after this first move."
            }
          ],
          "audioUrlHash": "252bd46cc20650c079ea09bad0e859fbeabb714f25959e30f08d8e0fd6a29d4b"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 52,
            "to": 36
          },
          {
            "from": 11,
            "to": 27
          },
          {
            "from": 53,
            "to": 45
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          },
          {
            "from": 27,
            "to": 36
          },
          {
            "from": 45,
            "to": 36
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 27,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, Black will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d1975a35dca46408c868cb9256b3b2483b1fdd29eef1db115f1fe036eab9008b"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 52,
                "to": 36
              },
              {
                "from": 11,
                "to": 27
              },
              {
                "from": 53,
                "to": 45
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 27
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 26,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center, fighting for space."
                }
              ],
              "audioUrlHash": "2334c5d8159a37807369dcc9d6e1f9e190b44c9385e5fa4345b55c9cc6ce36b4"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 27
              },
              {
                "from": 53,
                "to": 45
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 53,
          "to": 45
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 25,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The bishop will be ready to be "
                },
                {
                  "fragment": "developed",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 62,
                        "to": 26
                      }
                    ]
                  }
                },
                {
                  "fragment": " to an active square."
                }
              ],
              "audioUrlHash": "549d67328393bee3cafbf0e11bf371b7e53494d031b9862583fb535ea7f708f1"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 53,
                "to": 45
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 62,
                "to": 26
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 24,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 27,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will maintain the balance in material with a good "
                },
                {
                  "fragment": "trade",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 45,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "27a34e0c139965b67b45f9dab609b1bc8e903d0834768a8b68b99084e5a17349"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 27,
                "to": 36
              },
              {
                "from": 45,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 45,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 45,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 21
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Recapturing with the pawn will keep the center healthy and stable."
                }
              ],
              "audioUrlHash": "7d08ba03d40e2e6262c762f838d756850db0bbb514d4fd66836ead3b983d9227"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 27
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 11,
    "to": 27
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18549"></a>
## FND-18549: Ply 3 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -54
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The Blackmar-Diemer Gambit takes full control of the center with e4, immediately attacks the d5 pawn, and allows the queen and light-squared bishop to develop."
            }
          ],
          "audioUrlHash": "e09520a6547ca211e2a317e6f4d57cbb5ddd2f1156431976e3b07004b80e6dc7"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 29
          },
          {
            "from": 36,
            "to": 29
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -54
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center with a pawn, trying to gain space."
                }
              ],
              "audioUrlHash": "e72817438cbf1a7ce809d88fb462c1b0470eae473112f737a7919d7af52d3f19"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 29
              },
              {
                "from": 36,
                "to": 29
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -54
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 36,
                "to": 29
              },
              {
                "from": 7,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 36,
    "to": 29
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18550"></a>
## FND-18550: Ply 4 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 36,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -54
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That pawn was yours for the taking!"
            }
          ],
          "audioUrlHash": "2be85fe239251098e1f912098724e134e98842bfb8acd72741b6de99cf458db4"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 36,
            "to": 29
          },
          {
            "from": 7,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -54
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 36,
                "to": 29
              },
              {
                "from": 7,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -54
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 13,
                        "to": 28
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 13,
                "to": 28
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 7,
    "to": 13
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18551"></a>
## FND-18551: Ply 5 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 6,
      "to": 13
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -110
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their bishop moves into the game."
            }
          ],
          "audioUrlHash": "dc608215bba6cb2c48006d545b62d72d023107ba2af028612d7a5863c1b5a4bc"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 7,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -54
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They bring out their knight, increasing their control over the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 13,
                    "to": 28
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "32f67324b4a97164f6bac80c75970a2aee4a459fd3c97b89116ba6e2539cb3a4"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 13,
            "to": 28
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 13
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -110
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the bishop off its starting square."
                }
              ],
              "audioUrlHash": "fab60bbbc16cf570514cf6af1fb5bf2324eff4d7bb8b44f4e87393b83799f8dd"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18552"></a>
## FND-18552: Ply 6 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 63,
      "to": 46
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -110
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Developing the knight and increasing influence in the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 29
                  },
                  {
                    "from": 46,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "1d2decea8d82126236d0be0330d78436af2c322f88652927313b79ccd914987b"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 46,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -110
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18553"></a>
## FND-18553: Ply 7 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 4,
      "to": 20
    },
    "moveClassification": 9,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -434
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The queen is left hanging, letting you grab it immediately."
            }
          ],
          "audioUrlHash": "0428b78ba437c68e5ece717d9db78f9a2394bb3e12aa555f6cb17187606e75a8"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 4,
            "to": 20
          },
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -110
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their knight comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "482cede704c7932299734c583a24c2083f7583a6a6437e077fa4e4944179855c"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 5,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 4,
          "to": 20
        },
        "moveClassification": 9,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -434
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will leave the queen hanging and available to be taken immediately."
                }
              ],
              "audioUrlHash": "b654f0e78d7fc7f44c52aca4028f4909c4a3f12cc6cd131826da35c1894c9c28"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 4,
                "to": 20
              },
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -434
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a free queen."
                }
              ],
              "audioUrlHash": "ff0ecddae91942343a732190723fa8045c2f78cc8636ec5534995c3b2c525d4a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -434
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 29,
    "to": 20
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18554"></a>
## FND-18554: Ply 8 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 29,
      "to": 20
    },
    "moveClassification": 3,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -434
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You won material by capturing a queen."
            }
          ],
          "audioUrlHash": "3db44183e4517a56b9a1ca24f99ee4ad7748f4925893bb08be05e040ed4675d5"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 2,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -434
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Capturing that queen will win material."
                }
              ],
              "audioUrlHash": "d18f7087b665c16841e8ea1deea30f54fde30c89d0422bedbe9660e6a55a80a9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -434
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 13,
    "to": 20
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18555"></a>
## FND-18555: Ply 9 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 20
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -495
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Recaptures."
            }
          ],
          "audioUrlHash": "5b6fb2d6e06b1533ccb50cac54d3217cb2c8a8c786b140b85f25c92593f53468"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 13,
      "to": 20
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -434
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A clear recapture."
            }
          ],
          "audioUrlHash": "887801f5c34b862cbbb942e9fb8e0d1452d1b168fea3d2a22ff136b513101d51"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 20
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -495
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will recapture."
                }
              ],
              "audioUrlHash": "d5bbdeae05f35b76991dd4c45ba07aa37be520cc5e61563ed05f5f719dd2966d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 58,
    "to": 43
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18556"></a>
## FND-18556: Ply 10 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 58,
      "to": 43
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -495
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are bringing your knight into play, eyeing the "
            },
            {
              "fragment": "central squares",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 43,
                    "to": 28
                  },
                  {
                    "from": 43,
                    "to": 37
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "431312a35dba0b14ca986c486512b8b9f4224ef115fb32dde112bd60e2bddf43"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 58,
            "to": 43
          },
          {
            "from": 7,
            "to": 22
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 43,
            "to": 28
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 43,
            "to": 37
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 58,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -495
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 43,
                        "to": 28
                      },
                      {
                        "from": 43,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "0a4311db259d6632c24a0de8ff3ea1c0abc150432204af13f565f9320e675b0c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 58,
                "to": 43
              },
              {
                "from": 7,
                "to": 22
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 43,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 43,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -495
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will prepare to tuck the king safely on the kingside."
                }
              ],
              "audioUrlHash": "8df0cb4f3306124b320c4d2910c4dff0e6e64dff6a000493e98620ca0ae84cc2"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 5,
                "to": 7
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 7,
    "to": 22
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18557"></a>
## FND-18557: Ply 11 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 13,
      "to": 40
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -606
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That bishop is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "bf506586444905da2bf7029b61813ad44990e299e12f5459945c21b5ca4729f9"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 40
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 7,
            "to": 22
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 7,
      "to": 22
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -495
        }
      },
      "depth": 14,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Kingside castling becomes available for your opponent here."
            }
          ],
          "audioUrlHash": "b41e00cd7c10337e6b05309c023b12d9f69742270109ff5fd6db294c6baaf709"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 5,
            "to": 7
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 40
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -606
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the bishop on an unsafe square."
                }
              ],
              "audioUrlHash": "846398c77e8f33fbb1ba864355138f3be7185a9d8768140692d72742a9015d89"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 40
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 7,
                "to": 22
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -606
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free bishop."
                }
              ],
              "audioUrlHash": "805e09f2431790f5002fbb2cf3c0317fb3c34d6d4e2ca06dd52df5bb9fd64ba6"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 3,
                "to": 21
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18558"></a>
## FND-18558: Ply 12 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 43,
      "to": 28
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -566
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You won a pawn for free."
            }
          ],
          "audioUrlHash": "f009c951bb1068d542596c5291de11b08a7c10086ee2e4e3e38827ffde915728"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 28
          },
          {
            "from": 40,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -606
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You won a bishop for free."
            }
          ],
          "audioUrlHash": "ca1beccda0945b5019413372af563dcd2c35130c04c61151cdc56e594480dee0"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 3,
            "to": 21
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 28
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -566
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 28
              },
              {
                "from": 40,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -566
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 4
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18559"></a>
## FND-18559: Ply 13 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 3,
      "to": 12
    },
    "moveClassification": 7,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -676
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are now able to win material through a "
            },
            {
              "fragment": "discovered",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 28,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " attack."
            }
          ],
          "audioUrlHash": "8b07f868754740f9c370a6f784c3540e4f763e48f9b1876e940bfc77117b4c7d"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 3,
            "to": 12
          },
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 13
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 59,
            "to": 38
          },
          {
            "from": 13,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 20,
            "to": 28
          }
        ],
        "showText": "Show Discovery",
        "hideText": "Hide Discovery"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 28,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -566
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move puts their bishop on a safer square."
            }
          ],
          "audioUrlHash": "b0a89f220a0dc16c01cadb1b172096df4b0eac66629de4af8348c16561b0a669"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 7,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -676
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You are now able to win material through a "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " attack."
                }
              ],
              "audioUrlHash": "8b07f868754740f9c370a6f784c3540e4f763e48f9b1876e940bfc77117b4c7d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 3,
                "to": 12
              },
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -676
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 20
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": " attack will be powerful here , Black will win material with it."
                }
              ],
              "audioUrlHash": "256d0749820e5622cacbb32d5e519e582b2db4a202a2e0402b97e60706644156"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 13
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lose a rook."
                }
              ],
              "audioUrlHash": "ec963fed2af387afd5fc47e1ce11f8f28d5a66b0812f0694acb70ccf78b41f3c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 38
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A new attacker will join the pressure on the pawn."
                }
              ],
              "audioUrlHash": "310647695a1bc02033ca07d908b2bcf562a1f8a2ea2a52ae8fd0ba4c5da83ef3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 38,
                "to": 20
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 28
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the pawn from an immediate threat."
                }
              ],
              "audioUrlHash": "fe01531c67e1371281fffcd682f963b97198b16f10beffb129991a01662eb19f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 28
              },
              {
                "from": 38,
                "to": 31
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 28,
    "to": 11
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18560"></a>
## FND-18560: Ply 14 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 28,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -676
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A "
            },
            {
              "fragment": "discovered",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 60,
                    "to": 20
                  },
                  {
                    "from": 11,
                    "to": 5
                  }
                ]
              }
            },
            {
              "fragment": " attack is always powerful. This time, you will win material with it."
            }
          ],
          "audioUrlHash": "ba15510279ca9c05ba0c318be42c72242b1099faa27166bec34dbd4f43c6ecc4"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 13
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 59,
            "to": 38
          },
          {
            "from": 13,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 20,
            "to": 28
          }
        ],
        "showText": "Show Discovery",
        "hideText": "Hide Discovery"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 60,
            "to": 20
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 11,
            "to": 5
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -676
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 20
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": " attack will be powerful here , Black will win material with it."
                }
              ],
              "audioUrlHash": "256d0749820e5622cacbb32d5e519e582b2db4a202a2e0402b97e60706644156"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 13
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a rook."
                }
              ],
              "audioUrlHash": "2b5390c317b3abedebbe4a797221eba46683dccc64564dfaababcc3449ebb70e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 38
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The threat on the pawn will become more serious with this move."
                }
              ],
              "audioUrlHash": "ca25911ff3711080f3387b15efa6f0eec6052cc9a87ec87d66a1bb8e461fbcc5"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 38,
                "to": 20
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 28
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -687
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the pawn out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "4176025cc2bffebe087cdd2c07ed3106b13569f090eeaf0d718bb6de66b0bdb3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 28
              },
              {
                "from": 38,
                "to": 31
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 5,
    "to": 4
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18561"></a>
## FND-18561: Ply 15 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 5,
      "to": 6
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -701
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve made a mistake, and their rook is now lost."
            }
          ],
          "audioUrlHash": "c23daed586c105a4ad11a2852f26c54c2b3baa0f6283781fa2b52c9597d69a04"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 59,
            "to": 24
          },
          {
            "from": 22,
            "to": 5
          },
          {
            "from": 20,
            "to": 60
          },
          {
            "from": 19,
            "to": 36
          },
          {
            "from": 24,
            "to": 31
          },
          {
            "from": 36,
            "to": 51
          },
          {
            "from": 60,
            "to": 51
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 5,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -676
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their king steps away from the check by your knight."
            }
          ],
          "audioUrlHash": "1f53ff01efb92ee6eac398c8258a05e16b37c233215d41e5c4d8574d3014afa6"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 4,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lose a rook."
                }
              ],
              "audioUrlHash": "ec963fed2af387afd5fc47e1ce11f8f28d5a66b0812f0694acb70ccf78b41f3c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 59,
                "to": 24
              },
              {
                "from": 22,
                "to": 5
              },
              {
                "from": 20,
                "to": 60
              },
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 11,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will have only this move available."
                }
              ],
              "audioUrlHash": "0de6e3de99cf4115774b92836194851e54e6746926696581843927b8a38e776b"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 59,
                "to": 24
              },
              {
                "from": 22,
                "to": 5
              },
              {
                "from": 20,
                "to": 60
              },
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the knight out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "66dfca12a583e600c2ac880a9daed549466cd261b473a145ad13bd8b4c21ca40"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 24
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will prepare to tuck the king safely on the queenside."
                }
              ],
              "audioUrlHash": "e8a5a5657e5759e422c40b3c792c08577e40196c3afdee6b56ccb4fcfa6acf86"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 59,
                "to": 24
              },
              {
                "from": 22,
                "to": 5
              },
              {
                "from": 20,
                "to": 60
              },
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 61,
                "to": 59
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 22,
          "to": 5
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 10,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will win a tempo by "
                },
                {
                  "fragment": "threatening",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 5,
                        "to": 20
                      }
                    ],
                    "squares": [
                      20
                    ]
                  }
                },
                {
                  "fragment": " a queen and forcing it to move away."
                }
              ],
              "audioUrlHash": "48f7055681f8b33ff5185a5b371f8d117a7a063353e4255f5662b83244848d2c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 22,
                "to": 5
              },
              {
                "from": 20,
                "to": 60
              },
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 5,
                "to": 20
              },
              "color": 1
            }
          ],
          "squares": [
            {
              "square": 20,
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 60
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 9,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the queen on a safer square."
                }
              ],
              "audioUrlHash": "46723a9a66178e7635d84c07ceb0b11a0bebaf1f4403951905c63c4c7c9e6eec"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 60
              },
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 19,
          "to": 36
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 8,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This "
                },
                {
                  "fragment": "blocks",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 12
                      }
                    ],
                    "squares": [
                      36
                    ]
                  }
                },
                {
                  "fragment": " the attack on a bishop that could have been captured."
                }
              ],
              "audioUrlHash": "bebf658329a40f4f5b426c0dcd3f5a28c49703b8f606a4e28fa10789673024b9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 19,
                "to": 36
              },
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 12
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 36,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 24,
          "to": 31
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 7,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 24,
                "to": 31
              },
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 51
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 6,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 36,
                "to": 51
              },
              {
                "from": 60,
                "to": 51
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 51
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -701
            }
          },
          "depth": 5,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will simply recapture."
                }
              ],
              "audioUrlHash": "e7f6273fcdb5224c55b1a4b5ccae8e24cf32860d68c60f8c6e82a1a3c27b2082"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18562"></a>
## FND-18562: Ply 16 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 1
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -665
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That rook was yours for the taking!"
            }
          ],
          "audioUrlHash": "d7319aa316a79b21784e9a06cb95381bd1b3d7911f422a6ce4724df45023385b"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -701
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {},
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -665
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -665
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18563"></a>
## FND-18563: Ply 17 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 12,
      "to": 3
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -730
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move gives you the opportunity to win their bishop."
            }
          ],
          "audioUrlHash": "2f0febaa70593a64f4f58b97081bec86380e4f75cd19e304da6afc017ce7d712"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 3
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -665
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move the bishop to safety."
            }
          ],
          "audioUrlHash": "9c72c165fbd2018b4d7756ed288560df03b0a67fff1d94bd095c0d04745f58d5"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 3
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -730
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a bishop."
                }
              ],
              "audioUrlHash": "aef0cf0a74addc347ccfea09324e560c05b6452ab77e50a5e43446f550b820fa"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 3
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -730
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18564"></a>
## FND-18564: Ply 18 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 60,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -708
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Very good choice!"
            }
          ],
          "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 11,
            "to": 3
          },
          {
            "from": 13,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -730
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Very good choice!"
                }
              ],
              "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the queen out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "316739ec8456391318f79b9f85fee9d1eaa747fd0792f5050b9eca7a30e173ad"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the knight from an immediate threat."
                }
              ],
              "audioUrlHash": "20c251000ee4126f17d0416cfd3ef4eb9a59bdef948dd8d6dd8b9849620f7694"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 3
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 3,
                        "to": 6
                      }
                    ],
                    "squares": [
                      4
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 3,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 4,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18565"></a>
## FND-18565: Ply 19 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 5
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 1
        }
      },
      "depth": 97,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You get a chance to "
            },
            {
              "fragment": "checkmate",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 1,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " the king."
            }
          ],
          "audioUrlHash": "0c7cc39c8b71567bbb43dc81cf457bb654862b90056614472581230bd65c37ee"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 6,
            "to": 5
          },
          {
            "from": 1,
            "to": 11
          }
        ],
        "showText": "Show Checkmate",
        "hideText": "Hide Checkmate"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 1,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -708
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They "
            },
            {
              "fragment": "stopped",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 20,
                    "to": 6
                  }
                ],
                "squares": [
                  13
                ]
              }
            },
            {
              "fragment": " the check by interposing a piece between your queen and their king."
            }
          ],
          "audioUrlHash": "de2ba961ff92179678cbec734f026eeca914f7590f8956fd86ac891a6bb62582"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 11,
            "to": 3
          },
          {
            "from": 13,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 20,
            "to": 6
          },
          "color": 4
        }
      ],
      "squares": [
        {
          "square": 13,
          "color": 1
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 5
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 1
            }
          },
          "depth": 97,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You get a chance to "
                },
                {
                  "fragment": "checkmate",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 1,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " the king."
                }
              ],
              "audioUrlHash": "0c7cc39c8b71567bbb43dc81cf457bb654862b90056614472581230bd65c37ee"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 5
              },
              {
                "from": 1,
                "to": 11
              }
            ],
            "showText": "Show Checkmate",
            "hideText": "Hide Checkmate"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 1,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 1,
    "to": 11
  }
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18566"></a>
## FND-18566: Ply 20 in research/refinement/results/baseline.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 1,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 0
        }
      },
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Checkmate is always the best move!"
            }
          ],
          "audioUrlHash": "8237f9380206067826472c522ba41a27ceb3ddba6ec747609bf2d36c18f57180"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ]
}

### Evidence

- **SRC-0797** `research/refinement/results/baseline.json` — [preserved redacted evidence](../evidence/text/706b1b98d7428a1f8fb8c67cd3d8bfb063a1618ab77876db48c697d6c4e48d46.json)

**Source references:** SRC-0797  
**URL references:** None independently associated  
**Related findings:** FND-18545, FND-18546, FND-18547

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18569"></a>
## FND-18569: Ply 1 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 12,
      "to": 28
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 24
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A classic way to start the game."
            }
          ],
          "audioUrlHash": "e34164e86107e448227e66fe068734f6f1a854a953803e1f16a567378b8b8b47"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 28
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 24
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 37
                      }
                    ],
                    "squares": [
                      37
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "94b499feaeeac9ad99431f43e54b0dcf036cce4a3cb8d2e90f7fbd15f2bc2998"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 37
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 37,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18570"></a>
## FND-18570: Ply 2 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 52,
      "to": 36
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 31
        }
      },
      "depth": 25,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A standard response that battles for the center and opens up your light-squared bishop."
            }
          ],
          "audioUrlHash": "1227bfd4f44f8ce7462f2bd5b9d477db79ebef073829da82e48fd59e5b7a9302"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 31
            }
          },
          "depth": 25,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, Black will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d1975a35dca46408c868cb9256b3b2483b1fdd29eef1db115f1fe036eab9008b"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 7,
    "to": 22
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18571"></a>
## FND-18571: Ply 3 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -47
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The Blackmar-Diemer Gambit takes full control of the center with e4, immediately attacks the d5 pawn, and allows the queen and light-squared bishop to develop."
            }
          ],
          "audioUrlHash": "e09520a6547ca211e2a317e6f4d57cbb5ddd2f1156431976e3b07004b80e6dc7"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 29
          },
          {
            "from": 36,
            "to": 29
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -47
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center with a pawn, trying to gain space."
                }
              ],
              "audioUrlHash": "e72817438cbf1a7ce809d88fb462c1b0470eae473112f737a7919d7af52d3f19"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 29
              },
              {
                "from": 36,
                "to": 29
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -47
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 36,
    "to": 29
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18572"></a>
## FND-18572: Ply 4 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 36,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -47
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That pawn was yours for the taking!"
            }
          ],
          "audioUrlHash": "2be85fe239251098e1f912098724e134e98842bfb8acd72741b6de99cf458db4"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -47
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18573"></a>
## FND-18573: Ply 5 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 6,
      "to": 13
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -101
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Your opponent develops their bishop off its starting square."
            }
          ],
          "audioUrlHash": "2faa3e051e338a30ca3e4da41433ce9c6ec662231582ce92f69bc3494d0d0284"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -47
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nc3 develops the knight toward the center, attacks the e4 pawn and controls the b5 square."
            }
          ],
          "audioUrlHash": "64cb374b932595c3d95756f8030723b4c68bda1b4bba36f1f740ad79ffd9a62c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 13
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -101
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The bishop will come out and join the battle."
                }
              ],
              "audioUrlHash": "2834bdfd4bc83c67eba432766e40c8a2df26e2ba2533bf466dbcb7982868a495"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18574"></a>
## FND-18574: Ply 6 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 63,
      "to": 46
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -101
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Develops the knight and supports the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 29
                  },
                  {
                    "from": 46,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "cd4e8d35fa4992ad42186121edaaa8dcf3d5fa36cbb4833c291540c7427e1621"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 46,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -101
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "0a4311db259d6632c24a0de8ff3ea1c0abc150432204af13f565f9320e675b0c"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18575"></a>
## FND-18575: Ply 7 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 4,
      "to": 20
    },
    "moveClassification": 9,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -429
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The queen is left hanging, letting you grab it immediately."
            }
          ],
          "audioUrlHash": "0428b78ba437c68e5ece717d9db78f9a2394bb3e12aa555f6cb17187606e75a8"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 4,
            "to": 20
          },
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -101
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their knight comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "482cede704c7932299734c583a24c2083f7583a6a6437e077fa4e4944179855c"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 5,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 4,
          "to": 20
        },
        "moveClassification": 9,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -429
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will leave the queen hanging and available to be taken immediately."
                }
              ],
              "audioUrlHash": "b654f0e78d7fc7f44c52aca4028f4909c4a3f12cc6cd131826da35c1894c9c28"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 4,
                "to": 20
              },
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -429
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Capturing that queen will win material."
                }
              ],
              "audioUrlHash": "d18f7087b665c16841e8ea1deea30f54fde30c89d0422bedbe9660e6a55a80a9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -429
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 29,
    "to": 20
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18576"></a>
## FND-18576: Ply 8 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 29,
      "to": 20
    },
    "moveClassification": 3,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -429
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nice vision spotting and capturing that vulnerable queen."
            }
          ],
          "audioUrlHash": "1eb6390c5d22c81649f4c6b27b2294f4619d395211946891cfa4a055a93df204"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 2,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -429
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a free queen."
                }
              ],
              "audioUrlHash": "ff0ecddae91942343a732190723fa8045c2f78cc8636ec5534995c3b2c525d4a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -429
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 13,
    "to": 20
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18577"></a>
## FND-18577: Ply 9 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 20
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -490
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Takes back."
            }
          ],
          "audioUrlHash": "75740bc8dc07b75aafac22b7112e0ba6a1c23b141c96306524a1f17bfcb03ef3"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 13,
      "to": 20
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -429
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A straightforward recapture."
            }
          ],
          "audioUrlHash": "d34064bc9212b57ab3b3b7a517277b4546f19a903d97c439bb9f0ab4740673eb"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 20
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -490
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will recapture."
                }
              ],
              "audioUrlHash": "d5bbdeae05f35b76991dd4c45ba07aa37be520cc5e61563ed05f5f719dd2966d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 58,
    "to": 43
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18578"></a>
## FND-18578: Ply 10 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 58,
      "to": 43
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -490
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are bringing your knight into play, eyeing the "
            },
            {
              "fragment": "central squares",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 43,
                    "to": 28
                  },
                  {
                    "from": 43,
                    "to": 37
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "431312a35dba0b14ca986c486512b8b9f4224ef115fb32dde112bd60e2bddf43"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 58,
            "to": 43
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 43,
            "to": 28
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 43,
            "to": 37
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 58,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -490
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 43,
                        "to": 28
                      },
                      {
                        "from": 43,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 58,
                "to": 43
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 43,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 43,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -490
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18579"></a>
## FND-18579: Ply 11 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 40
    },
    "moveClassification": 7,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -592
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve moved the same piece again, which is less efficient for opening play."
            }
          ],
          "audioUrlHash": "63a83a95372c5afed6a56bc37fca530a629cd66cfd1f213dcb43fc80740d6429"
        },
        {
          "sentenceFragments": [
            {
              "fragment": "Their better move was to develop a knight and attack the center."
            }
          ],
          "audioUrlHash": "3e7642def3cb35f422a8116ac7e47160ff828eb403707437f362482b2ab75857"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 40
          },
          {
            "from": 43,
            "to": 26
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -490
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They bring out their knight, increasing their control over the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 19,
                    "to": 29
                  },
                  {
                    "from": 19,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "32f67324b4a97164f6bac80c75970a2aee4a459fd3c97b89116ba6e2539cb3a4"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 40
        },
        "moveClassification": 7,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -592
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Playing the same piece again will slow opening progress."
                }
              ],
              "audioUrlHash": "1a55db420b2f26167f026f0b7dbcb24a49e347f503864879ccd1c162c9191c7f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 40
              },
              {
                "from": 43,
                "to": 26
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 26
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -592
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 26
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -592
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 43,
    "to": 26
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18580"></a>
## FND-18580: Ply 12 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 43,
      "to": 28
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -566
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured a free pawn."
            }
          ],
          "audioUrlHash": "04e58c5d386f06f3ac6d05f334ea85eaa3aac1ed315db31eddd4fcd501945c9b"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 28
          },
          {
            "from": 40,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 43,
      "to": 26
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -592
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {},
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 26
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 28
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -566
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 28
              },
              {
                "from": 40,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -566
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 4
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18581"></a>
## FND-18581: Ply 13 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 3,
      "to": 12
    },
    "moveClassification": 7,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -682
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are now able to win material through a "
            },
            {
              "fragment": "discovered",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 28,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " attack."
            }
          ],
          "audioUrlHash": "8b07f868754740f9c370a6f784c3540e4f763e48f9b1876e940bfc77117b4c7d"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 3,
            "to": 12
          },
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Discovery",
        "hideText": "Hide Discovery"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 28,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -566
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move the bishop to safety."
            }
          ],
          "audioUrlHash": "9c72c165fbd2018b4d7756ed288560df03b0a67fff1d94bd095c0d04745f58d5"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 7,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -682
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You are now able to win material through a "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " attack."
                }
              ],
              "audioUrlHash": "8b07f868754740f9c370a6f784c3540e4f763e48f9b1876e940bfc77117b4c7d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 3,
                "to": 12
              },
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -682
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 20
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": " attack will be powerful here , Black will win material with it."
                }
              ],
              "audioUrlHash": "256d0749820e5622cacbb32d5e519e582b2db4a202a2e0402b97e60706644156"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lose a rook."
                }
              ],
              "audioUrlHash": "ec963fed2af387afd5fc47e1ce11f8f28d5a66b0812f0694acb70ccf78b41f3c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 11,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will have only this move available."
                }
              ],
              "audioUrlHash": "0de6e3de99cf4115774b92836194851e54e6746926696581843927b8a38e776b"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the knight out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "66dfca12a583e600c2ac880a9daed549466cd261b473a145ad13bd8b4c21ca40"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 28,
    "to": 11
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18582"></a>
## FND-18582: Ply 14 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 28,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -682
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A "
            },
            {
              "fragment": "discovered",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 60,
                    "to": 20
                  },
                  {
                    "from": 11,
                    "to": 5
                  }
                ]
              }
            },
            {
              "fragment": " attack is always powerful. This time, you will win material with it."
            }
          ],
          "audioUrlHash": "ba15510279ca9c05ba0c318be42c72242b1099faa27166bec34dbd4f43c6ecc4"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Discovery",
        "hideText": "Hide Discovery"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 60,
            "to": 20
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 11,
            "to": 5
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -682
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 20
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": " attack will be powerful here , Black will win material with it."
                }
              ],
              "audioUrlHash": "256d0749820e5622cacbb32d5e519e582b2db4a202a2e0402b97e60706644156"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a rook."
                }
              ],
              "audioUrlHash": "2b5390c317b3abedebbe4a797221eba46683dccc64564dfaababcc3449ebb70e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 11,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will have only this move available."
                }
              ],
              "audioUrlHash": "0de6e3de99cf4115774b92836194851e54e6746926696581843927b8a38e776b"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the knight from an immediate threat."
                }
              ],
              "audioUrlHash": "20c251000ee4126f17d0416cfd3ef4eb9a59bdef948dd8d6dd8b9849620f7694"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 5,
    "to": 4
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18583"></a>
## FND-18583: Ply 15 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 5,
      "to": 6
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -704
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move gives you the opportunity to win their rook."
            }
          ],
          "audioUrlHash": "7c58759841ef29ec4bbe16c96996f781115c45c84972d9f6585f2580695eac26"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 5,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -682
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move their king out of the check from your knight."
            }
          ],
          "audioUrlHash": "ff9525fcb15ccb49ad70ec02e7ec6fb8d1dbc804759aa5d3e5f03da2d310d922"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 4,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lose a rook."
                }
              ],
              "audioUrlHash": "ec963fed2af387afd5fc47e1ce11f8f28d5a66b0812f0694acb70ccf78b41f3c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 11,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will have only this move available."
                }
              ],
              "audioUrlHash": "0de6e3de99cf4115774b92836194851e54e6746926696581843927b8a38e776b"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -704
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the knight out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "66dfca12a583e600c2ac880a9daed549466cd261b473a145ad13bd8b4c21ca40"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18584"></a>
## FND-18584: Ply 16 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 1
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -667
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You won a rook for free."
            }
          ],
          "audioUrlHash": "a8b7ac03c55c72e2bf17b118de16b736554d5a7586fa02ad682f83ab4a69a3a2"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -704
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {},
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -667
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -667
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18585"></a>
## FND-18585: Ply 17 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 12,
      "to": 3
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -737
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move gives you the opportunity to win their bishop."
            }
          ],
          "audioUrlHash": "2f0febaa70593a64f4f58b97081bec86380e4f75cd19e304da6afc017ce7d712"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 3
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -667
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move puts their bishop on a safer square."
            }
          ],
          "audioUrlHash": "b0a89f220a0dc16c01cadb1b172096df4b0eac66629de4af8348c16561b0a669"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 3
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -737
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a bishop."
                }
              ],
              "audioUrlHash": "aef0cf0a74addc347ccfea09324e560c05b6452ab77e50a5e43446f550b820fa"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 3
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -737
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18586"></a>
## FND-18586: Ply 18 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 60,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -711
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Very good choice!"
            }
          ],
          "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 11,
            "to": 3
          },
          {
            "from": 13,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -737
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Very good choice!"
                }
              ],
              "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the queen out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "316739ec8456391318f79b9f85fee9d1eaa747fd0792f5050b9eca7a30e173ad"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the knight from an immediate threat."
                }
              ],
              "audioUrlHash": "20c251000ee4126f17d0416cfd3ef4eb9a59bdef948dd8d6dd8b9849620f7694"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 3
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 13,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -711
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 3,
                        "to": 6
                      }
                    ],
                    "squares": [
                      4
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 3,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 4,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18587"></a>
## FND-18587: Ply 19 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 5
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 1
        }
      },
      "depth": 97,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are now able to "
            },
            {
              "fragment": "checkmate",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 1,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " the king."
            }
          ],
          "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 6,
            "to": 5
          },
          {
            "from": 1,
            "to": 11
          }
        ],
        "showText": "Show Checkmate",
        "hideText": "Hide Checkmate"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 1,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -711
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They "
            },
            {
              "fragment": "stopped",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 20,
                    "to": 6
                  }
                ],
                "squares": [
                  13
                ]
              }
            },
            {
              "fragment": " the check by interposing a piece between your queen and their king."
            }
          ],
          "audioUrlHash": "de2ba961ff92179678cbec734f026eeca914f7590f8956fd86ac891a6bb62582"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 11,
            "to": 3
          },
          {
            "from": 13,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 20,
            "to": 6
          },
          "color": 4
        }
      ],
      "squares": [
        {
          "square": 13,
          "color": 1
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 5
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 1
            }
          },
          "depth": 97,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You are now able to "
                },
                {
                  "fragment": "checkmate",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 1,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " the king."
                }
              ],
              "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 5
              },
              {
                "from": 1,
                "to": 11
              }
            ],
            "showText": "Show Checkmate",
            "hideText": "Hide Checkmate"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 1,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "depth": 96,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 1,
    "to": 11
  }
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18588"></a>
## FND-18588: Ply 20 in research/refinement/results/comparison-control.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 1,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 0
        }
      },
      "depth": 96,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Congrats on your win!"
            }
          ],
          "audioUrlHash": "fb4c695e68ee26170e1fe0cfdfc9542aaf00e37260f101853c45cb2d62d71ee8"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "depth": 96,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ]
}

### Evidence

- **SRC-0798** `research/refinement/results/comparison-control.json` — [preserved redacted evidence](../evidence/text/c34d2c483a298ee4f7194d67a1e30830559fdeaa2e1b2c8835444e17a59c94de.json)

**Source references:** SRC-0798  
**URL references:** None independently associated  
**Related findings:** FND-18567, FND-18568, FND-18569

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18591"></a>
## FND-18591: Ply 1 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 12,
      "to": 28
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 22
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A strong first move played by grandmasters and beginners alike."
            }
          ],
          "audioUrlHash": "bc99cd093cdaa73e28ecdaea97fb7fae358e8bbfb159704a6327e275968c421f"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 28
          },
          {
            "from": 52,
            "to": 36
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 28
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 22
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 37
                      }
                    ],
                    "squares": [
                      37
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "94b499feaeeac9ad99431f43e54b0dcf036cce4a3cb8d2e90f7fbd15f2bc2998"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 28
              },
              {
                "from": 52,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 37
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 37,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 22
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, Black will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d1975a35dca46408c868cb9256b3b2483b1fdd29eef1db115f1fe036eab9008b"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 52,
    "to": 36
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18592"></a>
## FND-18592: Ply 2 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 52,
      "to": 36
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 22
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A standard response that battles for the center and opens up your light-squared bishop."
            }
          ],
          "audioUrlHash": "1227bfd4f44f8ce7462f2bd5b9d477db79ebef073829da82e48fd59e5b7a9302"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 22
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "7cbae0403100fe7c50106851a88b64f8affe69e6b76dfd4533534d27121c05f8"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 11,
    "to": 27
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18593"></a>
## FND-18593: Ply 3 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -52
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The Blackmar-Diemer Gambit takes full control of the center with e4, immediately attacks the d5 pawn, and allows the queen and light-squared bishop to develop."
            }
          ],
          "audioUrlHash": "e09520a6547ca211e2a317e6f4d57cbb5ddd2f1156431976e3b07004b80e6dc7"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 29
          },
          {
            "from": 36,
            "to": 29
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center with a pawn, trying to gain space."
                }
              ],
              "audioUrlHash": "e72817438cbf1a7ce809d88fb462c1b0470eae473112f737a7919d7af52d3f19"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 29
              },
              {
                "from": 36,
                "to": 29
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 36,
                "to": 29
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 36,
    "to": 29
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18594"></a>
## FND-18594: Ply 4 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 36,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -52
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured that free pawn."
            }
          ],
          "audioUrlHash": "f3c7f58f4b8f273f2e7d78eaa2f67f6e6267ed030236508dbbafa2825524434c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 36,
            "to": 29
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 36,
                "to": 29
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "defend",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 29
                      }
                    ]
                  }
                },
                {
                  "fragment": " the attacked pawn."
                }
              ],
              "audioUrlHash": "79b8a46393cfb043ce35ca23d139774fbb5908eec9ed5377f175ce58548dc998"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 3,
                "to": 39
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18595"></a>
## FND-18595: Ply 5 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 6,
      "to": 13
    },
    "moveClassification": 7,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -116
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their better move was to threaten to capture a pawn."
            }
          ],
          "audioUrlHash": "07cf85d2cb5eebb0bf22693a9d8c7e1fac15f74b77619aa622f96e1ca9b73d5d"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -52
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nc3 develops the knight toward the center, attacks the e4 pawn and controls the b5 square."
            }
          ],
          "audioUrlHash": "64cb374b932595c3d95756f8030723b4c68bda1b4bba36f1f740ad79ffd9a62c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -52
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "defend",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 29
                      }
                    ]
                  }
                },
                {
                  "fragment": " a pawn that was under attack and had no defenders."
                }
              ],
              "audioUrlHash": "4934cdc78d6a376266195c753fc070b51f43d101e4fd37ad262d19ffb45f70f2"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 3,
                "to": 39
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18596"></a>
## FND-18596: Ply 6 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 63,
      "to": 46
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -116
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are bringing your knight into play, eyeing the "
            },
            {
              "fragment": "central squares",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 29
                  },
                  {
                    "from": 46,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "431312a35dba0b14ca986c486512b8b9f4224ef115fb32dde112bd60e2bddf43"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 46,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -116
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "0a4311db259d6632c24a0de8ff3ea1c0abc150432204af13f565f9320e675b0c"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 3,
    "to": 21
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18597"></a>
## FND-18597: Ply 7 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 4,
      "to": 20
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -425
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That queen is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "7c4e6550d37837649b68526678acfe6b62f1631eca76d560a1880d80726c8428"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 4,
            "to": 20
          },
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 3,
            "to": 21
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 3,
      "to": 21
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -116
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their bishop comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "55ac96aa42725a16522cab9c72e76e69d7a5e5a68274287a254cc8e2ab17fac9"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 21,
            "to": 28
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 4,
          "to": 20
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -425
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the queen on an unsafe square."
                }
              ],
              "audioUrlHash": "7d33c64b8f71854d94c5a0462978279a11920c774fb9d3644293ee19562bced9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 4,
                "to": 20
              },
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 3,
                "to": 21
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -425
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Capturing that queen will win material."
                }
              ],
              "audioUrlHash": "d18f7087b665c16841e8ea1deea30f54fde30c89d0422bedbe9660e6a55a80a9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -425
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 29,
    "to": 20
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18598"></a>
## FND-18598: Ply 8 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 29,
      "to": 20
    },
    "moveClassification": 3,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -425
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nice vision spotting and capturing that vulnerable queen."
            }
          ],
          "audioUrlHash": "1eb6390c5d22c81649f4c6b27b2294f4619d395211946891cfa4a055a93df204"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 2,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -425
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a free queen."
                }
              ],
              "audioUrlHash": "ff0ecddae91942343a732190723fa8045c2f78cc8636ec5534995c3b2c525d4a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -425
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 13,
    "to": 20
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18599"></a>
## FND-18599: Ply 9 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 20
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -479
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Takes back."
            }
          ],
          "audioUrlHash": "75740bc8dc07b75aafac22b7112e0ba6a1c23b141c96306524a1f17bfcb03ef3"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 13,
      "to": 20
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -425
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A straightforward recapture."
            }
          ],
          "audioUrlHash": "d34064bc9212b57ab3b3b7a517277b4546f19a903d97c439bb9f0ab4740673eb"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 20
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -479
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will take back."
                }
              ],
              "audioUrlHash": "728b1b246f9fb0e54b613e54205e8b519447c7e0366ba99a1a19ecde8c8b8a57"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 58,
    "to": 43
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18600"></a>
## FND-18600: Ply 10 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 58,
      "to": 43
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -479
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move activates your knight to strengthen control over the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 43,
                    "to": 28
                  },
                  {
                    "from": 43,
                    "to": 37
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "8572a9290f0a0e47b076d9dec2cd4f7ee45288fe2e340f7d23cd38e2315eb4a9"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 58,
            "to": 43
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 43,
            "to": 28
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 43,
            "to": 37
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 58,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -479
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 43,
                        "to": 28
                      },
                      {
                        "from": 43,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 58,
                "to": 43
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 43,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 43,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -479
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18601"></a>
## FND-18601: Ply 11 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 13,
      "to": 40
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -588
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The bishop is left hanging, letting you grab it immediately."
            }
          ],
          "audioUrlHash": "9b9c4416bbd94c3bf6aee1129b455f94590b009441e6fdecbe5e7c89b1616792"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 40
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -479
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their knight comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "482cede704c7932299734c583a24c2083f7583a6a6437e077fa4e4944179855c"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 40
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -588
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the bishop on an unsafe square."
                }
              ],
              "audioUrlHash": "846398c77e8f33fbb1ba864355138f3be7185a9d8768140692d72742a9015d89"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 40
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -588
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That bishop will be free for the taking."
                }
              ],
              "audioUrlHash": "9238ea3ef22d103328b0d5041b7a6dcc4a51f6e878bd2b7082df75c50cf3e09c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18602"></a>
## FND-18602: Ply 12 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 43,
      "to": 28
    },
    "moveClassification": 6,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -542
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured a free pawn."
            }
          ],
          "audioUrlHash": "04e58c5d386f06f3ac6d05f334ea85eaa3aac1ed315db31eddd4fcd501945c9b"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 28
          },
          {
            "from": 40,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -588
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That bishop was yours for the taking!"
            }
          ],
          "audioUrlHash": "23c499a2ff2ab08cd16599788694db7a5548262bd1abb6aabd0267518dda4936"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 28
        },
        "moveClassification": 6,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -542
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 28
              },
              {
                "from": 40,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -542
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 4
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18603"></a>
## FND-18603: Ply 13 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 3,
      "to": 12
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -663
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You get a chance to win a rook through a "
            },
            {
              "fragment": "fork",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 28,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "d7b2ec1f2ae05d4ed0adf08e0b822e57a1420b08c3aa3da691d2e7ec9a612673"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 3,
            "to": 12
          },
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Fork",
        "hideText": "Hide Fork"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 28,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -542
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move puts their bishop on a safer square."
            }
          ],
          "audioUrlHash": "b0a89f220a0dc16c01cadb1b172096df4b0eac66629de4af8348c16561b0a669"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lose a rook."
                }
              ],
              "audioUrlHash": "ec963fed2af387afd5fc47e1ce11f8f28d5a66b0812f0694acb70ccf78b41f3c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 3,
                "to": 12
              },
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Fork",
            "hideText": "Hide Fork"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 11
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will win a rook with that "
                },
                {
                  "fragment": "fork",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 11,
                        "to": 1
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "517b03e8d3179837a21bce9d03da328ab69d6fc4f611e3a4cae7f5f8c1acc501"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Fork",
            "hideText": "Hide Fork"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 11,
                "to": 1
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will step the king away from the checking knight."
                }
              ],
              "audioUrlHash": "62f90284c646d3b0946d09d00cd3b99da515a734dc588215d02ac7cd59b5637c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 28,
    "to": 11
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18604"></a>
## FND-18604: Ply 14 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 28,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -663
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nice way to win material using a "
            },
            {
              "fragment": "fork",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 11,
                    "to": 1
                  },
                  {
                    "from": 11,
                    "to": 5
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "6beb3d1569cbda018a16b3d35dbffd918d7d8632b3f8f266375d49660910658d"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Fork",
        "hideText": "Hide Fork"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 11,
            "to": 1
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 11,
            "to": 5
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will win a rook with that "
                },
                {
                  "fragment": "fork",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 11,
                        "to": 1
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "517b03e8d3179837a21bce9d03da328ab69d6fc4f611e3a4cae7f5f8c1acc501"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Fork",
            "hideText": "Hide Fork"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 11,
                "to": 1
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will evade the check from the knight."
                }
              ],
              "audioUrlHash": "3126ef2039353bba4aced88eef1a34c3e38b913f68d14191bb3e6179519c41cb"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -663
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 5,
    "to": 4
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18605"></a>
## FND-18605: Ply 15 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 5,
      "to": 6
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -708
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve made a mistake, and their rook is now lost."
            }
          ],
          "audioUrlHash": "c23daed586c105a4ad11a2852f26c54c2b3baa0f6283781fa2b52c9597d69a04"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 13
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 20,
            "to": 28
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 5,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -663
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their king steps away from the check by your knight."
            }
          ],
          "audioUrlHash": "1f53ff01efb92ee6eac398c8258a05e16b37c233215d41e5c4d8574d3014afa6"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a rook."
                }
              ],
              "audioUrlHash": "2b5390c317b3abedebbe4a797221eba46683dccc64564dfaababcc3449ebb70e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 13
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 13
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 13,
                        "to": 28
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 7,
                "to": 13
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 13,
                "to": 28
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 20,
                "to": 28
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 28
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -708
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the pawn from an immediate threat."
                }
              ],
              "audioUrlHash": "fe01531c67e1371281fffcd682f963b97198b16f10beffb129991a01662eb19f"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18606"></a>
## FND-18606: Ply 16 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 11,
      "to": 1
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -677
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured a free rook."
            }
          ],
          "audioUrlHash": "ba801356a54b9375716d3fafde58d90abe56cffa48bc4da54e654930f0f0b296"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -708
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {},
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 13
          },
          {
            "from": 11,
            "to": 1
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -677
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -677
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18607"></a>
## FND-18607: Ply 17 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 12,
      "to": 3
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -742
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve made a mistake, and their bishop is now lost."
            }
          ],
          "audioUrlHash": "a0dbb6c71cc0c86dbcf73e92b6937c313b167b37eafd7f721c00669cf83ff5ad"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 3
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -677
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move the bishop to safety."
            }
          ],
          "audioUrlHash": "9c72c165fbd2018b4d7756ed288560df03b0a67fff1d94bd095c0d04745f58d5"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 3
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -742
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a bishop."
                }
              ],
              "audioUrlHash": "aef0cf0a74addc347ccfea09324e560c05b6452ab77e50a5e43446f550b820fa"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 3
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -742
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18608"></a>
## FND-18608: Ply 18 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 60,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -724
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This is a fine move!"
            }
          ],
          "audioUrlHash": "ddcc1ce8c3420c43e9fa544cfdfa07239406eddd546aa3fd12f076e3418b3cee"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 15,
            "to": 23
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -742
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -724
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This is a fine move!"
                }
              ],
              "audioUrlHash": "ddcc1ce8c3420c43e9fa544cfdfa07239406eddd546aa3fd12f076e3418b3cee"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 15,
                "to": 23
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -724
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -724
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the queen from an immediate threat."
                }
              ],
              "audioUrlHash": "81da04c6cb78df21886c74ed0c329f251ada9e05cca2faa7b0d3a49a02f505d0"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 15,
                "to": 23
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 15,
          "to": 23
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -724
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 15,
                "to": 23
              },
              {
                "from": 11,
                "to": 3
              },
              {
                "from": 6,
                "to": 15
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18609"></a>
## FND-18609: Ply 19 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 5
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 1
        }
      },
      "depth": 24,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are now able to "
            },
            {
              "fragment": "checkmate",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 1,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " the king."
            }
          ],
          "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 6,
            "to": 5
          },
          {
            "from": 1,
            "to": 11
          }
        ],
        "showText": "Show Checkmate",
        "hideText": "Hide Checkmate"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 1,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -724
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They "
            },
            {
              "fragment": "blocked",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 20,
                    "to": 6
                  }
                ],
                "squares": [
                  13
                ]
              }
            },
            {
              "fragment": " the check from your queen."
            }
          ],
          "audioUrlHash": "0a0fd0ffc62822329f42d78d0287af43259b2f24c83ba5f44cb46aff3c28fa96"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 20,
            "to": 6
          },
          "color": 4
        }
      ],
      "squares": [
        {
          "square": 13,
          "color": 1
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 5
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 1
            }
          },
          "depth": 24,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You are now able to "
                },
                {
                  "fragment": "checkmate",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 1,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " the king."
                }
              ],
              "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 5
              },
              {
                "from": 1,
                "to": 11
              }
            ],
            "showText": "Show Checkmate",
            "hideText": "Hide Checkmate"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 1,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 1,
    "to": 11
  }
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18610"></a>
## FND-18610: Ply 20 in research/refinement/results/comparison-human.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 1,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 0
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Always feels nice to win!"
            }
          ],
          "audioUrlHash": "0ce80c724d5290e06639882611f093179df9e4354be09416cb3176c66c4eed86"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ]
}

### Evidence

- **SRC-0799** `research/refinement/results/comparison-human.json` — [preserved redacted evidence](../evidence/text/81c11a8fa3203b9960e6c43a066ded07b63f39e4cafa26a35e55a13f46092357.json)

**Source references:** SRC-0799  
**URL references:** None independently associated  
**Related findings:** FND-18589, FND-18590, FND-18591

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18618"></a>
## FND-18618: Ply 1 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 12,
      "to": 28
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 52
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "d4 is slightly less common but just as strong as e4."
            }
          ],
          "audioUrlHash": "741fa74a29e164420402c646f67f5a42f6f285fb40441e3771aeee7cc96dceac"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 28
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 52
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 37
                      }
                    ],
                    "squares": [
                      37
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "94b499feaeeac9ad99431f43e54b0dcf036cce4a3cb8d2e90f7fbd15f2bc2998"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 37
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 37,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18619"></a>
## FND-18619: Ply 2 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 52,
      "to": 36
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 73
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "I like this response. It's proactive, versatile, and battles for the center."
            }
          ],
          "audioUrlHash": "30a22829e1ea598b8eb4101fb166f6feb4596dbd2c337f182e04dbd5fc784dd8"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 73
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, Black will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d1975a35dca46408c868cb9256b3b2483b1fdd29eef1db115f1fe036eab9008b"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 7,
    "to": 22
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18620"></a>
## FND-18620: Ply 3 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -106
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The Blackmar-Diemer Gambit takes full control of the center with e4, immediately attacks the d5 pawn, and allows the queen and light-squared bishop to develop."
            }
          ],
          "audioUrlHash": "e09520a6547ca211e2a317e6f4d57cbb5ddd2f1156431976e3b07004b80e6dc7"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 29
          },
          {
            "from": 36,
            "to": 29
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -106
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center, fighting for space."
                }
              ],
              "audioUrlHash": "2334c5d8159a37807369dcc9d6e1f9e190b44c9385e5fa4345b55c9cc6ce36b4"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 29
              },
              {
                "from": 36,
                "to": 29
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -106
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 36,
    "to": 29
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18621"></a>
## FND-18621: Ply 4 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 36,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -106
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured that free pawn."
            }
          ],
          "audioUrlHash": "f3c7f58f4b8f273f2e7d78eaa2f67f6e6267ed030236508dbbafa2825524434c"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -106
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18622"></a>
## FND-18622: Ply 5 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 13
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -237
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their best option was to threaten to capture a pawn."
            }
          ],
          "audioUrlHash": "bd3a96c5e063f38ca7cc0f81ebe13da0e99a722f5d1a00b7f132b3aafea3517c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -106
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nc3 develops the knight toward the center, attacks the e4 pawn and controls the b5 square."
            }
          ],
          "audioUrlHash": "64cb374b932595c3d95756f8030723b4c68bda1b4bba36f1f740ad79ffd9a62c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -106
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -106
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "defend",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 29
                      }
                    ]
                  }
                },
                {
                  "fragment": " the attacked pawn."
                }
              ],
              "audioUrlHash": "79b8a46393cfb043ce35ca23d139774fbb5908eec9ed5377f175ce58548dc998"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 14,
                "to": 22
              },
              {
                "from": 29,
                "to": 22
              },
              {
                "from": 7,
                "to": 22
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18623"></a>
## FND-18623: Ply 6 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 63,
      "to": 46
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -237
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move activates your knight to strengthen control over the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 29
                  },
                  {
                    "from": 46,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "8572a9290f0a0e47b076d9dec2cd4f7ee45288fe2e340f7d23cd38e2315eb4a9"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 46,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -237
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18624"></a>
## FND-18624: Ply 7 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 4,
      "to": 20
    },
    "moveClassification": 9,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -960
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That queen is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "7c4e6550d37837649b68526678acfe6b62f1631eca76d560a1880d80726c8428"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 4,
            "to": 20
          },
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -237
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their knight comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "482cede704c7932299734c583a24c2083f7583a6a6437e077fa4e4944179855c"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 5,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 4,
          "to": 20
        },
        "moveClassification": 9,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -960
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will leave the queen hanging and available to be taken immediately."
                }
              ],
              "audioUrlHash": "b654f0e78d7fc7f44c52aca4028f4909c4a3f12cc6cd131826da35c1894c9c28"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 4,
                "to": 20
              },
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -960
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a free queen."
                }
              ],
              "audioUrlHash": "ff0ecddae91942343a732190723fa8045c2f78cc8636ec5534995c3b2c525d4a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -960
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 29,
    "to": 20
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18625"></a>
## FND-18625: Ply 8 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 29,
      "to": 20
    },
    "moveClassification": 3,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -960
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nice vision spotting and capturing that vulnerable queen."
            }
          ],
          "audioUrlHash": "1eb6390c5d22c81649f4c6b27b2294f4619d395211946891cfa4a055a93df204"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 2,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -960
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Capturing that queen will win material."
                }
              ],
              "audioUrlHash": "d18f7087b665c16841e8ea1deea30f54fde30c89d0422bedbe9660e6a55a80a9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -960
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 13,
    "to": 20
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18626"></a>
## FND-18626: Ply 9 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1100
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Recaptures."
            }
          ],
          "audioUrlHash": "5b6fb2d6e06b1533ccb50cac54d3217cb2c8a8c786b140b85f25c92593f53468"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 13,
      "to": 20
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -960
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A straightforward recapture."
            }
          ],
          "audioUrlHash": "d34064bc9212b57ab3b3b7a517277b4546f19a903d97c439bb9f0ab4740673eb"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1100
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will take back."
                }
              ],
              "audioUrlHash": "728b1b246f9fb0e54b613e54205e8b519447c7e0366ba99a1a19ecde8c8b8a57"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 58,
    "to": 43
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18627"></a>
## FND-18627: Ply 10 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 58,
      "to": 43
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1100
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Developing the knight and increasing influence in the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 43,
                    "to": 28
                  },
                  {
                    "from": 43,
                    "to": 37
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "1d2decea8d82126236d0be0330d78436af2c322f88652927313b79ccd914987b"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 43,
            "to": 28
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 43,
            "to": 37
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 58,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1100
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 43,
                        "to": 28
                      },
                      {
                        "from": 43,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "0a4311db259d6632c24a0de8ff3ea1c0abc150432204af13f565f9320e675b0c"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 43,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 43,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 7,
    "to": 22
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18628"></a>
## FND-18628: Ply 11 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 13,
      "to": 40
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1402
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That bishop is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "bf506586444905da2bf7029b61813ad44990e299e12f5459945c21b5ca4729f9"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 7,
            "to": 22
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 7,
      "to": 22
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1100
        }
      },
      "depth": 15,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Kingside castling becomes available for your opponent here."
            }
          ],
          "audioUrlHash": "b41e00cd7c10337e6b05309c023b12d9f69742270109ff5fd6db294c6baaf709"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 5,
            "to": 7
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 40
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1402
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the bishop on an unsafe square."
                }
              ],
              "audioUrlHash": "846398c77e8f33fbb1ba864355138f3be7185a9d8768140692d72742a9015d89"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 7,
                "to": 22
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18629"></a>
## FND-18629: Ply 12 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 43,
      "to": 28
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1345
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That pawn was yours for the taking!"
            }
          ],
          "audioUrlHash": "2be85fe239251098e1f912098724e134e98842bfb8acd72741b6de99cf458db4"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 28
          },
          {
            "from": 40,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1402
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That bishop was yours for the taking!"
            }
          ],
          "audioUrlHash": "23c499a2ff2ab08cd16599788694db7a5548262bd1abb6aabd0267518dda4936"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 28
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1345
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 28
              },
              {
                "from": 40,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1345
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 4
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18630"></a>
## FND-18630: Ply 13 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 3,
      "to": 12
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1461
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You can pick up a "
            },
            {
              "fragment": "free",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 40
                  }
                ],
                "squares": [
                  40
                ]
              }
            },
            {
              "fragment": " bishop."
            }
          ],
          "audioUrlHash": "198a7bb89c5df09804b5e794a609cd938958297e8fc6c5be81d8ad03a37036d2"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 3,
            "to": 12
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Free Piece",
        "hideText": "Hide Free Piece"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 40,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1345
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move the bishop to safety."
            }
          ],
          "audioUrlHash": "9c72c165fbd2018b4d7756ed288560df03b0a67fff1d94bd095c0d04745f58d5"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1461
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "give away",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 40
                      }
                    ],
                    "squares": [
                      40
                    ]
                  }
                },
                {
                  "fragment": " a free bishop."
                }
              ],
              "audioUrlHash": "bbc6399caa9ecc606fe9daf0509014c7b79e510fd6427b6e9b25d87cf5a9ebce"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 3,
                "to": 12
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Free Piece",
            "hideText": "Hide Free Piece"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 40,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1461
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free bishop."
                }
              ],
              "audioUrlHash": "805e09f2431790f5002fbb2cf3c0317fb3c34d6d4e2ca06dd52df5bb9fd64ba6"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18631"></a>
## FND-18631: Ply 14 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 28,
      "to": 11
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1451
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You can win a rook with a "
            },
            {
              "fragment": "fork",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 11,
                    "to": 1
                  },
                  {
                    "from": 11,
                    "to": 5
                  }
                ]
              }
            },
            {
              "fragment": ". Very nice!"
            }
          ],
          "audioUrlHash": "32c771737a7a1415ecc07c7b761b771cb66a22e891342fdfcc911b4ae878047e"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 4
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Fork",
        "hideText": "Hide Fork"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 11,
            "to": 1
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 11,
            "to": 5
          },
          "color": 4
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1461
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured a free bishop."
            }
          ],
          "audioUrlHash": "38aef1177ba2e0a00ae285bd66cd801fb6fb9e5bf7d77c49b2c09b2988b08572"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1451
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will win a rook with that "
                },
                {
                  "fragment": "fork",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 11,
                        "to": 1
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "517b03e8d3179837a21bce9d03da328ab69d6fc4f611e3a4cae7f5f8c1acc501"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 4
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Fork",
            "hideText": "Hide Fork"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 11,
                "to": 1
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1451
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will step the king away from the checking knight."
                }
              ],
              "audioUrlHash": "62f90284c646d3b0946d09d00cd3b99da515a734dc588215d02ac7cd59b5637c"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1451
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1451
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 5,
    "to": 4
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18632"></a>
## FND-18632: Ply 15 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 5,
      "to": 6
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1570
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve made a mistake, and their rook is now lost."
            }
          ],
          "audioUrlHash": "c23daed586c105a4ad11a2852f26c54c2b3baa0f6283781fa2b52c9597d69a04"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 2,
            "to": 19
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 5,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1451
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their king steps away from the check by your knight."
            }
          ],
          "audioUrlHash": "1f53ff01efb92ee6eac398c8258a05e16b37c233215d41e5c4d8574d3014afa6"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a rook."
                }
              ],
              "audioUrlHash": "2b5390c317b3abedebbe4a797221eba46683dccc64564dfaababcc3449ebb70e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 11,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will have only this move available."
                }
              ],
              "audioUrlHash": "0de6e3de99cf4115774b92836194851e54e6746926696581843927b8a38e776b"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free rook."
                }
              ],
              "audioUrlHash": "87ca52efe8f46240cfb9c11e241463c1fe51202f0f2154211c4d12fd4ab6088f"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 2,
                "to": 19
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1570
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the knight from an immediate threat."
                }
              ],
              "audioUrlHash": "20c251000ee4126f17d0416cfd3ef4eb9a59bdef948dd8d6dd8b9849620f7694"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18633"></a>
## FND-18633: Ply 16 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 1
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1469
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured a free rook."
            }
          ],
          "audioUrlHash": "ba801356a54b9375716d3fafde58d90abe56cffa48bc4da54e654930f0f0b296"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1570
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1469
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1469
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18634"></a>
## FND-18634: Ply 17 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 12,
      "to": 3
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1608
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They’ve made a mistake, and their bishop is now lost."
            }
          ],
          "audioUrlHash": "a0dbb6c71cc0c86dbcf73e92b6937c313b167b37eafd7f721c00669cf83ff5ad"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 3
          },
          {
            "from": 59,
            "to": 31
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 7,
            "to": 13
          },
          {
            "from": 31,
            "to": 40
          },
          {
            "from": 6,
            "to": 7
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 59,
            "to": 31
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1469
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move puts their bishop on a safer square."
            }
          ],
          "audioUrlHash": "b0a89f220a0dc16c01cadb1b172096df4b0eac66629de4af8348c16561b0a669"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 3
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a bishop."
                }
              ],
              "audioUrlHash": "aef0cf0a74addc347ccfea09324e560c05b6452ab77e50a5e43446f550b820fa"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 3
              },
              {
                "from": 59,
                "to": 31
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 7,
                "to": 13
              },
              {
                "from": 31,
                "to": 40
              },
              {
                "from": 6,
                "to": 7
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 59,
                "to": 31
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 31
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Moving from its starting spot, the bishop will join the game."
                }
              ],
              "audioUrlHash": "316c235de357363aa17a6832ff71e9f09604e77b957665070579700ba317aee3"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this move, Black will be ready to castle on the queenside."
                }
              ],
              "audioUrlHash": "0dace5b2402825148151a9a39139522cc2ec906aab18694aa3c477bf462c4aef"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 7,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 61,
                "to": 59
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 31,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1608
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 59,
    "to": 31
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18635"></a>
## FND-18635: Ply 18 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 60,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1565
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move reaches across the board to win the pawn."
            }
          ],
          "audioUrlHash": "133aeee541ed97e2d2d97d79b159f80d9e917e54514bcf735adaae5b5f47ae3c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          },
          {
            "from": 3,
            "to": 12
          },
          {
            "from": 11,
            "to": 10
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 51,
            "to": 43
          },
          {
            "from": 16,
            "to": 24
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 60,
            "to": 20
          },
          "color": 4
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 59,
      "to": 31
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1608
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You’re preparing for the game ahead, activating the bishop in the opening."
            }
          ],
          "audioUrlHash": "fd5cbdeef98b54f4426d9669b60f5cbbc0312a28a4aca308eecb2d70729548c4"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "From across the board, Black will pick off the pawn."
                }
              ],
              "audioUrlHash": "e10d46ae7450074ee5173544fd5c8e39516abf6f182e461a1c763ad0489e37dd"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              },
              {
                "from": 3,
                "to": 12
              },
              {
                "from": 11,
                "to": 10
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 51,
                "to": 43
              },
              {
                "from": 16,
                "to": 24
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the queen from an immediate threat."
                }
              ],
              "audioUrlHash": "81da04c6cb78df21886c74ed0c329f251ada9e05cca2faa7b0d3a49a02f505d0"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the bishop from an immediate threat."
                }
              ],
              "audioUrlHash": "470b461f3113726b8582ccb80fea34e84267d3fb62cf9aa3e7485939b9a50a25"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 10
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will step the knight out of danger and keep material balance."
                }
              ],
              "audioUrlHash": "66dfca12a583e600c2ac880a9daed549466cd261b473a145ad13bd8b4c21ca40"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 51,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will gain a strong "
                },
                {
                  "fragment": "protected passed pawn",
                  "arrowsAndSquares": {
                    "squares": [
                      43
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "b524876c32e247a798823bceff01ec97e07d235917fc29afd7331d5de56c7fae"
            }
          ]
        },
        "boardMarkings": {
          "squares": [
            {
              "square": 43,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 16,
          "to": 24
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1565
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18636"></a>
## FND-18636: Ply 19 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 5
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 1
        }
      },
      "depth": 97,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You are now able to "
            },
            {
              "fragment": "checkmate",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 1,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " the king."
            }
          ],
          "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 6,
            "to": 5
          },
          {
            "from": 1,
            "to": 11
          }
        ],
        "showText": "Show Checkmate",
        "hideText": "Hide Checkmate"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 1,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1565
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They "
            },
            {
              "fragment": "blocked",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 20,
                    "to": 6
                  }
                ],
                "squares": [
                  13
                ]
              }
            },
            {
              "fragment": " the check from your queen."
            }
          ],
          "audioUrlHash": "0a0fd0ffc62822329f42d78d0287af43259b2f24c83ba5f44cb46aff3c28fa96"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 20,
            "to": 6
          },
          "color": 4
        }
      ],
      "squares": [
        {
          "square": 13,
          "color": 1
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 5
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 1
            }
          },
          "depth": 97,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You are now able to "
                },
                {
                  "fragment": "checkmate",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 1,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " the king."
                }
              ],
              "audioUrlHash": "7d815e90e73fbae9304d8d2589ac3f0655f43795988c50b455f662dacd88b841"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 5
              },
              {
                "from": 1,
                "to": 11
              }
            ],
            "showText": "Show Checkmate",
            "hideText": "Hide Checkmate"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 1,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 1,
    "to": 11
  }
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18637"></a>
## FND-18637: Ply 20 in research/refinement/results/followup-hash128-softfalse.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 1,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 0
        }
      },
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Always feels nice to win!"
            }
          ],
          "audioUrlHash": "0ce80c724d5290e06639882611f093179df9e4354be09416cb3176c66c4eed86"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ]
}

### Evidence

- **SRC-0805** `research/refinement/results/followup-hash128-softfalse.json` — [preserved redacted evidence](../evidence/text/0edde93fa173dd926d959dc27c87111296c86121e2ad3375e36d8d9596d6a54c.json)

**Source references:** SRC-0805  
**URL references:** None independently associated  
**Related findings:** FND-18616, FND-18617, FND-18618

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18640"></a>
## FND-18640: Ply 1 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 12,
      "to": 28
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 47
        }
      },
      "depth": 25,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Fighting for the center and opening up their pieces for development."
            }
          ],
          "audioUrlHash": "d503ab104c9e1d8a3b84c2213e692f5301ce47ffd1d5b18316cc27d5e4fd3e75"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 28
          },
          {
            "from": 52,
            "to": 36
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 28
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 47
            }
          },
          "depth": 25,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, White will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 28,
                        "to": 37
                      }
                    ],
                    "squares": [
                      37
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d575221e5c1c6344f85df924f675e080a38c1bdd864fd14fc97306c5f5d3f2bc"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 28
              },
              {
                "from": 52,
                "to": 36
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 37
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 37,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 47
            }
          },
          "depth": 24,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will make a solid central advance, "
                },
                {
                  "fragment": "gaining influence",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and restricting counterplay."
                }
              ],
              "audioUrlHash": "7cbae0403100fe7c50106851a88b64f8affe69e6b76dfd4533534d27121c05f8"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 52,
    "to": 36
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18641"></a>
## FND-18641: Ply 2 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 52,
      "to": 36
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": 47
        }
      },
      "depth": 24,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A standard response that battles for the center and opens up your light-squared bishop."
            }
          ],
          "audioUrlHash": "1227bfd4f44f8ce7462f2bd5b9d477db79ebef073829da82e48fd59e5b7a9302"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 52,
          "to": 36
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": 47
            }
          },
          "depth": 24,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With this push, Black will grab "
                },
                {
                  "fragment": "central ground",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 36,
                        "to": 29
                      }
                    ],
                    "squares": [
                      29
                    ]
                  }
                },
                {
                  "fragment": " and open lines for development."
                }
              ],
              "audioUrlHash": "d1975a35dca46408c868cb9256b3b2483b1fdd29eef1db115f1fe036eab9008b"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 36,
                "to": 29
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 29,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 11,
    "to": 27
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18642"></a>
## FND-18642: Ply 3 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 13,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -113
        }
      },
      "depth": 24,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "The Blackmar-Diemer Gambit takes full control of the center with e4, immediately attacks the d5 pawn, and allows the queen and light-squared bishop to develop."
            }
          ],
          "audioUrlHash": "e09520a6547ca211e2a317e6f4d57cbb5ddd2f1156431976e3b07004b80e6dc7"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 13,
            "to": 29
          },
          {
            "from": 36,
            "to": 29
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -113
            }
          },
          "depth": 24,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will strike at the center with a pawn, trying to gain space."
                }
              ],
              "audioUrlHash": "e72817438cbf1a7ce809d88fb462c1b0470eae473112f737a7919d7af52d3f19"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 13,
                "to": 29
              },
              {
                "from": 36,
                "to": 29
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -113
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 36,
    "to": 29
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18643"></a>
## FND-18643: Ply 4 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 36,
      "to": 29
    },
    "moveClassification": 1,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -113
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That pawn was yours for the taking!"
            }
          ],
          "audioUrlHash": "2be85fe239251098e1f912098724e134e98842bfb8acd72741b6de99cf458db4"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 36,
          "to": 29
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -113
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18644"></a>
## FND-18644: Ply 5 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 13
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -257
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their best option was to threaten to capture a pawn."
            }
          ],
          "audioUrlHash": "bd3a96c5e063f38ca7cc0f81ebe13da0e99a722f5d1a00b7f132b3aafea3517c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -113
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Nc3 develops the knight toward the center, attacks the e4 pawn and controls the b5 square."
            }
          ],
          "audioUrlHash": "64cb374b932595c3d95756f8030723b4c68bda1b4bba36f1f740ad79ffd9a62c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 63,
            "to": 46
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -113
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 19,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "7197bfa9f7c84f063268948321282665c45fe64bf259374ee7c1034c68706253"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 63,
                "to": 46
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 1,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -113
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "defend",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 19,
                        "to": 29
                      }
                    ]
                  }
                },
                {
                  "fragment": " a pawn that was under attack and had no defenders."
                }
              ],
              "audioUrlHash": "4934cdc78d6a376266195c753fc070b51f43d101e4fd37ad262d19ffb45f70f2"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 63,
                "to": 46
              },
              {
                "from": 14,
                "to": 22
              },
              {
                "from": 29,
                "to": 22
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 53,
                "to": 45
              },
              {
                "from": 6,
                "to": 20
              },
              {
                "from": 62,
                "to": 53
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 19,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 63,
    "to": 46
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18645"></a>
## FND-18645: Ply 6 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 63,
      "to": 46
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -257
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move activates your knight to strengthen control over the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 46,
                    "to": 29
                  },
                  {
                    "from": 46,
                    "to": 36
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "8572a9290f0a0e47b076d9dec2cd4f7ee45288fe2e340f7d23cd38e2315eb4a9"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 46,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 63,
          "to": 46
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -257
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 46,
                        "to": 29
                      },
                      {
                        "from": 46,
                        "to": 36
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "59906ce50b37f651c96f00596d759bbdb5716cc0227cbbeb90935377dcb54024"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 29
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 46,
                "to": 36
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 2,
    "to": 19
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18646"></a>
## FND-18646: Ply 7 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 4,
      "to": 20
    },
    "moveClassification": 9,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -983
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That queen is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "7c4e6550d37837649b68526678acfe6b62f1631eca76d560a1880d80726c8428"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 4,
            "to": 20
          },
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 2,
            "to": 19
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 2,
      "to": 19
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -257
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their knight comes into play, supporting the center."
            }
          ],
          "audioUrlHash": "482cede704c7932299734c583a24c2083f7583a6a6437e077fa4e4944179855c"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 19,
            "to": 29
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 19,
            "to": 36
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 5,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 4,
          "to": 20
        },
        "moveClassification": 9,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -983
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the queen on an unsafe square."
                }
              ],
              "audioUrlHash": "7d33c64b8f71854d94c5a0462978279a11920c774fb9d3644293ee19562bced9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 4,
                "to": 20
              },
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 2,
                "to": 19
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -983
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a free queen."
                }
              ],
              "audioUrlHash": "ff0ecddae91942343a732190723fa8045c2f78cc8636ec5534995c3b2c525d4a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -983
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 29,
    "to": 20
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18647"></a>
## FND-18647: Ply 8 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 29,
      "to": 20
    },
    "moveClassification": 3,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -983
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You won material by capturing that queen."
            }
          ],
          "audioUrlHash": "187f5c59cfc978e58f427a180343e3c7dee1326ddc915a2c16fcdd54b5e11043"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 29,
            "to": 20
          },
          {
            "from": 13,
            "to": 20
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 2,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 29,
          "to": 20
        },
        "moveClassification": 3,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -983
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Capturing that queen will win material."
                }
              ],
              "audioUrlHash": "d18f7087b665c16841e8ea1deea30f54fde30c89d0422bedbe9660e6a55a80a9"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 29,
                "to": 20
              },
              {
                "from": 13,
                "to": 20
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -983
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will simply recapture."
                }
              ],
              "audioUrlHash": "d689b1ce83c3ebf35d89c7e61118940904a4978a8ed008bccfe1c71b703c5b69"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 13,
    "to": 20
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18648"></a>
## FND-18648: Ply 9 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1134
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Recaptures."
            }
          ],
          "audioUrlHash": "5b6fb2d6e06b1533ccb50cac54d3217cb2c8a8c786b140b85f25c92593f53468"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 13,
      "to": 20
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -983
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "A clear recapture."
            }
          ],
          "audioUrlHash": "887801f5c34b862cbbb942e9fb8e0d1452d1b168fea3d2a22ff136b513101d51"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1134
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will recapture."
                }
              ],
              "audioUrlHash": "d5bbdeae05f35b76991dd4c45ba07aa37be520cc5e61563ed05f5f719dd2966d"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 58,
    "to": 43
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18649"></a>
## FND-18649: Ply 10 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 58,
      "to": 43
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1134
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Develops the knight and supports the "
            },
            {
              "fragment": "center",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 43,
                    "to": 28
                  },
                  {
                    "from": 43,
                    "to": 37
                  }
                ]
              }
            },
            {
              "fragment": "."
            }
          ],
          "audioUrlHash": "cd4e8d35fa4992ad42186121edaaa8dcf3d5fa36cbb4833c291540c7427e1621"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 43,
            "to": 28
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 43,
            "to": 37
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 58,
          "to": 43
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1134
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the knight and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 43,
                        "to": 28
                      },
                      {
                        "from": 43,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "0a4311db259d6632c24a0de8ff3ea1c0abc150432204af13f565f9320e675b0c"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 43,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 43,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 28,
    "to": 36
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18650"></a>
## FND-18650: Ply 11 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 13,
      "to": 40
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1393
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "That bishop is unprotected and can be captured right away."
            }
          ],
          "audioUrlHash": "bf506586444905da2bf7029b61813ad44990e299e12f5459945c21b5ca4729f9"
        }
      ]
    },
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 28,
            "to": 36
          },
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 28,
      "to": 36
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1134
        }
      },
      "depth": 16,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 40
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1393
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Uh oh , this move will place the bishop on an unsafe square."
                }
              ],
              "audioUrlHash": "846398c77e8f33fbb1ba864355138f3be7185a9d8768140692d72742a9015d89"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 28,
                "to": 36
              },
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18651"></a>
## FND-18651: Ply 12 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 43,
      "to": 28
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1297
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured that free pawn."
            }
          ],
          "audioUrlHash": "f3c7f58f4b8f273f2e7d78eaa2f67f6e6267ed030236508dbbafa2825524434c"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 43,
            "to": 28
          },
          {
            "from": 40,
            "to": 4
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1393
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured that free bishop."
            }
          ],
          "audioUrlHash": "cc3e543bc043197fbf305b1c0d102037a6a5d9c65ad17fd2bf90274c2f74e197"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 28,
            "to": 36
          },
          {
            "from": 43,
            "to": 26
          },
          {
            "from": 20,
            "to": 28
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 43,
          "to": 28
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1297
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That pawn will be free for the taking."
                }
              ],
              "audioUrlHash": "4cd8f474bd0b955f409d0db85ddbbf2716a5b0bfaf88539593a26cd7176a447d"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 43,
                "to": 28
              },
              {
                "from": 40,
                "to": 4
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 4
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1297
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will move the bishop to safety."
                }
              ],
              "audioUrlHash": "47024708fecbc7ef75ea9f21facb49ef8de4222676c3c261ab189fd159dc5992"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 4
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18652"></a>
## FND-18652: Ply 13 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 3,
      "to": 12
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1521
        }
      },
      "depth": 23,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Your opponent develops their bishop off its starting square."
            }
          ],
          "audioUrlHash": "2faa3e051e338a30ca3e4da41433ce9c6ec662231582ce92f69bc3494d0d0284"
        }
      ]
    },
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 4
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1297
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They move the bishop to safety."
            }
          ],
          "audioUrlHash": "9c72c165fbd2018b4d7756ed288560df03b0a67fff1d94bd095c0d04745f58d5"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 3,
          "to": 12
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 23,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the bishop off its starting square."
                }
              ],
              "audioUrlHash": "fab60bbbc16cf570514cf6af1fb5bf2324eff4d7bb8b44f4e87393b83799f8dd"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 28,
    "to": 11
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18653"></a>
## FND-18653: Ply 14 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 28,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1521
        }
      },
      "depth": 22,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You'll win a pawn using a "
            },
            {
              "fragment": "discovered",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 60,
                    "to": 20
                  },
                  {
                    "from": 11,
                    "to": 5
                  }
                ]
              }
            },
            {
              "fragment": " attack."
            }
          ],
          "audioUrlHash": "91ac14e6b6406e44f707ce53204f508df07501f3e641008498917eb05da3f635"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 28,
            "to": 11
          },
          {
            "from": 5,
            "to": 13
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 2,
            "to": 17
          },
          {
            "from": 59,
            "to": 38
          },
          {
            "from": 17,
            "to": 11
          },
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 13,
            "to": 5
          },
          {
            "from": 57,
            "to": 60
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 53,
            "to": 37
          },
          {
            "from": 1,
            "to": 3
          }
        ],
        "showText": "Show Discovery",
        "hideText": "Hide Discovery"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 60,
            "to": 20
          },
          "color": 4
        },
        {
          "arrow": {
            "from": 11,
            "to": 5
          },
          "color": 4
        }
      ]
    }
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 28,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 22,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "A "
                },
                {
                  "fragment": "discovered",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 60,
                        "to": 20
                      },
                      {
                        "from": 11,
                        "to": 5
                      }
                    ]
                  }
                },
                {
                  "fragment": " attack will be powerful here."
                }
              ],
              "audioUrlHash": "934aaadd850d9120e2e4af622638447ad4aef8006a57d6c79c557eecf0d2a64a"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 28,
                "to": 11
              },
              {
                "from": 5,
                "to": 13
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 2,
                "to": 17
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 17,
                "to": 11
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 13,
                "to": 5
              },
              {
                "from": 57,
                "to": 60
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 53,
                "to": 37
              },
              {
                "from": 1,
                "to": 3
              }
            ],
            "showText": "Show Discovery",
            "hideText": "Hide Discovery"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 60,
                "to": 20
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 11,
                "to": 5
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will evade the check from the knight."
                }
              ],
              "audioUrlHash": "3126ef2039353bba4aced88eef1a34c3e38b913f68d14191bb3e6179519c41cb"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 17
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will develop the knight off its starting square."
                }
              ],
              "audioUrlHash": "7d083d699713824af6a0721409c36b44aae9167e544fb69819735b285e50a606"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 2,
                "to": 17
              },
              {
                "from": 59,
                "to": 38
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 38
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The threat on the pawn will become more serious with this move."
                }
              ],
              "audioUrlHash": "ca25911ff3711080f3387b15efa6f0eec6052cc9a87ec87d66a1bb8e461fbcc5"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 38,
                "to": 20
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 17,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will capture a knight and eliminates a threat."
                }
              ],
              "audioUrlHash": "713dbdfb77bc7717b791da5232a9da039866c05fc77afa589dba6ea286db394c"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 17,
                "to": 11
              },
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 13,
                "to": 5
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That will be a free pawn."
                }
              ],
              "audioUrlHash": "6a3737e6601bdde6fe68756d27e0b8a8ce798e75037263bdd73135101b6233ef"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 13,
                "to": 5
              },
              {
                "from": 57,
                "to": 60
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 53,
                "to": 37
              },
              {
                "from": 1,
                "to": 3
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 13,
          "to": 5
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will step the king away from the checking queen."
                }
              ],
              "audioUrlHash": "d06127c4ff40ac22ac06fa9f83f25b09b35a868f7c3690d543c5ac1144d1263c"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 57,
          "to": 60
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will stack pieces, improving coordination."
                }
              ],
              "audioUrlHash": "f6840c4f4ab7352842cf02cd4063c6d9aa4b140612258ffad5db541bed1613c8"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "protect",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 12
                      },
                      {
                        "from": 20,
                        "to": 12
                      }
                    ]
                  }
                },
                {
                  "fragment": " an underdefended bishop that is under attack."
                }
              ],
              "audioUrlHash": "55de9dc18e866b23582badcce3f3d7665407eabfe926414cd6d305231d7cdd21"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 12
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 20,
                "to": 12
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 53,
          "to": 37
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 12,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "After a follow-up, this will win a bishop by kicking a defender."
                }
              ],
              "audioUrlHash": "2032732daa5e4f342fbcb6fb634806f005efabc8a00c28c9e996f53d119b0cea"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 53,
                "to": 37
              },
              {
                "from": 1,
                "to": 3
              },
              {
                "from": 37,
                "to": 29
              },
              {
                "from": 22,
                "to": 37
              },
              {
                "from": 20,
                "to": 12
              },
              {
                "from": 5,
                "to": 6
              }
            ],
            "showText": "Show Defender Kick",
            "hideText": "Hide Defender Kick"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 3
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1521
            }
          },
          "depth": 11,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "defend",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 3,
                        "to": 11
                      },
                      {
                        "from": 20,
                        "to": 11
                      }
                    ]
                  }
                },
                {
                  "fragment": " the attacked knight."
                }
              ],
              "audioUrlHash": "ed82480766c229f8b837bda548b4b8081a67f089d927eb5284c80e5e74063482"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 3,
                "to": 11
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 20,
                "to": 11
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 5,
    "to": 13
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18654"></a>
## FND-18654: Ply 15 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 5,
      "to": 6
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1555
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move gives you the opportunity to win their rook."
            }
          ],
          "audioUrlHash": "7c58759841ef29ec4bbe16c96996f781115c45c84972d9f6585f2580695eac26"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 5,
            "to": 6
          },
          {
            "from": 46,
            "to": 40
          },
          {
            "from": 7,
            "to": 22
          },
          {
            "from": 59,
            "to": 38
          },
          {
            "from": 2,
            "to": 19
          },
          {
            "from": 38,
            "to": 20
          },
          {
            "from": 6,
            "to": 7
          },
          {
            "from": 11,
            "to": 1
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 5,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1521
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Their king steps away from the check by your knight."
            }
          ],
          "audioUrlHash": "1f53ff01efb92ee6eac398c8258a05e16b37c233215d41e5c4d8574d3014afa6"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 5,
          "to": 6
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a rook."
                }
              ],
              "audioUrlHash": "2b5390c317b3abedebbe4a797221eba46683dccc64564dfaababcc3449ebb70e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 5,
                "to": 6
              },
              {
                "from": 46,
                "to": 40
              },
              {
                "from": 7,
                "to": 22
              },
              {
                "from": 59,
                "to": 38
              },
              {
                "from": 2,
                "to": 19
              },
              {
                "from": 38,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              },
              {
                "from": 11,
                "to": 1
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 7,
          "to": 22
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "White will "
                },
                {
                  "fragment": "develop",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 22,
                        "to": 28
                      },
                      {
                        "from": 22,
                        "to": 37
                      }
                    ]
                  }
                },
                {
                  "fragment": " the knight, increasing influence in the center."
                }
              ],
              "audioUrlHash": "d04d5a6b7bba27134711836200db32b0f5a48f901b90b706ac409ec3eb3b7155"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 22,
                "to": 28
              },
              "color": 4
            },
            {
              "arrow": {
                "from": 22,
                "to": 37
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 59,
          "to": 38
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Black will develop the bishop and support the "
                },
                {
                  "fragment": "center",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 38,
                        "to": 29
                      }
                    ]
                  }
                },
                {
                  "fragment": "."
                }
              ],
              "audioUrlHash": "409df0e7ac7c19e0b7165e39779bbae00016c9644992b1ca70299fb726c672b9"
            }
          ]
        },
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 38,
                "to": 29
              },
              "color": 4
            }
          ]
        }
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 2,
          "to": 19
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "With the knight also developed, White will have all pieces ready for action."
                }
              ],
              "audioUrlHash": "85e9f3d50f8d772e9a3678304506f99c684d59384dfea1a12789f3dbad222eac"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 38,
          "to": 20
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 15,
          "engine": 11
        },
        "speech": {},
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 38,
                "to": 20
              },
              {
                "from": 6,
                "to": 7
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 7
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 14,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will evade the check from the bishop."
                }
              ],
              "audioUrlHash": "6a7265b3f362ddc46da560ca283311eea709e3d54ac0d80e33e6252143dc3a51"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1555
            }
          },
          "depth": 13,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "After precise calculation, Black will capture the well-deserved rook."
                }
              ],
              "audioUrlHash": "a750d8c65733688541eda3a5755aeadd31d657b3d210c9a29cf3c6a14547ed1c"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18655"></a>
## FND-18655: Ply 16 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 11,
      "to": 1
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1515
        }
      },
      "depth": 21,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You captured that free rook."
            }
          ],
          "audioUrlHash": "d500c35e6973d0ea529babee77ebc559d98a9ec0f9178b0a04e5e6ae8ecb9ec4"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 11,
            "to": 1
          },
          {
            "from": 40,
            "to": 13
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1555
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 4,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 11,
          "to": 1
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1515
            }
          },
          "depth": 21,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "That rook will be free for the taking."
                }
              ],
              "audioUrlHash": "bc9b61026224e2f170654eb34b317a2e48282c1ca7283bfa131895ba35d216a3"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 11,
                "to": 1
              },
              {
                "from": 40,
                "to": 13
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1515
            }
          },
          "depth": 20,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This move will put the bishop on a safer square."
                }
              ],
              "audioUrlHash": "6490e8be64c0aa95a89a5536ab81694e500b0f22627e6ceb408f43f6577f4958"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 1
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18656"></a>
## FND-18656: Ply 17 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 12,
      "to": 3
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1620
        }
      },
      "depth": 19,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move gives you the opportunity to win their bishop."
            }
          ],
          "audioUrlHash": "2f0febaa70593a64f4f58b97081bec86380e4f75cd19e304da6afc017ce7d712"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 12,
            "to": 3
          },
          {
            "from": 46,
            "to": 40
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 46,
            "to": 40
          },
          "color": 2
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1515
        }
      },
      "depth": 20,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "This move puts their bishop on a safer square."
            }
          ],
          "audioUrlHash": "b0a89f220a0dc16c01cadb1b172096df4b0eac66629de4af8348c16561b0a669"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 12,
          "to": 3
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1620
            }
          },
          "depth": 19,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will lead to losing a bishop."
                }
              ],
              "audioUrlHash": "aef0cf0a74addc347ccfea09324e560c05b6452ab77e50a5e43446f550b820fa"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 12,
                "to": 3
              },
              {
                "from": 46,
                "to": 40
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 46,
                "to": 40
              },
              "color": 2
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 46,
          "to": 40
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1620
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {},
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 46,
    "to": 40
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18657"></a>
## FND-18657: Ply 18 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 60,
      "to": 20
    },
    "moveClassification": 5,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1597
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Very good choice!"
            }
          ],
          "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 60,
            "to": 20
          },
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {}
  },
  "bestAlternativeMove": {
    "move": {
      "from": 46,
      "to": 40
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1620
        }
      },
      "depth": 18,
      "engine": 11
    },
    "speech": {},
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 1,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 60,
          "to": 20
        },
        "moveClassification": 5,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1597
            }
          },
          "depth": 18,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "Very good choice!"
                }
              ],
              "audioUrlHash": "69891d6138484ff43a1607b51d613bf9463a494b60e49408543e4d2dc4cdaf38"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 60,
                "to": 20
              },
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {}
      },
      "movedColor": 2
    },
    {
      "playedMove": {
        "move": {
          "from": 40,
          "to": 13
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1597
            }
          },
          "depth": 17,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will "
                },
                {
                  "fragment": "block",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 20,
                        "to": 6
                      }
                    ],
                    "squares": [
                      13
                    ]
                  }
                },
                {
                  "fragment": " the check from an opposing queen."
                }
              ],
              "audioUrlHash": "088e129b72d765c7c091bebc18c8b6eb73e29ec13c0d631b5d0a6cc2ece2e49e"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 40,
                "to": 13
              },
              {
                "from": 20,
                "to": 11
              }
            ],
            "showText": "Show Follow-Up",
            "hideText": "Hide Follow-Up"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 20,
                "to": 6
              },
              "color": 4
            }
          ],
          "squares": [
            {
              "square": 13,
              "color": 1
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 20,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "scoreCentipawnsWhite",
              "value": -1597
            }
          },
          "depth": 16,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "This will calmly remove the queen from an immediate threat."
                }
              ],
              "audioUrlHash": "81da04c6cb78df21886c74ed0c329f251ada9e05cca2faa7b0d3a49a02f505d0"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 40,
    "to": 13
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18658"></a>
## FND-18658: Ply 19 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "isKeyMoment": true,
  "playedMove": {
    "move": {
      "from": 6,
      "to": 5
    },
    "moveClassification": 8,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 1
        }
      },
      "depth": 97,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "You get a chance to "
            },
            {
              "fragment": "checkmate",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 1,
                    "to": 11
                  }
                ],
                "squares": [
                  11
                ]
              }
            },
            {
              "fragment": " the king."
            }
          ],
          "audioUrlHash": "0c7cc39c8b71567bbb43dc81cf457bb654862b90056614472581230bd65c37ee"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 6,
            "to": 5
          },
          {
            "from": 1,
            "to": 11
          }
        ],
        "showText": "Show Checkmate",
        "hideText": "Hide Checkmate"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 1,
            "to": 11
          },
          "color": 2
        }
      ],
      "squares": [
        {
          "square": 11,
          "color": 3
        }
      ]
    }
  },
  "bestAlternativeMove": {
    "move": {
      "from": 40,
      "to": 13
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "scoreCentipawnsWhite",
          "value": -1597
        }
      },
      "depth": 17,
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "They "
            },
            {
              "fragment": "blocked",
              "arrowsAndSquares": {
                "arrows": [
                  {
                    "from": 20,
                    "to": 6
                  }
                ],
                "squares": [
                  13
                ]
              }
            },
            {
              "fragment": " the check from your queen."
            }
          ],
          "audioUrlHash": "0a0fd0ffc62822329f42d78d0287af43259b2f24c83ba5f44cb46aff3c28fa96"
        }
      ]
    },
    "showMovesButtons": [
      {
        "movesToShow": [
          {
            "from": 40,
            "to": 13
          },
          {
            "from": 20,
            "to": 11
          }
        ],
        "showText": "Show Follow-Up",
        "hideText": "Hide Follow-Up"
      }
    ],
    "boardMarkings": {
      "arrows": [
        {
          "arrow": {
            "from": 20,
            "to": 6
          },
          "color": 4
        }
      ],
      "squares": [
        {
          "square": 13,
          "color": 1
        }
      ]
    }
  },
  "movedColor": 1,
  "coachEmotion": 6,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 6,
          "to": 5
        },
        "moveClassification": 8,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 1
            }
          },
          "depth": 97,
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "You get a chance to "
                },
                {
                  "fragment": "checkmate",
                  "arrowsAndSquares": {
                    "arrows": [
                      {
                        "from": 1,
                        "to": 11
                      }
                    ],
                    "squares": [
                      11
                    ]
                  }
                },
                {
                  "fragment": " the king."
                }
              ],
              "audioUrlHash": "0c7cc39c8b71567bbb43dc81cf457bb654862b90056614472581230bd65c37ee"
            }
          ]
        },
        "showMovesButtons": [
          {
            "movesToShow": [
              {
                "from": 6,
                "to": 5
              },
              {
                "from": 1,
                "to": 11
              }
            ],
            "showText": "Show Checkmate",
            "hideText": "Hide Checkmate"
          }
        ],
        "boardMarkings": {
          "arrows": [
            {
              "arrow": {
                "from": 1,
                "to": 11
              },
              "color": 2
            }
          ],
          "squares": [
            {
              "square": 11,
              "color": 3
            }
          ]
        }
      },
      "movedColor": 1
    },
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ],
  "bestNextMove": {
    "from": 1,
    "to": 11
  }
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.

<a id="FND-18659"></a>
## FND-18659: Ply 20 in research/refinement/results/followup-hash128-softtrue.json

**Category:** native_review_moves  
**Classification:** verified observation  
**Verification:** historical  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

{
  "playedMove": {
    "move": {
      "from": 1,
      "to": 11
    },
    "moveClassification": 4,
    "score": {
      "score": {
        "score": {
          "case": "mateInBlack",
          "value": 0
        }
      },
      "engine": 11
    },
    "speech": {
      "sentences": [
        {
          "sentenceFragments": [
            {
              "fragment": "Always feels nice to win!"
            }
          ],
          "audioUrlHash": "0ce80c724d5290e06639882611f093179df9e4354be09416cb3176c66c4eed86"
        }
      ]
    },
    "boardMarkings": {}
  },
  "movedColor": 2,
  "coachEmotion": 3,
  "explainLine": [
    {
      "playedMove": {
        "move": {
          "from": 1,
          "to": 11
        },
        "moveClassification": 4,
        "score": {
          "score": {
            "score": {
              "case": "mateInBlack",
              "value": 0
            }
          },
          "engine": 11
        },
        "speech": {
          "sentences": [
            {
              "sentenceFragments": [
                {
                  "fragment": "The game will be over."
                }
              ],
              "audioUrlHash": "0242a53e821bbb94b2fa86f61bb1309679b9d01052685004cb5fa7bfa1268847"
            }
          ]
        },
        "boardMarkings": {}
      },
      "movedColor": 2
    }
  ]
}

### Evidence

- **SRC-0806** `research/refinement/results/followup-hash128-softtrue.json` — [preserved redacted evidence](../evidence/text/67ccc4f7cd7385a25512f228d6c41b286c091695cc4de9013e9fa157d60c2e7c.json)

**Source references:** SRC-0806  
**URL references:** None independently associated  
**Related findings:** FND-18638, FND-18639, FND-18640

**Additional notes:** Full per-ply scores, alternatives, speech fragments, native audio hashes and markings are preserved. Repeated trials are intentionally not merged across different source payloads.
