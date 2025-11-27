# Day 15-16: Gene Sequence Extraction & Analysis

## 🧬 Advanced Sequence Analysis Project

Build a comprehensive **Gene Sequence Analyzer** that performs professional-level bioinformatics operations: parsing FASTA files, finding Open Reading Frames (ORFs), identifying motifs, calculating codon usage, and generating detailed reports.

### Project Goals

- Parse complex FASTA files with multiple sequences
- Find and extract Open Reading Frames (ORFs)
- Identify biological motifs using pattern matching
- Perform codon usage analysis
- Generate professional analysis reports
- Handle edge cases and validate data

---

## 🎯 Project Requirements

### Core Functionality

1. **FASTA Parser** - Handle single and multiple sequences
2. **ORF Finder** - Identify coding regions in all reading frames
3. **Motif Scanner** - Find patterns and restriction sites
4. **Sequence Extraction** - Extract subsequences by coordinates
5. **Translation** - Convert DNA/RNA to protein
6. **Report Generator** - Create comprehensive analysis reports

### Advanced Features

7. Reverse complement analysis
8. Six-frame translation
9. Codon usage statistics
10. Export to various formats

---

## 🧩 Component 1: Advanced FASTA Parser

### Robust Multi-Sequence Parser

```python
import re
from typing import Dict, List, Tuple, Optional

def parse_fasta(text: str) -> Dict[str, Dict[str, str]]:
    """
    Parse FASTA format with full metadata
    
    Returns:
        dict: {seq_id: {'description': str, 'sequence': str}}
    """
    records = {}
    current_id = None
    current_desc = None
    current_seq = []
    
    for line in text.strip().splitlines():
        line = line.strip()
        
        if not line:  # Skip empty lines
            continue
        
        if line.startswith('>'):
            # Save previous sequence
            if current_id is not None:
                records[current_id] = {
                    'description': current_desc,
                    'sequence': ''.join(current_seq).upper()
                }
            
            # Parse new header
            header = line[1:].strip()
            parts = header.split(maxsplit=1)
            current_id = parts[0]
            current_desc = parts[1] if len(parts) > 1 else ""
            current_seq = []
        
        elif line.startswith(';'):
            # Comment line - skip
            continue
        
        else:
            # Sequence line
            current_seq.append(line)
    
    # Save last sequence
    if current_id is not None:
        records[current_id] = {
            'description': current_desc,
            'sequence': ''.join(current_seq).upper()
        }
    
    return records

# Test
fasta_test = """>gene1 Homo sapiens BRCA1
ATGCTAGCTAGCTAGC
TAGCTAGCTAGCTAG
>gene2 Beta-globin
ATGATGATGTAGTAA
;This is a comment
>gene3
GCGCGCGC"""

sequences = parse_fasta(fasta_test)
for seq_id, data in sequences.items():
    print(f"{seq_id}: {len(data['sequence'])} bp")
```

### Sequence Validation

```python
def validate_sequence(sequence: str, seq_type: str = 'DNA') -> Tuple[bool, List[str]]:
    """
    Validate biological sequence
    
    Parameters:
        sequence: Sequence string
        seq_type: 'DNA', 'RNA', or 'PROTEIN'
    
    Returns:
        tuple: (is_valid, list_of_errors)
    """
    errors = []
    
    if not sequence:
        errors.append("Empty sequence")
        return False, errors
    
    # Define valid characters
    valid_chars = {
        'DNA': set('ATCGN'),
        'RNA': set('AUCGN'),
        'PROTEIN': set('ACDEFGHIKLMNPQRSTVWY*')
    }
    
    if seq_type not in valid_chars:
        errors.append(f"Unknown sequence type: {seq_type}")
        return False, errors
    
    # Check for invalid characters
    invalid = set(sequence.upper()) - valid_chars[seq_type]
    if invalid:
        errors.append(f"Invalid characters: {invalid}")
    
    # Check length
    if len(sequence) < 3:
        errors.append("Sequence too short (< 3 bases)")
    
    # Check for excessive runs of same nucleotide
    for base in 'ATCGN':
        if base * 15 in sequence.upper():
            errors.append(f"Excessive {base} homopolymer detected (>15)")
    
    is_valid = len(errors) == 0
    return is_valid, errors

# Test
test_seqs = [
    ("ATCGATCG", "DNA"),
    ("AUCGAUCG", "RNA"),
    ("ATCGXYZ", "DNA"),
    ("AT", "DNA")
]

for seq, stype in test_seqs:
    valid, errs = validate_sequence(seq, stype)
    print(f"{seq}: {'✓' if valid else '✗'} {errs if errs else ''}")
```

---

## 🧩 Component 2: ORF Finder

### Understanding ORFs

