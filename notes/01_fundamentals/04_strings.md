# Day 4: Strings

## 🧵 Understanding Strings

**Strings** are one of the most important data types in Python, especially for bioinformatics where DNA, RNA, and protein sequences are represented as strings. A string is a sequence of characters enclosed in quotes.

### String Fundamentals

```python
# Different ways to create strings
text = "Python Programming"
dna = 'ATCGATCG'
protein = """MKTAYIAKQRQISFVKSHFSRQLE
ERLIHGKQVDVQDSLHKVLNKPFNF"""  # Multi-line string

print(text)
print(type(text))  # <class 'str'>
```

### Key Properties

1. **Immutable**: Once created, strings cannot be modified (but you can create new ones)
2. **Ordered**: Characters have a specific position (index)
3. **Iterable**: You can loop through each character
4. **Sequence**: Supports indexing, slicing, and sequence operations

```python
# Strings are immutable
sequence = "ATCG"
# sequence[0] = "G"  # This would cause an error!

# But you can create a new string
new_sequence = "G" + sequence[1:]  # "GTCG"
print(new_sequence)
```

### Quote Styles

```python
# Single quotes
gene = 'BRCA1'

# Double quotes
description = "Breast cancer gene"

# Triple quotes (preserve formatting, good for multi-line)
fasta = """
>seq001
ATCGATCGATCG
GCTAGCTAGCTA
"""

# Escape quotes inside strings
message = "She said, \"DNA is amazing!\""
alternate = 'He replied, "I agree!"'
```

---

## 🔢 Indexing and Slicing

Strings are indexed sequences. Each character has a position, starting from 0. This is crucial for extracting parts of biological sequences!

### Indexing Basics

```python
sequence = "ATCGATCG"
#          01234567  (positive indices)
#          -8-7-6-5-4-3-2-1  (negative indices)

# Positive indexing (from left)
print(sequence[0])   # A (first character)
print(sequence[1])   # T (second character)
print(sequence[7])   # G (last character)

# Negative indexing (from right)
print(sequence[-1])  # G (last character)
print(sequence[-2])  # C (second to last)
print(sequence[-8])  # A (first character)
```

### Slicing Syntax

**Format**: `string[start:stop:step]`

- **start**: Beginning index (inclusive)
- **stop**: Ending index (exclusive)
- **step**: Skip pattern (default is 1)

```python
dna = "ATCGATCGATCG"

# Basic slicing
print(dna[0:4])    # ATCG (indices 0,1,2,3)
print(dna[4:8])    # ATCG (indices 4,5,6,7)

# Omitting indices
print(dna[:4])     # ATCG (from start to index 4)
print(dna[4:])     # ATCGATCG (from index 4 to end)
print(dna[:])      # ATCGATCGATCG (entire string - copy)

# Negative indices in slicing
print(dna[-4:])    # ATCG (last 4 characters)
print(dna[:-4])    # ATCGATCG (all except last 4)

# Using step
print(dna[::2])    # ACATG (every 2nd character)
print(dna[::3])    # AGTG (every 3rd character - codons!)
print(dna[::-1])   # GCTAGCTAGCTA (reverse - complement direction)
```

### Bioinformatics Applications

```python
# Extract codons (triplets)
mrna = "AUGUCGGCUAAACCC"

codon1 = mrna[0:3]    # AUG (start codon)
codon2 = mrna[3:6]    # UCG
codon3 = mrna[6:9]    # GCU
codon4 = mrna[9:12]   # AAA
codon5 = mrna[12:15]  # CCC

print(f"Start codon: {codon1}")

# Extract every 3rd position (codon analysis)
first_positions = mrna[0::3]   # AUGAA
second_positions = mrna[1::3]  # UCGAC
third_positions = mrna[2::3]   # GGTNC

# Reverse complement (simplified - just reversal)
reverse = mrna[::-1]
print(f"Reverse: {reverse}")

# Get primer regions
forward_primer = mrna[:20]   # First 20 bases
reverse_primer = mrna[-20:]  # Last 20 bases
```

