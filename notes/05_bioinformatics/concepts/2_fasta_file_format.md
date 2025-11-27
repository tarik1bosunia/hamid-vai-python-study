# FASTA File Format - Complete Guide

## Introduction

The **FASTA format** is the most widely used file format in bioinformatics for representing biological sequences (DNA, RNA, or proteins). Introduced in 1985 with the FASTA alignment program by William Pearson and David Lipman, it remains the standard for sequence data exchange due to its simplicity and human-readability.

**Common Uses:**
- Genome assembly and annotation
- Sequence database storage (GenBank, NCBI, Ensembl, UniProt)
- Input for BLAST, alignment tools, and annotation pipelines
- Protein structure prediction (AlphaFold, RoseTTAFold)
- Metagenomics and transcriptomics data

**Key Advantage**: Plain text format that's easy to parse, view, and edit with any text editor.

---

## FASTA File Structure

A FASTA file contains **one or more sequence records**. Each record has two components:

### 1. Header Line (Description Line)

**Format:**
```
>identifier optional_description
```

**Rules:**
- **Must start with `>`** (greater-than symbol)
- First word after `>` is the **unique identifier** (no spaces)
- Everything after the first space is the **description** (optional)
- Header must be on a single line

**Examples:**
```fasta
>gene1
>NM_000546.6 Homo sapiens tumor protein p53
>sp|P04637|P53_HUMAN Cellular tumor antigen p53
>chr1:1000-2000 (+)
```

### 2. Sequence Lines

**Format:**
- One or more lines containing the biological sequence
- Can be written as single long line or wrapped to 60-80 characters
- Case-insensitive (ATGC or atgc both valid)

**Valid Characters:**

| Molecule Type | Characters | Notes |
|---------------|------------|-------|
| **DNA** | A, T, G, C, N | N = any nucleotide |
| **RNA** | A, U, G, C, N | U instead of T |
| **Protein** | 20 amino acids + X, B, Z | X = unknown, B = Asp/Asn, Z = Glu/Gln |

**IUPAC Ambiguity Codes** (DNA/RNA):
- R = A/G (puRine)
- Y = C/T (pYrimidine)
- M = A/C, K = G/T, S = G/C, W = A/T
- B = not A, D = not C, H = not G, V = not T
- N = any nucleotide

---

## Complete FASTA Examples

### Single Sequence

```fasta
>seq1 Human beta-globin gene
ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAA
CGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCC
AGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCT
AAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCT
GGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACG
TGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCAC
TTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGT
GGCTAATGCCCTGGCCCACAAGTATCACTAA
```

### Multiple Sequences

```fasta
>gene1 cytochrome c
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKN
KGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE

>gene2 histone H4
MSGRGKGGKGLGKGGAKRHRKVLRDNIQGITKPAIRRLARRGGVKRISGLIYEETR
GVLKVFLENVIRDAVTYTEHAKRKTVTAMDVVYALKRQGRTLYGFGG

>gene3 insulin precursor
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRRE
AEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN
```

---

## Parsing FASTA Files in Python

### Method 1: Manual Parsing (No Dependencies)

```python
def parse_fasta(filename: str) -> dict:
    """
    Parse FASTA file and return dictionary of sequences.
    
    Args:
        filename: Path to FASTA file
        
    Returns:
        Dictionary with sequence IDs as keys and sequences as values
    """
    sequences = {}
    current_id = None
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('>'):
                # Save previous sequence if exists
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                
                # Start new sequence
                current_id = line[1:].split()[0]  # Get ID (first word)
                current_seq = []
            else:
                # Accumulate sequence lines
                current_seq.append(line)
        
        # Don't forget the last sequence
        if current_id:
            sequences[current_id] = ''.join(current_seq)
    
    return sequences

# Usage
seqs = parse_fasta('genome.fasta')
for seq_id, sequence in seqs.items():
    print(f"{seq_id}: {len(sequence)} bp")
```

### Method 2: Using BioPython (Recommended)

```python
from Bio import SeqIO

def parse_fasta_biopython(filename: str):
    """Parse FASTA using BioPython SeqIO."""
    sequences = {}
    
    for record in SeqIO.parse(filename, "fasta"):
        sequences[record.id] = str(record.seq)
        print(f"ID: {record.id}")
        print(f"Description: {record.description}")
        print(f"Sequence length: {len(record.seq)}")
        print(f"First 50 bp: {record.seq[:50]}")
        print()
    
    return sequences

# Usage
seqs = parse_fasta_biopython('proteins.fasta')
```

