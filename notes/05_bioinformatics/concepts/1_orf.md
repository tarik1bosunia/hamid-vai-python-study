# Open Reading Frames (ORFs) - Complete Guide

## Introduction

An **Open Reading Frame (ORF)** is a continuous stretch of DNA codons that begins with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA) without any intermediate stop codons. ORFs are potential protein-coding regions in a genome and are fundamental to gene prediction and genome annotation.

**Why ORFs Matter:**
- Gene prediction in newly sequenced genomes
- Identifying coding sequences in viral genomes
- Detecting frameshift mutations
- Predicting protein-coding potential
- Comparative genomics studies

---

## Core Concepts

### 1. DNA Reading Frames

DNA can be read in **6 different reading frames**:
- 3 forward frames (starting at positions 0, 1, 2)
- 3 reverse frames (reverse complement, positions 0, 1, 2)

```
DNA: ATGCGTAAATAG
Frame 0: ATG CGT AAA TAG (start...codons...stop)
Frame 1:  TGC GTA AAT AG  (shifted by 1)
Frame 2:   GCG TAA ATA G  (shifted by 2)
```

### 2. Start and Stop Codons

**Start Codon:**
- `ATG` (Methionine in eukaryotes)
- Alternative: `GTG`, `TTG` in some prokaryotes

**Stop Codons:**
- `TAA` (Ochre)
- `TAG` (Amber)
- `TGA` (Opal/Umber)

### 3. ORF Classification

| Type | Description | Significance |
|------|-------------|--------------|
| **Complete ORF** | Has both start and stop codons | Likely coding sequence |
| **Partial ORF** | Missing start or stop | May extend beyond sequence boundary |
| **Short ORF** | <300 bp (100 codons) | Usually non-coding |
| **Long ORF** | >300 bp | Strong candidate for gene |

---

## Finding ORFs - Implementation

### Basic ORF Finder Function

```python
def find_orfs(seq: str, min_len_codons: int = 50) -> list[tuple[int, int, str]]:
    """
    Find all ORFs in a DNA sequence.
    
    Args:
        seq: DNA sequence string (uppercase)
        min_len_codons: Minimum ORF length in codons
        
    Returns:
        List of tuples: (start_pos, end_pos, orf_sequence)
        Positions are 1-based, end-inclusive
    """
    stops = {"TAA", "TAG", "TGA"}
    orfs = []
    n = len(seq)
    i = 0
    
    while i < n - 2:
        codon = seq[i:i+3]
        
        # Look for start codon
        if codon == "ATG":
            j = i + 3
            
            # Scan until stop codon or end of sequence
            while j < n - 2 and seq[j:j+3] not in stops:
                j += 3
            
            # If we found a stop codon
            if j < n - 2:
                length_codons = (j - i) // 3
                
                if length_codons >= min_len_codons:
                    orfs.append((i + 1, j + 3, seq[i:j+3]))
                
                i = j + 3  # Continue after stop codon
                continue
        
        i += 1
    
    return orfs
```

### How It Works

**Step 1: Initialize**
```python
stops = {"TAA", "TAG", "TGA"}  # Stop codon set
orfs = []                       # Results collection
i = 0                           # Current position
```

**Step 2: Scan for Start Codons**
```python
while i < n - 2:
    codon = seq[i:i+3]
    if codon == "ATG":  # Found start
```

**Step 3: Find Corresponding Stop**
```python
j = i + 3  # Position after start
while j < n - 2 and seq[j:j+3] not in stops:
    j += 3  # Move by codon (3 bases)
```

**Step 4: Validate and Store**
```python
if j < n - 2:  # Stop codon found
    length_codons = (j - i) // 3
    if length_codons >= min_len_codons:
        orfs.append((i + 1, j + 3, seq[i:j+3]))
```

---

## Advanced ORF Analysis

### Find All 6 Reading Frames

```python
def reverse_complement(seq: str) -> str:
    """Return reverse complement of DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(complement[base] for base in reversed(seq))

def find_all_orfs(seq: str, min_len: int = 100) -> dict:
    """
    Find ORFs in all 6 reading frames.
    
    Returns:
        Dictionary with frame names as keys and ORF lists as values
    """
    results = {}
    rev_seq = reverse_complement(seq)
    
    # Forward frames
    for frame in range(3):
        orfs = find_orfs(seq[frame:], min_len)
        # Adjust positions for frame offset
        adjusted_orfs = [(start + frame, end + frame, orf_seq) 
                         for start, end, orf_seq in orfs]
        results[f'forward_{frame+1}'] = adjusted_orfs
    
    # Reverse frames
    for frame in range(3):
        orfs = find_orfs(rev_seq[frame:], min_len)
        # Adjust positions for reverse strand
        adjusted_orfs = [(len(seq) - end - frame + 1, 
                          len(seq) - start - frame + 1, 
                          orf_seq) 
                         for start, end, orf_seq in orfs]
        results[f'reverse_{frame+1}'] = adjusted_orfs
    
    return results
```

### ORF Translation

