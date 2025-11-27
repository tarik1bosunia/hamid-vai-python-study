# Explanation of the GFFutils + Biopython RNA Feature Extraction Script

```python
# Install gffutils only if it is not already installed
try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

# Install biopython only if it is not already installed
try:
    from Bio import SeqIO
    from Bio.Seq import Seq
except ImportError:
    !pip install biopython
    from Bio import SeqIO
    from Bio.Seq import Seq

import pandas as pd
import random
import gzip
import os

# ▼ Input file paths (change if needed)
gff_file = "/content/Caenorhabditis_elegans.WBcel235.61.chromosome.I.gff3.gz"
fasta_file = "/content/Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz"
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = gff_file.removesuffix(".gz").removesuffix(".gff3") + ".rna_seq.tsv"

# Specify the length of sequences to extract
promoter_len = 100
terminator_len = 100

# Create GFF database
if not os.path.exists(db_fn):
    print("Creating GFF database... (this may take some time)")
    db = gffutils.create_db(
        gff_file, db_fn, force=True, keep_order=False, disable_infer_transcripts=True,
        merge_strategy="create_unique", sort_attribute_values=True
    )
    files.download(db_fn)
else:
    db = gffutils.FeatureDB(db_fn)

sample_genes = random.sample(list(db.features_of_type("gene")), 100)

with gzip.open(fasta_file, "rt") as handle:
    genome = {record.id: record.seq for record in SeqIO.parse(handle, "fasta")}

transcript_types = [
    "transcript", "mRNA", "ncRNA", "lnc_RNA", "miRNA", "tRNA",
    "rRNA", "snRNA", "snoRNA", "scRNA", "antisense_RNA",
    "pseudogenic_transcript", "processed_transcript"
]

attribute_keys = set()
rows = []

for gene in sample_genes:
    gene_id = gene.attributes.get("gene_id", [""])[0]
    gene_name = gene.attributes.get("Name", [""])[0]
    chrom = gene.chrom
    strand = gene.strand

    for tx in db.children(gene, featuretype=transcript_types, level=1):
        tx_id = tx.id
        transcript_id = tx.attributes.get("transcript_id", [tx_id])[0]
        tx_name = tx.attributes.get("Name", [tx_id])[0]
        biotype = tx.attributes.get("biotype", [""])[0]
        attr_dict = {k: v[0] for k, v in tx.attributes.items()}
        attribute_keys.update(attr_dict.keys())

        exon_count = sum([1 for _ in db.children(tx, featuretype="exon")])

        def extract_sequence(start, end):
            seq = genome[chrom][start:end]
            return seq.reverse_complement() if strand == "-" else seq

        def get_concat_seq(featuretype):
            parts = list(db.children(tx, featuretype=featuretype, order_by='start'))
            if parts:
                seq = Seq("".join(str(genome[chrom][f.start-1:f.end]) for f in parts))
                if strand == "-":
                    seq = seq.reverse_complement()
            else:
                seq = None
            return seq

        utr5 = get_concat_seq("five_prime_UTR")
        cds = get_concat_seq("CDS")
        utr3 = get_concat_seq("three_prime_UTR")

        if strand == "+":
            promoter = extract_sequence(tx.start - promoter_len-1, tx.start - 1)
            terminator = extract_sequence(tx.end, tx.end + terminator_len)
        else:
            promoter = extract_sequence(tx.end, tx.end + promoter_len)
            terminator = extract_sequence(tx.start - terminator_len-1, tx.start - 1)

        row = {
            "gene_id": gene_id,
            "gene_name": gene_name,
            "transcript_id": transcript_id,
            "Exon Count": exon_count,
            "5'UTR": str(utr5) if utr5 else None,
            "CDS": str(cds) if cds else None,
            "3'UTR": str(utr3) if utr3 else None,
            "Protein": str(cds.translate()) if cds else None,
            "Promoter": str(promoter),
            "Terminator": str(terminator),
        }
        rows.append(row)

rna_seq_df = pd.DataFrame(rows)

display(rna_seq_df)

with open(output_path, "w") as f:
    rna_seq_df.to_csv(f, sep="	", index=False)

files.download(output_path)
```

