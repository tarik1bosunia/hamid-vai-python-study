# Python Variable Scope (LEGB Rule)

## 🎯 Understanding Scope for Bioinformatics Functions

Variable scope determines where variables can be accessed and modified. Mastering scope is essential for building complex bioinformatics pipelines with nested functions, configuration management, and modular code.

---

## 🧩 The LEGB Rule

Python resolves variable names using **LEGB** order:

| Level | Scope | Description | Example Use Case |
|-------|-------|-------------|------------------|
| **L**ocal | Function | Inside current function | Loop counters, temporary calculations |
| **E**nclosing | Nested | Parent function (closures) | Configuration builders, callbacks |
| **G**lobal | Module | Module-level variables | Constants, shared state |
| **B**uilt-in | Python | Built-in functions/vars | `len`, `print`, `str` |

---

## 🔹 Local Scope

Variables defined inside functions are **local** - they exist only during function execution.

```python
def calculate_gc_content(sequence):
    # All these are LOCAL variables
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    gc_percent = (g_count + c_count) / total * 100
    
    return gc_percent

result = calculate_gc_content("ATCGATCG")
print(f"GC%: {result}")

# print(g_count)  # ❌ Error: g_count doesn't exist here
```

### Bioinformatics Example

```python
def find_orfs(sequence, min_length=30):
    """Find ORFs - all variables are local"""
    orfs = []  # Local list
    start_codon = 'ATG'  # Local constant
    stop_codons = {'TAA', 'TAG', 'TGA'}  # Local set
    
    i = 0
    while i < len(sequence) - 2:
        if sequence[i:i+3] == start_codon:
            # j is also local to this function
            j = i + 3
            while j < len(sequence) - 2:
                if sequence[j:j+3] in stop_codons:
                    if j + 3 - i >= min_length:
                        orfs.append((i, j + 3))
                    i = j + 3
                    break
                j += 3
            else:
                i += 3
        else:
            i += 3
    
    return orfs
    # After return, all local variables disappear
```

---

## 🔹 Global Scope

Global variables exist at module level and persist throughout program execution.

```python
# Global constants (uppercase by convention)
GENETIC_CODE = {
    'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*',
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L'
}

MAX_SEQUENCE_LENGTH = 100000
DEFAULT_ORGANISM = "Homo sapiens"

# Global counter
sequences_processed = 0

def translate_codon(codon):
    """Access global constant"""
    return GENETIC_CODE.get(codon, 'X')

def process_sequence(sequence):
    """Modify global variable"""
    global sequences_processed  # Must declare to modify
    
    # Process sequence...
    sequences_processed += 1
    
    return f"Processed {sequences_processed} sequences"

# Use functions
print(translate_codon('ATG'))  # M
print(process_sequence("ATCG"))  # Processed 1 sequences
print(process_sequence("GCTA"))  # Processed 2 sequences
```

### When to Use Global

```python
# ✅ Good: Configuration constants
CODON_TABLE = {...}
DEFAULT_PARAMETERS = {...}

# ✅ Good: Shared cache
_sequence_cache = {}

def get_sequence(seq_id):
    global _sequence_cache
    if seq_id not in _sequence_cache:
        _sequence_cache[seq_id] = fetch_from_database(seq_id)
    return _sequence_cache[seq_id]

# ❌ Bad: Avoid global mutable state when possible
# total_errors = 0  # Hard to track, debug, and test
```

---

## 🔹 Enclosing Scope (Closures)

Variables from outer functions are accessible in nested (inner) functions.

```python
def create_sequence_filter(min_gc, max_gc):
    """Factory function that returns a configured filter"""
    # These are ENCLOSING scope for the inner function
    min_threshold = min_gc
    max_threshold = max_gc
    
    def filter_sequence(sequence):
        """Inner function - can access outer variables"""
        g = sequence.count('G')
        c = sequence.count('C')
        gc_percent = (g + c) / len(sequence) * 100
        
        # Access enclosing scope variables
        return min_threshold <= gc_percent <= max_threshold
    
    return filter_sequence

# Create custom filters
high_gc_filter = create_sequence_filter(60, 100)
low_gc_filter = create_sequence_filter(0, 40)

sequences = ["GCGCGCGC", "ATATATAT", "ATCGATCG"]

print("High GC sequences:")
for seq in sequences:
    if high_gc_filter(seq):
        print(f"  {seq}")

print("Low GC sequences:")
for seq in sequences:
    if low_gc_filter(seq):
        print(f"  {seq}")
```

### Practical Bioinformatics Example

