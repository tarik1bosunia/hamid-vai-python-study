# Named Groups in Python Regex - Complete Guide

## Introduction

**Named capture groups** make regular expressions more readable and maintainable by using descriptive names instead of numeric indexes. They're especially valuable in complex patterns where remembering group numbers becomes difficult.

**Why Named Groups Matter:**
- Self-documenting patterns (readable by others)
- Easier refactoring (adding groups doesn't break existing code)
- Better error messages and debugging
- Direct conversion to dictionaries for structured data
- Essential for complex bioinformatics parsers

**Python Syntax:**
```python
(?P<group_name>pattern)  # Define named group
match.group('group_name')  # Access by name
match.groupdict()         # Get all as dictionary
```

---

## Basic Named Groups

### Simple Example

```python
import re

text = "User: alice, Age: 21"

# With numbered groups (old way)
pattern_numbered = r"User: (\w+), Age: (\d+)"
match = re.search(pattern_numbered, text)
print(match.group(1))  # alice - what is group 1 again?
print(match.group(2))  # 21 - what is group 2?

# With named groups (better way)
pattern_named = r"User: (?P<name>\w+), Age: (?P<age>\d+)"
match = re.search(pattern_named, text)
print(match.group('name'))  # alice - clear!
print(match.group('age'))   # 21 - obvious!
```

### Accessing Named Groups

```python
text = "2024-03-15"
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, text)

# Method 1: Access individually by name
print(match.group('year'))   # 2024
print(match.group('month'))  # 03
print(match.group('day'))    # 15

# Method 2: Get all as dictionary
print(match.groupdict())
# {'year': '2024', 'month': '03', 'day': '15'}

# Method 3: Still works with numbers
print(match.group(1))  # 2024 (first group, even though it's named)
print(match.groups())  # ('2024', '03', '15')
```

---

## Working with Multiple Matches

### Using `re.findall()` with Named Groups

```python
log = """
2024-01-15: Alice scored 92
2024-01-16: Bob scored 85
2024-01-17: Charlie scored 78
"""

# Named groups with findall returns tuples (not dicts!)
pattern = r"(?P<date>\d{4}-\d{2}-\d{2}): (?P<name>\w+) scored (?P<score>\d+)"
matches = re.findall(pattern, log)

print(matches)
# [('2024-01-15', 'Alice', '92'),
#  ('2024-01-16', 'Bob', '85'),
#  ('2024-01-17', 'Charlie', '78')]

# Process as tuples
for date, name, score in matches:
    print(f"{name}: {score} on {date}")
```

### Using `re.finditer()` for Dictionary Access

```python
# finditer() gives Match objects, so groupdict() works!
for match in re.finditer(pattern, log):
    data = match.groupdict()
    print(f"{data['name']}: {data['score']} on {data['date']}")
    
# Or unpack directly
for match in re.finditer(pattern, log):
    print(match.group('name'), match.group('score'))
```

---

## Complex Named Group Patterns

### Email Parser

```python
email_pattern = r'''
    (?P<username>[a-zA-Z0-9._%+-]+)  # Local part
    @                                  # @ symbol
    (?P<domain>[a-zA-Z0-9.-]+)        # Domain name
    \.                                 # Dot
    (?P<tld>[a-zA-Z]{2,})             # Top level domain
'''

email = "john.doe@example.com"
match = re.search(email_pattern, email, re.VERBOSE)

if match:
    info = match.groupdict()
    print(f"Username: {info['username']}")  # john.doe
    print(f"Domain: {info['domain']}")      # example
    print(f"TLD: {info['tld']}")           # com
```

### URL Parser

```python
url_pattern = r'''
    (?P<protocol>https?)://           # http or https
    (?:(?P<subdomain>\w+)\.)?         # Optional subdomain (non-capturing outer group)
    (?P<domain>[\w-]+)                # Domain name
    (?:\.(?P<tld>\w+))?               # Optional TLD
    (?::(?P<port>\d+))?               # Optional port
    (?P<path>/[^\s?]*)?               # Optional path
    (?:\?(?P<query>[^\s]*))?          # Optional query string
'''

urls = [
    "https://www.example.com:8080/path/to/page?id=123",
    "http://api.server.com/endpoint",
    "https://localhost:3000"
]

for url in urls:
    match = re.search(url_pattern, url, re.VERBOSE)
    if match:
        print(f"\nURL: {url}")
        for key, value in match.groupdict().items():
            if value:  # Only print captured values
                print(f"  {key:12s}: {value}")
```

### IP Address Parser

```python
ip_pattern = r'''
    (?P<oct1>\d{1,3})\.
    (?P<oct2>\d{1,3})\.
    (?P<oct3>\d{1,3})\.
    (?P<oct4>\d{1,3})
'''

def parse_ip(ip_string):
    match = re.match(ip_pattern, ip_string, re.VERBOSE)
    if not match:
        return None
    
    octets = match.groupdict()
    
    # Validate each octet is 0-255
    for key, value in octets.items():
        if int(value) > 255:
            return None
    
    return octets

# Test
print(parse_ip("192.168.1.1"))
# {'oct1': '192', 'oct2': '168', 'oct3': '1', 'oct4': '1'}

print(parse_ip("999.1.1.1"))  # None (invalid)
```

---

## Bioinformatics Applications

### FASTA Header Parser

```python
fasta_pattern = r'''
    >(?P<db>\w+)\|                    # Database (sp, tr, etc.)
    (?P<accession>[\w.]+)\|           # Accession number
    (?P<entry>[\w_]+)                 # Entry name
    \s+(?P<description>[^O]+)         # Description
    OS=(?P<organism>[^G]+)            # Organism
    (?:GN=(?P<gene>\w+))?             # Optional gene name
'''

headers = [
    ">sp|P12345|MYC_HUMAN Myc proto-oncogene protein OS=Homo sapiens GN=MYC",
    ">tr|Q9Y6K1|Q9Y6K1_HUMAN Uncharacterized protein OS=Homo sapiens",
]

for header in headers:
    match = re.search(fasta_pattern, header, re.VERBOSE)
    if match:
        info = match.groupdict()
        print(f"\nAccession: {info['accession']}")
        print(f"  Gene: {info['gene'] or 'N/A'}")
        print(f"  Organism: {info['organism'].strip()}")
        print(f"  Description: {info['description'].strip()}")
```

### GFF3 Attribute Parser

```python
def parse_gff3_attributes(attr_string):
    """
    Parse GFF3 attribute column into dictionary.
    Example: "ID=gene001;Name=MYC;Dbxref=HGNC:7553"
    """
    pattern = r'(?P<key>\w+)=(?P<value>[^;]+)'
    
    attributes = {}
    for match in re.finditer(pattern, attr_string):
        key = match.group('key')
        value = match.group('value')
        attributes[key] = value
    
    return attributes

# Test
attrs = "ID=gene001;Name=MYC;Dbxref=HGNC:7553,Ensembl:ENSG00000136997;Note=Oncogene"
parsed = parse_gff3_attributes(attrs)

print(parsed)
# {'ID': 'gene001', 'Name': 'MYC', 'Dbxref': 'HGNC:7553,Ensembl:ENSG00000136997', 'Note': 'Oncogene'}
```

### SAM/BAM Alignment Parser

```python
sam_pattern = r'''
    ^(?P<qname>\S+)\t                # Query name
    (?P<flag>\d+)\t                  # Flag
    (?P<rname>\S+)\t                 # Reference name
    (?P<pos>\d+)\t                   # Position
    (?P<mapq>\d+)\t                  # Mapping quality
    (?P<cigar>\S+)\t                 # CIGAR string
    (?P<rnext>\S+)\t                 # Reference name of mate
    (?P<pnext>\d+)\t                 # Position of mate
    (?P<tlen>-?\d+)\t                # Template length
    (?P<seq>[ATGCN]+)\t              # Sequence
    (?P<qual>\S+)                    # Quality
'''

sam_line = "READ001\t0\tchr1\t12345\t60\t100M\t*\t0\t0\tATGCATGC\tIIIIIIII"

match = re.match(sam_pattern, sam_line, re.VERBOSE)
if match:
    alignment = match.groupdict()
    print(f"Read: {alignment['qname']}")
    print(f"Chromosome: {alignment['rname']}")
    print(f"Position: {alignment['pos']}")
    print(f"CIGAR: {alignment['cigar']}")
    print(f"Sequence: {alignment['seq']}")
```

### VCF Variant Parser

```python
vcf_pattern = r'''
    (?P<chrom>[\w.]+)\t              # Chromosome
    (?P<pos>\d+)\t                   # Position
    (?P<id>[\w.;]+)\t                # ID
    (?P<ref>[ATGCN]+)\t              # Reference allele
    (?P<alt>[ATGCN,]+)\t             # Alternate allele(s)
    (?P<qual>[\d.]+)\t               # Quality score
    (?P<filter>[\w.;]+)\t            # Filter status
    (?P<info>.+)                     # Info field
'''

vcf_line = "chr1\t123456\trs12345\tA\tG\t99.9\tPASS\tDP=100;AF=0.5"

match = re.match(vcf_pattern, vcf_line, re.VERBOSE)
if match:
    variant = match.groupdict()
    print(f"Variant at {variant['chrom']}:{variant['pos']}")
    print(f"  {variant['ref']} → {variant['alt']}")
    print(f"  Quality: {variant['qual']}")
    print(f"  Filter: {variant['filter']}")
```

### Primer Design Output Parser

```python
primer_pattern = r'''
    (?P<direction>Forward|Reverse):\s+
    (?P<sequence>[ATGC]+)\s+
    \(Tm:\s+(?P<tm>[\d.]+)°C,\s+
    GC:\s+(?P<gc>\d+)%\)\s+
    Position:\s+(?P<start>\d+)-(?P<end>\d+)
'''

primer_info = "Forward: ATGCGTACGT (Tm: 58.5°C, GC: 60%) Position: 100-109"

match = re.search(primer_pattern, primer_info, re.VERBOSE)
if match:
    primer = match.groupdict()
    print(f"{primer['direction']} Primer:")
    print(f"  Sequence: {primer['sequence']}")
    print(f"  Tm: {primer['tm']}°C")
    print(f"  GC content: {primer['gc']}%")
    print(f"  Location: {primer['start']}-{primer['end']}")
```

---

## Advanced Techniques

### Named Backreferences

```python
# Find repeated words using named backreference
text = "The the cat sat on the the mat"
pattern = r'\b(?P<word>\w+)\s+(?P=word)\b'  # (?P=word) refers to named group

for match in re.finditer(pattern, text, re.IGNORECASE):
    print(f"Repeated: '{match.group('word')}' at position {match.start()}")

# Output:
# Repeated: 'The' at position 0
# Repeated: 'the' at position 19
```

### Named Groups in `re.sub()`

```python
# Reformat dates using named groups
text = "Events: 03/15/2024 and 12/25/2024"
pattern = r'(?P<month>\d{2})/(?P<day>\d{2})/(?P<year>\d{4})'

# Reference by name in replacement
result = re.sub(pattern, r'\g<year>-\g<month>-\g<day>', text)
print(result)
# Events: 2024-03-15 and 2024-12-25

# Alternative numeric syntax still works
result2 = re.sub(pattern, r'\3-\1-\2', text)
print(result2)  # Same result
```

### Conditional Patterns with Named Groups

```python
# Extract different ID formats
id_pattern = r'''
    (?:
        (?P<ensembl>ENS[A-Z]*\d+(?:\.\d+)?) |  # Ensembl ID
        (?P<uniprot>[A-Z0-9]{6,10}) |          # UniProt ID
        (?P<refseq>[NX][MP]_\d+(?:\.\d+)?)     # RefSeq ID
    )
'''

ids = ["ENSG00000136997", "P12345", "NM_001234.5", "XP_123456.2"]

for id_str in ids:
    match = re.search(id_pattern, id_str, re.VERBOSE)
    if match:
        groups = match.groupdict()
        for db, value in groups.items():
            if value:
                print(f"{id_str} is a {db.upper()} ID")
                break
```

### Creating Structured Data

```python
# Parse multiple entries into structured format
log_entries = """
[2024-01-15 10:30:45] INFO: Server started on port 8080
[2024-01-15 10:31:02] ERROR: Connection failed to database
[2024-01-15 10:31:15] WARNING: High memory usage detected
"""

pattern = r'''
    \[(?P<date>\d{4}-\d{2}-\d{2})\s+
    (?P<time>\d{2}:\d{2}:\d{2})\]\s+
    (?P<level>\w+):\s+
    (?P<message>.+)
'''

logs = []
for match in re.finditer(pattern, log_entries, re.VERBOSE):
    logs.append(match.groupdict())

# Now you have structured data
import json
print(json.dumps(logs, indent=2))
```

---

## Combining Named and Numbered Groups

```python
# Mix named groups for important parts, regular groups for less important
pattern = r'''
    (?P<gene_id>ENS\w+\d+)     # Named: gene ID (important)
    \.(\d+)                     # Unnamed: version (less important)
    \s+
    (?P<symbol>[A-Z0-9]+)      # Named: gene symbol (important)
    \s+\((\d+)\)               # Unnamed: chromosome (less important)
'''

entry = "ENSG00000136997.10 MYC (8)"
match = re.search(pattern, entry, re.VERBOSE)

if match:
    # Access named groups
    print(f"Gene: {match.group('gene_id')}")
    print(f"Symbol: {match.group('symbol')}")
    
    # Access numbered groups
    print(f"Version: {match.group(2)}")
    print(f"Chromosome: {match.group(4)}")
    
    # groupdict() only includes named groups
    print(f"Named groups: {match.groupdict()}")
    # {'gene_id': 'ENSG00000136997', 'symbol': 'MYC'}
```

---

## Converting to Data Structures

### Creating DataFrames from Matches

```python
import pandas as pd

fasta_entries = """
>sp|P12345|MYC_HUMAN Myc protein OS=Homo sapiens GN=MYC
>sp|P04637|P53_HUMAN Cellular tumor antigen p53 OS=Homo sapiens GN=TP53
>sp|P00533|EGFR_HUMAN Epidermal growth factor receptor OS=Homo sapiens GN=EGFR
"""

pattern = r'>sp\|(?P<accession>\w+)\|(?P<entry>[\w_]+)\s+(?P<description>[^O]+)OS=(?P<organism>[^G]+)GN=(?P<gene>\w+)'

# Extract all matches
data = []
for match in re.finditer(pattern, fasta_entries):
    data.append(match.groupdict())

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
#   accession      entry                          description         organism gene
# 0    P12345  MYC_HUMAN                          Myc protein   Homo sapiens    MYC
# 1    P04637  P53_HUMAN   Cellular tumor antigen p53   Homo sapiens   TP53
# 2    P00533 EGFR_HUMAN  Epidermal growth factor receptor   Homo sapiens   EGFR
```

### Creating JSON from Matches

```python
import json

# Parse structured data and convert to JSON
sample_info = """
Sample: S001 Type: tumor Purity: 0.85 Stage: III
Sample: S002 Type: normal Purity: 1.00 Stage: -
Sample: S003 Type: tumor Purity: 0.72 Stage: II
"""

pattern = r'Sample:\s+(?P<id>\S+)\s+Type:\s+(?P<type>\w+)\s+Purity:\s+(?P<purity>[\d.]+)\s+Stage:\s+(?P<stage>[\w-]+)'

samples = []
for match in re.finditer(pattern, sample_info):
    sample_dict = match.groupdict()
    sample_dict['purity'] = float(sample_dict['purity'])  # Convert to number
    samples.append(sample_dict)

# Export to JSON
json_output = json.dumps(samples, indent=2)
print(json_output)
```

---

## Practice Exercises

### Basic Level

1. **Parse Full Name**: Extract first, middle, and last name from "John Q. Public".

2. **Phone Variants**: Handle phone formats like "(555) 123-4567", "555-123-4567", "555.123.4567".

3. **Date Formats**: Parse dates in "DD/MM/YYYY", "MM-DD-YYYY", "YYYY.MM.DD" formats.

4. **Email Components**: Extract username, domain, and TLD from email addresses.

5. **Temperature**: Extract value and unit from "25.5°C" or "77.9°F".

### Intermediate Level

6. **Protein Accession**: Parse different protein ID formats (UniProt, RefSeq, Ensembl).

7. **Citation Parser**: Extract author, year, title, journal from bibliography entries.

8. **Log Entry**: Parse timestamp, severity, module, message from application logs.

9. **BED Format**: Extract chromosome, start, end, name, score, strand from BED file lines.

10. **CIGAR Parser**: Break down CIGAR strings into operations and lengths.

### Advanced Level

11. **Multi-format Parser**: Create single regex handling multiple related formats.

12. **Nested Attributes**: Parse GFF3 attributes with nested key-value pairs.

13. **BLAST Output**: Extract query, subject, identity, E-value, coordinates from BLAST tabular output.

14. **FASTQ Quality**: Parse FASTQ headers with all Illumina metadata.

15. **Complex Citation**: Handle various citation formats (APA, MLA, Chicago) with single pattern.

---

## Best Practices

### 1. Name Groups Descriptively

```python
# Bad: unclear names
pattern = r'(?P<a>\d+)-(?P<b>\d+)-(?P<c>\d+)'

# Good: clear names
pattern = r'(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+)'
```

### 2. Use Non-Capturing Groups for Structure

```python
# Mix named (important) and non-capturing (structure only)
pattern = r'(?:https?://)?(?P<domain>[\w.-]+)(?:/(?P<path>\S+))?'
```

### 3. Validate Extracted Data

```python
def parse_coordinate(coord_string):
    pattern = r'(?P<chrom>chr[\dXY]+):(?P<start>\d+)-(?P<end>\d+)'
    match = re.match(pattern, coord_string)
    
    if not match:
        raise ValueError(f"Invalid coordinate: {coord_string}")
    
    coords = match.groupdict()
    start = int(coords['start'])
    end = int(coords['end'])
    
    if start >= end:
        raise ValueError(f"Start must be less than end: {start} >= {end}")
    
    return coords
```

### 4. Document Complex Patterns

```python
# Use re.VERBOSE and comments
pattern = r'''
    (?P<id>ENS\w+\d+)          # Ensembl gene ID
    \.(?P<version>\d+)         # Version number
    \s+
    (?P<symbol>[A-Z0-9]+)      # Gene symbol
    \s+
    (?P<name>[^(]+)            # Full gene name
    \((?P<synonyms>[^)]+)\)    # Comma-separated synonyms
'''
```

### 5. Handle Optional Groups

```python
def safe_get(match, group_name, default=''):
    """Safely get named group value."""
    value = match.group(group_name)
    return value if value is not None else default

# Usage
match = re.search(r'(?P<required>\w+)(?:\s+(?P<optional>\d+))?', "test")
print(safe_get(match, 'required'))  # test
print(safe_get(match, 'optional', 'N/A'))  # N/A
```

---

## Summary

| Feature | Syntax | Purpose |
|---------|--------|---------|
| Define named group | `(?P<name>pattern)` | Capture with descriptive name |
| Access by name | `match.group('name')` | Retrieve named group |
| All named groups | `match.groupdict()` | Dictionary of all named captures |
| Named backreference | `(?P=name)` | Refer to earlier named group |
| In replacement | `\g<name>` | Use named group in re.sub() |

**Key Advantages:**
- ✅ Self-documenting code
- ✅ Easier maintenance and refactoring
- ✅ Direct conversion to dictionaries/DataFrames
- ✅ Better error messages

---

**Previous Topic**: [Capture Groups Basics](./1_regex_capture_groups.md)

**Related**: [Regular Expressions Guide](../12_advanced_string_handling(regular%20expression).md)
