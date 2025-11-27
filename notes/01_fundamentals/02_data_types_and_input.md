# Day 2: Data Types & Input

## 🔢 Understanding Python Data Types

Every value in Python has a **data type** that determines what operations you can perform on it. Python has several built-in data types, but we'll focus on the four fundamental ones first.

### The Four Fundamental Types

| Type | Description | Example | Use Case |
|------|-------------|---------|----------|
| **int** | Whole numbers (positive, negative, or zero) | `42`, `-17`, `0` | Counting, indexing, IDs |
| **float** | Decimal/floating-point numbers | `3.14`, `-0.5`, `2.0` | Measurements, percentages, calculations |
| **str** | Text/string data (in quotes) | `"DNA"`, `'ATCG'` | Sequences, names, text data |
| **bool** | Boolean values (True or False) | `True`, `False` | Conditions, flags, logic |

### Exploring Data Types

```python
# Examples of each data type
age = 25                    # int - whole number
gc_content = 52.3           # float - decimal number
dna_sequence = "ATCGATCG"   # str - text/sequence
is_valid = True             # bool - logical value

# Check the type of any variable using type()
print(age, "→", type(age))
print(gc_content, "→", type(gc_content))
print(dna_sequence, "→", type(dna_sequence))
print(is_valid, "→", type(is_valid))
```

**Output:**

```
25 → <class 'int'>
52.3 → <class 'float'>
ATCGATCG → <class 'str'>
True → <class 'bool'>
```

### Integers (int)

Integers are whole numbers without decimal points. They can be positive, negative, or zero.

```python
# Integer examples in bioinformatics
sequence_length = 1500        # Length of a DNA sequence
chromosome_number = 23        # Human chromosome count
read_depth = 50              # Sequencing coverage
mutation_position = -1       # Can be negative (often used as flag)

# Python integers have unlimited precision!
very_large_number = 123456789012345678901234567890
print(very_large_number)  # No overflow error!
```

### Floats (float)

Floats represent decimal numbers. Essential for scientific calculations.

```python
# Float examples in bioinformatics
gc_percentage = 45.7          # GC content percentage
e_value = 1.5e-10            # Scientific notation (1.5 × 10⁻¹⁰)
melting_temperature = 72.5    # Tm of a primer
ratio = 260.0 / 280.0        # Absorbance ratio for purity

print(f"E-value: {e_value}")  # 1.5e-10
print(f"Ratio: {ratio}")      # 0.9285714285714286
```

**Important**: Floats have limited precision (~15-17 decimal places)

```python
# Float precision limitation
result = 0.1 + 0.2
print(result)  # 0.30000000000000004 (not exactly 0.3!)
```

### Strings (str)

Strings are sequences of characters enclosed in quotes. Crucial for working with biological sequences!

```python
# String examples
dna = "ATCGATCG"
gene_name = 'BRCA1'
description = """
This is a multi-line string.
Useful for longer text.
"""

# Strings can use single, double, or triple quotes
print("Single or double quotes are interchangeable")
print('But be consistent!')

# Triple quotes preserve line breaks
sequence_header = """
>seq001
ATCGATCGATCGATCG
"""
print(sequence_header)
```

### Booleans (bool)

Booleans represent truth values: `True` or `False`. Essential for decision-making in programs.

```python
# Boolean examples
sequence_is_valid = True
contains_ambiguous_base = False
is_protein_coding = True
mutation_found = False

# Booleans are often results of comparisons
length = 150
is_short_read = length < 200  # True
is_long_read = length > 500   # False

print(f"Is short read? {is_short_read}")  # True
print(f"Is long read? {is_long_read}")    # False
```

**Note**: Boolean values are capitalized (`True`, `False`), not `true` or `false`.

---

## 🔄 Type Casting: Converting Between Types

Type casting allows you to convert data from one type to another. This is essential when working with user input or different data sources.

### Common Type Conversions

```python
# String to Integer
sequence_id_str = "12345"
sequence_id_int = int(sequence_id_str)
print(sequence_id_int + 1)  # 12346

# String to Float
gc_content_str = "52.3"
gc_content_float = float(gc_content_str)
print(gc_content_float + 1.5)  # 53.8

# Number to String
read_count = 1000
message = "Total reads: " + str(read_count)
print(message)  # Total reads: 1000

# Integer to Float
bases = 100
bases_float = float(bases)
print(bases_float)  # 100.0

# Float to Integer (truncates decimal part)
gc = 52.7
gc_int = int(gc)
print(gc_int)  # 52 (not rounded, just truncated!)
```

### Type Conversion Table

| From → To | Function | Example | Result |
|-----------|----------|---------|--------|
| str → int | `int()` | `int("123")` | `123` |
| str → float | `float()` | `float("12.5")` | `12.5` |
| int → str | `str()` | `str(123)` | `"123"` |
| float → str | `str()` | `str(12.5)` | `"12.5"` |
| float → int | `int()` | `int(12.9)` | `12` |
| int → float | `float()` | `float(12)` | `12.0` |
| any → bool | `bool()` | `bool(1)` | `True` |

### Boolean Conversion Rules

When converting to boolean, Python follows these rules:

```python
# These values are considered False:
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False (empty string)
print(bool([]))         # False (empty list)
print(bool(None))       # False

# Everything else is considered True:
print(bool(1))          # True
print(bool(-1))         # True
print(bool("DNA"))      # True
print(bool(0.1))        # True
```

