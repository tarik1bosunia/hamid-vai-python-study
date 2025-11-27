# Regex Capture Groups in Python - Complete Guide

## Introduction

**Capture groups** are one of the most powerful features of regular expressions, allowing you to extract specific portions of matched text. They use parentheses `()` to mark parts of the pattern you want to capture separately.

**Why Capture Groups Matter:**
- Extract structured data from text (emails, phone numbers, dates)
- Parse log files and extract key information
- Split complex strings into components
- Validate and extract biological sequence annotations
- Rearrange text using backreferences

**In Bioinformatics:**
- Extract gene IDs from FASTA headers
- Parse GFF3 feature attributes
- Extract sequence coordinates from alignment results
- Parse BLAST output
- Extract primer sequences with coordinates

---

## Core Concepts

### Basic Capture Group Syntax

```python
import re

# Simple example
text = "User: alice, Age: 21"
pattern = r"User: (\w+), Age: (\d+)"
match = re.search(pattern, text)

print(match.groups())   # ('alice', '21')
print(match.group(1))   # alice
print(match.group(2))   # 21
print(match.group(0))   # User: alice, Age: 21 (entire match)
```

**Pattern Breakdown:**

| Pattern Part | Type           | Meaning                      | Captures |
|--------------|----------------|------------------------------|----------|
| `User:`      | Literal        | Matches "User:" exactly      | No       |
| `(\w+)`      | Capture Group 1| One or more word characters  | Yes      |
| `, Age:`     | Literal        | Matches ", Age:" exactly     | No       |
| `(\d+)`      | Capture Group 2| One or more digits           | Yes      |

### The Match Object Methods

```python
match = re.search(r"(\d+)-(\d+)-(\d+)", "2024-03-15")

# Access individual groups
print(match.group(0))    # 2024-03-15 (entire match)
print(match.group(1))    # 2024 (first group)
print(match.group(2))    # 03 (second group)
print(match.group(3))    # 15 (third group)

# Access all groups as tuple
print(match.groups())    # ('2024', '03', '15')

# Access multiple groups
print(match.group(1, 3)) # ('2024', '15')

# Group start/end positions
print(match.start(1))    # Position where group 1 starts
print(match.end(1))      # Position where group 1 ends
print(match.span(1))     # (start, end) tuple for group 1
```

---

## Working with Multiple Matches

### Using `re.findall()` with Groups

```python
# Single capture group - returns list of strings
text = "Scores: 85, 92, 78, 95"
pattern = r"(\d+)"
scores = re.findall(pattern, text)
print(scores)  # ['85', '92', '78', '95']

# Multiple capture groups - returns list of tuples
log = """
2024-01-15: Alice scored 92
2024-01-16: Bob scored 85
2024-01-17: Charlie scored 78
"""
pattern = r"(\d{4}-\d{2}-\d{2}): (\w+) scored (\d+)"
matches = re.findall(pattern, log)
print(matches)
# [('2024-01-15', 'Alice', '92'),
#  ('2024-01-16', 'Bob', '85'),
#  ('2024-01-17', 'Charlie', '78')]

# Process matches
for date, name, score in matches:
    print(f"{name} got {score} on {date}")
```

### Using `re.finditer()` for Match Objects

```python
text = "Contacts: alice@example.com, bob@test.org"
pattern = r"(\w+)@([\w.]+)"

for match in re.finditer(pattern, text):
    username = match.group(1)
    domain = match.group(2)
    print(f"User: {username}, Domain: {domain}")
    print(f"  Found at position {match.start()}-{match.end()}")

# Output:
# User: alice, Domain: example.com
#   Found at position 10-28
# User: bob, Domain: test.org
#   Found at position 30-42
```

---

## Non-Capturing Groups

Sometimes you need grouping for alternation or repetition but don't want to capture the content.

### Syntax: `(?:pattern)`

