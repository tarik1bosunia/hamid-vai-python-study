# GFF3 File Format - Complete Guide

## Introduction

**GFF3 (General Feature Format Version 3)** is a standard tab-delimited text format for describing genomic features and their annotations. It is one of the most important file formats in bioinformatics for representing genes, transcripts, exons, regulatory elements, and other genomic features.

**Why GFF3 Matters:**
- Genome annotation storage and exchange
- Gene structure representation (genes → transcripts → exons)
- Input for genome browsers (IGV, UCSC, Ensembl)
- RNA-seq analysis and transcript quantification
- Comparative genomics and genome editing

**Key Databases Using GFF3:**
- Ensembl
- NCBI RefSeq
- FlyBase, WormBase, TAIR
- Genome assembly projects

---

## GFF3 File Structure

### The 9 Mandatory Columns

Every GFF3 feature line contains exactly **9 tab-separated fields**:

```
seqid  source  type  start  end  score  strand  phase  attributes
```

All 9 columns are **required** (use `.` for missing/not-applicable values).

### Column Descriptions

| Column | Name | Description | Example Values |
|--------|------|-------------|----------------|
| 1 | **seqid** | Chromosome/contig name | chr1, scaffold_1, CM000001.1 |
| 2 | **source** | Annotation source | Ensembl, RefSeq, AUGUSTUS, MAKER |
| 3 | **type** | Feature type (SO term) | gene, mRNA, exon, CDS, UTR |
| 4 | **start** | Start position (1-based, inclusive) | 1000 |
| 5 | **end** | End position (1-based, inclusive) | 2000 |
| 6 | **score** | Numeric score or `.` | 0.95, 100, . |
| 7 | **strand** | DNA strand | +, -, . |
| 8 | **phase** | CDS reading frame | 0, 1, 2, . |
| 9 | **attributes** | Semicolon-separated key=value pairs | ID=gene1;Name=TP53 |

---

## Detailed Column Explanations

### 1. seqid (Sequence ID)

The name of the chromosome, scaffold, or contig.

**Examples:**
```
chr1
2
chrX
scaffold_123
NC_000001.11
```

**Note**: Must match sequence names in corresponding FASTA file.

### 2. source

The program, database, or pipeline that generated the annotation.

**Examples:**
- `Ensembl` - Ensembl genome browser
- `RefSeq` - NCBI Reference Sequence database
- `AUGUSTUS` - Gene prediction tool
- `MAKER` - Genome annotation pipeline
- `.` - Unknown source

### 3. type (Feature Type)

Controlled vocabulary from **Sequence Ontology (SO)**.

**Common Feature Types:**

| Type | Description |
|------|-------------|
| `gene` | Complete gene span |
| `mRNA` | Messenger RNA transcript |
| `exon` | Exon (transcribed region) |
| `CDS` | Coding sequence (translated region) |
| `five_prime_UTR` | 5' untranslated region |
| `three_prime_UTR` | 3' untranslated region |
| `intron` | Intron (spliced out) |
| `ncRNA` | Non-coding RNA |
| `tRNA` | Transfer RNA |
| `rRNA` | Ribosomal RNA |
| `promoter` | Promoter region |
| `enhancer` | Enhancer element |

### 4-5. start and end (Genomic Coordinates)

**Important**: GFF3 uses **1-based, inclusive** coordinates.

```
start=100, end=102 means positions 100, 101, 102 (3 bases total)
```

**Comparison with other formats:**

| Format | Coordinate System |
|--------|-------------------|
| GFF3 | 1-based, inclusive (start, end) |
| BED | 0-based, half-open [start, end) |
| SAM/BAM | 1-based, inclusive |

### 6. score

Optional numeric value indicating quality or confidence.

**Uses:**
- BLAST alignment score
- Gene prediction confidence (0-1)
- Phred quality score
- `.` if not applicable

### 7. strand

DNA strand orientation:
- `+` = Forward (plus) strand
- `-` = Reverse (minus) strand
- `.` = Not stranded or unknown

### 8. phase (CDS Only)

Indicates where the next codon begins (reading frame).

**Values:**
- `0` = CDS starts at first base of codon
- `1` = CDS starts at second base (1 base from previous exon)
- `2` = CDS starts at third base (2 bases from previous exon)
- `.` = Not a CDS feature

