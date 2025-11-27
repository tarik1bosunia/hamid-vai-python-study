# Day 10-11: Functions

## 🔹 Understanding Functions

A **function** is a reusable block of code that performs a specific task. Functions help organize code, avoid repetition, and make programs more modular and maintainable. In bioinformatics, functions are essential for creating analysis pipelines and processing biological data efficiently.

### Why Functions Matter in Bioinformatics

- Create reusable analysis tools (GC calculator, sequence validator)
- Build modular pipelines (quality control → alignment → analysis)
- Encapsulate complex operations (ORF finding, translation)
- Reduce code duplication across projects
- Make code easier to test and debug
- Share functionality across team members
- Create libraries of biological tools

---

## 🔹 Function Anatomy

```python
def function_name(parameters):
    """Docstring: describes what the function does"""
    # Function body
    statement1
    statement2
    return result  # Optional
```

**Components:**
- `def`: Keyword to define a function
- `function_name`: Name following Python naming conventions
- `parameters`: Input values (optional)
- `docstring`: Documentation string (optional but recommended)
- `return`: Output value (optional)

---

## ✅ Basic Functions (No Parameters, No Return)

### Syntax

```python
def function_name():
    # code block
    statement
```

### Examples

```python
# Simple greeting
def greet():
    print("Hello, welcome to Python!")

greet()  # Output: Hello, welcome to Python!

# Sequence banner
def print_banner():
    print("=" * 50)
    print("  DNA SEQUENCE ANALYZER v1.0")
    print("=" * 50)

print_banner()

# Display menu
def show_menu():
    print("\n=== Bioinformatics Tools ===")
    print("1. Calculate GC Content")
    print("2. Translate DNA to Protein")
    print("3. Find ORFs")
    print("4. Exit")

show_menu()
```

---

## ✅ Functions with Parameters

### Positional Parameters

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")  # Hello, Alice!
greet_user("Bob")    # Hello, Bob!

# Multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 25)

# Order matters with positional parameters
def divide(a, b):
    return a / b

print(divide(10, 2))  # 5.0
print(divide(2, 10))  # 0.2
```

### Bioinformatics Examples

```python
# Calculate GC content
def calculate_gc(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_count / len(sequence)) * 100
    print(f"GC Content: {gc_percent:.2f}%")

calculate_gc("ATCGATCG")

# Validate sequence
def validate_dna(sequence):
    valid_bases = set("ATCG")
    sequence_bases = set(sequence.upper())
    if sequence_bases.issubset(valid_bases):
        print("Valid DNA sequence")
    else:
        invalid = sequence_bases - valid_bases
        print(f"Invalid: contains {invalid}")

validate_dna("ATCGATCG")
validate_dna("ATCGXYZ")

# Transcribe DNA to RNA
def transcribe(dna):
    rna = dna.replace('T', 'U')
    print(f"DNA: {dna}")
    print(f"RNA: {rna}")

transcribe("ATCGATCG")

# Display sequence info
def show_sequence_info(name, sequence, organism):
    print(f"\nSequence Name: {name}")
    print(f"Organism: {organism}")
    print(f"Length: {len(sequence)} bp")
    print(f"Sequence: {sequence}")

show_sequence_info("BRCA1", "ATCGATCG", "Homo sapiens")
```

---

## ✅ Functions with Return Values

Functions can return values using the `return` statement. This allows the function to compute something and pass it back to the caller.

### Basic Return Examples

```python
# Return single value
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Sum: {result}")  # Sum: 8

# Return without storing
print(add(10, 20))  # 30

# Return string
def get_greeting(name):
    return f"Hello, {name}!"

message = get_greeting("Alice")
print(message)

# Return boolean
def is_even(number):
    return number % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# Multiple return statements
def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(5))   # Positive
print(classify_number(-3))  # Negative
print(classify_number(0))   # Zero
```

### Bioinformatics Return Examples

```python
# Return GC percentage
def calculate_gc_content(sequence):
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

gc1 = calculate_gc_content("ATCGATCG")
gc2 = calculate_gc_content("GCGCGCGC")
print(f"Sequence 1 GC: {gc1:.2f}%")
print(f"Sequence 2 GC: {gc2:.2f}%")

# Return complement
def get_complement(sequence):
    complement = ""
    base_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in sequence.upper():
        complement += base_pairs.get(base, 'N')
    return complement

original = "ATCG"
comp = get_complement(original)
print(f"Original:   {original}")
print(f"Complement: {comp}")

# Return reverse complement
def reverse_complement(sequence):
    complement = get_complement(sequence)
    return complement[::-1]

