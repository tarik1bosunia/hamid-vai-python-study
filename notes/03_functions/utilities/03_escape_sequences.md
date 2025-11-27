# Escape Sequences in Python

## 🔤 Special Characters in Strings

Escape sequences represent special characters using backslash `\` notation - essential for newlines, tabs, quotes, and file paths.

---

## 🧩 Common Escape Sequences

| Sequence | Meaning | Example |
|----------|---------|---------|
| `\n` | Newline | Line break |
| `\t` | Tab | Horizontal tab |
| `\\` | Backslash | Literal `\` |
| `\'` | Single quote | Inside `'...'` |
| `\"` | Double quote | Inside `"..."` |
| `\r` | Carriage return | Windows line ending |
| `\b` | Backspace | Delete previous |

---

## 🧬 Bioinformatics Examples

### Example 1: FASTA Formatting

```python
# Multi-line FASTA
fasta = ">seq1\nATCGATCG\nGCTAGCTA"
print(fasta)
# >seq1
# ATCGATCG
# GCTAGCTA

# With tabs
header = "ID\tSequence\tLength"
data = "seq1\tATCG\t4"
print(header)
print(data)
```

### Example 2: File Paths (Windows)

```python
# ❌ Wrong: Single backslash
# path = "C:\data\sequences.fasta"  # Error!

# ✅ Correct: Escape backslash
path = "C:\\data\\sequences.fasta"
print(path)  # C:\data\sequences.fasta

# ✅ Better: Raw string
path = r"C:\data\sequences.fasta"

# ✅ Best: Forward slash (works everywhere)
path = "C:/data/sequences.fasta"
```

### Example 3: Multi-line Strings

```python
# Using \n
sequence = "ATCG\nGCTA\nTAGC"

# Triple quotes (better for multi-line)
sequence = """ATCG
GCTA
TAGC"""

# FASTA with triple quotes
fasta = """>seq1 Homo sapiens
ATCGATCGATCG
GCTAGCTAGCTA
TAGCTAGCTAGC"""
```

---

## 🔧 Raw Strings

Use `r` prefix to treat backslashes literally:

```python
# Regular string - escapes processed
text = "C:\new\data"  # \n becomes newline!
print(text)  # C:
             # ew\data

# Raw string - backslashes literal
text = r"C:\new\data"
print(text)  # C:\new\data

# Perfect for regex patterns
import re
pattern = r"\d+"  # Literal \d, not escape
```

---

## 💡 Key Takeaways

✓ `\n` creates new line  
✓ `\t` creates tab  
✓ `\\` creates literal backslash  
✓ Use raw strings `r"..."` for file paths  
✓ Triple quotes for multi-line text  
✓ Forward slash `/` works on all OS
