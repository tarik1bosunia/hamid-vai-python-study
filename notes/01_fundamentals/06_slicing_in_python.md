# Day 6: Slicing in Python

## 🔪 Understanding Slicing

**Slicing** is one of Python's most powerful features for working with sequences. It allows you to extract portions of strings, lists, tuples, and other sequence types efficiently. For bioinformatics, slicing is essential for extracting sequence regions, codons, and analyzing specific portions of genetic data.

### Why Slicing Matters in Bioinformatics

- Extract specific regions from DNA/RNA sequences
- Get codons (triplets) from sequences
- Analyze primers and restriction sites
- Extract exons from genes
- Reverse sequences for complement calculations
- Process large datasets efficiently

---

## 🔹 Slicing Syntax

### General Format

```python
sequence[start:stop:step]
```

**Parameters:**
- **start**: Beginning index (inclusive) - where to start slicing
- **stop**: Ending index (exclusive) - where to stop (not included)
- **step**: Skip interval - how many items to skip (default: 1)

**Defaults:**
- If `start` is omitted: starts from beginning (index 0)
- If `stop` is omitted: goes to end
- If `step` is omitted: step of 1 (every element)

### Index System

```python
text = "ATCGATCG"
#      01234567    (positive indices)
#      -8-7-6-5-4-3-2-1  (negative indices)

# Positive indices count from left (start)
# Negative indices count from right (end)
```

---

## ✅ String Slicing

Strings are the most common sequence type in bioinformatics. Mastering string slicing is crucial!

### Basic String Slicing

```python
dna = "ATCGATCG"

# Extract subsequences
print(dna[0:4])    # ATCG (indices 0,1,2,3)
print(dna[2:6])    # CGAT (indices 2,3,4,5)
print(dna[4:8])    # ATCG (indices 4,5,6,7)

# Omit start or stop
print(dna[:4])     # ATCG (from beginning to index 4)
print(dna[4:])     # ATCG (from index 4 to end)
print(dna[:])      # ATCGATCG (entire string - makes a copy)

# Negative indices
print(dna[-4:])    # ATCG (last 4 characters)
print(dna[:-4])    # ATCG (all except last 4)
print(dna[-6:-2])  # CGAT (from -6 to -2)

# Using step
print(dna[::2])    # ACAC (every 2nd character)
print(dna[::3])    # AGT (every 3rd character)
print(dna[1::2])   # TCGG (start at 1, every 2nd)

# Reverse string
print(dna[::-1])   # GCTAGCTA (reversed)
```

### Advanced String Slicing

```python
sequence = "ATCGATCGATCGATCG"

# Extract every third base (codon analysis)
first_codon_positions = sequence[0::3]   # AGAG
second_codon_positions = sequence[1::3]  # TCAC
third_codon_positions = sequence[2::3]   # GTTG

print(f"1st positions: {first_codon_positions}")
print(f"2nd positions: {second_codon_positions}")
print(f"3rd positions: {third_codon_positions}")

# Extract codons
codon1 = sequence[0:3]    # ATC
codon2 = sequence[3:6]    # GAT
codon3 = sequence[6:9]    # CGA
codon4 = sequence[9:12]   # TCG

# Get all codons using a loop
codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
print(f"Codons: {codons}")

# Reverse complement preparation (just reversal)
reversed_seq = sequence[::-1]
print(f"Reversed: {reversed_seq}")

# Get middle portion
length = len(sequence)
quarter = length // 4
middle_half = sequence[quarter:-quarter]
print(f"Middle half: {middle_half}")
```

### Bioinformatics String Examples

```python
# FASTA sequence (header + sequence)
fasta = ">seq001|gene=BRCA1\nATCGATCGATCGATCG"

# Extract header and sequence
lines = fasta.split('\n')
header = lines[0][1:]  # Remove '>' character
sequence = lines[1]

print(f"Header: {header}")
print(f"Sequence: {sequence}")

# Extract gene name from header
gene_info = header.split('|')[1]  # "gene=BRCA1"
gene_name = gene_info.split('=')[1]  # "BRCA1"
print(f"Gene: {gene_name}")

# Get primer regions
forward_primer = sequence[:20]   # First 20 bases
reverse_primer = sequence[-20:]  # Last 20 bases

print(f"Forward primer: {forward_primer}")
print(f"Reverse primer: {reverse_primer}")

# Extract ORF region (example: positions 10-50)
orf = sequence[10:50]
print(f"ORF region: {orf}")

# Get reading frames
frame1 = sequence[0:]    # Frame 1
frame2 = sequence[1:]    # Frame 2
frame3 = sequence[2:]    # Frame 3

print(f"Frame 1: {frame1[:30]}...")
print(f"Frame 2: {frame2[:30]}...")
print(f"Frame 3: {frame3[:30]}...")
```

