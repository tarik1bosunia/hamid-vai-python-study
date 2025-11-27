# Day 8: Loops

## 🔄 Understanding Loops

**Loops** are programming constructs that allow you to repeat a block of code multiple times without writing it repeatedly. They're essential for processing sequences, analyzing data, and automating repetitive tasks—particularly valuable when working with biological sequences and large datasets.

### Why Loops Matter in Bioinformatics

- Iterate through DNA/RNA sequences character by character
- Process multiple sequences from files
- Analyze each codon in a gene
- Calculate statistics across datasets
- Scan for motifs or patterns
- Process quality scores for reads
- Automate batch analysis of samples

---

## 🔹 Types of Loops in Python

| Loop Type | Use Case | When to Use |
|-----------|----------|-------------|
| `for` loop | Iterate over sequences (strings, lists, ranges) | When you know how many iterations or have a collection to process |
| `while` loop | Repeat while condition is True | When iterations depend on a condition, not a fixed count |
| Nested loops | Loop within a loop | For multi-dimensional data, pairwise comparisons, matrix operations |

---

## ✅ The for Loop

The `for` loop iterates over items in a sequence (string, list, tuple, range, etc.) **in order**.

### Syntax

```python
for variable in sequence:
    # code to execute for each item
    statement1
    statement2
```

### Basic Examples

```python
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate over a string
dna = "ATCG"
for base in dna:
    print(base)

# Using range()
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Range with start and stop
for i in range(2, 8):
    print(i)  # Prints 2, 3, 4, 5, 6, 7

# Range with step
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

# Iterate with index using enumerate()
sequences = ["ATCG", "GCTA", "TAGC"]
for index, seq in enumerate(sequences):
    print(f"Sequence {index}: {seq}")
```

### Bioinformatics Examples

```python
# Count nucleotides
dna_sequence = "ATCGATCGATCG"
a_count = 0
t_count = 0
c_count = 0
g_count = 0

for base in dna_sequence:
    if base == 'A':
        a_count += 1
    elif base == 'T':
        t_count += 1
    elif base == 'C':
        c_count += 1
    elif base == 'G':
        g_count += 1

print(f"A: {a_count}, T: {t_count}, C: {c_count}, G: {g_count}")

# Calculate GC content
sequence = "ATCGATCGATCG"
gc_count = 0
for base in sequence:
    if base in ['G', 'C']:
        gc_count += 1
gc_percent = (gc_count / len(sequence)) * 100
print(f"GC content: {gc_percent:.2f}%")

# Process codons
mrna = "AUGUCGGCUAAACCCGGGAAA"
print("Codons:")
for i in range(0, len(mrna), 3):
    codon = mrna[i:i+3]
    if len(codon) == 3:
        print(codon)

# Analyze multiple sequences
sequences = ["ATCG", "GCTA", "TAGC", "CGAT"]
for i, seq in enumerate(sequences, start=1):
    length = len(seq)
    gc = (seq.count('G') + seq.count('C')) / length * 100
    print(f"Seq {i}: {seq} | Length: {length} | GC: {gc:.1f}%")

# Quality score filtering
quality_scores = [35, 28, 40, 22, 38, 30, 25, 42]
passed = 0
failed = 0
for score in quality_scores:
    if score >= 30:
        passed += 1
    else:
        failed += 1
print(f"Passed: {passed}, Failed: {failed}")
```

---

## ✅ The while Loop

The `while` loop repeats as long as a condition is `True`. Be careful to ensure the condition eventually becomes `False` to avoid infinite loops!

### Syntax

```python
while condition:
    # code to execute while condition is True
    statement1
    statement2
```

### Basic Examples

```python
# Simple counting
count = 1
while count <= 5:
    print(f"Count = {count}")
    count += 1

# Countdown
number = 10
while number > 0:
    print(number)
    number -= 1
print("Blast off!")

# Sum until threshold
total = 0
num = 1
while total < 50:
    total += num
    num += 1
print(f"Total: {total}")

# User input validation (conceptual)
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")
```

