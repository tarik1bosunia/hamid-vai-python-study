# Gene Structure and Transcript Overview

## Introduction

Understanding gene structure is fundamental to molecular biology and bioinformatics. A gene is not simply a continuous coding sequence—it contains multiple regions with distinct functions during transcription and translation. This guide explains the complete structure of eukaryotic genes and their transcripts.

**Why This Matters:**
- RNA-seq analysis and transcript quantification
- Gene expression studies
- Mutation impact prediction
- Drug target identification
- CRISPR guide RNA design

---

## The Complete Gene Structure

### Overview Diagram

```
5'───────────────────────────────────────────────────────────────3'

     Promoter    TSS           Gene Body              TTS    Terminator
        ↓         ↓                                    ↓          ↓
    [====]───────▓▓▓▓▓█████▓▓▓▓▓███▓▓▓▓▓██████▓▓▓▓▓───────[====]
                  ↑    ↑    ↑    ↑   ↑     ↑    ↑
              5'UTR  Exon  Intron CDS Intron Exon 3'UTR

Legend:
[====] = Regulatory regions (promoter, terminator)
▓▓▓▓▓  = Transcribed but not translated (UTRs)
█████  = Coding sequence (CDS) - translated to protein
───    = Introns (spliced out) or intergenic regions
```

---

## Part 1: DNA Level (The Gene)

### 1. Promoter Region

**Location**: Upstream (5') of the transcription start site (TSS)

**Function**:
- Binding site for RNA polymerase and transcription factors
- Controls when and how much the gene is expressed
- Tissue-specific expression patterns

**Key Elements**:
- **TATA box** (TATAAA): ~25-30 bp upstream of TSS
- **CAAT box**: ~80 bp upstream
- **GC box**: Various positions
- **Enhancers**: Can be kb away

**Example**:
```
Position: -100 to -1 (relative to TSS at +1)
Sequence: ...CAAT...TATAAA...GC...
```

### 2. Transcription Start Site (TSS)

**Position**: +1 (by convention)

**Function**: Where RNA polymerase II begins transcription

**Recognition**: Often has Initiator (Inr) sequence: YYANWYY

### 3. 5' Untranslated Region (5'UTR)

**Location**: From TSS to start codon (ATG)

**Length**: Variable, typically 50-500 nucleotides

**Function**:
- Contains ribosome binding site (Kozak sequence in eukaryotes)
- Regulates translation efficiency
- mRNA stability signals

**Kozak Consensus Sequence** (eukaryotes):
```
GCC(A/G)CCAUGG
         ^^^
       Start codon
```

**Example**:
```
5'UTR: GCAGCCACCATG...
                 ^^^
              Start codon begins CDS
```

### 4. Exons

**Definition**: Sequences that remain in mature mRNA after splicing

**Contents**:
- 5'UTR (first exon only)
- CDS (coding sequence)
- 3'UTR (last exon only)

**Number**: Varies widely
- Simple genes: 1 exon (intronless)
- Complex genes: 50+ exons (e.g., titin: 363 exons)

**Average**: ~8-10 exons per human gene

### 5. Introns

**Definition**: Non-coding sequences removed during splicing

**Boundaries**: Always begin with GT and end with AG (GT-AG rule)

```
Exon 1...AG | GT...intron...AG | GT...Exon 2
           ↑  ↑              ↑  ↑
        Splice              Splice
         site               site
```

**Function**:
- Allow alternative splicing (protein diversity)
- Regulate gene expression
- Increase recombination diversity

**Size**: Can be huge (>100 kb in some genes)

### 6. Coding Sequence (CDS)

**Location**: From start codon (ATG) to stop codon (TAA/TAG/TGA)

**Function**: Encodes the amino acid sequence of the protein

**Reading Frame**: Must be read in triplets (codons)

**Example**:
```
CDS: ATGGGCTTCAAGTGA
     |||||||||||||||
     Met Gly Phe Lys STOP
```

**Note**: CDS can span multiple exons (split by introns)

### 7. 3' Untranslated Region (3'UTR)

**Location**: From stop codon to polyadenylation signal

**Length**: Variable, 100-1000+ nucleotides

**Function**:
- mRNA localization
- mRNA stability (half-life)
- MicroRNA binding sites
- Regulation of translation

**Key Signals**:
- **Polyadenylation signal**: AATAAA or ATTAAA
- **Downstream element**: GT-rich or T-rich region

### 8. Transcription Termination Site (TTS)

**Location**: End of transcription

**Includes**: Polyadenylation signal and cleavage site

### 9. Terminator Region

**Location**: Downstream of TTS

**Function**: Signals to RNA polymerase to stop and release

---

## Part 2: RNA Level (The Transcript)

### Pre-mRNA (Primary Transcript)

**Definition**: Initial RNA copy containing both exons and introns

**Processing Steps:**
1. **5' Capping**: 7-methylguanosine cap added to 5' end
2. **Splicing**: Introns removed, exons joined
3. **3' Polyadenylation**: Poly(A) tail (~200 A's) added to 3' end

