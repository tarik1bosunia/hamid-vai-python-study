# Python `range()` Function - Complete Guide

## 🔢 Generate Sequences Efficiently

The `range()` function generates sequences of numbers - essential for loops, creating indices, and generating coordinate ranges for sequence analysis.

---

## 🧩 Basic Syntax

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, increment by step
```

### Simple Examples

```python
# Single argument - from 0 to n-1
for i in range(5):
    print(i, end=' ')  # 0 1 2 3 4

# Two arguments - from start to stop-1
for i in range(2, 6):
    print(i, end=' ')  # 2 3 4 5

# Three arguments - with step
for i in range(0, 10, 2):
    print(i, end=' ')  # 0 2 4 6 8

# Negative step - countdown
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
```

---

## 🧬 Bioinformatics Applications

### Example 1: Iterating Sequence Positions

```python
sequence = "ATCGATCGATCG"

# Access each position
for i in range(len(sequence)):
    print(f"Position {i}: {sequence[i]}")

# Process codons (every 3 bases)
for i in range(0, len(sequence), 3):
    codon = sequence[i:i+3]
    print(f"Codon at {i}: {codon}")
```

### Example 2: Sliding Window Analysis

```python
def sliding_window(sequence, window_size=3):
    """Generate sliding windows over sequence"""
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        yield i, window

# Example
dna = "ATCGATCG"
for pos, window in sliding_window(dna, 3):
    print(f"Position {pos}: {window}")
```

### Example 3: Six Reading Frames

```python
def get_reading_frames(sequence):
    """Get all 6 reading frames"""
    # Forward frames
    for frame in range(3):
        print(f"Frame +{frame+1}: {sequence[frame::3]}")
    
    # Reverse complement frames
    rc = reverse_complement(sequence)
    for frame in range(3):
        print(f"Frame -{frame+1}: {rc[frame::3]}")

def reverse_complement(seq):
    complement = str.maketrans('ATCG', 'TAGC')
    return seq.translate(complement)[::-1]
```

### Example 4: Generate Coordinates

```python
# Generate chromosome coordinates
chromosome = "chr1"
start = 1000
end = 2000

for position in range(start, end + 1, 100):
    print(f"{chromosome}:{position}")
```

---

## 🔧 Advanced Usage

### Convert to List

```python
# range() returns a range object, not a list
nums = range(5)
print(type(nums))  # <class 'range'>

# Convert to list
num_list = list(range(5))
print(num_list)  # [0, 1, 2, 3, 4]

# Generate list of positions
positions = list(range(0, 100, 10))
print(positions)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```

### Reverse Ranges

```python
# Countdown
for i in range(10, 0, -1):
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1

# Reverse iteration
for i in range(len(sequence)-1, -1, -1):
    print(sequence[i], end='')  # Prints sequence backwards
```

### Enumerate Alternative

```python
sequence = "ATCG"

# Using range
for i in range(len(sequence)):
    print(f"{i}: {sequence[i]}")

# Better: Use enumerate
for i, base in enumerate(sequence):
    print(f"{i}: {base}")
```

---

## 💡 Key Takeaways

✓ `range(n)` generates 0 to n-1  
✓ `range(start, stop)` generates start to stop-1  
✓ `range(start, stop, step)` uses custom increment  
✓ Stop value is **exclusive** (not included)  
✓ Negative step creates reverse sequence  
✓ Returns range object, not list (memory efficient)  
✓ Perfect for indexing sequences  
✓ Use `enumerate()` when you need both index and value
