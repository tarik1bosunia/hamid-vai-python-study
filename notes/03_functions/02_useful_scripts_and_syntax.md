# Day 12: Useful Scripts & Common Patterns

## 📜 Understanding Useful Patterns

This guide covers **practical Python patterns and mini-scripts** that you'll use frequently in bioinformatics and general programming. These patterns demonstrate Pythonic ways to solve common problems efficiently.

### Why These Patterns Matter

- Write cleaner, more efficient code
- Solve common problems quickly
- Understand idiomatic Python style
- Build foundation for complex algorithms
- Improve code readability
- Leverage Python's built-in capabilities

---

## ✅ Variable Swapping

### Traditional vs Pythonic

```python
# Traditional way (using temp variable)
a = 10
b = 20
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# Pythonic way (tuple unpacking)
a = 10
b = 20
a, b = b, a
print(f"a = {a}, b = {b}")  # a = 20, b = 10

# Swap multiple variables
x, y, z = 1, 2, 3
x, y, z = z, y, x
print(f"x={x}, y={y}, z={z}")  # x=3, y=2, z=1
```

### Bioinformatics Applications

```python
# Swap strands
forward_strand = "ATCG"
reverse_strand = "CGAT"
forward_strand, reverse_strand = reverse_strand, forward_strand
print(f"Forward: {forward_strand}, Reverse: {reverse_strand}")

# Rotate codon positions
first, second, third = "AUG", "UCC", "GCA"
first, second, third = third, first, second
print(f"{first} {second} {third}")
```

---

## ✅ Finding Minimum and Maximum

### Built-in Functions

```python
# Basic min/max
numbers = [5, 9, 2, 7, 3, 8, 1]
print(f"Min: {min(numbers)}")  # 1
print(f"Max: {max(numbers)}")  # 9

# With strings (lexicographic comparison)
words = ["apple", "banana", "cherry", "date"]
print(f"Min: {min(words)}")  # apple
print(f"Max: {max(words)}")  # date

# Multiple arguments
print(min(10, 5, 20, 3))  # 3
print(max(10, 5, 20, 3))  # 20

# Custom key function
sequences = ["ATCG", "AT", "ATCGATCG", "ATCGAT"]
longest = max(sequences, key=len)
shortest = min(sequences, key=len)
print(f"Longest: {longest}")
print(f"Shortest: {shortest}")
```

### Bioinformatics Examples

```python
# Find sequence with highest GC content
sequences = ["ATATATAT", "GCGCGCGC", "ATCGATCG"]
highest_gc = max(sequences, key=lambda s: s.count('G') + s.count('C'))
print(f"Highest GC: {highest_gc}")

# Find read with best quality
reads = ["ATCG", "GCTA", "TAGC"]
qualities = [35, 42, 28]
best_read = reads[qualities.index(max(qualities))]
print(f"Best quality read: {best_read}")

# Find longest ORF
orfs = ["ATGATCGTAG", "ATGATCGATCGATCGTAA", "ATGAAATAG"]
longest_orf = max(orfs, key=len)
print(f"Longest ORF: {longest_orf} ({len(longest_orf)} bp)")
```

---

## ✅ Prime Number Checker

### Implementation

```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(2))    # True
print(is_prime(7))    # True
print(is_prime(12))   # False
print(is_prime(17))   # True
print(is_prime(100))  # False

# Find all primes up to N
def find_primes(n):
    """Find all prime numbers up to n"""
    return [i for i in range(2, n+1) if is_prime(i)]

primes = find_primes(30)
print(f"Primes up to 30: {primes}")
```

### Bioinformatics Connection

```python
# Prime numbers in sequence analysis (example: hash functions)
def simple_hash(sequence, prime=31):
    """Simple polynomial rolling hash using prime"""
    hash_value = 0
    for i, char in enumerate(sequence):
        hash_value += ord(char) * (prime ** i)
    return hash_value % 1000000007

seq1 = "ATCG"
seq2 = "GCTA"
print(f"Hash(seq1): {simple_hash(seq1)}")
print(f"Hash(seq2): {simple_hash(seq2)}")
```

---

## ✅ Factorial Calculation

### Multiple Approaches

