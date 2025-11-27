# Day 7: Conditional Statements

## 🔀 Understanding Conditional Statements

**Conditional statements** (also called decision-making statements) allow your programs to make choices and execute different code based on whether conditions are true or false. They're fundamental to creating intelligent, responsive programs that can handle different scenarios.

### Why Conditionals Matter in Bioinformatics

- Classify sequences based on characteristics (GC content, length)
- Validate biological data (check sequence validity, format correctness)
- Make decisions in analysis pipelines (quality filtering, threshold detection)
- Handle different file formats or data types
- Implement biological rules (codon usage, splice site detection)
- Error handling and data validation

---

## 🔹 Comparison and Logical Operators Review

### Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal to | `x >= 5` |
| `<=` | Less than or equal to | `x <= 5` |

### Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | Both conditions must be True | `x > 5 and x < 10` |
| `or` | At least one condition must be True | `x < 5 or x > 10` |
| `not` | Negates the condition | `not (x > 5)` |

### Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Checks if value exists in sequence | `'A' in dna_seq` |
| `not in` | Checks if value doesn't exist | `'U' not in dna_seq` |

---

## ✅ The if Statement

The `if` statement executes a block of code **only if** the condition evaluates to `True`.

### Syntax

```python
if condition:
    # code to execute if condition is True
    statement1
    statement2
```

**Important**: Indentation (4 spaces or 1 tab) is required in Python to define the code block!

### Basic Examples

```python
# Simple if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Multiple statements in if block
temperature = 37
if temperature > 30:
    print("It's hot!")
    print("Stay hydrated!")

# No output if condition is False
y = 3
if y > 5:
    print("This won't print")  # Skipped because 3 is not > 5
```

### Bioinformatics Examples

```python
# Check sequence length
dna = "ATCGATCG"
if len(dna) >= 6:
    print(f"Sequence is long enough for analysis: {len(dna)} bp")

# Validate nucleotide
nucleotide = 'A'
if nucleotide in ['A', 'T', 'C', 'G']:
    print(f"{nucleotide} is a valid DNA nucleotide")

# Check GC content
gc_content = 0.58
if gc_content > 0.5:
    print("High GC content detected")
    print("This might indicate GC-rich region")

# Quality score filtering
quality_score = 35
if quality_score >= 30:
    print("High quality read - keep for analysis")

# Sequence similarity
similarity = 0.95
if similarity >= 0.9:
    print("Sequences are highly similar")
```

---

## ✅ The if-else Statement

The `if-else` statement provides an **alternative path**: if the condition is `False`, the `else` block executes.

### Syntax

```python
if condition:
    # executed if condition is True
    statement1
else:
    # executed if condition is False
    statement2
```

### Basic Examples

```python
# Number classification
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Age check
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Bioinformatics Examples

```python
# Sequence validation
sequence = "ATCGATXCG"
if 'X' not in sequence:
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence - contains unknown characters")

# Strand determination
strand = "+"
if strand == "+":
    print("Forward strand")
else:
    print("Reverse strand")

# Quality filtering
quality = 25
if quality >= 30:
    print("Read passed quality filter")
else:
    print("Read failed quality filter - discarding")

# Sequence type detection
sequence = "AUGCUA"
if 'U' in sequence:
    print("This is an RNA sequence")
else:
    print("This is a DNA sequence")

# Length threshold
read_length = 45
min_length = 50
if read_length >= min_length:
    print(f"Read length {read_length} meets minimum requirement")
else:
    print(f"Read too short: {read_length} bp (minimum: {min_length} bp)")
```

---

## ✅ The if-elif-else Chain

When you have **multiple conditions** to check, use `elif` (else if). Python checks each condition in order and executes the first matching block.

### Syntax

```python
if condition1:
    # executed if condition1 is True
    statement1
elif condition2:
    # executed if condition1 is False and condition2 is True
    statement2
elif condition3:
    # executed if condition1 and condition2 are False, and condition3 is True
    statement3
else:
    # executed if all conditions are False
    statement4
```

### Basic Examples

```python
# Grading system
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Temperature classification
temp = 15
if temp > 30:
    print("Hot")
elif temp > 20:
    print("Warm")
