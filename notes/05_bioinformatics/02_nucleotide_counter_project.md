# Day 14: Practice Project — Nucleotide Counter (FASTA Format)

## 🧬 Project Overview

Build a complete **Nucleotide Counter** that reads FASTA-formatted sequences and performs comprehensive analysis. This project reinforces string manipulation, file handling, dictionaries, functions, and biological data processing.

### Learning Objectives

- Parse FASTA file format
- Count and analyze nucleotide frequencies
- Calculate biological metrics (GC content, AT/GC ratios)
- Handle real-world sequence data
- Implement error handling and validation
- Generate professional analysis reports

---

## 📘 Understanding FASTA Format

### What is FASTA?

**FASTA** is the most common format for representing biological sequences. It's simple, human-readable, and widely supported.

### FASTA Structure

```
>SequenceID Description information here
ATGCTAGCTAGCTAGCTAGCTAGCTAACG
TAGCTAGCTAGCTAGCTAGCTAGCTAGCT
>AnotherSequence Organism=Human Gene=BRCA1
GCTAGCTAGCTAGCTAGCTAGCTAGCTAG
```

**Components:**
- **Header line**: Starts with `>`, followed by sequence ID and optional description
- **Sequence lines**: One or more lines containing the actual sequence
- **Multiple records**: Each new header starts a new sequence

### FASTA Variants

```python
# Single-line sequence
">seq1\nATGCTAGCTAGC"

# Multi-line sequence (typical)
">seq1\nATGCTAGC\nTAGCTAGC"

# With detailed header
">NM_007294.3 Homo sapiens BRCA1 gene\nATGCTAGC"

# Multiple sequences
">seq1\nATGC\n>seq2\nGCTA"
```

---

## 🎯 Project Requirements

### Core Features

1. **Parse FASTA input** (string or file)
2. **Extract sequence data** (ignore headers)
3. **Count nucleotides** (A, T, G, C)
4. **Calculate GC content**
5. **Handle ambiguous bases** (N, R, Y, etc.)
6. **Validate sequences**
7. **Generate report**

### Advanced Features

8. Multiple sequence handling
9. Statistical analysis
10. Export results
11. Visualization (optional)

---

## 🧩 Step-by-Step Implementation

### Step 1: Parse FASTA Header

```python
def parse_fasta_header(header_line):
    """Parse FASTA header line"""
    # Remove '>' character
    header = header_line.lstrip('>')
    
    # Split ID from description
    parts = header.split(maxsplit=1)
    seq_id = parts[0] if parts else "Unknown"
    description = parts[1] if len(parts) > 1 else ""
    
    return seq_id, description

# Test
header = ">NM_007294.3 Homo sapiens BRCA1 gene"
seq_id, desc = parse_fasta_header(header)
print(f"ID: {seq_id}")
print(f"Description: {desc}")
```

### Step 2: Extract Sequence from FASTA

```python
def extract_sequence(fasta_text):
    """Extract sequence from FASTA format (single sequence)"""
    lines = fasta_text.strip().split('\n')
    
    # Join all non-header lines
    sequence = ''.join(
        line.strip() 
        for line in lines 
        if not line.startswith('>')
    ).upper()
    
    return sequence

# Test
fasta = """>seq1
ATGCTAGC
TAGCTAGC"""

seq = extract_sequence(fasta)
print(f"Extracted: {seq}")
```

### Step 3: Count Nucleotides with Dictionary

```python
def count_nucleotides(sequence):
    """Count each nucleotide in sequence"""
    counts = {}
    
    for base in sequence:
        counts[base] = counts.get(base, 0) + 1
    
    return counts

# Test
sequence = "ATGCTAGCTAGC"
counts = count_nucleotides(sequence)
print(counts)

# Alternative: Initialize dictionary
def count_nucleotides_v2(sequence):
    """Count with pre-initialized dictionary"""
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    
    for base in sequence:
        if base in counts:
            counts[base] += 1
        else:
            counts[base] = counts.get(base, 0) + 1
    
    return counts
```

### Step 4: Display Results Formatted

