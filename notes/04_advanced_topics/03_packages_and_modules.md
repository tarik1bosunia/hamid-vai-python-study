# Day 19: Python Packages & Modules for Bioinformatics

## 📦 Master Code Organization & BioPython

Learn to organize code into reusable modules and packages, and leverage powerful bioinformatics libraries like **BioPython**, **NumPy**, and **Pandas** to accelerate your research. Proper code organization is essential for maintainable bioinformatics projects.

### Why Modules & Packages?

- **Code Reusability**: Write once, import everywhere
- **Organization**: Separate concerns (parsing, analysis, visualization)
- **Collaboration**: Share code with team members
- **Standard Libraries**: Access thousands of pre-built tools
- **BioPython**: Professional-grade sequence analysis

---

## 🎯 Learning Objectives

By the end of this guide, you will:

✓ Create and import custom modules  
✓ Organize projects into packages  
✓ Use Python standard library for bioinformatics  
✓ Install and use BioPython effectively  
✓ Leverage NumPy for numerical analysis  
✓ Use Pandas for genomic data tables  
✓ Build professional project structures  

---

## 🧩 Part 1: Python Modules

### Creating Your First Module

Create a file `sequence_utils.py`:

```python
# sequence_utils.py
"""Utility functions for sequence analysis"""

def gc_content(sequence):
    """Calculate GC content percentage"""
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    return (g + c) / len(sequence) * 100 if len(sequence) > 0 else 0

def reverse_complement(sequence):
    """Return reverse complement of DNA sequence"""
    complement = str.maketrans('ATCG', 'TAGC')
    return sequence.upper().translate(complement)[::-1]

def count_nucleotides(sequence):
    """Count each nucleotide"""
    sequence = sequence.upper()
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G')
    }

# Module-level constants
GENETIC_CODE = {
    'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*',
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    # ... (abbreviated for brevity)
}
```

### Importing and Using Modules

```python
# main.py

# Method 1: Import entire module
import sequence_utils

dna = "ATCGATCG"
gc = sequence_utils.gc_content(dna)
print(f"GC content: {gc:.2f}%")

# Method 2: Import specific functions
from sequence_utils import gc_content, reverse_complement

gc = gc_content(dna)
rc = reverse_complement(dna)
print(f"Reverse complement: {rc}")

# Method 3: Import with alias
import sequence_utils as seq

counts = seq.count_nucleotides(dna)
print(f"Nucleotide counts: {counts}")

# Method 4: Import all (not recommended)
from sequence_utils import *
```

### The __name__ Variable

```python
# sequence_utils.py

def gc_content(sequence):
    """Calculate GC content"""
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    return (g + c) / len(sequence) * 100

# This only runs if module is executed directly
if __name__ == "__main__":
    # Test code
    test_seq = "ATCGATCG"
    print(f"Testing GC content: {gc_content(test_seq):.2f}%")
```

When you run `python sequence_utils.py`, the test code executes.  
When you `import sequence_utils`, the test code is skipped.

---

## 🧩 Part 2: Creating Packages

### Package Structure

```
biotools/
    __init__.py          # Makes it a package
    sequences.py         # Sequence functions
    parsers.py          # File parsers
    analysis.py         # Analysis tools
    utils/
        __init__.py
        validation.py    # Validation functions
        conversions.py   # Format conversions
```

### biotools/__init__.py

```python
# biotools/__init__.py
"""BioTools - A bioinformatics toolkit"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import key functions for easy access
from .sequences import gc_content, reverse_complement
from .parsers import parse_fasta, parse_fastq
from .analysis import find_orfs, translate

# Package-level variable
SUPPORTED_FORMATS = ['fasta', 'fastq', 'genbank']

print(f"BioTools v{__version__} loaded")
```

### biotools/sequences.py

```python
# biotools/sequences.py
"""Core sequence manipulation functions"""

def gc_content(sequence):
    """Calculate GC content percentage"""
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    return (g + c) / len(sequence) * 100 if len(sequence) > 0 else 0

def reverse_complement(sequence):
    """Return reverse complement"""
    complement = str.maketrans('ATCGN', 'TAGCN')
    return sequence.upper().translate(complement)[::-1]

def transcribe(dna):
    """Convert DNA to RNA"""
    return dna.upper().replace('T', 'U')

def validate_dna(sequence):
    """Check if sequence is valid DNA"""
    valid_bases = set('ATCGN')
    return set(sequence.upper()).issubset(valid_bases)
```

