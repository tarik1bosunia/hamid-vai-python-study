# Day 9: File Handling & Exception Handling

## 📂 Understanding File Handling

**File handling** allows programs to read data from files and write data to files. This is essential for working with biological data stored in various file formats (FASTA, FASTQ, GFF, VCF, etc.). Python provides built-in functions and context managers to handle files safely and efficiently.

### Why File Handling Matters in Bioinformatics

- Read sequence data from FASTA/FASTQ files
- Parse annotation files (GFF3, GTF)
- Process large datasets that don't fit in memory
- Save analysis results permanently
- Batch process multiple files
- Import/export data between tools
- Create analysis pipelines

---

## 🔹 File Operations Overview

| Operation | Description | Mode |
|-----------|-------------|------|
| Read | Open and read existing file | `'r'` |
| Write | Create new file or overwrite existing | `'w'` |
| Append | Add content to end of existing file | `'a'` |
| Read/Write | Both read and write | `'r+'` |
| Write/Read | Create for reading and writing | `'w+'` |
| Binary Read | Read binary files | `'rb'` |
| Binary Write | Write binary files | `'wb'` |

### File Handling Syntax

```python
# Basic approach (manual close)
file = open('filename.txt', 'r')
content = file.read()
file.close()

# Recommended approach (with statement - auto close)
with open('filename.txt', 'r') as file:
    content = file.read()
    # file automatically closed when block ends
```

---

## ✅ Reading Files

### Reading Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `read()` | Read entire file as single string | String |
| `read(n)` | Read n characters | String |
| `readline()` | Read one line | String |
| `readlines()` | Read all lines into list | List of strings |
| Iteration | Loop through file line by line | String per iteration |

### Basic Reading Examples

```python
# Read entire file
with open('sequence.txt', 'r') as file:
    content = file.read()
    print(content)

# Read specific number of characters
with open('sequence.txt', 'r') as file:
    first_20 = file.read(20)
    print(first_20)

# Read one line
with open('sequence.txt', 'r') as file:
    line = file.readline()
    print(line)

# Read all lines into list
with open('sequence.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline

# Iterate line by line (memory efficient)
with open('sequence.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

### Bioinformatics Reading Examples

```python
# Read FASTA file (simplified)
def read_fasta_simple(filename):
    """Read simple FASTA file"""
    with open(filename, 'r') as file:
        header = ""
        sequence = ""
        
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:  # Save previous sequence
                    print(f"Header: {header}")
                    print(f"Sequence: {sequence}")
                    print(f"Length: {len(sequence)} bp\n")
                header = line[1:]  # Remove '>'
                sequence = ""
            else:
                sequence += line
        
        # Don't forget last sequence
        if sequence:
            print(f"Header: {header}")
            print(f"Sequence: {sequence}")
            print(f"Length: {len(sequence)} bp")

# Read quality scores
def read_quality_file(filename):
    """Read file with quality scores"""
    scores = []
    with open(filename, 'r') as file:
        for line in file:
            score = int(line.strip())
            scores.append(score)
    return scores

# Read CSV-like data
def read_gene_expression(filename):
    """Read gene expression data"""
    data = []
    with open(filename, 'r') as file:
        header = file.readline().strip().split(',')
        print(f"Columns: {header}")
        
        for line in file:
            values = line.strip().split(',')
            data.append(values)
    return data

# Read sequences from multi-line file
def read_sequences(filename):
    """Read multiple sequences"""
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            seq = line.strip()
            if seq:  # Skip empty lines
                sequences.append(seq)
    return sequences
