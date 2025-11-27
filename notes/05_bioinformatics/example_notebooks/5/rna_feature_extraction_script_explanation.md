# RNA Feature Extraction Script - Complete Explanation

## Introduction

This document provides a comprehensive explanation of a Python script that extracts RNA features (promoters, coding sequences, UTRs, and terminators) from genomic data using GFF3 annotations and FASTA sequences. This is a common workflow in bioinformatics for analyzing gene structure and expression.

**What This Script Does:**
1. Downloads/uses GFF3 annotation and FASTA genome files
2. Converts GFF3 to SQLite database for fast querying
3. Extracts features for randomly selected genes
4. Retrieves DNA sequences for each feature
5. Exports data to TSV format for analysis

**Use Cases:**
- Promoter motif analysis
- Codon usage bias studies
- UTR regulatory element discovery
- Comparative genomics
- Training machine learning models for gene prediction

---

## Prerequisites and Installation

### Required Libraries

```python
# Package installation check with auto-install
try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

try:
    from Bio import SeqIO
    from Bio.Seq import Seq
except ImportError:
    !pip install biopython
    from Bio import SeqIO
    from Bio.Seq import Seq

import pandas as pd
import random
import gzip
import os
```

**Library Purposes:**
- `gffutils`: Parse GFF3 files, create databases, query features
- `Biopython`: Parse FASTA files, handle sequences
- `pandas`: Data manipulation and export
- `gzip`: Handle compressed files
- `random`: Random gene sampling

---

## Script Overview

### Complete Workflow Diagram

```
1. Input Files
   ├─ GFF3 (genome annotation)
   └─ FASTA (genome sequence)

2. Create Database
   └─ Convert GFF3 → SQLite DB (one-time)

3. Sample Genes
   └─ Select N random genes

4. Extract Features
   ├─ Promoter (upstream of TSS)
   ├─ 5'UTR
   ├─ CDS (coding sequence)
   ├─ 3'UTR
   └─ Terminator (downstream of TTS)

5. Retrieve Sequences
   └─ Map coordinates → FASTA → extract DNA

6. Output
   └─ TSV file with all features and sequences
```

---

## Part 1: Configuration and Setup

### File Paths and Parameters

```python
# ▼ Input file paths (change if needed)
gff_file = "/content/Caenorhabditis_elegans.WBcel235.61.chromosome.I.gff3.gz"
fasta_file = "/content/Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz"

# Output files
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = gff_file.removesuffix(".gz").removesuffix(".gff3") + ".rna_seq.tsv"

# Feature extraction parameters
promoter_len = 100      # Bases upstream of TSS
terminator_len = 100    # Bases downstream of TTS
num_genes = 100         # Number of genes to sample
```

**Configuration Explanation:**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `gff_file` | Path to GFF3 | Genome annotation (genes, exons, etc.) |
| `fasta_file` | Path to FASTA | Actual DNA sequences |
| `db_fn` | Generated .db path | SQLite database for fast queries |
| `output_path` | Generated .tsv path | Final output file |
| `promoter_len` | 100 bp | How far upstream to extract |
| `terminator_len` | 100 bp | How far downstream to extract |
| `num_genes` | 100 | Sample size for analysis |

---

## Part 2: Database Creation

### Create or Load GFF3 Database

```python
# Create GFF database
if not os.path.exists(db_fn):
    print("Creating GFF database... (this may take some time)")
    db = gffutils.create_db(
        gff_file,
        db_fn,
        force=True,
        keep_order=False,
        disable_infer_transcripts=True,
        merge_strategy="create_unique",
        sort_attribute_values=True
    )
else:
    print(f"Loading existing database: {db_fn}")
    db = gffutils.FeatureDB(db_fn)
```

**Why Database Conversion?**

| Without Database | With Database |
|------------------|---------------|
| Must scan entire GFF3 file for each query | Indexed lookups (milliseconds) |
| Slow parent-child navigation | Instant relationship queries |
| Re-parse file every run | Load once, use forever |
| Memory inefficient | Optimized memory usage |

**Parameters Explained:**

