# Day 17: Advanced String Handling & Regular Expressions

## 🔍 Master Pattern Matching for Bioinformatics

Regular expressions (regex) are **essential** for bioinformatics - they enable powerful pattern matching in DNA/RNA sequences, FASTA files, protein domains, and biological databases. Learn to find motifs, parse formats, and validate sequences efficiently.

### Why Regex for Bioinformatics?

- **Motif Discovery**: Find transcription factor binding sites, splice junctions
- **Sequence Validation**: Check format compliance, identify errors
- **Format Parsing**: Extract data from FASTA, GenBank, GFF, VCF files
- **Pattern Flexibility**: Match ambiguous nucleotides (N, R, Y, W, S)
- **High Performance**: Process millions of sequences efficiently

---

## 🎯 Learning Objectives

By the end of this guide, you will:

✓ Master regex syntax for biological pattern matching  
✓ Use character classes and quantifiers effectively  
✓ Capture and extract sequence features  
✓ Validate biological data formats  
✓ Parse complex file formats (FASTA, GenBank)  
✓ Find motifs with degenerate bases  
✓ Implement sequence quality control  

---

## 🧩 Part 1: Regex Fundamentals

### The re Module

```python
import re

# Four main methods
text = "ATGCGATCGATCG"

# 1. search() - Find first match
match = re.search(r'ATG', text)
if match:
    print(f"Found at position {match.start()}: {match.group()}")

# 2. findall() - Find all matches
all_matches = re.findall(r'ATG', text)
print(f"All matches: {all_matches}")

# 3. finditer() - Iterator with positions
for match in re.finditer(r'ATC', text):
    print(f"Position {match.start()}-{match.end()}: {match.group()}")

# 4. sub() - Replace matches
replaced = re.sub(r'ATG', 'START', text)
print(f"Replaced: {replaced}")
```

### Basic Pattern Elements

```python
# Literal characters
pattern = r'ATG'  # Matches exactly "ATG"

# Character classes
pattern = r'[ATCG]'      # Any nucleotide
pattern = r'[^ATCG]'     # NOT a nucleotide (^ = negation)
pattern = r'[AT]'        # A or T only
pattern = r'[A-Z]'       # Any uppercase letter

# Predefined classes
pattern = r'\d'          # Digit [0-9]
pattern = r'\w'          # Word character [A-Za-z0-9_]
pattern = r'\s'          # Whitespace [ \t\n\r]
pattern = r'.'           # ANY character (except newline)

# Examples
dna = "ATG123CGA"
print(re.findall(r'[ATCG]', dna))     # ['A', 'T', 'G', 'C', 'G', 'A']
print(re.findall(r'\d', dna))          # ['1', '2', '3']
print(re.findall(r'[ATCG]+', dna))     # ['ATG', 'CGA']
```

### Quantifiers

```python
# Basic quantifiers
r'A*'        # 0 or more A's
r'A+'        # 1 or more A's
r'A?'        # 0 or 1 A (optional)
r'A{3}'      # Exactly 3 A's
r'A{2,5}'    # 2 to 5 A's
r'A{3,}'     # 3 or more A's

# Examples
dna = "AAATGCAAAGC"
print(re.findall(r'A+', dna))          # ['AAA', 'AAA']
print(re.findall(r'A{2,}', dna))       # ['AAA', 'AAA']
print(re.findall(r'A{3}', dna))        # ['AAA', 'AAA']
print(re.findall(r'GC?', dna))         # ['G', 'GC', 'G', 'GC']
```

### Anchors and Boundaries

```python
# Position anchors
r'^ATG'      # Start of string
r'TAG$'      # End of string
r'\b\w+\b'   # Word boundary

# Examples
sequences = ["ATGCGA", "CGATG", "ATGCGATG"]

for seq in sequences:
    if re.search(r'^ATG', seq):
        print(f"{seq}: Starts with ATG (start codon)")
    if re.search(r'TAG$', seq):
        print(f"{seq}: Ends with TAG (stop codon)")

# Find complete words
text = "gene1 gene2 gene123"
genes = re.findall(r'\bgene\b', text)  # Only "gene", not "gene1"
print(genes)
```

---

## 🧩 Part 2: Bioinformatics Applications

### DNA/RNA Motif Finding

