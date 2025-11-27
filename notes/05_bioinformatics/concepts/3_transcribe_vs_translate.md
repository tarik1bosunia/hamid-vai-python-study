# Transcription vs Translation - The Central Dogma

## Introduction

The **Central Dogma of Molecular Biology** describes the flow of genetic information in biological systems:

```
DNA → (Transcription) → RNA → (Translation) → Protein
```

This fundamental principle explains how genetic instructions stored in DNA are converted into functional proteins that perform cellular work. Understanding transcription and translation is essential for:

- Gene expression analysis
- Drug target identification
- Genetic engineering and CRISPR
- Disease mechanism research
- Protein production in biotechnology

**Key Difference:**
- **Transcription**: DNA → RNA (copying genetic code)
- **Translation**: RNA → Protein (decoding genetic code)

---

## Part 1: Transcription (DNA → RNA)

### What is Transcription?

**Definition**: The process of synthesizing an RNA molecule from a DNA template.

**In Nature:**
- Enzyme: **RNA Polymerase**
- Location: Nucleus (eukaryotes), cytoplasm (prokaryotes)
- Product: Various RNA types (mRNA, tRNA, rRNA, etc.)
- Direction: 5' → 3' synthesis

### DNA vs RNA Nucleotides

| Feature | DNA | RNA |
|---------|-----|-----|
| **Bases** | A, T, G, C | A, U, G, C |
| **Sugar** | Deoxyribose | Ribose |
| **Strands** | Double-stranded | Single-stranded |
| **Stability** | More stable | Less stable |

**Key Change**: Thymine (T) in DNA is replaced by Uracil (U) in RNA.

### Transcription Rules

```
DNA Template:  3'- A T G C G T A A A -5'
                   ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
RNA Transcript: 5'- U A C G C A U U U -3'
```

**Base Pairing Rules:**
- DNA A → RNA U
- DNA T → RNA A
- DNA G → RNA C
- DNA C → RNA G

### Implementation in Python

```python
def transcribe(dna: str) -> str:
    """
    Transcribe DNA to RNA.
    
    Args:
        dna: DNA sequence (5' to 3')
        
    Returns:
        RNA sequence (5' to 3')
    """
    # Replace T with U
    rna = dna.replace('T', 'U')
    return rna

# Example
dna = "ATGCGTAAACCGATGGGC"
rna = transcribe(dna)
print(f"DNA: {dna}")
print(f"RNA: {rna}")
# Output:
# DNA: ATGCGTAAACCGATGGGC
# RNA: AUGCGUAAACCGAUGGGC
```

### Using BioPython

```python
from Bio.Seq import Seq

def transcribe_biopython(dna: str) -> str:
    """Transcribe DNA to RNA using BioPython."""
    dna_seq = Seq(dna)
    rna_seq = dna_seq.transcribe()
    return str(rna_seq)

# Example
dna = "ATGCGTAAACCGATGGGC"
rna = transcribe_biopython(dna)
print(rna)  # AUGCGUAAACCGAUGGGC
```

### Reverse Transcription (RNA → DNA)

```python
def reverse_transcribe(rna: str) -> str:
    """
    Convert RNA back to DNA (reverse transcription).
    Used by retroviruses like HIV.
    """
    dna = rna.replace('U', 'T')
    return dna

# Example
rna = "AUGCGUAAACCGAUGGGC"
dna = reverse_transcribe(rna)
print(dna)  # ATGCGTAAACCGATGGGC
```

---

## Part 2: Translation (RNA → Protein)

### What is Translation?

**Definition**: The process of synthesizing a protein from an mRNA template.

**In Nature:**
- Machinery: **Ribosomes** (rRNA + proteins)
- Adapter: **tRNA** (transfer RNA) brings amino acids
- Location: Cytoplasm (all cells)
- Product: **Polypeptide chain** (protein)
- Direction: 5' → 3' on mRNA

### The Genetic Code

Translation reads mRNA in **triplets (codons)**. Each codon specifies one amino acid.

```
mRNA: AUG GGC UUU UAA
      ↓   ↓   ↓   ↓
Protein: Met Gly Phe STOP
```

**Important Codons:**
- **Start codon**: AUG (codes for Methionine)
- **Stop codons**: UAA, UAG, UGA (no amino acid)

### Standard Genetic Code Table

| Codon | Amino Acid | 1-Letter | Type |
|-------|------------|----------|------|
| AUG | Methionine | M | Start |
| UUU, UUC | Phenylalanine | F | - |
| UUA, UUG, CUU, CUC, CUA, CUG | Leucine | L | - |
| UCU, UCC, UCA, UCG | Serine | S | - |
| UAU, UAC | Tyrosine | Y | - |
| UAA, UAG, UGA | STOP | * | Stop |
| UGU, UGC | Cysteine | C | - |
| UGG | Tryptophan | W | - |
| CGU, CGC, CGA, CGG | Arginine | R | - |
| GGU, GGC, GGA, GGG | Glycine | G | - |

