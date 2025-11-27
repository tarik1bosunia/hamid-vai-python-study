# LRU Cache - Memoization for Performance

## ⚡ Speed Up Recursive & Repetitive Functions

`@lru_cache` is a powerful decorator that **caches function results**, dramatically improving performance for recursive algorithms and repeated calculations - essential for computationally expensive bioinformatics tasks.

**LRU** = **Least Recently Used** - automatically discards oldest cached results when memory limit reached.

---

## 🧩 The Problem: Slow Recursion

### Without Cache - Exponential Time

```python
def fibonacci(n):
    """Naive recursive Fibonacci - very slow!"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Fast for small n
print(fibonacci(10))  # 55 (quick)

# Extremely slow for larger n
print(fibonacci(35))  # Takes seconds! 😰
print(fibonacci(40))  # Takes minutes! 😱
```

**Why so slow?** Massive redundant calculations:

```
fibonacci(5)
├─ fibonacci(4)
│  ├─ fibonacci(3)
│  │  ├─ fibonacci(2)  ← calculated
│  │  │  ├─ fibonacci(1)
│  │  │  └─ fibonacci(0)
│  │  └─ fibonacci(1)
│  └─ fibonacci(2)     ← recalculated!
│     ├─ fibonacci(1)
│     └─ fibonacci(0)
└─ fibonacci(3)        ← recalculated!
   ├─ fibonacci(2)     ← recalculated!
   │  ├─ fibonacci(1)
   │  └─ fibonacci(0)
   └─ fibonacci(1)
```

Time complexity: **O(2ⁿ)** - exponential growth!

---