```python
def display_counts(counts, sequence_length):
    """Display nucleotide counts with formatting"""
    print("\n" + "="*50)
    print("NUCLEOTIDE ANALYSIS REPORT")
    print("="*50)
    
    print(f"\nTotal Length: {sequence_length} bp")
    print("\nNucleotide Frequencies:")
    print("-" * 40)
    
    # Standard bases
    for base in ['A', 'T', 'G', 'C']:
        count = counts.get(base, 0)
        percent = (count / sequence_length * 100) if sequence_length > 0 else 0
        print(f"  {base}: {count:5d} ({percent:6.2f}%)")
    
    # Other bases (if any)
    other_bases = {k: v for k, v in counts.items() if k not in 'ATGC'}
    if other_bases:
        print("\nAmbiguous/Other Bases:")
        print("-" * 40)
        for base, count in sorted(other_bases.items()):
            percent = (count / sequence_length * 100) if sequence_length > 0 else 0
            print(f"  {base}: {count:5d} ({percent:6.2f}%)")
    
    print("="*50 + "\n")

# Test
counts = {'A': 7, 'T': 6, 'G': 5, 'C': 7, 'N': 2}
display_counts(counts, sum(counts.values()))
```

### Step 5: Calculate GC Content

```python
def calculate_metrics(counts, sequence_length):
    """Calculate biological metrics"""
    if sequence_length == 0:
        return {}
    
    # Basic counts
    a_count = counts.get('A', 0)
    t_count = counts.get('T', 0)
    g_count = counts.get('G', 0)
    c_count = counts.get('C', 0)
    
    # Metrics
    at_count = a_count + t_count
    gc_count = g_count + c_count
    
    at_percent = (at_count / sequence_length) * 100
    gc_percent = (gc_count / sequence_length) * 100
    
    # Ratios
    at_gc_ratio = at_count / gc_count if gc_count > 0 else float('inf')
    
    # Skew
    gc_skew = (g_count - c_count) / (g_count + c_count) if (g_count + c_count) > 0 else 0
    at_skew = (a_count - t_count) / (a_count + t_count) if (a_count + t_count) > 0 else 0
    
    return {
        'at_percent': at_percent,
        'gc_percent': gc_percent,
        'at_gc_ratio': at_gc_ratio,
        'gc_skew': gc_skew,
        'at_skew': at_skew
    }

def display_metrics(metrics):
    """Display calculated metrics"""
    print("\nBIOLOGICAL METRICS:")
    print("-" * 40)
    print(f"AT Content: {metrics['at_percent']:.2f}%")
    print(f"GC Content: {metrics['gc_percent']:.2f}%")
    print(f"AT/GC Ratio: {metrics['at_gc_ratio']:.3f}")
    print(f"GC Skew: {metrics['gc_skew']:.3f}")
    print(f"AT Skew: {metrics['at_skew']:.3f}")
```

### Step 6: Handle Ambiguous Bases

```python
def categorize_bases(sequence):
    """Categorize bases as standard, ambiguous, or invalid"""
    standard = set('ATGC')
    ambiguous = set('NRYKMSWBDHV')  # IUPAC ambiguity codes
    
    standard_bases = []
    ambiguous_bases = []
    invalid_bases = []
    
    for base in sequence.upper():
        if base in standard:
            standard_bases.append(base)
        elif base in ambiguous:
            ambiguous_bases.append(base)
        else:
            invalid_bases.append(base)
    
    return {
        'standard': standard_bases,
        'ambiguous': ambiguous_bases,
        'invalid': invalid_bases
    }

def analyze_sequence_quality(sequence):
    """Analyze sequence quality"""
    categorized = categorize_bases(sequence)
    
    total = len(sequence)
    standard_count = len(categorized['standard'])
    ambiguous_count = len(categorized['ambiguous'])
    invalid_count = len(categorized['invalid'])
    
    print("\nSEQUENCE QUALITY:")
    print("-" * 40)
    print(f"Total bases: {total}")
    print(f"Standard (ATGC): {standard_count} ({standard_count/total*100:.1f}%)")
    print(f"Ambiguous (N,R,Y...): {ambiguous_count} ({ambiguous_count/total*100:.1f}%)")
    print(f"Invalid: {invalid_count} ({invalid_count/total*100:.1f}%)")
    
    if invalid_count > 0:
        unique_invalid = set(categorized['invalid'])
        print(f"Invalid characters: {unique_invalid}")
    
    return categorized
```