**Why phase matters**: Ensures correct translation across split exons.

```
Exon 1: ATG GCT (phase=0, complete codons)
Exon 2: AAA GGG (phase=0, starts new codon)

Exon 1: ATG GC (phase=0)
Exon 2: T AAA GGG (phase=2, completes "GCT" codon)
```

### 9. attributes

Semicolon-separated `key=value` pairs providing additional information.

**Standard Attributes:**

| Attribute | Required For | Description |
|-----------|--------------|-------------|
| `ID` | All features with children | Unique identifier |
| `Parent` | Child features | ID of parent feature |
| `Name` | Optional | Human-readable name |
| `Alias` | Optional | Alternative names |
| `Note` | Optional | Free text description |
| `Dbxref` | Optional | External database reference |
| `Ontology_term` | Optional | SO or GO term |

**Examples:**
```
ID=gene:BRCA1;Name=BRCA1;biotype=protein_coding
Parent=transcript:BRCA1-201;exon_number=1
ID=cds:BRCA1-201;Parent=transcript:BRCA1-201;protein_id=ENSP00000350283
```

---

## GFF3 Hierarchy and Parent-Child Relationships

GFF3 uses explicit `ID` and `Parent` attributes to build feature hierarchies.

**Typical Gene Structure:**
```
gene
 └── mRNA (transcript)
      ├── five_prime_UTR
      ├── exon
      ├── CDS
      ├── exon
      ├── CDS
      ├── three_prime_UTR
      └── exon
```

**Example GFF3 with Hierarchy:**

```gff3
##gff-version 3
chr17  Ensembl  gene     7565097  7590856  .  +  .  ID=gene:TP53;Name=TP53;biotype=protein_coding
chr17  Ensembl  mRNA     7565097  7590856  .  +  .  ID=transcript:TP53-201;Parent=gene:TP53;Name=TP53-201
chr17  Ensembl  exon     7565097  7565332  .  +  .  ID=exon:TP53-201-E1;Parent=transcript:TP53-201;exon_number=1
chr17  Ensembl  CDS      7565097  7565332  .  +  0  ID=cds:TP53-201;Parent=transcript:TP53-201;protein_id=P04637
chr17  Ensembl  exon     7577019  7577155  .  +  .  ID=exon:TP53-201-E2;Parent=transcript:TP53-201;exon_number=2
chr17  Ensembl  CDS      7577019  7577155  .  +  0  ID=cds:TP53-201;Parent=transcript:TP53-201
```

---

## Complete GFF3 Example

```gff3
##gff-version 3
##sequence-region chr1 1 248956422
#
# Example gene: Hemoglobin subunit beta (HBB)
#
chr11  RefSeq  gene        5225464  5227071  .  -  .  ID=gene:HBB;Name=HBB;description=hemoglobin subunit beta
chr11  RefSeq  mRNA        5225464  5227071  .  -  .  ID=transcript:NM_000518;Parent=gene:HBB;Name=HBB-201
chr11  RefSeq  exon        5226929  5227071  .  -  .  ID=exon:HBB-E1;Parent=transcript:NM_000518;exon_number=1
chr11  RefSeq  exon        5226576  5226799  .  -  .  ID=exon:HBB-E2;Parent=transcript:NM_000518;exon_number=2
chr11  RefSeq  exon        5225464  5225725  .  -  .  ID=exon:HBB-E3;Parent=transcript:NM_000518;exon_number=3
chr11  RefSeq  CDS         5226929  5227020  .  -  0  Parent=transcript:NM_000518
chr11  RefSeq  CDS         5226576  5226799  .  -  2  Parent=transcript:NM_000518
chr11  RefSeq  CDS         5225625  5225725  .  -  0  Parent=transcript:NM_000518
chr11  RefSeq  five_prime_UTR   5227021  5227071  .  -  .  Parent=transcript:NM_000518
chr11  RefSeq  three_prime_UTR  5225464  5225624  .  -  .  Parent=transcript:NM_000518
```

---

## Parsing GFF3 Files

### Method 1: Using gffutils (Recommended)

