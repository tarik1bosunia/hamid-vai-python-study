# 🧵 Python Escape Sequences — Complete Guide (with Examples)

Escape sequences are **special character combinations** used inside string literals to represent characters that are hard to type or see (newlines, tabs, quotes, Unicode, etc.). They start with a **backslash** (`\`).

---

## 🔹 String Literal Basics

```python
s1 = 'single quotes'
s2 = "double quotes"
s3 = """triple-quoted strings can span
multiple lines without \n"""
```

* Use **`\\`** to write a single backslash in normal strings.
* Triple quotes are useful for multi-line text and docstrings.

---

## 🔹 Common Escape Sequences

| Escape | Meaning                | Example                 | Output               |
| ------ | ---------------------- | ----------------------- | -------------------- |
| `\n`   | Newline                | `print('Hello\nWorld')` | Hello↵World          |
| `\t`   | Horizontal tab         | `print('A\tB')`         | A···B                |
| `\\`   | Backslash              | `print('\\')`           | `\`                  |
| `\'`   | Single quote           | `print('\'quote\'')`    | 'quote'              |
| `\"`   | Double quote           | `print(\"\"quote\"\")`  | "quote"              |
| `\r`   | Carriage return        | `print('123\rXY')`      | XY3*                 |
| `\b`   | Backspace              | `print('ABC\bD')`       | ABD*                 |
| `\f`   | Form feed (page break) | `print('A\fB')`         | A◼B*                 |
| `\v`   | Vertical tab           | `print('A\vB')`         | A◼B*                 |
| `\a`   | Bell (alert)           | `print('\a')`           | (beep on some terms) |

* Rendering depends on your terminal; `\r`, `\b`, `\f`, `\v` are control chars.

**Tip:** To **see** escape characters rather than their effects, use `repr()`:

```python
s = 'Line1\nLine2\tTab'
print(s)       # shows formatted text
print(repr(s)) # 'Line1\nLine2\tTab'
```

---

## 🔹 Unicode & Hex Escapes

Python strings are Unicode by default.

| Escape       | Meaning         | Example                          | Output |
| ------------ | --------------- | -------------------------------- | ------ |
| `\xhh`       | Hex byte        | `"\x41"`                         | 'A'    |
| `\uXXXX`     | 16‑bit Unicode  | `"\u03B1"`                       | 'α'    |
| `\UXXXXXXXX` | 32‑bit Unicode  | `"\U0001F600"`                   | 😀     |
| `\N{NAME}`   | Unicode by name | `"\N{GREEK SMALL LETTER ALPHA}"` | α      |

```python
print('\x48\x69')        # Hi
print('\u2764')           # ❤
print('\U0001F680')       # 🚀
print('\N{SNOWMAN}')      # ☃
```

---

## 🔹 Raw Strings `r'...'`

Raw strings **do not process backslash escapes** (mostly). Great for Windows paths & regex.

```python
path = r"C:\Users\Alice\Documents"   # no need to double the backslashes
print(path)
```

**Important caveats:**

* A raw string **cannot end** with a single backslash: `r"text\"` ❌
* Quotes must still be escaped if they **terminate** the string: `r'It\'s'` ✅
* `\u` and `\x` are **not** turned into Unicode/hex in raw strings.

Comparison:

```python
print('C:\\new')   # C:\new
print(r'C:\new')    # C:\new (raw)
```

---

## 🔹 Escaping Quotes Inside Strings

```python
s1 = 'It\'s fine.'
s2 = "He said: \"Hello!\""
s3 = """She said: "Hello" without escaping"""
```

Pick the quoting style that avoids the most escapes.

---

## 🔹 Windows Paths & URLs

```python
win = 'C:\\Program Files\\Python39\\python.exe'
win_raw = r'C:\Program Files\Python39\python.exe'
url = 'https://example.com/a?x=1&y=2'
print(win)     
print(win_raw)
print(url)
```

---

## 🔹 Multiline, Indentation, and Newlines

```python
poem = (
    'Roses are red\n'
    'Violets are blue\n'
    'Tabs:\tare visible too\n'
)
print(poem)
```

Automatic concatenation inside parentheses is handy; each piece can include escapes.

---

## 🔹 Bytes Literals & Escapes

Bytes (`b'...'`) store raw 0–255 values. Useful for binary I/O.

```python
b = b"A\x42\n"   # 65, 66, 10
print(b)             # b'AB\n'
print(list(b))       # [65, 66, 10]
```

* In bytes literals, only a subset of escapes is valid: `\n`, `\r`, `\t`, `\\`, `\'`, `\"`, octal (`\ooo`), hex (`\xhh`).

---

## 🔹 f-Strings & Escaping Braces

In f-strings, **double the braces** to show literal `{` or `}`.

```python
name = 'Alice'
print(f'Hello, {name}!')
print(f'Use {{curly}} braces to show braces.')  # Use {curly} braces to show braces.
```

---

## 🔹 Regex Strings: Raw + Escapes

Regex uses many backslashes; prefer **raw strings** to reduce escaping.

```python
import re
pat1 = "\\d+"      # normal string: \\d+
pat2 = r"\d+"       # raw string: \d+
print(re.findall(pat2, 'Room 42, Floor 7'))  # ['42', '7']
```

---

## 🔹 Printing Visible Escapes (`unicode_escape`)

```python
s = 'Line1\nLine2\tTab \u2192 Arrow'
print(s)
print(s.encode('unicode_escape').decode())
# Line1
# Line2	Tab → Arrow
# 'Line1\nLine2\tTab \u2192 Arrow'
```

---

## 🔹 Edge Cases & Pitfalls

* `"\x4"` ❌ invalid (hex needs **two** digits). Use `"\x04"`.
* `r"\u2764"` prints `\u2764`, not ❤ (raw strings don’t interpret escapes).
* `r'ends with backslash\\'` ✅ but `r'ends with backslash\'` ❌
* Newline style: `\n` works on all platforms; Python converts to the platform default on file write unless you pass `newline=''`.

---

## 🔹 Mini‑Cookbook

**1) JSON string with quotes**

```python
json_line = '{\"name\": \"Alice\"}'
```

**2) Template with braces in f-strings**

```python
tmpl = f'Hello {{name}}, today is {{day}}.'
```

**3) Show path literally in docstring**

```python
help_text = r"""
Put your data in C:\Data\2025\input.csv
"""
```

**4) Mixed Unicode**

```python
msg = 'Pi: \u03C0, Rocket: \U0001F680, Heart: \N{HEAVY BLACK HEART}'
print(msg)
```

---

## ✅ Practice Exercises

1. Print `He said: "Python\trocks"` so the **tab** is real; then show the **repr** of the same string.
2. Build a Windows path string for `C:\Users\YourName\Desktop\notes.txt` using **raw** and **non‑raw** forms.
3. Print three lines with one `print()` using `\n`.
4. Create an f-string that prints literal `{x}` and `{y}` without formatting them.
5. Print the snowman using three methods: `\u2603`, `\N{SNOWMAN}`, and the literal character.

---

### TL;DR

* Use escape sequences to represent control characters (`\n`, `\t`), quotes, and Unicode.
* Prefer **raw strings** for regex and Windows paths.
* Use `repr()` or `encode('unicode_escape')` to **see** escapes.
* In f-strings, escape braces with `{{` and `}}`.