elif temp > 10:
    print("Cool")
else:
    print("Cold")

# Time of day
hour = 14
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
elif hour < 22:
    print("Good evening!")
else:
    print("Good night!")
```

### Bioinformatics Examples

```python
# GC content classification
gc_percent = 58.5
if gc_percent > 60:
    print("Very high GC content")
elif gc_percent > 50:
    print("High GC content")
elif gc_percent > 40:
    print("Medium GC content")
else:
    print("Low GC content")

# Sequence length categorization
seq_length = 150
if seq_length >= 500:
    print("Long sequence")
elif seq_length >= 100:
    print("Medium sequence")
elif seq_length >= 20:
    print("Short sequence")
else:
    print("Very short sequence")

# Quality score interpretation
phred_score = 35
if phred_score >= 40:
    print("Excellent quality (99.99% accuracy)")
elif phred_score >= 30:
    print("Good quality (99.9% accuracy)")
elif phred_score >= 20:
    print("Fair quality (99% accuracy)")
else:
    print("Poor quality - consider filtering")

# Protein size classification
amino_acids = 250
if amino_acids < 100:
    print("Small protein")
elif amino_acids < 300:
    print("Medium protein")
elif amino_acids < 600:
    print("Large protein")
else:
    print("Very large protein")

# Expression level categorization
expression_value = 12.5
if expression_value > 10:
    print("Highly expressed")
elif expression_value > 5:
    print("Moderately expressed")
elif expression_value > 1:
    print("Low expression")
else:
    print("Not expressed")
```

---

## ✅ Nested if Statements

You can place an `if` statement **inside another** `if` statement. This is useful for checking multiple related conditions.

### Syntax

```python
if outer_condition:
    statement1
    if inner_condition:
        statement2
    else:
        statement3
else:
    statement4
```

### Basic Examples

```python
# Number classification
num = 15
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even positive number")
    else:
        print("Odd positive number")
else:
    print("Non-positive number")

# Login system
username = "admin"
password = "pass123"
if username == "admin":
    if password == "pass123":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("User not found")

# Age and license check
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("Too young to drive")
```

### Bioinformatics Examples

```python
# Sequence validation and analysis
sequence = "ATCGATCG"
if 'X' not in sequence:
    print("Valid sequence")
    if len(sequence) >= 6:
        print("Length is sufficient for analysis")
        gc_count = sequence.count('G') + sequence.count('C')
        gc_percent = (gc_count / len(sequence)) * 100
        if gc_percent > 50:
            print("High GC content")
        else:
            print("Normal GC content")
    else:
        print("Sequence too short")
else:
    print("Invalid sequence")

# Quality and length filtering
quality = 35
length = 75
min_length = 50
if quality >= 30:
    print("Quality check passed")
    if length >= min_length:
        print("Length check passed - read accepted")
    else:
        print("Read too short - rejected")
else:
    print("Low quality - rejected")

# Gene expression analysis
gene_type = "protein_coding"
expression = 12.5
if gene_type == "protein_coding":
    print("Protein coding gene")
    if expression > 10:
        print("Highly expressed protein coding gene")
        print("Flag for further analysis")
    elif expression > 5:
        print("Moderately expressed")
    else:
        print("Low expression")
else:
    print("Non-coding gene")

# Mutation classification
mutation_type = "SNP"
frequency = 0.25
if mutation_type == "SNP":
    print("Single nucleotide polymorphism")
    if frequency > 0.01:
        print("Common variant")
        if frequency > 0.05:
            print("Very common - likely benign")
    else:
        print("Rare variant - investigate pathogenicity")
```

---

## ✅ Ternary Operator (Short-hand if)

A **ternary operator** is a compact way to write simple `if-else` statements in one line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Basic Examples

```python
# Simple ternary
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Even

# Print directly
age = 20
print("Adult") if age >= 18 else print("Minor")

# Assign value
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(grade)  # Pass

# Multiple ternary (chained)
marks = 75
grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "F"
print(grade)  # C
```

### Bioinformatics Examples

```python
# Sequence type
sequence = "AUGCUA"
seq_type = "RNA" if 'U' in sequence else "DNA"
print(seq_type)  # RNA