```python
def find_start_codons(sequence):
    """Find all start codon positions"""
    positions = []
    for match in re.finditer(r'ATG', sequence):
        positions.append(match.start())
    return positions

def find_stop_codons(sequence):
    """Find all stop codon positions"""
    stop_pattern = r'TAA|TAG|TGA'
    positions = []
    for match in re.finditer(stop_pattern, sequence):
        positions.append((match.start(), match.group()))
    return positions

# Test
dna = "ATGCGATCGTAAATGGGCTAGTGA"
starts = find_start_codons(dna)
stops = find_stop_codons(dna)

print(f"Start codons at: {starts}")
print(f"Stop codons: {stops}")
```

### Restriction Enzyme Sites

```python
def find_restriction_sites(sequence):
    """
    Find common restriction enzyme recognition sites
    Returns dict with enzyme names and positions
    """
    enzymes = {
        'EcoRI': r'GAATTC',
        'BamHI': r'GGATCC',
        'PstI': r'CTGCAG',
        'HindIII': r'AAGCTT',
        'NotI': r'GCGGCCGC',
        'EcoRV': r'GATATC'
    }
    
    results = {}
    
    for enzyme, pattern in enzymes.items():
        matches = list(re.finditer(pattern, sequence))
        if matches:
            results[enzyme] = [m.start() for m in matches]
    
    return results

# Test
dna = "ATCGGAATTCCGATGGATCCAAGCTTGCGGCCGC"
sites = find_restriction_sites(dna)

for enzyme, positions in sites.items():
    print(f"{enzyme}: positions {positions}")
```

### Degenerate Base Matching

```python
def create_degenerate_pattern(motif):
    """
    Convert IUPAC degenerate bases to regex pattern
    
    IUPAC codes:
    R = A or G (puRine)
    Y = C or T (pYrimidine)
    W = A or T (Weak)
    S = G or C (Strong)
    M = A or C (aMino)
    K = G or T (Keto)
    N = any base
    """
    conversions = {
        'R': '[AG]',
        'Y': '[CT]',
        'W': '[AT]',
        'S': '[GC]',
        'M': '[AC]',
        'K': '[GT]',
        'N': '[ATCG]',
        'A': 'A', 'T': 'T', 'G': 'G', 'C': 'C'
    }
    
    pattern = ''.join(conversions.get(base, base) for base in motif.upper())
    return pattern

def find_motif(sequence, motif):
    """Find motif with degenerate bases"""
    pattern = create_degenerate_pattern(motif)
    matches = []
    
    for match in re.finditer(pattern, sequence.upper()):
        matches.append({
            'position': match.start(),
            'sequence': match.group(),
            'motif': motif
        })
    
    return matches

# Test: Find TATA box variants
dna = "GCGCTATAATAAGCTATAAATGCTATAGAA"
tata_box = "TATAWAW"  # W = A or T

matches = find_motif(dna, tata_box)
for m in matches:
    print(f"Position {m['position']}: {m['sequence']} (motif: {m['motif']})")
```

### Kozak Consensus Sequence

```python
def find_kozak_sequence(sequence):
    """
    Find Kozak consensus: (gcc)gccRccATGG
    R = A or G
    Lowercase = less conserved
    """
    # Strong Kozak: GCCRCCATGG
    strong_pattern = r'GCC[AG]CCATGG'
    
    # Weak Kozak: just ATG with some context
    weak_pattern = r'[AG]CC[AG]..ATG'
    
    strong_matches = list(re.finditer(strong_pattern, sequence))
    weak_matches = list(re.finditer(weak_pattern, sequence))
    
    return {
        'strong': [(m.start(), m.group()) for m in strong_matches],
        'weak': [(m.start(), m.group()) for m in weak_matches]
    }

# Test
mrna = "GCGAGCCRCCATGGCGCCGCCATGGCTAGATG"
kozak = find_kozak_sequence(mrna)

print("Strong Kozak sequences:")
for pos, seq in kozak['strong']:
    print(f"  Position {pos}: {seq}")
```

---

## 🧩 Part 3: Capture Groups & Extraction

### Basic Capture Groups

```python
# Parentheses create capture groups
pattern = r'(ATG)(\w{3})(TAG)'
text = "ATGAAATAG"

match = re.search(pattern, text)
if match:
    print(f"Full match: {match.group(0)}")    # ATGAAATAG
    print(f"Group 1: {match.group(1)}")       # ATG
    print(f"Group 2: {match.group(2)}")       # AAA
    print(f"Group 3: {match.group(3)}")       # TAG
```

### FASTA Header Parsing