This document explains, step by step, what the provided Python script does. The script uses **gffutils** and **Biopython** to extract various transcript-related sequences (UTRs, CDS, protein, promoter, terminator) from a genome.

---

## 1. Library Installation and Imports

```python
# Install gffutils only if it is not already installed
try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

# Install biopython only if it is not already installed
try:
    from Bio import SeqIO
    from Bio.Seq import Seq
except ImportError:
    !pip install biopython
    from Bio import SeqIO
    from Bio.Seq import Seq

import pandas as pd
import random
import gzip
import os
```

### What this does

* Tries to import **gffutils**. If it is not available, it installs it using `pip` (this assumes a Jupyter/Colab-style environment where `!` is allowed) and then imports it.
* Similarly, it tries to import **Biopython** modules `SeqIO` and `Seq` and installs Biopython if necessary.
* Imports standard Python modules:

  * `pandas` for table/dataframe handling.
  * `random` for random sampling of genes.
  * `gzip` for reading compressed `.gz` files.
  * `os` for file path and existence checks.

---

## 2. Input Files and Output Paths

```python
# ▼ Input file paths (change if needed)
gff_file = "/content/Caenorhabditis_elegans.WBcel235.61.chromosome.I.gff3.gz"
fasta_file = "/content/Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz"
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = gff_file.removesuffix(".gz").removesuffix(".gff3") + ".rna_seq.tsv"

# Specify the length of sequences to extract
promoter_len = 100
terminator_len = 100
```

### What this does

* `gff_file`: path to the **GFF3 annotation** file (compressed with gzip).
* `fasta_file`: path to the **FASTA genome sequence** (also compressed).
* `db_fn`: the filename of the **gffutils database**. It removes the `.gz` suffix from the GFF filename and appends `.db`.
* `output_path`: output TSV file where extracted sequences will be stored. It removes `.gz` and `.gff3` from the GFF filename and appends `.rna_seq.tsv`.
* `promoter_len` and `terminator_len`: lengths (in base pairs) of promoter and terminator regions to extract upstream/downstream of each transcript.

---

## 3. Creating or Loading the GFF Database

```python
# Create GFF database
if not os.path.exists(db_fn):
    print("Creating GFF database... (this may take some time)")
    # Normally: keep_order=True, disable_infer_transcripts=False, merge_strategy="merge"
    # For speed: keep_order=False, disable_infer_transcripts=True, merge_strategy="create_unique"
    db = gffutils.create_db(
        gff_file, db_fn, force=True, keep_order=False, disable_infer_transcripts=True,
        merge_strategy="create_unique", sort_attribute_values=True
    )
    # Save the GFF database
    files.download(db_fn)
else:
    db = gffutils.FeatureDB(db_fn)
```

### What this does

* Checks if the `.db` file already exists.
* If **not**:

  * Prints a message that it is creating the GFF database (this can be slow for large genomes).
  * Calls `gffutils.create_db` to parse the GFF3 file and build a **SQLite database**.

    * `keep_order=False`, `disable_infer_transcripts=True`, and `merge_strategy="create_unique"` are settings chosen for speed.
    * `sort_attribute_values=True` sorts attribute values to keep them consistent.
  * Optionally downloads the created database file using `files.download(db_fn)` (this assumes a Colab environment where `files` was previously imported from `google.colab`).
* If the `.db` file **does exist**, it opens the existing database using `gffutils.FeatureDB`.

### Why use a database?

* The GFF3 file is a large text file. Converting it to a database allows **fast queries** for features like genes, transcripts, and exons, and makes traversing parent–child relationships more efficient.

---

## 4. Selecting Genes to Process

