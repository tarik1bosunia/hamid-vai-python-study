# Day 1: Introduction & Setup

## 🐍 What is Python? Why Use It?

**Python** is a high-level, interpreted programming language created by Guido van Rossum in 1991. It has become one of the most popular programming languages in the world, especially in scientific computing and bioinformatics.

### Key Characteristics

* **High-level**: Abstracts complex computer details, allowing you to focus on logic
* **Interpreted**: Code runs line-by-line without compilation, making debugging easier
* **Dynamically typed**: Variable types are determined automatically at runtime
* **Multi-paradigm**: Supports procedural, object-oriented, and functional programming

### Why Python for Bioinformatics?

1. **Readable Syntax**: Python reads almost like English, making it perfect for scientists without extensive programming backgrounds
2. **Rich Ecosystem**: Libraries like Biopython, NumPy, Pandas streamline biological data analysis
3. **Large Community**: Extensive documentation, tutorials, and Stack Overflow support
4. **Cross-platform**: Write once, run on Windows, Mac, or Linux
5. **Integration**: Easily interfaces with other tools and databases
6. **Rapid Development**: Prototype and test ideas quickly

### Common Applications

* **Web Development**: Django, Flask frameworks
* **Data Science & AI/ML**: Pandas, scikit-learn, TensorFlow
* **Bioinformatics**: Sequence analysis, genomics, proteomics
* **Automation & Scripting**: Task automation, data processing pipelines
* **Scientific Computing**: NumPy, SciPy for numerical analysis

---

## 💻 Setting Up Your Environment

### Option 1: Google Colab (Recommended for Beginners)

**Google Colab** is a free, cloud-based Jupyter Notebook environment that requires no setup.

**Advantages:**
- ✓ No installation required
- ✓ Free GPU/TPU access
- ✓ Automatically saves to Google Drive
- ✓ Pre-installed popular libraries
- ✓ Easy sharing and collaboration

**How to Access:**
1. Go to https://colab.research.google.com
2. Sign in with your Google account
3. Click "New Notebook"

**Understanding Colab Interface:**
- **Cells**: Building blocks of notebooks
  - **Code cells**: Write and execute Python code
  - **Text cells**: Write explanations using Markdown
- **Runtime**: The virtual computer running your code
  - Connect: Start the runtime
  - Restart: Clear memory and variables
  - Run all: Execute all cells in sequence
- **Saving**: Notebooks auto-save to Google Drive

**Keyboard Shortcuts:**
- `Ctrl + Enter`: Run current cell
- `Shift + Enter`: Run cell and move to next
- `Ctrl + M, B`: Insert cell below
- `Ctrl + M, A`: Insert cell above

### Option 2: Local Installation

**For Windows/Mac/Linux:**
1. Download Python from https://python.org (version 3.8+)
2. Install an IDE:
   - VS Code (lightweight, extensible)
   - PyCharm (feature-rich, beginner-friendly)
   - Jupyter Notebook (interactive, great for data analysis)

---

## 👩‍💻 Your First Python Program

Let's write the traditional "Hello, World!" program:

```python
# My first Python program
print("Hello, World!")
```

**Output:**

```
Hello, World!
```

### Understanding the Code

- `print()`: A built-in function that displays output to the screen
- `"Hello, World!"`: A string (text data) enclosed in quotes
- `#`: Begins a comment (ignored by Python)

### Try It Yourself

```python
# Different ways to use print()
print("Hello, Bioinformatics!")
print('Single quotes work too')
print(2 + 2)  # You can print numbers and expressions
print("Python", "is", "awesome")  # Multiple items separated by spaces
```

**Output:**

```
Hello, Bioinformatics!
Single quotes work too
4
Python is awesome
```

---

## ✍️ Comments: Documenting Your Code

Comments are essential for making your code understandable. They're ignored by Python but crucial for humans reading your code (including future you!).

### Single-Line Comments

```python
# This is a single-line comment
# Use them to explain what the next line does

# Calculate the area of a rectangle
area = length * width  # You can also add comments at the end of lines
```

### Multi-Line Comments

```python
"""
This is a multi-line comment (docstring).
Use them for longer explanations.
They're often used to document functions and classes.
"""

'''
You can also use single quotes
for multi-line comments.
'''
```

### Best Practices for Comments

✅ **DO:**
- Explain WHY, not just WHAT
- Document complex logic
- Note assumptions or limitations
- Include examples when helpful

