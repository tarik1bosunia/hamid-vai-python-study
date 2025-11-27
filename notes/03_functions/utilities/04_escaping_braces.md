# Escaping Braces in f-Strings

## 🎯 Literal Curly Braces in Formatted Strings

F-strings use `{}` for variable interpolation. To include literal braces, double them: `{{` and `}}`.

---

## 🧩 The Problem

```python
# ❌ Error: Braces interpreted as placeholder
# result = f"Set: {1, 2, 3}"  # Syntax error!

# ✅ Solution: Double the braces
result = f"Set: {{1, 2, 3}}"
print(result)  # Set: {1, 2, 3}
```

---

## 🧬 Bioinformatics Examples

### Example 1: JSON-like Output

```python
gene = "BRCA1"
length = 7000

# Output with literal braces
output = f'{{"gene": "{gene}", "length": {length}}}'
print(output)  # {"gene": "BRCA1", "length": 7000}
```

### Example 2: Regex Patterns

```python
min_length = 30

# Regex with literal braces
pattern = f"ATG[ATCG]{{{min_length},}}"
print(pattern)  # ATG[ATCG]{30,}
```

### Example 3: Dictionary String

```python
seq_id = "seq1"
sequence = "ATCG"

# Format as dict-like string
result = f"{{'{seq_id}': '{sequence}'}}"
print(result)  # {'seq1': 'ATCG'}
```

---

## 🔧 Mixed Braces

```python
# Mix literal and interpolated braces
name = "BRCA1"
count = 10

message = f"Gene {name} has {{special}} with {count} variants"
print(message)  # Gene BRCA1 has {special} with 10 variants
```

---

## 💡 Key Takeaways

✓ `{{` produces literal `{`  
✓ `}}` produces literal `}`  
✓ Use for JSON, regex, dict formatting  
✓ Can mix literal and interpolated braces
