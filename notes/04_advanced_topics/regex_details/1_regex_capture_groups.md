#  Understanding Regex Capture Groups in Python

Let’s break down how **capture groups** work in Python’s `re` module using this example:

```python
import re

log = "User: alice, Age: 21"
pattern = r"User: (\w+), Age: (\d+)"
match = re.search(pattern, log)

print(match.groups())  # ('alice', '21')
print(match.group(1))  # alice
print(match.group(2))  # 21
```

---

## 🧩 Step 1: The Text

```python
log = "User: alice, Age: 21"
```

This is our input string — it contains both a **name** and an **age**.

Goal → Extract the **username (`alice`)** and **age (`21`)**.

---

## 🧩 Step 2: The Pattern

```python
pattern = r"User: (\w+), Age: (\d+)"
```

This describes what we’re looking for.

| Pattern Part | Meaning                                                    |
| ------------ | ---------------------------------------------------------- |
| `User:`      | Matches the literal text `User:`                           |
| `(\w+)`      | Captures one or more **word characters** → matches `alice` |
| `, Age:`     | Matches the literal text `, Age:`                          |
| `(\d+)`      | Captures one or more **digits** → matches `21`             |

🧠 Note: Parentheses `()` are **capture groups**. They store matched portions separately.

---

## 🧩 Step 3: Searching for the Pattern

```python
match = re.search(pattern, log)
```

* `re.search()` scans the entire string for the first match.
* Returns a **Match object** if found, otherwise `None`.

✅ In this case, the match covers:

```
User: alice, Age: 21
```

---

## 🧩 Step 4: Extracting Matches

```python
print(match.groups())
```

Returns **all captured groups** as a tuple:

```
('alice', '21')
```

Each `()` pair in the regex corresponds to one item in this tuple.

---

## 🧩 Step 5: Accessing Individual Groups

```python
print(match.group(1))  # alice
print(match.group(2))  # 21
```

* `group(1)` → value captured by the first parentheses → `'alice'`
* `group(2)` → value captured by the second parentheses → `'21'`

You can also get the **entire matched string**:

```python
print(match.group(0))  # User: alice, Age: 21
```

---

## ✅ Summary Table

| Method           | Returns              | Example Output           |
| ---------------- | -------------------- | ------------------------ |
| `match.group(0)` | Entire match         | `'User: alice, Age: 21'` |
| `match.group(1)` | First capture group  | `'alice'`                |
| `match.group(2)` | Second capture group | `'21'`                   |
| `match.groups()` | Tuple of all groups  | `('alice', '21')`        |

---

## 🔖 Bonus — Named Groups

You can make your regex more readable by naming groups:

```python
pattern = r"User: (?P<name>\w+), Age: (?P<age>\d+)"
match = re.search(pattern, log)

print(match.group('name'))  # alice
print(match.group('age'))   # 21
```

🟢 Output:

```
alice
21
```

This way, instead of remembering group numbers, you can refer to names (`'name'`, `'age'`).

---
Note: if you want to know more about named groups click here: [named groups](./2_named_groups_in_python_regex.md)

## 🧠 Key Takeaways

* Parentheses `()` **capture** parts of a match.
* Use `.groups()` to get all captured parts.
* Use `.group(n)` to access one specific group.
* Use **named groups** (`?P<name>`) for clarity.
* `group(0)` always gives the **entire matched string**.

✨ Capture groups make regex extremely powerful for structured text extraction like logs, forms, or datasets!
