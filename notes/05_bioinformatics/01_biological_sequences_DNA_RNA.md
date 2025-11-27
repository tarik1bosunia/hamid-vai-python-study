# Day 13: Biological Sequences — DNA & RNA as Strings

## 🧬 Understanding Biological Sequences

Biological sequences (DNA, RNA, proteins) are fundamental to bioinformatics. In Python, we represent these sequences as **strings**, which allows us to leverage powerful string manipulation methods for biological analysis.

### Why Sequences as Strings Matter

- DNA and RNA are essentially text - sequences of nucleotides
- Python's string methods map naturally to sequence operations
- Efficient processing of genomic data
- Foundation for more complex bioinformatics tools
- Enables pattern matching and motif finding
- Supports sequence alignment and comparison

---

## 🔹 DNA and RNA Fundamentals

### Nucleotide Composition

**DNA (Deoxyribonucleic Acid)**
- Adenine (A)
- Thymine (T)  
- Cytosine (C)
- Guanine (G)

**RNA (Ribonucleic Acid)**
- Adenine (A)
- Uracil (U) — replaces Thymine
- Cytosine (C)
- Guanine (G)

### Base Pairing Rules

**DNA Base Pairing (Watson-Crick)**
- A (Adenine) pairs with T (Thymine) — 2 hydrogen bonds
- C (Cytosine) pairs with G (Guanine) — 3 hydrogen bonds

**RNA Base Pairing**
- A pairs with U (Uracil)
- C pairs with G

### DNA Structure

```python
# DNA is typically double-stranded
# 5' to 3' direction matters

forward_strand = "5'-ATCGATCG-3'"
# Complement (antiparallel)
reverse_strand = "3'-TAGCTAGC-5'"
```

---

## ✅ Representing Sequences in Python

### Basic Sequence Representation

```python
# DNA sequence
dna = "ATGCGTACGTAGCTAGCTA"
print(f"DNA Sequence: {dna}")
print(f"Length: {len(dna)} base pairs (bp)")

# RNA sequence
rna = "AUGCGUACGUAGCUAGCUA"
print(f"RNA Sequence: {rna}")

# Multi-line sequences (for readability)
long_dna = (
    "ATGCTAGCTAGCTAGCTAGC"
    "TAGCTAGCTAGCTAGCTAGC"
    "ATGCTAGCTAGCTAGCTAG"
)
print(f"Long sequence: {long_dna}")

# Sequence with metadata
sequence_record = {
    'id': 'seq001',
    'description': 'Human BRCA1 gene fragment',
    'sequence': 'ATGCGTACGTAGCTAGCTA',
    'organism': 'Homo sapiens'
}
print(f"ID: {sequence_record['id']}")
print(f"Sequence: {sequence_record['sequence']}")
```

### Case Handling

```python
# Sequences are typically uppercase
dna_mixed = "AtCgAtCg"
dna_upper = dna_mixed.upper()
print(f"Uppercase: {dna_upper}")

# Check if sequence is properly formatted
is_uppercase = dna.isupper()
print(f"Is uppercase: {is_uppercase}")
```

---

## ✅ Counting Nucleotides

### Basic Counting

```python
dna = "ATGCGTACGTAGCTAGCTA"

# Count individual bases
a_count = dna.count('A')
t_count = dna.count('T')
c_count = dna.count('C')
g_count = dna.count('G')

print(f"Adenine (A): {a_count}")
print(f"Thymine (T): {t_count}")
print(f"Cytosine (C): {c_count}")
print(f"Guanine (G): {g_count}")

# Total verification
total = a_count + t_count + c_count + g_count
print(f"Total bases: {total}")
```

### Comprehensive Nucleotide Counter

```python
def count_nucleotides(sequence):
    """Count all nucleotides in a sequence"""
    sequence = sequence.upper()
    counts = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G')
    }
    return counts

dna = "ATGCGTACGTAGCTAGCTA"
counts = count_nucleotides(dna)

print("\nNucleotide Frequencies:")
for base, count in counts.items():
    percent = (count / len(dna)) * 100
    print(f"{base}: {count:3d} ({percent:5.2f}%)")
```

