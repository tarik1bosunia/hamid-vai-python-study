# 🧬 Day 13: Biological Sequences — DNA & RNA as Strings

Biological data such as DNA and RNA can be represented and processed in Python using **strings**.
This lesson covers how to manipulate nucleotide sequences, count bases, and extract codons.

---

## 🔹 1. Representing DNA and RNA Sequences

DNA and RNA are composed of **nucleotides**, represented by letters:

* DNA → `A`, `T`, `C`, `G`
* RNA → `A`, `U`, `C`, `G`

### Example — Representing DNA as a String

```python
dna = "ATGCGTACGTAGCTAGCTA"
print("DNA Sequence:", dna)
```

---

## 🔹 2. Counting Nucleotides

You can count occurrences of each base using the `.count()` string method.

```python
dna = "ATGCGTACGTAGCTAGCTA"

print("Adenine (A):", dna.count('A'))
print("Thymine (T):", dna.count('T'))
print("Cytosine (C):", dna.count('C'))
print("Guanine (G):", dna.count('G'))
```

🧠 You can also compute **GC content** — an important biological metric:

```python
gc_content = (dna.count('G') + dna.count('C')) / len(dna) * 100
print(f"GC Content: {gc_content:.2f}%")
```

---

## 🔹 3. Transcription — DNA → RNA

In transcription, **Thymine (T)** is replaced with **Uracil (U)**.

```python
rna = dna.replace('T', 'U')
print("RNA Sequence:", rna)
```

**Output:**

```
RNA Sequence: AUGCGUACGUAGCUAGCUA
```

---

## 🔹 4. String Slicing for Codons

A **codon** is a group of 3 nucleotides that codes for one amino acid.

You can slice your DNA sequence every 3 characters.

```python
dna = "ATGCGTACGTAGCTAGCTA"
codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
print(codons)
```

**Output:**

```
['ATG', 'CGT', 'ACG', 'TAG', 'CTA', 'GCT', 'A']
```

🧠 Note: The last codon may be incomplete if the total length isn’t a multiple of 3.

---

## 🔹 5. Reverse Complement (Bonus)

In DNA, bases pair as follows:

* `A ↔ T`
* `C ↔ G`

The **reverse complement** is obtained by reversing the sequence and swapping each base.

```python
complement = dna.translate(str.maketrans('ATCG', 'TAGC'))
reverse_complement = complement[::-1]

print("Complement:", complement)
print("Reverse Complement:", reverse_complement)
```

---

## 🔹 6. Practical Tasks

1. Count nucleotide frequency for a given DNA sequence.
2. Convert DNA → RNA using string replacement.
3. Extract codons using slicing.
4. Compute GC content of any DNA string.
5. Find reverse complement using `translate()` and slicing.
6. Write a function `is_valid_dna(seq)` that checks if a sequence contains only A, T, C, G.

---

## ✅ Summary

| Concept            | Description                | Example               |
| ------------------ | -------------------------- | --------------------- |
| DNA as string      | Letters `A`, `T`, `C`, `G` | `'ATGCGA'`            |
| Count nucleotides  | `.count()` method          | `dna.count('A')`      |
| Transcription      | `replace('T', 'U')`        | `'AUGCGA'`            |
| Codons             | Groups of 3 bases          | `['ATG', 'CGA', ...]` |
| Reverse Complement | Base pairing rule          | `A↔T`, `C↔G`          |
| GC Content         | % of G & C bases           | `(G+C)/total * 100`   |

---

### 💡 Example Exercise

Write a Python program that:

1. Takes a DNA sequence as input.
2. Prints its RNA equivalent.
3. Displays codons and GC content.
4. Shows the reverse complement.

```python
dna = input("Enter a DNA sequence: ").upper()
rna = dna.replace('T', 'U')
codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
gc = (dna.count('G') + dna.count('C')) / len(dna) * 100
reverse_complement = dna.translate(str.maketrans('ATCG', 'TAGC'))[::-1]

print(f"\nRNA: {rna}")
print(f"Codons: {codons}")
print(f"GC Content: {gc:.2f}%")
print(f"Reverse Complement: {reverse_complement}")
```
