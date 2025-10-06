# 🧮 Python `range()` Function — Complete Guide

The `range()` function in Python is one of the most commonly used tools for generating sequences of numbers.
It’s especially useful for **loops**, **indexing**, **iteration**, and **creating numeric sequences**.

---

## 🔹 1. What is `range()`?

`range()` generates a sequence of numbers — usually used with `for` loops.

Syntax:

```python
range(start, stop, step)
```

### Parameters

| Parameter | Description                                       | Default  |
| --------- | ------------------------------------------------- | -------- |
| `start`   | The number at which the sequence begins           | 0        |
| `stop`    | The number **up to but not including** this value | Required |
| `step`    | The increment (can be negative)                   | 1        |

---

## 🔹 2. Basic Examples

### Example 1 — Simple Range

```python
for i in range(5):
    print(i)
```

**Output:**

```
0
1
2
3
4
```

✅ By default, `start = 0` and `step = 1`.

---

### Example 2 — Custom Start and Stop

```python
for i in range(2, 6):
    print(i)
```

**Output:**

```
2
3
4
5
```

✅ Includes `2` but excludes `6`.

---

### Example 3 — Using Step

```python
for i in range(0, 10, 2):
    print(i)
```

**Output:**

```
0
2
4
6
8
```

✅ The third argument (`2`) means *increment by 2*.

---

### Example 4 — Negative Step (Descending Order)

```python
for i in range(10, 0, -2):
    print(i)
```

**Output:**

```
10
8
6
4
2
```

✅ Negative step values let you **count backward**.

---

## 🔹 3. Converting Range to a List

`range()` doesn’t create a list directly — it creates an **iterator** (memory-efficient).
But you can convert it to a list:

```python
nums = list(range(5))
print(nums)
```

**Output:**

```
[0, 1, 2, 3, 4]
```

---

### Example — Custom Range as a List

```python
nums = list(range(2, 11, 2))
print(nums)
```

**Output:**

```
[2, 4, 6, 8, 10]
```

---

## 🔹 4. Using `range()` in Loops

### Example 1 — Summing Numbers

```python
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)
```

**Output:**

```
Sum: 15
```

### Example 2 — Using `range()` with List Indexes

```python
colors = ['red', 'green', 'blue']
for i in range(len(colors)):
    print(i, colors[i])
```

**Output:**

```
0 red
1 green
2 blue
```

---

## 🔹 5. Negative Ranges

### Example 1 — Reverse Counting

```python
for i in range(5, -1, -1):
    print(i)
```

**Output:**

```
5
4
3
2
1
0
```

### Example 2 — Printing Even Numbers Backward

```python
for i in range(10, 0, -2):
    print(i)
```

**Output:**

```
10
8
6
4
2
```

---

## 🔹 6. Using `range()` in Conditionals

You can use `range()` with membership tests.

```python
x = 5
if x in range(1, 10):
    print("x is between 1 and 9")
else:
    print("x not in range")
```

**Output:**

```
x is between 1 and 9
```

---

## 🔹 7. Nested Ranges (Nested Loops)

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()
```

**Output:**

```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

---

## 🔹 8. Skipping Iterations

You can use `continue` to skip values from a range.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

**Output:**

```
1
3
5
7
9
```

---

## 🔹 9. Using `range()` in List Comprehensions

```python
squares = [i**2 for i in range(1, 6)]
print(squares)
```

**Output:**

```
[1, 4, 9, 16, 25]
```

---

## 🔹 10. Memory Efficiency

`range()` is not a list — it’s a **lazy sequence** that generates numbers on demand.

```python
nums = range(1000000)
print(type(nums))
print(len(nums))
```

**Output:**

```
<class 'range'>
1000000
```

✅ Even though it represents 1 million numbers, it doesn’t store them all in memory!

---

## 🔹 11. Examples with Different Steps

| Expression       | Output          | Description      |
| ---------------- | --------------- | ---------------- |
| `range(5)`       | 0,1,2,3,4       | Default step = 1 |
| `range(2,10)`    | 2,3,4,5,6,7,8,9 | Custom start     |
| `range(0,10,2)`  | 0,2,4,6,8       | Step of 2        |
| `range(10,0,-1)` | 10→1            | Reverse order    |
| `range(1,20,5)`  | 1,6,11,16       | Step of 5        |

---

## 🔹 12. Combining `range()` with Functions

### Example — Generate Even Numbers List

```python
def even_numbers(n):
    return list(range(0, n+1, 2))

print(even_numbers(10))
```

**Output:**

```
[0, 2, 4, 6, 8, 10]
```

### Example — Sum of Squares

```python
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n+1))

print(sum_of_squares(5))
```

**Output:**

```
55
```

---

## 🔹 13. Real-Life Use Cases

* Iterating over lists or strings with indices.
* Creating numeric ranges for charts or arrays.
* Repeating code blocks a fixed number of times.
* Generating sequences of even, odd, or random steps.
* Memory-efficient looping in large datasets.

---

## ✅ Summary

| Feature           | Description                | Example                        |
| ----------------- | -------------------------- | ------------------------------ |
| Default Range     | Starts from 0              | `range(5)` → 0..4              |
| Custom Start/Stop | Define range boundaries    | `range(2,6)` → 2..5            |
| Step              | Define increment           | `range(0,10,2)` → even numbers |
| Negative Step     | Reverse order              | `range(5,0,-1)`                |
| Convert to List   | `list(range(5))`           | `[0,1,2,3,4]`                  |
| Memory Efficient  | Does not store all numbers | `range(1000000)`               |

---

### 🧠 Practice Tasks

1. Print all odd numbers between 1 and 50.
2. Create a list of multiples of 3 using `range()`.
3. Generate countdown from 10 to 1.
4. Use nested ranges to print a 5×5 grid of coordinates.
5. Write a function that prints all squares less than 100 using `range()`.

---

✅ **In summary:**
`range()` is a versatile, efficient, and foundational function for creating numeric sequences, making it essential for loops, iterations, and performance-oriented Python code!
