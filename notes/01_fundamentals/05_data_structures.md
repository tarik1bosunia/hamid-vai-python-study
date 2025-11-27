# Day 5: Data Structures

## 📦 Introduction to Data Structures

**Data structures** are containers that organize and store collections of data efficiently. Python provides four fundamental built-in data structures:

1. **Lists** - Ordered, mutable sequences
2. **Tuples** - Ordered, immutable sequences
3. **Sets** - Unordered collections of unique elements
4. **Dictionaries** - Key-value pairs for fast lookups

Choosing the right data structure is crucial for writing efficient bioinformatics code. Each has specific use cases and performance characteristics.

---

## 📋 Lists

**Lists** are the most versatile data structure in Python. They are ordered, mutable (changeable), and can contain elements of different types.

### Creating Lists

```python
# Empty list
empty_list = []
also_empty = list()

# List with elements
dna_bases = ['A', 'T', 'G', 'C']
numbers = [1, 2, 3, 4, 5]
mixed = [1, "DNA", 3.14, True]

# Nested lists (lists within lists)
sequences = [
    ['ATCG', 100],
    ['GCTA', 150],
    ['TAGC', 120]
]

print(dna_bases)  # ['A', 'T', 'G', 'C']
print(type(dna_bases))  # <class 'list'>
```

### Accessing List Elements

```python
bases = ['A', 'T', 'G', 'C', 'N']

# Indexing (starts at 0)
print(bases[0])    # A (first element)
print(bases[2])    # G (third element)
print(bases[-1])   # N (last element)
print(bases[-2])   # C (second to last)

# Slicing
print(bases[1:3])   # ['T', 'G']
print(bases[:2])    # ['A', 'T']
print(bases[2:])    # ['G', 'C', 'N']
print(bases[::2])   # ['A', 'G', 'N'] (every 2nd element)
print(bases[::-1])  # ['N', 'C', 'G', 'T', 'A'] (reversed)
```

### Modifying Lists

```python
genes = ['BRCA1', 'TP53', 'EGFR']

# Change element
genes[1] = 'KRAS'
print(genes)  # ['BRCA1', 'KRAS', 'EGFR']

# Change multiple elements
genes[0:2] = ['MYC', 'RAS']
print(genes)  # ['MYC', 'RAS', 'EGFR']
```

### List Methods

```python
sequences = ['ATCG', 'GCTA']

# append() - Add element to end
sequences.append('TAGC')
print(sequences)  # ['ATCG', 'GCTA', 'TAGC']

# insert() - Add element at specific position
sequences.insert(1, 'AAAA')
print(sequences)  # ['ATCG', 'AAAA', 'GCTA', 'TAGC']

# extend() - Add multiple elements
sequences.extend(['CCCC', 'GGGG'])
print(sequences)  # ['ATCG', 'AAAA', 'GCTA', 'TAGC', 'CCCC', 'GGGG']

# remove() - Remove first occurrence of value
sequences.remove('AAAA')
print(sequences)  # ['ATCG', 'GCTA', 'TAGC', 'CCCC', 'GGGG']

# pop() - Remove and return element at index (default: last)
last = sequences.pop()
print(last)       # GGGG
print(sequences)  # ['ATCG', 'GCTA', 'TAGC', 'CCCC']

first = sequences.pop(0)
print(first)      # ATCG

# clear() - Remove all elements
# sequences.clear()  # []

# index() - Find position of element
pos = sequences.index('TAGC')
print(pos)  # 1

# count() - Count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))  # 3

# sort() - Sort list in place
bases = ['G', 'A', 'T', 'C']
bases.sort()
print(bases)  # ['A', 'C', 'G', 'T']

# Sort in reverse
bases.sort(reverse=True)
print(bases)  # ['T', 'G', 'C', 'A']

# reverse() - Reverse list in place
bases.reverse()
print(bases)  # ['A', 'C', 'G', 'T']

# copy() - Create a shallow copy
bases_copy = bases.copy()
```

### List Operations

