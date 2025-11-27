# 🧬 Python for Bioinformatics & Computational Biology

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![Bioinformatics](https://img.shields.io/badge/Bioinformatics-Ready-brightgreen.svg)]()

A **comprehensive, production-quality learning resource** for Python programming with specialized focus on **bioinformatics applications**, text processing, and biological sequence analysis. This repository contains 42+ enhanced tutorials, practical projects, and real-world bioinformatics examples.

---

## 🎯 What You'll Learn

- ✅ **Python Fundamentals** - Data types, operators, control flow, functions
- ✅ **Advanced Programming** - OOP, regex, modules, virtual environments
- ✅ **Bioinformatics Core** - DNA/RNA sequences, FASTA parsing, ORF finding
- ✅ **File Formats** - GFF3, VCF, SAM/BAM, GenBank, FASTQ
- ✅ **API Integration** - NCBI, Ensembl, UniProt data access
- ✅ **Real Projects** - Sequence analyzers, calculators, grading systems
- ✅ **Best Practices** - Clean code, error handling, performance optimization

---

## 🚀 Quick Start for Students

### 🎓 **RECOMMENDED: Google Colab (No Installation Required!)**

**Perfect for students!** No setup needed - just click and start learning.

#### 📖 How to Open Notebooks in Google Colab:

**Method 1: Direct Link (Easiest)**

Replace `github.com` with `colab.research.google.com/github` in any notebook URL:

```
https://github.com/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb
                                    ↓ Replace with ↓
https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb
```

**Method 2: From GitHub**
1. Browse to any `.ipynb` file in this repository
2. Click "Open in Colab" badge (if available)
3. Or copy the URL and use Method 1

#### 🔗 Quick Access Links for Students:

**English Notebooks:**
- [1. Hello World & Basics](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb) ⭐ **START HERE**
- [2. Python Basics](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/2_python_basics_FULL_EN.ipynb)
- [3. Useful Scripts & Syntax](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/3_useful_scripts_basic_syntax_FULL_EN.ipynb)
- [4. Text & Sequences](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/4_text_and_sequence_FULL_EN.ipynb)

**Japanese Notebooks (日本語):**
- [1. Hello World](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/japanise/1_hello_world.ipynb)
- [2. Python 基礎](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/japanise/2_python_basics.ipynb)
- [3. スクリプトと構文](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/japanise/3_useful_scripts_basic_syntax.ipynb)
- [4. テキストとシーケンス](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/japanise/4_text_and_sequence.ipynb)
- [5. 遺伝子配列抽出](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/japanise/5_gene_sequence_extraction.ipynb)

---

### 💻 Option 2: Local Setup (For Advanced Users)

```bash
# Clone the repository
git clone https://github.com/tarik1bosunia/hamid-vai-python-study.git
cd hamid-vai-python-study

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install jupyter numpy pandas biopython requests
```

---

## 📚 Complete Learning Path

### 🎯 **For Students: Start Here!**

**New to Programming?** Follow this simple path:

1. ⭐ **[Open Hello World in Colab](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb)** - Start here!
2. 📖 Read **[Introduction & Setup](./notes/01_fundamentals/01_introduction_and_setup.md)** - Understand basics
3. 📚 Complete all **Phase 1** tutorials below
4. 💪 Do practice exercises (15 per topic)
5. ✅ Move to next phase when comfortable

**Already Know Python?** Jump to:
- 🧬 [Phase 5: Bioinformatics Applications](#-phase-5-bioinformatics-applications) - For biology students
- 🔧 [Phase 4: Advanced Topics](#-phase-4-advanced-topics) - For programmers

---

Follow this structured 7-phase curriculum for optimal learning progression:

### 📂 Phase 1: Python Fundamentals

**Master the core building blocks of Python programming**

| # | Topic | Content | Practice |
|---|-------|---------|----------|
| 1 | [Introduction & Setup](./notes/01_fundamentals/01_introduction_and_setup.md) | Python installation, IDEs, first program | 15 exercises |
| 2 | [Data Types & Input](./notes/01_fundamentals/02_data_types_and_input.md) | Strings, integers, floats, booleans, type conversion | 15 exercises |
| 3 | [Operators](./notes/01_fundamentals/03_operators.md) | Arithmetic, comparison, logical, bitwise operators | 15 exercises |
| 4 | [Strings](./notes/01_fundamentals/04_strings.md) | String methods, formatting, f-strings | 15 exercises |
| 5 | [Data Structures](./notes/01_fundamentals/05_data_structures.md) | Lists, tuples, dictionaries, sets | 15 exercises |
| 6 | [Slicing](./notes/01_fundamentals/06_slicing_in_python.md) | Array slicing, negative indices, step values | 15 exercises |

**Total: ~6 hours** | **90 exercises**

---

### 📂 Phase 2: Control Flow

**Learn to control program execution and handle data**

| # | Topic | Content | Practice |
|---|-------|---------|----------|
| 1 | [Conditional Statements](./notes/02_control_flow/01_conditional_statements.md) | if/elif/else, nested conditions, ternary operator | 15 exercises |
| 2 | [Loops](./notes/02_control_flow/02_loops.md) | for/while loops, break/continue, comprehensions | 15 exercises |
| 3 | [File Handling & Exceptions](./notes/02_control_flow/03_file_handling_and_exceptions.md) | Reading/writing files, try/except, context managers | 15 exercises |

**Total: ~4 hours** | **45 exercises**

---

### 📂 Phase 3: Functions & Utilities

**Write reusable, modular code with best practices**

#### Core Functions
| # | Topic | Content | Practice |
|---|-------|---------|----------|
| 1 | [Functions Basics](./notes/03_functions/01_functions_basics.md) | Definition, parameters, return values, docstrings | 15 exercises |
| 2 | [Useful Scripts & Syntax](./notes/03_functions/02_useful_scripts_and_syntax.md) | Common patterns, idioms, best practices | 15 exercises |

#### Advanced Concepts
- 📌 [Variable Scope](./notes/03_functions/advanced/2_python_variable_scope.md) - Global, local, nonlocal, closures
- 📌 [Mutable Default Arguments](./notes/03_functions/advanced/3_mutable_default_argument.md) - Common pitfalls and solutions
- 📌 [LRU Cache](./notes/03_functions/advanced/4_lru_cache.md) - Performance optimization with memoization
- 📌 [Functions Deep Dive](./notes/03_functions/advanced/function_part2_deep_dive.md) - Lambda, decorators, generators

#### Python Utilities
- 🔧 [Range Function](./notes/03_functions/utilities/1_range_function_in_python.md) - Iteration and sequence generation
- 🔧 [Join Method](./notes/03_functions/utilities/2_join_in_python.md) - String concatenation techniques
- 🔧 [Escape Sequences](./notes/03_functions/utilities/3_escape_sequences.md) - Special characters in strings
- 🔧 [Escaping Braces in f-Strings](./notes/03_functions/utilities/4_Escaping%20Braces%20in%20f-Strings.md) - Advanced formatting
- 🔧 [Naming Conventions](./notes/03_functions/utilities/5_python_identifier_naming_rules_and_conventions.md) - PEP 8 standards

**Total: ~8 hours** | **150+ exercises**

---

### 📂 Phase 4: Advanced Topics

**Master advanced programming concepts and tools**

| # | Topic | Content | Practice |
|---|-------|---------|----------|
| 1 | [Regular Expressions](./notes/04_advanced_topics/01_regex_and_string_handling.md) | Pattern matching, text extraction, validation | 15 exercises |
| 2 | [Object-Oriented Programming](./notes/04_advanced_topics/02_object_oriented_programming.md) | Classes, inheritance, polymorphism, encapsulation | 15 exercises |
| 3 | [Packages & Modules](./notes/04_advanced_topics/03_packages_and_modules.md) | Code organization, imports, package creation | 15 exercises |
| 4 | [Virtual Environments](./notes/04_advanced_topics/04_virtual_environments.md) | venv, conda, dependency management | 15 exercises |
| 5 | [CRUD & APIs](./notes/04_advanced_topics/05_crud_using_requests.md) | HTTP requests, REST APIs, JSON handling | 15 exercises |

#### Regular Expression Deep Dives
- 🎯 [Capture Groups](./notes/04_advanced_topics/regex_details/1_regex_capture_groups.md) - Extract structured data from text
- 🎯 [Named Groups](./notes/04_advanced_topics/regex_details/2_named_groups_in_python_regex.md) - Readable, maintainable patterns
- 🎯 [Dot Metacharacter](./notes/04_advanced_topics/regex_details/regix_symbol/1_dot.md) - Multi-line matching with DOTALL

**Total: ~10 hours** | **120+ exercises**

---

### 📂 Phase 5: Bioinformatics Applications

**Apply Python to real bioinformatics problems**

#### Core Sequence Analysis
| # | Topic | Content | Focus |
|---|-------|---------|-------|
| 1 | [DNA/RNA Sequences](./notes/05_bioinformatics/01_biological_sequences_DNA_RNA.md) | Sequence manipulation, transcription, translation | String operations |
| 2 | [Nucleotide Counter](./notes/05_bioinformatics/02_nucleotide_counter_project.md) | GC content, AT/GC ratios, statistics | File parsing |
| 3 | [Gene Sequence Extraction](./notes/05_bioinformatics/03_gene_sequence_extraction.md) | Coordinate-based extraction, feature parsing | Pattern matching |

#### Bioinformatics Concepts
- 🧬 [Open Reading Frames (ORF)](./notes/05_bioinformatics/concepts/1_orf.md) - Finding coding sequences, 6-frame translation
- 🧬 [FASTA Format](./notes/05_bioinformatics/concepts/2_fasta_file_format.md) - Parsing headers, multi-line sequences, BioPython
- 🧬 [Transcription vs Translation](./notes/05_bioinformatics/concepts/3_transcribe_vs_translate.md) - Central dogma, codon tables, mutations

#### File Formats & Databases
- 📄 [GFF3 Format](./notes/05_bioinformatics/file_formats/gff3.md) - Genome annotation parsing with gffutils
- 📄 [GFF3 to Database](./notes/05_bioinformatics/file_formats/why_dff3_to_db.md) - Performance optimization (300-600x speedup)

#### Real-World Examples
- 💡 [Gene Structure & Transcripts](./notes/05_bioinformatics/example_notebooks/gene_structure_and_transcript_overview.md) - Exons, introns, splicing
- 💡 [RNA Feature Extraction](./notes/05_bioinformatics/example_notebooks/rna_feature_extraction_script_explanation.md) - Complete pipeline walkthrough

**Total: ~12 hours** | **135+ exercises**

---

### 📂 Phase 6: Practice Projects

**Build real applications to solidify your skills**

| Project | Description | Technologies | Complexity |
|---------|-------------|--------------|------------|
| [Mini Calculator](./notes/06_projects/practice/mini_calculator.md) | 3 versions: Basic → Enhanced → Scientific + Bioinformatics calculator | Functions, error handling, user input | ⭐⭐ |
| [Student Grading System](./notes/06_projects/practice/student_grading_system.md) | 3 versions: Single student → Multiple students → Weighted GPA system | Data structures, statistics, file I/O | ⭐⭐⭐ |

**Features:**
- Progressive difficulty levels (basic → intermediate → advanced)
- Complete working code with explanations
- 15 extension exercises per project
- Bioinformatics adaptations included

**Total: ~6 hours** | **30+ exercises**

---

### 📂 Phase 7: Tools & Environment

**Set up professional development environment**

| Tool | Guide | Coverage |
|------|-------|----------|
| [Jupyter in VS Code](./notes/07_tools_and_setup/01_jupyter_notebook_in_vscode.md) | Complete setup guide | Installation, configuration, kernels, debugging, bioinformatics workflows |

**Total: ~2 hours**

---

## 🎓 Key Features

### 📖 Comprehensive Content
- **42+ enhanced tutorials** with 3-5x content expansion
- **600+ practice exercises** (15 per topic)
- **Real bioinformatics examples** throughout
- **Production-quality code** with error handling

### 🧬 Bioinformatics Focus
- Parse FASTA, GFF3, VCF, SAM/BAM, GenBank formats
- Work with NCBI, Ensembl, UniProt APIs
- Implement ORF finding, sequence analysis, feature extraction
- Handle real genomic data and workflows

## 💻 Multi-Format Learning

### 📓 Interactive Notebooks (Best for Students!)

#### English Notebooks
Located in `english/` folder - **Open directly in Colab** (see Quick Start above):

1. **[Hello World & Basics](./english/1_hello_world_FULL_EN.ipynb)** - First steps in Python
2. **[Python Basics](./english/2_python_basics_FULL_EN.ipynb)** - Data types, operators, control flow
3. **[Useful Scripts & Syntax](./english/3_useful_scripts_basic_syntax_FULL_EN.ipynb)** - Common patterns
4. **[Text & Sequences](./english/4_text_and_sequence_FULL_EN.ipynb)** - String manipulation, biological sequences

#### Japanese Notebooks (日本語ノートブック)
Located in `japanise/` folder - **Open directly in Colab**:

1. **[Hello World](./japanise/1_hello_world.ipynb)** - Python入門
2. **[Python Basics](./japanise/2_python_basics.ipynb)** - 基本構文
3. **[Useful Scripts](./japanise/3_useful_scripts_basic_syntax.ipynb)** - よく使うパターン
4. **[Text & Sequences](./japanise/4_text_and_sequence.ipynb)** - 文字列と配列
5. **[Gene Sequence Extraction](./japanise/5_gene_sequence_extraction.ipynb)** - 遺伝子配列の抽出

#### Experimental & Practice Notebooks
- `experiment/` - Work-in-progress notebooks
- `notebooks/` - Additional practice materials

### 📖 Comprehensive Markdown Guides

All content in `notes/` folder with detailed explanations, examples, and exercises:
- **42+ enhanced tutorials** with bioinformatics examples
- **600+ practice exercises** across all topics
- **Progressive difficulty** from basic to advanced
- **Professional code examples** ready to use

---

## 📁 Repository Structure

```
hamid-vai-python-study/
│
├── 📖 README.md                        # This file
├── 📓 notes/                           # Main learning content (42+ files)
│   ├── 01_fundamentals/                # Python basics (6 topics)
│   ├── 02_control_flow/                # Conditionals, loops, files (3 topics)
│   ├── 03_functions/                   # Functions and utilities (11 topics)
│   │   ├── advanced/                   # Scope, decorators, closures (4 topics)
│   │   └── utilities/                  # Range, join, escape sequences (5 topics)
│   ├── 04_advanced_topics/             # OOP, regex, modules (5 topics)
│   │   └── regex_details/              # Detailed regex patterns (3 topics)
│   ├── 05_bioinformatics/              # Sequence analysis (10 topics)
│   │   ├── concepts/                   # ORF, FASTA, translation (3 topics)
│   │   ├── file_formats/               # GFF3, database conversion (2 topics)
│   │   └── example_notebooks/          # Real-world examples (2 topics)
│   ├── 06_projects/                    # Practice projects (2 projects)
│   │   └── practice/                   # Calculator, grading system
│   └── 07_tools_and_setup/             # Development environment (1 topic)
│
├── 📔 english/                         # Jupyter notebooks (English)
│   ├── 1_hello_world_FULL_EN.ipynb
│   ├── 2_python_basics_FULL_EN.ipynb
│   ├── 3_useful_scripts_basic_syntax_FULL_EN.ipynb
│   └── 4_text_and_sequence_FULL_EN.ipynb
│
├── 📔 japanise/                        # Jupyter notebooks (Japanese)
│   ├── 1_hello_world.ipynb
│   ├── 2_python_basics.ipynb
│   ├── 3_useful_scripts_basic_syntax.ipynb
│   ├── 4_text_and_sequence.ipynb
│   └── 5_gene_sequence_extraction.ipynb
│
├── 🧪 experiment/                      # Experimental notebooks
│   └── 4_text_and_sequence.ipynb
│
└── 📒 notebooks/                       # Additional practice notebooks
    └── string.ipynb
```

---

## 🎯 Learning Recommendations

### 📚 For Students (Beginners)
**Perfect if you're new to programming!**

**Week 1-2: Get Started**
1. ⭐ Open [Hello World Colab Notebook](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb)
2. Work through Phase 1: Fundamentals (all 6 topics)
3. Practice exercises after each lesson
4. Use Colab - no installation needed!

**Week 3-4: Build Skills**
1. Complete Phase 2: Control Flow
2. Try the practice notebooks
3. Start simple projects

**Week 5-6: Apply Knowledge**
1. Learn Phase 3: Functions
2. Build the Mini Calculator project
3. Start exploring bioinformatics examples

**Study Tips:**
- ✅ 2-3 hours per day is ideal
- ✅ Complete all exercises before moving forward
- ✅ Use Colab for easy experimentation
- ✅ Ask questions when stuck!

**Estimated Time:** 4-6 weeks

---

### For Absolute Beginners
1. ✅ Start with **Phase 1: Fundamentals** (complete all 6 topics)
2. ✅ Practice all exercises before moving forward
3. ✅ Complete **Phase 2: Control Flow** 
4. ✅ Build basic projects from **Phase 6**

**Estimated Time:** 4-6 weeks (2-3 hours/day)

### For Bioinformatics Students/Researchers
1. ✅ Quick review of **Phases 1-2** (if comfortable with Python basics)
2. ✅ Focus on **Phase 3: Functions** (essential for sequence analysis)
3. ✅ Deep dive into **Phase 5: Bioinformatics Applications**
4. ✅ Study file format parsers and API integration
5. ✅ Adapt projects to your research needs

**Estimated Time:** 3-4 weeks (3-4 hours/day)

### For Advanced Programmers
1. ✅ Skip to **Phase 4: Advanced Topics** (OOP, regex)
2. ✅ Focus on **Phase 5: Bioinformatics** (domain-specific knowledge)
3. ✅ Study API integration and database optimization
4. ✅ Implement custom bioinformatics pipelines

**Estimated Time:** 2-3 weeks (2-3 hours/day)

---

## 🛠️ Prerequisites

### Required
- Computer with internet connection
- Python 3.8 or higher ([Download here](https://www.python.org/downloads/))
- Text editor (VS Code recommended) or Jupyter Notebook

### Recommended Packages
```bash
pip install biopython pandas numpy requests jupyter matplotlib seaborn
```

### Optional (for advanced topics)
```bash
pip install gffutils pysam pyfaidx

 pyvcf reportlab
```

---

## 👥 Target Audience

This course is designed for:

- 🎓 **Beginners** learning Python from scratch
- 🧬 **Biology/Life Science students** entering bioinformatics
- 🔬 **Researchers** working with biological sequence data
- 💻 **Programmers** expanding into computational biology
- 📊 **Data analysts** working with genomic datasets
- 🧪 **Lab scientists** automating sequence analysis workflows

**No prior programming experience required!** Start from Phase 1 and progress at your own pace.

---

## 🌟 Why This Resource?

### ✅ Production Quality
- All content enhanced to professional standards
- Real-world examples and use cases
- Industry best practices included
- Error handling and edge cases covered

### ✅ Bioinformatics Integrated
- Not just generic Python tutorials
- Every concept applied to biological sequences
- Real file formats and databases
- API integration with major bioinformatics resources

### ✅ Progressive Learning
- Carefully structured curriculum
- Building blocks approach
- Each phase prepares for the next
- Clear learning objectives

### ✅ Comprehensive Practice
- 600+ exercises across all topics
- Multiple difficulty levels
- Complete projects with extensions
- Self-assessment opportunities

---

## 📊 Content Statistics

| Metric | Count |
|--------|-------|
| **Enhanced Tutorials** | 42+ files |
| **Practice Exercises** | 600+ exercises |
| **Code Examples** | 1,000+ snippets |
| **Jupyter Notebooks** | 10+ notebooks |
| **Learning Phases** | 7 structured phases |
| **Hours of Content** | 48+ hours |
| **Languages** | English, Japanese |
| **File Formats Covered** | FASTA, GFF3, VCF, SAM, GenBank, FASTQ |
| **APIs Covered** | NCBI, Ensembl, UniProt |

---

## 🤝 Contributing

While this is primarily a learning resource, suggestions and corrections are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- **BioPython** - For excellent bioinformatics tools
- **Python Community** - For comprehensive documentation
- **NCBI, Ensembl, UniProt** - For public APIs and data
- **Students and Researchers** - For feedback and use cases

---

## 📞 Support & Feedback

- 🐛 **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/tarik1bosunia/hamid-vai-python-study/issues)
- 💬 **Discussions**: Ask questions in [GitHub Discussions](https://github.com/tarik1bosunia/hamid-vai-python-study/discussions)
- ⭐ **Star this repo** if you find it helpful!

---

## 🚀 Get Started Now!

### For Students (Recommended Path):

**Step 1: Click here to start** → [Open Hello World in Colab](https://colab.research.google.com/github/tarik1bosunia/hamid-vai-python-study/blob/main/english/1_hello_world_FULL_EN.ipynb) ⭐

**Step 2: Read the guide** → [Phase 1 - Introduction & Setup](./notes/01_fundamentals/01_introduction_and_setup.md)

**Step 3: Explore more notebooks** → See [Quick Start section](#-quick-start-for-students) above

---

### For Developers (Local Setup):

```bash
git clone https://github.com/tarik1bosunia/hamid-vai-python-study.git
cd hamid-vai-python-study
```

**Begin your journey**: [Phase 1 - Introduction & Setup](./notes/01_fundamentals/01_introduction_and_setup.md)

---

<div align="center">

### Happy Learning! 🎉

**Made with ❤️ for Bioinformatics Education**

[⬆ Back to Top](#-python-for-bioinformatics--computational-biology)

</div>