---

## ✅ List Slicing

Lists support all the same slicing operations as strings, but since lists are mutable, you can also assign to slices!

### Basic List Slicing

```python
bases = ['A', 'T', 'C', 'G', 'A', 'T', 'C', 'G']

# Extract sublists
print(bases[0:4])    # ['A', 'T', 'C', 'G']
print(bases[2:6])    # ['C', 'G', 'A', 'T']
print(bases[:4])     # ['A', 'T', 'C', 'G']
print(bases[4:])     # ['A', 'T', 'C', 'G']

# With step
print(bases[::2])    # ['A', 'C', 'A', 'C'] (every 2nd)
print(bases[1::2])   # ['T', 'G', 'T', 'G'] (start at 1, every 2nd)

# Reverse list
print(bases[::-1])   # ['G', 'C', 'T', 'A', 'G', 'C', 'T', 'A']

# Copy a list
bases_copy = bases[:]
print(bases_copy)
```

### Modifying Lists with Slices

```python
genes = ['BRCA1', 'TP53', 'EGFR', 'KRAS', 'MYC']

# Replace elements
genes[1:3] = ['BRAF', 'ALK']
print(genes)  # ['BRCA1', 'BRAF', 'ALK', 'KRAS', 'MYC']

# Insert elements (empty slice)
genes[2:2] = ['NRAS', 'HRAS']
print(genes)  # ['BRCA1', 'BRAF', 'NRAS', 'HRAS', 'ALK', 'KRAS', 'MYC']

# Delete elements
genes[2:4] = []
print(genes)  # ['BRCA1', 'BRAF', 'ALK', 'KRAS', 'MYC']

# Replace with different number of elements
genes[0:2] = ['TP53']
print(genes)  # ['TP53', 'ALK', 'KRAS', 'MYC']

# Delete using del
del genes[1:3]
print(genes)  # ['TP53', 'MYC']
```

### Bioinformatics List Examples

```python
# Quality scores for a sequence
quality_scores = [30, 32, 35, 28, 40, 38, 35, 33, 29, 31]

# Get first 5 scores
first_five = quality_scores[:5]
print(f"First 5 scores: {first_five}")

# Get last 5 scores
last_five = quality_scores[-5:]
print(f"Last 5 scores: {last_five}")

# Get middle scores (skip first and last 2)
middle_scores = quality_scores[2:-2]
print(f"Middle scores: {middle_scores}")

# Get every other score
alternate_scores = quality_scores[::2]
print(f"Alternate scores: {alternate_scores}")

# Gene expression data
expression_values = [5.2, 8.7, 3.1, 12.4, 6.8, 9.3, 4.5, 11.2]

# Get highly expressed genes (top 3)
sorted_expression = sorted(expression_values, reverse=True)
top_3 = sorted_expression[:3]
print(f"Top 3 expression values: {top_3}")

# Sequence fragments
fragments = ['ATCG', 'GCTA', 'TAGC', 'CGAT', 'ATGC']

# Get first 3 fragments
first_three = fragments[:3]
print(f"First 3 fragments: {first_three}")

# Get last 2 fragments
last_two = fragments[-2:]
print(f"Last 2 fragments: {last_two}")

# Reverse fragment order
reversed_fragments = fragments[::-1]
print(f"Reversed: {reversed_fragments}")

# Take every second fragment
every_second = fragments[::2]
print(f"Every second: {every_second}")
```

---

## ✅ Tuple Slicing

Tuples support slicing just like strings and lists, but remember they're immutable, so you can't assign to slices.

### Basic Tuple Slicing