```python
def parse_fasta_header(header):
    """
    Parse NCBI FASTA header
    Format: >gi|ID|ref|ACCESSION.VERSION| Description
    """
    # Pattern with capture groups
    pattern = r'>(?:gi\|)?(\w+)\|(?:ref\|)?(\w+\.?\d*)\|\s*(.+)'
    
    match = re.search(pattern, header)
    if match:
        return {
            'id': match.group(1),
            'accession': match.group(2),
            'description': match.group(3)
        }
    
    # Simple format: >ID Description
    simple_pattern = r'>(\S+)\s+(.*)'
    match = re.search(simple_pattern, header)
    if match:
        return {
            'id': match.group(1),
            'accession': '',
            'description': match.group(2)
        }
    
    return None

# Test
headers = [
    ">gi|123456|ref|NM_001234.5| Homo sapiens BRCA1",
    ">NM_007294 BRCA1 gene",
    ">gene1 Tumor suppressor"
]

for header in headers:
    parsed = parse_fasta_header(header)
    print(f"ID: {parsed['id']}, Accession: {parsed['accession']}")
    print(f"  Description: {parsed['description']}\n")
```

### GenBank Feature Extraction

```python
def extract_genbank_features(genbank_text):
    """Extract features from GenBank format"""
    # Pattern for feature entries
    # Format:     feature_type    start..end
    pattern = r'^\s{5}(\w+)\s+(\d+)\.\.(\d+)'
    
    features = []
    
    for line in genbank_text.split('\n'):
        match = re.match(pattern, line)
        if match:
            features.append({
                'type': match.group(1),
                'start': int(match.group(2)),
                'end': int(match.group(3))
            })
    
    return features

# Test
genbank = """
     CDS             123..456
     gene            789..1200
     mRNA            123..1200
"""

features = extract_genbank_features(genbank)
for f in features:
    print(f"{f['type']}: {f['start']}-{f['end']}")
```

### Named Groups

```python
def parse_coordinate(coord_string):
    """
    Parse genomic coordinates
    Format: chr1:12345-67890
    """
    pattern = r'(?P<chr>chr\w+):(?P<start>\d+)-(?P<end>\d+)'
    
    match = re.search(pattern, coord_string)
    if match:
        return {
            'chromosome': match.group('chr'),
            'start': int(match.group('start')),
            'end': int(match.group('end')),
            'length': int(match.group('end')) - int(match.group('start')) + 1
        }
    
    return None

# Test
coordinates = "chr1:123456-789012"
parsed = parse_coordinate(coordinates)
print(f"Chromosome: {parsed['chromosome']}")
print(f"Region: {parsed['start']}-{parsed['end']}")
print(f"Length: {parsed['length']} bp")
```

---

## 🧩 Part 4: Advanced Patterns

### Lookahead and Lookbehind

```python
# Positive lookahead: (?=...)
# Match if followed by pattern
pattern = r'ATG(?=TAA)'  # ATG followed by TAA
text = "ATGTAA ATGTAG"
print(re.findall(pattern, text))  # ['ATG'] (only first one)

# Negative lookahead: (?!...)
# Match if NOT followed by pattern
pattern = r'ATG(?!TAA)'  # ATG NOT followed by TAA
print(re.findall(pattern, text))  # ['ATG'] (second one)

# Positive lookbehind: (?<=...)
# Match if preceded by pattern
pattern = r'(?<=ATG)TAA'  # TAA preceded by ATG
print(re.findall(pattern, text))  # ['TAA']

# Practical example: Find CpG islands
def find_cpg_islands(sequence, min_length=20):
    """
    Find CpG islands (regions with high CG content)
    Definition: CG followed by another CG within 10 bases
    """
    cpg_pattern = r'CG(?=.{0,10}CG)'
    
    matches = list(re.finditer(cpg_pattern, sequence))
    
    # Group nearby matches into islands
    islands = []
    if matches:
        start = matches[0].start()
        end = matches[0].end()
        
        for match in matches[1:]:
            if match.start() - end < 10:
                end = match.end()
            else:
                if end - start >= min_length:
                    islands.append((start, end))
                start = match.start()
                end = match.end()
        
        if end - start >= min_length:
            islands.append((start, end))
    
    return islands

# Test
dna = "ATCGCGCGATATCGCGCGAT"
islands = find_cpg_islands(dna)
print(f"CpG islands: {islands}")
```

### Greedy vs Non-Greedy

```python
text = "<gene>BRCA1</gene><gene>TP53</gene>"

# Greedy (default): matches as much as possible
greedy = re.findall(r'<gene>.*</gene>', text)
print(f"Greedy: {greedy}")
# Output: ['<gene>BRCA1</gene><gene>TP53</gene>']

# Non-greedy: matches as little as possible
non_greedy = re.findall(r'<gene>.*?</gene>', text)
print(f"Non-greedy: {non_greedy}")
# Output: ['<gene>BRCA1</gene>', '<gene>TP53</gene>']

# Practical: Extract sequences from FASTA
fasta = ">gene1\nATCG\nGCTA\n>gene2\nTAGC\n"

# Wrong (greedy)
wrong = re.findall(r'>.*\n(.+)', fasta)
print(f"Wrong: {wrong}")

# Correct (non-greedy with proper pattern)
sequences = re.findall(r'>.*?\n((?:[ATCG\n]+))', fasta)
print(f"Correct: {sequences}")
```

