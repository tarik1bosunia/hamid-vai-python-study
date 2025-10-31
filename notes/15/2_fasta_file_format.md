# FASTA File Format: Detailed Explanation: [see in wikipedia](https://en.wikipedia.org/wiki/FASTA_format)

## Overview

The **FASTA file format** is a simple, text-based standard used to represent biological sequences such as DNA, RNA, or proteins. It was first introduced with the **FASTA program** by Lipman and Pearson in 1985 and has since become the most widely used format in bioinformatics.

---

## Structure of a FASTA File

A FASTA file is composed of **one or more records**, and each record contains two main parts:

1. **Header line (definition line)**
2. **Sequence lines**

### 1. Header Line

* The header line **always starts with a '>' symbol**.
* It provides an **identifier** (ID) and an **optional description**.

**Syntax:**

```
>identifier optional_description
```

**Example:**

```
>gene1 Homo sapiens hemoglobin beta chain
```

| Component                            | Description                         |
| ------------------------------------ | ----------------------------------- |
| `>`                                  | Indicates the start of a new record |
| `gene1`                              | Unique identifier for the sequence  |
| `Homo sapiens hemoglobin beta chain` | Optional description or annotation  |

> Note: Most bioinformatics tools treat only the **first word** (before the first space) as the sequence ID.

---

### 2. Sequence Lines

* These lines contain the **biological sequence data**.
* Characters used depend on the molecule type:

  * **DNA/RNA:** A, T, G, C, U, and N (N = any nucleotide)
  * **Protein:** 20 amino acid single-letter codes (A, R, N, D, etc.)
* Sequences can be written on a **single line** or **wrapped over multiple lines**.
* FASTA is **case-insensitive** (A = a).

**Example:**

```
ATGCTAGCAGTACGATCGATCGTAGCTAGCTAGC
```

---

## Example of a Multi-Record FASTA File

```
>gene1 Homo sapiens hemoglobin beta chain
ATGCTAGCAGTACGATCGATCGTAGCTAGCTAGC
>gene2 Mus musculus hemoglobin alpha chain
ATTTGCGCGTTATGCGATGCTAGCGATCGTAACT
>gene3 Drosophila melanogaster opsin gene
GGCTTACGATCGATGCTGATGCTAGCTAGCTGAC
```

This file contains **three sequence records**.

---

## File Extensions and Conventions

| Extension | Description                            |
| --------- | -------------------------------------- |
| `.fasta`  | General FASTA file                     |
| `.fa`     | Shortened version (common for genomes) |
| `.fna`    | Nucleic acid sequences                 |
| `.faa`    | Amino acid (protein) sequences         |
| `.ffn`    | CDS (coding DNA sequence) features     |
| `.frn`    | RNA sequences                          |

---

## FASTA Header Variants

Different databases may include metadata in the header, separated by pipes (`|`) or key-value pairs.

**Examples:**

```
>sp|P68871|HBB_HUMAN Hemoglobin subunit beta OS=Homo sapiens GN=HBB
>lcl|GeneID:1017|Homo sapiens hemoglobin alpha chain
```

| Code  | Meaning          |                           |
| ----- | ---------------- | ------------------------- |
| `sp   | `                | Swiss-Prot database entry |
| `lcl  | `                | Local identifier          |
| `OS=` | Organism species |                           |
| `GN=` | Gene name        |                           |

---

## Comments in FASTA

Lines beginning with a semicolon `;` are **comments** (rarely used in modern practice).

Example:

```
; this is a comment line
>gene1
ATGCATGC
```

---

## FASTA vs FASTQ

| Feature             | FASTA                                  | FASTQ                     |
| ------------------- | -------------------------------------- | ------------------------- |
| Contains            | Sequence only                          | Sequence + Quality scores |
| Header symbol       | `>`                                    | `@`                       |
| Quality information | ❌ No                                   | ✅ Yes                     |
| Typical use         | Reference databases, assembled genomes | Raw sequencing reads      |

---

## Reading FASTA Files in Python (Biopython)

```python
from Bio import SeqIO

for record in SeqIO.parse('genes.fasta', 'fasta'):
    print(record.id)
    print(record.description)
    print(record.seq)
```

**Output:**

```
gene1
gene1 Homo sapiens hemoglobin beta chain
ATGCTAGCAGTACGATCGATCGTAGCTAGCTAGC
```

---

## Key Properties Summary

| Feature             | Description                  |
| ------------------- | ---------------------------- |
| File Type           | Plain text                   |
| Header Symbol       | `>`                          |
| Sequence Characters | DNA, RNA, or Protein letters |
| Case Sensitivity    | Not sensitive                |
| Sequence Wrapping   | Allowed                      |
| Multiple Records    | Allowed                      |
| Comments            | Optional (`;`)               |

---

## Summary

> The **FASTA format** is a simple, human-readable standard for representing biological sequences. Each record starts with a `>` header line followed by the sequence itself. Despite its simplicity, it remains the **most universal format** for biological databases and sequence analysis tools.
