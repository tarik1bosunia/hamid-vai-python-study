# Understanding Named Groups in Python Regex

Named groups make regular expressions **more readable** and easier to manage, especially when working with multiple captured values.

---

## 🧩 Step 1: The Text

```python
log = "User: alice, Age: 21"
```

This is our input string — it contains a **username** (`alice`) and an **age** (`21`).

Goal → Extract both values clearly using regex.

---

## 🧩 Step 2: The Pattern with Named Groups

```python
pattern = r"User: (?P<name>\w+), Age: (?P<age>\d+)"
```

This pattern uses **named capture groups** instead of numbered ones.

| Regex Part      | Meaning                                                                | Example Match    |
| --------------- | ---------------------------------------------------------------------- | ---------------- |
| `User:`         | Literal text `User:`                                                   | Matches `User:`  |
| `(?P<name>\w+)` | Defines a **named group** called `name` to capture **word characters** | Captures `alice` |
| `, Age:`        | Literal text                                                           | Matches `, Age:` |
| `(?P<age>\d+)`  | Defines a **named group** called `age` to capture **digits**           | Captures `21`    |

🧠 **Syntax:** `(?P<group_name>pattern)` creates a named capture group in Python.

---

## 🧩 Step 3: Searching the String

```python
import re
match = re.search(pattern, log)
```

* `re.search()` scans the entire string.
* Returns a **Match object** if the pattern is found.
* In this case, it matches:

  ```
  User: alice, Age: 21
  ```

---

## 🧩 Step 4: Accessing Named Groups

```python
print(match.group('name'))  # alice
print(match.group('age'))   # 21
```

**Output:**

```
alice
21
```

This retrieves each value using its **group name**, not by number.

You can also get all named results at once:

```python
print(match.groupdict())
```

**Output:**

```
{'name': 'alice', 'age': '21'}
```

---

## 🧩 Step 5: Why Use Named Groups?

| Advantage            | Description                                                    |
| -------------------- | -------------------------------------------------------------- |
| 🧠 Readability       | `group('name')` is easier to understand than `group(1)`        |
| 🔁 Maintainability   | Ideal when working with long or complex patterns               |
| 📦 Structured Output | `groupdict()` can easily convert results to JSON or DataFrames |

---

## 🧩 Step 6: Example with Multiple Matches

```python
text = """User: alice, Age: 21
User: bob, Age: 19
User: charlie, Age: 25"""

pattern = r"User: (?P<name>\w+), Age: (?P<age>\d+)"

for m in re.finditer(pattern, text):
    print(m.group('name'), m.group('age'))
```

**Output:**

```
alice 21
bob 19
charlie 25
```

Here, `re.finditer()` finds all matches and returns an iterator of Match objects.

---

## 🧠 Key Takeaways

* Parentheses `()` **capture** parts of text that match.
* Named groups use the format **`(?P<name>pattern)`**.
* Access them with `match.group('name')` instead of numeric indexes.
* Use `match.groupdict()` to get a dictionary of all named matches.
* Combine with `re.finditer()` to extract all occurrences from a long text.

---

### ✅ Summary

| Function              | Description                                   |
| --------------------- | --------------------------------------------- |
| `re.search()`         | Finds the first match in a string             |
| `match.group('name')` | Returns the content of the named group `name` |
| `match.groupdict()`   | Returns a dictionary of all named groups      |
| `re.finditer()`       | Returns an iterator over all matches          |

✨ Named groups are the best practice for parsing structured text — like logs, CSV-like data, or reports!