---

## 🧩 Part 5: Complete Validators

### DNA Sequence Validator

```python
import re

def validate_dna_sequence(sequence):
    """
    Comprehensive DNA sequence validation
    Returns (is_valid, errors, warnings)
    """
    errors = []
    warnings = []
    
    # 1. Check empty
    if not sequence:
        errors.append("Empty sequence")
        return False, errors, warnings
    
    # 2. Check valid characters
    if not re.match(r'^[ATCGNatcgn]+$', sequence):
        invalid_chars = set(re.findall(r'[^ATCGNatcgn]', sequence))
        errors.append(f"Invalid characters: {invalid_chars}")
    
    # 3. Check for too many N's
    n_count = len(re.findall(r'[Nn]', sequence))
    if n_count / len(sequence) > 0.1:
        warnings.append(f"High N content: {n_count/len(sequence)*100:.1f}%")
    
    # 4. Check for homopolymers (e.g., AAAAAAAA)
    for base in 'ATCG':
        pattern = base + '{15,}'
        if re.search(pattern, sequence, re.IGNORECASE):
            warnings.append(f"Long {base} homopolymer detected (>15 bp)")
    
    # 5. Check for low complexity regions
    if re.search(r'(.{2,3})\1{5,}', sequence, re.IGNORECASE):
        warnings.append("Low complexity region detected (repeated di/tri-nucleotides)")
    
    is_valid = len(errors) == 0
    return is_valid, errors, warnings

# Test
sequences = [
    "ATCGATCG",
    "ATCGXYZ",
    "ATCGATCGNNNNNNNNNNATCG",
    "AAAAAAAAAAAAAAAAAAA",
    "ATATATATATATATATATAT"
]

for seq in sequences:
    valid, errors, warnings = validate_dna_sequence(seq)
    print(f"\n{seq[:20]}...")
    print(f"  Valid: {valid}")
    if errors:
        print(f"  Errors: {errors}")
    if warnings:
        print(f"  Warnings: {warnings}")
```

### FASTA Format Validator

```python
def validate_fasta(text):
    """
    Validate FASTA format
    Returns (is_valid, errors)
    """
    errors = []
    
    # 1. Check for at least one header
    if not re.search(r'^>', text, re.MULTILINE):
        errors.append("No FASTA header found (must start with >)")
        return False, errors
    
    # 2. Split into records
    records = re.split(r'\n(?=>)', text.strip())
    
    for i, record in enumerate(records, 1):
        lines = record.split('\n')
        
        # Check header format
        if not re.match(r'^>\S+', lines[0]):
            errors.append(f"Record {i}: Invalid header format")
            continue
        
        # Check sequence exists
        if len(lines) < 2:
            errors.append(f"Record {i}: No sequence found")
            continue
        
        # Validate sequence lines
        sequence = ''.join(lines[1:])
        if not re.match(r'^[A-Za-z\-*]+$', sequence):
            errors.append(f"Record {i}: Invalid sequence characters")
        
        # Check sequence length
        if len(sequence) == 0:
            errors.append(f"Record {i}: Empty sequence")
    
    is_valid = len(errors) == 0
    return is_valid, errors

# Test
valid_fasta = """>gene1
ATCGATCG
GCTAGCTA
>gene2
TAGCTAGC"""

invalid_fasta = """gene1
ATCG
>gene2"""

print("Valid FASTA:")
valid, errors = validate_fasta(valid_fasta)
print(f"  Valid: {valid}")

print("\nInvalid FASTA:")
valid, errors = validate_fasta(invalid_fasta)
print(f"  Valid: {valid}")
print(f"  Errors: {errors}")
```

---

## 🧩 Part 6: Real-World Parser

### Complete FASTQ Parser