An **Open Reading Frame (ORF)** is a continuous stretch of codons that:
- Starts with a start codon (ATG)
- Ends with a stop codon (TAA, TAG, TGA)
- Contains no internal stop codons

### Basic ORF Finder

```python
def find_orfs(sequence: str, min_length: int = 30) -> List[Dict]:
    """
    Find all ORFs in a sequence
    
    Parameters:
        sequence: DNA sequence
        min_length: Minimum ORF length in bp
    
    Returns:
        list: List of ORF dictionaries
    """
    sequence = sequence.upper()
    start_codon = 'ATG'
    stop_codons = {'TAA', 'TAG', 'TGA'}
    orfs = []
    
    # Search for ORFs
    i = 0
    while i < len(sequence) - 2:
        codon = sequence[i:i+3]
        
        if codon == start_codon:
            # Found start, look for stop
            j = i + 3
            while j < len(sequence) - 2:
                stop_codon = sequence[j:j+3]
                if stop_codon in stop_codons:
                    # Found complete ORF
                    orf_seq = sequence[i:j+3]
                    if len(orf_seq) >= min_length:
                        orfs.append({
                            'start': i,
                            'end': j + 3,
                            'length': len(orf_seq),
                            'sequence': orf_seq,
                            'frame': i % 3
                        })
                    i = j + 3  # Continue search after this ORF
                    break
                j += 3
            else:
                # No stop found
                i += 3
        else:
            i += 3
    
    return orfs

# Test
dna = "ATGATCGTAGCGATGAAATCGTAGATGCCCTAGTAA"
orfs = find_orfs(dna, min_length=9)

print(f"Found {len(orfs)} ORFs:")
for i, orf in enumerate(orfs, 1):
    print(f"  {i}. Position {orf['start']}-{orf['end']}: {orf['length']} bp")
    print(f"     Sequence: {orf['sequence']}")
```

### Six-Frame ORF Analysis

```python
def find_orfs_all_frames(sequence: str, min_length: int = 30) -> Dict:
    """
    Find ORFs in all six reading frames
    
    Returns:
        dict: ORFs organized by frame (+1, +2, +3, -1, -2, -3)
    """
    
    def get_reverse_complement(seq):
        """Get reverse complement"""
        complement = str.maketrans('ATCG', 'TAGC')
        return seq.translate(complement)[::-1]
    
    results = {}
    
    # Forward frames
    for frame in range(3):
        frame_name = f"+{frame+1}"
        frame_seq = sequence[frame:]
        results[frame_name] = find_orfs(frame_seq, min_length)
        
        # Adjust positions to full sequence coordinates
        for orf in results[frame_name]:
            orf['start'] += frame
            orf['end'] += frame
            orf['strand'] = '+'
    
    # Reverse frames
    rev_comp = get_reverse_complement(sequence)
    for frame in range(3):
        frame_name = f"-{frame+1}"
        frame_seq = rev_comp[frame:]
        results[frame_name] = find_orfs(frame_seq, min_length)
        
        # Adjust positions to original sequence coordinates
        seq_len = len(sequence)
        for orf in results[frame_name]:
            # Convert to reverse strand coordinates
            orf['start_rc'] = orf['start'] + frame
            orf['end_rc'] = orf['end'] + frame
            orf['start'] = seq_len - orf['end'] - frame
            orf['end'] = seq_len - orf['start_rc'] - frame
            orf['strand'] = '-'
    
    return results

def display_orf_summary(all_orfs: Dict):
    """Display summary of ORFs found"""
    print("\nORF ANALYSIS SUMMARY")
    print("="*60)
    
    total = sum(len(orfs) for orfs in all_orfs.values())
    print(f"Total ORFs found: {total}\n")
    
    for frame, orfs in sorted(all_orfs.items()):
        if orfs:
            print(f"{frame} frame: {len(orfs)} ORFs")
            for i, orf in enumerate(orfs, 1):
                strand_symbol = orf.get('strand', '+')
                print(f"  {i}. {orf['start']}-{orf['end']} ({orf['length']} bp) [{strand_symbol}]")
    
    print("="*60)

# Test
dna = "ATGATCGTAGCGATGAAATCGTAGATGCCCTAGTAA"
all_orfs = find_orfs_all_frames(dna, min_length=9)
display_orf_summary(all_orfs)
```

---

## 🧩 Component 3: Motif Scanner

### Pattern Matching with Regular Expressions