```python
# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# Repetition
motif = ['ATG']
repeated = motif * 3
print(repeated)  # ['ATG', 'ATG', 'ATG']

# Membership
bases = ['A', 'T', 'G', 'C']
print('A' in bases)      # True
print('U' in bases)      # False
print('X' not in bases)  # True

# Length
print(len(bases))  # 4

# Min, Max, Sum (for numeric lists)
scores = [85, 92, 78, 95, 88]
print(min(scores))  # 78
print(max(scores))  # 95
print(sum(scores))  # 438
```

### List Comprehensions

```python
# Create lists efficiently
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)  # [4, 16]

# DNA to RNA conversion
dna_seq = ['A', 'T', 'C', 'G', 'T']
rna_seq = ['U' if base == 'T' else base for base in dna_seq]
print(rna_seq)  # ['A', 'U', 'C', 'G', 'U']
```

### Bioinformatics Applications

```python
# Store sequence data
sequences = [
    "ATCGATCG",
    "GCTAGCTA",
    "TTTTAAAA"
]

# Calculate lengths
lengths = [len(seq) for seq in sequences]
print(f"Lengths: {lengths}")

# Filter by length
long_seqs = [seq for seq in sequences if len(seq) > 8]
print(f"Long sequences: {long_seqs}")

# Store quality scores
quality_scores = [30, 35, 28, 40, 32, 38]
high_quality = [score for score in quality_scores if score >= 30]
print(f"High quality count: {len(high_quality)}")

# Gene expression data
gene_expression = [
    ['Gene1', 5.2],
    ['Gene2', 8.7],
    ['Gene3', 2.1],
    ['Gene4', 10.5]
]

# Extract gene names
gene_names = [item[0] for item in gene_expression]
print(f"Genes: {gene_names}")

# Find highly expressed genes
highly_expressed = [item[0] for item in gene_expression if item[1] > 7.0]
print(f"Highly expressed: {highly_expressed}")
```

---

## 🔒 Tuples

**Tuples** are ordered, immutable sequences. Once created, they cannot be modified. Use tuples for data that shouldn't change.

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()
also_empty = tuple()

# Tuple with elements
dna_bases = ('A', 'T', 'G', 'C')
coordinates = (10, 20, 30)

# Single element tuple (note the comma!)
single = (5,)  # Comma is required
not_tuple = (5)  # This is just an integer

# Without parentheses
simple = 1, 2, 3  # Still a tuple!
print(type(simple))  # <class 'tuple'>

# Mixed types
mixed = (1, "DNA", 3.14, True)

# Nested tuples
gene_data = (
    ('Gene1', 'chr1', 1000, 2000),
    ('Gene2', 'chr2', 5000, 6000)
)
```

### Accessing Tuple Elements

```python
bases = ('A', 'T', 'G', 'C')

# Indexing
print(bases[0])    # A
print(bases[-1])   # C

# Slicing
print(bases[1:3])  # ('T', 'G')
print(bases[:2])   # ('A', 'T')
print(bases[2:])   # ('G', 'C')
```

### Tuple Operations

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)

# Repetition
motif = ('ATG',)
repeated = motif * 3
print(repeated)  # ('ATG', 'ATG', 'ATG')

# Membership
print('A' in bases)  # True

# Length
print(len(bases))  # 4

# count() and index()
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))   # 3
print(numbers.index(3))   # 3
```

### Tuple Unpacking

```python
# Unpack values into variables
gene_info = ('BRCA1', 'chr17', 43044295, 43125483)
name, chromosome, start, end = gene_info

print(f"Gene: {name}")
print(f"Location: {chromosome}:{start}-{end}")

# Swap variables
a, b = 10, 20
a, b = b, a  # Now a=20, b=10

# Multiple return values from functions
def get_stats(sequence):
    return len(sequence), sequence.count('G'), sequence.count('C')

length, g_count, c_count = get_stats("ATCGATCG")
print(f"Length: {length}, G: {g_count}, C: {c_count}")
```

### When to Use Tuples