### Using Collections Counter

```python
from collections import Counter

dna = "ATGCGTACGTAGCTAGCTA"
nucleotide_freq = Counter(dna)

print("\nFrequency Analysis:")
for base, count in nucleotide_freq.most_common():
    print(f"{base}: {count}")
```

---

## ✅ GC Content Calculation

### Why GC Content Matters

- **Gene prediction**: Genes often have higher GC content
- **Primer design**: GC content affects melting temperature
- **Species identification**: GC% varies across organisms
- **Genome structure**: CpG islands are GC-rich regions
- **PCR optimization**: Affects reaction conditions

### Basic GC Content

```python
def calculate_gc_content(sequence):
    """Calculate GC content percentage"""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total = len(sequence)
    
    if total == 0:
        return 0.0
    
    gc_percent = ((g_count + c_count) / total) * 100
    return gc_percent

dna = "ATGCGTACGTAGCTAGCTA"
gc = calculate_gc_content(dna)
print(f"GC Content: {gc:.2f}%")

# Classification
if gc > 60:
    print("High GC content")
elif gc > 40:
    print("Medium GC content")
else:
    print("Low GC content")
```

### Advanced GC Analysis

```python
def analyze_gc(sequence):
    """Comprehensive GC analysis"""
    sequence = sequence.upper()
    length = len(sequence)
    
    # Count all bases
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    # AT and GC counts
    at_count = a_count + t_count
    gc_count = g_count + c_count
    
    # Percentages
    at_percent = (at_count / length * 100) if length > 0 else 0
    gc_percent = (gc_count / length * 100) if length > 0 else 0
    
    # GC skew (for strand bias detection)
    gc_skew = ((g_count - c_count) / (g_count + c_count)) if (g_count + c_count) > 0 else 0
    
    print(f"Sequence Length: {length} bp")
    print(f"\nBase Composition:")
    print(f"  AT: {at_count} ({at_percent:.2f}%)")
    print(f"  GC: {gc_count} ({gc_percent:.2f}%)")
    print(f"\nDetailed:")
    print(f"  A: {a_count}  T: {t_count}  G: {g_count}  C: {c_count}")
    print(f"\nGC Skew: {gc_skew:.3f}")
    
    return {
        'length': length,
        'gc_percent': gc_percent,
        'at_percent': at_percent,
        'gc_skew': gc_skew,
        'counts': {'A': a_count, 'T': t_count, 'G': g_count, 'C': c_count}
    }

dna = "ATGCGTACGTAGCTAGCTA"
analysis = analyze_gc(dna)
```

---

## ✅ Transcription: DNA → RNA

### The Transcription Process

In molecular biology, **transcription** is the process of copying DNA into RNA. The key change: **Thymine (T) becomes Uracil (U)**.

### Basic Transcription

```python
def transcribe(dna):
    """Transcribe DNA to RNA"""
    return dna.replace('T', 'U')

dna = "ATGCTAGCTAGC"
rna = transcribe(dna)

print(f"DNA: {dna}")
print(f"RNA: {rna}")
```

### Comprehensive Transcription

```python
def transcribe_dna(dna, direction='sense'):
    """
    Transcribe DNA to RNA
    
    Parameters:
        dna: DNA sequence string
        direction: 'sense' (template) or 'antisense'
    
    Returns:
        RNA sequence
    """
    dna = dna.upper()
    
    # Validate DNA
    valid_bases = set('ATCG')
    if not set(dna).issubset(valid_bases):
        invalid = set(dna) - valid_bases
        raise ValueError(f"Invalid DNA bases: {invalid}")
    
    # Template strand transcription
    rna = dna.replace('T', 'U')
    
    print(f"DNA ({direction}): 5'-{dna}-3'")
    print(f"RNA:            5'-{rna}-3'")
    
    return rna

dna = "ATGCGTACGTAGC"
rna = transcribe_dna(dna)
```

