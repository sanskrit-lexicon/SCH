# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**SCH** is the corrections and research repository for the Cologne digitization of Schmidt's *Nachträge zum Sanskrit-Wörterbuch* (Supplement to the Sanskrit Dictionary, 1928). The canonical source lives in `csl-orig/v02/sch/sch.txt`.

## Architecture

| File/Directory | Purpose |
|---|---|
| `schissues/` | Per-issue correction workflows (`issueNNN/` pattern) |
| `greek/` | Greek loanword and citation research |
| `ls/` | Literary source link research |
| `sch.dtd` | DTD for the SCH XML format |
| `schmidt_orig_utf8.txt` | Original digitization in UTF-8 encoding |
| `change_01_utf8.txt` | Change file for the original UTF-8 version |
| `sch-meta2.txt` | Metadata (page count, entry count, etc.) |
| `SCH-Nachtraege.{doc,htm,pdf}` | Schmidt Nachträge supplementary material |
| `Cologne-sch-tree.txt` | Directory tree of the SCH Cologne installation |
| `VideoTutorials.txt` | Notes on video tutorial recordings |

### Issue correction pattern (`schissues/issueNNN/`)

Each issue folder follows the standard workflow:
1. Copy current `sch.txt` to a local `temp_sch_0.txt` (not tracked by git)
2. Apply corrections incrementally as `temp_sch_1.txt`, `temp_sch_2.txt`, etc.
3. Rebuild XML with `generate_dict.sh` and validate with `xmlchk_xampp.sh`
4. Commit the corrected file to `csl-orig`, then sync to Cologne
5. Commit issue documentation back here

## Common Commands

### Apply line-level corrections
```bash
python updateByLine.py <input_file> <changein_file> <output_file>
```

### Rebuild and validate XML (from `csl-pywork/v02/`)
```bash
sh generate_dict.sh sch ../../SCHScan/2020
sh xmlchk_xampp.sh sch
```

## Dependencies

- **Python 3**
- **sch.txt** — in `$BASE/cologne/csl-orig/v02/sch/sch.txt`