```python
# Coordinates (shouldn't change)
gene_position = (12345, 67890)

# Return multiple values
def analyze_sequence(seq):
    return (len(seq), seq.count('A'), seq.count('T'), seq.count('G'), seq.count('C'))

# Dictionary keys (tuples are hashable, lists are not)
mutation_data = {
    ('chr1', 12345): 'A>G',
    ('chr2', 67890): 'C>T'
}

# Function arguments
colors = ('red', 'green', 'blue')
# Can't accidentally modify
```

---

## 🎯 Sets

**Sets** are unordered collections of unique elements. Perfect for removing duplicates and performing set operations.

### Creating Sets

```python
# Empty set (use set(), not {})
empty_set = set()

# Set with elements
dna_bases = {'A', 'T', 'G', 'C'}
numbers = {1, 2, 3, 4, 5}

# From a list (duplicates removed automatically)
numbers_with_dups = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_with_dups)
print(unique_numbers)  # {1, 2, 3, 4}

# From a string
unique_chars = set("ATCGATCGATCG")
print(unique_chars)  # {'A', 'T', 'C', 'G'}
```

### Set Methods

```python
bases = {'A', 'T', 'G', 'C'}

# add() - Add single element
bases.add('N')
print(bases)  # {'A', 'T', 'G', 'C', 'N'}

# update() - Add multiple elements
bases.update(['R', 'Y'])
print(bases)  # {'A', 'T', 'G', 'C', 'N', 'R', 'Y'}

# remove() - Remove element (raises error if not found)
bases.remove('R')

# discard() - Remove element (no error if not found)
bases.discard('X')  # No error

# pop() - Remove and return arbitrary element
element = bases.pop()

# clear() - Remove all elements
# bases.clear()
```

### Set Operations

```python
# Union (all elements from both sets)
set1 = {'A', 'T', 'G'}
set2 = {'G', 'C', 'N'}
union = set1 | set2  # or set1.union(set2)
print(union)  # {'A', 'T', 'G', 'C', 'N'}

# Intersection (common elements)
intersection = set1 & set2  # or set1.intersection(set2)
print(intersection)  # {'G'}

# Difference (in set1 but not in set2)
difference = set1 - set2  # or set1.difference(set2)
print(difference)  # {'A', 'T'}

# Symmetric difference (in either but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff)  # {'A', 'T', 'C', 'N'}

# Subset
print({'A', 'T'}.issubset({'A', 'T', 'G', 'C'}))  # True

# Superset
print({'A', 'T', 'G', 'C'}.issuperset({'A', 'T'}))  # True
```

### Bioinformatics Applications

```python
# Find unique bases in a sequence
sequence = "ATCGATCGATCGNNNATCG"
unique_bases = set(sequence)
print(f"Unique bases: {unique_bases}")

# Check if sequence contains only valid DNA bases
valid_dna = {'A', 'T', 'G', 'C'}
sequence_bases = set(sequence.upper())
is_valid = sequence_bases.issubset(valid_dna)
print(f"Valid DNA: {is_valid}")  # False (contains N)

# Find invalid characters
invalid_chars = sequence_bases - valid_dna
print(f"Invalid characters: {invalid_chars}")  # {'N'}

# Compare two sequences
seq1_bases = set("ATCGATCG")
seq2_bases = set("GCTAGCTA")
common_bases = seq1_bases & seq2_bases
print(f"Common bases: {common_bases}")

# Unique to seq1
unique_to_seq1 = seq1_bases - seq2_bases
print(f"Unique to seq1: {unique_to_seq1}")

# All different bases across samples
sample1 = set("ATCG")
sample2 = set("GCTA")
sample3 = set("TAGC")
all_bases = sample1 | sample2 | sample3
print(f"All bases: {all_bases}")
```

---

## 🗂️ Dictionaries

**Dictionaries** store key-value pairs for fast lookups. Perfect for mapping relationships and storing structured data.

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
also_empty = dict()

# Dictionary with elements
nucleotide_names = {
    'A': 'Adenine',
    'T': 'Thymine',
    'G': 'Guanine',
    'C': 'Cytosine'
}