(Full table has 64 codons → 20 amino acids + stop)

### Translation Implementation

```python
def translate(rna: str) -> str:
    """
    Translate RNA sequence to protein.
    
    Args:
        rna: RNA sequence (must start with AUG)
        
    Returns:
        Protein sequence (1-letter codes)
    """
    # Standard genetic code
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
        'UAC': 'Y', 'UGU': 'C', 'UGC': 'C', 'UGG': 'W', 'CUU': 'L',
        'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P',
        'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q',
        'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'ACU': 'T', 'ACC': 'T',
        'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K',
        'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A',
        'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G',
        'GGG': 'G', 'UAA': '*', 'UAG': '*', 'UGA': '*'
    }
    
    protein = []
    
    # Read codons (3 bases at a time)
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        
        if codon in codon_table:
            amino_acid = codon_table[codon]
            
            # Stop at stop codon
            if amino_acid == '*':
                break
            
            protein.append(amino_acid)
        else:
            protein.append('X')  # Unknown codon
    
    return ''.join(protein)

# Example
rna = "AUGGGCUUUUAA"
protein = translate(rna)
print(f"RNA:     {rna}")
print(f"Protein: {protein}")
# Output:
# RNA:     AUGGGCUUUUAA
# Protein: MGF
```

### Using BioPython for Translation

```python
from Bio.Seq import Seq

def translate_biopython(rna: str) -> str:
    """Translate RNA to protein using BioPython."""
    rna_seq = Seq(rna)
    protein = rna_seq.translate()
    return str(protein)

# Example
rna = "AUGGGCUUUUAA"
protein = translate_biopython(rna)
print(protein)  # MGF

# BioPython also stops at stop codons automatically
```

---

## Complete Pipeline: DNA → RNA → Protein

### Full Workflow Implementation

```python
from Bio.Seq import Seq

def central_dogma_pipeline(dna: str, show_steps: bool = True):
    """
    Complete DNA → RNA → Protein pipeline.
    
    Args:
        dna: DNA sequence (5' to 3')
        show_steps: Print intermediate steps
        
    Returns:
        Dictionary with RNA and protein sequences
    """
    # Step 1: Transcription
    dna_seq = Seq(dna)
    rna_seq = dna_seq.transcribe()
    
    # Step 2: Translation
    protein_seq = rna_seq.translate()
    
    if show_steps:
        print("=" * 60)
        print("CENTRAL DOGMA PIPELINE")
        print("=" * 60)
        print(f"DNA:     {dna_seq}")
        print(f"RNA:     {rna_seq}")
        print(f"Protein: {protein_seq}")
        print(f"\nProtein length: {len(protein_seq)} amino acids")
        print(f"DNA length: {len(dna_seq)} bp")
        print(f"RNA length: {len(rna_seq)} bp")
        print("=" * 60)
    
    return {
        'dna': str(dna_seq),
        'rna': str(rna_seq),
        'protein': str(protein_seq)
    }

# Example: Insulin signal peptide
dna = "ATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAA"
result = central_dogma_pipeline(dna)
```

### Translate All 6 Reading Frames

```python
def translate_all_frames(dna: str) -> dict:
    """
    Translate DNA in all 6 reading frames.
    Important for gene prediction and ORF analysis.
    """
    from Bio.Seq import Seq
    
    results = {}
    dna_seq = Seq(dna)
    rev_comp = dna_seq.reverse_complement()
    
    # Forward frames (0, 1, 2)
    for frame in range(3):
        frame_seq = dna_seq[frame:]
        protein = frame_seq.translate()
        results[f'forward_{frame+1}'] = str(protein)
    
    # Reverse frames (0, 1, 2)
    for frame in range(3):
        frame_seq = rev_comp[frame:]
        protein = frame_seq.translate()
        results[f'reverse_{frame+1}'] = str(protein)
    
    return results

# Example
dna = "ATGGGCTTTAGATAG"
translations = translate_all_frames(dna)

for frame, protein in translations.items():
    print(f"{frame:12s}: {protein}")
```

---

## Bioinformatics Applications

### 1. Finding Coding Sequences (CDS)

