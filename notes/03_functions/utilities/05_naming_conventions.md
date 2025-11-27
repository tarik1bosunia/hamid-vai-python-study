# Python Identifier Naming Rules & Conventions

## 📝 Writing Clean, Readable Code

Following naming conventions makes code professional, readable, and maintainable - essential for collaborative bioinformatics projects.

---

## 🧩 Basic Rules (Required)

### Must Follow

1. **Start with letter or underscore**: `a`, `_var`, `gene_name`
2. **Contain only**: letters, digits, underscores
3. **Case sensitive**: `Gene` ≠ `gene`
4. **Cannot use keywords**: `class`, `if`, `for`, etc.

```python
# ✅ Valid
gene_name = "BRCA1"
sequence1 = "ATCG"
_private = 42
CONSTANT = 100

# ❌ Invalid
# 1gene = "BRCA1"    # Starts with digit
# gene-name = "TP53" # Contains hyphen
# class = "MyClass"  # Reserved keyword
```

---

## 🎨 Naming Conventions (PEP 8)

### Variables & Functions: `snake_case`

```python
# Variables
sequence_length = 100
gc_content = 45.5
max_quality_score = 40

# Functions
def calculate_gc_content(sequence):
    pass

def find_open_reading_frames(dna, min_length=30):
    pass
```

### Constants: `UPPER_SNAKE_CASE`

```python
# Module-level constants
GENETIC_CODE = {...}
DEFAULT_QUALITY_THRESHOLD = 30
MAX_SEQUENCE_LENGTH = 10000
NUCLEOTIDES = {'A', 'T', 'C', 'G'}
```

### Classes: `PascalCase` (CapWords)

```python
class DNASequence:
    pass

class FastaParser:
    pass

class QualityFilter:
    pass

class GeneAnnotation:
    pass
```

### Private: Prefix with `_`

```python
# Private by convention (internal use)
_cache = {}
_internal_counter = 0

class Sequence:
    def __init__(self):
        self._sequence = ""  # Private attribute
    
    def _validate(self):  # Private method
        pass
```

### Double Underscore: Name Mangling

```python
class Gene:
    def __init__(self):
        self.__private = "internal"  # Mangled to _Gene__private
```

---

## 🧬 Bioinformatics Examples

### Good Naming

```python
# ✅ Clear, descriptive
def calculate_gc_content(dna_sequence):
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_length = len(dna_sequence)
    gc_percentage = (g_count + c_count) / total_length * 100
    return gc_percentage

# ✅ Constants
CODON_TABLE = {...}
START_CODON = 'ATG'
STOP_CODONS = {'TAA', 'TAG', 'TGA'}

# ✅ Classes
class FastaRecord:
    pass

class SequenceAlignment:
    pass
```

### Bad Naming

```python
# ❌ Too short, unclear
def gc(s):
    g = s.count('G')
    c = s.count('C')
    return (g + c) / len(s) * 100

# ❌ Inconsistent
def CalculateGCcontent(DNAseq):  # Mixed styles
    pass

# ❌ Not descriptive
def process(data):  # What does it process?
    pass
```

---

## 💡 Best Practices

### Be Descriptive

```python
# ❌ Unclear
s = "ATCG"
l = len(s)
r = calculate(s)

# ✅ Clear
dna_sequence = "ATCG"
sequence_length = len(dna_sequence)
gc_percentage = calculate_gc_content(dna_sequence)
```

### Use Domain Terms

```python
# ✅ Bioinformatics terminology
codon = sequence[i:i+3]
reading_frame = 0
open_reading_frame = find_orf(sequence)
transcript_id = "NM_007294"
chromosome = "chr17"
```

### Avoid Abbreviations (Unless Standard)

```python
# ✅ Standard abbreviations OK
gc_content = 45.5
dna_sequence = "ATCG"
rna_seq = "AUCG"
pcr_primers = ["ATCG", "GCTA"]

# ❌ Non-standard abbreviations
seq_len = 100  # Use sequence_length
qual_scr = 30  # Use quality_score
```

---

## 📋 Quick Reference

| Type | Convention | Example |
|------|-----------|---------|
| Variable | `snake_case` | `gene_name` |
| Function | `snake_case` | `calculate_gc()` |
| Constant | `UPPER_CASE` | `MAX_LENGTH` |
| Class | `PascalCase` | `DNASequence` |
| Private | `_leading` | `_internal` |
| Module | `lowercase` | `sequences.py` |

---

## 💡 Key Takeaways

✓ Use `snake_case` for variables and functions  
✓ Use `PascalCase` for classes  
✓ Use `UPPER_CASE` for constants  
✓ Prefix private members with `_`  
✓ Be descriptive over brief  
✓ Use domain-specific terminology  
✓ Stay consistent throughout project  
✓ Follow PEP 8 style guide