```python
gffutils.create_db(
    gff_file,                          # Input GFF3
    db_fn,                             # Output database
    force=True,                        # Overwrite if exists
    keep_order=False,                  # Don't preserve line order (faster)
    disable_infer_transcripts=True,    # Don't auto-create transcript features
    merge_strategy="create_unique",    # Handle duplicate IDs by making unique
    sort_attribute_values=True         # Sort attributes alphabetically
)
```

**Typical Creation Time:**
- Small genome (bacteria, C. elegans chromosome): 30 seconds - 2 minutes
- Full C. elegans genome: 5-10 minutes
- Human genome: 15-30 minutes

---

## Part 3: Gene Sampling

### Random Gene Selection

```python
# Get all genes and sample randomly
all_genes = list(db.features_of_type("gene"))
print(f"Total genes in database: {len(all_genes)}")

sample_genes = random.sample(all_genes, min(num_genes, len(all_genes)))
print(f"Sampled {len(sample_genes)} genes for analysis")
```

**Why Random Sampling?**
- Reduce computation time for large genomes
- Create representative dataset
- Enable statistical analysis
- Test pipeline on subset before full run

**Alternative Sampling Strategies:**

```python
# Option 1: All genes (no sampling)
sample_genes = list(db.features_of_type("gene"))

# Option 2: Genes in specific region
sample_genes = list(db.region(
    seqid='chrI',
    start=1000000,
    end=2000000,
    featuretype='gene'
))

# Option 3: Genes with specific criteria
sample_genes = [g for g in db.features_of_type("gene") 
                if len(g) > 1000]  # Only long genes
```

---

## Part 4: Loading Genome Sequences

### Parse FASTA with BioPython

```python
# Load genome sequence(s) from FASTA
with gzip.open(fasta_file, "rt") as handle:
    genome = {record.id: record.seq for record in SeqIO.parse(handle, "fasta")}

print(f"Loaded {len(genome)} chromosome(s)")
for chr_id, seq in genome.items():
    print(f"  {chr_id}: {len(seq):,} bp")
```

**Data Structure:**

```python
genome = {
    'I': Seq('GCGATCGATCGATC...'),      # Chromosome I
    'II': Seq('ATGCATGCATGCAT...'),     # Chromosome II
    ...
}
```

**Why Dictionary?**
- Fast O(1) lookup by chromosome name
- Keeps all chromosomes in memory
- Works with multi-chromosome genomes

**Memory Considerations:**

| Genome | Size | Memory Usage |
|--------|------|--------------|
| E. coli | 4.6 Mb | ~5 MB RAM |
| C. elegans | 100 Mb | ~100 MB RAM |
| Human | 3.2 Gb | ~3.2 GB RAM |

---

## Part 5: Feature Extraction Functions

### Extract Promoter Sequence

```python
def get_promoter(gene, genome, promoter_len):
    """
    Extract promoter region (upstream of TSS).
    
    Args:
        gene: gffutils.Feature object
        genome: dict of {chr: Seq}
        promoter_len: bp upstream of TSS
    
    Returns:
        DNA sequence string or None
    """
    seqid = gene.seqid
    if seqid not in genome:
        return None
    
    chr_seq = genome[seqid]
    chr_len = len(chr_seq)
    
    if gene.strand == '+':
        # Forward: upstream = lower coordinates
        start = max(0, gene.start - promoter_len - 1)
        end = gene.start - 1
        seq = chr_seq[start:end]
    else:
        # Reverse: upstream = higher coordinates (reverse complement)
        start = gene.end
        end = min(chr_len, gene.end + promoter_len)
        seq = chr_seq[start:end].reverse_complement()
    
    return str(seq)
```

**Strand Handling:**

```
Forward strand (+):
    Promoter  →  Gene
    ────────  →  ████████
    -100  -1  →  1...1000

Reverse strand (-):
    Gene  ←  Promoter
    ████████  ←  ────────
    1...1000  ←  1001  1100
```

### Extract UTRs and CDS