---

## 🔧 Essential String Methods

Python provides powerful built-in methods for string manipulation. These are invaluable for sequence analysis!

### Case Conversion

```python
sequence = "atcGATcg"

print(sequence.upper())       # ATCGATCG (all uppercase)
print(sequence.lower())       # atcgatcg (all lowercase)
print(sequence.capitalize())  # Atcgatcg (first letter capitalized)
print(sequence.title())       # Atcgatcg (each word capitalized)
print(sequence.swapcase())    # ATCgatCG (swap cases)
```

### Whitespace Handling

```python
messy_sequence = "  ATCGATCG  \n"

print(messy_sequence.strip())   # "ATCGATCG" (remove both ends)
print(messy_sequence.lstrip())  # "ATCGATCG  \n" (remove left)
print(messy_sequence.rstrip())  # "  ATCGATCG" (remove right)

# Remove specific characters
data = ">>ATCGATCG<<"
print(data.strip("><"))  # "ATCGATCG"
```

### Search and Replace

```python
dna = "ATCGATCGATCG"

# Find substring position
print(dna.find("GAT"))      # 3 (first occurrence)
print(dna.find("XYZ"))      # -1 (not found)
print(dna.rfind("GAT"))     # 7 (last occurrence)
print(dna.index("GAT"))     # 3 (like find, but raises error if not found)

# Count occurrences
print(dna.count("AT"))      # 3
print(dna.count("G"))       # 4

# Replace substrings
rna = dna.replace("T", "U")  # AUCGAUCGAUCG (DNA to RNA)
print(rna)

# Remove all spaces
formatted = "AT CG AT CG".replace(" ", "")  # ATCGATCG
print(formatted)
```

### Split and Join

```python
# Split string into list
sequence_data = "seq001,ATCGATCG,100,45.5"
fields = sequence_data.split(",")
print(fields)  # ['seq001', 'ATCGATCG', '100', '45.5']

seq_id, seq, length, gc = sequence_data.split(",")
print(f"ID: {seq_id}, Sequence: {seq}")

# Split by whitespace (default)
text = "DNA RNA Protein"
words = text.split()  # ['DNA', 'RNA', 'Protein']

# Split by newlines
fasta = """ATCG
GCTA
TAGC"""
lines = fasta.split("\n")  # ['ATCG', 'GCTA', 'TAGC']

# Join list into string
bases = ['A', 'T', 'C', 'G']
sequence = "".join(bases)  # "ATCG"
print(sequence)

# Join with separator
codons = ['ATG', 'GCT', 'TAA']
spaced = "-".join(codons)  # "ATG-GCT-TAA"
print(spaced)
```

### String Validation

```python
# Check string properties
print("ATCG".isalpha())       # True (only letters)
print("123".isdigit())         # True (only digits)
print("ATCGatcg".islower())    # False
print("ATCG".isupper())        # True
print("seq123".isalnum())      # True (letters and numbers)
print("  ".isspace())          # True (only whitespace)

# Check prefixes and suffixes
gene_id = "NM_001234"
print(gene_id.startswith("NM"))      # True
print(gene_id.endswith("234"))       # True
print(gene_id.startswith("XM"))      # False

# Useful for file extensions
filename = "sequence.fasta"
print(filename.endswith(".fasta"))   # True
print(filename.endswith((".fasta", ".fa")))  # True (multiple options)
```

---

## 🔤 String Concatenation and Repetition

### Concatenation

```python
# Using + operator
first = "ATCG"
second = "GCTA"
combined = first + second  # "ATCGGCTA"

# Building sequences
forward = "ATCG"
reverse = "CGAT"
palindrome = forward + reverse  # "ATCGCGAT"

# Multiple concatenations
prefix = ">"
seq_id = "seq001"
separator = " "
description = "E. coli gene"
header = prefix + seq_id + separator + description
print(header)  # ">seq001 E. coli gene"

# Note: For many concatenations, use join() instead
parts = [">", "seq001", " ", "E. coli gene"]
header = "".join(parts)  # More efficient
```