## ✅ The Solution: Add @lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # Unlimited cache
def fibonacci(n):
    """Cached Fibonacci - blazing fast!"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Now extremely fast even for large n
print(fibonacci(10))   # Instant
print(fibonacci(100))  # Instant! ⚡
print(fibonacci(500))  # Still instant! ⚡
```

Time complexity: **O(n)** - linear! Each value calculated once.

---

## 🧬 Bioinformatics Applications

### Example 1: Longest Common Subsequence (LCS)

Used for sequence alignment, finding conserved regions.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def lcs_length(seq1, seq2, i, j):
    """
    Find longest common subsequence length
    
    Without cache: O(2^(m+n))
    With cache: O(m*n)
    """
    # Base case
    if i == 0 or j == 0:
        return 0
    
    # Match
    if seq1[i-1] == seq2[j-1]:
        return 1 + lcs_length(seq1, seq2, i-1, j-1)
    
    # No match - try both options
    return max(
        lcs_length(seq1, seq2, i-1, j),
        lcs_length(seq1, seq2, i, j-1)
    )

# Example: Find LCS between two DNA sequences
seq1 = "ATCGATCG"
seq2 = "AGCTAGCT"

length = lcs_length(seq1, seq2, len(seq1), len(seq2))
print(f"LCS length: {length}")

# Check cache statistics
print(lcs_length.cache_info())
```

### Example 2: Edit Distance (Levenshtein)

Measures similarity between sequences - used in sequence alignment.

```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def edit_distance(seq1, seq2):
    """
    Calculate minimum edits to transform seq1 to seq2
    
    Operations: insert, delete, substitute
    """
    # Base cases
    if len(seq1) == 0:
        return len(seq2)
    if len(seq2) == 0:
        return len(seq1)
    
    # Last characters match - no edit needed
    if seq1[-1] == seq2[-1]:
        return edit_distance(seq1[:-1], seq2[:-1])
    
    # Try all three operations, pick minimum
    return 1 + min(
        edit_distance(seq1[:-1], seq2),      # Delete from seq1
        edit_distance(seq1, seq2[:-1]),      # Insert to seq1
        edit_distance(seq1[:-1], seq2[:-1])  # Substitute
    )

# Example
s1 = "ATCGATCG"
s2 = "AGCTAGCT"

distance = edit_distance(s1, s2)
print(f"Edit distance: {distance}")
print(f"Cache: {edit_distance.cache_info()}")
```

### Example 3: Codon Optimization Score

```python
from functools import lru_cache

# Codon usage frequency table (example values)
CODON_FREQ = {
    'ATG': 1.00, 'TAA': 0.30, 'TAG': 0.24, 'TGA': 0.46,
    'TTT': 0.45, 'TTC': 0.55, 'TTA': 0.07, 'TTG': 0.13,
    'GCT': 0.26, 'GCC': 0.40, 'GCA': 0.23, 'GCG': 0.11
    # ... (simplified)
}

@lru_cache(maxsize=128)
def codon_score(codon):
    """Get usage frequency score for codon"""
    return CODON_FREQ.get(codon, 0.0)

@lru_cache(maxsize=1024)
def sequence_optimization_score(sequence):
    """
    Calculate optimization score for entire sequence
    Cached to avoid recalculating for repeated sequences
    """
    if len(sequence) < 3:
        return 0.0
    
    scores = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        scores.append(codon_score(codon))
    
    return sum(scores) / len(scores) if scores else 0.0

# Test
sequences = ["ATGTTTTAG", "ATGTTCTAG", "ATGTTTTAG"]  # Third is duplicate

for seq in sequences:
    score = sequence_optimization_score(seq)
    print(f"{seq}: {score:.3f}")

print(f"\nCache stats: {sequence_optimization_score.cache_info()}")
```

### Example 4: GC Content Windows

```python
from functools import lru_cache

@lru_cache(maxsize=512)
def gc_content(sequence):
    """Calculate GC% for a sequence (cached)"""
    if len(sequence) == 0:
        return 0.0
    g = sequence.count('G')
    c = sequence.count('C')
    return (g + c) / len(sequence) * 100

def analyze_sliding_window(sequence, window_size=100):
    """
    Analyze GC content in sliding windows
    Repeated windows benefit from cache
    """
    results = []
    
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        gc = gc_content(window)  # Cached!
        results.append((i, gc))
    
    return results

# Test with sequence containing repeated patterns
dna = "ATCGATCG" * 50  # 400 bp with repeating pattern
windows = analyze_sliding_window(dna, window_size=8)

print(f"Analyzed {len(windows)} windows")
print(f"Cache stats: {gc_content.cache_info()}")
print(f"Cache hit rate: {gc_content.cache_info().hits / (gc_content.cache_info().hits + gc_content.cache_info().misses):.2%}")
```

---

## 🔧 Cache Configuration

### maxsize Parameter

```python
from functools import lru_cache

# Unlimited cache (uses more memory)
@lru_cache(maxsize=None)
def func1(n):
    return n ** 2

# Limited cache (saves memory, LRU eviction)
@lru_cache(maxsize=128)  # Keep last 128 results
def func2(n):
    return n ** 2

# Minimal cache
@lru_cache(maxsize=1)  # Only cache last result
def func3(n):
    return n ** 2
```

### Cache Statistics

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(x):
    return x ** 2

# Use function
for i in range(10):
    expensive_function(i % 5)  # Only 5 unique values

# Get statistics
info = expensive_function.cache_info()
print(f"Hits: {info.hits}")          # Times cache was used
print(f"Misses: {info.misses}")      # Times function was called
print(f"Cache size: {info.currsize}")  # Current cache size
print(f"Max size: {info.maxsize}")    # Maximum cache size

# Hit rate (efficiency)
hit_rate = info.hits / (info.hits + info.misses)
print(f"Hit rate: {hit_rate:.1%}")
```

### Clearing Cache

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_sequence_info(seq_id):
    # Expensive database lookup
    return {"id": seq_id, "length": 1000}

# Use cache
info1 = get_sequence_info("seq1")

# Clear cache (e.g., when data updated)
get_sequence_info.cache_clear()

# Cache is empty now
info2 = get_sequence_info("seq1")  # Will recalculate
```

---

## ⚠️ Important Limitations

### 1. Arguments Must Be Hashable

```python
from functools import lru_cache

# ✅ Works - hashable arguments
@lru_cache
def process_sequence(sequence: str, min_length: int):
    return len(sequence) >= min_length

# ❌ Fails - list is not hashable
@lru_cache
def process_list(items: list):  # Error!
    return sum(items)

# ✅ Solution - convert to tuple
@lru_cache
def process_tuple(items: tuple):  # Works!
    return sum(items)

# Usage
result = process_tuple(tuple([1, 2, 3]))
```

### 2. Memory Usage

```python
# Large cache can use significant memory
@lru_cache(maxsize=None)  # Unlimited - watch memory!
def cache_sequences(sequence):
    return sequence.upper()

# Better - limit cache size
@lru_cache(maxsize=1000)  # Reasonable limit
def cache_sequences_limited(sequence):
    return sequence.upper()
```

### 3. Not Thread-Safe for Mutation

```python
# Don't modify cached results!
from functools import lru_cache

@lru_cache
def get_list():
    return [1, 2, 3]

lst1 = get_list()
lst1.append(4)  # ❌ Modifies cached object!

lst2 = get_list()
print(lst2)  # [1, 2, 3, 4] - unexpected!
```

---

## 📝 Practice Tasks

### Basic
1. Add `@lru_cache` to recursive Fibonacci
2. Cache GC content calculation
3. Compare performance with/without cache

### Intermediate
4. Implement cached edit distance
5. Build cached codon usage calculator
6. Create sliding window analyzer with caching

### Advanced
7. Implement LCS with cache statistics reporting
8. Build cached sequence alignment scorer
9. Create cache-aware batch processor

---

## 💡 Key Takeaways

✓ `@lru_cache` **dramatically speeds up** recursive functions  
✓ Converts **O(2ⁿ)** to **O(n)** for many algorithms  
✓ Essential for **dynamic programming** problems  
✓ Arguments must be **hashable** (strings, numbers, tuples)  
✓ Use `maxsize=None` for unlimited cache  
✓ Use `maxsize=128` (default) for memory efficiency  
✓ Call `.cache_info()` to see hit/miss statistics  
✓ Call `.cache_clear()` to reset cache  
✓ Perfect for: sequence alignment, edit distance, recursion  
✓ Watch memory usage with large caches  
✓ Don't modify cached return values  
✓ Thread-safe for reading, not mutation
