# Day 3: Operators

## Introduction to Operators

**Operators** are special symbols that perform operations on values and variables. They are the building blocks of expressions and calculations in Python. Understanding operators is crucial for:
- Performing calculations on biological data
- Making comparisons and decisions
- Manipulating sequence data
- Creating logical conditions

Python provides several categories of operators, each serving a specific purpose.

---

## ➕ Arithmetic Operators

Arithmetic operators perform mathematical calculations. Essential for analyzing numerical biological data!

### Basic Arithmetic Operations

```python
a = 10
b = 3

print("Addition:", a + b)         # 13
print("Subtraction:", a - b)      # 7
print("Multiplication:", a * b)   # 30
print("Division:", a / b)         # 3.333... (always returns float)
print("Floor Division:", a // b)  # 3 (removes decimal part)
print("Modulus:", a % b)          # 1 (remainder after division)
print("Exponent:", a ** b)        # 1000 (10³)
```

### Operator Details

| Operator | Name | Example | Result | Description |
|----------|------|---------|--------|-------------|
| `+` | Addition | `5 + 3` | `8` | Adds two numbers |
| `-` | Subtraction | `5 - 3` | `2` | Subtracts right from left |
| `*` | Multiplication | `5 * 3` | `15` | Multiplies two numbers |
| `/` | Division | `5 / 2` | `2.5` | True division (returns float) |
| `//` | Floor Division | `5 // 2` | `2` | Integer division (truncates) |
| `%` | Modulus | `5 % 2` | `1` | Returns remainder |
| `**` | Exponent | `5 ** 2` | `25` | Raises to power |

### Bioinformatics Applications

```python
# Calculate GC content percentage
total_bases = 1000
gc_count = 520
gc_percentage = (gc_count / total_bases) * 100
print(f"GC Content: {gc_percentage}%")  # 52.0%

# Calculate coverage
total_reads = 1000000
genome_length = 5000000
coverage = total_reads / genome_length
print(f"Coverage: {coverage}x")  # 0.2x

# Find codon positions (every 3rd position)
position = 10
codon_number = position // 3  # Which codon is this base in?
position_in_codon = position % 3  # Position within the codon (0, 1, or 2)
print(f"Position {position} is in codon {codon_number}, position {position_in_codon}")

# Calculate primer melting temperature (simplified formula)
primer_length = 20
gc_content = 10
tm = 4 * gc_content + 2 * (primer_length - gc_content)
print(f"Melting temperature: {tm}°C")
```

### Operator Precedence

Python follows mathematical order of operations (PEMDAS):

```python
# Without parentheses
result1 = 2 + 3 * 4  # Multiplication first: 2 + 12 = 14

# With parentheses
result2 = (2 + 3) * 4  # Parentheses first: 5 * 4 = 20

print(result1)  # 14
print(result2)  # 20

# Complex expression
result3 = 10 + 2 ** 3 * 4 / 2 - 1  # 10 + 8*4/2 - 1 = 10 + 16 - 1 = 25
print(result3)
```

---

## ⚖️ Comparison (Relational) Operators

Comparison operators compare values and return Boolean results (`True` or `False`). Crucial for decision-making!

### Comparison Operations

```python
x = 5
y = 10

print("Equal:", x == y)              # False
print("Not equal:", x != y)          # True
print("Greater than:", x > y)        # False
print("Less than:", x < y)           # True
print("Greater or equal:", x >= 5)   # True
print("Less or equal:", y <= 10)     # True
```

### Comparison Table

| Operator | Name | Example | Result | Description |
|----------|------|---------|--------|-------------|
| `==` | Equal | `5 == 5` | `True` | Checks if values are equal |
| `!=` | Not equal | `5 != 3` | `True` | Checks if values are different |
| `>` | Greater than | `5 > 3` | `True` | Left is larger than right |
| `<` | Less than | `5 < 3` | `False` | Left is smaller than right |
| `>=` | Greater or equal | `5 >= 5` | `True` | Left is larger or equal |
| `<=` | Less or equal | `5 <= 3` | `False` | Left is smaller or equal |