```python
def find_motifs(sequence: str, pattern: str) -> List[Tuple[int, int, str]]:
    """
    Find all occurrences of a motif pattern
    
    Parameters:
        sequence: DNA sequence
        pattern: Regex pattern or simple string
    
    Returns:
        list: [(start_pos, end_pos, matched_text), ...]
    """
    matches = []
    
    for match in re.finditer(pattern, sequence):
        matches.append((
            match.start(),
            match.end(),
            match.group()
        ))
    
    return matches

# Test simple patterns
dna = "ATCGATCGGAATTCGCTAGAATTCGAT"

# Find EcoRI site (GAATTC)
ecori_sites = find_motifs(dna, "GAATTC")
print(f"EcoRI sites: {len(ecori_sites)}")
for start, end, seq in ecori_sites:
    print(f"  Position {start}-{end}: {seq}")

# Find any ATG
atg_sites = find_motifs(dna, "ATG")
print(f"\nATG codons: {len(atg_sites)}")
```

### Common Restriction Sites

```python
def find_restriction_sites(sequence: str) -> Dict[str, List[int]]:
    """
    Find common restriction enzyme recognition sites
    
    Returns:
        dict: {enzyme_name: [positions]}
    """
    # Common restriction enzymes
    enzymes = {
        'EcoRI': 'GAATTC',
        'BamHI': 'GGATCC',
        'PstI': 'CTGCAG',
        'HindIII': 'AAGCTT',
        'NotI': 'GCGGCCGC',
        'XbaI': 'TCTAGA',
        'SalI': 'GTCGAC',
        'KpnI': 'GGTACC'
    }
    
    results = {}
    
    for enzyme, site in enzymes.items():
        matches = find_motifs(sequence, site)
        if matches:
            results[enzyme] = [pos for pos, _, _ in matches]
    
    return results

def display_restriction_sites(sites: Dict[str, List[int]]):
    """Display restriction sites found"""
    if not sites:
        print("No restriction sites found")
        return
    
    print("\nRESTRICTION ENZYME SITES")
    print("="*60)
    
    for enzyme, positions in sorted(sites.items()):
        print(f"{enzyme}: {len(positions)} site(s)")
        for pos in positions:
            print(f"  Position: {pos}")
    
    print("="*60)

# Test
dna = "ATCGGAATTCCGATGGATCCAAGCTTGCGGCCGCTAG"
sites = find_restriction_sites(dna)
display_restriction_sites(sites)
```

### Advanced Pattern Matching

```python
def find_promoter_elements(sequence: str) -> Dict[str, List[int]]:
    """
    Find common promoter elements
    
    Returns:
        dict: {element_name: [positions]}
    """
    elements = {
        'TATA_box': r'TATA[AT]A[AT]',
        'CAAT_box': r'CCAAT',
        'GC_box': r'GGGCGG',
        'Kozak_sequence': r'[AG]CCATGG'
    }
    
    results = {}
    
    for element, pattern in elements.items():
        matches = find_motifs(sequence, pattern)
        if matches:
            results[element] = [(pos, seq) for pos, _, seq in matches]
    
    return results

# Test
dna = "GCGCTATAATAAGCCATGGCGCCCAATGGGCGGATCG"
promoters = find_promoter_elements(dna)

print("\nPROMOTER ELEMENTS:")
for element, positions in promoters.items():
    print(f"{element}:")
    for pos, seq in positions:
        print(f"  Position {pos}: {seq}")
```

---

## 🧩 Component 4: Translation

### DNA/RNA to Protein

```python
def translate(sequence: str, table: int = 1) -> str:
    """
    Translate DNA/RNA to protein
    
    Parameters:
        sequence: DNA or RNA sequence
        table: Genetic code table (1 = standard)
    
    Returns:
        Protein sequence
    """
    # Standard genetic code
    codon_table = {
        'ATG': 'M', 'TAA': '*', 'TAG': '*', 'TGA': '*',
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TGT': 'C', 'TGC': 'C',
        'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L',
        'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
        'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q',
        'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R',
        'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    # Handle RNA (U -> T)
    sequence = sequence.upper().replace('U', 'T')
    
    protein = []
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        amino_acid = codon_table.get(codon, 'X')  # X for unknown
        protein.append(amino_acid)
        
        if amino_acid == '*':  # Stop codon
            break
    
    return ''.join(protein)

# Test
dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
protein = translate(dna)
print(f"DNA:     {dna}")
print(f"Protein: {protein}")
```

---

## 🧠 Complete Gene Analyzer

