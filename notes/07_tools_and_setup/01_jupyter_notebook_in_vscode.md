# Jupyter Notebooks in VS Code - Complete Guide

## Introduction

Jupyter Notebooks are interactive computational documents that combine live code, visualizations, narrative text, and equations. They are the de facto standard for data science, machine learning, and bioinformatics workflows. This guide covers everything you need to use Jupyter Notebooks effectively in Visual Studio Code.

**Why Jupyter + VS Code?**
- IntelliSense and code completion
- Git integration for version control
- Debugging capabilities
- Multiple notebooks in tabs
- Integrated terminal
- Better performance than browser-based Jupyter

**Use Cases:**
- Data exploration and analysis
- Machine learning model development
- Bioinformatics sequence analysis
- Scientific computing and visualization
- Teaching and demonstrations
- Reproducible research

---

## Part 1: Initial Setup

### Prerequisites

**Required Software:**
1. Python 3.7+ installed
2. VS Code installed
3. Virtual environment (recommended)

### Step 1: Create and Activate Virtual Environment

**Why Virtual Environments?**
- Isolate project dependencies
- Prevent package conflicts
- Reproducible environments
- Clean project structure

**Create Virtual Environment:**

```powershell
# Windows PowerShell
python -m venv venv

# Linux/macOS
python3 -m venv venv
```

**Activate Virtual Environment:**

```powershell
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows Command Prompt
venv\Scripts\activate.bat

# Linux/macOS
source venv/bin/activate
```

**Verify Activation:**
```powershell
# Your prompt should show (venv)
(venv) PS C:\project>

# Check Python path
python -c "import sys; print(sys.executable)"
# Should point to venv\Scripts\python.exe
```

**Troubleshooting Activation Errors (Windows):**

If you get "execution of scripts is disabled":
```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
venv\Scripts\Activate.ps1
```

### Step 2: Install Jupyter and Essential Packages

```powershell
# Core Jupyter packages
pip install jupyter notebook ipykernel

# Data science essentials
pip install numpy pandas matplotlib seaborn

# For bioinformatics
pip install biopython

# For machine learning
pip install scikit-learn

# Save dependencies
pip freeze > requirements.txt
```

**Package Purposes:**

| Package | Purpose |
|---------|---------|
| `jupyter` | Jupyter Notebook framework |
| `notebook` | Classic notebook interface |
| `ipykernel` | Python kernel for Jupyter |
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `matplotlib` | Plotting and visualization |
| `seaborn` | Statistical visualizations |
| `biopython` | Bioinformatics tools |
| `scikit-learn` | Machine learning |

### Step 3: Install VS Code Extensions

**Required Extensions:**

1. **Python** (by Microsoft)
   - Extension ID: `ms-python.python`
   - Features: IntelliSense, debugging, linting
   
2. **Jupyter** (by Microsoft)
   - Extension ID: `ms-toolsai.jupyter`
   - Features: Notebook support, kernel management

**Installation Methods:**

**Method 1: Via Extensions Panel**
```
1. Press Ctrl+Shift+X (open Extensions)
2. Search for "Python"
3. Click Install (Microsoft's Python extension)
4. Search for "Jupyter"
5. Click Install (Microsoft's Jupyter extension)
```

**Method 2: Via Command Palette**
```
1. Press Ctrl+Shift+P
2. Type "Extensions: Install Extensions"
3. Search and install both extensions
```

**Method 3: Via Terminal**
```powershell
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
```

**Verify Installation:**
- Both extensions should show "✓ Enabled" in Extensions panel
- Restart VS Code if needed

---

## Part 2: Configuring VS Code for Jupyter

### Select Python Interpreter

**Why This Matters:**
- Ensures notebook uses correct environment
- Access to installed packages
- Consistent execution environment

**Steps:**

```
1. Press Ctrl+Shift+P
2. Type: "Python: Select Interpreter"
3. Choose your venv interpreter:
   - Windows: .\venv\Scripts\python.exe
   - Linux/macOS: ./venv/bin/python
```

**Verify Selected Interpreter:**
- Check bottom-left status bar in VS Code
- Should show: Python 3.x.x ('venv')

**Set as Default for Workspace:**
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe"
}
```

### Open Your Project Folder

```powershell
# Navigate to project directory
cd C:\Users\YourName\projects\my_project

# Open in VS Code
code .
```

**Or:**
- File → Open Folder → Select project directory

**Project Structure Recommendation:**
```
my_project/
├── venv/                    # Virtual environment
├── notebooks/               # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_visualization.ipynb
├── data/                    # Data files
│   ├── raw/
│   └── processed/
├── src/                     # Python modules
│   └── utils.py
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

---

## Part 3: Creating and Using Notebooks

### Create a New Notebook