```python
def get_utr_cds(transcript, genome, db):
    """
    Extract 5'UTR, CDS, and 3'UTR sequences.
    
    Returns:
        tuple: (utr5_seq, cds_seq, utr3_seq)
    """
    seqid = transcript.seqid
    if seqid not in genome:
        return None, None, None
    
    chr_seq = genome[seqid]
    
    # Get child features
    utr5_features = list(db.children(transcript, featuretype='five_prime_UTR'))
    cds_features = list(db.children(transcript, featuretype='CDS'))
    utr3_features = list(db.children(transcript, featuretype='three_prime_UTR'))
    
    # Extract sequences
    def extract_features(features):
        if not features:
            return ""
        
        # Sort by position
        sorted_features = sorted(features, key=lambda f: f.start)
        
        # Concatenate exons
        seq_parts = []
        for feat in sorted_features:
            seq_parts.append(chr_seq[feat.start-1:feat.end])
        
        full_seq = Seq('').join(seq_parts)
        
        # Reverse complement if minus strand
        if features[0].strand == '-':
            full_seq = full_seq.reverse_complement()
        
        return str(full_seq)
    
    utr5_seq = extract_features(utr5_features)
    cds_seq = extract_features(cds_features)
    utr3_seq = extract_features(utr3_features)
    
    return utr5_seq, cds_seq, utr3_seq
```

**Key Points:**
1. **Multiple Exons**: UTRs and CDS can be split across exons
2. **Sorting**: Must process exons in order
3. **Concatenation**: Join exon sequences to get complete region
4. **Strand**: Reverse complement for minus strand genes

### Extract Terminator

```python
def get_terminator(gene, genome, terminator_len):
    """
    Extract terminator region (downstream of TTS).
    """
    seqid = gene.seqid
    if seqid not in genome:
        return None
    
    chr_seq = genome[seqid]
    chr_len = len(chr_seq)
    
    if gene.strand == '+':
        # Forward: downstream = higher coordinates
        start = gene.end
        end = min(chr_len, gene.end + terminator_len)
        seq = chr_seq[start:end]
    else:
        # Reverse: downstream = lower coordinates (reverse complement)
        start = max(0, gene.start - terminator_len - 1)
        end = gene.start - 1
        seq = chr_seq[start:end].reverse_complement()
    
    return str(seq)
```

---

## Part 6: Main Extraction Loop

### Process Each Gene

```python
results = []

for gene in sample_genes:
    gene_id = gene.id
    gene_name = gene.attributes.get('Name', [gene_id])[0]
    
    # Get promoter
    promoter_seq = get_promoter(gene, genome, promoter_len)
    
    # Get terminator
    terminator_seq = get_terminator(gene, genome, terminator_len)
    
    # Process each transcript
    transcripts = list(db.children(gene, featuretype='mRNA'))
    
    if not transcripts:
        # Gene has no mRNA children, skip
        continue
    
    for transcript in transcripts:
        transcript_id = transcript.id
        
        # Get UTRs and CDS
        utr5_seq, cds_seq, utr3_seq = get_utr_cds(transcript, genome, db)
        
        # Store results
        results.append({
            'gene_id': gene_id,
            'gene_name': gene_name,
            'transcript_id': transcript_id,
            'chromosome': gene.seqid,
            'strand': gene.strand,
            'gene_start': gene.start,
            'gene_end': gene.end,
            'promoter_seq': promoter_seq,
            'utr5_seq': utr5_seq,
            'cds_seq': cds_seq,
            'utr3_seq': utr3_seq,
            'terminator_seq': terminator_seq,
            'promoter_len': len(promoter_seq) if promoter_seq else 0,
            'utr5_len': len(utr5_seq) if utr5_seq else 0,
            'cds_len': len(cds_seq) if cds_seq else 0,
            'utr3_len': len(utr3_seq) if utr3_seq else 0,
            'terminator_len': len(terminator_seq) if terminator_seq else 0
        })

print(f"Extracted features for {len(results)} transcripts")
```

**Data Collection:**
- Each row = one transcript
- Genes with multiple transcripts = multiple rows
- Captures all sequence regions and metadata

---

## Part 7: Export Results

### Create DataFrame and Save

```python
# Convert to pandas DataFrame
df = pd.DataFrame(results)

# Add summary statistics
df['total_transcript_len'] = df['utr5_len'] + df['cds_len'] + df['utr3_len']
df['gc_content_cds'] = df['cds_seq'].apply(
    lambda seq: (seq.count('G') + seq.count('C')) / len(seq) * 100 if len(seq) > 0 else 0
)

# Save to TSV
df.to_csv(output_path, sep='\t', index=False)

print(f"\nResults saved to: {output_path}")
print(f"Total transcripts analyzed: {len(df)}")
print(f"\nSummary Statistics:")
print(df[['promoter_len', 'utr5_len', 'cds_len', 'utr3_len', 'terminator_len']].describe())
```