### Repetition

```python
# Using * operator
motif = "ATG"
repeated = motif * 3  # "ATGATGATG"
print(repeated)

# Create separator lines
line = "=" * 50
print(line)  # ==================================================

# Create spacers
spacer = " " * 10  # 10 spaces

# Tandem repeats
repeat_unit = "CAG"
tandem_repeat = repeat_unit * 10  # Huntington's disease-related
print(f"Tandem repeat: {tandem_repeat}")
```

---

## 📝 String Formatting

Python offers multiple ways to format strings. Modern f-strings are the most readable and efficient.

### F-Strings (Formatted String Literals)

```python
# Basic f-strings
gene = "BRCA1"
length = 1863
gc_content = 58.2

report = f"Gene {gene} has {length} bases with {gc_content}% GC content"
print(report)

# Expressions inside f-strings
a_count = 450
t_count = 412
total = a_count + t_count
print(f"AT count: {a_count + t_count}")  # AT count: 862

# Formatting numbers
pi = 3.14159265359
print(f"Pi: {pi:.2f}")        # Pi: 3.14 (2 decimal places)
print(f"Pi: {pi:.4f}")        # Pi: 3.1416 (4 decimal places)

coverage = 15.7
print(f"Coverage: {coverage:>10.1f}x")  # Right-aligned, 1 decimal

# Formatting percentages
gc = 0.523
print(f"GC: {gc:.1%}")        # GC: 52.3%

# Scientific notation
e_value = 0.000000015
print(f"E-value: {e_value:.2e}")  # E-value: 1.50e-08
```

### Format Method

```python
# Basic format
template = "Gene: {}, Length: {}"
result = template.format("BRCA1", 1863)
print(result)

# Named placeholders
template = "Gene: {gene}, Length: {length}, GC: {gc}%"
result = template.format(gene="BRCA1", length=1863, gc=58.2)
print(result)

# Positional arguments
print("{0} to {1}".format("DNA", "RNA"))  # DNA to RNA
print("{1} to {0}".format("DNA", "RNA"))  # RNA to DNA
```

### Old-Style Formatting (% operator)

```python
# Still seen in older code
name = "BRCA1"
length = 1863
print("Gene %s has %d bases" % (name, length))
print("GC content: %.2f%%" % 58.234)  # GC content: 58.23%
```

---

## 🔍 Advanced String Operations

### Length and Membership

```python
sequence = "ATCGATCG"

# Get length
print(len(sequence))  # 8

# Check membership
print("ATG" in sequence)      # False
print("GAT" in sequence)      # True
print("XYZ" not in sequence)  # True

# Iterate through characters
for base in "ATCG":
    print(base, end=" ")  # A T C G
```

### String Comparison

```python
# Lexicographic comparison
print("ATCG" == "ATCG")  # True
print("ATCG" < "ATGC")   # True (C comes before G)
print("DNA" > "RNA")     # False (D comes before R)

# Case-insensitive comparison
seq1 = "ATCG"
seq2 = "atcg"
print(seq1.lower() == seq2.lower())  # True
```

### Multi-line Strings

```python
# Using triple quotes
fasta_entry = """
>seq001 | Homo sapiens | chromosome 17
ATCGATCGATCGATCGATCGATCGATCG
GCTAGCTAGCTAGCTAGCTAGCTAGCTA
TTTTAAAACCCCGGGG
"""

print(fasta_entry)

# Building multi-line strings
lines = [
    ">seq001",
    "ATCGATCG",
    "GCTAGCTA"
]
fasta = "\n".join(lines)
print(fasta)
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: DNA to RNA Transcription

```python
dna_sequence = "ATCGATCGATCG"
rna_sequence = dna_sequence.replace("T", "U")
print(f"DNA: {dna_sequence}")
print(f"RNA: {rna_sequence}")
```

### Example 2: Reverse Complement

```python
def reverse_complement(dna):
    # Create complement
    complement = dna.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
    complement = complement.upper()
    # Reverse it
    return complement[::-1]