```python
# Iterative approach
def factorial_iterative(n):
    """Calculate factorial using loop"""
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    """Calculate factorial using recursion"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Using math module
import math
print(math.factorial(5))  # 120

# Test
print(factorial_iterative(5))  # 120
print(factorial_recursive(5))  # 120
print(factorial_iterative(0))  # 1
print(factorial_iterative(10)) # 3628800
```

### Bioinformatics Applications

```python
# Combinatorial calculations (e.g., k-mer combinations)
def combinations(n, k):
    """Calculate nCk = n! / (k! * (n-k)!)"""
    if k > n:
        return 0
    return factorial_iterative(n) // (factorial_iterative(k) * factorial_iterative(n - k))

# Number of ways to choose 3 positions from 10
print(f"10C3 = {combinations(10, 3)}")  # 120

# Permutations: number of possible codon arrangements
def permutations(n, r):
    """Calculate nPr = n! / (n-r)!"""
    if r > n:
        return 0
    return factorial_iterative(n) // factorial_iterative(n - r)

# Number of ways to arrange 3 codons from 5
print(f"5P3 = {permutations(5, 3)}")  # 60
```

---

## ✅ Fibonacci Sequence

### Implementation

```python
# Generate Fibonacci sequence
def fibonacci_sequence(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci_sequence(10))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Print Fibonacci (memory efficient)
def print_fibonacci(n):
    """Print first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

print_fibonacci(15)

# Get nth Fibonacci number
def fibonacci_nth(n):
    """Return nth Fibonacci number (0-indexed)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"10th Fibonacci: {fibonacci_nth(10)}")  # 55
```

### Pattern Recognition

```python
# Fibonacci in nature (Golden Ratio approximation)
def golden_ratio_approximation(n):
    """Approximate golden ratio using Fibonacci"""
    fib = fibonacci_sequence(n)
    ratios = []
    for i in range(1, len(fib)):
        if fib[i-1] != 0:
            ratio = fib[i] / fib[i-1]
            ratios.append(ratio)
    return ratios

ratios = golden_ratio_approximation(15)
print(f"Ratio convergence: {ratios[-5:]}")
print(f"Golden ratio ≈ 1.618")
```

---

## ✅ Palindrome Detection

### String Palindromes

```python
# Basic palindrome check
def is_palindrome(text):
    """Check if text is a palindrome"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("Madam"))          # True
print(is_palindrome("racecar"))        # True
print(is_palindrome("Hello"))          # False
print(is_palindrome("A man a plan a canal Panama"))  # True

# Case-sensitive with punctuation
def is_palindrome_strict(text):
    """Palindrome check without modifications"""
    return text == text[::-1]

print(is_palindrome_strict("madam"))   # True
print(is_palindrome_strict("Madam"))   # False

# Alphanumeric only
def is_palindrome_alphanum(text):
    """Check palindrome considering only alphanumeric"""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome_alphanum("A man, a plan, a canal: Panama"))  # True
```

### Bioinformatics Applications

```python
# Check for palindromic sequences (restriction sites)
def is_palindromic_site(sequence):
    """Check if sequence is palindromic (complement reverse)"""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    sequence = sequence.upper()
    reverse_comp = ''.join(complement.get(base, 'N') for base in sequence[::-1])
    
    return sequence == reverse_comp

# EcoRI recognition site
print(is_palindromic_site("GAATTC"))  # True
print(is_palindromic_site("ATCGAT"))  # False

# Find palindromic restriction sites in sequence
def find_palindromic_sites(sequence, min_length=4, max_length=8):
    """Find palindromic restriction sites"""
    sites = []
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    for length in range(min_length, max_length + 1):
        for i in range(len(sequence) - length + 1):
            subseq = sequence[i:i+length]
            reverse_comp = ''.join(complement.get(base, 'N') for base in subseq[::-1])
            
            if subseq == reverse_comp:
                sites.append({'position': i, 'sequence': subseq})
    
    return sites

dna = "ATCGGAATTCCGAT"
sites = find_palindromic_sites(dna)
for site in sites:
    print(f"Position {site['position']}: {site['sequence']}")
```

---

## ✅ Word Counting and Frequency

### Basic Counting