# Strand symbol
strand = "+"
strand_name = "forward" if strand == "+" else "reverse"
print(strand_name)  # forward

# Quality pass/fail
quality = 35
status = "PASS" if quality >= 30 else "FAIL"
print(status)  # PASS

# GC content classification
gc_percent = 58
gc_class = "High" if gc_percent > 55 else "Normal"
print(gc_class)  # High

# Expression status
expression = 0.5
exp_status = "Expressed" if expression > 1 else "Not expressed"
print(exp_status)  # Not expressed

# Mutation impact (simplified)
frequency = 0.005
impact = "Rare" if frequency < 0.01 else "Common"
print(impact)  # Rare

# Codon check
codon = "ATG"
start_codon = "Start" if codon == "ATG" else "Not start"
print(start_codon)  # Start
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: Sequence Validator

```python
def validate_sequence(sequence, seq_type="DNA"):
    """Validate DNA or RNA sequence"""
    sequence = sequence.upper()
    
    if seq_type == "DNA":
        valid_chars = set("ATCG")
        if set(sequence).issubset(valid_chars):
            print(f"✓ Valid DNA sequence: {sequence}")
            return True
        else:
            print(f"✗ Invalid DNA sequence: {sequence}")
            print(f"  Contains invalid characters: {set(sequence) - valid_chars}")
            return False
    elif seq_type == "RNA":
        valid_chars = set("AUCG")
        if set(sequence).issubset(valid_chars):
            print(f"✓ Valid RNA sequence: {sequence}")
            return True
        else:
            print(f"✗ Invalid RNA sequence: {sequence}")
            print(f"  Contains invalid characters: {set(sequence) - valid_chars}")
            return False
    else:
        print(f"✗ Unknown sequence type: {seq_type}")
        return False

# Test
validate_sequence("ATCGATCG", "DNA")
validate_sequence("AUCGAUCG", "RNA")
validate_sequence("ATCGATXG", "DNA")
```

### Example 2: GC Content Analyzer

```python
def analyze_gc_content(sequence):
    """Analyze and classify GC content"""
    sequence = sequence.upper()
    
    if len(sequence) == 0:
        print("Error: Empty sequence")
        return None
    
    # Calculate GC content
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_count / len(sequence)) * 100
    
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)} bp")
    print(f"GC content: {gc_percent:.2f}%")
    
    # Classify
    if gc_percent > 70:
        print("Classification: Extremely high GC")
        print("Note: Difficult to sequence, may indicate CpG island")
    elif gc_percent > 60:
        print("Classification: Very high GC")
        print("Note: May indicate promoter region")
    elif gc_percent > 50:
        print("Classification: High GC")
    elif gc_percent > 40:
        print("Classification: Moderate GC")
        print("Note: Typical for many organisms")
    elif gc_percent > 30:
        print("Classification: Low GC")
    else:
        print("Classification: Very low GC")
        print("Note: Unusual, check sequence quality")
    
    return gc_percent

# Test
analyze_gc_content("GCGCGCGCGC")
print()
analyze_gc_content("ATATATATATAT")
```

### Example 3: Quality Filter

```python
def filter_read(sequence, quality_score, min_length=50, min_quality=30):
    """Filter sequencing read based on quality and length"""
    passed = True
    reasons = []
    
    # Check length
    if len(sequence) < min_length:
        passed = False
        reasons.append(f"Length {len(sequence)} < minimum {min_length}")
    
    # Check quality
    if quality_score < min_quality:
        passed = False
        reasons.append(f"Quality {quality_score} < minimum {min_quality}")
    
    # Check for ambiguous bases
    ambiguous = set(sequence.upper()) - set("ATCGN")
    if ambiguous:
        passed = False
        reasons.append(f"Contains ambiguous bases: {ambiguous}")
    
    # Report
    if passed:
        print(f"✓ PASS: Read accepted")
        print(f"  Length: {len(sequence)} bp")
        print(f"  Quality: {quality_score}")
    else:
        print(f"✗ FAIL: Read rejected")
        for reason in reasons:
            print(f"  - {reason}")
    
    return passed

# Test
print("Read 1:")
filter_read("ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG", 35)
print("\nRead 2:")
filter_read("ATCGATCG", 35)
print("\nRead 3:")
filter_read("ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG", 25)
```