**Method 1: Command Palette**
```
1. Press Ctrl+Shift+P
2. Type: "Jupyter: Create New Jupyter Notebook"
3. Save as "my_notebook.ipynb"
```

**Method 2: File Explorer**
```
1. Right-click in Explorer panel
2. New File
3. Name: "analysis.ipynb"
4. VS Code auto-detects .ipynb extension
```

**Method 3: Terminal**
```powershell
# Create empty notebook
New-Item -Path "notebooks/analysis.ipynb" -ItemType File
```

### Notebook Interface Overview

```
┌─────────────────────────────────────────────────────┐
│ 🔷 analysis.ipynb                    [Select Kernel]│
├─────────────────────────────────────────────────────┤
│ [ + Code ▼] [▶ Run All] [⟳ Restart] [Variables]   │
├─────────────────────────────────────────────────────┤
│ Cell 1 [Code] ▶                                     │
│ ┌─────────────────────────────────────────────┐    │
│ │ import numpy as np                          │    │
│ │ print("Hello, Jupyter!")                    │    │
│ └─────────────────────────────────────────────┘    │
│ Output:                                             │
│ Hello, Jupyter!                                     │
├─────────────────────────────────────────────────────┤
│ Cell 2 [Markdown] ▶                                │
│ # Data Analysis                                     │
│ This notebook explores...                           │
└─────────────────────────────────────────────────────┘
```

### Select Kernel

**What is a Kernel?**
- Computational engine executing code
- Maintains execution state (variables, imports)
- Each notebook has one active kernel

**Select Kernel:**
```
1. Click "Select Kernel" (top-right of notebook)
2. Choose "Python Environments..."
3. Select your venv: Python 3.x.x ('venv')
```

**Verify Kernel:**
- Top-right should show: Python 3.x.x (venv)
- Kernel indicator shows connection status

---

## Part 4: Working with Cells

### Cell Types

**1. Code Cells**
- Execute Python code
- Display output below cell
- Support rich output (plots, tables, HTML)

**2. Markdown Cells**
- Write formatted text
- Support headings, lists, links
- LaTeX math equations

**3. Raw Cells**
- Plain text, not executed
- Used for documentation

### Running Cells

**Keyboard Shortcuts:**

| Shortcut | Action |
|----------|--------|
| `Shift + Enter` | Run cell, move to next |
| `Ctrl + Enter` | Run cell, stay in same cell |
| `Alt + Enter` | Run cell, insert new cell below |
| `Ctrl + Shift + Enter` | Run all cells |

**Cell Toolbar Buttons:**
- ▶ Run Cell
- ⏹ Stop Execution
- ⟳ Restart Kernel

### Code Cell Example

```python
# Cell 1: Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq

print("Libraries imported successfully!")
```

```python
# Cell 2: Load data
data = pd.read_csv('data/sequences.csv')
print(f"Loaded {len(data)} sequences")
data.head()
```

```python
# Cell 3: Analysis
dna_seq = Seq("ATGCGTAAACCGATGGGCTTTTGA")
protein = dna_seq.translate()

print(f"DNA: {dna_seq}")
print(f"Protein: {protein}")
```

```python
# Cell 4: Visualization
plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title("Sample Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

### Markdown Cell Examples

```markdown
# Main Heading

## Subheading

### Analysis Steps

1. Load data
2. Clean and preprocess
3. Analyze results

**Bold text** and *italic text*

`inline code`

[Link to documentation](https://docs.python.org)

- Bullet point 1
- Bullet point 2

Math equation: $E = mc^2$

Code block:
```python
def hello():
    print("Hello, World!")
```
```

### Cell Management

**Add Cells:**
- Click "+ Code" or "+ Markdown" buttons
- Hover between cells, click "+"
- Press `B` (below) or `A` (above) in command mode

**Delete Cells:**
- Click trash icon on cell
- Press `DD` (double D) in command mode

**Move Cells:**
- Drag cell by left margin
- Click ↑ or ↓ arrows in cell toolbar

**Copy/Paste Cells:**
- `Ctrl + C` to copy
- `Ctrl + V` to paste

---

## Part 5: Advanced Features

### Variables Explorer

**Access Variables:**
```
1. Click "Variables" button in notebook toolbar
2. See all defined variables, types, and values
3. Click variable to inspect details
```

**Example:**
```python
# Define variables
x = 42
name = "Gene Analysis"
data = [1, 2, 3, 4, 5]
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

# View in Variables Explorer:
# x: int = 42
# name: str = "Gene Analysis"
# data: list (5 items)
# df: DataFrame (2 rows × 2 columns)
```

### Interactive Plots with Plotly

```python
# Install plotly
!pip install plotly

import plotly.express as px

# Interactive scatter plot
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                 color="species", hover_data=['petal_width'])
fig.show()
```

### Magic Commands

**IPython Magic Commands:**

```python
# Time execution
%timeit sum(range(1000))