```python
# Capturing group (creates group)
pattern1 = r"(https?)://(\w+)"
match1 = re.search(pattern1, "https://example")
print(match1.groups())  # ('https', 'example')

# Non-capturing group (no group created)
pattern2 = r"(?:https?)://(\w+)"
match2 = re.search(pattern2, "https://example")
print(match2.groups())  # ('example',) - only one group!
```

### When to Use Non-Capturing Groups

```python
# Extract version numbers, ignore protocol
text = "Download from http://v2.5.1 or https://v3.0.2"
pattern = r"(?:https?://)v(\d+\.\d+\.\d+)"

versions = re.findall(pattern, text)
print(versions)  # ['2.5.1', '3.0.2']

# Without non-capturing group, you'd get tuples:
bad_pattern = r"(https?://)v(\d+\.\d+\.\d+)"
result = re.findall(bad_pattern, text)
print(result)  # [('http://', '2.5.1'), ('https://', '3.0.2')]
```

---

## Nested Capture Groups

Groups can be nested, and they're numbered by the position of their opening parenthesis.

```python
text = "Phone: (555) 123-4567"
pattern = r"Phone: (\((\d{3})\) (\d{3})-(\d{4}))"
match = re.search(pattern, text)

print(match.group(0))  # Phone: (555) 123-4567
print(match.group(1))  # (555) 123-4567
print(match.group(2))  # 555 (nested inside group 1)
print(match.group(3))  # 123
print(match.group(4))  # 4567

# All groups
print(match.groups())  # ('(555) 123-4567', '555', '123', '4567')
```

### Complex Nesting Example

```python
html = '<div class="content">Hello</div>'
pattern = r'<(\w+)(?: class="([^"]+)")?>([^<]+)</\1>'
match = re.search(pattern, html)

print(match.group(1))  # div (tag name)
print(match.group(2))  # content (class name)
print(match.group(3))  # Hello (content)
```

---

## Backreferences

Backreferences allow you to refer to previously captured groups within the same pattern.

### Syntax: `\1`, `\2`, etc.

```python
# Find repeated words
text = "The the cat sat on the the mat"
pattern = r"\b(\w+)\s+\1\b"  # \1 refers to whatever group 1 matched

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)  # ['the', 'the']

# Find all occurrences with context
for match in re.finditer(pattern, text, re.IGNORECASE):
    print(f"Repeated word: {match.group(1)} at position {match.start()}")
```

### Matching Paired HTML Tags

```python
html = """
<b>Bold text</b>
<i>Italic text</i>
<b>More bold</b>
"""

pattern = r'<(\w+)>([^<]+)</\1>'
matches = re.findall(pattern, html)
print(matches)
# [('b', 'Bold text'), ('i', 'Italic text'), ('b', 'More bold')]

# \1 ensures closing tag matches opening tag
```

### Finding Repeated Sequences

```python
# Find tandem repeats in DNA sequence
dna = "ATGCATGCATGCGGCCGGCC"
pattern = r'([ATGC]{4,})\1+'  # Find sequence repeated 2+ times

match = re.search(pattern, dna)
if match:
    print(f"Repeat unit: {match.group(1)}")
    print(f"Full repeat: {match.group(0)}")
# Repeat unit: ATGC
# Full repeat: ATGCATGCATGC
```

---

## Bioinformatics Applications

### Parsing FASTA Headers

```python
import re

fasta_header = ">sp|P12345|GENE_HUMAN Protein description OS=Homo sapiens GN=GENE"

# Extract all components
pattern = r'>(\w+)\|(\w+)\|(\w+)\s+([^O]+)OS=([^G]+)GN=(\w+)'
match = re.search(pattern, fasta_header)

if match:
    db, accession, entry, description, organism, gene = match.groups()
    print(f"Database: {db}")
    print(f"Accession: {accession}")
    print(f"Entry: {entry}")
    print(f"Description: {description.strip()}")
    print(f"Organism: {organism.strip()}")
    print(f"Gene: {gene}")
```