```
Pre-mRNA:  5'cap-[5'UTR-Exon1-Intron1-Exon2-Intron2-Exon3-3'UTR]-AAAA...
                                  ↓ Splicing
Mature mRNA: 5'cap-[5'UTR-Exon1-Exon2-Exon3-3'UTR]-AAAA...
```

### Mature mRNA Structure

```
5' Cap
   ↓
m7G━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━AAAA...AAA 3'
     ▓▓▓▓▓     █████████████████████     ▓▓▓▓▓
    5'UTR          CDS (ORF)            3'UTR
             
    ↑                                    ↑
  Kozak                           Poly(A) signal
  sequence                        (AAUAAA)
```

**Components**:
1. **5' cap** (m7G): Protects from degradation, aids translation
2. **5'UTR**: Regulatory region before start codon
3. **CDS**: Open reading frame (ORF) - translated region
4. **3'UTR**: Regulatory region after stop codon
5. **Poly(A) tail**: Protects from degradation, aids translation

---

## Part 3: Protein Level

### Translation Process

```
mRNA Codon:     AUG  GGC  UUU  AAG  UGA
                 ↓    ↓    ↓    ↓    ↓
Amino Acids:    Met  Gly  Phe  Lys  STOP

Protein:        M----G----F----K
                └────Peptide Bonds────┘
```

### Protein Structure from CDS

**Steps**:
1. Ribosome binds at start codon (AUG)
2. tRNAs bring amino acids matching each codon
3. Amino acids linked by peptide bonds
4. Translation stops at stop codon

**Result**: Polypeptide chain that folds into functional protein

---

## Alternative Splicing

### Creating Protein Diversity

Same gene → Different mRNA isoforms → Different proteins

**Example**:
```
Gene:      E1─I1─E2─I2─E3─I3─E4

Isoform 1: E1───E2───E3───E4  (all exons)
Isoform 2: E1───E2───────E4  (E3 skipped)
Isoform 3: E1───────E3───E4  (E2 skipped)
```

**Types of Alternative Splicing**:
1. **Exon skipping**: Most common (~40%)
2. **Alternative 5' splice site**: Different donor site
3. **Alternative 3' splice site**: Different acceptor site
4. **Intron retention**: Intron kept in mRNA
5. **Mutually exclusive exons**: Only one of multiple exons included

**Impact**: One human gene can produce 2-10 (or more) different proteins

---

## Bioinformatics Representations

### In FASTA Files

```fasta
>gene1_mRNA
ATGGCTTTTAAGTGAGGGGCCCAAA...
^                         ^
Start                   Stop
```

### In GFF3 Files

```gff3
chr1  Ensembl  gene      1000  5000  .  +  .  ID=gene1
chr1  Ensembl  mRNA      1000  5000  .  +  .  ID=trans1;Parent=gene1
chr1  Ensembl  five_prime_UTR  1000  1099  .  +  .  Parent=trans1
chr1  Ensembl  exon      1000  1500  .  +  .  Parent=trans1
chr1  Ensembl  CDS       1100  1500  .  +  0  Parent=trans1
chr1  Ensembl  exon      3000  3500  .  +  .  Parent=trans1
chr1  Ensembl  CDS       3000  3200  .  +  1  Parent=trans1
chr1  Ensembl  three_prime_UTR 3201  3500  .  +  .  Parent=trans1
```

---

## Key Differences: Prokaryotic vs Eukaryotic Genes