❌ **DON'T:**
- State the obvious (`x = 5  # assign 5 to x`)
- Leave outdated comments
- Over-comment simple code

**Example:**

```python
# Good comment
gc_content = (g_count + c_count) / total_bases * 100  # GC content affects DNA stability

# Bad comment
gc_content = (g_count + c_count) / total_bases * 100  # Calculate GC content
```

---

## 📦 Variables: Storing and Managing Data

Variables are named containers that store values. Think of them as labeled boxes where you put information.

### Creating Variables

```python
# Assigning values to variables
name = "Alice"           # String (text)
age = 20                 # Integer (whole number)
pi = 3.1416              # Float (decimal number)
is_student = True        # Boolean (True/False)

# Printing variables
print(name)
print(age)
print(pi)
print(is_student)
```

**Output:**

```
Alice
20
3.1416
True
```

### Python's Dynamic Typing

Unlike languages like Java or C++, Python automatically determines variable types:

```python
x = 10        # x is an integer
print(type(x))  # <class 'int'>

x = "DNA"     # Now x is a string
print(type(x))  # <class 'str'>

x = 3.14      # Now x is a float
print(type(x))  # <class 'float'>
```

### Variable Naming Rules

**Must Follow:**
- Start with a letter (a-z, A-Z) or underscore (_)
- Contain only letters, numbers, and underscores
- Cannot be a Python keyword (`if`, `for`, `class`, etc.)

**Best Practices:**
- Use descriptive names: `gene_count` not `gc`
- Use snake_case: `sequence_length` not `sequenceLength`
- Avoid single letters (except in loops: `i`, `j`, `k`)
- CONSTANTS in UPPER_CASE: `MAX_SEQUENCE_LENGTH = 1000`

```python
# Good variable names
dna_sequence = "ATCG"
nucleotide_count = 1000
gc_content_percentage = 52.5

# Poor variable names (but valid)
x = "ATCG"
n = 1000
a = 52.5
```

### Multiple Assignments

```python
# Assign same value to multiple variables
x = y = z = 0

# Assign different values in one line
name, age, city = "Alice", 25, "Boston"

# Swap variables
a, b = 10, 20
a, b = b, a  # Now a=20, b=10
```

---

## 🧬 Practical Example: Bioinformatics Context

Let's combine what we learned in a bioinformatics-relevant example:

```python
# DNA Sequence Analysis - Introduction
# This program stores and displays basic information about a DNA sequence

# Store a DNA sequence
dna_sequence = "ATCGATCGATCG"

# Store metadata
sequence_id = "SEQ_001"
organism = "E. coli"
sequence_length = 12  # Number of bases

# Display information
print("Sequence Analysis Report")
print("=" * 30)  # Print a separator line
print("ID:", sequence_id)
print("Organism:", organism)
print("Sequence:", dna_sequence)
print("Length:", sequence_length, "bases")
```

**Output:**

```
Sequence Analysis Report
==============================
ID: SEQ_001
Organism: E. coli
Sequence: ATCGATCGATCG
Length: 12 bases
```

---

## 📝 Practice Tasks (Day 1)

Complete these exercises to reinforce your learning:

### Basic Exercises

1. **Personal Info**: Write a program that prints your name, age, and favorite programming language.

2. **Favorite Number**: Store your favorite number in a variable and print a message about it.

3. **Simple Calculator**: Create variables for two numbers, add them, and print the result with a descriptive message.

4. **Code Documentation**: Take exercise 3 and add meaningful comments explaining each step.

### Intermediate Challenges

5. **DNA Basics**: Create variables for the four DNA bases (A, T, G, C) with descriptions and print them nicely formatted.

6. **Variable Swap**: Create two variables with values 100 and 200. Swap their values and print before/after.

7. **Multiple Data Types**: Create one variable for each data type (int, float, str, bool) related to biology and print them with their types.

### Advanced Challenge

8. **Lab Report Header**: Create a small program that displays a formatted lab report header with:
   - Experiment name
   - Date
   - Researcher name
   - Sample ID
   - Use variables and comments appropriately

---

## 💡 Key Takeaways

✓ Python is powerful yet beginner-friendly, ideal for bioinformatics
✓ Google Colab provides a free, easy-to-use environment for learning
✓ `print()` displays output to the screen
✓ Comments (#) document your code for humans
✓ Variables store data and are dynamically typed
✓ Good naming conventions make code readable and maintainable

**Next**: Day 2 - Data Types & Input (Understanding how Python handles different types of information)
