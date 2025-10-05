# 📅 Day 12: Advanced String Handling (Regular Expressions)

Regular expressions (**regex**) allow powerful searching, matching, and manipulation of text patterns in Python. The built-in `re` module provides all regex functionalities.

---

## ✅ Importing the Module

```python
import re
```

---

## 🔹 Common Functions

| Function       | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `re.match()`   | Checks for a match only at the **beginning** of the string |
| `re.search()`  | Searches the **entire** string for a match                 |
| `re.findall()` | Returns all **non-overlapping matches** as a list          |
| `re.sub()`     | **Replaces** matches with a new string                     |
| `re.split()`   | **Splits** a string by occurrences of a pattern            |

---

## 🔤 Common Regex Symbols

| Symbol | Meaning                           | Example                       |
| ------ | --------------------------------- | ----------------------------- |
| `.`    | Any character (except newline)    | `a.c` → matches `abc`, `axc`  |
| `^`    | Start of string                   | `^Hi` → matches `Hi there`    |
| `$`    | End of string                     | `end$` → matches `the end`    |
| `*`    | 0 or more repetitions             | `go*` → `g`, `go`, `goo`      |
| `+`    | 1 or more repetitions             | `go+` → `go`, `goo`           |
| `?`    | 0 or 1 repetition                 | `colou?r` → `color`, `colour` |
| `\d`   | Any digit                         | `\d+` → matches numbers       |
| `\w`   | Word character (a-z, A-Z, 0-9, _) | `\w+` → words                 |
| `\s`   | Whitespace                        | `\s+` → spaces, tabs          |
| `[]`   | Character set                     | `[aeiou]` → matches vowels    |
| `[^]`  | Negation set                      | `[^0-9]` → non-digits         |

---

## 🔎 Pattern Matching & Searching

### Example 1 — Find All Digits in a String

```python
import re
text = "Order A12 has 3 items, ID: 98765"

# Find all individual digits
single_digits = re.findall(r"\d", text)
print(single_digits)  # ['1', '2', '3', '9', '8', '7', '6', '5']

# Find complete numbers
numbers = re.findall(r"\d+", text)
print(numbers)  # ['12', '3', '98765']
```

### Example 2 — Find All Words

```python
sentence = "Python is powerful and easy to learn."
words = re.findall(r"\w+", sentence)
print(words)
# ['Python', 'is', 'powerful', 'and', 'easy', 'to', 'learn']
```

### Example 3 — Search vs Match

```python
s = "abc123"
print(re.match(r"abc", s))   # Match only at the start
print(re.search(r"123", s))  # Search anywhere in the string
```

### Example 4 — Capture Groups: [see details group capture](./12/1_regex_capture_groups.md)

```python
log = "User: alice, Age: 21"
pattern = r"User: (\w+), Age: (\d+)"
match = re.search(pattern, log)
print(match.groups())  # ('alice', '21')
print(match.group(1))  # alice
print(match.group(2))  # 21
```

### Example 5 — Named Groups

```python
pattern = r"User: (?P<name>\w+), Age: (?P<age>\d+)"
match = re.search(pattern, log)
print(match.group('name'))  # alice
print(match.group('age'))   # 21
```

### Example 6 — Substitution (Replace)

```python
sentence = "My phone number is 123-456-7890."
masked = re.sub(r"\d", "*", sentence)
print(masked)
# My phone number is ***-***-****
```

### Example 7 — Splitting a String

```python
text = "apple, banana; orange|grape"
fruits = re.split(r",|;|\|", text)
print(fruits)
# ['apple', 'banana', 'orange', 'grape']
```

### Example 8 — Validate Email Address

```python
email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

emails = ["user@example.com", "invalid@com", "john.doe@gmail.com"]
for e in emails:
    if re.match(email_pattern, e):
        print(e, "✅ valid")
    else:
        print(e, "❌ invalid")
```

### Example 9 — Extract Hashtags from Text

```python
text = "#Python is #fun and #powerful!"
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # ['#Python', '#fun', '#powerful']
```

### Example 10 — Extract Phone Numbers

```python
text = "Call 01712345678 or 01987654321 today!"
phones = re.findall(r"01[3-9]\d{8}", text)
print(phones)  # ['01712345678', '01987654321']
```

---

## 🧠 Practice Tasks (Day 12)

1. Extract all email addresses from a paragraph.
2. Find all words starting with a capital letter.
3. Replace all digits in a string with `#`.
4. Extract all phone numbers formatted as `xxx-xxx-xxxx`.
5. Write a regex to check if a string is a valid Bangladeshi phone number (`01XXXXXXXXX`).
6. Find all hashtags in a tweet-like text.
7. Split a CSV line by commas using regex.
8. Extract domain names from email addresses.
9. Replace multiple spaces in a text with a single space.
10. Validate if a string ends with `.com` or `.org`.
