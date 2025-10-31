# OUBIC Bioinformatics Workshop (Full English Version)

## Session 1 (Afternoon): Introduction to Nucleotide Sequence Manipulation

### Acquiring and Saving Nucleotide Sequences

* **Last updated:** 2025-06-29
* **Author:** Shotaro Yamasaki (Osaka University · OUBIC · RNA Informatics)

> This material was created by the author with assistance from ChatGPT (OpenAI) for structure, wording, and code generation. Reliability checks and final decisions are the responsibility of the author.

---

# Getting Started

## ✅ Save a Copy to Drive

1. From the top menu, click **File → Save a copy in Drive**.
   → A copy of this notebook is created in your Google Drive (usually in the **Colab Notebooks** folder). Move it elsewhere if you prefer.
2. **Work on the copied notebook.** Changes to the original may not persist.

## 🗂️ Show the Table of Contents

Use the Table of Contents icon (top-left) to quickly jump between sections.

---

# What This Notebook Is For

### 🧬 Retrieve Gene & Sequence Information

Accurately obtaining *gene metadata* and *nucleotide sequences* is the starting point for virtually all bioinformatics workflows (expression analysis, variant analysis, structure prediction, etc.).

**Skill to learn:** Retrieve data from reliable, user-friendly databases (e.g., Ensembl, NCBI) efficiently and reproducibly.

### ✅ You Don’t Need to Master Every Line of Code (Important)

* For now, being able to **use existing code** is enough.
* If results don’t fully meet your needs, gradually learn and adapt the code.
* Modify in small, safe steps.

---

# Background Knowledge

## 🔹 Python Basics (recommended)

| Topic                                 | Why it matters                              |
| ------------------------------------- | ------------------------------------------- |
| Variables (assign & reference)        | Define/edit sequences                       |
| Indexing & slicing                    | Extract subsequences                        |
| Calling functions & passing arguments | Use helpers like `.translate()`, `.count()` |
| `for`/`if` (optional)                 | Helpful for automating sequence operations  |

## 🔹 Molecular Biology Basics (recommended)

| Topic                           | Why it matters                                     |
| ------------------------------- | -------------------------------------------------- |
| DNA–RNA–Protein flow            | For `transcribe()` and `translate()` understanding |
| Complement / reverse complement | To use `.complement()` / `.reverse_complement()`   |
| Codons & genetic code           | For translation and stop-codon handling            |

---

# License & Usage Terms

