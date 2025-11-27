# 🏁 Day 16: Final Mini‑Project — Gene Sequence Analyzer

Build a small but complete **Gene Sequence Analyzer**. Your tool will:

1. **Load** FASTA‑like data, 2) **Extract** a target sequence by ID, 3) **Count** nucleotides & **GC%**, 4) **Find motifs** (regex), and 5) Print a clean **report**.

> Work in Colab or local. Keep functions small and testable.

---

## 🎯 Requirements

* Parse one or more sequences from a FASTA‑like input (string or file)
* Extract a sequence by **ID** (e.g., `gene2`)
* Compute **nucleotide counts** (A/T/G/C) and **GC content**
* Find **motifs** using regex (user‑provided pattern)
* (Bonus) Reverse complement, coordinate slicing, save report to file

---

## 🧩 Project Scaffold (Copy‑Paste)

```python
import re
from typing import Dict, List, Tuple

# ---------- Parsing ----------
def parse_fasta(text: str) -> Dict[str, str]:
    recs: Dict[str, str] = {}
    head = None
    buf = []
    for raw in text.strip().splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('>'):
            if head is not None:
                recs[head] = ''.join(buf).upper()
            head = line[1:].split()[0]
            buf = []
        else:
            buf.append(line)
    if head is not None:
        recs[head] = ''.join(buf).upper()
    return recs

# ---------- Core analytics ----------
def base_counts(seq: str) -> Dict[str, int]:
    seq = seq.upper()
    return {b: seq.count(b) for b in 'ATGC'}

def gc_content(seq: str) -> float:
    seq = seq.upper()
    total = len(seq) or 1
    return 100.0 * (seq.count('G') + seq.count('C')) / total


def find_motifs(seq: str, pattern: str) -> List[Tuple[int, int, str]]:
    """Return list of (start_1based, end_1based, matched_text)."""
    hits = []
    for m in re.finditer(pattern, seq):
        hits.append((m.start() + 1, m.end(), m.group()))
    return hits

# ---------- Extras ----------
def reverse_complement(seq: str) -> str:
    tbl = str.maketrans('ATCGNatcgn', 'TAGCNtagcn')
    return seq.translate(tbl)[::-1]

# ---------- Reporting ----------
def make_report(gid: str, seq: str, pattern: str) -> str:
    counts = base_counts(seq)
    gc = gc_content(seq)
    motifs = find_motifs(seq, pattern) if pattern else []

    lines = []
    lines.append(f"# Gene Report: {gid}")
    lines.append("")
    lines.append(f"Length: {len(seq)} bp")
    lines.append(f"Counts: A={counts['A']}  T={counts['T']}  G={counts['G']}  C={counts['C']}")
    lines.append(f"GC%: {gc:.2f}%")
    if pattern:
        lines.append(f"Motif pattern: {pattern}")
        lines.append(f"Motif hits: {len(motifs)}")
        for i, (s, e, mtxt) in enumerate(motifs, 1):
            lines.append(f"  {i:>2}. {mtxt} @ {s}-{e}")
    return '\n'.join(lines)

# ---------- CLI‑style runner ----------
def run_analyzer(fasta_text: str, target_id: str, motif_pattern: str = r"") -> str:
    recs = parse_fasta(fasta_text)
    if target_id not in recs:
        raise KeyError(f"ID '{target_id}' not found. Available: {', '.join(recs)}")
    seq = recs[target_id]
    return make_report(target_id, seq, motif_pattern)
```

---

## 🧪 Sample Data & Run

```python
FASTA = ">gene1 desc\nATGCTAGCTAG\n>gene2 sample\nATTTGCGCGATTATATA\n>geneX\nCCCGGGTTTAA"

print(run_analyzer(FASTA, target_id='gene2', motif_pattern=r'TATA'))
```

**Expected output (example):**

```
# Gene Report: gene2

Length: 17 bp
Counts: A=6  T=6  G=3  C=2
GC%: 29.41%
Motif pattern: TATA
Motif hits: 2
   1. TATA @ 12-15
   2. TATA @ 14-17
```

> Note: Overlapping matches are found because regex engines can step forward and match again (e.g., at positions 12–15 and 14–17). Use a **lookahead** to ensure overlaps: `r"(?=(TATA))"` and read `m.start(1)`/`m.end(1)`.

---

## ➕ Optional Add‑Ons (Choose any)

1. **Overlapping motifs** with lookahead:

   ```python
   def find_motifs_overlap(seq: str, pattern: str) -> list[tuple[int,int,str]]:
       hits = []
       for m in re.finditer(fr"(?=({pattern}))", seq):
           s = m.start(1) + 1
           e = m.end(1)
           hits.append((s, e, m.group(1)))
       return hits
   ```
2. **Slice by coordinates** (1‑based; strand‑aware) and analyze the slice.
3. **Reverse‑complement mode**: analyze `revcomp` instead of `seq`.
4. **Export** the report to a text file; save a subset to FASTA.
5. **Validate DNA** (A/T/G/C only) and list invalid symbols.
6. **Plot** base composition with `matplotlib`.

---

## 📋 Rubric (Self‑Check)

* [ ] Parses FASTA correctly (multiple records)
* [ ] Extracts sequence by ID
* [ ] Prints A/T/G/C counts and correct **GC%**
* [ ] Finds motifs with a user pattern
* [ ] Clean, readable functions with docstrings/types
* [ ] Bonus: overlaps / reverse complement / slicing / export

---

## 🧠 Hints & Gotchas

* Always `.upper()` sequences before counting.
* Be explicit about indexing: coordinates shown here are **1‑based inclusive**.
* Regex for DNA sets: `[ATGC]`, any base: `[ACGTN]`.
* For **overlaps**, prefer lookaheads: `(?=(PATTERN))`.

---

## 🏎️ Challenge Modes

* **Pro**: Scan all records for a motif and return a ranked table of top hit counts.
* **Pro**: Sliding‑window GC% across the sequence (window=100, step=10).
* **Pro**: ORF scan (start ATG; stops TAA/TAG/TGA) and report longest ORF.

---

### ✅ What to Submit

* Your `.py` file or notebook with the functions above
* A short run showing the **report** for at least one sequence and one motif
* (Optional) A screenshot of bonus outputs (e.g., plot, overlaps)