```python
import gffutils

# Create database from GFF3 (one-time operation)
db = gffutils.create_db(
    'genes.gff3',
    'genes.db',
    force=True,
    keep_order=True,
    merge_strategy='merge',
    sort_attribute_values=True
)

# Or load existing database
db = gffutils.FeatureDB('genes.db')

# Query all genes
for gene in db.features_of_type('gene'):
    print(f"Gene: {gene.id} ({gene.start}-{gene.end})")
    
    # Get all transcripts for this gene
    for transcript in db.children(gene, featuretype='mRNA'):
        print(f"  Transcript: {transcript.id}")
        
        # Get all exons for this transcript
        exons = list(db.children(transcript, featuretype='exon'))
        print(f"    Exons: {len(exons)}")
```

### Method 2: Using BioPython

```python
from BCBio import GFF

# Parse GFF3 file
with open('genes.gff3') as handle:
    for record in GFF.parse(handle):
        print(f"Sequence: {record.id}")
        
        for feature in record.features:
            if feature.type == 'gene':
                print(f"  Gene: {feature.id}")
                print(f"  Location: {feature.location}")
                print(f"  Strand: {feature.strand}")
```

### Method 3: Manual Parsing

```python
def parse_gff3_simple(filename: str):
    """
    Simple GFF3 parser for basic use cases.
    """
    features = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue
            
            # Split by tabs
            fields = line.split('\t')
            
            if len(fields) != 9:
                continue
            
            # Parse attributes
            attrs = {}
            for attr in fields[8].split(';'):
                if '=' in attr:
                    key, value = attr.split('=', 1)
                    attrs[key] = value
            
            feature = {
                'seqid': fields[0],
                'source': fields[1],
                'type': fields[2],
                'start': int(fields[3]),
                'end': int(fields[4]),
                'score': fields[5],
                'strand': fields[6],
                'phase': fields[7],
                'attributes': attrs
            }
            
            features.append(feature)
    
    return features

# Usage
features = parse_gff3_simple('genes.gff3')
for feat in features[:5]:
    print(f"{feat['type']}: {feat['seqid']}:{feat['start']}-{feat['end']}")
```

---

## Bioinformatics Applications

### 1. Extract All Genes from Chromosome

```python
import gffutils

db = gffutils.FeatureDB('genome.db')

chromosome = 'chr1'
genes = []

for gene in db.region(seqid=chromosome, featuretype='gene'):
    genes.append({
        'id': gene.id,
        'name': gene.attributes.get('Name', [''])[0],
        'start': gene.start,
        'end': gene.end,
        'strand': gene.strand,
        'length': len(gene)
    })

print(f"Found {len(genes)} genes on {chromosome}")

# Sort by position
genes.sort(key=lambda x: x['start'])

for gene in genes[:10]:
    print(f"{gene['name']:10s} {gene['start']:10d}-{gene['end']:10d} ({gene['length']} bp)")
```

### 2. Calculate Exon Statistics

```python
def analyze_exons(db_file: str):
    """
    Calculate comprehensive exon statistics.
    """
    import gffutils
    
    db = gffutils.FeatureDB(db_file)
    
    exon_counts = []
    exon_lengths = []
    intron_lengths = []
    
    for gene in db.features_of_type('gene'):
        for transcript in db.children(gene, featuretype='mRNA'):
            exons = sorted(list(db.children(transcript, featuretype='exon')),
                          key=lambda x: x.start)
            
            if not exons:
                continue
            
            exon_counts.append(len(exons))
            
            # Exon lengths
            for exon in exons:
                exon_lengths.append(len(exon))
            
            # Intron lengths (between consecutive exons)
            for i in range(len(exons) - 1):
                intron_len = exons[i+1].start - exons[i].end - 1
                intron_lengths.append(intron_len)
    
    stats = {
        'total_transcripts': len(exon_counts),
        'mean_exons_per_transcript': sum(exon_counts) / len(exon_counts),
        'max_exons': max(exon_counts),
        'mean_exon_length': sum(exon_lengths) / len(exon_lengths),
        'mean_intron_length': sum(intron_lengths) / len(intron_lengths) if intron_lengths else 0
    }
    
    return stats

# Usage
stats = analyze_exons('genome.db')
print(f"Mean exons per transcript: {stats['mean_exons_per_transcript']:.1f}")
print(f"Mean exon length: {stats['mean_exon_length']:.1f} bp")
print(f"Mean intron length: {stats['mean_intron_length']:.1f} bp")
```