### biotools/parsers.py

```python
# biotools/parsers.py
"""File format parsers"""

def parse_fasta(text):
    """
    Parse FASTA format
    
    Returns:
        dict: {seq_id: {'description': str, 'sequence': str}}
    """
    records = {}
    current_id = None
    current_desc = None
    current_seq = []
    
    for line in text.strip().splitlines():
        line = line.strip()
        
        if line.startswith('>'):
            # Save previous sequence
            if current_id:
                records[current_id] = {
                    'description': current_desc,
                    'sequence': ''.join(current_seq).upper()
                }
            
            # Parse header
            header = line[1:].strip()
            parts = header.split(maxsplit=1)
            current_id = parts[0]
            current_desc = parts[1] if len(parts) > 1 else ""
            current_seq = []
        else:
            current_seq.append(line)
    
    # Save last sequence
    if current_id:
        records[current_id] = {
            'description': current_desc,
            'sequence': ''.join(current_seq).upper()
        }
    
    return records

def parse_fastq(text):
    """Parse FASTQ format"""
    records = []
    lines = text.strip().split('\n')
    
    for i in range(0, len(lines), 4):
        if i + 3 < len(lines):
            header = lines[i].lstrip('@')
            sequence = lines[i + 1]
            quality = lines[i + 3]
            
            records.append({
                'id': header,
                'sequence': sequence,
                'quality': quality
            })
    
    return records
```

### biotools/analysis.py

```python
# biotools/analysis.py
"""Sequence analysis functions"""

from .sequences import transcribe

def find_orfs(sequence, min_length=30):
    """Find Open Reading Frames"""
    sequence = sequence.upper()
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs = []
    
    i = 0
    while i < len(sequence) - 2:
        if sequence[i:i+3] == start_codon:
            j = i + 3
            while j < len(sequence) - 2:
                if sequence[j:j+3] in stop_codons:
                    orf_seq = sequence[i:j+3]
                    if len(orf_seq) >= min_length:
                        orfs.append({
                            'start': i,
                            'end': j + 3,
                            'sequence': orf_seq,
                            'length': len(orf_seq)
                        })
                    i = j + 3
                    break
                j += 3
            else:
                i += 3
        else:
            i += 3
    
    return orfs

def translate(dna_sequence):
    """Translate DNA to protein"""
    codon_table = {
        'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*',
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TGT': 'C', 'TGC': 'C',
        'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L',
        'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
        'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q',
        'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
        'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = []
    dna = dna_sequence.upper()
    
    for i in range(0, len(dna) - 2, 3):
        codon = dna[i:i+3]
        aa = codon_table.get(codon, 'X')
        if aa == '*':
            break
        protein.append(aa)
    
    return ''.join(protein)
```

### Using Your Package

```python
# main.py

# Import entire package
import biotools

# Use package functions
dna = "ATCGATCGATCG"
gc = biotools.gc_content(dna)
print(f"GC content: {gc:.2f}%")

# Import specific submodules
from biotools import sequences, parsers, analysis

# Use functions
rc = sequences.reverse_complement(dna)
orfs = analysis.find_orfs(dna, min_length=9)

print(f"Reverse complement: {rc}")
print(f"ORFs found: {len(orfs)}")

# Parse FASTA
fasta_text = """>gene1
ATCGATCG
>gene2
GCTAGCTA"""

records = parsers.parse_fasta(fasta_text)
for seq_id, data in records.items():
    print(f"{seq_id}: {len(data['sequence'])} bp")
```

---

## 🧩 Part 3: Standard Library

### os and pathlib - File System

```python
import os
from pathlib import Path

# Using os
current_dir = os.getcwd()
files = os.listdir('.')
file_exists = os.path.exists('sequences.fasta')

# Using pathlib (modern approach)
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)  # Create directory

fasta_files = list(data_dir.glob('*.fasta'))
for file in fasta_files:
    print(f"Found: {file.name}, Size: {file.stat().st_size} bytes")

# Read file
if fasta_files:
    content = fasta_files[0].read_text()
```

