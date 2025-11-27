# 🧬 Day 14: Practice Project — Nucleotide Counter (FASTA-like Sequence)

In this practice project, you’ll write a Python script to **count nucleotides** (A, T, C, G, and others) from a **FASTA-like sequence**.

This will help reinforce string manipulation, file reading, and dictionary usage.

---

## 📘 What is a FASTA File?

A **FASTA** file stores biological sequences (DNA, RNA, or protein) in plain text format.

### Example of a FASTA-like file:

```
>Sequence_1
ATGCTAGCTAGCTAGCTAGCTAGCTAACG
```

* The first line starts with `>` (description or ID)
* The following lines contain the **sequence** itself

---

## 🎯 Objective

Write a script that:

1. Reads a FASTA-like input string or file.
2. Extracts the DNA sequence (ignoring the `>` header).
3. Counts occurrences of each nucleotide (A, T, G, C).
4. Handles unexpected characters (e.g., `N`, `X`, `-`).
5. Prints results in a clean format.

---

## 🧩 Step 1 — Input FASTA-like Sequence

You can simulate a FASTA file as a multiline string:

```python
fasta_data = ">seq1\nATGCTAGCTAGCTAGCTAGCTAGCTAACG"
```

Or read from a file:

```python
with open('sequence.fasta', 'r') as f:
    fasta_data = f.read()
```

---

## 🧩 Step 2 — Extract Sequence (Ignore Header)

```python
lines = fasta_data.strip().split('\n')
sequence = ''.join(line for line in lines if not line.startswith('>')).upper()
print(sequence)
```

**Output:**

```
ATGCTAGCTAGCTAGCTAGCTAGCTAACG
```

---

## 🧩 Step 3 — Count Nucleotides Using a Dictionary

```python
counts = {}
for base in sequence:
    counts[base] = counts.get(base, 0) + 1

print(counts)
```

**Output:**

```
{'A': 7, 'T': 6, 'G': 5, 'C': 7}
```

---

## 🧩 Step 4 — Display Results Nicely

```python
print("\nNucleotide Counts:")
for base in sorted(counts):
    print(f"{base}: {counts[base]}")
```

**Output:**

```
Nucleotide Counts:
A: 7
C: 7
G: 5
T: 6
```

---

## 🧩 Step 5 — Handle Ambiguous Bases (like `N`)

```python
sequence = "ATGCNNNATG--CGA"

valid_bases = {'A', 'T', 'G', 'C'}
counts = {base: sequence.count(base) for base in valid_bases}
invalids = [base for base in sequence if base not in valid_bases]

print("Base Counts:", counts)
print("Invalid Characters:", set(invalids))
```

**Output:**

```
Base Counts: {'A': 2, 'T': 2, 'G': 2, 'C': 2}
Invalid Characters: {'N', '-'}
```

---

## 🧠 Step 6 — Compute GC Content

```python
gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
print(f"GC Content: {gc_content:.2f}%")
```

---

## 🧠 Step 7 — Combine Everything Into One Script

```python
def count_nucleotides(fasta_text):
    lines = fasta_text.strip().split('\n')
    sequence = ''.join(line for line in lines if not line.startswith('>')).upper()

    valid_bases = ['A', 'T', 'G', 'C']
    counts = {base: sequence.count(base) for base in valid_bases}

    total = len(sequence)
    gc_content = (counts['G'] + counts['C']) / total * 100 if total > 0 else 0

    print("Nucleotide Counts:")
    for base in valid_bases:
        print(f"{base}: {counts[base]}")

    print(f"\nGC Content: {gc_content:.2f}%")

# Example run
data = ">seq1\nATGCTAGCTAGCTAGCTAGCTAGCTAACG"
count_nucleotides(data)
```

**Output:**

```
Nucleotide Counts:
A: 7
T: 6
G: 5
C: 7

GC Content: 44.44%
```

---

## 🧠 Bonus Ideas

* Accept FASTA filename as a command-line argument.
* Handle multi-sequence FASTA files.
* Visualize nucleotide frequencies using `matplotlib`.
* Add reverse complement and transcription functions.

---

## ✅ Learning Outcomes

By completing this project, students will:

* Understand FASTA structure.
* Practice file and string manipulation.
* Use dictionaries and loops efficiently.
* Apply GC-content formula in code.
* Build a reusable function for biological analysis.

---
