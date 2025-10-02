# Day 6: Conditional Statements

### 🔀 What are Conditional Statements?

Conditional statements allow a program to make **decisions** based on conditions.

---

### ✅ if Statement

Executes a block of code if the condition is True.

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

---

### ✅ if-else Statement

Runs one block if condition is True, another if False.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

---

### ✅ if-elif-else Chain

Used when there are multiple conditions.

```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

---

### ✅ Nested if Statements

An `if` inside another `if`.

```python
num = 15
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

---

### ✅ Short-hand if (Ternary Operator)

```python
x = 10
print("Even") if x % 2 == 0 else print("Odd")
```

---

### 📝 Practice Tasks (Day 6)

1. Write a program to check if a number is positive, negative, or zero.
2. Take a number from the user and check if it is even or odd.
3. Write a grading program that prints A, B, C, or F based on score.
4. Use a nested `if` to check if a number is divisible by 2 and 3.
5. Use a short-hand if to check if someone is an adult (age ≥ 18).