### 3. Extract Gene Sequences

```python
import gffutils
from Bio import SeqIO

def extract_gene_sequences(gff_db: str, fasta_file: str, output_file: str):
    """
    Extract DNA sequences for all genes.
    """
    db = gffutils.FeatureDB(gff_db)
    
    # Load genome sequence
    genome = {}
    for record in SeqIO.parse(fasta_file, 'fasta'):
        genome[record.id] = record.seq
    
    with open(output_file, 'w') as out:
        for gene in db.features_of_type('gene'):
            seqid = gene.seqid
            
            if seqid not in genome:
                continue
            
            # Extract sequence
            gene_seq = genome[seqid][gene.start-1:gene.end]
            
            # Reverse complement if on minus strand
            if gene.strand == '-':
                gene_seq = gene_seq.reverse_complement()
            
            # Write FASTA
            gene_name = gene.attributes.get('Name', [gene.id])[0]
            out.write(f">{gene_name} {seqid}:{gene.start}-{gene.end} ({gene.strand})\n")
            out.write(f"{gene_seq}\n")
    
    print(f"Extracted sequences written to {output_file}")

# Usage
extract_gene_sequences('genome.db', 'genome.fasta', 'genes.fasta')
```

### 4. Find Overlapping Genes

```python
def find_overlapping_genes(db_file: str):
    """
    Find genes that overlap on the same strand.
    Important for understanding genome organization.
    """
    import gffutils
    
    db = gffutils.FeatureDB(db_file)
    
    overlaps = []
    
    # Group genes by chromosome
    genes_by_chr = {}
    for gene in db.features_of_type('gene'):
        if gene.seqid not in genes_by_chr:
            genes_by_chr[gene.seqid] = []
        genes_by_chr[gene.seqid].append(gene)
    
    # Check for overlaps within each chromosome
    for chr_name, genes in genes_by_chr.items():
        genes_sorted = sorted(genes, key=lambda x: x.start)
        
        for i in range(len(genes_sorted) - 1):
            gene1 = genes_sorted[i]
            gene2 = genes_sorted[i + 1]
            
            # Check same strand
            if gene1.strand == gene2.strand:
                # Check overlap
                if gene1.end >= gene2.start:
                    overlap_len = gene1.end - gene2.start + 1
                    overlaps.append({
                        'chr': chr_name,
                        'gene1': gene1.attributes.get('Name', [gene1.id])[0],
                        'gene2': gene2.attributes.get('Name', [gene2.id])[0],
                        'overlap_bp': overlap_len,
                        'strand': gene1.strand
                    })
    
    return overlaps

# Usage
overlaps = find_overlapping_genes('genome.db')
print(f"Found {len(overlaps)} overlapping gene pairs")

for overlap in overlaps[:10]:
    print(f"{overlap['gene1']} <-> {overlap['gene2']}: {overlap['overlap_bp']} bp overlap ({overlap['strand']} strand)")
```

### 5. Extract Promoter Regions

```python
def extract_promoters(db_file: str, fasta_file: str, 
                     upstream: int = 2000, downstream: int = 200):
    """
    Extract promoter regions (upstream of transcription start site).
    
    Args:
        upstream: Bases upstream of TSS
        downstream: Bases downstream of TSS
    """
    import gffutils
    from Bio import SeqIO
    
    db = gffutils.FeatureDB(db_file)
    genome = {rec.id: rec.seq for rec in SeqIO.parse(fasta_file, 'fasta')}
    
    promoters = []
    
    for gene in db.features_of_type('gene'):
        seqid = gene.seqid
        
        if seqid not in genome:
            continue
        
        if gene.strand == '+':
            # Forward strand: upstream of start
            prom_start = max(1, gene.start - upstream)
            prom_end = gene.start + downstream
            prom_seq = genome[seqid][prom_start-1:prom_end]
        else:
            # Reverse strand: upstream of end (in reverse direction)
            prom_start = gene.end - downstream
            prom_end = min(len(genome[seqid]), gene.end + upstream)
            prom_seq = genome[seqid][prom_start-1:prom_end].reverse_complement()
        
        gene_name = gene.attributes.get('Name', [gene.id])[0]
        
        promoters.append({
            'gene': gene_name,
            'sequence': str(prom_seq),
            'location': f"{seqid}:{prom_start}-{prom_end}",
            'strand': gene.strand
        })
    
    return promoters

# Usage
promoters = extract_promoters('genome.db', 'genome.fasta', upstream=2000)
print(f"Extracted {len(promoters)} promoter sequences")
```