### Transcription with mRNA Features

```python
def transcribe_with_features(dna):
    """Transcribe and identify mRNA features"""
    rna = dna.replace('T', 'U')
    
    # Look for start codon
    has_start = 'AUG' in rna
    
    # Look for stop codons
    stop_codons = ['UAA', 'UAG', 'UGA']
    has_stop = any(codon in rna for codon in stop_codons)
    
    print(f"DNA: {dna}")
    print(f"RNA: {rna}")
    print(f"Start codon (AUG): {'Found' if has_start else 'Not found'}")
    print(f"Stop codon: {'Found' if has_stop else 'Not found'}")
    
    return rna

dna = "ATGTACGATAA"
rna = transcribe_with_features(dna)
```

---

## ✅ Working with Codons

### Understanding Codons

A **codon** is a sequence of three nucleotides that codes for a specific amino acid or stop signal.

```
DNA: ATG CGT ACG TAG CTA GCT
     |   |   |   |   |   |
Codons: 3 bp each
```

### Extracting Codons

```python
def extract_codons(sequence):
    """Extract all complete codons from sequence"""
    codons = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:  # Only complete codons
            codons.append(codon)
    return codons

dna = "ATGCGTACGTAGCTAGCTA"
codons = extract_codons(dna)

print("Codons:")
for i, codon in enumerate(codons, 1):
    print(f"  {i}. {codon}")

# Using list comprehension
codons_comp = [dna[i:i+3] for i in range(0, len(dna), 3) if len(dna[i:i+3]) == 3]
print(f"\nTotal complete codons: {len(codons_comp)}")
```

### Codon Analysis

```python
def analyze_codons(sequence):
    """Comprehensive codon analysis"""
    codons = extract_codons(sequence)
    
    # Count codons
    from collections import Counter
    codon_counts = Counter(codons)
    
    # Identify start and stop
    start_codons = [c for c in codons if c == 'ATG']
    stop_codons = [c for c in codons if c in ['TAA', 'TAG', 'TGA']]
    
    print(f"Total codons: {len(codons)}")
    print(f"Unique codons: {len(codon_counts)}")
    print(f"Start codons (ATG): {len(start_codons)}")
    print(f"Stop codons: {len(stop_codons)}")
    
    if codon_counts:
        most_common = codon_counts.most_common(3)
        print(f"\nMost common codons:")
        for codon, count in most_common:
            print(f"  {codon}: {count}")
    
    return codons, codon_counts

dna = "ATGCGTACGTAGATGCTAGCTATAAGCTA"
codons, counts = analyze_codons(dna)
```

---

## ✅ Complement and Reverse Complement

### Base Complementation

```python
def get_complement(sequence):
    """Get complement of DNA sequence"""
    complement_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    complement = ''
    for base in sequence.upper():
        complement += complement_map.get(base, 'N')
    
    return complement

dna = "ATCG"
comp = get_complement(dna)
print(f"Original:   5'-{dna}-3'")
print(f"Complement: 3'-{comp}-5'")
```

### Reverse Complement

```python
def reverse_complement(sequence):
    """Get reverse complement of DNA sequence"""
    # Get complement
    complement_map = str.maketrans('ATCG', 'TAGC')
    complement = sequence.translate(complement_map)
    
    # Reverse
    reverse_comp = complement[::-1]
    
    return reverse_comp

# Alternative implementation
def reverse_complement_v2(sequence):
    """Alternative reverse complement implementation"""
    complement = get_complement(sequence)
    return complement[::-1]

dna = "ATCGATCG"
rev_comp = reverse_complement(dna)

print(f"Original:           5'-{dna}-3'")
print(f"Reverse Complement: 5'-{rev_comp}-3'")

# Verify
print(f"\nVerification:")
print(f"Original:   {dna}")
print(f"Complement: {get_complement(dna)}")
print(f"Reversed:   {dna[::-1]}")
print(f"Rev Comp:   {rev_comp}")
```