# Various data types
gene_data = {
    'name': 'BRCA1',
    'chromosome': 17,
    'length': 81189,
    'protein_coding': True
}

# Using dict() constructor
codon_table = dict(ATG='Methionine', TAA='Stop', TAG='Stop')

# From list of tuples
pairs = [('A', 'Adenine'), ('T', 'Thymine')]
base_names = dict(pairs)
```

### Accessing Dictionary Elements

```python
gene_info = {
    'name': 'BRCA1',
    'chr': 17,
    'start': 43044295,
    'end': 43125483
}

# Using key
print(gene_info['name'])  # BRCA1
print(gene_info['chr'])   # 17

# Using get() - safer, returns None if key doesn't exist
print(gene_info.get('name'))        # BRCA1
print(gene_info.get('organism'))    # None
print(gene_info.get('organism', 'Unknown'))  # Unknown (default value)
```

### Modifying Dictionaries

```python
gene = {'name': 'TP53', 'chr': 17}

# Add new key-value pair
gene['length'] = 20000
print(gene)  # {'name': 'TP53', 'chr': 17, 'length': 20000}

# Modify existing value
gene['length'] = 25000

# Remove key-value pair
del gene['length']

# pop() - Remove and return value
chr_num = gene.pop('chr')
print(chr_num)  # 17

# popitem() - Remove and return last item
# item = gene.popitem()

# clear() - Remove all items
# gene.clear()
```

### Dictionary Methods

```python
gene_data = {
    'BRCA1': {'chr': 17, 'length': 81189},
    'TP53': {'chr': 17, 'length': 20000},
    'EGFR': {'chr': 7, 'length': 188307}
}

# keys() - Get all keys
print(gene_data.keys())
# dict_keys(['BRCA1', 'TP53', 'EGFR'])

# values() - Get all values
print(gene_data.values())

# items() - Get key-value pairs
print(gene_data.items())

# update() - Add/update multiple items
gene_data.update({'KRAS': {'chr': 12, 'length': 35000}})

# setdefault() - Get value or set default if key doesn't exist
value = gene_data.setdefault('MYC', {'chr': 8, 'length': 5000})
```

### Iterating Through Dictionaries

```python
codon_table = {
    'ATG': 'Methionine',
    'TAA': 'Stop',
    'TAG': 'Stop',
    'TGA': 'Stop'
}

# Iterate over keys
for codon in codon_table:
    print(codon)

# Iterate over keys explicitly
for codon in codon_table.keys():
    print(codon)

# Iterate over values
for amino_acid in codon_table.values():
    print(amino_acid)

# Iterate over key-value pairs
for codon, amino_acid in codon_table.items():
    print(f"{codon} codes for {amino_acid}")
```

### Nested Dictionaries

```python
# Store complex data
sequences = {
    'seq001': {
        'sequence': 'ATCGATCG',
        'length': 8,
        'gc_content': 50.0,
        'organism': 'E. coli'
    },
    'seq002': {
        'sequence': 'GCTAGCTA',
        'length': 8,
        'gc_content': 50.0,
        'organism': 'H. sapiens'
    }
}

# Access nested data
print(sequences['seq001']['organism'])  # E. coli
print(sequences['seq002']['gc_content'])  # 50.0
```

### Bioinformatics Applications

```python
# Genetic code (simplified)
genetic_code = {
    'ATG': 'Met',
    'TGG': 'Trp',
    'TAA': 'Stop',
    'TAG': 'Stop',
    'TGA': 'Stop'
}

# Translate codon
codon = 'ATG'
amino_acid = genetic_code.get(codon, 'Unknown')
print(f"{codon} -> {amino_acid}")

# Count nucleotides
def count_nucleotides(sequence):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in sequence.upper():
        if base in counts:
            counts[base] += 1
    return counts

dna = "ATCGATCGATCG"
result = count_nucleotides(dna)
print(result)  # {'A': 3, 'T': 3, 'G': 3, 'C': 3}

