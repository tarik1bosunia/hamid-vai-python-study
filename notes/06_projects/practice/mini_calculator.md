## 🧮 Day 11: Mini Project — Build a Simple Calculator

Welcome to your first **mini Python project!** Today, we’ll create a basic calculator app that can perform simple arithmetic operations like addition, subtraction, multiplication, and division.

---

### 🎯 **Learning Goals**

By the end of this project, you’ll be able to:

* Use **functions** to organize code
* Take **user input** and process it
* Handle **errors and invalid input** gracefully

---

### 🧩 **Step-by-Step Guide**

#### 1️⃣ Define the Calculator Functions

Each operation can be defined as a separate function.

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y
```

---

#### 2️⃣ Create a Menu for User Selection

Show a list of operations so the user can choose which one to perform.

```python
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
```

---

#### 3️⃣ Get User Input

```python
choice = input("Enter choice (1/2/3/4): ")

# Validate user input
if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input! Please select from 1 to 4.")
```

---

### ⚙️ **Full Code Together**

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input! Please select from 1 to 4.")
```

---

### 💡 **Bonus Challenge**

Try to make your calculator even smarter:

* Add an option to **run again** without restarting the program
* Support **power (x^y)** and **modulus (%)** operations
* Wrap the whole calculator in a **loop** until the user chooses to exit

---

### 🏁 **Output Example**

```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 1
Enter first number: 5
Enter second number: 3
Result: 5.0 + 3.0 = 8.0
```

---

### ✅ **Concepts Covered**

* Functions and modular programming
* Input and output handling
* Conditional statements (`if`, `elif`, `else`)
* Error handling for division by zero

> 🧠 **Takeaway:** This mini project is a building block for interactive programs — next, you can try building a **scientific calculator** or even a **GUI calculator** using `tkinter`!