### Bioinformatics Applications

```python
# Sequence quality control
read_length = 150
min_length = 50
max_length = 300

is_valid_length = (read_length >= min_length) and (read_length <= max_length)
print(f"Valid read length: {is_valid_length}")  # True

# GC content filtering
gc_content = 45.5
is_gc_rich = gc_content > 60
is_gc_poor = gc_content < 40
is_gc_normal = not (is_gc_rich or is_gc_poor)
print(f"Normal GC content: {is_gc_normal}")  # True

# Compare sequences
seq1_length = 100
seq2_length = 100
sequences_same_length = seq1_length == seq2_length
print(f"Same length: {sequences_same_length}")  # True

# Quality score threshold
quality_score = 30
high_quality = quality_score >= 30
print(f"High quality: {high_quality}")  # True
```

### String Comparisons

```python
# Strings are compared lexicographically (alphabetically)
print("apple" < "banana")  # True (a comes before b)
print("DNA" == "DNA")      # True
print("ATCG" > "ATCC")     # True (G comes after C)

# Case matters!
print("dna" == "DNA")      # False

# Comparing sequence bases
base1 = "A"
base2 = "T"
print(base1 == base2)      # False
```

---

## 🔗 Logical Operators

Logical operators combine multiple conditions and return Boolean results. Essential for complex decision-making!

### The Three Logical Operators

```python
p = True
q = False

print("AND:", p and q)    # False (both must be True)
print("OR:", p or q)      # True (at least one must be True)
print("NOT:", not p)      # False (inverts the value)
```

### Truth Tables

**AND Operator** - Both conditions must be True:

| p | q | p and q |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**OR Operator** - At least one condition must be True:

| p | q | p or q |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**NOT Operator** - Inverts the Boolean value:

| p | not p |
|---|-------|
| True | False |
| False | True |

### Bioinformatics Applications

```python
# Sequence validation
sequence = "ATCGATCG"
min_length = 5
max_length = 100

# Check if sequence length is within range
is_valid_length = len(sequence) >= min_length and len(sequence) <= max_length
print(f"Valid length: {is_valid_length}")  # True

# Check for stop codons
has_taa = "TAA" in sequence
has_tag = "TAG" in sequence
has_tga = "TGA" in sequence
has_stop_codon = has_taa or has_tag or has_tga
print(f"Contains stop codon: {has_stop_codon}")  # False

# Quality filtering
quality_score = 35
read_length = 150
gc_content = 50

# Keep reads that meet multiple criteria
is_high_quality = (quality_score >= 30 and 
                   read_length >= 100 and 
                   gc_content >= 40 and gc_content <= 60)
print(f"High quality read: {is_high_quality}")  # True

# Exclude reads with ambiguous bases
contains_n = "N" in sequence
is_clean = not contains_n
print(f"Clean sequence: {is_clean}")  # True
```

### Short-Circuit Evaluation

Python evaluates logical operators efficiently:

```python
# AND: If first condition is False, second is not evaluated
x = 0
result = (x != 0) and (10 / x > 5)  # Safe! Doesn't cause division by zero

# OR: If first condition is True, second is not evaluated
y = 100
result = (y == 100) or (10 / 0 > 5)  # Safe! Doesn't evaluate second part
```

---

## 🔑 Assignment Operators

Assignment operators assign values to variables. They can combine assignment with arithmetic operations for conciseness.

### Basic Assignment

```python
x = 5  # Assign 5 to x
```

### Compound Assignment Operators

```python
x = 10

x += 3   # x = x + 3  → x becomes 13
x -= 2   # x = x - 2  → x becomes 11
x *= 4   # x = x * 4  → x becomes 44
x /= 2   # x = x / 2  → x becomes 22.0
x //= 3  # x = x // 3 → x becomes 7.0
x %= 5   # x = x % 5  → x becomes 2.0
x **= 2  # x = x ** 2 → x becomes 4.0

print(x)  # 4.0
```

### Complete Assignment Operators Table