# Gene annotation
genes = {
    'BRCA1': {
        'full_name': 'Breast cancer type 1',
        'function': 'DNA repair',
        'chromosome': 17,
        'diseases': ['Breast cancer', 'Ovarian cancer']
    },
    'TP53': {
        'full_name': 'Tumor protein p53',
        'function': 'Cell cycle regulation',
        'chromosome': 17,
        'diseases': ['Li-Fraumeni syndrome']
    }
}

# Query gene information
gene = 'BRCA1'
if gene in genes:
    info = genes[gene]
    print(f"Gene: {gene}")
    print(f"Full name: {info['full_name']}")
    print(f"Function: {info['function']}")
    print(f"Diseases: {', '.join(info['diseases'])}")
```

---

## 🔄 Choosing the Right Data Structure

| Use Case | Best Structure | Reason |
|----------|----------------|---------|
| Ordered collection that changes | List | Mutable, indexed |
| Ordered collection that doesn't change | Tuple | Immutable, hashable |
| Unique elements only | Set | Automatic deduplication |
| Remove duplicates | Set | Built-in uniqueness |
| Fast lookups by key | Dictionary | O(1) average lookup |
| Store paired data | Dictionary | Key-value mapping |
| Mathematical set operations | Set | Union, intersection, etc. |
| Sequence analysis | List or String | Ordered access |
| Configuration data | Dictionary | Named fields |
| Coordinates | Tuple | Immutable position |

---

## 📝 Practice Tasks (Day 5)

### Basic Exercises

1. **List Creation**: Create a list of 5 gene names and print the first and last elements.

2. **List Manipulation**: Create a list of numbers 1-10, add 11 to the end, remove 5, and print the result.

3. **Tuple Practice**: Create a tuple with your name, age, and city. Unpack it into three variables.

4. **Set Operations**: Create two sets of nucleotides and find their union and intersection.

5. **Dictionary Basics**: Create a dictionary mapping three codons to their amino acids. Print each mapping.

### Intermediate Challenges

6. **Nucleotide Counter**: Write a program using a dictionary to count each nucleotide in "ATCGATCGATCGNNNATCG".

7. **Unique Bases**: Given a list of sequences, use a set to find all unique bases across all sequences.

8. **Gene Database**: Create a dictionary storing information about 3 genes (name, chromosome, length). Print all gene names.

9. **List Comprehension**: Create a list of GC contents for these sequences: ["ATCG", "GGCC", "AATT", "GCGC"].

10. **Sequence Filter**: Given a list of sequences, create a new list containing only sequences longer than 5 bases.

### Advanced Challenges

11. **Codon Table**: Build a dictionary representing the genetic code (at least 10 codons). Write a function to translate a DNA sequence.

12. **Sequence Analyzer**: Create a function that takes a sequence and returns a dictionary with:
    - Length
    - Nucleotide counts
    - GC percentage
    - Unique bases

13. **Data Structure Comparison**: Store the same sequence data in a list, tuple, set, and dictionary. Compare access methods and use cases.

14. **Gene Expression Data**: Create a nested dictionary storing gene expression data for multiple genes across multiple samples. Calculate average expression per gene.

15. **Mutation Tracker**: Build a dictionary that tracks mutations at specific positions: `{position: {'ref': 'A', 'alt': 'G', 'count': 10}}`. Add, update, and query mutation data.

---

## 💡 Key Takeaways

✓ **Lists**: Ordered, mutable, indexed - use for sequences that change  
✓ **Tuples**: Ordered, immutable, indexed - use for fixed data  
✓ **Sets**: Unordered, unique elements - use for deduplication and set operations  
✓ **Dictionaries**: Key-value pairs - use for fast lookups and structured data  
✓ Lists and tuples allow duplicates; sets don't  
✓ Lists are mutable; tuples are immutable  
✓ Dictionary keys must be immutable (strings, numbers, tuples)  
✓ Choose data structures based on your specific needs  
✓ List comprehensions provide efficient list creation  
✓ Use `get()` for safe dictionary access  

**Next**: Day 6 - Slicing in Python (Advanced slicing techniques for all sequence types)
