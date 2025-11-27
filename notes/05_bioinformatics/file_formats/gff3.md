# 📘 **Complete Guide to GFF3 Files (General Feature Format Version 3)**

GFF3 is one of the most important file formats in bioinformatics for representing **genome annotations**, including genes, transcripts, exons, UTRs, CDS regions, and regulatory features. This document explains GFF3 in depth.

---

# 🔍 **What is a GFF3 File?**

A GFF3 file is a **tab‑delimited text file** that describes features on a genome. It follows a strict standardized structure defined by the **Sequence Ontology**.

Typical content:

* Genes
* Transcripts (mRNA, ncRNA)
* Exons / Introns
* CDS (coding regions)
* 5'UTR / 3'UTR
* Promoters, enhancers, regulatory elements
* Protein features

GFF3 files are used in:

* Ensembl
* NCBI RefSeq
* UCSC Genome Browser
* MAKER, AUGUSTUS, BRAKER
* BLAST, BEDTools, GATK pipelines

---

# 🧬 **GFF3 File Structure**

Each feature is represented by **9 columns**, separated by TAB characters:

```
seqid   source   type   start   end   score   strand   phase   attributes
```

Below is a detailed explanation.

---

## 1️⃣ **seqid**

The chromosome or contig the feature belongs to.
Examples:

* `chr1`
* `1`
* `CM000001.1`

---

## 2️⃣ **source**

The tool, software pipeline, or database providing the annotation.

Examples:

* `Ensembl`
* `RefSeq`
* `AUGUSTUS`
* `maker`

---

## 3️⃣ **type**

Feature type, defined by **Sequence Ontology (SO)**.

Common types:

* `gene`
* `mRNA`
* `exon`
* `CDS`
* `five_prime_UTR`
* `three_prime_UTR`
* `intron`
* `promoter`

---

## 4️⃣ **start** & 5️⃣ **end**

Genomic coordinates (1‑based inclusive).

Example:

* `start = 100`
* `end   = 500`

This means the feature spans 100 → 500.

---

## 6️⃣ **score**

Numeric value or `.` if not applicable.
Examples:

* BLAST alignment score
* Prediction confidence
* Gene-finder evidence score

---

## 7️⃣ **strand**

Feature orientation:

* `+` forward strand
* `-` reverse strand
* `.` unknown

---

## 8️⃣ **phase** (CDS only)

Defines where the next codon begins.

* `0` → CDS starts at first base of codon
* `1` → CDS starts at second base
* `2` → CDS starts at third base
* `.` → not CDS

---

## 9️⃣ **attributes field**

A semicolon-separated list of key=value tags.

Common tags:

* `ID=` → unique identifier
* `Parent=` → links features to their parent
* `Name=` → human-readable label
* `biotype=` → protein_coding / miRNA / lncRNA
* `gene_id=` → gene identifier

Example:

```
ID=gene:TP53;Name=TP53;biotype=protein_coding
```

---

# 🧬 **GFF3 Example (Gene → Transcript → Exons)**

```
##gff-version 3
chr17  Ensembl  gene     7565097  7590856  .  +  .  ID=gene:TP53;Name=TP53;biotype=protein_coding
chr17  Ensembl  mRNA     7565097  7590856  .  +  .  ID=transcript:TP53-201;Parent=gene:TP53
chr17  Ensembl  exon     7565097  7565194  .  +  .  Parent=transcript:TP53-201
chr17  Ensembl  CDS      7565097  7565194  .  +  0  Parent=transcript:TP53-201
```

Hierarchy:

```
gene
 └── mRNA (transcript)
      ├── exon
      └── CDS
```

---

# 🧬 **Parent–Child Hierarchy in GFF3**

GFF3 uses explicit relationships:

* Gene has **transcripts**
* Transcript has **exons**, **UTRs**, **CDS**

Example:

```
ID=gene1
  Parent=gene1 → mRNA1
    Parent=mRNA1 → exon1, exon2, CDS1
```

This structure allows software to reconstruct gene models accurately.

---

# 🧯 **Comments in GFF3**

Lines starting with `#` are comments.
Examples:

```
# This is a comment
##gff-version 3
##sequence-region chr1 1 248956422
```

---

# 🧪 **GFF3 vs GTF**

| Feature          | GFF3               | GTF           |
| ---------------- | ------------------ | ------------- |
| Attribute format | `key=value`        | `key "value"` |
| Hierarchy        | explicit ID/Parent | implicit      |
| Standardization  | high               | low           |
| Readability      | easier             | harder        |
| Used by          | Ensembl, MAKER     | RNA-seq tools |

**GFF3 is more structured and modern.**

---

# 🛠️ **Tools for Working with GFF3**

### Command-line

* **bedtools**
* **samtools**
* **gffread**
* **agat** toolkit

### Programming

* **Python:** `gffutils`, `Biopython`
* **R:** `rtracklayer`

### Browsers

* IGV
* UCSC Genome Browser
* Ensembl Genome Browser

---

# 🧪 **Validating GFF3 Files**

GFF3 must follow strict rules:

* No spaces
* Tabs only
* Attributes must have `key=value`
* Parent IDs must exist

Validation tools:

* **AGAT** (`agat_convert_sp_gff2gff3.pl`)
* **Galaxy** GFF3 validator
* **NCBI validator**

---

# 🔗 **Useful Resources**

* Ensembl GFF3 Spec: [https://useast.ensembl.org/info/website/upload/gff3.html](https://useast.ensembl.org/info/website/upload/gff3.html)
* Sequence Ontology: [http://www.sequenceontology.org/](http://www.sequenceontology.org/)
* GFF3 Specification: [https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)

---

# 🎯 **Summary**

A GFF3 file is a structured genome annotation format with:

* 9 mandatory fields
* parent-child relationships
* support for genes, transcripts, exons, CDS, UTRs, regulatory elements
* broad usage across genomics tools

GFF3 is clear, powerful, and essential for genome annotation.

---

If you want, I can add:

* A diagram showing gene → transcript → exon → CDS
* A fully annotated real TP53 GFF3 block
* A Python example to parse GFF3 using `gffutils`