```python
# Count words
sentence = "Python makes coding simple and powerful and elegant"
words = sentence.split()
print(f"Word count: {len(words)}")

# Word frequency (dictionary)
text = "apple banana apple orange banana apple"
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)
# {'apple': 3, 'banana': 2, 'orange': 1}

# Using Counter (collections module)
from collections import Counter

freq = Counter(words)
print(freq)
print(f"Most common: {freq.most_common(2)}")

# Character frequency
text = "hello world"
char_freq = Counter(text)
print(char_freq)
```

### Bioinformatics Examples

```python
# Nucleotide frequency
def nucleotide_frequency(sequence):
    """Calculate nucleotide frequencies"""
    sequence = sequence.upper()
    freq = {}
    for base in sequence:
        freq[base] = freq.get(base, 0) + 1
    return freq

dna = "ATCGATCGATCGATCG"
freq = nucleotide_frequency(dna)
print(f"Nucleotide frequencies: {freq}")

# Codon usage
def codon_usage(sequence):
    """Calculate codon usage frequency"""
    codons = [sequence[i:i+3] for i in range(0, len(sequence)-2, 3)]
    return Counter(codons)

mrna = "AUGUCGGCUAAAAUGCCCGGGAUG"
usage = codon_usage(mrna)
print(f"Codon usage: {usage}")
print(f"Most common: {usage.most_common(3)}")

# K-mer frequency
def kmer_frequency(sequence, k):
    """Calculate k-mer frequencies"""
    kmers = [sequence[i:i+k] for i in range(len(sequence) - k + 1)]
    return Counter(kmers)

dna = "ATCGATCGATCG"
kmers_3 = kmer_frequency(dna, 3)
print(f"3-mer frequencies: {kmers_3}")
```

---

## ✅ Duplicate Detection

### Finding Duplicates

```python
# Find duplicates in list
nums = [1, 2, 3, 2, 4, 5, 1, 6, 7, 1]

# Method 1: Using set
duplicates = [x for x in set(nums) if nums.count(x) > 1]
print(f"Duplicates: {duplicates}")

# Method 2: Using Counter
from collections import Counter
count = Counter(nums)
duplicates = [item for item, freq in count.items() if freq > 1]
print(f"Duplicates: {duplicates}")

# Method 3: Track seen items
def find_duplicates(items):
    """Find all duplicate items"""
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

print(find_duplicates(nums))

# Find first duplicate
def find_first_duplicate(items):
    """Find first duplicate"""
    seen = set()
    for item in items:
        if item in seen:
            return item
        seen.add(item)
    return None

print(f"First duplicate: {find_first_duplicate(nums)}")
```

### Bioinformatics Examples

```python
# Find duplicate sequences
sequences = ["ATCG", "GCTA", "ATCG", "TAGC", "GCTA", "ATCG"]
duplicates = [seq for seq in set(sequences) if sequences.count(seq) > 1]
print(f"Duplicate sequences: {duplicates}")

# Find duplicate gene IDs
gene_ids = ["BRCA1", "TP53", "BRCA1", "EGFR", "TP53", "KRAS"]
duplicate_genes = find_duplicates(gene_ids)
print(f"Duplicate genes: {duplicate_genes}")

# Detect repeated motifs
def find_repeated_motifs(sequence, motif_length=4):
    """Find repeated motifs of given length"""
    motifs = [sequence[i:i+motif_length] 
              for i in range(len(sequence) - motif_length + 1)]
    counts = Counter(motifs)
    repeated = {motif: count for motif, count in counts.items() if count > 1}
    return repeated

dna = "ATCGATCGATCGATCG"
repeated = find_repeated_motifs(dna, 4)
print(f"Repeated 4-mers: {repeated}")
```

---

## ✅ List Comprehensions

### Powerful One-Liners

```python
# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# With condition
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# With if-else
parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(f"Parity: {parity}")

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Matrix: {matrix}")

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Flattened: {flat}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares dict: {squares_dict}")

# Set comprehension
unique_squares = {x**2 for x in [1, -1, 2, -2, 3, -3]}
print(f"Unique squares: {unique_squares}")
```

### Bioinformatics Examples

