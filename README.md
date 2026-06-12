# SCH - Schmidt Nachtraege zum Sanskrit-Woerterbuch

<!-- BEGIN MANUAL: overview -->
SCH is the working repository for Richard Schmidt's *Nachtraege zum
Sanskrit-Woerterbuch*, a continuation/supplement related to the Petersburger
Woerterbuch tradition.  The canonical CDSL source text lives in
[`csl-orig/v02/sch/sch.txt`](https://github.com/sanskrit-lexicon/csl-orig/blob/master/v02/sch/sch.txt);
this repository keeps correction work for Greek fragments, literary-source
markup, link targets, metadata, and issue-specific batches.

## Primary data

| Item | Location | Notes |
|---|---|---|
| Canonical CDSL source | `csl-orig/v02/sch/sch.txt` | Target of accepted corrections. |
| Source metadata | `sch-meta2.txt`, `sch.dtd` | Coding conventions and validation context. |
| Printed-source files | `SCH-Nachtraege.doc`, `.htm`, `.pdf`; `schmidt_orig_utf8.txt` | Source and conversion evidence. |
| Tree/export notes | `Cologne-sch-tree.txt` | Historical generated-file layout. |

## Directories

| Path | Purpose |
|---|---|
| `greek/` | Small set of Greek text-fragment corrections. |
| `ls/` | Literary-source (`<ls>`) markup and front-matter abbreviation work. |
| `schissues/` | Issue-specific work; for example issue 10 handles Bhagavata Purana link-target standardization. |

## Major workflows

| Workflow | Paths | Result |
|---|---|---|
| Greek fragments | `greek/` | `change_1.txt` style changes validated through `csl-pywork`. |
| Literary-source markup | `ls/` | Large `<ls>` marking pass using front-matter lists and PW/PWG bibliography aids. |
| Link target cleanup | `schissues/issue*/` | Issue-local scripts, summaries, and change files. |

## How work is done

SCH work usually starts from a snapshot of `csl-orig/v02/sch/sch.txt`, creates
`temp_sch_*.txt` stages, generates change files, and validates by rebuilding SCH
through `csl-pywork`:

```text
csl-orig/sch.txt -> temp_sch_0.txt -> scripts/manual edits -> change_*.txt -> temp_sch_N.txt -> csl-pywork validation
```

Keep the temp/change/log files with the issue folder so a later reviewer can
see both the mechanical change and the reason for it.

## Common commands

Examples from existing notes:

```sh
python diff_to_changes.py temp_sch_0.txt temp_sch_1.txt change_1.txt
python change_ls1.py temp_sch_1.txt front1a.txt change_2.txt freq_ls1a.txt
python updateByLine.py temp_sch_1.txt change_2.txt temp_sch_2.txt
sh generate_dict.sh sch ../../sch
sh xmlchk_xampp.sh sch
```

Most commands assume an XAMPP-style sibling checkout.  Check paths before
rerunning.

## Data format

`sch-meta2.txt` is the local authority for SCH coding conventions.  The source
uses UTF-8, page/column break markers such as `[Page001.1]`, and older
`{#...#}`, `{%...%}`, `{!...!}` coding rather than only XML-like tags.  New
changes should respect those conventions unless an issue explicitly changes the
encoding/model.

## Current status / open questions

- `ls/` contains a large literary-source marking workflow; read the local notes
  before changing `front*.txt` or generated frequency files.
- Some source abbreviations were resolved by comparison with PW/PWG bibliography
  inputs; keep those provenance links visible.
- Issue folders are the safest starting point for recent link-target changes.
<!-- END MANUAL: overview -->

## Issues

This repository uses the Sanskrit Lexicon unified issue taxonomy with:
- **9 type labels**: link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **3 severity levels**: minor, medium, hard
- **4 milestones**: Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

## GitHub Issue Conventions

All issues follow the unified taxonomy. See [CLAUDE.md](CLAUDE.md) for details.

---
*Updated by Cologne Issue Runbook*
