# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**SCH** is the development and correction repository for **Richard Schmidt's *Nachträge zum Sanskrit-Wörterbuch in kürzerer Fassung***, a supplement (Nachträge) to the abridged Petersburg dictionary (PWK), within the [Cologne Digital Sanskrit Lexicon](https://www.sanskrit-lexicon.uni-koeln.de/) (CDSL).

- **Canonical source text**: [`csl-orig/v02/sch/sch.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/main/v02/sch/sch.txt) (28,455 entries) — corrections are applied to that file, not stored here.
- This repository holds **development artifacts**: corrections, markup, comparison, and per-issue working files.
- An addenda volume continuing PWK with words and citations not in the original; entries are keyed to the Petersburg tradition.

## Architecture

| Path | Purpose |
|---|---|
| `.github/` | GitHub Actions workflows + issue templates |
| `greek/` | `greek/` working files |
| `ls/` | `ls/` working files |
| `schissues/` | `schissues/` working files |

## Key commands

Corrections follow the CDSL `updateByLine.py` pattern, applied against the csl-orig source:

```sh
python updateByLine.py <input> <changefile> <output>
```

Change-file format (paired lines; `;`-prefixed comments):

```
1234 old <original line>
1234 new <replacement line>
```
Supports `new` (replace), `ins` (insert after), `del` (delete). All files UTF-8 (**no BOM**).

## Data format

SCH entries use standard CDSL Sanskrit-lexicography markup. See [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for the full tag reference.

| Tag | Role |
|---|---|
| `<L>NNNN<pc>PPP` | Entry begin, with print page-column ref |
| `<k1>`, `<k2>` | Primary / secondary headword (SLP1) |
| `<LEND>` | Entry end |
| `{#…#}` | Sanskrit text (SLP1) |
| `{%…%}` | German gloss / italic display text |
| `¦` | Headword / definition separator |
| `<lex>…</lex>` | Lexical category |
| `<ls>…</ls>` | Literary source citation |

Annotated example — the first entry of `sch.txt`:

```
<L>1<pc>001-1<k1>a<k2>a˚
2. {%a˚%}¦ , {%asvaptum%} <ls>Tāṇḍya-Br. 10,4,4.</ls> {part=,seq=1,type=,n=1}
<LEND>
```

## Dependencies

- Python 3 (correction and comparison scripts).
- No build step in this repo; XML and web display are generated centrally from `csl-orig` via `csl-pywork`.

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.