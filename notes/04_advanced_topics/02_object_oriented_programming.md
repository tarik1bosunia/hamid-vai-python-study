# Day 18: Object-Oriented Programming for Bioinformatics

## 🧬 Build Reusable Biological Classes

Object-Oriented Programming (OOP) enables you to create **reusable, modular code** for bioinformatics. Design classes for sequences, genes, proteins, and analyses that encapsulate data and behavior together - essential for large-scale computational biology projects.

### Why OOP for Bioinformatics?

- **Data Encapsulation**: Bundle sequence data with methods (e.g., `dna.transcribe()`)
- **Code Reuse**: Write once, use many times (DRY principle)
- **Inheritance**: Create specialized classes (DNA → Gene → Transcript)
- **Maintainability**: Easier to debug and extend
- **Real Libraries**: BioPython, pandas, scikit-bio all use OOP

---

## 🎯 Learning Objectives

By the end of this guide, you will:

✓ Understand classes, objects, and instances  
✓ Create biological sequence classes  
✓ Implement methods for sequence operations  
✓ Use inheritance for specialized sequences  
✓ Apply encapsulation and data protection  
✓ Build complete gene/protein analysis tools  
✓ Design professional bioinformatics APIs  

---

## 🧩 Part 1: Class Basics

### Creating Your First Class

```python
class DNASequence:
    """Represents a DNA sequence"""
    
    def __init__(self, sequence):
        """Constructor - called when creating new instance"""
        self.sequence = sequence.upper()
    
    def get_length(self):
        """Return sequence length"""
        return len(self.sequence)
    
    def get_gc_content(self):
        """Calculate GC content percentage"""
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        return (g_count + c_count) / len(self.sequence) * 100

# Create instances (objects)
seq1 = DNASequence("ATCGATCG")
seq2 = DNASequence("gctagcta")

print(f"Sequence 1: {seq1.sequence}, Length: {seq1.get_length()}")
print(f"GC content: {seq1.get_gc_content():.2f}%")

print(f"Sequence 2: {seq2.sequence}, Length: {seq2.get_length()}")
```

### The __init__ Constructor

```python
class Gene:
    """Represents a gene with metadata"""
    
    def __init__(self, gene_id, name, sequence, chromosome=""):
        """
        Initialize gene
        
        Parameters:
            gene_id: Unique identifier (e.g., 'ENSG00000139618')
            name: Gene symbol (e.g., 'BRCA2')
            sequence: DNA sequence
            chromosome: Chromosome location (optional)
        """
        self.gene_id = gene_id
        self.name = name
        self.sequence = sequence.upper()
        self.chromosome = chromosome
    
    def __str__(self):
        """String representation for print()"""
        return f"Gene({self.name}, {self.gene_id}, {len(self.sequence)} bp)"
    
    def __repr__(self):
        """Official representation for debugging"""
        return f"Gene(gene_id='{self.gene_id}', name='{self.name}')"

# Create gene instance
brca2 = Gene("ENSG00000139618", "BRCA2", "ATCGATCGATCG", "chr13")

print(brca2)  # Uses __str__
print(repr(brca2))  # Uses __repr__
print(f"Chromosome: {brca2.chromosome}")
```

### Instance vs Class Variables

```python
class Sequence:
    """Biological sequence with class-level statistics"""
    
    # Class variable (shared by all instances)
    total_sequences = 0
    valid_bases = set('ATCGN')
    
    def __init__(self, sequence, seq_id=""):
        # Instance variables (unique to each instance)
        self.sequence = sequence.upper()
        self.seq_id = seq_id
        self.length = len(sequence)
        
        # Increment class variable
        Sequence.total_sequences += 1
    
    @classmethod
    def get_total_count(cls):
        """Class method - operates on class, not instance"""
        return cls.total_sequences
    
    @staticmethod
    def is_valid_base(base):
        """Static method - doesn't need class or instance"""
        return base.upper() in Sequence.valid_bases

# Test
seq1 = Sequence("ATCG", "seq1")
seq2 = Sequence("GCTA", "seq2")
seq3 = Sequence("TAGC", "seq3")

print(f"Total sequences created: {Sequence.get_total_count()}")
print(f"Is 'A' valid? {Sequence.is_valid_base('A')}")
print(f"Is 'X' valid? {Sequence.is_valid_base('X')}")
```

---

## 🧩 Part 2: Methods & Functionality

### DNA Sequence Class