### glob - Pattern Matching

```python
import glob

# Find all FASTA files
fasta_files = glob.glob('data/*.fasta')
fastq_files = glob.glob('data/*.fastq')

# Recursive search
all_seq_files = glob.glob('**/*.{fasta,fastq}', recursive=True)

for file in fasta_files:
    print(f"Processing: {file}")
```

### re - Regular Expressions

```python
import re

# Find restriction sites
sequence = "ATCGGAATTCCGATGGATCC"
ecori_sites = [m.start() for m in re.finditer(r'GAATTC', sequence)]
print(f"EcoRI sites at: {ecori_sites}")

# Parse FASTA header
header = ">NM_007294 BRCA1 gene"
match = re.match(r'>(\S+)\s+(.*)', header)
if match:
    seq_id = match.group(1)
    description = match.group(2)
```

### collections - Data Structures

```python
from collections import Counter, defaultdict

# Count nucleotides
sequence = "ATCGATCGATCG"
counts = Counter(sequence)
print(f"Nucleotide counts: {counts}")

# Group sequences by length
sequences = ["ATCG", "AT", "GCTA", "CG"]
by_length = defaultdict(list)

for seq in sequences:
    by_length[len(seq)].append(seq)

print(f"Grouped by length: {dict(by_length)}")
```

### statistics - Basic Stats

```python
import statistics

# Quality scores
quality_scores = [30, 35, 40, 38, 42, 45, 33]

mean_qual = statistics.mean(quality_scores)
median_qual = statistics.median(quality_scores)
stdev_qual = statistics.stdev(quality_scores)

print(f"Mean quality: {mean_qual:.2f}")
print(f"Median quality: {median_qual}")
print(f"Std deviation: {stdev_qual:.2f}")
```

---

## 🧩 Part 4: BioPython

### Installation

```bash
pip install biopython
```

### Working with Sequences

```python
from Bio.Seq import Seq

# Create sequence
dna = Seq("ATCGATCGATCG")

# Basic operations
print(f"Length: {len(dna)}")
print(f"Complement: {dna.complement()}")
print(f"Reverse complement: {dna.reverse_complement()}")

# Transcription
rna = dna.transcribe()
print(f"RNA: {rna}")

# Translation
protein = dna.translate()
print(f"Protein: {protein}")

# Find motif
positions = [i for i in range(len(dna) - 2) if dna[i:i+3] == "ATG"]
print(f"ATG at positions: {positions}")
```

### Parsing FASTA Files

```python
from Bio import SeqIO

# Parse FASTA file
records = list(SeqIO.parse("sequences.fasta", "fasta"))

for record in records:
    print(f"ID: {record.id}")
    print(f"Description: {record.description}")
    print(f"Sequence length: {len(record.seq)}")
    print(f"GC content: {(record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100:.2f}%")
    print()

# Parse single sequence
record = SeqIO.read("single_sequence.fasta", "fasta")
print(f"Loaded: {record.id}")
```

### Writing FASTA Files

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Create records
records = [
    SeqRecord(Seq("ATCGATCG"), id="seq1", description="First sequence"),
    SeqRecord(Seq("GCTAGCTA"), id="seq2", description="Second sequence"),
    SeqRecord(Seq("TAGCTAGC"), id="seq3", description="Third sequence")
]

# Write to file
SeqIO.write(records, "output.fasta", "fasta")
print("Sequences written to output.fasta")
```

### BLAST-like Searching

```python
from Bio import SeqIO
from Bio.Seq import Seq

def find_similar_sequences(query, database_file, max_mismatches=2):
    """Find sequences similar to query"""
    query = str(query).upper()
    matches = []
    
    for record in SeqIO.parse(database_file, "fasta"):
        sequence = str(record.seq).upper()
        
        # Sliding window search
        for i in range(len(sequence) - len(query) + 1):
            window = sequence[i:i+len(query)]
            
            # Count mismatches
            mismatches = sum(1 for a, b in zip(query, window) if a != b)
            
            if mismatches <= max_mismatches:
                matches.append({
                    'record_id': record.id,
                    'position': i,
                    'sequence': window,
                    'mismatches': mismatches
                })
    
    return matches

