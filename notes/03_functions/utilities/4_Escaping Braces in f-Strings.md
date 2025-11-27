# 🧩 Escaping Braces in f-Strings

In **Python f-strings**, curly braces `{}` are used to insert or evaluate variables and expressions directly inside a string.
But sometimes, you want to **display the braces themselves** literally. Let’s understand how to do that 👇

---

## 🔹 1. Normal Use of Braces

```python
name = "Alice"
print(f"Hello {name}!")
```

**Output:**

```
Hello Alice!
```

✅ `{name}` acts as a **placeholder**, and Python replaces it with the variable’s value.

---

## 🔹 2. The Problem — Literal Braces

If you try to print a brace directly inside an f-string:

```python
print(f"Use {curly} braces in syntax")
```

❌ Python will raise an **error**, because it tries to find a variable named `curly`.

---

## 🔹 3. The Solution — Double Braces

To print curly braces `{` or `}` literally in an f-string, **double them**:

* `{{` → prints `{`
* `}}` → prints `}`

### ✅ Example

```python
print(f"Use {{curly}} braces in syntax")
```

**Output:**

```
Use {curly} braces in syntax
```

---

## 🔹 4. Why This Works

When Python parses an f-string:

| Symbol      | Meaning                            |
| ----------- | ---------------------------------- |
| `{...}`     | Expression placeholder (evaluated) |
| `{{` / `}}` | Literal brace (printed as is)      |

You can even mix both:

```python
x = 10
print(f"The value of x = {x}, written as {{x}} in docs.")
```

**Output:**

```
The value of x = 10, written as {x} in docs.
```

---

## 🔹 5. Example — JSON-like String

Suppose you want to build a JSON-style output:

```python
data = {"name": "Alice", "age": 25}

# ✅ Using escaped braces
print(f"{{'name': '{data['name']}', 'age': {data['age']}}}")
```

**Output:**

```
{'name': 'Alice', 'age': 25}
```

---

## 🔹 6. Quick Reference Table

| What You Type | What You Get | Meaning                    |
| ------------- | ------------ | -------------------------- |
| `{x}`         | Value of `x` | Insert variable            |
| `{{`          | `{`          | Print literal `{`          |
| `}}`          | `}`          | Print literal `}`          |
| `{{x}}`       | `{x}`        | Print text `{x}` literally |

---

## 🔹 7. More Examples

```python
name = "Ruhul"

print(f"{{name}}")             # prints {name}
print(f"Hello {{ {name} }}!")  # prints Hello { Ruhul }!
```

**Output:**

```
{name}
Hello { Ruhul }!
```

---

## ✅ Summary

* f-strings use `{}` for **expressions**.
* To show braces literally, use **double braces** `{{` and `}}`.
* This tells Python: “Don’t evaluate this — just print the brace.”

**Formula:**
`f"{{text}}"` → prints `{text}`