```python
def find_coding_sequences(dna: str, min_length: int = 30) -> list:
    """
    Find potential coding sequences (ORFs with translation).
    
    Returns:
        List of dicts with ORF info and translated protein
    """
    from Bio.Seq import Seq
    
    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}
    
    cds_list = []
    i = 0
    
    while i < len(dna) - 2:
        if dna[i:i+3] == start_codon:
            j = i + 3
            
            # Find stop codon
            while j < len(dna) - 2 and dna[j:j+3] not in stop_codons:
                j += 3
            
            if j < len(dna) - 2:
                orf = dna[i:j+3]
                
                if len(orf) >= min_length:
                    # Translate
                    protein = str(Seq(orf).translate())
                    
                    cds_list.append({
                        'start': i + 1,
                        'end': j + 3,
                        'length_bp': len(orf),
                        'length_aa': len(protein) - 1,  # Exclude stop
                        'dna': orf,
                        'protein': protein
                    })
                
                i = j + 3
                continue
        
        i += 1
    
    return cds_list

# Example
genome = "GCGATGCGTAAACCGATGGGCTTTTGATAGCCCATGAAATAAGGCCC"
cds = find_coding_sequences(genome, min_length=15)

for i, seq in enumerate(cds, 1):
    print(f"\nCDS {i}:")
    print(f"  Position: {seq['start']}-{seq['end']}")
    print(f"  DNA: {seq['dna']}")
    print(f"  Protein: {seq['protein']}")
```

### 2. Codon Usage Analysis

```python
def codon_usage(rna: str) -> dict:
    """
    Calculate codon usage frequency.
    Different organisms prefer different synonymous codons.
    """
    from collections import Counter
    
    codons = [rna[i:i+3] for i in range(0, len(rna) - 2, 3)]
    codon_counts = Counter(codons)
    
    # Calculate frequencies
    total = sum(codon_counts.values())
    codon_freq = {codon: count / total * 100 
                  for codon, count in codon_counts.items()}
    
    return {
        'counts': dict(codon_counts),
        'frequencies': codon_freq,
        'total_codons': total
    }

# Example
rna = "AUGGGCUUUUAAAUGCCCGGGUAG"
usage = codon_usage(rna)
print("Codon Usage:")
for codon, freq in usage['frequencies'].items():
    print(f"  {codon}: {freq:.1f}%")
```

### 3. Detecting Mutations and Their Effects

```python
def compare_translations(original_dna: str, mutated_dna: str):
    """
    Compare original and mutated DNA to see effect on protein.
    Classify mutation type.
    """
    from Bio.Seq import Seq
    
    orig_protein = str(Seq(original_dna).translate())
    mut_protein = str(Seq(mutated_dna).translate())
    
    # Find differences
    differences = []
    for i, (orig_aa, mut_aa) in enumerate(zip(orig_protein, mut_protein)):
        if orig_aa != mut_aa:
            differences.append({
                'position': i + 1,
                'original': orig_aa,
                'mutated': mut_aa
            })
    
    # Classify mutation
    if len(orig_protein) != len(mut_protein):
        mutation_type = "Frameshift"
    elif not differences:
        mutation_type = "Silent (synonymous)"
    elif any(d['mutated'] == '*' for d in differences):
        mutation_type = "Nonsense (introduces stop)"
    else:
        mutation_type = "Missense (amino acid change)"
    
    return {
        'original_protein': orig_protein,
        'mutated_protein': mut_protein,
        'mutation_type': mutation_type,
        'differences': differences
    }

# Example: Point mutation
original = "ATGGGCTTTTAA"
mutated  = "ATGAGCTTTTAA"  # G→A at position 4

result = compare_translations(original, mutated)
print(f"Mutation type: {result['mutation_type']}")
print(f"Original: {result['original_protein']}")
print(f"Mutated:  {result['mutated_protein']}")
```

### 4. Back-Translation (Protein → DNA)

```python
def back_translate(protein: str, codon_preference: dict = None) -> str:
    """
    Convert protein back to DNA (reverse translation).
    Multiple codons can encode same amino acid.
    
    Args:
        protein: Protein sequence (1-letter codes)
        codon_preference: Dict of preferred codons for each amino acid
    """
    # Default: use most common codon in humans
    if codon_preference is None:
        codon_preference = {
            'M': 'ATG', 'F': 'TTC', 'L': 'CTG', 'S': 'AGC', 'Y': 'TAC',
            'C': 'TGC', 'W': 'TGG', 'P': 'CCC', 'H': 'CAC', 'Q': 'CAG',
            'R': 'CGC', 'I': 'ATC', 'T': 'ACC', 'N': 'AAC', 'K': 'AAG',
            'V': 'GTG', 'A': 'GCC', 'D': 'GAC', 'E': 'GAG', 'G': 'GGC',
            '*': 'TAA'
        }
    
    dna = ''.join(codon_preference.get(aa, 'NNN') for aa in protein)
    return dna

# Example
protein = "MGFYK"
dna = back_translate(protein)
print(f"Protein: {protein}")
print(f"DNA:     {dna}")
# Output: ATGGGCTTCTACAAG (using preferred codons)
```