```python
# Convert sequences to uppercase
sequences = ["atcg", "gcta", "tagc"]
upper_seqs = [seq.upper() for seq in sequences]
print(upper_seqs)

# Filter by length
valid_seqs = [seq for seq in sequences if len(seq) >= 4]
print(valid_seqs)

# Calculate GC content for all sequences
gc_contents = [(seq.count('g') + seq.count('c')) / len(seq) * 100 
               for seq in sequences]
print(f"GC contents: {[f'{gc:.1f}%' for gc in gc_contents]}")

# Extract codons
mrna = "AUGUCGGCUAAA"
codons = [mrna[i:i+3] for i in range(0, len(mrna)-2, 3)]
print(f"Codons: {codons}")

# Get complement
sequence = "ATCG"
complement = ''.join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[base] 
                      for base in sequence])
print(f"Complement: {complement}")

# Quality filtering
reads = ["ATCG", "GCTA", "TAGC", "CGAT"]
qualities = [35, 28, 40, 25]
high_quality = [read for read, qual in zip(reads, qualities) if qual >= 30]
print(f"High quality: {high_quality}")

# Create sequence dictionary
seq_dict = {f"seq_{i}": seq for i, seq in enumerate(sequences, 1)}
print(seq_dict)
```

---

## 📝 Practice Tasks (Day 12)

### Basic Exercises

1. **Digit Sum**: Write a function that calculates the sum of digits of a number.

2. **Prime Generator**: Create a function to generate the first N prime numbers.

3. **Palindrome Checker**: Write a function to check if a string is a palindrome (ignore case and spaces).

4. **Vowel Counter**: Create a function to count vowels in a sentence.

5. **Cube List**: Generate a list of cubes for numbers 1-10 using list comprehension.

### Intermediate Challenges

6. **Second Largest**: Write a function to find the second largest number in a list.

7. **Anagram Detector**: Create a function that checks if two strings are anagrams.

8. **Remove Duplicates**: Write a function that removes duplicates from a list while preserving order.

9. **Merge Sorted Lists**: Implement a function that merges two sorted lists into one sorted list.

10. **Nucleotide Counter**: Create a comprehensive nucleotide counter that also calculates percentages.

### Advanced Challenges

11. **Pattern Finder**: Write a function that finds all occurrences of a pattern in a sequence using list comprehension.

12. **Codon Table**: Create a dictionary of all 64 codons and their amino acids using dictionary comprehension.

13. **Sequence Processor**: Build a function that processes multiple sequences with various operations (reverse, complement, translate) using comprehensions.

14. **K-mer Generator**: Write a function that generates all k-mers of specified length from multiple sequences.

15. **Optimization Challenge**: Take any of the previous functions and optimize it using comprehensions, built-ins, or alternative algorithms.

---

## 💡 Key Takeaways

✓ Tuple unpacking enables elegant variable swapping  
✓ `min()` and `max()` accept custom key functions  
✓ List comprehensions create new lists concisely  
✓ Dictionary comprehensions build dictionaries efficiently  
✓ `Counter` from collections simplifies frequency counting  
✓ Generator expressions save memory for large datasets  
✓ Set operations efficiently find duplicates  
✓ Built-in functions (`sum`, `len`, `all`, `any`) are optimized  
✓ String methods provide powerful text processing  
✓ Leverage Python's built-ins before writing custom solutions  
✓ Comprehensions are faster than equivalent loops  
✓ Choose readability over cleverness when code is complex  

**Next**: Advanced function concepts (scope, decorators, closures)

---

## 📚 Additional Resources

For deeper understanding of specific concepts:

| Topic | Link |
|-------|------|
| Range Function | [utilities/1_range_function_in_python.md](./utilities/1_range_function_in_python.md) |
| Join Function | [utilities/2_join_in_python.md](./utilities/2_join_in_python.md) |
| Escape Sequences | [utilities/3_escape_sequences.md](./utilities/3_escape_sequences.md) |
| F-String Braces | [utilities/4_Escaping Braces in f-Strings.md](./utilities/4_Escaping%20Braces%20in%20f-Strings.md) |
| Naming Conventions | [utilities/5_python_identifier_naming_rules_and_conventions.md](./utilities/5_python_identifier_naming_rules_and_conventions.md) |