```python
class DNA:
    """Complete DNA sequence class"""
    
    def __init__(self, sequence, seq_id=""):
        self.sequence = sequence.upper()
        self.seq_id = seq_id
    
    def __len__(self):
        """Enable len(dna)"""
        return len(self.sequence)
    
    def __getitem__(self, index):
        """Enable indexing and slicing: dna[0], dna[1:10]"""
        return self.sequence[index]
    
    def transcribe(self):
        """Convert DNA to RNA (T -> U)"""
        rna_seq = self.sequence.replace('T', 'U')
        return RNA(rna_seq, self.seq_id)
    
    def reverse_complement(self):
        """Return reverse complement"""
        complement_map = str.maketrans('ATCG', 'TAGC')
        complement = self.sequence.translate(complement_map)
        return DNA(complement[::-1], f"{self.seq_id}_rc")
    
    def gc_content(self):
        """Calculate GC percentage"""
        g = self.sequence.count('G')
        c = self.sequence.count('C')
        return (g + c) / len(self.sequence) * 100 if len(self.sequence) > 0 else 0
    
    def count_nucleotides(self):
        """Return dict of nucleotide counts"""
        return {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'C': self.sequence.count('C'),
            'G': self.sequence.count('G')
        }
    
    def find_motif(self, motif):
        """Find all positions of motif"""
        positions = []
        motif = motif.upper()
        for i in range(len(self.sequence) - len(motif) + 1):
            if self.sequence[i:i+len(motif)] == motif:
                positions.append(i)
        return positions

# Test
dna = DNA("ATCGATCGATCG", "test_seq")

print(f"Length: {len(dna)}")
print(f"First 4 bases: {dna[:4]}")
print(f"GC content: {dna.gc_content():.2f}%")
print(f"Nucleotide counts: {dna.count_nucleotides()}")

rna = dna.transcribe()
print(f"RNA: {rna.sequence}")

rc = dna.reverse_complement()
print(f"Reverse complement: {rc.sequence}")

atg_positions = dna.find_motif("ATG")
print(f"ATG found at: {atg_positions}")
```

### RNA Sequence Class

```python
class RNA:
    """RNA sequence class with translation"""
    
    CODON_TABLE = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    def __init__(self, sequence, seq_id=""):
        self.sequence = sequence.upper()
        self.seq_id = seq_id
    
    def __len__(self):
        return len(self.sequence)
    
    def translate(self):
        """Translate RNA to protein"""
        protein = []
        
        for i in range(0, len(self.sequence) - 2, 3):
            codon = self.sequence[i:i+3]
            amino_acid = self.CODON_TABLE.get(codon, 'X')
            
            if amino_acid == '*':  # Stop codon
                break
            
            protein.append(amino_acid)
        
        return Protein(''.join(protein), self.seq_id)
    
    def find_start_codons(self):
        """Find all AUG positions"""
        positions = []
        for i in range(len(self.sequence) - 2):
            if self.sequence[i:i+3] == 'AUG':
                positions.append(i)
        return positions

# Test
rna = RNA("AUGUGCUAAUCGAAA", "mrna1")
print(f"RNA: {rna.sequence}")

start_codons = rna.find_start_codons()
print(f"Start codons at: {start_codons}")

protein = rna.translate()
print(f"Protein: {protein.sequence}")
```

### Protein Sequence Class

```python
class Protein:
    """Protein sequence class"""
    
    # Amino acid properties
    HYDROPHOBIC = set('AILMFWV')
    POLAR = set('STNQ')
    CHARGED = set('DEKR')
    AROMATIC = set('FWY')
    
    # Molecular weights (Da)
    MW_TABLE = {
        'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1,
        'C': 121.2, 'Q': 146.2, 'E': 147.1, 'G': 75.1,
        'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2,
        'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1,
        'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1
    }
    
    def __init__(self, sequence, seq_id=""):
        self.sequence = sequence.upper()
        self.seq_id = seq_id
    
    def __len__(self):
        return len(self.sequence)
    
    def molecular_weight(self):
        """Calculate molecular weight in Daltons"""
        weight = sum(self.MW_TABLE.get(aa, 0) for aa in self.sequence)
        # Subtract water molecules from peptide bonds
        weight -= (len(self.sequence) - 1) * 18.015
        return weight
    
    def count_amino_acids(self):
        """Return frequency of each amino acid"""
        counts = {}
        for aa in self.sequence:
            counts[aa] = counts.get(aa, 0) + 1
        return counts
    
    def get_composition(self):
        """Get composition by property"""
        return {
            'hydrophobic': sum(1 for aa in self.sequence if aa in self.HYDROPHOBIC),
            'polar': sum(1 for aa in self.sequence if aa in self.POLAR),
            'charged': sum(1 for aa in self.sequence if aa in self.CHARGED),
            'aromatic': sum(1 for aa in self.sequence if aa in self.AROMATIC)
        }
    
    def calculate_pi(self):
        """Estimate isoelectric point (simplified)"""
        # Count charged residues
        positive = sum(1 for aa in self.sequence if aa in 'KR')
        negative = sum(1 for aa in self.sequence if aa in 'DE')
        
        # Very simplified estimation
        if positive > negative:
            return 7.0 + (positive - negative) * 0.5
        elif negative > positive:
            return 7.0 - (negative - positive) * 0.5
        else:
            return 7.0

# Test
protein = Protein("MKTAYIAKQRQISFVKSHFSRQLEERLGLIEV", "p53_fragment")

print(f"Protein: {protein.sequence}")
print(f"Length: {len(protein)} amino acids")
print(f"Molecular weight: {protein.molecular_weight():.2f} Da")
print(f"Composition: {protein.get_composition()}")
print(f"Estimated pI: {protein.calculate_pi():.2f}")
print(f"Amino acid counts: {protein.count_amino_acids()}")
```