### Bioinformatics Examples

```python
# Read sequences until stop signal
sequences = ["ATCG", "GCTA", "STOP", "TAGC"]
index = 0
while index < len(sequences) and sequences[index] != "STOP":
    print(f"Processing: {sequences[index]}")
    index += 1
print("Stop signal reached")

# Process until quality threshold
quality_scores = [35, 32, 30, 28, 25, 22, 20]
index = 0
min_quality = 25
while index < len(quality_scores) and quality_scores[index] >= min_quality:
    print(f"Read {index+1}: Quality {quality_scores[index]} - PASS")
    index += 1
if index < len(quality_scores):
    print(f"Read {index+1}: Quality {quality_scores[index]} - FAIL (stopped)")

# Find ORF
sequence = "ATCATGATCGATCGTAG"
position = 0
orf_found = False
while position < len(sequence) - 2 and not orf_found:
    codon = sequence[position:position+3]
    if codon == "ATG":
        print(f"Start codon found at position {position}")
        orf_found = True
    position += 1

# Accumulate sequence until length threshold
total_length = 0
seq_count = 0
sequences = ["ATCG", "GCTAGCTA", "AT", "CGTAGC"]
while seq_count < len(sequences) and total_length < 20:
    current_seq = sequences[seq_count]
    total_length += len(current_seq)
    seq_count += 1
    print(f"Added sequence {seq_count}: {current_seq} (Total: {total_length} bp)")
```

---

## ✅ Loop Control: break Statement

The `break` statement **immediately exits** the loop, regardless of the loop condition.

### Basic Examples

```python
# Stop at specific value
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# Search for item
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "cherry":
        print("Found cherry!")
        break
    print(f"Checking {fruit}")

# Stop when condition met
numbers = [2, 4, 6, 7, 8, 10]
for num in numbers:
    if num % 2 != 0:  # Found odd number
        print(f"First odd number: {num}")
        break
```

### Bioinformatics Examples

```python
# Find first stop codon
sequence = "ATGATCGTAGCGATAA"
print("Searching for stop codon...")
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    print(f"Position {i}: {codon}")
    if codon in ["TAA", "TAG", "TGA"]:
        print(f"Stop codon found: {codon} at position {i}")
        break

# Find sequence above quality threshold
reads = ["ATCG", "GCTA", "TAGC", "CGAT"]
qualities = [25, 28, 35, 30]
for i, (read, qual) in enumerate(zip(reads, qualities)):
    if qual >= 30:
        print(f"First high-quality read: {read} (Q={qual})")
        break

# Search for motif
sequence = "ATCGATCGGAATTCGCTAGC"
motif = "GAATTC"  # EcoRI restriction site
for i in range(len(sequence) - len(motif) + 1):
    window = sequence[i:i+len(motif)]
    if window == motif:
        print(f"Motif {motif} found at position {i}")
        break
else:
    print(f"Motif {motif} not found")

# Validate sequences
sequences = ["ATCG", "GCTA", "XYZW", "TAGC"]
for seq in sequences:
    if not set(seq).issubset(set("ATCG")):
        print(f"Invalid sequence found: {seq}")
        break
    print(f"Valid: {seq}")
```

---

## ✅ Loop Control: continue Statement

The `continue` statement **skips the current iteration** and moves to the next one.

### Basic Examples

```python
# Skip specific value
for i in range(6):
    if i == 3:
        continue
    print(i)  # Prints 0, 1, 2, 4, 5 (skips 3)

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints 1, 3, 5, 7, 9

# Skip specific items
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)  # Prints all except banana
```

### Bioinformatics Examples