```python
coordinates = (12, 45, 78, 90, 123, 156, 189)

# Extract sub-tuples
print(coordinates[0:3])    # (12, 45, 78)
print(coordinates[2:5])    # (78, 90, 123)
print(coordinates[:4])     # (12, 45, 78, 90)
print(coordinates[4:])     # (123, 156, 189)

# With step
print(coordinates[::2])    # (12, 78, 123, 189)
print(coordinates[1::2])   # (45, 90, 156)

# Reverse tuple
print(coordinates[::-1])   # (189, 156, 123, 90, 78, 45, 12)
```

### Bioinformatics Tuple Examples

```python
# Gene positions (chromosome, start, end)
gene_positions = (
    ('chr1', 1000, 2000),
    ('chr1', 5000, 6000),
    ('chr2', 3000, 4000),
    ('chr2', 7000, 8000),
    ('chr3', 2000, 3000)
)

# Get genes on first 2 chromosomes
first_two_chr = gene_positions[:4]
print(f"First two chromosomes: {first_two_chr}")

# Get every other gene
alternate_genes = gene_positions[::2]
print(f"Alternate genes: {alternate_genes}")

# SNP data (position, ref, alt, frequency)
snps = (
    (12345, 'A', 'G', 0.25),
    (23456, 'T', 'C', 0.15),
    (34567, 'G', 'A', 0.30),
    (45678, 'C', 'T', 0.20)
)

# Get first 2 SNPs
first_two_snps = snps[:2]
print(f"First 2 SNPs: {first_two_snps}")

# Extract positions only
positions = tuple(snp[0] for snp in snps)
print(f"SNP positions: {positions}")
```

---

## ✅ Advanced Slicing Techniques

### Slicing with Negative Step

```python
sequence = "ATCGATCG"

# Reverse with negative step
print(sequence[::-1])     # GCTAGCTA

# Every 2nd character, reversed
print(sequence[::-2])     # GCAC

# Slice backwards
print(sequence[7:3:-1])   # GCTA (from index 7 to 4, backwards)
print(sequence[6:2:-1])   # CTAG (from index 6 to 3, backwards)

# Start from end, go backwards
print(sequence[-1:-5:-1]) # GCTA (last 4, reversed)
```

### Nested Sequence Slicing

```python
# 2D sequence data
matrix = [
    ['A', 'T', 'C', 'G'],
    ['G', 'C', 'T', 'A'],
    ['T', 'A', 'G', 'C'],
    ['C', 'G', 'A', 'T']
]

# Slice rows
first_two_rows = matrix[0:2]
print(f"First 2 rows: {first_two_rows}")

# Slice within a row
first_row_subset = matrix[0][1:3]
print(f"Row 0, cols 1-2: {first_row_subset}")  # ['T', 'C']

# Get first two elements of each row
first_two_cols = [row[:2] for row in matrix]
print(f"First 2 columns: {first_two_cols}")

# Get diagonal (requires loop)
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Diagonal: {diagonal}")  # ['A', 'C', 'G', 'T']

# Reverse each row
reversed_rows = [row[::-1] for row in matrix]
print(f"Reversed rows: {reversed_rows}")
```

### Slicing for Data Analysis

```python
# Sequence reads with quality scores
reads = [
    "ATCGATCG",
    "GCTAGCTA",
    "TAGCTAGC",
    "CGATCGAT"
]

quality_scores = [
    [30, 32, 35, 28, 40, 38, 35, 33],
    [28, 30, 32, 35, 38, 40, 35, 30],
    [35, 38, 40, 35, 30, 28, 32, 35],
    [40, 38, 35, 33, 30, 32, 35, 38]
]

# Trim first and last 2 bases (low quality at ends)
trimmed_reads = [read[2:-2] for read in reads]
trimmed_scores = [scores[2:-2] for scores in quality_scores]

print("Trimmed reads:")
for read, scores in zip(trimmed_reads, trimmed_scores):
    print(f"  {read} -> {scores}")

# Get first half of each read
first_halves = [read[:len(read)//2] for read in reads]
print(f"First halves: {first_halves}")

# Get middle 4 bases
middle_4 = [read[2:6] for read in reads]
print(f"Middle 4 bases: {middle_4}")
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: Codon Extraction

```python
def extract_codons(sequence):
    """Extract all codons from a sequence"""
    codons = []
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:  # Only complete codons
            codons.append(codon)
    return codons