### Why Reverse Complement Matters

```python
# Example: Primer design
forward_primer = "ATCGATCG"
reverse_primer = reverse_complement(forward_primer)

print("PCR Primer Pair:")
print(f"Forward: 5'-{forward_primer}-3'")
print(f"Reverse: 5'-{reverse_primer}-3'")

# Example: Reading both strands
def analyze_both_strands(sequence):
    """Analyze both DNA strands"""
    forward = sequence
    reverse = reverse_complement(sequence)
    
    print(f"Forward strand: {forward}")
    print(f"  GC content: {calculate_gc_content(forward):.2f}%")
    
    print(f"Reverse strand: {reverse}")
    print(f"  GC content: {calculate_gc_content(reverse):.2f}%")
    
    return forward, reverse

dna = "ATGCGTACGTAGCTAGCTA"
analyze_both_strands(dna)
```

---

## ✅ Sequence Validation

### Basic Validation

```python
def is_valid_dna(sequence):
    """Check if sequence contains only valid DNA bases"""
    valid_bases = set('ATCG')
    sequence_bases = set(sequence.upper())
    return sequence_bases.issubset(valid_bases)

# Test
sequences = ["ATCG", "ATCGX", "AUGC", "atcg"]
for seq in sequences:
    valid = is_valid_dna(seq)
    print(f"{seq}: {'Valid' if valid else 'Invalid'}")
```

### Comprehensive Validation

```python
def validate_sequence(sequence, seq_type='DNA'):
    """
    Validate biological sequence
    
    Parameters:
        sequence: sequence string
        seq_type: 'DNA', 'RNA', or 'PROTEIN'
    
    Returns:
        tuple: (is_valid, error_messages)
    """
    sequence = sequence.upper()
    errors = []
    
    # Check if empty
    if not sequence:
        errors.append("Empty sequence")
        return False, errors
    
    # Define valid characters
    if seq_type == 'DNA':
        valid = set('ATCGN')  # N for ambiguous
    elif seq_type == 'RNA':
        valid = set('AUCGN')
    else:
        errors.append(f"Unknown sequence type: {seq_type}")
        return False, errors
    
    # Check for invalid characters
    invalid_chars = set(sequence) - valid
    if invalid_chars:
        errors.append(f"Invalid characters: {invalid_chars}")
    
    # Check for suspicious patterns
    if len(sequence) < 3:
        errors.append("Sequence too short (< 3 bases)")
    
    # Check for homopolymer runs (quality control)
    for base in 'ATCG':
        if base * 10 in sequence:
            errors.append(f"Long {base} homopolymer detected")
    
    is_valid = len(errors) == 0
    return is_valid, errors

# Test validation
test_sequences = [
    ("ATCGATCG", "DNA"),
    ("AUCGAUCG", "RNA"),
    ("ATCGXYZ", "DNA"),
    ("AA", "DNA"),
    ("AAAAAAAAAAAATCG", "DNA")
]

for seq, stype in test_sequences:
    valid, errors = validate_sequence(seq, stype)
    print(f"\n{seq} ({stype}): {'✓ Valid' if valid else '✗ Invalid'}")
    for error in errors:
        print(f"  - {error}")
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: Complete Sequence Analyzer

```python
def analyze_sequence(sequence, name="Unknown"):
    """Complete sequence analysis"""
    print(f"{'='*50}")
    print(f"Sequence Analysis: {name}")
    print(f"{'='*50}\n")
    
    # Basic info
    print(f"Sequence: {sequence}")
    print(f"Length: {len(sequence)} bp\n")
    
    # Nucleotide counts
    counts = count_nucleotides(sequence)
    print("Nucleotide Composition:")
    for base, count in sorted(counts.items()):
        percent = (count / len(sequence)) * 100
        print(f"  {base}: {count:3d} ({percent:5.2f}%)")
    
    # GC content
    gc = calculate_gc_content(sequence)
    print(f"\nGC Content: {gc:.2f}%")
    
    # Transcription
    rna = transcribe(sequence)
    print(f"\nTranscribed RNA: {rna}")
    
    # Codons
    codons = extract_codons(sequence)
    print(f"\nCodons ({len(codons)} total):")
    print(f"  {' '.join(codons[:10])}")
    if len(codons) > 10:
        print(f"  ... and {len(codons) - 10} more")
    
    # Complement
    complement = get_complement(sequence)
    rev_comp = reverse_complement(sequence)
    print(f"\nComplement:        {complement}")
    print(f"Reverse Complement: {rev_comp}")
    
    print(f"\n{'='*50}\n")