```python
def parse_fastq(text):
    """
    Parse FASTQ format (sequence + quality scores)
    Format:
        @ID
        SEQUENCE
        +
        QUALITY
    """
    # Pattern for one complete FASTQ record
    pattern = r'@(\S+)[^\n]*\n([ATCGN]+)\n\+\n(.+)'
    
    records = []
    
    for match in re.finditer(pattern, text, re.IGNORECASE):
        seq_id = match.group(1)
        sequence = match.group(2)
        quality = match.group(3)
        
        # Validate lengths match
        if len(sequence) != len(quality):
            print(f"Warning: {seq_id} - sequence/quality length mismatch")
            continue
        
        records.append({
            'id': seq_id,
            'sequence': sequence,
            'quality': quality,
            'length': len(sequence)
        })
    
    return records

# Test
fastq_data = """@read1
ATCGATCGATCG
+
IIIIIIIIIIII
@read2
GCTAGCTAGCTA
+
HHHHHHHHHHHH"""

reads = parse_fastq(fastq_data)
for read in reads:
    print(f"{read['id']}: {read['length']} bp")
    print(f"  Seq: {read['sequence'][:20]}...")
    print(f"  Qual: {read['quality'][:20]}...")
```

### VCF File Parser

```python
def parse_vcf_variants(vcf_text):
    """
    Parse VCF (Variant Call Format) entries
    Format: CHROM POS ID REF ALT QUAL FILTER INFO
    """
    # Skip header lines starting with #
    pattern = r'^(?!#)(\S+)\s+(\d+)\s+(\S+)\s+([ATCG]+)\s+([ATCG,]+)\s+(\S+)\s+(\S+)\s+(.+)'
    
    variants = []
    
    for line in vcf_text.split('\n'):
        match = re.match(pattern, line)
        if match:
            variants.append({
                'chrom': match.group(1),
                'pos': int(match.group(2)),
                'id': match.group(3),
                'ref': match.group(4),
                'alt': match.group(5).split(','),
                'qual': match.group(6),
                'filter': match.group(7),
                'info': match.group(8)
            })
    
    return variants

# Test
vcf_data = """##fileformat=VCFv4.2
#CHROM POS ID REF ALT QUAL FILTER INFO
chr1 12345 rs123 A G 30 PASS DP=100
chr1 67890 . C T,G 45 PASS DP=150"""

variants = parse_vcf_variants(vcf_data)
for var in variants:
    print(f"{var['chrom']}:{var['pos']} {var['ref']}->{var['alt']}")
```

---

## 📝 Practice Tasks (Day 17)

### Basic Exercises

1. **Codon Finder**: Find all ATG codons in a sequence and return their positions.

2. **GC Content by Window**: Calculate GC% in 100bp sliding windows using regex.

3. **Simple Validator**: Create a function that validates protein sequences (only ACDEFGHIKLMNPQRSTVWY*).

4. **Header Extractor**: Extract all FASTA headers from a multi-sequence file.

5. **Stop Codon Counter**: Count occurrences of all three stop codons.

### Intermediate Challenges

6. **Restriction Site Mapper**: Find all palindromic restriction sites (4-8 bp).

7. **Splice Site Finder**: Find GT-AG splice junctions with context (10 bp flanking).

8. **Quality Filter**: Parse FASTQ and filter reads with average quality > 30.

9. **Degenerate Motif Scanner**: Implement full IUPAC ambiguity code support.

10. **ORF Extractor**: Use regex to extract all ORFs (ATG...STOP) with positions.

### Advanced Challenges

11. **GenBank Parser**: Parse complete GenBank entries including features, sequence, and metadata.

12. **CpG Island Detector**: Implement sophisticated CpG island algorithm with clustering.

13. **Multi-Format Converter**: Convert between FASTA, FASTQ, and GenBank formats.

14. **Variant Annotator**: Parse VCF and annotate variants (synonymous/nonsynonymous).

15. **Regex-Based Aligner**: Implement simple local alignment using regex patterns.

---

## 💡 Key Takeaways

✓ **Raw strings (r'...')** prevent escape sequence interpretation  
✓ **Character classes []** match any single character from set  
✓ **Quantifiers (+, *, ?, {n,m})** control repetition  
✓ **Anchors (^, $)** match positions, not characters  
✓ **Capture groups ()** extract matched substrings  
✓ **Non-greedy (.*?)** matches minimal text  
✓ **Lookahead/lookbehind** match without consuming  
✓ **IUPAC codes** enable degenerate base matching  
✓ **re.finditer()** provides positions + matches  
✓ **Named groups (?P<name>)** improve readability  
✓ **Compile patterns** for repeated use: `re.compile()`  
✓ **MULTILINE flag** makes ^ and $ match line boundaries  
✓ **Always validate** biological data before processing  
✓ **Test edge cases**: empty sequences, special characters  
✓ **Combine regex with Python** for complex parsing  

**Next**: Object-Oriented Programming for Bioinformatics