> **Creative Commons Attribution–NonCommercial 4.0 International (CC BY‑NC 4.0)**
> [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

* Free for education and research.
* **Commercial use is prohibited** (e.g., paid courses, commercial services).
* No author citation required when presenting results.
* Generic Python syntax and library usage examples are free to reuse.
* For instructional structure that reflects the author’s unique exposition, please credit:
  `# Based on code by Shotaro Yamasaki (Osaka University, OUBIC)`

## Disclaimer

* Designed for **Google Colab**; other environments are not guaranteed.
* Library/environment changes may break code; future compatibility is not guaranteed.
* Use at your own risk; the author bears no liability.
* Avoid sensitive data in Colab (cloud runtime).

---

# 🔰 Quick Intro to Google Colab

**What is Colab?** A free, browser-based Python environment running on Google’s cloud VMs.

* No local installation needed.
* Mix prose + code for lab notebooks and tutorials.

**Cells:**

* **Text cells** hold explanations and headings.
* **Code cells** run Python. Click ▶ to execute.
* Shortcuts: **Shift+Enter** (run & go next), **Ctrl/Cmd+Enter** (run & stay).

**Runtime model:**

* Each session spins up a **temporary VM**.
* Variables/files in `/content/` disappear when the runtime resets.
* Persist by downloading or saving to **Google Drive**.

---

# 🌐 Key Databases for Sequences & Gene Info

| Database                                           | Main Content                       | Human | Non‑human |       API       | Example                                                                          |
| -------------------------------------------------- | ---------------------------------- | :---: | :-------: | :-------------: | -------------------------------------------------------------------------------- |
| [NCBI Entrez](https://www.ncbi.nlm.nih.gov/)       | Genes, mRNA, genome, PubMed        |   ✅   |     ✅     | ✅ (E-utilities) | [TP53 mRNA](https://www.ncbi.nlm.nih.gov/nuccore/NM_000546)                      |
| [Ensembl](https://www.ensembl.org/)                | Gene structure, isoforms, variants |   ✅   |     ✅     |     ✅ (REST)    | [TP53 gene](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141510) |
| [UCSC](https://genome.ucsc.edu/)                   | Genome annotation & visualization  |   ✅   |     ✅     |        ✅        | TP53 (hg38) tracks                                                               |
| [UniProt](https://www.uniprot.org/)                | Protein sequence & function        |   ✅   |     ✅     |        ✅        | [P04637 (TP53)](https://www.uniprot.org/uniprotkb/P04637/entry)                  |
| [InterPro](https://www.ebi.ac.uk/interpro/)        | Protein domains/motifs             |   ✅   |     ✅     |        ✅        | P53 domain page                                                                  |
| [HGNC](https://www.genenames.org/)                 | Human gene names                   |   ✅   |     ❌     |        ✅        | TP53 entry                                                                       |
| [PDBe](https://www.ebi.ac.uk/pdbe/)                | Protein 3D structures              |   ✅   |     ✅     |        ✅        | TP53 structures                                                                  |
| [Expression Atlas](https://www.ebi.ac.uk/gxa/home) | RNA‑seq expression                 |   ✅   |     ✅     |     partial     | TP53 expression                                                                  |
| [GTEx Portal](https://gtexportal.org/)             | Tissue expression (human)          |   ✅   |     ❌     |        ❌        | TP53 at GTEx                                                                     |
| [OMIM](https://omim.org/)                          | Mendelian disease links            |   ✅   |     ❌     |        ❌        | TP53 OMIM                                                                        |
| [GeneCards](https://www.genecards.org/)            | Aggregated gene info               |   ✅   |     ❌     |        ❌        | TP53 GeneCard                                                                    |
| [STRING](https://string-db.org/)                   | PPI networks                       |   ✅   |     ✅     |        ✅        | TP53 interactions                                                                |

### Focus of this workshop

We’ll use **Ensembl** (primary) and **NCBI** to retrieve **gene info** and **nucleotide sequences**.

---

# Manual Retrieval for a Few Targets

For a small set of genes, the websites’ search UIs are sufficient (e.g., searching **TP53**).

**Caveats:** Different databases use different IDs/coordinates; RefSeq vs Ensembl isoforms may differ. For later genome‑wide processing, we prioritize **Ensembl**.

## Workflow

### Start at Ensembl

* Go to [https://www.ensembl.org](https://www.ensembl.org) and search `TP53` or `TP53 human`.
* Navigate to the gene page (e.g., `ENSG00000141510`).

### ✅ Pattern 1: Found in Ensembl

* Access accurate structures (exons/CDS/UTRs) and sequences (genomic/mRNA/CDS).
* Export per region as FASTA.
* **Promoter:** Transcript page → Export Data → “5' flanking” (e.g., 1000 bp).
* **Terminator:** Use “3' flanking”.

### ❌ Pattern 2: Not in Ensembl

* Try **NCBI Gene** (e.g., TP53) for gene info and RefSeq links.
* From RefSeq mRNA (e.g., **NM_000546.6**), switch to **GenBank** view to inspect CDS/UTR feature coordinates.

---

# Automating Retrieval via API (Few to Dozens of Genes)

**API = Application Programming Interface**: programmatic web access to datasets.

Below we define a function that, given a **species** (e.g., `homo_sapiens`) and a **gene symbol** (e.g., `TP53`), will:

1. Look up the Ensembl **gene ID**.
2. For up to `max_transcripts` transcripts, fetch:

   * cDNA (mRNA), 5'UTR, CDS, 3'UTR
   * Protein sequence (if coding)
   * **Promoter** (upstream of TSS) & **Terminator** (downstream of TES)
3. Display results in a table and save as TSV.

> Run the next cell once to load the function.

```python
import os
import requests
import pandas as pd
from google.colab import files

def get_gene_and_transcripts_info(
    species: str,
    symbol: str,
    promoter_len: int = 1000,
    terminator_len: int = 500,
    max_transcripts: int = 10,
    output_dir: str = "/content",
):
    """
    Get gene & transcript information from Ensembl (REST API).

    Returns: (lookup_json, output_path)
    """
    headers_json = {"Content-Type": "application/json"}
    headers_fasta = {"Content-Type": "text/x-fasta"}

    # 1) Resolve Ensembl Gene ID from symbol
    xref_url = f"https://rest.ensembl.org/xrefs/symbol/{species}/{symbol}?"
    xref_res = requests.get(xref_url, headers=headers_json)
    if xref_res.status_code != 200 or not xref_res.json():
        print(f"❌ '{symbol}' not found in Ensembl.")
        print("🔍 Check the spelling via NCBI:")
        print(f"https://www.ncbi.nlm.nih.gov/gene/?term={symbol}+{species}")
        return None

    gene_id = xref_res.json()[0]["id"]

    # 2) Gene lookup (with transcripts)
    lookup_url = f"https://rest.ensembl.org/lookup/id/{gene_id}?expand=1"
    lookup = requests.get(lookup_url, headers=headers_json).json()

    # 3) Basic gene info
    gene_info = {
        "Gene name": lookup.get("display_name"),
        "Ensembl Gene ID": gene_id,
        "Chromosome": lookup.get("seq_region_name"),
        "Start": lookup.get("start"),
        "End": lookup.get("end"),
        "Strand": lookup.get("strand"),
        "Description": lookup.get("description", "").split("[")[0].strip(),
        "Biotype": lookup.get("biotype"),
        "Transcript count": len(lookup.get("Transcript", [])),
        "Canonical Transcript": lookup.get("canonical_transcript")
    }

    header_lines = [f"# {k}: {v}" for k, v in gene_info.items()]
    print(f"Gene name       : {gene_info['Gene name']}")
    print(f"Gene ID         : {gene_info['Ensembl Gene ID']}")
    print(f"Transcript count: {gene_info['Transcript count']}")

    # 4) Iterate transcripts
    rows = []
    for t in lookup["Transcript"][:max_transcripts]:
        tid = t["id"]
        print(f"Transcript ID   : {tid}")
        tname = t.get("display_name", tid)
        is_coding = "protein_coding" in t.get("biotype", "")

        # fetch sequences by type
        def fetch_seq(seqtype):
            url = f"https://rest.ensembl.org/sequence/id/{tid}?type={seqtype}"
            res = requests.get(url, headers=headers_fasta)
            if res.status_code == 200:
                lines = res.text.strip().split("
")
                return "".join(lines[1:])  # drop FASTA header
            return None

        t_start = t.get("start"); t_end = t.get("end")
        chrom = gene_info["Chromosome"]
        strand = gene_info["Strand"]

        if strand == 1:
            promoter_start = max(1, t_start - promoter_len)
            promoter_end   = t_start - 1
            terminator_start = t_end + 1
            terminator_end   = t_end + terminator_len
        else:
            promoter_start = t_end + 1
            promoter_end   = t_end + promoter_len
            terminator_start = max(1, t_start - terminator_len)
            terminator_end   = t_start - 1

        def fetch_region(start, end):
            region_url = f"https://rest.ensembl.org/sequence/region/{species}/{chrom}:{start}..{end}:{strand}"
            r = requests.get(region_url, headers=headers_fasta)
            if r.status_code == 200:
                return "".join(r.text.strip().split("
")[1:])
            return None

        cdna = fetch_seq("cdna")
        if is_coding:
            cds = fetch_seq("cds")
            utr_list = cdna.split(cds) if (cdna and cds) else []
            if len(utr_list) == 2:
                utr_5, utr_3 = utr_list[0], utr_list[1]
            else:
                utr_5, cds, utr_3 = None, cds, None
        else:
            utr_5 = cds = utr_3 = None

        row = {
            "Gene": gene_info["Gene name"],
            "Transcript ID": tid,
            "Transcript name": tname,
            "Coding": is_coding,
            "mRNA (cDNA)": cdna,
            "5'UTR": utr_5,
            "CDS": cds,
            "3'UTR": utr_3,
            "Protein (aa)": fetch_seq("protein") if is_coding else None,
            f"Promoter ({promoter_len}bp)": fetch_region(promoter_start, promoter_end),
            f"Terminator ({terminator_len}bp)": fetch_region(terminator_start, terminator_end),
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    display(df)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{species}.{symbol}.tsv")
    with open(path, "w") as f:
        f.write("
".join(header_lines) + "
")
        df.to_csv(f, sep="	", index=False)

    print("✅ Created TSV:", path)
    return lookup, path

print("Function loaded.")
```

### Example usage (multiple genes)

```python
gene_list = ["TP53", "BRCA1", "EGFR"]
for symbol in gene_list:
    print(f"🔽 Processing {symbol}...")
    _, path = get_gene_and_transcripts_info(
        species="homo_sapiens",
        symbol=symbol,
        promoter_len=1000,
        terminator_len=500,
        max_transcripts=5,
        output_dir="/content"
    )
    # Recommended: disable auto-download in loops; download later if needed
    # files.download(path)
```

### Mount Google Drive (optional)

```python
# from google.colab import drive
# drive.mount('/content/drive')
```

### Retrieve TP53 (example)

```python
lookup, path = get_gene_and_transcripts_info(
    species="homo_sapiens",
    symbol="TP53",
    promoter_len=100,
    terminator_len=100,
    max_transcripts=3,
    # output_dir="/content/drive/MyDrive/data"
    output_dir="/content"
)
from google.colab import files
files.download(path)
```

---

# Genome‑Wide Retrieval (FASTA + GFF3)

For hundreds to thousands of genes, API calls are **slow/unreliable** and may hit rate limits. Prefer bulk downloads:

* **FASTA**: genome sequences
* **GFF3**: gene models/annotations

## FASTA Format Recap

```
>sequence_id description
ATGCGTAGCTAGCTAGGCTAG...
```

* Header starts with `>`; ID is the first token, rest is description.
* Lines typically wrap every 60–80 characters.
* Often distributed as `.fa.gz` (gzip).

## GFF3 Format Recap

```
seqid  source  type  start  end  score  strand  phase  attributes
chr1   ensembl gene  11869 14409 .      +       .      ID=gene:ENSG...;Name=DDX11L1;biotype=...
```

* 9 tab‑separated columns. No header line. `#` lines are comments.
* 1‑based coordinates.
* Parent/child links via `ID=` and `Parent=`.

## FASTA/GFF3 Naming Consistency

Chromosome names may vary: `1` vs `chr1` vs `chr01`. Prefer **paired FASTA+GFF3** from the *same provider* (e.g., Ensembl) to avoid mismatches.

### Provider notes

| Provider                                   | Pros                                                                    | Watch‑outs                                              |
| ------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| Ensembl                                    | Uniform format across species; consistent FASTA/GFF3; regularly updated | May lag species‑specific DBs for bleeding‑edge curation |
| Species‑specific DBs (FlyBase, TAIR, etc.) | Rich species tools                                                      | Sometimes non‑standard GFF3 quirks                      |

---

# Download Example Data (C. elegans)

Reasons: well‑maintained in Ensembl Metazoa, manageable genome size, eukaryote.

### FASTA (genome DNA)

* Ensembl Metazoa → *C. elegans* → **FASTA**.
* Choose `dna.toplevel.fa.gz` for full chromosomes.
* For speed, you may use a single chromosome file (e.g., **chromosome I**).

### GFF3 (annotations)

* Ensembl Metazoa → *C. elegans* → **GFF3**.
* For speed, use the matching **chromosome I** GFF3 file.

---

# Getting Files into Colab

## 1) `files.upload()`

```python
from google.colab import files
uploaded = files.upload()  # files land in /content/
```

## 2) Left “Files” panel → Upload to session storage

Drag & drop; paths look like `/content/your_file`.

## 3) Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

## 4) Download from public URL

```python
!wget https://example.org/data.fa.gz -O /content/data.fa.gz
```

Summary:

| Method           | Best for             | Reusable? | Size          | Auth | Where                |
| ---------------- | -------------------- | --------- | ------------- | ---- | -------------------- |
| `files.upload()` | Small manual uploads | ❌         | ~100MB        | No   | `/content/`          |
| Files panel      | Temporary assets     | ❌         | ~100MB        | No   | `/content/`          |
| Drive mount      | Large / persistent   | ✅         | Drive limit   | Yes  | `/content/drive/...` |
| `wget`/`curl`    | Public datasets      | ❌         | Net‑dependent | No   | `/content/`          |

---

# Parse GFF3 → Summarize Genes (with `gffutils`)

**Goal:** Read GFF3, summarize per‑gene metadata into a table (chromosome, start/end, strand, length, #transcripts, non‑redundant exon count, attributes), then save TSV.

```python
# Install gffutils if needed
try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

import pandas as pd
import os
from google.colab import files

# Input GFF3 path (adjust as needed)
gff_file = "/content/Caenorhabditis_elegans.WBcel235.61.chromosome.I.gff3.gz"
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = gff_file.removesuffix(".gz").removesuffix(".gff3") + ".gene_info.tsv"

# Create or open the DB
if not os.path.exists(db_fn):
    print("Building GFF database... (this may take a while)")
    db = gffutils.create_db(
        gff_file, db_fn, force=True, keep_order=False, disable_infer_transcripts=True,
        merge_strategy="create_unique", sort_attribute_values=True
    )
    files.download(db_fn)
else:
    db = gffutils.FeatureDB(db_fn)

attribute_keys = set()
rows = []

transcript_types = [
    "transcript", "mRNA", "ncRNA", "lnc_RNA", "miRNA", "tRNA",
    "rRNA", "snRNA", "snoRNA", "scRNA", "antisense_RNA",
    "pseudogenic_transcript", "processed_transcript"
]

for gene in db.features_of_type("gene"):
    gene_id = gene.id
    chrom = gene.chrom
    start = gene.start
    end = gene.end
    strand = gene.strand
    length = end - start + 1

    attr_dict = {k: v[0] for k, v in gene.attributes.items()}
    attribute_keys.update(attr_dict.keys())

    transcript_count = 0
    exon_set = set()
    for transcript in db.children(gene, featuretype=transcript_types, level=1):
        transcript_count += 1
        for exon in db.children(transcript, featuretype="exon"):
            exon_set.add((exon.start, exon.end))

    row = {
        "Name": None,
        "gene_id": None,
        "Chromosome": chrom,
        "Start": start,
        "End": end,
        "Strand": strand,
        "Length": length,
        "Transcript Count": transcript_count,
        "Exon Count": len(exon_set),
    }
    row.update(attr_dict)
    rows.append(row)

main_cols = ["Name", "gene_id", "Chromosome", "Start", "End", "Strand", "Length", "Transcript Count", "Exon Count"]
if "Name" in attribute_keys: attribute_keys.remove("Name")
if "gene_id" in attribute_keys: attribute_keys.remove("gene_id")
attribute_cols = sorted(attribute_keys)

gene_df = pd.DataFrame(rows)[main_cols + attribute_cols]
display(gene_df)

gene_df.to_csv(output_path, sep="	", index=False)
files.download(output_path)
```

---

# Join FASTA + GFF3 → Extract Sequences

**Goal:** For (sampled) genes and their transcripts, build a table with:

* exon counts
* 5'UTR / CDS / 3'UTR sequences
* translated protein sequence (from CDS)
* **Promoter** (upstream) / **Terminator** (downstream)

```python
# Install dependencies if needed
try:
    import gffutils
except ImportError:
    !pip install gffutils
    import gffutils

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
from google.colab import files

# ▼ Input paths (adjust as needed)
gff_file = "/content/Caenorhabditis_elegans.WBcel235.61.chromosome.I.gff3.gz"
fasta_file = "/content/Caenorhabditis_elegans.WBcel235.dna.chromosome.I.fa.gz"
db_fn = gff_file.removesuffix(".gz") + ".db"
output_path = gff_file.removesuffix(".gz").removesuffix(".gff3") + ".rna_seq.tsv"

promoter_len = 100
terminator_len = 100

# Create/open DB
if not os.path.exists(db_fn):
    print("Building GFF database... (this may take a while)")
    db = gffutils.create_db(
        gff_file, db_fn, force=True, keep_order=False, disable_infer_transcripts=True,
        merge_strategy="create_unique", sort_attribute_values=True
    )
    files.download(db_fn)
else:
    db = gffutils.FeatureDB(db_fn)

# Sample genes (use all genes by replacing with list(db.features_of_type("gene")))
sample_genes = random.sample(list(db.features_of_type("gene")), 100)

# Load genome sequences
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

        exon_count = sum(1 for _ in db.children(tx, featuretype="exon"))

        def extract_sequence(start, end):
            # NOTE: gffutils features are 1-based inclusive; adjust when slicing
            seq = genome[chrom][start-1:end]
            return seq.reverse_complement() if strand == "-" else seq

        def get_concat_seq(featuretype):
            parts = list(db.children(tx, featuretype=featuretype, order_by='start'))
            if parts:
                seq = Seq("".join(str(genome[chrom][p.start-1:p.end]) for p in parts))
                if strand == "-":
                    seq = seq.reverse_complement()
                return seq
            return None

        utr5 = get_concat_seq("five_prime_UTR")
        cds  = get_concat_seq("CDS")
        utr3 = get_concat_seq("three_prime_UTR")

        if strand == "+":
            promoter   = extract_sequence(tx.start - promoter_len, tx.start - 1)
            terminator = extract_sequence(tx.end + 1, tx.end + terminator_len)
        else:
            promoter   = extract_sequence(tx.end + 1, tx.end + promoter_len)
            terminator = extract_sequence(tx.start - terminator_len, tx.start - 1)

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
            "Promoter": str(promoter) if promoter else None,
            "Terminator": str(terminator) if terminator else None,
        }
        rows.append(row)

rna_seq_df = pd.DataFrame(rows)
display(rna_seq_df)

rna_seq_df.to_csv(output_path, sep="	", index=False)
files.download(output_path)
```

---

# Edit FASTA Files

## DataFrame → FASTA

Use `rna_seq_df` rows to write FASTA where:

* `id` = `transcript_id`
* description = `gene_id gene_name`
* sequence = the value from `5'UTR` (skip if empty)

```python
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from google.colab import files

records = []
for _, row in rna_seq_df.iterrows():
    seq = row.get("5'UTR", None)
    if not seq:
        continue
    record = SeqRecord(
        Seq(seq),
        id=row.get("transcript_id", ""),
        description=f"{row.get('gene_id', '')} {row.get('gene_name', '')}"
    )
    records.append(record)

output_path = "test_output.fa"
SeqIO.write(records, output_path, "fasta")
files.download(output_path)
```

## FASTA → DataFrame

Read `test_output.fa` back and store `Name`, `Description`, `Sequence` in a TSV.

```python
from Bio import SeqIO
import pandas as pd
from google.colab import files

records = list(SeqIO.parse("test_output.fa", "fasta"))

data = []
for r in records:
    parts = r.description.split(" ", 1)
    name = parts[0]
    desc = parts[1] if len(parts) > 1 else ""
    data.append({"Name": name, "Description": desc, "Sequence": str(r.seq)})

df_fasta = pd.DataFrame(data)
display(df_fasta)

output_path = "test_output.tsv"
df_fasta.to_csv(output_path, sep="	", index=False)
files.download(output_path)
```

## Select First 10 Sequences → Save

```python
from Bio import SeqIO
from google.colab import files

records = list(SeqIO.parse("test_output.fa", "fasta"))
subset = records[:10]

output_path = "test_output_2.fa"
with open(output_path, "w") as f:
    SeqIO.write(subset, f, "fasta")
files.download(output_path)
```

## Trim Each Sequence to First 10 Bases → Save

```python
from Bio import SeqRecord
from Bio import SeqIO
from google.colab import files

short_records = []
for r in SeqIO.parse("test_output.fa", "fasta"):
    short_seq = r.seq[:10]
    new_record = SeqRecord.SeqRecord(short_seq, id=r.id, description=r.description)
    short_records.append(new_record)

output_path = "test_output_3.fa"
with open(output_path, "w") as f:
    SeqIO.write(short_records, f, "fasta")
files.download(output_path)
```

---

# 🎉 Wrap‑Up

* Retrieve sequences from **Ensembl/NCBI**.
* Understand and use **FASTA** and **GFF3**.
* Automate extraction for multiple genes/transcripts.
* Convert between **DataFrame** and **FASTA**.
* Create subsets and trimmed FASTA for downstream tasks.

Use these building blocks for primer design, annotation pipelines, and web‑app backends for sequence analysis.
