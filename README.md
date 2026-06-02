# SCH — Schmidt *Nachträge zum Sanskrit-Wörterbuch* (1928)

Development and correction repository for **Richard Schmidt's *Nachträge zum Sanskrit-Wörterbuch in kürzerer Fassung***, a supplement (Nachträge) to the abridged Petersburg dictionary (PWK), part of the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) (CDSL). The canonical source text lives in [`csl-orig/v02/sch/sch.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/sch/sch.txt) (28,455 entries); this repository holds the development, correction, and enrichment work.

An addenda volume continuing PWK with words and citations not in the original; entries are keyed to the Petersburg tradition.

## Documentation

- [CLAUDE.md](CLAUDE.md) — repository guide and data-format reference.
- [DATA_DICTIONARY.md](DATA_DICTIONARY.md) — markup tag reference.
- [CONTRIBUTING.md](CONTRIBUTING.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Contents

| Path | Purpose |
|---|---|
| `greek/` | `greek/` working files |
| `ls/` | `ls/` working files |
| `schissues/` | `schissues/` working files |

## Timeline

| Period | Activity |
|---|---|
| 2014 | Repository activity begins (first tracked issues) |
| 2017–2024 | Ongoing corrections, markup, and comparison work |
| 2026-05 | Issue taxonomy, citation metadata, documentation |

## Projects & Milestones

| Milestone | Open | Closed | Total |
|---|---|---|---|
| Dictionary to Book | 0 | 0 | 0 |
| Digitization Quality | 0 | 2 | 2 |
| Structured Data | 1 | 5 | 6 |
| Major Enhancements | 3 | 1 | 4 |
| **Total** | **4** | **8** | **12** |

```mermaid
pie showData
  title SCH issues by milestone
  "Digitization Quality" : 2
  "Structured Data" : 6
  "Major Enhancements" : 4
```

## Issues

```mermaid
pie showData
  title SCH issues by type
  "markup" : 5
  "content-enhancement" : 4
  "encoding" : 2
  "question" : 1
```

### Open

| # | Title | Type | Severity | Milestone |
|---|---|---|---|---|
| 4 | 12427 (º) & 3148 (*) Entries | question | minor | Structured Data |
| 6 | Preface, Partial translation | content-enhancement | medium | Major Enhancements |
| 9 | SCH -- AB version for adopting into CDSL system | content-enhancement | medium | Major Enhancements |
| 12 | docs-pass: SCH documentation review | content-enhancement | medium | Major Enhancements |

### Solved

| # | Title | Type | Severity | Milestone |
|---|---|---|---|---|
| 1 | Anglicized Sanskrit Coding Scheme | encoding | minor | Digitization Quality |
| 2 | SCH-Nachträge | content-enhancement | medium | Major Enhancements |
| 3 | [Schµ793] €1 | markup | minor | Structured Data |
| 5 | Changes to sch.txt and sch.xml | markup | minor | Structured Data |
| 7 | greek text | encoding | minor | Digitization Quality |
| 8 | ls markup | markup | minor | Structured Data |
| 10 | BHĀGAVATAPURĀṆA SCH literary source markup | markup | minor | Structured Data |
| 11 | [markup] Minor sch.txt Markup Oddities | markup | minor | Structured Data |

## Labels

### Type labels

| Label | Meaning |
|---|---|
| `link-target` | Click-throughs from `<ls>` abbreviations to scanned PDF pages |
| `link-splitting` | Splitting combined `SOURCE N,N` refs into per-page links |
| `markup` | Normalising XML tag content |
| `text-correction` | Corrections to German/Sanskrit definitions or headwords |
| `content-enhancement` | New material or structural additions beyond correction |
| `encoding` | SLP1/IAST transcoding, character normalisation |
| `scan-quality` | Replacing blurry/skewed/missing scan pages |
| `bug` | Broken links, XML errors, broken downloads |
| `question` | Scholarly questions requiring research |

### Severity labels

| Label | Meaning |
|---|---|
| `minor` | Targeted fix — a handful of lines or a single file |
| `medium` | Standard unit of work — one batch of corrections |
| `hard` | Large effort spanning many sources or files |

## Contributors

| Contributor | Commits |
|---|---|
| gasyoun (Mārcis Gasūns) | 23 |
| funderburkjim | 17 |

## Source

- **Author**: Schmidt, Richard
- **Title**: *Nachträge zum Sanskrit-Wörterbuch in kürzerer Fassung*
- **Place / Publisher**: Leipzig: Otto Harrassowitz
- **Year(s)**: 1928
- **Language pair**: Sanskrit → German
- **Size (CDSL headword index)**: 28,455 entries
- **License (digital edition)**: CC BY-SA 4.0
- See [CITATION.cff](CITATION.cff) for machine-readable citation.

## Encoding

- UTF-8 (NFC) throughout.
- Sanskrit text in SLP1 transliteration, wrapped in `{#…#}`; German gloss / italic display text in `{%…%}`.
- Devanāgarī and IAST display forms are generated at display time, not stored in the source.

## How it works

```mermaid
flowchart LR
  S["Print scan"] -->|keyboarding| O["csl-orig/v02/sch/sch.txt"]
  O -->|updateByLine.py| C["change_*.txt corrections"]
  C --> O
  O -->|csl-pywork build| X["sch.xml"]
  X --> A["csl-app web display"]
```

---
*Issue taxonomy and documentation per the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md).*
