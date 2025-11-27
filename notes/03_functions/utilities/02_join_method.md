# Python `join()` Method - String Concatenation

## 🔗 Efficiently Combine Strings

The `join()` method concatenates strings efficiently - crucial for building sequences, formatting output, and creating file content.

---

## 🧩 Basic Syntax

```python
separator.join(iterable)
```

### Simple Examples

```python
# Join list of strings
bases = ['A', 'T', 'C', 'G']
sequence = ''.join(bases)
print(sequence)  # ATCG

# Join with separator
codons = ['ATG', 'GCC', 'TAG']
result = '-'.join(codons)
print(result)  # ATG-GCC-TAG

# Join with space
words = ['Homo', 'sapiens']
species = ' '.join(words)
print(species)  # Homo sapiens
```

---

## 🧬 Bioinformatics Applications

### Example 1: Build Sequences

```python
# Assemble sequence from fragments
fragments = ['ATCG', 'GCTA', 'TAGC']
full_sequence = ''.join(fragments)
print(full_sequence)  # ATCGGCTATAGC

# Build from nucleotides
nucleotides = ['A', 'T', 'C', 'G', 'A', 'T']
dna = ''.join(nucleotides)
print(dna)  # ATCGAT
```

### Example 2: Format FASTA Output

```python
def format_fasta(seq_id, sequence, line_length=60):
    """Format sequence as FASTA with line breaks"""
    lines = [f">{seq_id}"]
    
    for i in range(0, len(sequence), line_length):
        lines.append(sequence[i:i+line_length])
    
    return '\n'.join(lines)

# Example
fasta = format_fasta("seq1", "ATCGATCG" * 10)
print(fasta)
```

### Example 3: Build Quality String

```python
# Create FASTQ quality string
qualities = ['I'] * 50  # High quality
quality_string = ''.join(qualities)
print(quality_string)  # IIIIII...

# Mixed qualities
quality_scores = ['I', 'I', 'H', 'G', 'F', 'I', 'I']
quality_line = ''.join(quality_scores)
```

### Example 4: CSV Generation

```python
# Generate CSV from sequence data
def sequences_to_csv(sequences):
    """Convert sequence data to CSV"""
    rows = ['ID,Sequence,Length,GC%']
    
    for seq_id, seq in sequences.items():
        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
        row = ','.join([seq_id, seq, str(len(seq)), f"{gc:.2f}"])
        rows.append(row)
    
    return '\n'.join(rows)

# Example
data = {
    'seq1': 'ATCGATCG',
    'seq2': 'GCGCGCGC'
}
csv = sequences_to_csv(data)
print(csv)
```

---

## 🔧 Advanced Patterns

### Join with Different Separators

```python
# Tab-separated (TSV)
fields = ['chr1', '1000', '2000', 'gene1']
tsv_line = '\t'.join(fields)

# Comma-separated (CSV)
csv_line = ','.join(fields)

# Pipe-separated
pipe_line = '|'.join(fields)

# Custom separator
custom = ' -> '.join(['start', 'middle', 'end'])
```

### Join Numbers (Convert First)

```python
# Must convert to strings first
numbers = [1, 2, 3, 4, 5]
# result = ','.join(numbers)  # ❌ Error!

# ✅ Correct
result = ','.join(str(n) for n in numbers)
print(result)  # 1,2,3,4,5

# Or map
result = ','.join(map(str, numbers))
```

### Performance Comparison

```python
# ❌ Slow: String concatenation
sequence = ''
for base in bases:
    sequence += base  # Creates new string each time

# ✅ Fast: join()
sequence = ''.join(bases)  # Single operation
```

---

## 💡 Key Takeaways

✓ `separator.join(iterable)` concatenates strings  
✓ Empty string `''` joins without separator  
✓ Much **faster** than `+=` for many strings  
✓ Works with any iterable of strings  
✓ Must convert non-strings first  
✓ Perfect for building sequences, CSV, TSV  
✓ Use `'\n'.join()` for multi-line text
