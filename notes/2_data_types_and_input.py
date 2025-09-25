# Day 2: Data Types & Input

### 🔢 Integers, Floats, Strings, Booleans

Python has different types of data for storing values:

* **Integer (`int`)** → whole numbers
* **Float (`float`)** → decimal numbers
* **String (`str`)** → text data
* **Boolean (`bool`)** → `True` or `False`

```python
# Examples of data types
age = 25          # int
pi = 3.1416       # float
name = "Alice"    # string
is_student = True # boolean

print(age, type(age))
print(pi, type(pi))
print(name, type(name))
print(is_student, type(is_student))
```

**Output:**

```
25 <class 'int'>
3.1416 <class 'float'>
Alice <class 'str'>
True <class 'bool'>
```

---

### 🔄 Type Casting (Converting Between Types)

You can convert between types using built-in functions:

* `int()` → convert to integer
* `float()` → convert to float
* `str()` → convert to string
* `bool()` → convert to boolean

```python
x = "100"     # string
y = int(x)    # convert to integer
z = float(x)  # convert to float

print(x, type(x))
print(y, type(y))
print(z, type(z))
```

**Output:**

```
100 <class 'str'>
100 <class 'int'>
100.0 <class 'float'>
```

---

### ⌨️ Getting User Input

Use `input()` to get data from the user. Input is always returned as a **string**.

```python
# Taking user input
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name, "you are", age, "years old.")
```

**Output (example):**

```
Enter your name: Alice
Enter your age: 20
Hello Alice you are 20 years old.
```

👉 If you need numbers, convert them using `int()` or `float()`:

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)
```

---

### 📝 Practice Tasks (Day 2)

1. Ask the user for their birth year and calculate their age.
2. Convert a float number to an integer and print both values.
3. Write a program that asks for two numbers and prints their product.
4. Create a variable `is_python_fun` with a boolean value and print it.