### 5. Transcriptome Analysis

```python
def analyze_transcriptome(sequences: dict) -> dict:
    """
    Analyze multiple transcripts (e.g., from RNA-seq).
    
    Args:
        sequences: Dict of {gene_id: rna_sequence}
        
    Returns:
        Statistics about the transcriptome
    """
    from Bio.Seq import Seq
    
    stats = {
        'total_genes': len(sequences),
        'total_bases': 0,
        'coding_genes': 0,
        'avg_length': 0,
        'proteins': {}
    }
    
    lengths = []
    
    for gene_id, rna in sequences.items():
        lengths.append(len(rna))
        stats['total_bases'] += len(rna)
        
        # Check if it has ORF
        if rna.startswith('AUG'):
            protein = str(Seq(rna).translate())
            if '*' in protein:  # Has stop codon
                stats['coding_genes'] += 1
                stats['proteins'][gene_id] = protein.split('*')[0]  # Up to first stop
    
    stats['avg_length'] = stats['total_bases'] / stats['total_genes'] if stats['total_genes'] > 0 else 0
    stats['coding_percentage'] = stats['coding_genes'] / stats['total_genes'] * 100 if stats['total_genes'] > 0 else 0
    
    return stats

# Example
transcripts = {
    'gene1': 'AUGGGCUUUUAA',
    'gene2': 'AUGCCCAAAUAG',
    'gene3': 'GGGCCCUUUAAA'  # No start codon
}

stats = analyze_transcriptome(transcripts)
print(f"Total genes: {stats['total_genes']}")
print(f"Coding genes: {stats['coding_genes']} ({stats['coding_percentage']:.1f}%)")
print(f"Proteins: {len(stats['proteins'])}")
```

---

## Practice Exercises

### Basic Level

1. **Transcribe DNA**: Transcribe this DNA to RNA: `ATGCGTAAACCCGGG`

2. **Translate RNA**: Translate this RNA to protein: `AUGGGCUUUUGA`

3. **Count Codons**: Count how many codons are in a 150 bp coding sequence.

4. **Find Stop**: Write a function to find the first stop codon in an RNA sequence.

5. **Reverse Transcribe**: Convert RNA back to DNA: `AUGCCCUUUAAA`

### Intermediate Level

6. **Complete Pipeline**: Implement DNA → RNA → Protein for multiple sequences.

7. **All Frames**: Translate DNA in all 6 reading frames and find longest protein.

8. **Codon Table**: Create a function that prints the full genetic code table.

9. **Mutation Effect**: Compare original and mutated sequences, classify mutation type.

10. **GC in Codons**: Calculate GC content separately for position 1, 2, 3 of codons.

### Advanced Level

11. **Alternative Genetic Codes**: Implement translation using mitochondrial genetic code (differs from standard).

12. **Kozak Sequence**: Detect Kozak consensus sequences around start codons (important for eukaryotic translation).

13. **Shine-Dalgarno**: Find ribosome binding sites (AGGAGGU) in bacterial mRNA.

14. **Codon Optimization**: Optimize a protein sequence for expression in a specific organism (E. coli, yeast, human).

15. **UTR Analysis**: Parse mRNA with 5'UTR, CDS, and 3'UTR; extract and analyze each region separately.

---

## Key Takeaways

1. **Central Dogma**: DNA → RNA → Protein is the fundamental information flow in biology.

2. **Transcription**: DNA to RNA, T→U substitution only, same genetic information.

3. **Translation**: RNA to protein, 3 bases (codon) → 1 amino acid, information decoded.

4. **Start Codon**: AUG marks beginning of translation (encodes Methionine).

5. **Stop Codons**: UAA, UAG, UGA terminate translation (no amino acid).

6. **Reading Frames**: 6 possible (3 forward, 3 reverse) - gene prediction checks all.

7. **Genetic Code**: Universal (mostly), 64 codons → 20 amino acids (degeneracy/redundancy).

8. **Mutations**: Can be silent (same AA), missense (different AA), nonsense (stop), or frameshift.

9. **BioPython**: Use `.transcribe()` and `.translate()` methods for production code.

10. **Applications**: Gene finding, mutation analysis, protein prediction, synthetic biology.

---

## References

- **NCBI Genetic Codes**: https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
- **BioPython Tutorial**: http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec21
- Crick, F. (1970). Central dogma of molecular biology. *Nature*.
- **ExPASy Translate Tool**: https://web.expasy.org/translate/

---

**Next Steps**: Learn about gene structure (exons, introns, UTRs) and how eukaryotic genes are more complex than simple ORFs.
