# Day 9: File Handling & Exceptions

### 📂 File Handling in Python

Python allows reading and writing files using the built-in `open()` function.

**Syntax:**

```python
open(filename, mode)
```

### ✅ File Modes

* `'r'` → Read (default, error if file not found)
* `'w'` → Write (creates/overwrites file)
* `'a'` → Append (adds to end of file)
* `'r+'` → Read and Write

---

### ✅ Example 1: Writing and Reading a File (Colab Local Storage)

```python
# Writing to a file
with open("example.txt", "w") as f:
    f.write("Hello from Google Colab!\n")
    f.write("This file is stored in Colab's virtual machine.\n")

# Reading the file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)
```

**Output:**

```
Hello from Google Colab!
This file is stored in Colab's virtual machine.
```

⚠️ Note: This file will be deleted once the Colab session ends.

---

### ✅ Example 2: Saving File Permanently to Google Drive

```python
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Save file into Drive
with open("/content/drive/My Drive/example.txt", "w") as f:
    f.write("This file is saved permanently in Google Drive!")

# Read the file back
with open("/content/drive/My Drive/example.txt", "r") as f:
    print(f.read())
```

---

### ✅ Example 3: Upload File from Computer to Colab

```python
from google.colab import files

# Upload a file from your local computer
uploaded = files.upload()  # Choose file(s) manually from local PC

# Read the uploaded file
for fn in uploaded.keys():
    with open(fn, "r") as f:
        print(f.read())
```

---

### ✅ Example 4: Download File from Colab to Computer

```python
from google.colab import files

# Write some data into a file
with open("notes.txt", "w") as f:
    f.write("This file will be downloaded.")

# Download to your computer
files.download("notes.txt")
```

---

## ⚠️ Exception Handling

Exceptions are errors that occur during runtime. We can handle them with `try` and `except`.

### ✅ Example 5: Basic Exception

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
```

---

### ✅ Example 6: Multiple Exceptions

```python
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid number!")
except Exception as e:
    print("Other error:", e)
```

---

### ✅ Example 7: finally Block

`finally` runs whether there is an error or not.

```python
try:
    f = open("file.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Program finished.")
```

---

### 📝 Practice Tasks (Day 9)

1. Write a program to create a file and write your name into it.
2. Append your age to the same file.
3. Read the file and print its contents line by line.
4. Handle the case where the file does not exist.
5. Write a program that divides two numbers but handles division by zero using exceptions.
6. Save a file into Google Drive from Colab and read it back.
7. Upload a text file from your computer into Colab and print its contents.
8. Download a generated file from Colab to your computer.