mrna = "AUGUCGGCUAAACCCGGGAAA"
codons = extract_codons(mrna)
print(f"Codons: {codons}")
# Output: ['AUG', 'UCG', 'GCU', 'AAA', 'CCC', 'GGG', 'AAA']
```

### Example 2: Extract ORF

```python
def find_orfs(sequence):
    """Find Open Reading Frames (simplified)"""
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    orfs = []
    
    # Find all start positions
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            # Look for stop codon
            for j in range(i+3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    orf = sequence[i:j+3]
                    orfs.append(orf)
                    break
    
    return orfs

dna = "ATCATGATCGATCGTAGATCG"
orfs = find_orfs(dna)
print(f"ORFs found: {orfs}")
```

### Example 3: Sequence Window Analysis

```python
def sliding_window(sequence, window_size=10, step=1):
    """Extract overlapping windows from sequence"""
    windows = []
    for i in range(0, len(sequence) - window_size + 1, step):
        window = sequence[i:i+window_size]
        windows.append(window)
    return windows

sequence = "ATCGATCGATCGATCGATCG"
windows = sliding_window(sequence, window_size=6, step=3)

print("Sliding windows:")
for i, window in enumerate(windows):
    gc_count = window.count('G') + window.count('C')
    gc_percent = (gc_count / len(window)) * 100
    print(f"  Window {i+1}: {window} (GC: {gc_percent:.1f}%)")
```

### Example 4: Trim Adapters

```python
def trim_adapters(read, adapter_5="ATCG", adapter_3="CGAT"):
    """Remove adapters from both ends"""
    # Remove 5' adapter
    if read.startswith(adapter_5):
        read = read[len(adapter_5):]
    
    # Remove 3' adapter
    if read.endswith(adapter_3):
        read = read[:-len(adapter_3)]
    
    return read

read = "ATCGATCGATCGATCGATCGCGAT"
trimmed = trim_adapters(read)
print(f"Original: {read}")
print(f"Trimmed:  {trimmed}")
```

---

## 📝 Practice Tasks (Day 6)

### Basic Exercises

1. **String Extraction**: Take the string "ATCGATCGATCG" and print characters at positions 2, 4, 6, and 8.

2. **Reverse Slicing**: Reverse the string "BIOINFORMATICS" using slicing.

3. **List Trimming**: Create a list of 10 numbers, extract the middle 6 elements.

4. **Every Nth Element**: From a list [0,1,2,3,4,5,6,7,8,9], print every 3rd element starting from index 1.

5. **Tuple Splitting**: Given a tuple of 12 elements, split it into 3 equal parts using slicing.

### Intermediate Challenges

6. **Codon Extractor**: Write a function that takes a DNA sequence and returns a list of all codons (triplets).

7. **Quality Trimming**: Given a sequence and quality scores, trim the first and last 5 bases from both.

8. **Reading Frames**: Extract all three reading frames from a DNA sequence using slicing.

9. **Primer Extraction**: Write a function that extracts forward (first 20 bases) and reverse (last 20 bases) primer regions.

10. **Sliding Window GC**: Calculate GC content for overlapping windows of size 10, sliding by 5 bases each time.

### Advanced Challenges

11. **ORF Finder**: Write a function that finds all ORFs (ATG to stop codon) using slicing. Handle all three reading frames.

12. **Adapter Trimmer**: Create a function that removes both 5' and 3' adapters from sequencing reads using slicing.

13. **Reverse Complement**: Implement a function that returns the reverse complement of a DNA sequence using slicing and string manipulation.

14. **Sequence Aligner**: Write a function that extracts matching regions between two sequences of different lengths using sliding windows.

15. **Matrix Transpose**: Given a 2D list representing sequence alignment, use slicing and list comprehension to transpose it (rows become columns).

---

## 💡 Key Takeaways

✓ Slicing syntax: `sequence[start:stop:step]`  
✓ Start is inclusive, stop is exclusive  
✓ Negative indices count from the end  
✓ Omitted start defaults to 0, omitted stop defaults to end  
✓ Negative step reverses the sequence  
✓ Slicing creates a new object (doesn't modify original for immutable types)  
✓ For lists, you can assign to slices to modify them  
✓ Slicing is essential for codon extraction, ORF finding, and sequence analysis  
✓ Use `[:]` to create a copy of a sequence  
✓ `[::-1]` reverses any sequence  
✓ Step parameter enables powerful pattern extraction  

**Next**: Day 7 - Loops (Automating repetitive tasks and iterating through data)