```python
def create_quality_filter(min_quality, min_length):
    """Create a configured FASTQ filter"""
    
    def phred_to_score(char):
        """Convert Phred character to quality score"""
        return ord(char) - 33
    
    def filter_read(sequence, quality):
        """Filter based on enclosing parameters"""
        # Check length
        if len(sequence) < min_length:
            return False
        
        # Check average quality
        scores = [phred_to_score(q) for q in quality]
        avg_quality = sum(scores) / len(scores)
        
        return avg_quality >= min_quality
    
    return filter_read

# Create filter
quality_filter = create_quality_filter(min_quality=30, min_length=50)

# Use filter
reads = [
    ("ATCGATCG" * 10, "IIIIIIII" * 10),  # High quality, long
    ("ATCG", "IIII"),  # High quality, too short
    ("ATCGATCG" * 10, "!!!!!!!!" * 10),  # Low quality, long
]

for seq, qual in reads:
    if quality_filter(seq, qual):
        print(f"PASS: {len(seq)} bp")
    else:
        print(f"FAIL: {len(seq)} bp")
```

---

## 🔹 The `nonlocal` Keyword

Use `nonlocal` to modify variables from enclosing scope.

```python
def create_sequence_counter():
    """Create a stateful counter using closures"""
    count = 0  # Enclosing variable
    
    def add_sequence(sequence):
        nonlocal count  # Allow modification of enclosing variable
        count += 1
        return f"Sequence #{count}: {len(sequence)} bp"
    
    def get_count():
        return count
    
    return add_sequence, get_count

# Use counter
add_seq, get_count = create_sequence_counter()

print(add_seq("ATCG"))     # Sequence #1: 4 bp
print(add_seq("GCTAGC"))   # Sequence #2: 6 bp
print(add_seq("TAGCTA"))   # Sequence #3: 6 bp
print(f"Total: {get_count()}")  # Total: 3
```

### Complex Example: Statistics Accumulator

```python
def create_sequence_analyzer():
    """Stateful sequence analyzer"""
    total_length = 0
    total_gc = 0
    count = 0
    
    def analyze(sequence):
        nonlocal total_length, total_gc, count
        
        count += 1
        total_length += len(sequence)
        
        g = sequence.count('G')
        c = sequence.count('C')
        gc = (g + c) / len(sequence) * 100
        total_gc += gc
        
        return {
            'sequence_num': count,
            'length': len(sequence),
            'gc_percent': gc
        }
    
    def get_stats():
        if count == 0:
            return None
        return {
            'total_sequences': count,
            'average_length': total_length / count,
            'average_gc': total_gc / count
        }
    
    return analyze, get_stats

# Use analyzer
analyze, get_stats = create_sequence_analyzer()

sequences = ["ATCGATCG", "GCGCGCGC", "ATATATAT"]
for seq in sequences:
    result = analyze(seq)
    print(f"Seq {result['sequence_num']}: {result['gc_percent']:.1f}% GC")

stats = get_stats()
print(f"\nOverall: {stats['total_sequences']} sequences, "
      f"avg {stats['average_length']:.1f} bp, "
      f"avg {stats['average_gc']:.1f}% GC")
```

---

## 🔹 Built-in Scope

Python's built-in functions and constants are always accessible.

```python
# Built-in functions
sequence = "ATCGATCG"
print(len(sequence))      # Built-in: len()
print(type(sequence))     # Built-in: type()
print(max(sequence))      # Built-in: max()

# Don't shadow built-ins!
# ❌ Bad:
# len = 10  # Now len() function is gone!

# ✅ Good:
seq_len = 10  # Use different name
```

---

## 📝 Practice Tasks

### Basic
1. Create function with local variables for nucleotide counting
2. Define global genetic code table and use it in translation function
3. Write function that modifies global counter

### Intermediate
4. Create closure that returns configured GC filter
5. Build sequence processor with nonlocal statistics
6. Implement cache using global dictionary

### Advanced
7. Create factory for customized ORF finders
8. Build stateful parser with multiple nested functions
9. Implement decorator using closures

---

## 💡 Key Takeaways

✓ **Local** variables disappear after function ends  
✓ **Global** keyword required to modify global variables  
✓ **Closures** capture enclosing scope variables  
✓ **nonlocal** modifies enclosing scope variables  
✓ Use **UPPERCASE** for global constants  
✓ Avoid global mutable state when possible  
✓ Closures enable factory patterns  
✓ Don't shadow built-in names  
✓ LEGB lookup order: Local → Enclosing → Global → Built-in