---

## 🧠 Complete Nucleotide Counter Program

```python
def analyze_fasta_sequence(fasta_text, show_quality=True):
    """
    Complete FASTA sequence analysis
    
    Parameters:
        fasta_text: FASTA formatted string
        show_quality: Show quality metrics
    
    Returns:
        dict: Analysis results
    """
    # Parse header
    lines = fasta_text.strip().split('\n')
    header_line = lines[0] if lines[0].startswith('>') else ">Unknown"
    seq_id, description = parse_fasta_header(header_line)
    
    # Extract sequence
    sequence = extract_sequence(fasta_text)
    
    # Count nucleotides
    counts = count_nucleotides(sequence)
    
    # Calculate metrics
    metrics = calculate_metrics(counts, len(sequence))
    
    # Display results
    print("\n" + "="*60)
    print(f"SEQUENCE ANALYSIS: {seq_id}")
    print("="*60)
    
    if description:
        print(f"Description: {description}")
    
    print(f"\nSequence Preview: {sequence[:60]}...")
    print(f"Total Length: {len(sequence)} bp")
    
    # Nucleotide counts
    print("\nNUCLEOTIDE FREQUENCIES:")
    print("-" * 40)
    for base in ['A', 'T', 'G', 'C']:
        count = counts.get(base, 0)
        percent = (count / len(sequence) * 100) if len(sequence) > 0 else 0
        bar = '█' * int(percent / 2)  # Visual bar
        print(f"  {base}: {count:5d} ({percent:6.2f}%) {bar}")
    
    # Metrics
    display_metrics(metrics)
    
    # Quality check
    if show_quality:
        analyze_sequence_quality(sequence)
    
    print("="*60 + "\n")
    
    return {
        'id': seq_id,
        'description': description,
        'sequence': sequence,
        'length': len(sequence),
        'counts': counts,
        'metrics': metrics
    }

# Example usage
fasta_example = """>NM_007294.3 Homo sapiens BRCA1 gene fragment
ATGCTAGCTAGCTAGCTAGCTAGCTAACG
TAGCTAGCTAGCTAGCTAGCTAGCTAGCT
NNNATGCTAGC"""

result = analyze_fasta_sequence(fasta_example)
```

---

## 🔧 Advanced Features

### Multiple Sequence Handling

```python
def parse_multi_fasta(fasta_text):
    """Parse multiple FASTA sequences"""
    sequences = {}
    current_id = None
    current_seq = []
    
    for line in fasta_text.strip().split('\n'):
        line = line.strip()
        
        if line.startswith('>'):
            # Save previous sequence
            if current_id:
                sequences[current_id] = ''.join(current_seq).upper()
            
            # Start new sequence
            current_id, _ = parse_fasta_header(line)
            current_seq = []
        else:
            current_seq.append(line)
    
    # Save last sequence
    if current_id:
        sequences[current_id] = ''.join(current_seq).upper()
    
    return sequences

def analyze_multiple_sequences(fasta_text):
    """Analyze multiple FASTA sequences"""
    sequences = parse_multi_fasta(fasta_text)
    
    print(f"\nFound {len(sequences)} sequences")
    print("="*60)
    
    results = {}
    for seq_id, sequence in sequences.items():
        counts = count_nucleotides(sequence)
        metrics = calculate_metrics(counts, len(sequence))
        
        results[seq_id] = {
            'length': len(sequence),
            'counts': counts,
            'metrics': metrics
        }
        
        print(f"\n{seq_id}:")
        print(f"  Length: {len(sequence)} bp")
        print(f"  GC Content: {metrics['gc_percent']:.2f}%")
    
    return results

# Test with multiple sequences
multi_fasta = """>seq1
ATGCTAGC
>seq2
GCGCGCGC
>seq3
ATATATATAT"""

analyze_multiple_sequences(multi_fasta)
```

### File Reading and Writing