| Operator | Example | Equivalent | Description |
|----------|---------|------------|-------------|
| `=` | `x = 5` | - | Simple assignment |
| `+=` | `x += 3` | `x = x + 3` | Add and assign |
| `-=` | `x -= 3` | `x = x - 3` | Subtract and assign |
| `*=` | `x *= 3` | `x = x * 3` | Multiply and assign |
| `/=` | `x /= 3` | `x = x / 3` | Divide and assign |
| `//=` | `x //= 3` | `x = x // 3` | Floor divide and assign |
| `%=` | `x %= 3` | `x = x % 3` | Modulus and assign |
| `**=` | `x **= 3` | `x = x ** 3` | Exponent and assign |

### Bioinformatics Applications

```python
# Count nucleotides in a sequence
sequence = "ATCGATCGATCGNNNATCG"

a_count = 0
t_count = 0
g_count = 0
c_count = 0

for base in sequence:
    if base == 'A':
        a_count += 1  # Increment A counter
    elif base == 'T':
        t_count += 1
    elif base == 'G':
        g_count += 1
    elif base == 'C':
        c_count += 1

print(f"A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}")

# Calculate running total for coverage
total_coverage = 0.0
total_coverage += 15.5  # Sample 1
total_coverage += 18.2  # Sample 2
total_coverage += 20.1  # Sample 3
average_coverage = total_coverage / 3
print(f"Average coverage: {average_coverage:.2f}x")
```

---

## 🔍 Membership Operators

Membership operators test whether a value exists in a sequence (string, list, tuple, set, etc.). Perfect for sequence analysis!

### The Two Membership Operators

```python
sequence = "ATCGATCG"
codon_list = ["ATG", "TAA", "TAG", "TGA"]

# Check if value exists
print("ATG" in codon_list)      # True
print("GGG" in codon_list)      # False

# Check if value doesn't exist
print("N" not in sequence)      # True
print("A" not in sequence)      # False
```

### Bioinformatics Applications

```python
# Check for specific bases
dna_sequence = "ATCGATCGNNNATCG"

has_adenine = "A" in dna_sequence
has_uracil = "U" in dna_sequence  # False for DNA
has_ambiguous = "N" in dna_sequence

print(f"Contains A: {has_adenine}")      # True
print(f"Contains U: {has_uracil}")       # False
print(f"Contains N: {has_ambiguous}")    # True

# Check for motifs/patterns
motif = "GATC"
has_motif = motif in dna_sequence
print(f"Contains GATC motif: {has_motif}")  # True

# Check for restriction sites
restriction_sites = ["EcoRI", "BamHI", "HindIII"]
enzyme = "EcoRI"
is_available = enzyme in restriction_sites
print(f"{enzyme} available: {is_available}")  # True

# Validate nucleotides
valid_dna_bases = "ATCG"
test_base = "X"
is_valid = test_base in valid_dna_bases
print(f"Valid DNA base: {is_valid}")  # False

# Check for start/stop codons
start_codons = ["ATG"]
stop_codons = ["TAA", "TAG", "TGA"]

test_codon = "ATG"
is_start = test_codon in start_codons
is_stop = test_codon in stop_codons

print(f"Start codon: {is_start}")  # True
print(f"Stop codon: {is_stop}")    # False
```

### Case Sensitivity

```python
# Membership operators are case-sensitive
sequence = "ATCG"

print("atcg" in sequence)    # False
print("ATCG" in sequence)    # True

# Convert to uppercase for case-insensitive search
user_input = "atcg"
print(user_input.upper() in sequence)  # True
```

---

## 🆔 Identity Operators

Identity operators check if two variables point to the same object in memory (not just equal values). Important for understanding Python's object model!

### The Two Identity Operators

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # False (different objects, same content)
print(a is c)      # True (same object)
print(a is not b)  # True (confirms they're different objects)

# Check content equality
print(a == b)      # True (same content)
```

### Identity vs. Equality

**`is`** checks if variables refer to the same object in memory  
**`==`** checks if variables have the same value

```python
# Lists: Different objects even with same content
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True (same content)
print(list1 is list2)  # False (different objects)