---

## GFF3 vs GTF Comparison

| Feature | GFF3 | GTF (GFF2) |
|---------|------|------------|
| **Version** | 3 | 2.x |
| **Attributes format** | `key=value` | `key "value"` |
| **Hierarchy** | Explicit ID/Parent | Implicit (gene_id/transcript_id) |
| **Standard** | Well-defined spec | Less standardized |
| **Flexibility** | More flexible | More rigid |
| **Modern tools** | Preferred | Legacy support |

**Example Comparison:**

GFF3:
```gff3
chr1  Ensembl  gene  1000  2000  .  +  .  ID=gene1;Name=BRCA1
chr1  Ensembl  mRNA  1000  2000  .  +  .  ID=trans1;Parent=gene1
```

GTF:
```gtf
chr1  Ensembl  gene  1000  2000  .  +  .  gene_id "gene1"; gene_name "BRCA1";
chr1  Ensembl  transcript  1000  2000  .  +  .  gene_id "gene1"; transcript_id "trans1";
```

---

## Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| **Parsing errors** | Validate with `gff3_validate.py` or AGAT |
| **Missing Parent IDs** | Check that all Parent references exist as IDs |
| **Spaces in attributes** | URL-encode special characters |
| **Coordinate mismatches** | Ensure 1-based indexing |
| **Large files** | Use gffutils database for efficient querying |
| **Mixed tabs/spaces** | Use proper tab characters (`\t`) |

---

## Practice Exercises

### Basic Level

1. **Count Features**: Count how many genes, mRNAs, and exons are in a GFF3 file.

2. **Parse Attributes**: Extract all gene names from the attributes column.

3. **Filter by Chromosome**: Extract all features from chr1 only.

4. **Calculate Lengths**: Calculate the length of each gene feature.

5. **Strand Distribution**: Count features on + strand vs - strand.

### Intermediate Level

6. **Exons Per Gene**: Calculate the mean number of exons per gene.

7. **Extract CDSs**: Extract all CDS features and their parent transcripts.

8. **Gene Density**: Calculate gene density (genes per Mb) for each chromosome.

9. **Build Hierarchy**: Reconstruct gene → transcript → exon hierarchy from flat GFF3.

10. **Convert to BED**: Convert GFF3 gene features to BED format.

### Advanced Level

11. **Alternative Splicing**: Identify genes with multiple transcript isoforms.

12. **UTR Extraction**: Extract 5'UTR and 3'UTR regions for all transcripts.

13. **Intergenic Regions**: Calculate distances between consecutive genes.

14. **Gene Overlap Graph**: Build a network of overlapping genes.

15. **Comparative Annotation**: Compare two GFF3 files (different annotations of same genome) and identify discrepancies.

---

## Key Takeaways

1. **Standard Format**: GFF3 is the modern standard for genome annotations.

2. **9 Columns**: Always tab-delimited: seqid, source, type, start, end, score, strand, phase, attributes.

3. **1-Based Coordinates**: start and end are inclusive (unlike BED format).

4. **Hierarchical Structure**: Use ID/Parent to link genes → transcripts → exons.

5. **Sequence Ontology**: Feature types follow SO controlled vocabulary.

6. **Use gffutils**: For production analysis, convert to SQLite database for speed.

7. **Phase Matters**: Critical for correct CDS translation across exon boundaries.

8. **Validate**: Always validate GFF3 files before using in pipelines.

---

## References

- **GFF3 Specification**: https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md
- **Sequence Ontology**: http://www.sequenceontology.org/
- **Ensembl GFF3**: https://useast.ensembl.org/info/website/upload/gff3.html
- **gffutils Documentation**: https://daler.github.io/gffutils/

---

**Next Steps**: Learn about the GFF3 to database conversion process and why it dramatically improves query performance.