```python
# Randomly sample any 100 genes
sample_genes = random.sample(list(db.features_of_type("gene")), 100)

# To process all genes instead, use:
# sample_genes = list(db.features_of_type("gene"))
```

### What this does

* Retrieves all features of type `"gene"` from the GFF database.
* Uses `random.sample` to pick **100 genes at random** to process.
* A commented alternative shows how to process **all genes** instead (by simply converting the generator to a list).

This sampling is helpful when testing or when full-genome processing would be too slow.

---

## 5. Loading the Genome Sequence

```python
# Read genome sequence (dictionary format)
with gzip.open(fasta_file, "rt") as handle:
    genome = {record.id: record.seq for record in SeqIO.parse(handle, "fasta")}
```

### What this does

* Opens the compressed FASTA file in **text mode** (`"rt"`).
* Uses `SeqIO.parse` to iterate through each sequence record in the FASTA file.
* Builds a dictionary:

  * **Key**: `record.id` (e.g., chromosome ID like `"I"`)
  * **Value**: `record.seq` (a Biopython `Seq` object representing the DNA sequence of that chromosome).

This dictionary allows fast access to genomic sequences by chromosome.

---

## 6. Defining Transcript Types

```python
# Transcript types (mRNA, ncRNA, etc.)
transcript_types = [
    "transcript", "mRNA", "ncRNA", "lnc_RNA", "miRNA", "tRNA",
    "rRNA", "snRNA", "snoRNA", "scRNA", "antisense_RNA",
    "pseudogenic_transcript", "processed_transcript"
]
```

### What this does

* Defines a list of feature types that should be considered as **transcripts**.
* This includes protein-coding RNA (`mRNA`), non-coding RNAs (`ncRNA`, `lnc_RNA`, `miRNA`, etc.), and other transcript-like features.

This list is used later when querying child features of each gene.

---

## 7. Data Structures for Results

```python
# Collect information for each gene/transcript
attribute_keys = set()
rows = []
```

### What this does

* `attribute_keys`: a set that could be used to collect all attribute names encountered (for potential use in columns later).
* `rows`: a list of dictionaries, where each dictionary will represent one **transcript** and its extracted sequence information.

---

## 8. Main Loop Over Genes and Transcripts

```python
for gene in sample_genes:
    gene_id = gene.attributes.get("gene_id", [""])[0]
    gene_name = gene.attributes.get("Name", [""])[0]
    chrom = gene.chrom
    strand = gene.strand

    for tx in db.children(gene, featuretype=transcript_types, level=1):
        tx_id = tx.id
        transcript_id = tx.attributes.get("transcript_id", [tx_id])[0]
        tx_name = tx.attributes.get("Name", [tx_id])[0]
        biotype = tx.attributes.get("biotype", [""])[0]
        attr_dict = {k: v[0] for k, v in tx.attributes.items()}
        attribute_keys.update(attr_dict.keys())
```

### What this does

1. **Outer loop:** iterates over each sampled `gene`.

   * Extracts:

     * `gene_id` from the `gene_id` attribute if present.
     * `gene_name` from the `Name` attribute if present.
     * `chrom`: chromosome name where the gene is located.
     * `strand`: `"+"` or `"-"`, indicating the strand.

2. **Inner loop:** iterates over child features of the gene whose types are in `transcript_types`.

   * `db.children(gene, featuretype=transcript_types, level=1)` returns transcripts that are direct children of the gene.
   * For each transcript `tx`:

     * `tx_id`: the feature ID.
     * `transcript_id`: either the `transcript_id` attribute or fallback to `tx_id`.
     * `tx_name`: either the `Name` attribute or fallback to `tx_id`.
     * `biotype`: biotype attribute if available.
     * `attr_dict`: dictionary of transcript attributes, taking only the first value for each.
     * `attribute_keys` is updated with all attribute names seen so far.