```python
def translate_orf(orf_seq: str) -> str:
    """
    Translate ORF DNA sequence to protein.
    """
    codon_table = {
        'ATG': 'M', 'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y',
        'TAC': 'Y', 'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L',
        'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P',
        'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q',
        'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ACT': 'T', 'ACC': 'T',
        'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
        'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
        'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
        'GGG': 'G', 'TAA': '*', 'TAG': '*', 'TGA': '*'
    }
    
    protein = []
    for i in range(0, len(orf_seq), 3):
        codon = orf_seq[i:i+3]
        if len(codon) == 3:
            protein.append(codon_table.get(codon, 'X'))
    
    return ''.join(protein)
```

---

## Bioinformatics Applications

### 1. Gene Prediction in Prokaryotic Genomes

```python
def predict_genes_prokaryote(genome: str, min_gene_length: int = 300) -> list:
    """
    Simple gene prediction for bacterial genomes.
    Bacteria lack introns, so long ORFs are likely genes.
    """
    all_orfs = find_all_orfs(genome, min_len=min_gene_length // 3)
    
    genes = []
    for frame, orfs in all_orfs.items():
        for start, end, seq in orfs:
            protein = translate_orf(seq)
            genes.append({
                'frame': frame,
                'start': start,
                'end': end,
                'length_bp': end - start + 1,
                'length_aa': len(protein) - 1,  # Exclude stop
                'sequence': seq,
                'protein': protein
            })
    
    # Sort by length (longer ORFs more likely to be genes)
    genes.sort(key=lambda x: x['length_bp'], reverse=True)
    return genes

# Example usage
genome = "ATGCGTAAACCCATGGGCTTTTGATAGCCCATGAAATAA"
genes = predict_genes_prokaryote(genome, min_gene_length=15)

for i, gene in enumerate(genes, 1):
    print(f"Gene {i}:")
    print(f"  Position: {gene['start']}-{gene['end']} ({gene['frame']})")
    print(f"  Length: {gene['length_bp']} bp, {gene['length_aa']} aa")
    print(f"  Protein: {gene['protein']}")
    print()
```

### 2. Detecting Frameshift Mutations

```python
def detect_frameshifts(original: str, mutated: str) -> dict:
    """
    Detect frameshift mutations by comparing ORFs.
    """
    orig_orfs = find_orfs(original, min_len_codons=10)
    mut_orfs = find_orfs(mutated, min_len_codons=10)
    
    # Compare longest ORF in each
    orig_longest = max(orig_orfs, key=lambda x: len(x[2])) if orig_orfs else None
    mut_longest = max(mut_orfs, key=lambda x: len(x[2])) if mut_orfs else None
    
    if not orig_longest or not mut_longest:
        return {'frameshift': True, 'reason': 'ORF lost'}
    
    orig_len = len(orig_longest[2])
    mut_len = len(mut_longest[2])
    
    # Significant length change indicates frameshift
    if abs(orig_len - mut_len) > 9:  # >3 codons different
        return {
            'frameshift': True,
            'original_length': orig_len,
            'mutated_length': mut_len,
            'difference': mut_len - orig_len
        }
    
    return {'frameshift': False}

# Example: Insertion causes frameshift
original = "ATGCGTAAACCCGGGTAG"
mutated  = "ATGCGTAACCCGGGTAG"  # Missing one 'A'

result = detect_frameshifts(original, mutated)
print(result)
# Output: {'frameshift': True, 'original_length': 18, 'mutated_length': 9, ...}
```

### 3. Viral Genome Analysis

```python
def analyze_viral_genome(genome: str) -> dict:
    """
    Analyze small viral genome for ORFs.
    Viruses often have overlapping genes and use all reading frames.
    """
    all_orfs = find_all_orfs(genome, min_len=20)  # Small min for viruses
    
    stats = {
        'genome_length': len(genome),
        'total_orfs': sum(len(orfs) for orfs in all_orfs.values()),
        'frames': {},
        'overlapping_orfs': []
    }
    
    # Analyze each frame
    for frame, orfs in all_orfs.items():
        stats['frames'][frame] = {
            'count': len(orfs),
            'total_length': sum(end - start + 1 for start, end, _ in orfs),
            'avg_length': sum(end - start + 1 for start, end, _ in orfs) / len(orfs) if orfs else 0
        }
    
    # Check for overlapping ORFs (common in viruses)
    all_orf_list = [(frame, start, end) for frame, orfs in all_orfs.items() 
                    for start, end, _ in orfs]
    all_orf_list.sort(key=lambda x: x[1])  # Sort by start position
    
    for i in range(len(all_orf_list) - 1):
        frame1, start1, end1 = all_orf_list[i]
        frame2, start2, end2 = all_orf_list[i + 1]
        
        if start2 < end1:  # Overlap detected
            overlap = end1 - start2 + 1
            stats['overlapping_orfs'].append({
                'orf1': f"{frame1} ({start1}-{end1})",
                'orf2': f"{frame2} ({start2}-{end2})",
                'overlap_bp': overlap
            })
    
    return stats
```