```python
# Skip invalid nucleotides
sequence = "ATCGXNATCG"
clean_sequence = ""
for base in sequence:
    if base not in "ATCG":
        continue
    clean_sequence += base
print(f"Cleaned: {clean_sequence}")  # ATCGATCG

# Process only high-quality reads
reads = ["ATCG", "GCTA", "TAGC", "CGAT", "ATGC"]
qualities = [35, 22, 38, 25, 40]
for read, qual in zip(reads, qualities):
    if qual < 30:
        continue
    print(f"Processing: {read} (Q={qual})")

# Skip incomplete codons
sequence = "ATGATCGTAGCGATAA"
print("Complete codons:")
for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    if len(codon) < 3:
        continue
    print(codon)

# Filter sequences by length
sequences = ["AT", "ATCGATCG", "GC", "TAGCTAGC", "A"]
min_length = 5
print("Sequences passing length filter:")
for seq in sequences:
    if len(seq) < min_length:
        continue
    print(f"  {seq} ({len(seq)} bp)")

# Skip stop codons in analysis
codons = ["ATG", "TCC", "TAA", "GCA", "TAG", "AAA"]
print("Non-stop codons:")
for codon in codons:
    if codon in ["TAA", "TAG", "TGA"]:
        continue
    print(codon)
```

---

## ✅ else Clause with Loops

Python allows an `else` block with loops. It executes **only if the loop completes normally** (not interrupted by `break`).

### Syntax

```python
for item in sequence:
    # loop body
    if condition:
        break
else:
    # executed if loop finished without break
    statement
```

### Examples

```python
# Search with else
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num % 2 != 0:
        print(f"Found odd number: {num}")
        break
else:
    print("No odd numbers found")

# While loop with else
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Count reached 5")

# Validation with else
items = ["apple", "banana", "cherry"]
for item in items:
    if item == "grape":
        print("Found grape!")
        break
else:
    print("Grape not found in list")
```

### Bioinformatics Examples

```python
# Check if all sequences are valid
sequences = ["ATCG", "GCTA", "TAGC"]
for seq in sequences:
    if not set(seq).issubset(set("ATCG")):
        print(f"Invalid sequence: {seq}")
        break
else:
    print("All sequences are valid!")

# Find stop codon
sequence = "ATGATCGCAGCAATG"
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    if codon in ["TAA", "TAG", "TGA"]:
        print(f"Stop codon found: {codon}")
        break
else:
    print("No stop codon found - possible incomplete ORF")

# Quality check all reads
reads = ["ATCG", "GCTA", "TAGC"]
qualities = [35, 38, 40]
min_quality = 30
for read, qual in zip(reads, qualities):
    if qual < min_quality:
        print(f"Quality check failed for {read}")
        break
else:
    print("All reads passed quality check!")
```

---

## ✅ Nested Loops

A **nested loop** is a loop inside another loop. The inner loop completes all its iterations for each iteration of the outer loop.

### Syntax

```python
for outer_variable in outer_sequence:
    for inner_variable in inner_sequence:
        # code executes for each combination
        statement
```

### Basic Examples

```python
# Simple nested loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")

# Pattern printing
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()  # New line

# 2D list traversal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

### Bioinformatics Examples

```python
# Pairwise sequence comparison
sequences = ["ATCG", "ATCG", "GCTA"]
print("Pairwise sequence comparison:")
for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        seq1, seq2 = sequences[i], sequences[j]
        matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
        similarity = matches / len(seq1) * 100
        print(f"  Seq{i} vs Seq{j}: {similarity:.1f}% similar")

# Codon frequency table
sequence = "ATGATCGCAGCATAG"
codon_counts = {}
for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i+3]
    if len(codon) == 3:
        if codon not in codon_counts:
            codon_counts[codon] = 0
        codon_counts[codon] += 1

print("Codon frequencies:")
for codon, count in codon_counts.items():
    print(f"  {codon}: {count}")

# Motif scanning in multiple sequences
sequences = ["ATCGATCG", "GCTAGCTA", "ATCGTACG"]
motif = "ATCG"
print(f"Scanning for motif '{motif}':")
for seq_num, sequence in enumerate(sequences, start=1):
    print(f"Sequence {seq_num}:")
    for i in range(len(sequence) - len(motif) + 1):
        window = sequence[i:i+len(motif)]
        if window == motif:
            print(f"  Found at position {i}")

