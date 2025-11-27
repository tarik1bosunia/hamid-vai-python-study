# Day 20: Virtual Environments & Project Setup

## 🔧 Professional Python Project Management

Master **virtual environments** to create isolated, reproducible Python projects for bioinformatics. Learn best practices for dependency management, project structure, and collaboration - essential skills for research and production code.

### Why Virtual Environments?

- **Isolation**: Each project has its own dependencies
- **Reproducibility**: Share exact package versions with collaborators
- **No Conflicts**: Different projects can use different package versions
- **Clean System**: Don't clutter global Python installation
- **Best Practice**: Required for professional development

---

## 🎯 Learning Objectives

By the end of this guide, you will:

✓ Understand what virtual environments are and why they matter  
✓ Create and activate virtual environments  
✓ Install packages in isolated environments  
✓ Manage dependencies with requirements.txt  
✓ Structure bioinformatics projects professionally  
✓ Use pip effectively  
✓ Share reproducible projects  

---

## 🧩 Part 1: Understanding Virtual Environments

### What is a Virtual Environment?

A virtual environment is an **isolated Python installation** separate from your system Python. It has its own:

- Python interpreter (or link to one)
- Package installation directory
- Scripts and executables

### Why Use Them?

**Problem without virtual environments:**

```
System Python 3.10
├── BioPython 1.79
├── Pandas 1.5.0
└── NumPy 1.23.0

Project A needs: BioPython 1.79, Pandas 1.5.0
Project B needs: BioPython 1.81, Pandas 2.0.0  ❌ CONFLICT!
```

**Solution with virtual environments:**

```
System Python 3.10
│
├── venv_project_a/
│   ├── BioPython 1.79
│   └── Pandas 1.5.0
│
└── venv_project_b/
    ├── BioPython 1.81
    └── Pandas 2.0.0
```

---

## 🧩 Part 2: Creating Virtual Environments

### Using venv (Built-in)

```bash
# Windows PowerShell
# Navigate to your project directory
cd F:\my_bioinformatics_project

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# You'll see (venv) in your prompt:
# (venv) PS F:\my_bioinformatics_project>

# Deactivate when done
deactivate
```

```bash
# Linux/Mac
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate
```

### Using conda (Recommended for Data Science)

```bash
# Create environment with specific Python version
conda create -n bioinfo python=3.10

# Activate environment
conda activate bioinfo

# Install packages
conda install biopython numpy pandas

# Deactivate
conda deactivate

# List environments
conda env list

# Remove environment
conda env remove -n bioinfo
```

### Naming Conventions

```bash
# Project-specific
python -m venv venv_genome_analyzer
python -m venv venv_rnaseq_pipeline

# Or simply
python -m venv venv
python -m venv env
python -m venv .venv

# Conda environments
conda create -n genome_analyzer
conda create -n rnaseq_pipeline
```

---

## 🧩 Part 3: Managing Packages

### Installing Packages

```bash
# After activating environment

# Install single package
pip install biopython

# Install specific version
pip install biopython==1.79

# Install latest compatible with constraint
pip install "biopython>=1.79,<2.0"

# Install multiple packages
pip install biopython pandas numpy matplotlib

# Install from requirements file
pip install -r requirements.txt

# Upgrade package
pip install --upgrade biopython

# Uninstall package
pip uninstall biopython
```

### Checking Installed Packages

```bash
# List all installed packages
pip list

# Show details about specific package
pip show biopython

# Check outdated packages
pip list --outdated

# Export installed packages
pip freeze > requirements.txt
```

### Understanding requirements.txt

```txt
# requirements.txt - exact versions (pip freeze output)
biopython==1.81
numpy==1.24.3
pandas==2.0.2
matplotlib==3.7.1
```

```txt
# requirements.txt - flexible versions (recommended)
biopython>=1.79
numpy>=1.23
pandas>=1.5
matplotlib>=3.5

# With comments
# Core bioinformatics
biopython>=1.79  # Sequence analysis

# Data processing
numpy>=1.23      # Numerical operations
pandas>=1.5      # DataFrame manipulation

# Visualization
matplotlib>=3.5  # Plotting
```

---

## 🧩 Part 4: Project Structure

### Basic Bioinformatics Project