# Time cell execution
%%time
result = [i**2 for i in range(10000)]

# Display matplotlib inline
%matplotlib inline

# List all variables
%whos

# Run external Python file
%run script.py

# Load code from file
%load analysis.py

# Save cell to file
%%writefile utils.py
def calculate_gc(seq):
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

# Execute shell commands
!pip list
!ls -la
```

### Debugging

**Debug a Cell:**
```
1. Set breakpoint: Click left margin of code line
2. Click "Debug Cell" instead of "Run Cell"
3. Use debug toolbar: Step Over, Step Into, Continue
4. Inspect variables in Debug panel
```

**Example:**
```python
# Set breakpoint on line 2
def analyze_sequence(seq):
    gc_content = (seq.count('G') + seq.count('C')) / len(seq)  # Breakpoint here
    return gc_content * 100

result = analyze_sequence("ATGCGC")
```

---

## Part 6: Bioinformatics Examples

### Sequence Analysis Workflow

```python
# Cell 1: Setup
from Bio import SeqIO
from Bio.Seq import Seq
import pandas as pd
import matplotlib.pyplot as plt

# Cell 2: Load FASTA file
sequences = []
for record in SeqIO.parse("data/genes.fasta", "fasta"):
    sequences.append({
        'id': record.id,
        'length': len(record.seq),
        'gc_content': (record.seq.count('G') + record.seq.count('C')) / len(record.seq) * 100
    })

df = pd.DataFrame(sequences)
df.head()

# Cell 3: Analyze GC content distribution
plt.figure(figsize=(10, 6))
plt.hist(df['gc_content'], bins=30, edgecolor='black')
plt.title("GC Content Distribution")
plt.xlabel("GC %")
plt.ylabel("Frequency")
plt.show()

# Cell 4: Find ORFs
def find_orfs(seq, min_length=100):
    orfs = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'ATG':
            for j in range(i+3, len(seq)-2, 3):
                if seq[j:j+3] in ['TAA', 'TAG', 'TGA']:
                    if j - i >= min_length:
                        orfs.append((i, j, seq[i:j+3]))
                    break
    return orfs

# Test on first sequence
test_seq = "ATGCGTAAACCGATGGGCTTTTGA"
orfs = find_orfs(test_seq, min_length=15)
print(f"Found {len(orfs)} ORFs")

# Cell 5: Translate ORFs
for start, end, orf in orfs:
    protein = Seq(orf).translate()
    print(f"Position {start}-{end}: {protein}")
```

### RNA-seq Data Exploration

```python
# Cell 1: Load RNA-seq counts
counts = pd.read_csv("data/rna_counts.csv", index_col=0)
print(f"Shape: {counts.shape}")
counts.head()

# Cell 2: Normalize (CPM)
cpm = counts.div(counts.sum(axis=0), axis=1) * 1e6
cpm.head()

# Cell 3: Visualize top expressed genes
top_genes = cpm.mean(axis=1).nlargest(20)

plt.figure(figsize=(12, 6))
top_genes.plot(kind='barh')
plt.title("Top 20 Expressed Genes")
plt.xlabel("Mean CPM")
plt.tight_layout()
plt.show()

# Cell 4: Sample correlation heatmap
import seaborn as sns

correlation = cpm.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title("Sample Correlation")
plt.show()
```

---

## Part 7: Best Practices

### Notebook Organization

**Structure Guidelines:**
1. **Title and Description** (Markdown cell at top)
2. **Imports** (all in first code cell)
3. **Configuration** (paths, parameters)
4. **Data Loading**
5. **Analysis Sections** (with Markdown headers)
6. **Results and Conclusions**

**Example Template:**

```markdown
# Genome Sequence Analysis
**Author:** Your Name  
**Date:** 2025-11-27  
**Purpose:** Analyze GC content and find ORFs in bacterial genome

## 1. Setup and Imports
```

```python
# Imports
import numpy as np
import pandas as pd
from Bio import SeqIO
```

```markdown
## 2. Data Loading
```

```python
# Load genome
genome = SeqIO.read("genome.fasta", "fasta")
```

### Code Quality

**Use Functions:**
```python
# Good: Reusable function
def calculate_gc_content(seq):
    """Calculate GC content of DNA sequence."""
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

gc = calculate_gc_content("ATGCGC")

# Bad: Repeated code in multiple cells
# gc1 = (seq1.count('G') + seq1.count('C')) / len(seq1) * 100
# gc2 = (seq2.count('G') + seq2.count('C')) / len(seq2) * 100
```

**Clear Variable Names:**
```python
# Good
dna_sequence = "ATGCGT"
gc_content_percentage = 55.2