# Generate all possible kmers (k=2)
sequence = "ATCG"
k = 2
kmers = []
for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    kmers.append(kmer)
print(f"All {k}-mers: {kmers}")

# Matrix dot product pattern
seq1 = "ATCG"
seq2 = "GCTA"
print("Base pair comparison matrix:")
print("    ", end="")
for base2 in seq2:
    print(base2, end=" ")
print()
for base1 in seq1:
    print(base1, "  ", end="")
    for base2 in seq2:
        if base1 == base2:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: Comprehensive Nucleotide Counter

```python
def count_nucleotides(sequence):
    """Count all nucleotides in a sequence"""
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    total = 0
    
    for base in sequence.upper():
        if base in counts:
            counts[base] += 1
            total += 1
    
    print(f"Sequence: {sequence}")
    print(f"Total valid bases: {total}")
    print("\nNucleotide counts:")
    for nucleotide, count in counts.items():
        percent = (count / total * 100) if total > 0 else 0
        print(f"  {nucleotide}: {count} ({percent:.2f}%)")
    
    # GC content
    gc_content = ((counts['G'] + counts['C']) / total * 100) if total > 0 else 0
    print(f"\nGC content: {gc_content:.2f}%")
    
    return counts

# Test
count_nucleotides("ATCGATCGATCGATCG")
```

### Example 2: ORF Finder

```python
def find_orfs(sequence):
    """Find all Open Reading Frames"""
    sequence = sequence.upper()
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    orfs = []
    
    print(f"Scanning sequence ({len(sequence)} bp) for ORFs...")
    
    # Check all three reading frames
    for frame in range(3):
        print(f"\nReading frame {frame + 1}:")
        i = frame
        
        while i < len(sequence) - 2:
            codon = sequence[i:i+3]
            
            if codon == start_codon:
                # Found start, look for stop
                orf_start = i
                j = i + 3
                
                while j < len(sequence) - 2:
                    stop_candidate = sequence[j:j+3]
                    if stop_candidate in stop_codons:
                        orf = sequence[orf_start:j+3]
                        orf_length = len(orf)
                        print(f"  ORF found: {orf_start}-{j+3} ({orf_length} bp)")
                        orfs.append({
                            'sequence': orf,
                            'start': orf_start,
                            'end': j+3,
                            'length': orf_length,
                            'frame': frame + 1
                        })
                        i = j + 3
                        break
                    j += 3
                else:
                    # No stop codon found
                    i += 3
            else:
                i += 3
    
    print(f"\nTotal ORFs found: {len(orfs)}")
    return orfs

# Test
dna = "ATGATCGTAGCGATGAAATCGTAG"
orfs = find_orfs(dna)
```

### Example 3: Sliding Window Analysis

```python
def sliding_window_gc(sequence, window_size=10, step=5):
    """Calculate GC content using sliding windows"""
    sequence = sequence.upper()
    
    print(f"Sequence length: {len(sequence)} bp")
    print(f"Window size: {window_size} bp")
    print(f"Step size: {step} bp\n")
    
    windows = []
    for i in range(0, len(sequence) - window_size + 1, step):
        window = sequence[i:i+window_size]
        gc_count = window.count('G') + window.count('C')
        gc_percent = (gc_count / window_size) * 100
        
        windows.append({
            'position': i,
            'sequence': window,
            'gc_percent': gc_percent
        })
        
        print(f"Position {i:3d}: {window} | GC: {gc_percent:5.1f}%")
    
    # Find highest and lowest GC windows
    if windows:
        highest = max(windows, key=lambda x: x['gc_percent'])
        lowest = min(windows, key=lambda x: x['gc_percent'])
        
        print(f"\nHighest GC: {highest['gc_percent']:.1f}% at position {highest['position']}")
        print(f"Lowest GC:  {lowest['gc_percent']:.1f}% at position {lowest['position']}")
    
    return windows

# Test
sequence = "ATCGATCGGGCCCGATCGAAAATTTGCGCGATCG"
sliding_window_gc(sequence, window_size=8, step=4)
```