---

## 🧩 Part 3: Inheritance

### Base Sequence Class

```python
class BioSequence:
    """Base class for all biological sequences"""
    
    def __init__(self, sequence, seq_id="", description=""):
        self.sequence = sequence.upper()
        self.seq_id = seq_id
        self.description = description
    
    def __len__(self):
        return len(self.sequence)
    
    def __str__(self):
        preview = self.sequence[:50] + "..." if len(self.sequence) > 50 else self.sequence
        return f"{self.__class__.__name__}({self.seq_id}, {len(self)} bp): {preview}"
    
    def to_fasta(self, line_length=60):
        """Export as FASTA format"""
        header = f">{self.seq_id}"
        if self.description:
            header += f" {self.description}"
        
        lines = [header]
        for i in range(0, len(self.sequence), line_length):
            lines.append(self.sequence[i:i+line_length])
        
        return '\n'.join(lines)

class DNASeq(BioSequence):
    """DNA sequence - inherits from BioSequence"""
    
    def __init__(self, sequence, seq_id="", description=""):
        # Call parent constructor
        super().__init__(sequence, seq_id, description)
        
        # Validate DNA
        valid_bases = set('ATCGN')
        if not set(self.sequence).issubset(valid_bases):
            raise ValueError(f"Invalid DNA sequence: contains non-DNA characters")
    
    def transcribe(self):
        """Convert to RNA"""
        rna_seq = self.sequence.replace('T', 'U')
        return RNASeq(rna_seq, self.seq_id, self.description)
    
    def gc_content(self):
        """Calculate GC%"""
        g = self.sequence.count('G')
        c = self.sequence.count('C')
        return (g + c) / len(self.sequence) * 100 if len(self.sequence) > 0 else 0

class RNASeq(BioSequence):
    """RNA sequence - inherits from BioSequence"""
    
    def __init__(self, sequence, seq_id="", description=""):
        super().__init__(sequence, seq_id, description)
        
        # Validate RNA
        valid_bases = set('AUCGN')
        if not set(self.sequence).issubset(valid_bases):
            raise ValueError(f"Invalid RNA sequence: contains non-RNA characters")
    
    def back_transcribe(self):
        """Convert to DNA"""
        dna_seq = self.sequence.replace('U', 'T')
        return DNASeq(dna_seq, self.seq_id, self.description)

# Test inheritance
dna = DNASeq("ATCGATCG", "gene1", "Test gene")
print(dna)
print(f"GC content: {dna.gc_content():.2f}%")

rna = dna.transcribe()
print(rna)

print("\nFASTA format:")
print(dna.to_fasta(line_length=40))
```

### Specialized Gene Class