seq = "ATCGATCG"
rev_comp = reverse_complement(seq)
print(f"Sequence:           {seq}")
print(f"Reverse Complement: {rev_comp}")

# Return validation status
def is_valid_dna(sequence):
    return set(sequence.upper()).issubset(set("ATCG"))

print(is_valid_dna("ATCG"))    # True
print(is_valid_dna("ATCGX"))   # False

# Return codon count
def count_codons(sequence):
    return len(sequence) // 3

mrna = "AUGUCGGCUAAACCC"
num_codons = count_codons(mrna)
print(f"Number of codons: {num_codons}")
```

### Returning Multiple Values

```python
# Return tuple (multiple values)
def get_nucleotide_counts(sequence):
    sequence = sequence.upper()
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    return a_count, t_count, c_count, g_count

# Unpack returned values
a, t, c, g = get_nucleotide_counts("ATCGATCGATCG")
print(f"A: {a}, T: {t}, C: {c}, G: {g}")

# Return dictionary
def analyze_sequence(sequence):
    sequence = sequence.upper()
    return {
        'length': len(sequence),
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G'),
        'gc_percent': (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
    }

analysis = analyze_sequence("ATCGATCGATCG")
print(f"Length: {analysis['length']}")
print(f"GC%: {analysis['gc_percent']:.2f}")

# Return list
def extract_codons(sequence):
    codons = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            codons.append(codon)
    return codons

mrna = "AUGUCGGCUAAA"
codon_list = extract_codons(mrna)
print(f"Codons: {codon_list}")
```

---

## ✅ Default Parameters

Default parameters have predefined values and are optional when calling the function.

### Syntax and Examples

```python
# Single default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default exponent=2)
print(power(5, 3))   # 125 (overrides default)

# Multiple defaults
def greet(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice"))                          # Hello, Alice!
print(greet("Bob", "Hi"))                      # Hi, Bob!
print(greet("Charlie", "Hey", "."))            # Hey, Charlie.

# Defaults must come after non-defaults
def calculate_interest(principal, rate=5, time=1):
    return principal * rate * time / 100

print(calculate_interest(1000))           # 50.0
print(calculate_interest(1000, 7))        # 70.0
print(calculate_interest(1000, 7, 2))     # 140.0
```

### Bioinformatics Examples

```python
# Sequence validator with default type
def validate_sequence(sequence, seq_type="DNA"):
    sequence = sequence.upper()
    if seq_type == "DNA":
        valid_chars = set("ATCG")
    elif seq_type == "RNA":
        valid_chars = set("AUCG")
    else:
        return False
    return set(sequence).issubset(valid_chars)

print(validate_sequence("ATCG"))           # True (DNA by default)
print(validate_sequence("AUCG", "RNA"))    # True
print(validate_sequence("ATCG", "RNA"))    # False

# GC calculator with window size
def calculate_gc_window(sequence, window_size=10):
    sequence = sequence.upper()
    if len(sequence) < window_size:
        window_size = len(sequence)
    
    window = sequence[:window_size]
    gc = (window.count('G') + window.count('C')) / window_size * 100
    return gc

print(f"GC (default): {calculate_gc_window('ATCGATCGGGCCCC'):.1f}%")
print(f"GC (size=5): {calculate_gc_window('ATCGATCGGGCCCC', 5):.1f}%")

# Read quality filter with threshold
def filter_by_quality(reads, qualities, threshold=30):
    passed = []
    for read, qual in zip(reads, qualities):
        if qual >= threshold:
            passed.append(read)
    return passed

reads = ["ATCG", "GCTA", "TAGC", "CGAT"]
quals = [35, 28, 40, 25]
print(f"Passed (Q≥30): {filter_by_quality(reads, quals)}")
print(f"Passed (Q≥25): {filter_by_quality(reads, quals, 25)}")

# ORF finder with minimum length
def find_orfs(sequence, min_length=30):
    orfs = []
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            for j in range(i+3, len(sequence) - 2, 3):
                if sequence[j:j+3] in stop_codons:
                    orf = sequence[i:j+3]
                    if len(orf) >= min_length:
                        orfs.append(orf)
                    break
    return orfs

dna = "ATGATCGATCGTAGATCGATGATCGATAA"
print(f"ORFs (≥30bp): {len(find_orfs(dna))}")
print(f"ORFs (≥20bp): {len(find_orfs(dna, 20))}")
```

---

## ✅ Keyword Arguments

Keyword arguments allow you to specify parameters by name, making function calls more readable and order-independent.

### Examples

```python
# Order doesn't matter with keywords
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

introduce(name="Alice", age=25, city="Paris")
introduce(age=30, city="London", name="Bob")
introduce("Charlie", city="Berlin", age=28)  # Mix positional and keyword

# Readability benefit
def align_sequences(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-2):
    print(f"Aligning with: match={match_score}, mismatch={mismatch_penalty}, gap={gap_penalty}")

align_sequences("ATCG", "ATCG")
align_sequences("ATCG", "ATCG", gap_penalty=-3, mismatch_penalty=-2)
```

### Bioinformatics Examples

```python
# Sequence analysis with named parameters
def analyze_sequence_detailed(sequence, 
                              calculate_gc=True, 
                              find_motifs=False, 
                              motif="GAATTC",
                              case_sensitive=False):
    if not case_sensitive:
        sequence = sequence.upper()
        motif = motif.upper()
    
    results = {'length': len(sequence)}
    
    if calculate_gc:
        gc = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100
        results['gc_percent'] = gc
    
    if find_motifs:
        count = 0
        for i in range(len(sequence) - len(motif) + 1):
            if sequence[i:i+len(motif)] == motif:
                count += 1
        results['motif_count'] = count
    
    return results

# Clear, readable calls
result1 = analyze_sequence_detailed("ATCGAATTCGATCG", calculate_gc=True)
result2 = analyze_sequence_detailed("ATCGAATTCGATCG", find_motifs=True, motif="GAATTC")
result3 = analyze_sequence_detailed("ATCGAATTCGATCG", calculate_gc=True, find_motifs=True)

print(result1)
print(result2)
print(result3)
```

---

## ✅ Variable-Length Arguments

### *args (Variable Positional Arguments)

```python
# Accept any number of arguments
def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3))           # 6
print(total_sum(1, 2, 3, 4, 5))     # 15
print(total_sum(10))                # 10