| Feature | Prokaryotes (Bacteria) | Eukaryotes (Animals, Plants) |
|---------|------------------------|------------------------------|
| **Introns** | Rare or absent | Common (average ~8 per gene) |
| **Splicing** | No | Yes (alternative splicing) |
| **5' Cap** | No | Yes (m7G cap) |
| **Poly(A) tail** | No | Yes (~200 A's) |
| **Operons** | Yes (polycistronic) | No (monocistronic) |
| **Transcription** | Coupled with translation | Separate (nuclear vs cytoplasm) |
| **Promoter** | -10 and -35 boxes | TATA box, CAAT box |

---

## Practical Applications

### 1. Designing PCR Primers

```python
# Avoid introns - design primers in same exon or spanning exon junction
# For cDNA (spliced): primers can span exon boundaries
# For genomic DNA: must account for introns

# Example: Amplify CDS only
Forward primer: In first exon of CDS
Reverse primer: In last exon of CDS
```

### 2. Predicting Mutation Effects

```python
mutation_position = 1500  # bp from TSS

if mutation_position < utr5_end:
    effect = "5'UTR - may affect translation efficiency"
elif mutation_position < cds_end:
    effect = "CDS - may change amino acid (missense)"
    if mutation_causes_stop_codon:
        effect = "CDS - nonsense mutation (truncated protein)"
elif mutation_position < utr3_end:
    effect = "3'UTR - may affect mRNA stability"
else:
    effect = "Downstream - likely no effect"
```

### 3. RNA-seq Analysis

```python
# Different quantification strategies
transcript_level_expression()  # Count reads mapping to exons
gene_level_expression()        # Sum all transcripts from same gene
exon_level_expression()        # Detect exon skipping events
junction_reads()               # Identify alternative splicing
```

---

## Practice Exercises

### Basic Level

1. **Identify Regions**: Given a gene sequence, mark TSS, start codon, stop codon, and polyadenylation signal.

2. **Calculate Lengths**: For a gene with 3 exons, calculate total exon length vs gene span.

3. **UTR vs CDS**: Determine which part of an mRNA is 5'UTR, CDS, and 3'UTR.

4. **Splicing Prediction**: Given exon-intron boundaries, predict the mature mRNA sequence.

5. **Codon Counting**: Count how many codons are in a CDS of 450 bp.

### Intermediate Level

6. **Alternative Isoforms**: Design 3 different mRNA isoforms from a 4-exon gene.

7. **Promoter Analysis**: Identify TATA box and CAAT box in a promoter sequence.

8. **Mutation Impact**: Predict effect of mutation at different gene regions (5'UTR, CDS, 3'UTR).

9. **Reading Frame**: Explain why intron splicing must maintain reading frame in CDS.

10. **Extract CDS**: From a multi-exon gene, extract only CDS portions and join them.

### Advanced Level

11. **Parse GFF3**: Extract all exons for a gene from GFF3, reconstruct transcript sequence using FASTA.

12. **Alternative Splicing Detector**: Write code to identify all possible isoforms from exon structure.

13. **Kozak Scanner**: Scan 5'UTR sequences for Kozak consensus and predict translation efficiency.

14. **3'UTR miRNA Sites**: Predict microRNA binding sites in 3'UTRs.

15. **Comparative Gene Structure**: Compare exon-intron structures of orthologous genes across species.

---

## Key Takeaways

1. **Gene ≠ CDS**: Gene includes promoter, UTRs, introns, and regulatory regions.

2. **Exons in mRNA**: Only exons appear in mature mRNA (introns removed).

3. **CDS = Translated**: Only CDS becomes protein; UTRs are transcribed but not translated.

4. **5'UTR Regulation**: Contains Kozak sequence, affects translation initiation.

5. **3'UTR Regulation**: Contains stability signals and miRNA binding sites.

6. **Splicing Critical**: Must be accurate to maintain reading frame.

7. **Alternative Splicing**: Creates protein diversity from single gene.

8. **Coordinates Matter**: TSS, start codon, stop codon, poly(A) signal mark key boundaries.

---

## Visual Summary

```
DNA GENE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Promoter  5'UTR  Exon1  Intron  Exon2  Intron  Exon3  3'UTR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

↓ Transcription

PRE-mRNA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5'cap-5'UTR-Exon1-Intron-Exon2-Intron-Exon3-3'UTR-AAAA

↓ Splicing (remove introns)

MATURE mRNA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5'cap-5'UTR-Exon1-Exon2-Exon3-3'UTR-AAAA
           \_____CDS______/

↓ Translation (CDS only)

PROTEIN:
━━━━━━━━━━━━━━━━━━━━━━
Met-Gly-Phe-...-Lys-STOP
```

---

## References

- **NCBI Gene Structure**: https://www.ncbi.nlm.nih.gov/books/NBK21134/
- **Ensembl Transcript Nomenclature**: https://www.ensembl.org/info/genome/genebuild/transcript_quality_tags.html
- **Kozak Sequence**: Kozak, M. (1987). *Nucleic Acids Research*
- **Alternative Splicing**: Wang et al. (2008). *Nature Reviews Genetics*

---

**Next Steps**: Learn to extract and analyze these regions from real GFF3 + FASTA files using Python and BioPython.