# Test
dna = "ATGCGTACGTAGCTAGCTA"
analyze_sequence(dna, "Sample Gene")
```

### Example 2: Multi-Sequence Comparator

```python
def compare_sequences(seq1, seq2):
    """Compare two sequences"""
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}\n")
    
    # Length comparison
    print(f"Lengths: {len(seq1)} vs {len(seq2)}")
    
    # GC content comparison
    gc1 = calculate_gc_content(seq1)
    gc2 = calculate_gc_content(seq2)
    print(f"GC Content: {gc1:.2f}% vs {gc2:.2f}%")
    
    # Similarity (simple)
    if len(seq1) == len(seq2):
        matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
        similarity = (matches / len(seq1)) * 100
        print(f"Similarity: {similarity:.2f}%")
    else:
        print("Similarity: Cannot compare (different lengths)")
    
    # Complement check
    if seq2 == reverse_complement(seq1):
        print("\n⚠ Sequence 2 is the reverse complement of Sequence 1!")

seq1 = "ATCGATCG"
seq2 = "CGATCGAT"
compare_sequences(seq1, seq2)
```

---

## 📝 Practice Tasks (Day 13)

### Basic Exercises

1. **Nucleotide Counter**: Write a function that counts each nucleotide and prints percentages.

2. **GC Calculator**: Create a function that calculates and classifies GC content (low/medium/high).

3. **Transcription Tool**: Write a function that transcribes DNA to RNA and validates the input.

4. **Codon Extractor**: Extract all codons from a sequence and identify start/stop codons.

5. **Complement Generator**: Write functions for both complement and reverse complement.

### Intermediate Challenges

6. **Sequence Validator**: Create a comprehensive validator that checks for:
   - Valid nucleotides only
   - Minimum length
   - No long homopolymer runs
   - Returns detailed error messages

7. **Reading Frames**: Extract all three reading frames from a DNA sequence.

8. **Motif Finder**: Write a function that finds all occurrences of a specific motif in a sequence.

9. **AT/GC Ratio**: Calculate and compare AT vs GC ratios, including AT skew and GC skew.

10. **Batch Processor**: Process multiple sequences and generate a summary report.

### Advanced Challenges

11. **Palindrome Detector**: Find palindromic sequences (restriction enzyme sites) of length 4-8.

12. **ORF Finder**: Identify Open Reading Frames (start codon to stop codon) in all six reading frames.

13. **Melting Temperature**: Calculate Tm for primers using the formula: Tm = 4(G+C) + 2(A+T).

14. **Sequence Aligner**: Implement a simple alignment algorithm to compare two sequences.

15. **FASTA Parser**: Write a complete FASTA file parser that handles multiple sequences.

---

## 💡 Key Takeaways

✓ DNA uses A, T, C, G; RNA uses A, U, C, G  
✓ Sequences are represented as uppercase strings  
✓ `.count()` method counts nucleotide occurrences  
✓ GC content = (G + C) / total × 100  
✓ Transcription: replace T with U  
✓ Codons are 3-nucleotide groups  
✓ Complement: A↔T, C↔G  
✓ Reverse complement: complement + reverse  
✓ Validation ensures data quality  
✓ String slicing extracts subsequences  
✓ Always handle edge cases (empty, invalid characters)  
✓ Use helper functions for reusability  

**Next**: Day 14 - Nucleotide Counter Project (applying these concepts in a complete project)