### 4. Comparing ORF Content Between Species

```python
def compare_orf_content(seq1: str, seq2: str, species1: str, species2: str):
    """
    Compare ORF characteristics between two sequences.
    """
    orfs1 = find_orfs(seq1, min_len_codons=50)
    orfs2 = find_orfs(seq2, min_len_codons=50)
    
    comparison = {
        species1: {
            'total_orfs': len(orfs1),
            'total_coding_bp': sum(len(seq) for _, _, seq in orfs1),
            'avg_orf_length': sum(len(seq) for _, _, seq in orfs1) / len(orfs1) if orfs1 else 0,
            'coding_density': sum(len(seq) for _, _, seq in orfs1) / len(seq1) * 100
        },
        species2: {
            'total_orfs': len(orfs2),
            'total_coding_bp': sum(len(seq) for _, _, seq in orfs2),
            'avg_orf_length': sum(len(seq) for _, _, seq in orfs2) / len(orfs2) if orfs2 else 0,
            'coding_density': sum(len(seq) for _, _, seq in orfs2) / len(seq2) * 100
        }
    }
    
    return comparison

# Example
bacteria = "ATGCGTAAACCGATGATGGGCTTTTGATAG" * 10
eukaryote = "ATGCGTCCCAAACCGATGGGCTTTGCCATAG" * 8

result = compare_orf_content(bacteria, eukaryote, "E.coli", "H.sapiens")
for species, stats in result.items():
    print(f"{species}:")
    print(f"  ORFs: {stats['total_orfs']}")
    print(f"  Coding density: {stats['coding_density']:.2f}%")
    print(f"  Average ORF length: {stats['avg_orf_length']:.1f} bp")
```

---

## Practice Exercises

### Basic Level

1. **Find All ORFs**: Write code to find all ORFs (minimum 30 codons) in this sequence:
   ```python
   seq = "GCGATGCGTAAACCGATGGGCTTTTGATAGCCCATGAAATAA"
   ```

2. **Count Start Codons**: Count how many ATG codons appear in a 1000 bp random sequence.

3. **Longest ORF**: Find the single longest ORF in a sequence.

4. **ORF Statistics**: Calculate min, max, mean, and median ORF lengths.

5. **Partial ORFs**: Modify the function to detect ORFs that start at position 0 (no start codon at beginning).

### Intermediate Level

6. **All 6 Frames**: Implement complete 6-frame ORF analysis including reverse complement.

7. **GC Content**: Calculate GC content for each ORF found and identify GC-rich genes.

8. **Nested ORFs**: Find cases where one ORF is completely contained within another ORF.

9. **Translation**: Translate all ORFs to proteins and export to FASTA format.

10. **Overlapping Detection**: Identify all pairs of overlapping ORFs (common in viral genomes).

### Advanced Level

11. **Alternative Start Codons**: Extend ORF finder to recognize GTG and TTG as alternative starts (prokaryotes).

12. **Kozak Sequence**: Detect Kozak consensus sequences around ATG start codons (eukaryotes).

13. **Shine-Dalgarno**: Find ribosome binding sites (AGGAGGU) upstream of ORFs in bacterial sequences.

14. **Codon Usage Bias**: Calculate codon adaptation index (CAI) for each ORF.

15. **Gene Overlap Analysis**: Analyze overlapping genes in a viral genome and visualize with matplotlib.

---

## Key Takeaways

1. **ORF Definition**: Continuous sequence from start codon (ATG) to stop codon (TAA/TAG/TGA) without interruption.

2. **Reading Frames**: DNA has 6 possible reading frames (3 forward, 3 reverse) - all must be checked.

3. **Length Matters**: Longer ORFs (>300 bp) are more likely to be real genes; short ones are often random.

4. **Prokaryotes vs Eukaryotes**: 
   - Prokaryotes: Long ORFs = genes (no introns)
   - Eukaryotes: Need additional evidence (splicing, promoters, etc.)

5. **Algorithm Efficiency**: Scanning approach is O(n), acceptable for sequences up to several Mb.

6. **Bioinformatics Tools**: Real tools like NCBI ORF Finder, Glimmer, GeneMark use ORF detection + machine learning.

7. **Overlapping Genes**: Common in viruses and bacteria - maximize coding capacity in small genomes.

8. **Frameshift Mutations**: Insertions/deletions not divisible by 3 destroy ORF structure downstream.

---

## References and Further Reading

- **NCBI ORF Finder**: https://www.ncbi.nlm.nih.gov/orffinder/
- **Glimmer** (Prokaryotic gene prediction): http://ccb.jhu.edu/software/glimmer/
- **GeneMark**: http://exon.gatech.edu/GeneMark/
- **Sequence Ontology**: http://www.sequenceontology.org/
- Salzberg, S. L. et al. (1998). Microbial gene identification using interpolated Markov models. *Nucleic Acids Research*.

---

**Next Steps**: Explore the FASTA file format and learn to parse genome sequences for ORF analysis at scale.
