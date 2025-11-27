# Day 3: Operators

### ➕ Arithmetic Operators

Used for basic mathematical operations:

```python
a = 10
b = 3

print("Addition:", a + b)      # 13
print("Subtraction:", a - b)   # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)        # 1
print("Exponent:", a ** b)      # 1000
```

---

### ⚖️ Comparison (Relational) Operators

Used to compare values → result is `True` or `False`.

```python
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= 5)  # True
print(y <= 10) # True
```

---

### 🔗 Logical Operators

Used to combine conditional statements.

```python
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False
```

---

### 🔑 Assignment Operators

Used to assign values to variables.

```python
x = 5
x += 3  # same as x = x + 3
print(x) # 8

x *= 2  # same as x = x * 2
print(x) # 16
```

---

### 🔍 Membership Operators

Check if a value exists in a sequence.

```python
name = "Alice"

print("A" in name)     # True
print("z" not in name) # True
```

---

### 🆔 Identity Operators

Check if two variables refer to the same object in memory.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)     # False (different objects)
print(a is c)     # True  (same object)
print(a is not b) # True
```

---

### 📝 Practice Tasks (Day 3)

1. Take two numbers from the user and perform all arithmetic operations.
2. Write a program to check if a number is greater than 100 and less than 200.
3. Demonstrate the use of `and`, `or`, and `not` with conditions.
4. Check if the letter `'p'` exists in the string `'Python'`.
5. Show the difference between `is` and `==` using two lists.