At this point, the code has identified which gene and transcript it's working on and collected some metadata.

---

## 9. Counting Exons

```python
        # Exons
        exon_count = sum([1 for _ in db.children(tx, featuretype="exon")])
```

### What this does

* Uses `db.children(tx, featuretype="exon")` to iterate over all **exons** belonging to the transcript `tx`.
* Counts how many exon features there are by summing `1` for each exon.
* Stores the total exon count in `exon_count`.

---

## 10. Helper Function: `extract_sequence`

```python
        # Sequence extraction function (reverse strand supported)
        def extract_sequence(start, end):
            seq = genome[chrom][start:end]
            return seq.reverse_complement() if strand == "-" else seq
```

### What this does

* `extract_sequence(start, end)` takes genomic coordinates (`start`, `end`) and returns the corresponding DNA sequence.
* It uses `genome[chrom]` to get the chromosome sequence, then slices from `start` to `end` (0-based, half-open indexing).
* If the gene/transcript is on the **minus strand** (`"-"`), it returns the **reverse complement** of the sequence.

This handles strand orientation correctly.

---

## 11. Helper Function: `get_concat_seq`

```python
        # Get concatenated sequence for each region
        def get_concat_seq(featuretype):
            parts = list(db.children(tx, featuretype=featuretype, order_by='start'))
            if parts:
                seq = Seq("".join(str(genome[chrom][f.start-1:f.end]) for f in parts))
                if strand == "-":
                    seq = seq.reverse_complement()
            else:
                seq = None
            return seq
```

### What this does

* `get_concat_seq(featuretype)` collects all child features of type `featuretype` for the transcript `tx` (e.g., `five_prime_UTR`, `CDS`, `three_prime_UTR`).
* `order_by='start'` ensures the parts are ordered along the chromosome.
* If there are any such parts:

  * It extracts the sequence for each feature using `genome[chrom][f.start-1:f.end]` (GFF is 1-based inclusive, so `start-1` is used).
  * Joins them into a single contiguous sequence string.
  * Wraps the string in a Biopython `Seq` object.
  * If on the minus strand, reverse-complements the entire concatenated sequence.
* If there are no parts (no features of that type), it returns `None`.

This function is used to build full sequences for UTRs and CDS regions.

---

## 12. Extracting UTRs and CDS

```python
        utr5 = get_concat_seq("five_prime_UTR")
        cds = get_concat_seq("CDS")
        utr3 = get_concat_seq("three_prime_UTR")
```

### What this does

* Uses `get_concat_seq` to obtain:

  * `utr5`: concatenated **5' UTR** sequence.
  * `cds`: concatenated **CDS (coding sequence)**.
  * `utr3`: concatenated **3' UTR** sequence.
* Each of these is either a `Seq` object or `None` if not present.

---

## 13. Computing Promoter and Terminator Regions

```python
        # Promoter and terminator region (adjust start/end)
        if strand == "+":
            promoter = extract_sequence(tx.start - promoter_len-1, tx.start - 1)
            terminator = extract_sequence(tx.end, tx.end + terminator_len)
        else:
            promoter = extract_sequence(tx.end, tx.end + promoter_len)
            terminator = extract_sequence(tx.start - terminator_len-1, tx.start - 1)
```

### What this does

* Computes **promoter** and **terminator** regions relative to the transcript coordinates, taking strand into account.

For **plus strand (`"+"`)**:

* Promoter is upstream of `tx.start`:

  * From `tx.start - promoter_len - 1` to `tx.start - 1`.
* Terminator is downstream of `tx.end`:

  * From `tx.end` to `tx.end + terminator_len`.

For **minus strand (`"-"`)**:

* Promoter is downstream in genomic coordinates (but upstream in transcriptional direction):

  * From `tx.end` to `tx.end + promoter_len`.
* Terminator is upstream in genomic coordinates:

  * From `tx.start - terminator_len - 1` to `tx.start - 1`.