sequence = "ATCGATCG"
rev_comp = reverse_complement(sequence)
print(f"Original:    {sequence}")
print(f"Rev. Comp.:  {rev_comp}")
```

### Example 3: GC Content Calculator

```python
def calculate_gc_content(sequence):
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    
    if total == 0:
        return 0.0
    
    gc_percentage = ((g_count + c_count) / total) * 100
    return gc_percentage

dna = "ATCGATCGGGCCAATT"
gc = calculate_gc_content(dna)
print(f"Sequence: {dna}")
print(f"GC Content: {gc:.2f}%")
```

### Example 4: FASTA Parser (Simple)

```python
fasta_data = """>seq001
ATCGATCGATCG
GCTAGCTAGCTA
>seq002
TTTTAAAACCCC"""

lines = fasta_data.split("\n")
current_seq = ""

for line in lines:
    if line.startswith(">"):
        if current_seq:
            print(f"Length: {len(current_seq)}")
        print(f"Header: {line}")
        current_seq = ""
    else:
        current_seq += line

if current_seq:
    print(f"Length: {len(current_seq)}")
```

---

## 📝 Practice Tasks (Day 4)

### Basic Exercises

1. **Character Extraction**: Take a string input and print the first, middle, and last characters.

2. **String Reversal**: Write a program to reverse a string using slicing (`[::-1]`).

3. **Count Letters**: Count how many times the letter 'a' (case-insensitive) appears in a user-provided string.

4. **Case Converter**: Ask for a name and print it in uppercase, lowercase, and title case.

5. **String Formatting**: Use f-strings to create a formatted output: "My favorite gene is [gene] and it has [number] exons."

### Intermediate Challenges

6. **DNA Validator**: Write a program that checks if a sequence contains only valid DNA bases (A, T, G, C). Make it case-insensitive.

7. **Codon Extractor**: Given a DNA sequence, extract and print all codons (triplets). Handle sequences not divisible by 3.

8. **Find Motif**: Ask for a DNA sequence and a motif. Find and print all positions where the motif occurs.

9. **Sequence Statistics**: Write a program that takes a DNA sequence and reports:
   - Length
   - Count of each base (A, T, G, C)
   - GC percentage
   - AT percentage

10. **FASTA Header Parser**: Given a FASTA header like `>seq001|gene=BRCA1|organism=human`, extract and print each field separately.

### Advanced Challenges

11. **DNA to RNA Transcription**: Create a function that converts DNA to RNA, validates input, and handles both uppercase and lowercase.

12. **Reverse Complement**: Implement a function that returns the reverse complement of a DNA sequence.

13. **ORF Finder**: Find all occurrences of the start codon "ATG" in a sequence and print their positions.

14. **Sequence Cleaner**: Write a program that:
    - Removes whitespace and numbers from a sequence
    - Converts to uppercase
    - Removes invalid characters (keeps only ATGCN)
    - Reports what was removed

15. **Mini FASTA Formatter**: Take a long sequence and format it as a FASTA entry with:
    - A header line starting with ">"
    - Sequence split into lines of 60 characters each

---

## 💡 Key Takeaways

✓ Strings are immutable sequences of characters  
✓ Indexing starts at 0; negative indices count from the end  
✓ Slicing format: `string[start:stop:step]`  
✓ Essential methods: `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`, `find()`, `count()`  
✓ F-strings are the modern, preferred way to format strings  
✓ Use `in` and `not in` for membership testing  
✓ String concatenation: `+` operator or `join()` for multiple strings  
✓ String repetition: `*` operator  
✓ Always validate and clean biological sequence data  
✓ Case matters: "DNA" ≠ "dna" (use `.upper()` or `.lower()` for consistency)

**Next**: Day 5 - Data Structures (Lists, tuples, dictionaries, and sets for organizing data)