```python
def analyze_fasta_file(filename):
    """Analyze FASTA file"""
    try:
        with open(filename, 'r') as f:
            fasta_text = f.read()
        
        return analyze_fasta_sequence(fasta_text)
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def save_analysis_report(result, output_filename):
    """Save analysis report to file"""
    try:
        with open(output_filename, 'w') as f:
            f.write("NUCLEOTIDE ANALYSIS REPORT\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"Sequence ID: {result['id']}\n")
            f.write(f"Description: {result['description']}\n")
            f.write(f"Length: {result['length']} bp\n\n")
            
            f.write("Nucleotide Counts:\n")
            for base, count in sorted(result['counts'].items()):
                percent = (count / result['length'] * 100)
                f.write(f"  {base}: {count:5d} ({percent:6.2f}%)\n")
            
            f.write("\nMetrics:\n")
            for key, value in result['metrics'].items():
                f.write(f"  {key}: {value:.3f}\n")
        
        print(f"Report saved to {output_filename}")
    
    except Exception as e:
        print(f"Error saving report: {e}")
```

### Statistical Summary

```python
def generate_summary_statistics(sequences_dict):
    """Generate summary statistics for multiple sequences"""
    if not sequences_dict:
        return
    
    all_lengths = [len(seq) for seq in sequences_dict.values()]
    all_gc = []
    
    for seq in sequences_dict.values():
        counts = count_nucleotides(seq)
        metrics = calculate_metrics(counts, len(seq))
        all_gc.append(metrics['gc_percent'])
    
    print("\nSUMMARY STATISTICS:")
    print("="*60)
    print(f"Total sequences: {len(sequences_dict)}")
    print(f"\nLength Statistics:")
    print(f"  Min: {min(all_lengths)} bp")
    print(f"  Max: {max(all_lengths)} bp")
    print(f"  Mean: {sum(all_lengths)/len(all_lengths):.1f} bp")
    print(f"  Total: {sum(all_lengths)} bp")
    
    print(f"\nGC Content Statistics:")
    print(f"  Min: {min(all_gc):.2f}%")
    print(f"  Max: {max(all_gc):.2f}%")
    print(f"  Mean: {sum(all_gc)/len(all_gc):.2f}%")
```

---

## 📝 Practice Tasks (Day 14)

### Basic Exercises

1. **Simple Parser**: Write a function that extracts just the sequence ID from a FASTA header.

2. **Base Counter**: Create a function that counts only A, T, G, C and ignores other characters.

3. **GC Calculator**: Write a standalone function that takes a sequence and returns GC percentage.

4. **Sequence Cleaner**: Remove all non-ATGC characters from a sequence.

5. **Multi-line Handler**: Parse a multi-line FASTA sequence correctly.

### Intermediate Challenges

6. **Validation**: Add input validation that checks for:
   - Empty sequences
   - Invalid characters
   - Missing headers

7. **Comparative Analysis**: Compare GC content of two sequences and report which is higher.

8. **Batch Processor**: Process multiple FASTA sequences and create a summary table.

9. **Export Function**: Save results to CSV format with columns: ID, Length, A, T, G, C, GC%.

10. **Quality Score**: Assign quality scores based on:
    - Sequence length (longer = better)
    - GC content (40-60% = best)
    - Ambiguous bases (fewer = better)

### Advanced Challenges

11. **Complete Pipeline**: Build a complete pipeline that:
    - Reads FASTA file
    - Validates all sequences
    - Analyzes each sequence
    - Generates summary statistics
    - Exports results to file

12. **Codon Analysis**: Extend the counter to analyze codon frequencies.

13. **Motif Scanner**: Add functionality to find and count specific motifs (e.g., "TATA").

14. **Visualization**: Use string characters to create ASCII bar charts of nucleotide frequencies.

15. **Command-Line Tool**: Create a complete command-line tool that accepts arguments for input file, output file, and analysis options.

---

## 💡 Key Takeaways

✓ FASTA format: header line (>) + sequence lines  
✓ Use dictionaries for counting frequencies  
✓ `.get(key, default)` safely accesses dictionary values  
✓ String methods: `.split()`, `.strip()`, `.startswith()`  
✓ Calculate percentages: `(count / total) * 100`  
✓ Handle multiple sequences with loops and data structures  
✓ Validate input data before processing  
✓ Format output professionally with alignment and borders  
✓ Separate parsing, analysis, and display logic  
✓ Use try-except for file operations  
✓ Build reusable functions for common operations  
✓ Test with various inputs (single/multi-line, multiple sequences)  

**Next**: Day 15 - Gene Sequence Extraction (Advanced parsing and ORF finding)