### Handling Conversion Errors

Be careful: not all conversions are valid!

```python
# This will cause an error:
# invalid_conversion = int("hello")  # ValueError: invalid literal for int()

# Safe conversion with error handling (we'll learn more about this later)
text = "ATCG"
try:
    number = int(text)
except ValueError:
    print(f"Cannot convert '{text}' to integer")
```

---

## ⌨️ Getting User Input

The `input()` function allows your program to interact with users. **Important**: `input()` always returns a string!

### Basic Input

```python
# Get user input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# The type is always string
favorite_number = input("Enter your favorite number: ")
print(type(favorite_number))  # <class 'str'>
```

### Converting Input to Numbers

Since `input()` returns strings, you must convert them for mathematical operations:

```python
# Get numeric input
age_str = input("Enter your age: ")
age = int(age_str)  # Convert to integer

years_to_100 = 100 - age
print(f"You'll be 100 in {years_to_100} years!")

# Or combine input and conversion in one line:
weight = float(input("Enter weight in kg: "))
print(f"Weight in pounds: {weight * 2.205}")
```

### Practical Bioinformatics Example

```python
# DNA Sequence Quality Check
print("=== DNA Sequence Analyzer ===\n")

# Get sequence from user
sequence = input("Enter DNA sequence: ").upper()  # Convert to uppercase
length = len(sequence)  # Get length

# Get expected length
expected_length = int(input("Enter expected length: "))

# Check if length matches
is_correct_length = length == expected_length

print(f"\nSequence: {sequence}")
print(f"Actual length: {length}")
print(f"Expected length: {expected_length}")
print(f"Length is correct: {is_correct_length}")
```

**Sample Interaction:**

```
=== DNA Sequence Analyzer ===

Enter DNA sequence: atcgatcg
Enter expected length: 8

Sequence: ATCGATCG
Actual length: 8
Expected length: 8
Length is correct: True
```

### Multiple Inputs

```python
# Get multiple values at once
print("Enter start and end positions (separated by space):")
start, end = input().split()  # Split input by spaces
start = int(start)
end = int(end)

length = end - start + 1
print(f"Sequence region length: {length}")
```

### Input Validation

Always validate user input in real programs:

```python
# Basic validation example
sequence = input("Enter DNA sequence: ").upper()

# Check if sequence contains only valid bases
valid_bases = set("ATCGN")
sequence_bases = set(sequence)

if sequence_bases.issubset(valid_bases):
    print("✓ Valid DNA sequence")
else:
    invalid = sequence_bases - valid_bases
    print(f"✗ Invalid characters found: {invalid}")
```

---

## 🧬 Practical Example: GC Content Calculator

Let's combine everything we've learned:

```python
"""
GC Content Calculator
Calculates the percentage of G and C bases in a DNA sequence
"""

print("=== GC Content Calculator ===\n")

# Get DNA sequence
dna = input("Enter DNA sequence: ").upper()

# Count total bases
total_bases = len(dna)

# Count G and C
g_count = dna.count('G')
c_count = dna.count('C')
gc_count = g_count + c_count

# Calculate percentage
gc_percentage = (gc_count / total_bases) * 100

# Display results
print(f"\nSequence Analysis:")
print(f"  Total bases: {total_bases}")
print(f"  G count: {g_count}")
print(f"  C count: {c_count}")
print(f"  GC content: {gc_percentage:.2f}%")

# Interpretation
is_gc_rich = gc_percentage > 60
print(f"  GC-rich region: {is_gc_rich}")
```

---

## 📝 Practice Tasks (Day 2)

### Basic Exercises

1. **Age Calculator**: Ask the user for their birth year (as integer) and calculate their age in 2025.

2. **Type Conversion**: Create a string `"3.14"`, convert it to float, then to int, and print all three values with their types.

3. **Product Calculator**: Ask for two numbers from the user and print their product.

4. **Boolean Practice**: Create a variable `is_python_fun = True` and print it along with its type.

### Intermediate Challenges

5. **Temperature Converter**: Ask for temperature in Celsius, convert to Fahrenheit using the formula: F = (C × 9/5) + 32

6. **Sequence Stats**: Ask user for a DNA sequence, then display:
   - The sequence in uppercase
   - Length of the sequence
   - Number of A's, T's, G's, and C's

7. **Data Type Explorer**: Write a program that takes any input and tells the user what type it would be if converted to int, float, str, and bool (handle errors appropriately).

### Advanced Challenge

8. **Mini Sequence Validator**: Create a program that:
   - Asks for a DNA sequence
   - Asks for minimum and maximum allowed lengths
   - Validates the sequence (only ATCGN allowed)
   - Checks if length is within range
   - Calculates and reports GC content
   - Displays all results in a nicely formatted report

---

## 💡 Key Takeaways

✓ Python has four fundamental data types: int, float, str, bool
✓ Use `type()` to check the type of any value
✓ Type casting converts between types: `int()`, `float()`, `str()`, `bool()`
✓ `input()` always returns a string - convert it for calculations
✓ Integers have unlimited precision in Python
✓ Floats have limited precision (~15-17 decimal places)
✓ Booleans are capitalized: `True` and `False`
✓ Always validate user input in production code

**Next**: Day 3 - Operators (Learning to perform calculations and comparisons)