# Example usage
query = Seq("ATCGATCG")
# matches = find_similar_sequences(query, "database.fasta", max_mismatches=1)
```

### Sequence Analysis

```python
from Bio.SeqUtils import GC, molecular_weight
from Bio.Seq import Seq

dna = Seq("ATCGATCGATCGATCG")

# GC content
gc_percent = GC(dna)
print(f"GC content: {gc_percent:.2f}%")

# Molecular weight
mw = molecular_weight(dna)
print(f"Molecular weight: {mw:.2f} Da")

# Translate in all frames
for frame in range(3):
    protein = dna[frame:].translate()
    print(f"Frame +{frame+1}: {protein}")
```

---

## 🧩 Part 5: NumPy for Bioinformatics

### Installation & Basics

```bash
pip install numpy
```

```python
import numpy as np

# Create arrays for sequence data
quality_scores = np.array([30, 35, 40, 38, 42, 45, 33, 36])

# Basic statistics
print(f"Mean quality: {quality_scores.mean():.2f}")
print(f"Std dev: {quality_scores.std():.2f}")
print(f"Min quality: {quality_scores.min()}")
print(f"Max quality: {quality_scores.max()}")

# Filter high-quality positions
high_quality = quality_scores > 35
print(f"High quality positions: {np.where(high_quality)[0]}")
```

### Sequence Encoding

```python
import numpy as np

def encode_sequence(sequence):
    """Convert DNA to numerical encoding"""
    encoding = {'A': 0, 'T': 1, 'C': 2, 'G': 3, 'N': 4}
    return np.array([encoding.get(base, 4) for base in sequence.upper()])

def decode_sequence(encoded):
    """Convert numerical back to DNA"""
    decoding = {0: 'A', 1: 'T', 2: 'C', 3: 'G', 4: 'N'}
    return ''.join(decoding[code] for code in encoded)

# Test
dna = "ATCGATCG"
encoded = encode_sequence(dna)
print(f"Original: {dna}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decode_sequence(encoded)}")

# Vectorized operations
sequences = ["ATCG", "GCTA", "TAGC"]
encoded_seqs = np.array([encode_sequence(seq) for seq in sequences])
print(f"Batch encoded shape: {encoded_seqs.shape}")
```

### Position Weight Matrix (PWM)

```python
import numpy as np

def create_pwm(sequences):
    """Create Position Weight Matrix from aligned sequences"""
    # Encode sequences
    encoding = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
    encoded = np.array([[encoding[base] for base in seq] for seq in sequences])
    
    # Count nucleotides at each position
    pwm = np.zeros((4, encoded.shape[1]))
    
    for pos in range(encoded.shape[1]):
        for nuc in range(4):
            pwm[nuc, pos] = np.sum(encoded[:, pos] == nuc)
    
    # Convert to frequencies
    pwm = pwm / len(sequences)
    
    return pwm

# Test with aligned sequences
motif_sequences = [
    "ATCG",
    "ATGG",
    "ATCG",
    "ACCG"
]

pwm = create_pwm(motif_sequences)
print("Position Weight Matrix:")
print("   Pos1  Pos2  Pos3  Pos4")
for i, base in enumerate(['A', 'T', 'C', 'G']):
    print(f"{base}: {pwm[i]}")
```

---

## 🧩 Part 6: Pandas for Genomic Data

### Installation & Basics

```bash
pip install pandas
```

```python
import pandas as pd

# Create DataFrame from genomic data
data = {
    'gene_id': ['BRCA1', 'TP53', 'EGFR', 'KRAS'],
    'chromosome': ['chr17', 'chr17', 'chr7', 'chr12'],
    'start': [43044295, 7668421, 55019017, 25205246],
    'end': [43170245, 7687490, 55211628, 25250929],
    'expression': [125.5, 342.1, 89.3, 201.7]
}

df = pd.DataFrame(data)
print(df)
```

### Gene Expression Analysis

```python
import pandas as pd
import numpy as np

# Load expression data
expression_data = {
    'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC'],
    'sample1': [120, 300, 80, 190, 150],
    'sample2': [125, 310, 85, 195, 155],
    'sample3': [118, 295, 78, 188, 148]
}