### Method 3: Generator for Large Files

```python
def fasta_generator(filename: str):
    """
    Memory-efficient FASTA parser for large files.
    Yields one sequence at a time.
    """
    with open(filename, 'r') as f:
        header = None
        sequence = []
        
        for line in f:
            line = line.strip()
            
            if line.startswith('>'):
                if header:
                    yield header, ''.join(sequence)
                header = line[1:]
                sequence = []
            else:
                sequence.append(line)
        
        # Yield last sequence
        if header:
            yield header, ''.join(sequence)

# Usage - processes one sequence at a time (memory efficient)
for header, seq in fasta_generator('large_genome.fasta'):
    print(f"{header}: {len(seq)} bp")
    # Process each sequence without loading entire file into memory
```

---

## Writing FASTA Files

### Creating FASTA Output

```python
def write_fasta(sequences: dict, output_file: str, line_width: int = 60):
    """
    Write sequences to FASTA format.
    
    Args:
        sequences: Dictionary {seq_id: sequence}
        output_file: Output filename
        line_width: Number of characters per line (default 60)
    """
    with open(output_file, 'w') as f:
        for seq_id, sequence in sequences.items():
            # Write header
            f.write(f'>{seq_id}\n')
            
            # Write sequence in wrapped lines
            for i in range(0, len(sequence), line_width):
                f.write(sequence[i:i+line_width] + '\n')

# Example usage
sequences = {
    'gene1': 'ATGCGTAAACCGATGGGCTTTTGA',
    'gene2': 'ATGGGCAAATTTCCCTAG'
}

write_fasta(sequences, 'output.fasta')
```

### Using BioPython to Write FASTA

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

def write_fasta_biopython(sequences: dict, output_file: str):
    """Write FASTA using BioPython."""
    records = []
    
    for seq_id, sequence in sequences.items():
        record = SeqRecord(
            Seq(sequence),
            id=seq_id,
            description=""
        )
        records.append(record)
    
    SeqIO.write(records, output_file, "fasta")

# Usage
write_fasta_biopython(sequences, 'output.fasta')
```

---

## Bioinformatics Applications

### 1. Extracting Sequences by Criteria

```python
def filter_fasta_by_length(input_file: str, output_file: str, 
                           min_len: int, max_len: int = float('inf')):
    """
    Filter FASTA sequences by length range.
    Useful for filtering contigs, ORFs, or quality control.
    """
    from Bio import SeqIO
    
    filtered = []
    stats = {'total': 0, 'kept': 0, 'filtered': 0}
    
    for record in SeqIO.parse(input_file, "fasta"):
        stats['total'] += 1
        seq_len = len(record.seq)
        
        if min_len <= seq_len <= max_len:
            filtered.append(record)
            stats['kept'] += 1
        else:
            stats['filtered'] += 1
    
    SeqIO.write(filtered, output_file, "fasta")
    
    print(f"Total sequences: {stats['total']}")
    print(f"Kept: {stats['kept']}")
    print(f"Filtered out: {stats['filtered']}")
    
    return stats

# Example: Keep only sequences between 500-5000 bp
filter_fasta_by_length('genome.fasta', 'filtered.fasta', 500, 5000)
```

### 2. Calculate Sequence Statistics

```python
def fasta_statistics(filename: str):
    """
    Calculate comprehensive statistics for FASTA file.
    """
    from Bio import SeqIO
    from collections import Counter
    
    lengths = []
    gc_contents = []
    total_bases = 0
    nucleotide_counts = Counter()
    
    for record in SeqIO.parse(filename, "fasta"):
        seq = str(record.seq).upper()
        lengths.append(len(seq))
        total_bases += len(seq)
        
        # Count nucleotides
        nucleotide_counts.update(seq)
        
        # GC content
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        gc_contents.append(gc)
    
    # Calculate N50 (important for genome assemblies)
    lengths.sort(reverse=True)
    cumsum = 0
    n50 = 0
    for length in lengths:
        cumsum += length
        if cumsum >= total_bases / 2:
            n50 = length
            break
    
    stats = {
        'num_sequences': len(lengths),
        'total_bases': total_bases,
        'min_length': min(lengths),
        'max_length': max(lengths),
        'mean_length': sum(lengths) / len(lengths),
        'n50': n50,
        'mean_gc': sum(gc_contents) / len(gc_contents),
        'nucleotide_composition': dict(nucleotide_counts)
    }
    
    return stats

