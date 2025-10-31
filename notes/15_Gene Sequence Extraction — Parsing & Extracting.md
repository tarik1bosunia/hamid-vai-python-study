# 🧬 Day 15: Gene Sequence Extraction — Parsing & Extracting (Notebook 5)

Today you'll learn how to **parse gene data** from text/FASTA-like inputs and **extract specific sequences** by ID, coordinates, or motif. We'll do it first with **pure Python** (no extra libraries), then show an optional **Biopython** approach.

---

## 📦 Input Formats You’ll See

* **FASTA** (most common):

  ```
  >gene1 description here
  ATGCTAGCTAGCTAGC
  >gene2 another description
  ATTTGCGCGATTA
  ```
* **Tabular** (CSV/TSV) annotation: gene id, start, end, strand, etc.
* **Plain text** with IDs and sequences.

---

## ✅ 1) Parse Multi‑FASTA with Pure Python

Goal: Read text, **collect records** into a dict `{id: sequence}`.

```python
def parse_fasta(fasta_text: str) -> dict:
    records = {}
    header = None
    seq_parts = []
    for line in fasta_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('>'):
            # save previous record
            if header is not None:
                records[header] = ''.join(seq_parts).upper()
            # new header: take first token as id
            header = line[1:].split()[0]
            seq_parts = []
        else:
            seq_parts.append(line)
    # save last
    if header is not None:
        records[header] = ''.join(seq_parts).upper()
    return records

# Example
fasta_text = ">gene1 desc\nATGC\nTAGC\n>gene2\nATTTGCGC"
records = parse_fasta(fasta_text)
print(records)  # {'gene1': 'ATGCTAGC', 'gene2': 'ATTTGCGC'}
```

---

## ✅ 2) Extract by Gene ID

```python
def get_sequence(records: dict, gene_id: str) -> str | None:
    return records.get(gene_id)

seq = get_sequence(records, 'gene2')
print(seq)  # ATTTGCGC
```

---

## ✅ 3) Extract by Coordinates (Start–End, 1‑based)

Useful when you have a **genome** string and annotation coordinates.

```python
def slice_by_coords(sequence: str, start: int, end: int, strand: str = '+') -> str:
    """Return subsequence [start..end] inclusive (1-based). If strand is '-', return reverse complement."""
    # Convert to 0-based Python slice; end is inclusive
    sub = sequence[start-1:end]
    if strand == '-':
        tbl = str.maketrans('ATCGNatcgn', 'TAGCNtagcn')
        sub = sub.translate(tbl)[::-1]
    return sub

# Example
genome = "ATGCTAGCTAGCTAGC"
print(slice_by_coords(genome, 3, 8, '+'))  # GCTAGC
print(slice_by_coords(genome, 3, 8, '-'))  # GCTAGC reverse‑complemented
```

---

## ✅ 4) Find by Motif/Pattern (Regex)

Search a sequence for **motifs** (e.g., TATA box, restriction sites).

```python
import re

def find_motifs(seq: str, motif: str) -> list[tuple[int,int,str]]:
    """Return list of (start_1based, end_1based, match_seq). Motif is a regex."""
    hits = []
    for m in re.finditer(motif, seq):
        s, e = m.start()+1, m.end()  # convert to 1-based
        hits.append((s, e, m.group()))
    return hits

seq = "ATGCGATATAGCGCTATAAATATA"
print(find_motifs(seq, r"TATA"))  # [(7, 10, 'TATA'), (17, 20, 'TATA')]
```

> Tip: Turn IUPAC patterns into regex if you have ambiguous bases.

---

## ✅ 5) Extract All ORFs (Simple, 5'→3', Start ATG, Stop TAA/TAG/TGA): [see details: ORF](./15/1_orf.md)
```
The function find_orfs finds Open Reading Frames (ORFs) in a given DNA sequence.

An ORF is a stretch of DNA that:

Starts with a start codon "ATG"

Ends with one of the stop codons: "TAA", "TAG", or "TGA"

Has a length of at least a given number of codons (min_len_codons)
```

```python
def find_orfs(seq: str, min_len_codons: int = 50) -> list[tuple[int,int,str]]:
    stops = {"TAA", "TAG", "TGA"}
    orfs = []
    n = len(seq)
    i = 0
    while i < n-2:
        codon = seq[i:i+3]
        if codon == "ATG":
            j = i+3
            while j < n-2 and seq[j:j+3] not in stops:
                j += 3
            if j < n-2:  # found a stop
                length_codons = (j - i) // 3
                if length_codons >= min_len_codons:
                    orfs.append((i+1, j+3, seq[i:j+3]))  # 1-based inclusive
                i = j+3  # continue after stop codon
                continue
        i += 1
    return orfs

seq = "AAAATGAAACCCGGGTTTTAGCCCATGAAATTTTAA"
print(find_orfs(seq, min_len_codons=2))
```

---

## ✅ 6) Batch Extraction by ID List

```python
def extract_batch(records: dict, ids: list[str]) -> dict:
    return {gid: records[gid] for gid in ids if gid in records}

ids = ["gene2", "geneX"]
records = {
    "gene1": "ATGCTAGC",
    "gene2": "ATTTGCGC"
}
print(extract_batch(records, ids))  # {'gene2': 'ATTTGCGC'}
```

---

## ✅ 7) Write Extracted Sequences to FASTA

```python
def to_fasta(records: dict) -> str:
    lines = []
    for gid, seq in records.items():
        lines.append(f">{gid}")
        # wrap at 60 chars per FASTA convention
        for i in range(0, len(seq), 60):
            lines.append(seq[i:i+60])
    return "\n".join(lines)

print(to_fasta({"gene2": records['gene2']}))
```

---

## 🧪 8) Practical Mini‑Tasks

1. Parse a multi‑FASTA string and print **IDs with sequence lengths**.
2. Given an **ID list**, export only those sequences to a new FASTA.
3. Search a sequence for the motif **`ATG[ATGC]{3}TAA`** and report coordinates.
4. Given a genome and annotation `(start, end, strand)`, extract the gene and compute **GC%**.
5. Extend ORF finder to scan all **three frames** on the `+` strand.

---

## 🧰 9) Optional: Biopython Approach (if allowed)

> Install in Colab: `!pip install biopython`

```python
from Bio import SeqIO
from Bio.Seq import Seq

# Parse FASTA file
records = {rec.id: str(rec.seq) for rec in SeqIO.parse('genes.fasta', 'fasta')}

# Extract by ID
seq = records.get('gene2')

# Reverse complement
revcomp = str(Seq(seq).reverse_complement())

# Write a subset to FASTA
from Bio.SeqRecord import SeqRecord
subset = [SeqRecord(Seq(records[k]), id=k, description="") for k in ['gene1','gene2'] if k in records]
SeqIO.write(subset, 'subset.fasta', 'fasta')
```

---

## ✅ Learning Outcomes

* Parse FASTA strings into usable Python structures.
* Extract sequences by **ID**, **coordinates**, or **motif**.
* Compute reverse complements and scan for **ORFs**.
* Export results back to **FASTA**.

---

### 📌 Notes

* Always **uppercase** sequences (`A/T/G/C`) before analysis.
* When using coordinates from annotation files (GFF/CSV), confirm whether they are **1‑based or 0‑based** and whether **end is inclusive**.
* For minus‑strand genes, **reverse‑complement** the slice.