df = pd.DataFrame(expression_data)

# Calculate mean expression
df['mean_expression'] = df[['sample1', 'sample2', 'sample3']].mean(axis=1)

# Calculate fold change
df['fold_change'] = df['sample2'] / df['sample1']

# Filter highly expressed genes
high_expression = df[df['mean_expression'] > 150]

print(df)
print(f"\nHighly expressed genes:\n{high_expression}")
```

### Variant Analysis

```python
import pandas as pd

# VCF-like data
variants = {
    'chr': ['chr1', 'chr1', 'chr2', 'chr3'],
    'pos': [12345, 67890, 11111, 22222],
    'ref': ['A', 'C', 'G', 'T'],
    'alt': ['G', 'T', 'A', 'C'],
    'quality': [30, 45, 35, 40],
    'gene': ['BRCA1', 'TP53', 'EGFR', 'KRAS']
}

df = pd.DataFrame(variants)

# Filter by quality
high_quality = df[df['quality'] > 35]

# Group by chromosome
by_chr = df.groupby('chr').size()

print("All variants:")
print(df)
print(f"\nHigh quality variants:\n{high_quality}")
print(f"\nVariants per chromosome:\n{by_chr}")
```

### Reading Files

```python
import pandas as pd

# Read CSV
# df = pd.read_csv('gene_expression.csv')

# Read tab-delimited
# df = pd.read_csv('annotations.tsv', sep='\t')

# Read Excel
# df = pd.read_excel('results.xlsx', sheet_name='Sheet1')

# Example with sample data
df = pd.read_csv('data.csv') if Path('data.csv').exists() else pd.DataFrame()
```

---

## 📝 Practice Tasks (Day 19)

### Basic Exercises

1. **Simple Module**: Create `dna_tools.py` with 3 functions for GC content, reverse complement, and translation.

2. **Import Practice**: Write a script that imports and uses all functions from your module.

3. **Standard Library**: Use `glob` to find all `.fasta` files in a directory.

4. **Collections**: Use `Counter` to count codon frequencies in a sequence.

5. **BioPython Basics**: Parse a FASTA file and print sequence IDs and lengths.

### Intermediate Challenges

6. **Package Creation**: Create a package `seq_analysis` with submodules for parsing, analysis, and utilities.

7. **File Processing**: Use BioPython to read FASTA, calculate GC content, and write filtered sequences to new file.

8. **NumPy Analysis**: Encode DNA sequences as NumPy arrays and perform vectorized GC% calculation.

9. **Pandas Filtering**: Create DataFrame of genes with expression values, filter and sort.

10. **Module with Tests**: Create module with `if __name__ == "__main__":` block containing test cases.

### Advanced Challenges

11. **Complete Package**: Build a full package with `__init__.py`, multiple modules, and proper imports.

12. **Batch Processing**: Use BioPython to process multiple FASTA files and generate summary statistics.

13. **PWM Scanner**: Implement Position Weight Matrix scanner using NumPy for motif finding.

14. **Expression Pipeline**: Build Pandas-based pipeline to load, normalize, filter, and export gene expression data.

15. **Integration Project**: Combine BioPython, NumPy, and Pandas to analyze sequences, calculate statistics, and export to CSV.

---

## 💡 Key Takeaways

✓ **Modules** are single Python files with functions/classes  
✓ **Packages** are directories with `__init__.py` containing modules  
✓ **import** loads code from other files  
✓ **from ... import ...** imports specific items  
✓ **if __name__ == "__main__":** enables testing within modules  
✓ **BioPython** provides professional sequence analysis tools  
✓ **SeqIO** handles multiple file formats (FASTA, FASTQ, GenBank)  
✓ **NumPy** enables fast numerical operations on sequences  
✓ **Pandas** excels at tabular genomic data (variants, expression)  
✓ **Standard library** has tools for files, regex, stats  
✓ **Organize code** by functionality (parsing, analysis, I/O)  
✓ **Document modules** with docstrings  
✓ **Use virtual environments** to manage dependencies  
✓ **Install packages** with `pip install package_name`  
✓ **Read documentation** - official docs are invaluable  

**Next**: Virtual Environments & Project Management
