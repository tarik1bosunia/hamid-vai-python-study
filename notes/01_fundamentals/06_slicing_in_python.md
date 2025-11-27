# 📝 Slicing in Python

### 🔹 General Syntax

```python
sequence[start:end:step]
```

* **start** → index where slicing begins (default = 0)
* **end** → index where slicing stops (exclusive)
* **step** → how many items to skip (default = 1)

---

### ✅ String Slicing

```python
text = "Python"

print(text[0:4])   # Pyth (characters 0 to 3)
print(text[:3])    # Pyt (from start to 2)
print(text[2:])    # thon (from 2 to end)
print(text[-1])    # n (last character)
print(text[-3:])   # hon (last 3 characters)
print(text[::-1])  # nohtyP (reversed string)
```

---

### ✅ List Slicing

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::2])   # [10, 30, 50] (every 2nd element)
print(nums[::-1])  # [50, 40, 30, 20, 10] (reverse list)
```

---

### ✅ Tuple Slicing

Tuples also support slicing (but remember, they are immutable):

```python
colors = ("red", "green", "blue", "yellow")

print(colors[1:3])   # ('green', 'blue')
print(colors[::-1])  # ('yellow', 'blue', 'green', 'red')
```

---

### ✅ Nested List Slicing

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0:2])      # [[1, 2, 3], [4, 5, 6]]
print(matrix[0][1:3])   # [2, 3] (slice inside a row)
```

---

### 📝 Practice Tasks

1. Take a string and print the first 5 characters.
2. Reverse a string using slicing.
3. Create a list of numbers and print every second element.
4. Slice a tuple to get the middle two elements.
5. Use slicing to extract a sub-matrix from a nested list.
