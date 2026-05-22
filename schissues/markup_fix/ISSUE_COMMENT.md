### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `sch.txt`.

I ran the same two-job recipe over `csl-orig/v02/sch/sch.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `schissues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `sch.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<ls> word </ls>` | `<ls>word</ls>` |
| `<sup> word </sup>` | `<sup>word</sup>` |
| `<lang> word </lang>` | `<lang>word</lang>` |

Whitespace trimming applies to all 4 paired tag(s) in `sch.txt`: `<ls>`, `<sup>`, `<lang>`, `<ab>`. The original file is never modified — output goes to `sch_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). **Output is byte-identical to source** (no auto-fixes triggered).

### Closing-tag inventory in current `sch.txt`

| Tag | Count |
|---|---:|
| `</ls>` | 31 |
| `</041)>` | ? |
| `</sup>` | 1 |
| `</699)>` | ? |
| `</lang>` | 5 |
| `</ab>` | 2 |

### What it found in current `sch.txt`

- 0 whitespace trims — byte-identical to source.
- 2 within-line `<ab n="…">` non-standard expansion matches: `n="DHĀTUPĀṬHA"` — an abbreviation used in 2 instances. Decide whether to retain or standardise.
- 0 adjacent `</ab> <ab>` (only 2 `<ab>` tags in the entire file).
- 37 `{{old → new || …}}` correction records present.

### Usage

```
cd schissues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/sch/sch.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `sch_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

<ab> appears only twice; <ls> is the primary paired tag.

### Severity

`minor`