### Example 4: Codon Classification

```python
def classify_codon(codon):
    """Classify a codon as start, stop, or regular"""
    codon = codon.upper()
    
    if len(codon) != 3:
        print(f"Error: Invalid codon length ({len(codon)})")
        return None
    
    if codon == "ATG":
        print(f"{codon}: START codon (Methionine)")
        return "start"
    elif codon in ["TAA", "TAG", "TGA"]:
        print(f"{codon}: STOP codon")
        if codon == "TAA":
            print("  (Ochre)")
        elif codon == "TAG":
            print("  (Amber)")
        else:
            print("  (Opal)")
        return "stop"
    else:
        print(f"{codon}: Regular codon")
        return "regular"

# Test
classify_codon("ATG")
classify_codon("TAA")
classify_codon("GCC")
```

---

## 📝 Practice Tasks (Day 7)

### Basic Exercises

1. **Positive/Negative/Zero Checker**: Write a program that checks if a number is positive, negative, or zero.

2. **Even or Odd**: Take a number from the user and print whether it is even or odd.

3. **Grading System**: Create a grading program that assigns A (90-100), B (80-89), C (70-79), D (60-69), or F (0-59) based on score.

4. **Divisibility Check**: Use nested `if` to check if a number is divisible by both 2 and 3.

5. **Age Classifier**: Use ternary operator to print "Adult" if age ≥ 18, otherwise "Minor".

### Intermediate Challenges

6. **DNA Validator**: Write a function that checks if a string contains only valid DNA nucleotides (A, T, C, G). Print "Valid" or "Invalid".

7. **GC Content Classifier**: Calculate GC content of a sequence and classify it as "High" (>60%), "Medium" (40-60%), or "Low" (<40%).

8. **Sequence Type Detector**: Given a sequence, determine if it's DNA (contains T), RNA (contains U), or invalid (contains both or neither).

9. **Quality Filter**: Create a function that accepts/rejects sequencing reads based on length (min 50 bp) and quality score (min 30).

10. **Codon Analyzer**: Write a function that checks if a codon is a start codon (ATG), stop codon (TAA/TAG/TGA), or regular codon.

### Advanced Challenges

11. **Multi-Criteria Validator**: Create a comprehensive sequence validator that checks:
    - Contains only valid nucleotides
    - Length is between 20-1000 bp
    - GC content is between 20-80%
    - Print specific error messages for each failed criterion

12. **ORF Detector**: Write a function that checks if a sequence is a potential ORF:
    - Starts with ATG
    - Ends with stop codon
    - Length is multiple of 3
    - Contains no internal stop codons

13. **Expression Level Classifier**: Create a classifier for gene expression data that considers both expression value and fold-change, with different thresholds for upregulated/downregulated genes.

14. **Mutation Classifier**: Write a function that classifies mutations as:
    - Silent (synonymous)
    - Missense (non-synonymous)
    - Nonsense (creates stop codon)
    - Based on original and mutated codons

15. **Read Quality Analyzer**: Create a comprehensive read quality analyzer that checks multiple criteria (length, quality, GC content, complexity) and provides a detailed quality report with specific recommendations.

---

## 💡 Key Takeaways

✓ `if` executes code only when condition is `True`  
✓ `if-else` provides alternative paths for `True` and `False`  
✓ `if-elif-else` chains handle multiple conditions (checked in order)  
✓ Nested `if` statements allow checking multiple related conditions  
✓ Ternary operator provides compact one-line conditional assignments  
✓ Indentation is crucial in Python for defining code blocks  
✓ Use comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) for conditions  
✓ Combine conditions with logical operators (`and`, `or`, `not`)  
✓ Use `in` and `not in` for membership testing  
✓ First matching condition in `if-elif-else` executes, rest are skipped  
✓ Conditionals are essential for data validation and quality control  
✓ Use clear, readable conditions over complex nested structures when possible  

**Next**: Day 8 - Loops (Automating repetitive tasks and iterating through sequences)