# Bad
s = "ATGCGT"
x = 55.2
```

### Version Control

**Git Integration:**

```powershell
# Initialize git repository
git init

# Create .gitignore
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore
echo "data/*.csv" >> .gitignore

# Commit notebook
git add notebooks/analysis.ipynb
git commit -m "Add sequence analysis notebook"
```

**Clear Outputs Before Committing:**
```
1. Kernel → Restart & Clear Outputs
2. Save notebook
3. Commit clean version
```

### Performance Tips

**Large Datasets:**
```python
# Use chunking for large files
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# Use Dask for big data
import dask.dataframe as dd
df = dd.read_csv('huge_file.csv')
```

**Optimize Loops:**
```python
# Slow: Python loop
result = []
for i in range(1000000):
    result.append(i ** 2)

# Fast: NumPy vectorization
result = np.arange(1000000) ** 2
```

---

## Part 8: Troubleshooting

### Common Issues

**1. Kernel Not Found**

**Problem:** "Kernel Python 3.x.x (venv) not found"

**Solution:**
```powershell
# Ensure ipykernel is installed in venv
pip install ipykernel

# Register kernel
python -m ipykernel install --user --name=venv --display-name "Python (venv)"

# Restart VS Code
```

**2. Module Not Found**

**Problem:** `ModuleNotFoundError: No module named 'pandas'`

**Solution:**
```python
# Check which Python is running
import sys
print(sys.executable)

# Should show venv path
# If not, reselect interpreter and kernel

# Install missing package in venv
!pip install pandas
```

**3. Kernel Died/Crashed**

**Solutions:**
- Restart kernel: Click ⟳ button
- Check for infinite loops or memory errors
- Reduce dataset size
- Clear outputs and restart fresh

**4. Plots Not Showing**

**Solution:**
```python
# Add magic command
%matplotlib inline

# Or use explicit display
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()  # Important!
```

**5. Slow Performance**

**Solutions:**
- Close unused notebooks
- Clear output of old cells
- Restart kernel periodically
- Use more efficient algorithms (vectorization)

---

## Practice Exercises

### Basic Level

1. **Hello Jupyter**: Create notebook, run cell printing "Hello, World!"

2. **Math Operations**: Create cells performing basic calculations, display results.

3. **Import Test**: Import numpy, pandas, matplotlib, verify installation.

4. **Markdown Practice**: Create formatted documentation with headings, lists, code blocks.

5. **Simple Plot**: Generate line plot of y = x^2 from x = 0 to 10.

### Intermediate Level

6. **Data Loading**: Load CSV file, display first 10 rows, calculate summary statistics.

7. **Function Definition**: Write function to calculate GC content, test on DNA sequences.

8. **Loop Practice**: Process list of sequences, calculate length and GC% for each.

9. **Visualization**: Create bar chart showing sequence lengths distribution.

10. **Magic Commands**: Use `%timeit` to compare performance of different implementations.

### Advanced Level

11. **FASTA Parser**: Load multi-sequence FASTA, create DataFrame with ID, length, GC%.

12. **ORF Finder**: Implement complete ORF finding in all 6 reading frames.

13. **Interactive Dashboard**: Use Plotly to create interactive sequence browser.

14. **Parallel Processing**: Use multiprocessing to analyze large sequence dataset.

15. **Complete Pipeline**: Build end-to-end analysis: load data → clean → analyze → visualize → export results.

---

## Key Takeaways

1. **Jupyter in VS Code** = Interactive notebooks + IDE features (IntelliSense, debugging, Git).

2. **Virtual Environments** = Essential for isolated, reproducible projects.

3. **Extensions Required** = Python + Jupyter extensions (both by Microsoft).

4. **Kernel Selection** = Critical—must match virtual environment.

5. **Cell Types** = Code (executable), Markdown (documentation), Raw (plain text).

6. **Best Practices** = Clear structure, reusable functions, version control, clear outputs before commits.

7. **Bioinformatics** = Ideal platform for sequence analysis, data exploration, visualization.

8. **Troubleshooting** = Most issues solved by restarting kernel or verifying interpreter/kernel selection.

---

## References

- **Jupyter Documentation**: https://jupyter.org/documentation
- **VS Code Jupyter**: https://code.visualstudio.com/docs/datascience/jupyter-notebooks
- **IPython Magic Commands**: https://ipython.readthedocs.io/en/stable/interactive/magics.html
- **Pandas**: https://pandas.pydata.org/docs/
- **Matplotlib**: https://matplotlib.org/stable/contents.html

---

**Next Steps**: Start building your own analysis notebooks! Practice with real datasets and gradually increase complexity.