# Small integers: Python reuses same objects (optimization)
x = 5
y = 5

print(x == y)  # True (same value)
print(x is y)  # True (same object! Python optimization)

# Large integers: Different objects
big_x = 1000000
big_y = 1000000

print(big_x == big_y)  # True (same value)
print(big_x is big_y)  # False (different objects)

# Strings: Often same object (string interning)
str1 = "DNA"
str2 = "DNA"

print(str1 == str2)  # True
print(str1 is str2)  # True (Python optimization)
```

### When to Use Which

- Use `==` to compare values (most common)
- Use `is` to check if something is `None`, `True`, or `False`
- Use `is` when checking object identity matters

```python
# Best practice: Check for None using 'is'
result = None

if result is None:
    print("No result available")

# Check for boolean values
flag = True
if flag is True:
    print("Flag is set")

# For value comparison, use ==
sequence1 = "ATCG"
sequence2 = "ATCG"
if sequence1 == sequence2:
    print("Sequences match")
```

### Bioinformatics Context

```python
# Check if variable has been initialized
sequence_data = None

if sequence_data is None:
    print("No sequence loaded yet")
    sequence_data = "ATCGATCG"

# Compare references to large data structures
reference_genome = ["chr1", "chr2", "chr3"]
working_copy = reference_genome  # Same object
independent_copy = reference_genome.copy()  # Different object

print(working_copy is reference_genome)      # True
print(independent_copy is reference_genome)  # False
print(independent_copy == reference_genome)  # True
```

---

## 📝 Practice Tasks (Day 3)

### Basic Exercises

1. **Arithmetic Practice**: Take two numbers from the user and perform all arithmetic operations (+, -, *, /, //, %, **). Display results with labels.

2. **Range Checker**: Write a program to check if a number is greater than 100 AND less than 200.

3. **Logical Combinations**: Create variables for three conditions and demonstrate all combinations of `and`, `or`, and `not`.

4. **Membership Test**: Check if the letters 'p', 'y', 't' exist in the string 'Python' and print results.

5. **Identity vs Equality**: Create two lists with same content and show the difference between `is` and `==`.

### Intermediate Challenges

6. **GC Content Analyzer**: Ask for a DNA sequence and calculate:
   - Total bases
   - G count and C count
   - GC percentage
   - Whether GC content is between 40% and 60%

7. **Sequence Validator**: Write a program that:
   - Takes a DNA sequence as input
   - Checks if length is between 10 and 100
   - Verifies it contains only A, T, G, C
   - Confirms it doesn't contain 'N'
   - Reports if sequence is valid

8. **Codon Position Calculator**: Given a position in a sequence:
   - Calculate which codon it belongs to (using //)
   - Find position within that codon (using %)
   - Example: position 10 → codon 3, position 1

### Advanced Challenges

9. **Quality Filter**: Create a read quality filter that accepts a read if:
   - Quality score >= 30
   - Read length >= 100
   - GC content between 40% and 60%
   - No ambiguous bases (N)
   - Use logical operators to combine all conditions

10. **Restriction Site Finder**: Write a program that:
    - Takes a DNA sequence
    - Checks for multiple restriction enzyme sites (use membership operators)
    - Counts how many different sites are present
    - Reports if sequence is suitable for cloning (has specific sites)

---

## 💡 Key Takeaways

✓ **Arithmetic operators** perform calculations: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
✓ **Comparison operators** compare values and return Boolean: `==`, `!=`, `>`, `<`, `>=`, `<=`  
✓ **Logical operators** combine conditions: `and`, `or`, `not`  
✓ **Assignment operators** assign and modify values: `=`, `+=`, `-=`, `*=`, etc.  
✓ **Membership operators** check for presence in sequences: `in`, `not in`  
✓ **Identity operators** check object identity: `is`, `is not`  
✓ Use `==` for value equality, `is` for identity (especially with `None`)  
✓ Operator precedence follows PEMDAS (use parentheses for clarity)  
✓ Logical operators use short-circuit evaluation

**Next**: Day 4 - Strings (Deep dive into text and sequence manipulation)