# Usage
stats = fasta_statistics('genome.fasta')
print(f"Number of sequences: {stats['num_sequences']}")
print(f"Total bases: {stats['total_bases']:,}")
print(f"N50: {stats['n50']}")
print(f"Mean GC%: {stats['mean_gc']:.2f}%")
```

### 3. Reverse Complement Sequences

```python
def reverse_complement_fasta(input_file: str, output_file: str):
    """
    Generate reverse complement of all sequences.
    Useful for analyzing both strands.
    """
    from Bio import SeqIO
    
    rev_comp_records = []
    
    for record in SeqIO.parse(input_file, "fasta"):
        # BioPython automatically handles reverse complement
        rev_record = record.reverse_complement()
        rev_record.id = record.id + "_revcomp"
        rev_record.description = "reverse complement of " + record.description
        rev_comp_records.append(rev_record)
    
    SeqIO.write(rev_comp_records, output_file, "fasta")
    print(f"Generated {len(rev_comp_records)} reverse complement sequences")

# Usage
reverse_complement_fasta('genes.fasta', 'genes_revcomp.fasta')
```

### 4. Extract Subsequences (Slicing)

```python
def extract_region(input_file: str, seq_id: str, start: int, end: int, 
                   output_file: str):
    """
    Extract specific region from a sequence.
    Coordinates are 1-based, inclusive (like genomic coordinates).
    """
    from Bio import SeqIO
    
    for record in SeqIO.parse(input_file, "fasta"):
        if record.id == seq_id:
            # Convert to 0-based indexing
            subseq = record.seq[start-1:end]
            
            new_record = SeqRecord(
                subseq,
                id=f"{record.id}_{start}-{end}",
                description=f"region {start}-{end} of {record.description}"
            )
            
            SeqIO.write([new_record], output_file, "fasta")
            print(f"Extracted {len(subseq)} bp from {seq_id}")
            return
    
    print(f"Sequence {seq_id} not found")

# Extract bases 1000-2000 from chr1
extract_region('genome.fasta', 'chr1', 1000, 2000, 'region.fasta')
```

### 5. Merge Multiple FASTA Files

```python
def merge_fasta_files(input_files: list, output_file: str):
    """
    Combine multiple FASTA files into one.
    Useful for consolidating data from different sources.
    """
    from Bio import SeqIO
    
    all_records = []
    
    for input_file in input_files:
        records = list(SeqIO.parse(input_file, "fasta"))
        all_records.extend(records)
        print(f"{input_file}: {len(records)} sequences")
    
    SeqIO.write(all_records, output_file, "fasta")
    print(f"\nTotal: {len(all_records)} sequences merged")

# Usage
merge_fasta_files(['genes1.fasta', 'genes2.fasta', 'genes3.fasta'], 
                  'all_genes.fasta')
```

### 6. Convert FASTA to Tab-Delimited Format

```python
def fasta_to_table(input_file: str, output_file: str):
    """
    Convert FASTA to tab-delimited table (easier for Excel/R/pandas).
    """
    from Bio import SeqIO
    
    with open(output_file, 'w') as out:
        out.write("ID\tDescription\tLength\tSequence\n")
        
        for record in SeqIO.parse(input_file, "fasta"):
            out.write(f"{record.id}\t")
            out.write(f"{record.description}\t")
            out.write(f"{len(record.seq)}\t")
            out.write(f"{str(record.seq)}\n")
    
    print(f"Converted to table format: {output_file}")

# Usage
fasta_to_table('sequences.fasta', 'sequences.tsv')
```

### 7. Remove Duplicate Sequences

```python
def remove_duplicates(input_file: str, output_file: str):
    """
    Remove duplicate sequences, keeping only unique ones.
    """
    from Bio import SeqIO
    
    seen_sequences = set()
    unique_records = []
    
    for record in SeqIO.parse(input_file, "fasta"):
        seq_str = str(record.seq)
        
        if seq_str not in seen_sequences:
            seen_sequences.add(seq_str)
            unique_records.append(record)
    
    SeqIO.write(unique_records, output_file, "fasta")
    
    total = len(seen_sequences) + (len(list(SeqIO.parse(input_file, "fasta"))) - len(unique_records))
    print(f"Original: {total} sequences")
    print(f"Unique: {len(unique_records)} sequences")
    print(f"Removed: {total - len(unique_records)} duplicates")