# Combine with regular parameters
def calculate_average(name, *scores):
    if scores:
        avg = sum(scores) / len(scores)
        print(f"{name}'s average: {avg:.2f}")
    else:
        print(f"No scores for {name}")

calculate_average("Alice", 85, 90, 78, 92)
calculate_average("Bob", 88)
```

### **kwargs (Variable Keyword Arguments)

```python
# Accept any number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Paris")
print_info(gene="BRCA1", chromosome=17, start=43044295)

# Combine regular, *args, and **kwargs
def create_sequence_record(seq_id, *tags, **metadata):
    print(f"ID: {seq_id}")
    print(f"Tags: {tags}")
    print(f"Metadata: {metadata}")

create_sequence_record("seq001", "validated", "reviewed", 
                      organism="Human", length=1500, gc=58.5)
```

### Bioinformatics Examples

```python
# Calculate statistics for any number of sequences
def sequence_stats(*sequences):
    total_length = 0
    total_gc = 0
    
    for seq in sequences:
        seq = seq.upper()
        total_length += len(seq)
        total_gc += seq.count('G') + seq.count('C')
    
    avg_length = total_length / len(sequences) if sequences else 0
    avg_gc = (total_gc / total_length * 100) if total_length > 0 else 0
    
    print(f"Number of sequences: {len(sequences)}")
    print(f"Average length: {avg_length:.1f} bp")
    print(f"Average GC: {avg_gc:.2f}%")

sequence_stats("ATCG", "GCTAGCTA", "ATCGATCG")

# Flexible sequence processor
def process_sequences(*sequences, reverse=False, complement=False, uppercase=True):
    results = []
    
    for seq in sequences:
        if uppercase:
            seq = seq.upper()
        
        if complement:
            comp = ""
            pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            for base in seq:
                comp += pairs.get(base, 'N')
            seq = comp
        
        if reverse:
            seq = seq[::-1]
        
        results.append(seq)
    
    return results

seqs = process_sequences("ATCG", "GCTA", reverse=True)
print(seqs)

# Metadata logger
def log_analysis(**kwargs):
    print("\n=== Analysis Log ===")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

log_analysis(date="2025-11-27", sequences_processed=150, 
            avg_quality=35.2, pipeline_version="2.1.0")
```

---

## ✅ Lambda Functions (Anonymous Functions)

Lambda functions are small, anonymous functions defined in a single line.

### Syntax

```python
lambda parameters: expression
```

### Examples

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Multiple parameters
multiply = lambda x, y: x * y
print(multiply(4, 5))  # 20

# Used with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filtering
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Sorting
sequences = ["ATCG", "AT", "ATCGATCG", "ATCGAT"]
sorted_by_length = sorted(sequences, key=lambda x: len(x))
print(sorted_by_length)
```

### Bioinformatics Examples

