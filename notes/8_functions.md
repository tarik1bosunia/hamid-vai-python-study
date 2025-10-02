# Day 8: Functions

### 🔹 What is a Function?

* A **function** is a block of reusable code.
* Helps keep code organized and avoids repetition.

---

### ✅ Defining and Calling Functions

```python
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()
```

**Output:**

```
Hello, welcome to Python!
```

---

### ✅ Functions with Parameters

```python
def greet_user(name):
    print("Hello,", name)

greet_user("Alice")
greet_user("Bob")
```

**Output:**

```
Hello, Alice
Hello, Bob
```

---

### ✅ Functions with Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum =", result)
```

**Output:**

```
Sum = 8
```

---

### ✅ Default Arguments

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))    # 25 (default exponent=2)
print(power(5, 3)) # 125
```

---

### ✅ Keyword Arguments

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=20, name="Alice")
```

---

### ✅ Arbitrary Arguments (*args, **kwargs)

```python
# *args → variable number of positional arguments
def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4))  # 10

# **kwargs → variable number of keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(key, ":", value)

print_info(name="Alice", age=20, city="Paris")
```

---

### ✅ Lambda (Anonymous Function)

```python
square = lambda x: x * x
print(square(5))   # 25
```

---

### 📝 Practice Tasks (Day 8)

1. Write a function that takes two numbers and returns their product.
2. Write a function to check if a number is even or odd.
3. Create a function with a default parameter that calculates simple interest (`SI = P * R * T / 100`).
4. Write a function that accepts `*args` and prints the maximum value.
5. Use a lambda function to get the cube of a number.
