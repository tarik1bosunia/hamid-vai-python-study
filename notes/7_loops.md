# Day 7: Loops

### 🔄 What are Loops?

Loops allow us to **repeat a block of code** multiple times without writing it again and again.

---

### ✅ for Loop

Used to iterate over a sequence (string, list, tuple, etc.).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output:**

```
apple
banana
cherry
```

---

### ✅ while Loop

Runs as long as a condition is True.

```python
count = 1
while count <= 5:
    print("Count =", count)
    count += 1
```

**Output:**

```
Count = 1
Count = 2
Count = 3
Count = 4
Count = 5
```

---

### ✅ break Statement

Exits the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
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

---

### ✅ continue Statement

Skips the current iteration and moves to the next.

```python
for i in range(6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```
0
1
2
4
5
```

---

### ✅ else with Loops

The `else` block runs when the loop finishes **without a break**.

```python
for i in range(5):
    print(i)
else:
    print("Loop finished!")
```

---

### ✅ Nested Loops

A loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

**Output:**

```
0 0
0 1
1 0
1 1
2 0
2 1
```

---

### 📝 Practice Tasks (Day 7)

1. Print numbers from 1 to 20 using a `for` loop.
2. Use a `while` loop to print numbers from 10 down to 1.
3. Print even numbers between 1 and 50 using a loop.
4. Use `break` to stop a loop when number = 7.
5. Use `continue` to skip multiples of 3 in a loop from 1 to 15.
6. Write a nested loop to print a multiplication table for numbers 1–5.