```python
class Gene(DNASeq):
    """Gene class with additional features"""
    
    def __init__(self, sequence, seq_id="", description="", 
                 start_pos=0, end_pos=None, strand="+"):
        super().__init__(sequence, seq_id, description)
        
        self.start_pos = start_pos
        self.end_pos = end_pos if end_pos else len(sequence)
        self.strand = strand
        self.exons = []  # List of (start, end) tuples
    
    def add_exon(self, start, end):
        """Add an exon coordinate"""
        self.exons.append((start, end))
        self.exons.sort()  # Keep sorted
    
    def get_exon_sequence(self):
        """Extract and concatenate exon sequences"""
        exon_seqs = []
        for start, end in self.exons:
            exon_seqs.append(self.sequence[start:end])
        return ''.join(exon_seqs)
    
    def get_intron_count(self):
        """Return number of introns"""
        return max(0, len(self.exons) - 1)
    
    def is_coding(self):
        """Check if gene has exons (coding)"""
        return len(self.exons) > 0

# Test
gene = Gene("ATGAAATTTCCCGGGTAGAAATTTCCCTAA", "BRCA1", "Breast cancer gene")
gene.add_exon(0, 9)    # First exon: ATGAAATTT
gene.add_exon(12, 21)  # Second exon: CCCGGGTAG
gene.add_exon(24, 30)  # Third exon: AATTTC

print(gene)
print(f"Exon count: {len(gene.exons)}")
print(f"Intron count: {gene.get_intron_count()}")
print(f"Exon sequence: {gene.get_exon_sequence()}")
print(f"Is coding: {gene.is_coding()}")
```

---

## 🧩 Part 4: Encapsulation & Properties

### Private Attributes

```python
class SecureSequence:
    """Sequence with data validation"""
    
    def __init__(self, sequence):
        # Private attribute (by convention, use _)
        self._sequence = ""
        self._quality_score = None
        
        # Use setter to validate
        self.set_sequence(sequence)
    
    def get_sequence(self):
        """Getter method"""
        return self._sequence
    
    def set_sequence(self, sequence):
        """Setter method with validation"""
        sequence = sequence.upper()
        
        # Validate
        valid_bases = set('ATCGN')
        if not set(sequence).issubset(valid_bases):
            raise ValueError("Invalid sequence characters")
        
        if len(sequence) < 3:
            raise ValueError("Sequence too short")
        
        self._sequence = sequence
    
    def calculate_quality(self):
        """Calculate internal quality score"""
        n_count = self._sequence.count('N')
        self._quality_score = 100 - (n_count / len(self._sequence) * 100)
        return self._quality_score

# Test
seq = SecureSequence("ATCGATCG")
print(f"Sequence: {seq.get_sequence()}")
print(f"Quality: {seq.calculate_quality():.2f}")

# This will raise error
try:
    seq.set_sequence("ATCGXYZ")
except ValueError as e:
    print(f"Error: {e}")
```

### Property Decorators

```python
class ModernSequence:
    """Sequence using @property decorators"""
    
    def __init__(self, sequence):
        self._sequence = sequence.upper()
        self._gc_cache = None  # Cache for expensive calculation
    
    @property
    def sequence(self):
        """Getter as property"""
        return self._sequence
    
    @sequence.setter
    def sequence(self, value):
        """Setter with validation"""
        value = value.upper()
        if not set(value).issubset(set('ATCGN')):
            raise ValueError("Invalid characters")
        
        self._sequence = value
        self._gc_cache = None  # Invalidate cache
    
    @property
    def length(self):
        """Read-only property"""
        return len(self._sequence)
    
    @property
    def gc_content(self):
        """Cached property"""
        if self._gc_cache is None:
            g = self._sequence.count('G')
            c = self._sequence.count('C')
            self._gc_cache = (g + c) / len(self._sequence) * 100
        
        return self._gc_cache

# Test - use like attributes!
seq = ModernSequence("ATCGATCG")
print(f"Sequence: {seq.sequence}")
print(f"Length: {seq.length}")
print(f"GC%: {seq.gc_content:.2f}")

# Modify sequence
seq.sequence = "GCGCGCGC"
print(f"New GC%: {seq.gc_content:.2f}")
```

---

## 🧩 Part 5: Complete Example

### FASTA Record Class