```python
# Calculate GC content (lambda)
gc_content = lambda seq: (seq.count('G') + seq.count('C')) / len(seq) * 100
print(f"GC: {gc_content('ATCGATCG'):.1f}%")

# Complement
complement = lambda base: {'A':'T', 'T':'A', 'C':'G', 'G':'C'}.get(base, 'N')
print(complement('A'))  # T

# Sort sequences by GC content
sequences = ["ATATATAT", "GCGCGCGC", "ATCGATCG"]
sorted_by_gc = sorted(sequences, key=lambda s: s.count('G') + s.count('C'))
print(sorted_by_gc)

# Filter high-quality reads
reads = ["ATCG", "GCTA", "TAGC", "CGAT"]
qualities = [35, 28, 40, 25]
high_quality = [read for read, qual in zip(reads, qualities) if qual >= 30]
print(high_quality)

# Map nucleotide counts
sequences = ["ATCG", "GCTA", "TAGC"]
lengths = list(map(lambda s: len(s), sequences))
print(lengths)
```

---

## 🧬 Practical Bioinformatics Functions

### Complete Function Examples

```python
def comprehensive_sequence_analysis(sequence, seq_type="DNA"):
    """
    Perform comprehensive sequence analysis
    
    Parameters:
        sequence (str): DNA or RNA sequence
        seq_type (str): 'DNA' or 'RNA'
    
    Returns:
        dict: Analysis results
    """
    sequence = sequence.upper()
    
    # Validate
    valid_chars = set("ATCG") if seq_type == "DNA" else set("AUCG")
    is_valid = set(sequence).issubset(valid_chars)
    
    if not is_valid:
        return {'error': 'Invalid sequence'}
    
    # Calculate statistics
    length = len(sequence)
    a_count = sequence.count('A')
    t_u_count = sequence.count('T' if seq_type == "DNA" else 'U')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    gc_percent = ((g_count + c_count) / length * 100) if length > 0 else 0
    
    # Return results
    return {
        'type': seq_type,
        'length': length,
        'nucleotides': {
            'A': a_count,
            'T' if seq_type == "DNA" else 'U': t_u_count,
            'C': c_count,
            'G': g_count
        },
        'gc_percent': round(gc_percent, 2),
        'valid': is_valid
    }

# Test
result = comprehensive_sequence_analysis("ATCGATCGATCG")
print(result)
```

---

## 📝 Practice Tasks (Day 10-11)

### Basic Exercises

1. **Product Function**: Write a function that takes two numbers and returns their product.

2. **Even/Odd Checker**: Create a function that checks if a number is even or odd and returns the result.

3. **Simple Interest**: Write a function with default parameters that calculates simple interest (SI = P × R × T / 100).

4. **Maximum Finder**: Create a function that accepts `*args` and returns the maximum value.

5. **Cube Lambda**: Use a lambda function to calculate the cube of a number.

### Intermediate Challenges

6. **GC Calculator**: Write a function that takes a DNA sequence and returns its GC content percentage.

7. **Sequence Validator**: Create a function that validates DNA sequences and returns True/False with error messages.

8. **Codon Extractor**: Write a function that extracts all codons from a sequence and returns them as a list.

9. **Reverse Complement**: Implement a function that returns the reverse complement of a DNA sequence.

10. **Quality Filter**: Create a function that filters sequences by quality score with a default threshold of 30.

### Advanced Challenges

11. **Multi-Sequence Analyzer**: Write a function using `*args` that analyzes multiple sequences and returns average statistics.

12. **Flexible ORF Finder**: Create an ORF finder with parameters for minimum length, start codon, and stop codons (with defaults).

13. **Sequence Processor**: Build a function with `**kwargs` that can optionally reverse, complement, translate, and format sequences.

14. **FASTA Parser Function**: Write a function that parses FASTA format and returns a dictionary of sequences.

15. **Pipeline Builder**: Create a function that accepts other functions as parameters and applies them in sequence to data (function composition).

---

## 💡 Key Takeaways

✓ Functions encapsulate reusable code blocks  
✓ `def function_name(parameters):` defines a function  
✓ `return` sends values back to caller  
✓ Parameters can be positional, keyword, or have defaults  
✓ Default parameters must come after required parameters  
✓ `*args` accepts variable positional arguments (tuple)  
✓ `**kwargs` accepts variable keyword arguments (dictionary)  
✓ Lambda functions create small anonymous functions  
✓ Docstrings document what functions do  
✓ Functions should do one thing well (single responsibility)  
✓ Use descriptive names for functions and parameters  
✓ Return values rather than printing when possible (more flexible)  

**Next**: Advanced function concepts (scope, closures, decorators) - see `advanced/` directory

**See also**: [Function Part 2 - Deep Dive](./advanced/01_function_deep_dive.md) for scope, closures, decorators, and more advanced concepts.
