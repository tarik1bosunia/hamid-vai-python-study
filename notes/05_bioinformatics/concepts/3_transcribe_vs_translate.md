# transcription and translation

## 🧬 DNA → RNA → Protein

This is the **central dogma of molecular biology** — how genetic information flows inside cells.

```
DNA  --(transcription)-->  RNA  --(translation)-->  Protein
```

---

## 🧫 1️⃣ Transcription

🧠 **Definition:**

> Transcription is the process of copying a DNA sequence into an RNA sequence.

* In DNA, bases are **A, T, G, C**
* In RNA, bases are **A, U, G, C** (U replaces T)

So:

```
DNA:  G A T C G A T G G G C C T
RNA:  G A U C G A U G G G C C U
```

🧰 **In Biopython:**

```python
from Bio.Seq import Seq

dna = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
rna = dna.transcribe()
print(rna)
```

**Output:**

```
GAUCGAUGGGCCUAUAUAGGAUCGA...  (T → U)
```

💬 **In real cells:**

* RNA polymerase enzyme reads DNA and makes **mRNA (messenger RNA)**.
* mRNA carries the genetic “message” to ribosomes for protein synthesis.

---

## 🔠 2️⃣ Translation

🧠 **Definition:**

> Translation is the process of converting the RNA sequence into a **protein** (chain of amino acids).

* Every 3 RNA bases = **1 codon**
* Each codon → 1 amino acid (using the **genetic code**)

Example codons:

| RNA Codon     | Amino Acid         |
| ------------- | ------------------ |
| AUG           | Methionine (Start) |
| GGG           | Glycine            |
| UAA, UAG, UGA | Stop codons        |

🧰 **In Biopython:**

```python
protein = rna.translate()
print(protein)
```

**Output:**

```
DRWALKDRKIA...
```

(each letter represents an amino acid)

---

## 🧩 3️⃣ Summary Flow

| Step              | Input           | Output              | Process                       |
| ----------------- | --------------- | ------------------- | ----------------------------- |
| **Transcription** | DNA (`ATGC...`) | RNA (`AUGC...`)     | Replace T → U                 |
| **Translation**   | RNA (`AUG...`)  | Protein (`MGLA...`) | Convert codons to amino acids |

---

## 🧠 Example Full Code

```python
from Bio.Seq import Seq

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("DNA :", dna)

rna = dna.transcribe()
print("RNA :", rna)

protein = rna.translate()
print("Protein :", protein)
```

🧾 **Output:**

```
DNA : ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG
RNA : AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
Protein : MAIVMGR*KGAR*
```

> `*` means a stop codon — the end of the protein chain.

---

## 🧠 TL;DR

| Term                 | Description     | Example                  |
| -------------------- | --------------- | ------------------------ |
| **Transcription**    | DNA → RNA       | `ATG` → `AUG`            |
| **Translation**      | RNA → Protein   | `AUG` → `Methionine (M)` |
| **Biopython method** | `.transcribe()` | `.translate()`           |