```
genome_analyzer/
│
├── venv/                      # Virtual environment (don't commit)
│
├── data/                      # Input data
│   ├── raw/
│   │   ├── sequences.fasta
│   │   └── annotations.gff
│   └── processed/
│       └── filtered.fasta
│
├── src/                       # Source code
│   ├── __init__.py
│   ├── parsers.py            # File parsers
│   ├── analysis.py           # Analysis functions
│   └── visualization.py      # Plotting functions
│
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── test_parsers.py
│   └── test_analysis.py
│
├── notebooks/                 # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   └── 02_analysis.ipynb
│
├── scripts/                   # Executable scripts
│   ├── run_analysis.py
│   └── generate_report.py
│
├── results/                   # Output files
│   ├── figures/
│   └── tables/
│
├── docs/                      # Documentation
│   └── README.md
│
├── .gitignore                # Git ignore file
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── setup.py                  # Package installation (optional)
```

### .gitignore File

```gitignore
# .gitignore - Files to exclude from version control

# Virtual environments
venv/
env/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Jupyter Notebook
.ipynb_checkpoints/

# Data files (often too large)
data/raw/*
data/processed/*
*.fasta
*.fastq
*.bam
*.vcf

# Results (regeneratable)
results/

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db
```

### README.md Template

```markdown
# Genome Analyzer

Comprehensive toolkit for analyzing genomic sequences.

## Features

- FASTA/FASTQ parsing
- ORF detection
- GC content analysis
- Motif scanning
- Visualization

## Installation

```bash
# Clone repository
git clone https://github.com/username/genome_analyzer.git
cd genome_analyzer

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\Activate.ps1

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```python
from src.parsers import parse_fasta
from src.analysis import find_orfs

# Parse sequences
sequences = parse_fasta('data/raw/sequences.fasta')

# Find ORFs
for seq_id, data in sequences.items():
    orfs = find_orfs(data['sequence'])
    print(f"{seq_id}: {len(orfs)} ORFs found")
```

## Project Structure

```
genome_analyzer/
├── src/           # Source code
├── tests/         # Unit tests
├── notebooks/     # Jupyter notebooks
├── data/          # Input data
└── results/       # Output files
```

## Dependencies

- Python 3.8+
- BioPython >= 1.79
- NumPy >= 1.23
- Pandas >= 1.5

## License

MIT License
```

---

## 🧩 Part 5: Workflow Examples

### Starting a New Project

```bash
# 1. Create project directory
mkdir rnaseq_analysis
cd rnaseq_analysis

# 2. Initialize git (optional but recommended)
git init

# 3. Create virtual environment
python -m venv venv

# 4. Activate environment
.\venv\Scripts\Activate.ps1  # Windows
# source venv/bin/activate   # Linux/Mac

# 5. Create project structure
mkdir src data tests notebooks results
New-Item src/__init__.py, tests/__init__.py

# 6. Create requirements.txt
New-Item requirements.txt

# 7. Install packages
pip install biopython numpy pandas matplotlib
pip freeze > requirements.txt

# 8. Create .gitignore
New-Item .gitignore
# Add: venv/, __pycache__/, data/, results/

# 9. Create README.md
New-Item README.md
```

### Sharing Your Project

```bash
# 1. Export dependencies
pip freeze > requirements.txt

# 2. Create comprehensive requirements.txt
# Edit to remove unnecessary packages and add comments

# 3. Test installation
deactivate
python -m venv test_venv
.\test_venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 4. Commit to git
git add .
git commit -m "Initial project setup"
git push origin main
```

### Collaborator Setup

```bash
# 1. Clone repository
git clone https://github.com/username/rnaseq_analysis.git
cd rnaseq_analysis

# 2. Create virtual environment
python -m venv venv

# 3. Activate environment
.\venv\Scripts\Activate.ps1  # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Ready to work!
python scripts/run_analysis.py
```

---

## 🧩 Part 6: Best Practices

### Dependency Management

```python
# Bad: No version specification
# requirements.txt
biopython
pandas
numpy

# Good: Version ranges
# requirements.txt
biopython>=1.79,<2.0
pandas>=1.5,<3.0
numpy>=1.23,<2.0

# Better: Group by purpose
# requirements.txt
# Core dependencies
biopython>=1.79,<2.0

# Data processing
pandas>=1.5,<3.0
numpy>=1.23,<2.0

# Visualization
matplotlib>=3.5,<4.0
seaborn>=0.12

# Development dependencies (optional)
pytest>=7.0
black>=23.0
```

### Multiple Requirement Files

```bash
# requirements/
├── base.txt           # Core dependencies
├── dev.txt            # Development tools
└── production.txt     # Production-only

# base.txt
biopython>=1.79
pandas>=1.5
numpy>=1.23

# dev.txt
-r base.txt           # Include base requirements
pytest>=7.0
black>=23.0
jupyter>=1.0