### Extracting Coordinates from SAM/BAM

```python
# SAM alignment format
sam_line = "READ001	0	chr1	12345	60	100M	*	0	0	ATGC...	IIII..."

# Extract read name, chromosome, position, CIGAR
pattern = r'^(\S+)\t\d+\t(\S+)\t(\d+)\t\d+\t(\S+)'
match = re.search(pattern, sam_line)

if match:
    read_name, chrom, pos, cigar = match.groups()
    print(f"Read: {read_name}, Chr: {chrom}, Pos: {pos}, CIGAR: {cigar}")
```

### Parsing GFF3 Attributes

```python
# GFF3 attribute string
attributes = "ID=gene001;Name=MYC;Dbxref=HGNC:7553,Ensembl:ENSG00000136997"

# Extract key-value pairs
pattern = r'(\w+)=([^;]+)'
attrs = dict(re.findall(pattern, attributes))

print(attrs)
# {'ID': 'gene001', 'Name': 'MYC', 'Dbxref': 'HGNC:7553,Ensembl:ENSG00000136997'}
```

### Extracting ORF Coordinates

```python
orf_annotation = "ORF1 start:100 end:450 strand:+ frame:0"

pattern = r'(\w+)\s+start:(\d+)\s+end:(\d+)\s+strand:([+-])\s+frame:(\d)'
match = re.search(pattern, orf_annotation)

if match:
    orf_id, start, end, strand, frame = match.groups()
    print(f"ORF: {orf_id}")
    print(f"Coordinates: {start}-{end} ({strand})")
    print(f"Reading frame: {frame}")
```

### Parsing Primer Information

```python
primer_data = "Forward: ATGCGTACGT (Tm: 58.5°C, GC: 60%) Position: 100-109"

pattern = r'(\w+):\s+([ATGC]+)\s+\(Tm:\s+([\d.]+)°C,\s+GC:\s+(\d+)%\)\s+Position:\s+(\d+)-(\d+)'
match = re.search(pattern, primer_data)

if match:
    direction, sequence, tm, gc, start, end = match.groups()
    print(f"{direction} primer: {sequence}")
    print(f"Tm: {tm}°C, GC content: {gc}%")
    print(f"Position: {start}-{end}")
```

---

## Advanced Techniques

### Conditional Extraction

```python
# Extract email or phone (whichever is present)
contacts = [
    "Contact: alice@example.com",
    "Contact: (555) 123-4567",
    "Contact: bob@test.org"
]

email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
phone_pattern = r'\((\d{3})\)\s+(\d{3})-(\d{4})'

for contact in contacts:
    email = re.search(email_pattern, contact)
    phone = re.search(phone_pattern, contact)
    
    if email:
        print(f"Email: {email.group(1)}")
    elif phone:
        print(f"Phone: ({phone.group(1)}) {phone.group(2)}-{phone.group(3)}")
```

### Using Groups with `re.sub()`

```python
# Reformat dates from MM/DD/YYYY to YYYY-MM-DD
text = "Event on 03/15/2024 and 12/25/2024"
pattern = r'(\d{2})/(\d{2})/(\d{4})'
result = re.sub(pattern, r'\3-\1-\2', text)
print(result)  # Event on 2024-03-15 and 2024-12-25

# Add spaces to DNA sequence
sequence = "ATGCGTACGTTAGC"
spaced = re.sub(r'([ATGC]{3})', r'\1 ', sequence)
print(spaced)  # ATG CGT ACG TTA GC
```

### Group Validation

```python
# Validate and extract components
def parse_gene_id(gene_id):
    """
    Parse gene ID like: ENSG00000136997.10
    Extract: prefix, numeric ID, version
    """
    pattern = r'^([A-Z]+)(\d+)\.(\d+)$'
    match = re.match(pattern, gene_id)
    
    if not match:
        raise ValueError(f"Invalid gene ID: {gene_id}")
    
    prefix, numeric_id, version = match.groups()
    return {
        'prefix': prefix,
        'numeric_id': numeric_id,
        'version': int(version)
    }

try:
    info = parse_gene_id("ENSG00000136997.10")
    print(info)
    # {'prefix': 'ENSG', 'numeric_id': '00000136997', 'version': 10}
except ValueError as e:
    print(e)
```