**Output Format (TSV):**

| Column | Description |
|--------|-------------|
| gene_id | Unique gene identifier |
| gene_name | Human-readable name |
| transcript_id | Transcript variant ID |
| chromosome | Chromosome/contig name |
| strand | +/- strand |
| gene_start | Gene start position |
| gene_end | Gene end position |
| promoter_seq | Promoter DNA sequence |
| utr5_seq | 5'UTR sequence |
| cds_seq | Coding sequence |
| utr3_seq | 3'UTR sequence |
| terminator_seq | Terminator sequence |
| *_len | Length of each region |
| gc_content_cds | GC% in coding sequence |

---

## Complete Working Script

```python
#!/usr/bin/env python3
"""
RNA Feature Extraction Pipeline
Extracts promoters, UTRs, CDS, and terminators from GFF3 + FASTA
"""

# ═══════════════════════════════════════════════════════════════
# 1. IMPORTS AND SETUP
# ═══════════════════════════════════════════════════════════════

try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

try:
    from Bio import SeqIO
    from Bio.Seq import Seq
except ImportError:
    !pip install biopython
    from Bio import SeqIO
    from Bio.Seq import Seq

import pandas as pd
import random
import gzip
import os

# ═══════════════════════════════════════════════════════════════
# 2. CONFIGURATION
# ═══════════════════════════════════════════════════════════════

gff_file = "genome.gff3.gz"
fasta_file = "genome.fasta.gz"
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = "rna_features.tsv"

promoter_len = 100
terminator_len = 100
num_genes = 100

# ═══════════════════════════════════════════════════════════════
# 3. CREATE DATABASE
# ═══════════════════════════════════════════════════════════════

if not os.path.exists(db_fn):
    print("Creating GFF database...")
    db = gffutils.create_db(
        gff_file, db_fn, force=True, keep_order=False,
        disable_infer_transcripts=True, merge_strategy="create_unique",
        sort_attribute_values=True
    )
else:
    db = gffutils.FeatureDB(db_fn)

# ═══════════════════════════════════════════════════════════════
# 4. LOAD GENOME
# ═══════════════════════════════════════════════════════════════

with gzip.open(fasta_file, "rt") as handle:
    genome = {record.id: record.seq for record in SeqIO.parse(handle, "fasta")}

print(f"Loaded {len(genome)} chromosome(s)")

# ═══════════════════════════════════════════════════════════════
# 5. SAMPLE GENES
# ═══════════════════════════════════════════════════════════════

all_genes = list(db.features_of_type("gene"))
sample_genes = random.sample(all_genes, min(num_genes, len(all_genes)))

print(f"Sampled {len(sample_genes)} genes")

# ═══════════════════════════════════════════════════════════════
# 6. EXTRACTION FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def get_promoter(gene, genome, length):
    seqid = gene.seqid
    if seqid not in genome:
        return None
    
    chr_seq = genome[seqid]
    chr_len = len(chr_seq)
    
    if gene.strand == '+':
        start = max(0, gene.start - length - 1)
        end = gene.start - 1
        seq = chr_seq[start:end]
    else:
        start = gene.end
        end = min(chr_len, gene.end + length)
        seq = chr_seq[start:end].reverse_complement()
    
    return str(seq)

def get_terminator(gene, genome, length):
    seqid = gene.seqid
    if seqid not in genome:
        return None
    
    chr_seq = genome[seqid]
    chr_len = len(chr_seq)
    
    if gene.strand == '+':
        start = gene.end
        end = min(chr_len, gene.end + length)
        seq = chr_seq[start:end]
    else:
        start = max(0, gene.start - length - 1)
        end = gene.start - 1
        seq = chr_seq[start:end].reverse_complement()
    
    return str(seq)

def get_utr_cds(transcript, genome, db):
    seqid = transcript.seqid
    if seqid not in genome:
        return None, None, None
    
    chr_seq = genome[seqid]
    
    utr5_features = list(db.children(transcript, featuretype='five_prime_UTR'))
    cds_features = list(db.children(transcript, featuretype='CDS'))
    utr3_features = list(db.children(transcript, featuretype='three_prime_UTR'))
    
    def extract_features(features):
        if not features:
            return ""
        sorted_features = sorted(features, key=lambda f: f.start)
        seq_parts = [chr_seq[f.start-1:f.end] for f in sorted_features]
        full_seq = Seq('').join(seq_parts)
        if features[0].strand == '-':
            full_seq = full_seq.reverse_complement()
        return str(full_seq)
    
    return extract_features(utr5_features), extract_features(cds_features), extract_features(utr3_features)

# ═══════════════════════════════════════════════════════════════
# 7. EXTRACT FEATURES
# ═══════════════════════════════════════════════════════════════

results = []

for gene in sample_genes:
    promoter_seq = get_promoter(gene, genome, promoter_len)
    terminator_seq = get_terminator(gene, genome, terminator_len)
    
    for transcript in db.children(gene, featuretype='mRNA'):
        utr5_seq, cds_seq, utr3_seq = get_utr_cds(transcript, genome, db)
        
        results.append({
            'gene_id': gene.id,
            'transcript_id': transcript.id,
            'chromosome': gene.seqid,
            'strand': gene.strand,
            'promoter_seq': promoter_seq,
            'utr5_seq': utr5_seq,
            'cds_seq': cds_seq,
            'utr3_seq': utr3_seq,
            'terminator_seq': terminator_seq
        })

# ═══════════════════════════════════════════════════════════════
# 8. EXPORT RESULTS
# ═══════════════════════════════════════════════════════════════

df = pd.DataFrame(results)
df.to_csv(output_path, sep='\t', index=False)

print(f"\n✓ Results saved to: {output_path}")
print(f"✓ Total transcripts: {len(df)}")
```