# Install for development
pip install -r requirements/dev.txt
```

### Environment Variables

```python
# config.py
import os
from pathlib import Path

# Use environment variables for configuration
DATA_DIR = Path(os.getenv('DATA_DIR', 'data'))
RESULTS_DIR = Path(os.getenv('RESULTS_DIR', 'results'))
NUM_THREADS = int(os.getenv('NUM_THREADS', '4'))

# Load from .env file
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('NCBI_API_KEY')
```

### Testing Your Environment

```python
# check_environment.py
"""Verify environment setup"""

import sys

def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required")
        return False
    
    print("✓ Python version OK")
    return True

def check_packages():
    """Check required packages"""
    required = {
        'Bio': 'biopython',
        'numpy': 'numpy',
        'pandas': 'pandas',
        'matplotlib': 'matplotlib'
    }
    
    all_ok = True
    
    for module, package in required.items():
        try:
            __import__(module)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"❌ {package} not found")
            all_ok = False
    
    return all_ok

if __name__ == "__main__":
    print("Checking environment setup...\n")
    
    python_ok = check_python_version()
    packages_ok = check_packages()
    
    if python_ok and packages_ok:
        print("\n✓ Environment ready!")
    else:
        print("\n❌ Environment setup incomplete")
        print("Run: pip install -r requirements.txt")
```

---

## 🧩 Part 7: Conda vs venv

### Comparison

| Feature | venv | conda |
|---------|------|-------|
| Built-in | ✓ Yes | ✗ No (install Anaconda/Miniconda) |
| Python version | Uses system Python | Can install different Python versions |
| Package manager | pip | conda (also supports pip) |
| Non-Python packages | ✗ No | ✓ Yes (R, C libraries) |
| Best for | Simple projects | Data science, complex dependencies |
| Speed | Fast | Slower (solves dependencies) |

### When to Use venv

```bash
# Simple bioinformatics script
# Only Python packages needed
# Quick setup required

python -m venv venv
pip install biopython pandas
```

### When to Use conda

```bash
# Complex bioinformatics pipeline
# Need R integration
# Need system libraries (e.g., samtools)
# Data science project

conda create -n pipeline python=3.10
conda install -c bioconda biopython samtools star
conda install pandas numpy matplotlib
```

### Using Both

```bash
# Create conda environment with base packages
conda create -n myproject python=3.10 numpy pandas
conda activate myproject

# Use pip for packages not in conda
pip install specialized-bio-package
```

---

## 📝 Practice Tasks (Day 20)

### Basic Exercises

1. **Create Environment**: Create a virtual environment named `bioproject` and activate it.

2. **Install Packages**: Install BioPython, NumPy, and Pandas in your virtual environment.

3. **Export Requirements**: Use `pip freeze` to create `requirements.txt`.

4. **Fresh Install**: Create a new environment and install from `requirements.txt`.

5. **Check Packages**: Use `pip show` to view details of installed BioPython.

### Intermediate Challenges

6. **Project Structure**: Create a complete project structure with src, data, tests directories.

7. **Multiple Environments**: Create two environments with different package versions.

8. **Gitignore**: Write a comprehensive `.gitignore` for a bioinformatics project.

9. **README**: Write a professional README.md with installation instructions.

10. **Environment Check**: Write a script that verifies all required packages are installed.

### Advanced Challenges

11. **Conda Project**: Set up a project using conda with BioPython, R, and system tools.

12. **Multiple Requirements**: Create base.txt and dev.txt with different dependencies.

13. **CI/CD Setup**: Write GitHub Actions workflow to test installation in fresh environment.

14. **Docker Container**: Create Dockerfile that sets up environment and installs dependencies.

15. **Package Project**: Create `setup.py` to make your project installable with `pip install -e .`

---

## 💡 Key Takeaways

✓ **Virtual environments** isolate project dependencies  
✓ **venv** is built-in, simple, good for most projects  
✓ **conda** better for data science, complex dependencies  
✓ **Always activate** environment before installing packages  
✓ **requirements.txt** ensures reproducibility  
✓ **pip freeze** captures exact versions  
✓ **Version ranges** provide flexibility (>=1.79,<2.0)  
✓ **.gitignore** prevents committing venv/ directory  
✓ **Project structure** improves maintainability  
✓ **Document setup** in README.md  
✓ **Test clean install** before sharing  
✓ **One environment per project** is best practice  
✓ **Update regularly** but test after updates  
✓ **Share requirements.txt** not the venv/ directory  
✓ **Professional projects** use virtual environments  

**Next**: Web APIs & CRUD Operations for Bioinformatics