```python
class FastaRecord:
    """Complete FASTA record with full functionality"""
    
    def __init__(self, header, sequence):
        self._parse_header(header)
        self.sequence = sequence.upper().replace(' ', '').replace('\n', '')
    
    def _parse_header(self, header):
        """Parse FASTA header into components"""
        # Remove leading >
        header = header.lstrip('>')
        
        # Split ID and description
        parts = header.split(maxsplit=1)
        self.seq_id = parts[0]
        self.description = parts[1] if len(parts) > 1 else ""
    
    def __len__(self):
        return len(self.sequence)
    
    def __str__(self):
        return f"FastaRecord({self.seq_id}, {len(self)} bp)"
    
    def __repr__(self):
        return f"FastaRecord(seq_id='{self.seq_id}', length={len(self)})"
    
    def __eq__(self, other):
        """Enable comparison"""
        if not isinstance(other, FastaRecord):
            return False
        return self.sequence == other.sequence
    
    @property
    def header(self):
        """Reconstruct header"""
        if self.description:
            return f">{self.seq_id} {self.description}"
        return f">{self.seq_id}"
    
    def to_fasta(self, line_length=60):
        """Export as FASTA format"""
        lines = [self.header]
        
        for i in range(0, len(self.sequence), line_length):
            lines.append(self.sequence[i:i+line_length])
        
        return '\n'.join(lines)
    
    def gc_content(self):
        """Calculate GC percentage"""
        g = self.sequence.count('G')
        c = self.sequence.count('C')
        return (g + c) / len(self.sequence) * 100 if len(self.sequence) > 0 else 0
    
    def count_bases(self):
        """Return base composition"""
        return {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'C': self.sequence.count('C'),
            'G': self.sequence.count('G'),
            'N': self.sequence.count('N')
        }
    
    def reverse_complement(self):
        """Return new record with reverse complement"""
        complement = str.maketrans('ATCGN', 'TAGCN')
        rc_seq = self.sequence.translate(complement)[::-1]
        return FastaRecord(
            f"{self.seq_id}_rc",
            rc_seq
        )
    
    @classmethod
    def from_file(cls, filename):
        """Create records from FASTA file"""
        records = []
        current_header = None
        current_seq = []
        
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('>'):
                    # Save previous record
                    if current_header:
                        records.append(cls(current_header, ''.join(current_seq)))
                    
                    current_header = line
                    current_seq = []
                else:
                    current_seq.append(line)
            
            # Save last record
            if current_header:
                records.append(cls(current_header, ''.join(current_seq)))
        
        return records

# Test
record = FastaRecord(">NM_007294 BRCA1 gene", "ATCGATCGATCG")

print(record)
print(f"Header: {record.header}")
print(f"Length: {len(record)}")
print(f"GC%: {record.gc_content():.2f}")
print(f"Base counts: {record.count_bases()}")

print("\nFASTA format:")
print(record.to_fasta(line_length=40))

print("\nReverse complement:")
rc = record.reverse_complement()
print(rc.sequence)
```

---

## 📝 Practice Tasks (Day 18)

### Basic Exercises

1. **Simple Class**: Create a `Nucleotide` class with attributes for base, position, and quality score.

2. **Sequence Counter**: Create a `SequenceCollection` class that stores multiple sequences and counts total bases.

3. **Codon Class**: Create a `Codon` class with methods to translate to amino acid.

4. **Read Class**: Create a `SequencingRead` class for FASTQ entries (sequence + quality).

5. **Alignment Class**: Create a `PairwiseAlignment` class storing two sequences and a score.

### Intermediate Challenges

6. **Gene Hierarchy**: Implement inheritance chain: `Sequence` → `Gene` → `Transcript` → `Protein`.

7. **Motif Class**: Create a `Motif` class that finds itself in sequences with position tracking.

8. **Quality Control**: Implement a `QualityChecker` class that validates sequences with multiple criteria.

9. **Sequence Parser**: Create a `FastqParser` class that reads files and returns `FastqRecord` objects.

10. **Statistics Mixin**: Create a `StatsMixin` class with GC%, length, composition that other classes can inherit.

### Advanced Challenges

11. **Complete BioPython-like API**: Design a mini-library with `SeqRecord`, `Seq`, and `SeqIO` classes.

12. **Polymorphism**: Implement a `translate()` method that works differently for DNA vs RNA classes.

13. **Operator Overloading**: Implement `+` to concatenate sequences, `*` to repeat, `in` to find motifs.

14. **Context Manager**: Create a `FastaFile` class that works with `with` statement for safe file handling.

15. **Iterator Protocol**: Implement `__iter__` and `__next__` for a `GenomeScanner` class that yields windows.

---

## 💡 Key Takeaways

✓ **Classes** bundle data (attributes) and behavior (methods) together  
✓ **__init__** constructor initializes new instances  
✓ **self** refers to the instance itself  
✓ **Inheritance** enables code reuse via parent classes  
✓ **super()** calls parent class methods  
✓ **Properties (@property)** provide controlled attribute access  
✓ **Private attributes (_name)** indicate internal implementation  
✓ **Magic methods (__str__, __len__)** customize behavior  
✓ **Class methods (@classmethod)** operate on class level  
✓ **Static methods (@staticmethod)** don't need instance or class  
✓ **Encapsulation** hides implementation details  
✓ **Polymorphism** allows method overriding in subclasses  
✓ **Composition over inheritance** - prefer has-a over is-a  
✓ **Document classes** with docstrings for usability  
✓ **Design APIs** thinking about user experience  

**Next**: Python Packages, Modules, and BioPython
