## 🐍 Python Identifier Naming Rules and Conventions

In Python, an **identifier** is the name used to identify a **variable, class, function, object, module**, or any other entity in code. Identifiers are how Python keeps track of objects in memory.

---

### 🔹 1. **Basic Rules (Syntax Rules)**

These are the official rules enforced by Python’s interpreter — if broken, your code won’t run.

| Rule                                         | Description                                        | Example                   | Valid? |
| -------------------------------------------- | -------------------------------------------------- | ------------------------- | ------ |
| Must start with a letter or underscore       | First character must be **A–Z**, **a–z**, or **_** | `name`, `_value`          | ✅      |
| Cannot start with a digit                    | Numbers can appear after the first letter          | `2name`                   | ❌      |
| Can contain letters, digits, and underscores | No spaces or special symbols                       | `user_1`, `data_point`    | ✅      |
| Case-sensitive                               | `Name` and `name` are **different**                | `value` vs `Value`        | ✅      |
| No special characters                        | Cannot include `@`, `$`, `%`, `-`, etc.            | `user-name`               | ❌      |
| No spaces                                    | Use `_` instead of space                           | `user name` → `user_name` | ✅      |

---

### 🔹 2. **Naming Conventions (PEP 8 Guidelines)**

Python’s **PEP 8** style guide defines how identifiers should *look* to keep code readable and professional.

| Category                             | Naming Style                              | Example                          |
| ------------------------------------ | ----------------------------------------- | -------------------------------- |
| **Variable / Function**              | `snake_case` (lowercase with underscores) | `user_name`, `get_total()`       |
| **Class**                            | `PascalCase` (capitalize each word)       | `StudentRecord`, `DataLoader`    |
| **Constant**                         | `ALL_CAPS`                                | `PI = 3.14`, `MAX_USERS = 100`   |
| **Private Variable**                 | `_single_leading_underscore`              | `_temp`, `_helper_func()`        |
| **Strongly Private (Name Mangling)** | `__double_leading_underscore`             | `__password`, `__config`         |
| **Special (Magic / Dunder)**         | `__double_leading_and_trailing__`         | `__init__`, `__str__`, `__len__` |

---

### 🔹 3. **Reserved Keywords Cannot Be Used as Identifiers**

Python keywords are part of the language syntax and **cannot be used as names**.

#### ❌ Invalid Examples

```python
class = 10       # ❌ 'class' is a keyword
for = 5          # ❌ 'for' is reserved
True = 1         # ❌ cannot assign to built-in constants
```

You can view all reserved keywords using:

```python
import keyword
print(keyword.kwlist)
```

📘 For the full official list of Python keywords, visit:
👉 [Programiz – Python Keyword List](https://www.programiz.com/python-programming/keyword-list)

---

### 🔹 4. **Good Naming Practices**

* ✅ Use **meaningful** names: `student_age` instead of `sa`.
* ✅ Keep names **short but clear**.
* ✅ Avoid confusing letters: `l` (lowercase L), `O` (uppercase O), and `I` (uppercase i).
* ✅ Use consistent naming styles across your project.

---

### 🧠 **Examples Summary**

| Identifier  | Description                    | Valid?                         |
| ----------- | ------------------------------ | ------------------------------ |
| `age`       | simple variable                | ✅                              |
| `_count`    | internal variable (convention) | ✅                              |
| `__data`    | name-mangled (class private)   | ✅                              |
| `MAX_LIMIT` | constant                       | ✅                              |
| `user name` | contains space                 | ❌                              |
| `2user`     | starts with digit              | ❌                              |
| `user-name` | contains invalid character     | ❌                              |
| `print`     | overwrites built-in            | ⚠️ (works but not recommended) |

---

### 🧭 **In Summary**

> An **identifier** is any valid name you assign to a Python object.
> Follow PEP 8 style: **snake_case for variables**, **PascalCase for classes**, and **ALL_CAPS for constants** to make your code clear, readable, and Pythonic 🐍✨.