```python
class GeneAnalyzer:
    """Complete gene sequence analysis tool"""
    
    def __init__(self, fasta_text: str):
        """Initialize with FASTA input"""
        self.sequences = parse_fasta(fasta_text)
    
    def analyze_sequence(self, seq_id: str, min_orf_length: int = 30):
        """
        Perform complete analysis on a sequence
        
        Parameters:
            seq_id: Sequence identifier
            min_orf_length: Minimum ORF length
        
        Returns:
            dict: Complete analysis results
        """
        if seq_id not in self.sequences:
            raise KeyError(f"Sequence '{seq_id}' not found")
        
        seq_data = self.sequences[seq_id]
        sequence = seq_data['sequence']
        
        # Basic stats
        length = len(sequence)
        gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
        
        # Find ORFs
        orfs = find_orfs_all_frames(sequence, min_orf_length)
        total_orfs = sum(len(frame_orfs) for frame_orfs in orfs.values())
        
        # Find restriction sites
        sites = find_restriction_sites(sequence)
        
        # Validate
        valid, errors = validate_sequence(sequence, 'DNA')
        
        return {
            'id': seq_id,
            'description': seq_data['description'],
            'length': length,
            'gc_content': gc_content,
            'orfs': orfs,
            'total_orfs': total_orfs,
            'restriction_sites': sites,
            'valid': valid,
            'errors': errors
        }
    
    def generate_report(self, seq_id: str, min_orf_length: int = 30) -> str:
        """Generate comprehensive analysis report"""
        result = self.analyze_sequence(seq_id, min_orf_length)
        
        lines = []
        lines.append("="*70)
        lines.append(f"GENE SEQUENCE ANALYSIS REPORT")
        lines.append("="*70)
        lines.append(f"\nSequence ID: {result['id']}")
        lines.append(f"Description: {result['description']}")
        lines.append(f"Length: {result['length']} bp")
        lines.append(f"GC Content: {result['gc_content']:.2f}%")
        
        # Validation
        lines.append(f"\nValidation: {'✓ PASS' if result['valid'] else '✗ FAIL'}")
        if result['errors']:
            for error in result['errors']:
                lines.append(f"  - {error}")
        
        # ORFs
        lines.append(f"\nOpen Reading Frames: {result['total_orfs']} found")
        for frame, orfs in sorted(result['orfs'].items()):
            if orfs:
                lines.append(f"  {frame} frame: {len(orfs)} ORF(s)")
                for i, orf in enumerate(orfs[:3], 1):  # Show first 3
                    lines.append(f"    {i}. Position {orf['start']}-{orf['end']} ({orf['length']} bp)")
        
        # Restriction sites
        lines.append(f"\nRestriction Sites: {len(result['restriction_sites'])} enzyme(s)")
        for enzyme, positions in sorted(result['restriction_sites'].items()):
            lines.append(f"  {enzyme}: {len(positions)} site(s) at {positions}")
        
        lines.append("\n" + "="*70)
        
        return '\n'.join(lines)

# Example usage
fasta_input = """>NM_007294 BRCA1 gene fragment
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAG
TGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTT
GCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAA
"""

analyzer = GeneAnalyzer(fasta_input)
report = analyzer.generate_report('NM_007294', min_orf_length=30)
print(report)
```

---

## 📝 Practice Tasks (Day 15-16)

### Basic Exercises

1. **Simple ORF Finder**: Write a function that finds the first ORF in a sequence.

2. **Motif Counter**: Count occurrences of a specific motif in a sequence.

3. **Translation**: Implement basic DNA to protein translation.

4. **Sequence Slicer**: Extract a subsequence given start and end coordinates.

5. **GC Window**: Calculate GC content in sliding windows.

### Intermediate Challenges

6. **Multi-Frame ORF**: Find ORFs in all three forward reading frames.

7. **Restriction Mapper**: Create a restriction map showing all cut sites.

8. **Promoter Finder**: Search for TATA boxes and other promoter elements.

9. **Codon Usage**: Calculate codon usage frequency for all codons in ORFs.

10. **Export Function**: Export analysis results to CSV or JSON format.

### Advanced Challenges

11. **Six-Frame Translation**: Implement complete six-frame translation with ORF detection.

12. **Overlapping ORF Detection**: Find and report overlapping ORFs on same or different strands.

13. **Statistical Analysis**: Compare codon usage between multiple sequences and generate statistics.

14. **Visualization**: Create ASCII visualization of ORF locations, restriction sites, and GC content.

15. **Command-Line Tool**: Build a complete CLI tool with argument parsing for batch analysis.

---

## 💡 Key Takeaways

✓ ORFs start with ATG and end with stop codons (TAA, TAG, TGA)  
✓ Six reading frames: three forward, three reverse  
✓ Regex patterns enable flexible motif searching  
✓ Restriction enzymes cut at specific palindromic sequences  
✓ Translation uses genetic code (codon → amino acid mapping)  
✓ Reverse complement analysis finds antisense features  
✓ Validation prevents errors from propagating  
✓ Modular design enables code reuse and testing  
✓ Comprehensive reports provide actionable insights  
✓ Edge cases matter: overlapping ORFs, incomplete codons  
✓ Use dictionaries and data structures to organize results  
✓ Build incrementally: parse → analyze → report  

**Next**: Advanced topics (OOP, Regex, File formats)