# Usage
remove_duplicates('all_seqs.fasta', 'unique_seqs.fasta')
```

---

## Common FASTA Variations

### Multi-line FASTA (Standard)
```fasta
>seq1
ATGCGTAAACCGATGGGCTTTTGATAGCCCATGAAATAAGGCCCATGCGT
AAACCGATGGGCTTTTGATAGCCCATGAAATAAGGCCC
```

### Single-line FASTA
```fasta
>seq1
ATGCGTAAACCGATGGGCTTTTGATAGCCCATGAAATAAGGCCCATGCGTAAACCGATGGGCTTTTGATAGCCCATGAAATAAGGCCC
```

### FASTA with Complex Headers
```fasta
>gi|568815597|ref|NC_000913.3| Escherichia coli str. K-12 substr. MG1655, complete genome
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens OX=9606 GN=TP53 PE=1 SV=4
>lcl|chr1 chromosome 1, reference assembly, Homo sapiens
```

---

## Practice Exercises

### Basic Level

1. **Parse and Count**: Parse a FASTA file and count how many sequences it contains.

2. **Calculate Lengths**: Print the ID and length of each sequence in a FASTA file.

3. **Extract by ID**: Write a function to extract a specific sequence by its ID.

4. **GC Content**: Calculate GC% for each sequence in a multi-FASTA file.

5. **Uppercase Conversion**: Read FASTA, convert all sequences to uppercase, write new file.

### Intermediate Level

6. **Length Filter**: Filter sequences keeping only those between 500-2000 bp.

7. **Find Motifs**: Search for a specific motif (e.g., "TATAAA") in all sequences and report positions.

8. **Rename Headers**: Batch rename sequence IDs (e.g., add prefix "gene_").

9. **Split Multi-FASTA**: Split a multi-sequence FASTA into individual files (one per sequence).

10. **Calculate N50**: Implement N50 calculation for genome assembly assessment.

### Advanced Level

11. **Quality Filter**: Remove sequences with >5% ambiguous nucleotides (N characters).

12. **Translate All Frames**: Translate DNA sequences to proteins in all 6 reading frames.

13. **Find Open Reading Frames**: Extract all ORFs >300 bp and write to new FASTA.

14. **Codon Usage**: Calculate codon usage frequency table from coding sequences.

15. **BLAST Database Prep**: Parse UniProt FASTA headers and extract organism information, create summary table.

---

## Key Takeaways

1. **Universal Format**: FASTA is the most widely used sequence format - master it first.

2. **Simple Structure**: `>header` followed by sequence lines - easy to parse and write.

3. **Header Parsing**: Only the first word after `>` is the ID; rest is description.

4. **Line Wrapping**: Sequences can be one long line or wrapped (typically 60-80 characters).

5. **Case Insensitive**: ATGC and atgc are equivalent, but uppercase is conventional.

6. **Use BioPython**: For production code, use BioPython's SeqIO - handles edge cases.

7. **Memory Efficiency**: Use generators for large files (multi-GB genomes).

8. **Validation**: Always validate sequence characters match expected molecule type (DNA/RNA/protein).

---

## Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| **Wrapped lines** | Concatenate all lines until next `>` |
| **Blank lines** | Skip empty lines with `if line.strip()` |
| **Windows line endings** | Open with `open(file, 'r', newline='')` or use `.strip()` |
| **Large files** | Use generators, don't load entire file into memory |
| **Duplicate IDs** | Check for uniqueness, add suffix if needed |
| **Invalid characters** | Validate against allowed nucleotide/protein codes |

---

## References

- **NCBI FASTA Format**: https://www.ncbi.nlm.nih.gov/genbank/fastaformat/
- **BioPython Tutorial**: http://biopython.org/DIST/docs/tutorial/Tutorial.html
- **UniProt FASTA Headers**: https://www.uniprot.org/help/fasta-headers
- **Sequence Ontology**: http://www.sequenceontology.org/

---

**Next Steps**: Learn about other sequence formats (FASTQ, GenBank, GFF) and when to use each one.
