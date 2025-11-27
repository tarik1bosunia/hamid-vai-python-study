# 🐍 Python Modules and Packages

## 📘 What is a Module?

A **module** in Python is a single `.py` file that contains code — such as functions, classes, or variables — that can be imported and reused in other programs.

### ✅ Key Points

* Each Python file (`.py`) is a **module**.
* Modules help in organizing code logically.
* They promote **code reuse** and **maintainability**.

### 🧩 Example

**File:** `math_utils.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**Usage in another file:** `main.py`

```python
import math_utils

print(math_utils.add(5, 3))       # Output: 8
print(math_utils.subtract(10, 4)) # Output: 6
```

### 🧠 Importing Modules

You can import a module in several ways:

```python
import module_name
from module_name import function_name
from module_name import *  # (Not recommended)
```

### 🧱 Built-in Modules

Python provides many built-in modules ready to use:

```python
import math
import datetime
import random
```

**Examples:**

```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

---

## 📦 What is a Package?

A **package** is a **collection of modules** organized in a directory hierarchy. It helps you structure large programs into multiple smaller, manageable files.

### 📁 Structure Example

```
mypackage/
│
├── __init__.py
├── math_utils.py
└── string_utils.py
```

### 🧭 `__init__.py`

* The `__init__.py` file makes Python treat the directory as a **package**.
* It can be empty or contain initialization code.

### 🧰 Example Usage

```python
from mypackage import math_utils
print(math_utils.add(2, 3))  # Output: 5
```

You can also import directly from modules:

```python
from mypackage.string_utils import capitalize_text
```

---

## ⚖️ Module vs Package

| Feature                | Module              | Package                              |
| ---------------------- | ------------------- | ------------------------------------ |
| Definition             | A single `.py` file | A folder containing multiple modules |
| Example                | `math_utils.py`     | `mypackage/` folder                  |
| Import Example         | `import math_utils` | `from mypackage import math_utils`   |
| `__init__.py` Required | ❌ No                | ✅ Yes                                |

---

## 🧮 Why Use Modules and Packages?

* Encourage **modular programming**
* Improve **code readability and reuse**
* Simplify **maintenance and testing**
* Enable **namespaces** to avoid name collisions

---

## 🚀 Summary

| Concept     | Description                              | Example              |
| ----------- | ---------------------------------------- | -------------------- |
| **Module**  | Single `.py` file with code              | `math_utils.py`      |
| **Package** | Directory with modules and `__init__.py` | `mypackage/`         |
| **Import**  | Bring code from modules/packages         | `import module_name` |

> **In short:**
>
> * **Module** = one Python file.
> * **Package** = folder of modules.
> * Both make your code reusable, organized, and scalable.