```

---

## ✅ Writing Files

### Writing Methods

| Method | Description |
|--------|-------------|
| `write(string)` | Write string to file |
| `writelines(list)` | Write list of strings to file |

### Basic Writing Examples

```python
# Write to file (overwrites existing)
with open('output.txt', 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('output.txt', 'w') as file:
    file.writelines(lines)

# Append to existing file
with open('output.txt', 'a') as file:
    file.write("New line added\n")

# Write using print function
with open('output.txt', 'w') as file:
    print("First line", file=file)
    print("Second line", file=file)
```

### Bioinformatics Writing Examples

```python
# Write FASTA format
def write_fasta(filename, sequences):
    """Write sequences in FASTA format"""
    with open(filename, 'w') as file:
        for i, seq in enumerate(sequences, start=1):
            file.write(f">sequence_{i}\n")
            file.write(f"{seq}\n")

# Example usage
sequences = ["ATCGATCG", "GCTAGCTA", "TAGCTAGC"]
write_fasta('output.fasta', sequences)

# Write analysis results
def write_gc_results(filename, sequences):
    """Write GC content analysis results"""
    with open(filename, 'w') as file:
        file.write("Sequence\tLength\tGC_Content\n")
        
        for seq in sequences:
            length = len(seq)
            gc_count = seq.count('G') + seq.count('C')
            gc_percent = (gc_count / length * 100) if length > 0 else 0
            file.write(f"{seq}\t{length}\t{gc_percent:.2f}%\n")

# Write quality report
def write_quality_report(filename, reads, qualities):
    """Write quality report for reads"""
    with open(filename, 'w') as file:
        file.write("Read Quality Report\n")
        file.write("=" * 50 + "\n\n")
        
        passed = 0
        failed = 0
        
        for i, (read, qual) in enumerate(zip(reads, qualities), start=1):
            status = "PASS" if qual >= 30 else "FAIL"
            file.write(f"Read {i}: {read}\n")
            file.write(f"  Quality: {qual} - {status}\n\n")
            
            if qual >= 30:
                passed += 1
            else:
                failed += 1
        
        file.write(f"\nSummary: {passed} passed, {failed} failed\n")

# Write processed sequences
def write_cleaned_sequences(input_file, output_file):
    """Remove invalid characters and write clean sequences"""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            seq = line.strip().upper()
            # Keep only valid nucleotides
            cleaned = ''.join([base for base in seq if base in 'ATCG'])
            if cleaned:
                outfile.write(cleaned + '\n')
```

---

## ✅ File Paths and Existence

### Working with Paths

```python
import os

# Check if file exists
if os.path.exists('sequence.txt'):
    print("File exists")
else:
    print("File not found")

# Check if it's a file or directory
if os.path.isfile('sequence.txt'):
    print("It's a file")
if os.path.isdir('data'):
    print("It's a directory")

# Get file size
size = os.path.getsize('sequence.txt')
print(f"File size: {size} bytes")

# List files in directory
files = os.listdir('.')
for file in files:
    print(file)

# Create directory
if not os.path.exists('results'):
    os.mkdir('results')

# Join path components (cross-platform)
filepath = os.path.join('data', 'sequences', 'input.fasta')
print(filepath)
```

### Pathlib (Modern Approach)

```python
from pathlib import Path

# Create path object
file_path = Path('data/sequence.txt')

# Check existence
if file_path.exists():
    print("File exists")

# Read file
content = file_path.read_text()

# Write file
file_path.write_text("New content")

# Get file info
print(f"Name: {file_path.name}")
print(f"Suffix: {file_path.suffix}")
print(f"Parent: {file_path.parent}")

# Create directory
output_dir = Path('results')
output_dir.mkdir(exist_ok=True)

# Iterate over files
data_dir = Path('data')
for file in data_dir.glob('*.fasta'):
    print(file)
```

---

## ⚠️ Exception Handling

**Exceptions** are errors that occur during program execution. Proper exception handling prevents crashes and provides meaningful error messages.

### Exception Handling Syntax

```python
try:
    # code that might raise an exception
    risky_operation()
except ExceptionType:
    # handle specific exception
    handle_error()
except AnotherExceptionType:
    # handle different exception
    handle_different_error()
else:
    # executes if no exception occurred
    success_code()
finally:
    # always executes (cleanup)
    cleanup_code()
```

### Common Exception Types

| Exception | Description | Example |
|-----------|-------------|---------|
| `FileNotFoundError` | File doesn't exist | Opening non-existent file |
| `PermissionError` | No permission to access | Writing to protected file |
| `ValueError` | Invalid value | `int("abc")` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `KeyError` | Key not in dictionary | `dict['missing_key']` |
| `IndexError` | Index out of range | `list[100]` when list has 10 items |
| `TypeError` | Wrong type | `"abc" + 5` |
| `IOError` | Input/Output error | Disk full, corrupted file |

---

## ✅ Basic Exception Handling

### Simple Examples

```python
# Handle file not found
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

# Handle division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    result = None

# Handle invalid input
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format!")
    number = 0

# Multiple exceptions
try:
    value = int(input("Enter number: "))
    result = 100 / value
except ValueError:
    print("Invalid input - not a number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Using else and finally

```python
# else block (executes if no exception)
try:
    with open('data.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
    print(f"Length: {len(data)} characters")

# finally block (always executes)
file = None
try:
    file = open('data.txt', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
    print("Cleanup complete")
```

---

## ✅ Exception Handling for File Operations

### Bioinformatics Examples

```python
# Safe FASTA reader
def read_fasta_safe(filename):
    """Read FASTA with error handling"""
    try:
        sequences = {}
        with open(filename, 'r') as file:
            header = None
            sequence = []
            
            for line_num, line in enumerate(file, start=1):
                line = line.strip()
                
                if line.startswith('>'):
                    # Save previous sequence
                    if header:
                        sequences[header] = ''.join(sequence)
                    header = line[1:]
                    sequence = []
                elif line:
                    # Validate sequence
                    if not set(line.upper()).issubset(set('ATCGN')):
                        print(f"Warning: Invalid characters at line {line_num}")
                    sequence.append(line.upper())
            
            # Save last sequence
            if header:
                sequences[header] = ''.join(sequence)
        
        return sequences
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Safe file writing with validation
def write_sequences_safe(filename, sequences):
    """Write sequences with error handling"""
    try:
        # Validate sequences first
        for seq in sequences:
            if not isinstance(seq, str):
                raise ValueError("All sequences must be strings")
            if not seq:
                raise ValueError("Empty sequence found")
        
        # Write to file
        with open(filename, 'w') as file:
            for i, seq in enumerate(sequences, start=1):
                file.write(f">sequence_{i}\n")
                file.write(f"{seq}\n")
        
        print(f"Successfully wrote {len(sequences)} sequences to {filename}")
        return True
    
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except ValueError as e:
        print(f"Validation error: {e}")
        return False
    except IOError as e:
        print(f"I/O error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

# Process file with recovery
def process_with_recovery(input_file, output_file):
    """Process file with error recovery"""
    processed_count = 0
    error_count = 0
    
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                for line_num, line in enumerate(infile, start=1):
                    try:
                        seq = line.strip().upper()
                        
                        # Validate
                        if not seq:
                            continue
                        
                        if not set(seq).issubset(set('ATCG')):
                            raise ValueError("Invalid nucleotides")
                        
                        # Calculate GC content
                        gc = (seq.count('G') + seq.count('C')) / len(seq) * 100
                        
                        # Write result
                        outfile.write(f"{seq}\t{gc:.2f}\n")
                        processed_count += 1
                    
                    except ValueError as e:
                        error_count += 1
                        print(f"Line {line_num}: {e} - skipping")
                        continue
        
        print(f"\nProcessing complete:")
        print(f"  Processed: {processed_count}")
        print(f"  Errors: {error_count}")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
    except Exception as e:
        print(f"Fatal error: {e}")
```

---

## 🧬 Practical Bioinformatics Examples

### Example 1: FASTA File Parser with Error Handling

```python
def parse_fasta(filename):
    """Complete FASTA parser with error handling"""
    sequences = []
    
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        
        with open(filename, 'r') as file:
            current_header = None
            current_sequence = []
            line_count = 0
            
            for line in file:
                line_count += 1
                line = line.strip()
                
                if not line:  # Skip empty lines
                    continue
                
                if line.startswith('>'):
                    # Save previous sequence
                    if current_header is not None:
                        seq_data = {
                            'header': current_header,
                            'sequence': ''.join(current_sequence),
                            'length': len(''.join(current_sequence))
                        }
                        sequences.append(seq_data)
                    
                    # Start new sequence
                    current_header = line[1:]
                    current_sequence = []
                
                elif line.startswith(';'):
                    # Comment line - skip
                    continue
                
                else:
                    # Sequence line
                    if current_header is None:
                        raise ValueError(f"Sequence data before header at line {line_count}")
                    current_sequence.append(line.upper())
            
            # Don't forget last sequence
            if current_header is not None:
                seq_data = {
                    'header': current_header,
                    'sequence': ''.join(current_sequence),
                    'length': len(''.join(current_sequence))
                }
                sequences.append(seq_data)
        
        print(f"Successfully parsed {len(sequences)} sequences")
        return sequences
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Format error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
sequences = parse_fasta('sequences.fasta')
if sequences:
    for seq in sequences:
        print(f"{seq['header']}: {seq['length']} bp")
```

### Example 2: Batch Sequence Processor

```python
def batch_process_sequences(input_dir, output_dir):
    """Process all FASTA files in a directory"""
    
    try:
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Find all FASTA files
        fasta_files = [f for f in os.listdir(input_dir) 
                      if f.endswith(('.fasta', '.fa'))]
        
        if not fasta_files:
            print(f"No FASTA files found in {input_dir}")
            return
        
        print(f"Found {len(fasta_files)} files to process")
        
        results = []
        
        for filename in fasta_files:
            try:
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, f"processed_{filename}")
                
                print(f"\nProcessing {filename}...")
                
                # Read sequences
                with open(input_path, 'r') as infile:
                    sequences = []
                    current_seq = ""
                    
                    for line in infile:
                        line = line.strip()
                        if line.startswith('>'):
                            if current_seq:
                                sequences.append(current_seq)
                            current_seq = ""
                        else:
                            current_seq += line
                    
                    if current_seq:
                        sequences.append(current_seq)
                
                # Process and write
                with open(output_path, 'w') as outfile:
                    outfile.write(f"# Analysis of {filename}\n")
                    outfile.write("Sequence\tLength\tGC%\tValid\n")
                    
                    for seq in sequences:
                        length = len(seq)
                        gc = (seq.count('G') + seq.count('C')) / length * 100 if length > 0 else 0
                        valid = set(seq.upper()).issubset(set('ATCGN'))
                        
                        outfile.write(f"{seq[:20]}...\t{length}\t{gc:.2f}\t{valid}\n")
                
                results.append({
                    'file': filename,
                    'sequences': len(sequences),
                    'status': 'Success'
                })
                
            except Exception as e:
                print(f"  Error processing {filename}: {e}")
                results.append({
                    'file': filename,
                    'sequences': 0,
                    'status': f'Error: {e}'
                })
        
        # Write summary
        summary_path = os.path.join(output_dir, 'summary.txt')
        with open(summary_path, 'w') as summary:
            summary.write("Batch Processing Summary\n")
            summary.write("=" * 50 + "\n\n")
            
            for result in results:
                summary.write(f"File: {result['file']}\n")
                summary.write(f"  Sequences: {result['sequences']}\n")
                summary.write(f"  Status: {result['status']}\n\n")
        
        print(f"\nProcessing complete. Results in {output_dir}")
    
    except Exception as e:
        print(f"Fatal error: {e}")
```

---

## 📝 Practice Tasks (Day 9)

### Basic Exercises

1. **File Writer**: Create a file named `sequences.txt` and write three DNA sequences to it, one per line.

2. **File Reader**: Read the `sequences.txt` file and print each sequence with its length.

3. **Append to File**: Add two more sequences to the existing `sequences.txt` file.

4. **Line Counter**: Write a program that counts the number of lines in a text file.

5. **Exception Handler**: Write a program that tries to open a file. Handle the case where the file doesn't exist.

### Intermediate Challenges

6. **FASTA Writer**: Create a function that writes sequences in FASTA format (header line starting with `>`, followed by sequence).

7. **Quality Filter**: Read a file with quality scores (one per line), filter scores ≥30, and write them to a new file.

8. **Sequence Validator**: Read sequences from a file, validate each one (only ATCG), and write a report showing valid/invalid status.

9. **GC Calculator**: Read sequences from a file, calculate GC content for each, and write results to a CSV file.

10. **Error Logger**: Create a program that processes sequences and logs any errors to a separate error log file.

### Advanced Challenges

11. **FASTA Parser**: Write a complete FASTA parser that handles:
    - Multiple sequences
    - Multi-line sequences
    - Comments (lines starting with `;`)
    - Error handling for malformed files

12. **Batch Processor**: Create a program that processes all `.fasta` files in a directory and generates summary statistics for each.

13. **Safe File Converter**: Write a converter that reads sequences from one format and writes to another, with comprehensive error handling and validation.

14. **Sequence Database**: Create a simple sequence database system that can:
    - Add sequences to file
    - Search for sequences
    - Update sequences
    - Delete sequences
    - Handle all file errors gracefully

15. **Pipeline Manager**: Build a file processing pipeline that:
    - Validates input files
    - Processes data
    - Generates reports
    - Logs all operations
    - Recovers from errors without data loss

---

## 💡 Key Takeaways

✓ Use `with open()` for automatic file closing  
✓ `'r'` for reading, `'w'` for writing (overwrites), `'a'` for appending  
✓ `read()` gets entire file, `readline()` gets one line, iterate for line-by-line  
✓ Always handle exceptions when working with files  
✓ Check file existence with `os.path.exists()` before opening  
✓ Use `try-except` blocks to catch and handle errors gracefully  
✓ `finally` blocks ensure cleanup code always runs  
✓ Multiple `except` blocks handle different exception types  
✓ Pathlib provides modern, object-oriented file handling  
✓ Validate data before processing to catch errors early  
✓ Log errors for debugging and monitoring  
✓ Use specific exception types rather than catching all exceptions  

**Next**: Day 10-11 - Functions (Creating reusable code and organizing programs)