The `extract_sequence` function takes care of applying the reverse complement on the minus strand.

---

## 14. Building the Result Row

```python
        # Record results
        row = {
            "gene_id": gene_id,
            "gene_name": gene_name,
            "transcript_id": transcript_id,
            # "trans_name": tx_name,
            # "biotype": biotype,
            "Exon Count": exon_count,
            "5'UTR": str(utr5) if utr5 else None,
            "CDS": str(cds) if cds else None,
            "3'UTR": str(utr3) if utr3 else None,
            "Protein": str(cds.translate()) if cds else None,
            "Promoter": str(promoter),
            "Terminator": str(terminator),
        }
        # row.update(attr_dict)
        rows.append(row)
```

### What this does

* Creates a Python dictionary `row` representing one transcript and its associated sequences.
* Fields include:

  * `gene_id`, `gene_name`: metadata about the gene.
  * `transcript_id`: identifier of the transcript.
  * `Exon Count`: number of exon features.
  * `5'UTR`, `CDS`, `3'UTR`: string versions of the sequences or `None` if missing.
  * `Protein`: translation of the CDS using `cds.translate()` if CDS exists, else `None`.
  * `Promoter`, `Terminator`: promoter and terminator sequences as strings.
* The line `# row.update(attr_dict)` is commented out; if enabled, it would add all transcript attributes into the row as additional columns.
* Appends the `row` dictionary to the `rows` list.

---

## 15. Creating the DataFrame

```python
# Create DataFrame with arranged columns
main_cols = ["gene_id", "gene_name", "trans_id", "trans_name", "biotype", "Exon Count", "5'UTR", "CDS", "3'UTR", "Protein", "Promoter", "Terminator"]
# attribute_cols = sorted(attribute_keys)
# rna_seq_df = pd.DataFrame(rows)[main_cols + attribute_cols]
rna_seq_df = pd.DataFrame(rows)
```

### What this does

* Defines a list `main_cols` that looks like an intended ordered set of columns.

  * Note: the actual keys in `row` are `"transcript_id"`, not `"trans_id"`, and `"trans_name"`/`"biotype"` are commented out in `row`. So `main_cols` is **not** directly used.
* The commented lines show an alternative where the DataFrame would be created and columns ordered with `main_cols + attribute_cols`.
* The active line `rna_seq_df = pd.DataFrame(rows)` simply creates a DataFrame from all rows with columns inferred from the dictionaries.

---

## 16. Displaying and Saving the Results

```python
# Display
display(rna_seq_df)

# Save to file
with open(output_path, "w") as f:
    rna_seq_df.to_csv(f, sep="\t", index=False)

# Download the file
files.download(output_path)
```

### What this does

* `display(rna_seq_df)`: shows the DataFrame in a rich, table-like format (in Jupyter/Colab).
* `to_csv(..., sep="\t")`: writes the DataFrame to a **tab-separated values (TSV)** file.
* `files.download(output_path)`: triggers a file download (again, assuming a Colab environment with `files` imported from `google.colab`).

The resulting file contains, for each transcript:

* Gene and transcript IDs.
* Exon count.
* 5' UTR / CDS / 3' UTR sequences.
* Translated protein sequences.
* Promoter and terminator sequences.

---

## 17. High-Level Summary

This script:

1. Reads genome annotations (GFF3) and genome sequences (FASTA).
2. Converts the GFF3 into a **gffutils** database for fast feature queries.
3. Randomly selects 100 genes.
4. For each gene, iterates over its transcript features.
5. Extracts:

   * 5' UTR, CDS, 3' UTR sequences.
   * Promoter and terminator sequences around the transcript.
   * Translated protein sequences from the CDS.
   * Exon counts.
6. Stores all this information in a pandas DataFrame.
7. Saves the results as a TSV file for downstream analysis.

This provides a convenient table of transcript-level genomic features and sequences derived from the original annotation and reference genome.
