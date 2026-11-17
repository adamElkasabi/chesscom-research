# Contradictions,version distinctions and duplicates

[Master index](00_MASTER_INDEX.md)

Competing claims are preserved rather than silently harmonized. Namespaces,pipeline differences,chronology and evidence quality are stated per record. Duplicate sources are recorded by checksum in the source manifest; separate provenance remains even when evidence copies share content.

## CON-001 — Server-only absolute claim versus locally executable CEE

```json
{
  "id": "CON-001",
  "title": "Server-only absolute claim versus locally executable CEE",
  "claim_a": "uploads/PREMIUM-ANALYSIS.md says every number belongs to server and only presentation runs in browser.",
  "claim_b": "Later native WASM locally produces accuracy,rating,classifications,speech and human-mode searches.",
  "sources": [
    "SRC-2047",
    "SRC-0049",
    "SRC-0799"
  ],
  "best_supported_interpretation": "Native full website routing is server-side in inspected path; shipped local CEE is nevertheless capable of calculation. Earlier broad impossibilityclaim superseded.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-002 — Two different classification number spaces

```json
{
  "id": "CON-002",
  "title": "Two different classification number spaces",
  "claim_a": "LegacyanalysisMistake11/Blunder15/Miss20.",
  "claim_b": "CompactCEE Mistake8/Blunder9/Missed10/Tricky20.",
  "sources": [
    "SRC-2047",
    "SRC-0206",
    "SRC-0414"
  ],
  "best_supported_interpretation": "Different namespaces,not conflicting versions of the same enum. Decodebyfieldtype.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-003 — Engine11 was initially treated as evidence Human inactive

```json
{
  "id": "CON-003",
  "title": "Engine11 was initially treated as evidence Human inactive",
  "claim_a": "Earlier release notes say requested12/actual11meansnotTorchHuman.",
  "claim_b": "Successful human-mode probe stillreports11andlogsPVtreecommands.",
  "sources": [
    "SRC-0028",
    "SRC-0838",
    "SRC-2049"
  ],
  "best_supported_interpretation": "Underlying engine ID is not a sufficient human-mode detector; command/mode evidence required.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-004 — Old human verdict predates full experimental review

```json
{
  "id": "CON-004",
  "title": "Old human verdict predates full experimental review",
  "claim_a": "torch-human-client-verdict says no successful full human-modeGameReview.",
  "claim_b": "Later comparison-human generates fullreviewafter79human preloads.",
  "sources": [
    "SRC-0871",
    "SRC-1628",
    "SRC-0799"
  ],
  "best_supported_interpretation": "Chronological refinement; later result is an experimental local pipeline,not verified native server parity.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-005 — Audio unknown versus later user confirmation

```json
{
  "id": "CON-005",
  "title": "Audio unknown versus later user confirmation",
  "claim_a": "v0.1.7README audio playbackunconfirmed.",
  "claim_b": "User confirmedUIandsoundworked.",
  "sources": [
    "SRC-0016",
    "SRC-2049"
  ],
  "best_supported_interpretation": "Historical README not retroactively edited; user report adds runtime evidence,not all coach-path verification.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-006 — Hidden-card update initially blamed for failure

```json
{
  "id": "CON-006",
  "title": "Hidden-card update initially blamed for failure",
  "claim_a": "User first reported stuck2%andnotworking.",
  "claim_b": "User explicitly corrected thatanalysisworkedandonlyprogressdidnot.",
  "sources": [
    "SRC-2049",
    "SRC-0052"
  ],
  "best_supported_interpretation": "No confirmed fullanalysisregressionorrollback; coarseprogress was already0/2/100.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-007 — v0.1.9 README includes old coarse-progress notes

```json
{
  "id": "CON-007",
  "title": "v0.1.9 README includes old coarse-progress notes",
  "claim_a": "New topsection describes measuredestimate.",
  "claim_b": "Preserved v0.1.7section stillsayslastknownpercentageonly.",
  "sources": [
    "SRC-0028",
    "SRC-0052",
    "SRC-0047"
  ],
  "best_supported_interpretation": "Versionedhistoricalsections,not two current implementations; v0.1.9code authoritative.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-008 — 61trialsummary versus laterresultdirectorygrowth

```json
{
  "id": "CON-008",
  "title": "61trialsummary versus laterresultdirectorygrowth",
  "claim_a": "Refinementfindings61configurations53complete8failed.",
  "claim_b": "Laterprobe/comparisonresultfilesaddmoreoutcomes.",
  "sources": [
    "SRC-1629",
    "SRC-0799"
  ],
  "best_supported_interpretation": "61isphase1–3 historicalsweep count; inventory current trial records separately.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-009 — Metadata version versus startup version

```json
{
  "id": "CON-009",
  "title": "Metadata version versus startup version",
  "claim_a": "CEE startup1.130.285.",
  "claim_b": "Reviewmetadata1.211.5.",
  "sources": [
    "SRC-0874",
    "SRC-0109"
  ],
  "best_supported_interpretation": "Differentversionnamespacespossible; notresolvedtoadeploymentmapping.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-010 — CAPS2algorithm claimed driven by averagecentipawnloss

```json
{
  "id": "CON-010",
  "title": "CAPS2algorithm claimed driven by averagecentipawnloss",
  "claim_a": "Olddocinfersmathematicaldependencyfromfields.",
  "claim_b": "Schemaonlydeclaresthatbothmetricsarepresent.",
  "sources": [
    "SRC-2047",
    "SRC-0335"
  ],
  "best_supported_interpretation": "ExactCAPS2transformunknown; old causalassertionnotverified.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-011 — Native GameRatingV2 versus compatibility alias

```json
{
  "id": "CON-011",
  "title": "Native GameRatingV2 versus compatibility alias",
  "claim_a": "Page shows gameRatingV2field.",
  "claim_b": "Extension may fillitwithnativeeffectiveRating.",
  "sources": [
    "SRC-2047",
    "SRC-0049"
  ],
  "best_supported_interpretation": "UIfieldpresenceisnotproofV2algorithmran; diagnosticsratingSourcesisnecessary.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-012 — Rangeprobe onebyte versus fullasset size

```json
{
  "id": "CON-012",
  "title": "Rangeprobe onebyte versus fullasset size",
  "claim_a": "Probe-results206size1.",
  "claim_b": "Savedenginesaremegabytes.",
  "sources": [
    "SRC-0203",
    "SRC-0202"
  ],
  "best_supported_interpretation": "curl-r0-0explicitlyrequestedonebyte; notcorruption.",
  "resolution_status": "documented; originals preserved"
}
```

## CON-013 — Current docs reference missing old workspaces

```json
{
  "id": "CON-013",
  "title": "Current docs reference missing old workspaces",
  "claim_a": "Uploadsreferencechess-eval-bar/,raw/,tools/,crosscheck/,CLIENT-SIDE.md.",
  "claim_b": "Thosepathsarenotallpresentinoriginalsnapshot.",
  "sources": [
    "SRC-2047",
    "SRC-2048"
  ],
  "best_supported_interpretation": "Preservereferencesandmarkunavailable; donotclaimthoseofflineproofswerere-run.",
  "resolution_status": "documented; originals preserved"
}
```

## Duplicate content groups

[Source manifest](audit-metadata/source-manifest.json) retains same_content_source_ids for every checksum match,including archive-member versions. No overwritten documentation is used to reconcile conflicts.