---

## Practice Exercises

### Basic Level

1. **Modify Parameters**: Change promoter_len to 500 bp and re-run script.

2. **Add GC Content**: Calculate GC% for all regions (promoter, UTRs, terminator).

3. **Filter by Length**: Only extract genes longer than 1000 bp.

4. **Count Features**: Add column counting number of exons per transcript.

5. **Export FASTA**: Write extracted CDS sequences to FASTA format.

### Intermediate Level

6. **Translate CDS**: Add column with protein sequence translation.

7. **Find Motifs**: Search for TATA box (TATAAA) in promoter sequences.

8. **Codon Usage**: Calculate codon usage frequency for each CDS.

9. **Visualize Lengths**: Create histogram of CDS lengths using matplotlib.

10. **Batch Processing**: Modify to process all chromosomes in genome.

### Advanced Level

11. **Alternative Isoforms**: Compare feature lengths across transcript isoforms of same gene.

12. **Conservation Analysis**: Add column with conservation scores from phyloP data.

13. **Parallel Processing**: Use multiprocessing to speed up extraction for large genomes.

14. **Quality Control**: Add validation checks (e.g., CDS must be multiple of 3).

15. **Machine Learning Prep**: Format output for training gene prediction models.

---

## Key Takeaways

1. **GFF3 Database**: Essential for efficient querying of large annotations.

2. **Strand Matters**: Always reverse complement for minus strand features.

3. **Exon Handling**: UTRs and CDS can span multiple exons—must concatenate.

4. **Coordinate Systems**: GFF3 is 1-based, Python slicing is 0-based (subtract 1 from start).

5. **Memory Management**: Loading entire genome into memory is fine for small genomes, problematic for large ones.

6. **Error Handling**: Always check if chromosome exists in genome dictionary.

7. **Reproducibility**: Random sampling should use `random.seed()` for reproducible results.

8. **Validation**: Check that extracted sequences make biological sense (e.g., CDS length divisible by 3).

---

## References

- **gffutils**: https://daler.github.io/gffutils/
- **BioPython**: http://biopython.org/
- **Pandas**: https://pandas.pydata.org/
- Dale, R. K. et al. (2011). gffutils: working with GFF and GTF files. *Bioinformatics*.

---

**Next Steps**: Use the extracted features for downstream analysis—motif discovery, machine learning, comparative genomics, or regulatory element prediction.