---

## Practice Exercises

### Basic Level

1. **Extract Names**: Extract first and last names from "Smith, John" format.

2. **Parse Time**: Extract hours, minutes, seconds from "14:30:45".

3. **Get Domain**: Extract domain from email addresses.

4. **Split Phone**: Extract area code, prefix, and number from "(555) 123-4567".

5. **Parse Version**: Extract major, minor, patch from "v2.5.1".

### Intermediate Level

6. **FASTA Parser**: Extract sequence ID and length from FASTA headers.

7. **Log Parser**: Extract timestamp, level, and message from log lines.

8. **URL Components**: Extract protocol, domain, port, and path from URLs.

9. **Citation Parser**: Extract author, year, title from formatted citations.

10. **Coordinate Parser**: Extract chromosome, start, end from "chr1:12345-67890".

### Advanced Level

11. **Multi-format Date**: Handle dates in multiple formats (MM/DD/YYYY, DD-MM-YYYY, ISO).

12. **Nested HTML**: Extract content from nested HTML tags.

13. **VCF Parser**: Extract all fields from VCF file format lines.

14. **BLAST Parser**: Extract query, subject, score, E-value from BLAST output.

15. **Complex FASTA**: Handle multi-line FASTA with various header formats and extract all metadata.

---

## Common Pitfalls

### Greedy vs Non-Greedy

```python
text = "<b>Hello</b> <i>World</i>"

# Greedy (wrong for this case)
greedy = re.findall(r'<.+>', text)
print(greedy)  # ['<b>Hello</b> <i>World</i>'] - too much!

# Non-greedy (correct)
non_greedy = re.findall(r'<.+?>', text)
print(non_greedy)  # ['<b>', '</b>', '<i>', '</i>'] - just tags!

# Better: be specific
specific = re.findall(r'<(\w+)>([^<]+)</\1>', text)
print(specific)  # [('b', 'Hello'), ('i', 'World')]
```

### Forgetting to Escape Special Characters

```python
# Wrong - . matches any character
pattern = r'(\d+).(\d+)'
match = re.search(pattern, "3x14")  # Matches! (x is "any char")

# Correct - escape the dot
pattern = r'(\d+)\.(\d+)'
match = re.search(pattern, "3.14")  # Now only matches literal dot
```

### Group Numbering with Non-Capturing Groups

```python
# Without non-capturing group
pattern1 = r'(https?)://(www\.)?(\w+)'
match = re.search(pattern1, 'https://www.example')
print(match.groups())  # ('https', 'www.', 'example') - 3 groups

# With non-capturing group
pattern2 = r'(https?)://(?:www\.)?(\w+)'
match = re.search(pattern2, 'https://www.example')
print(match.groups())  # ('https', 'example') - only 2 groups!
```

---

## Summary

| Feature               | Syntax          | Purpose                          |
|-----------------------|-----------------|----------------------------------|
| Capture group         | `(pattern)`     | Capture matched text             |
| Non-capturing group   | `(?:pattern)`   | Group without capturing          |
| Backreference         | `\1`, `\2`      | Refer to captured group          |
| `match.group(n)`      | Method          | Access group n                   |
| `match.groups()`      | Method          | All groups as tuple              |
| `match.span(n)`       | Method          | Start/end position of group n    |
| Named groups          | `(?P<name>...)`  | Capture with name (see next file)|

---

**Next Topic**: [Named Groups in Python Regex](./2_named_groups_in_python_regex.md) - Learn how to use descriptive names instead of numbers!

**See Also**: [Regular Expressions Guide](../12_advanced_string_handling(regular%20expression).md)