### Example 4: Multiple Sequence Processor

```python
def process_sequences(sequences):
    """Process multiple sequences and generate report"""
    print(f"Processing {len(sequences)} sequences...\n")
    
    for i, seq in enumerate(sequences, start=1):
        print(f"=== Sequence {i} ===")
        print(f"Sequence: {seq}")
        print(f"Length: {len(seq)} bp")
        
        # Nucleotide composition
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for base in seq:
            if base in counts:
                counts[base] += 1
        
        print("Composition:", ", ".join([f"{k}:{v}" for k, v in counts.items()]))
        
        # GC content
        gc = ((counts['G'] + counts['C']) / len(seq) * 100) if len(seq) > 0 else 0
        print(f"GC content: {gc:.2f}%")
        
        # Validation
        valid = set(seq).issubset(set("ATCG"))
        print(f"Valid: {valid}")
        
        print()

# Test
sequences = [
    "ATCGATCG",
    "GCTAGCTA",
    "ATCGGGCCCTAG",
    "AAATTTGCGC"
]
process_sequences(sequences)
```

---

## 📝 Practice Tasks (Day 8)

### Basic Exercises

1. **Number Printer**: Print numbers from 1 to 20 using a `for` loop.

2. **Countdown**: Use a `while` loop to print numbers from 10 down to 1.

3. **Even Numbers**: Print even numbers between 1 and 50 using a loop.

4. **Break Practice**: Create a loop that stops when it reaches the number 7.

5. **Skip Multiples**: Use `continue` to skip multiples of 3 in a loop from 1 to 15.

### Intermediate Challenges

6. **Nucleotide Counter**: Count each nucleotide (A, T, C, G) in the sequence "ATCGATCGATCGATCG".

7. **Codon Printer**: Print all codons from the sequence "AUGUCGGCUAAACCCGGGAAA".

8. **Quality Filter**: Given a list of quality scores, count how many pass (≥30) and fail (<30).

9. **Find Motif**: Search for the motif "GAATTC" in a DNA sequence and print its position.

10. **GC Calculator**: Calculate GC content for each sequence in a list of sequences.

### Advanced Challenges

11. **Sequence Validator**: Loop through multiple sequences and validate each one (only ATCG allowed). Stop at first invalid sequence.

12. **ORF Scanner**: Write a program that scans a sequence for start codon (ATG) and stop codons (TAA/TAG/TGA) using nested loops.

13. **Pairwise Comparison**: Compare all pairs of sequences from a list and calculate their similarity percentage.

14. **Sliding Window**: Implement sliding window analysis that calculates GC content for windows of size 10, stepping by 5 bases.

15. **Multiplication Table**: Create a nested loop to print a multiplication table for numbers 1–5 (bioinformatics extension: use it to create a scoring matrix).

---

## 💡 Key Takeaways

✓ `for` loops iterate over sequences (strings, lists, ranges)  
✓ `while` loops continue while a condition is `True`  
✓ `range(start, stop, step)` generates number sequences  
✓ `enumerate()` provides both index and value in loops  
✓ `break` exits the loop immediately  
✓ `continue` skips current iteration and moves to next  
✓ `else` with loops executes if loop completes without `break`  
✓ Nested loops enable pairwise comparisons and matrix operations  
✓ Loops are essential for sequence processing and batch analysis  
✓ Always ensure `while` loops have an exit condition to avoid infinite loops  
✓ Use `for` when you know iterations, `while` when condition-dependent  
✓ List comprehensions can replace simple loops for cleaner code  

**Next**: Day 9 - Functions (Creating reusable code blocks and organizing programs)
