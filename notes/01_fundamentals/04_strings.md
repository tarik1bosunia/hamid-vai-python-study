# 📅 Day 4: Strings

### 🧵 What are Strings?

* A **string** is a sequence of characters inside quotes (`' '` or `" ").
* Strings are **immutable** (cannot be changed after creation).

```python
text = "Python Programming"
print(text)
print(type(text))
```

---

### 🔢 Indexing and Slicing

* Strings work like arrays of characters.
* Index starts at **0**.

```python
word = "Python"

print(word[0])   # P (first character)
print(word[-1])  # n (last character)
print(word[0:4]) # Pyth (slice)
print(word[:3])  # Pyt (from start)
print(word[2:])  # thon (to end)
```

---

### 🔧 Common String Methods

```python
msg = "  hello world  "

print(msg.upper())     # HELLO WORLD
print(msg.lower())     # hello world
print(msg.strip())     # removes spaces → 'hello world'
print(msg.replace("world", "Python")) # hello Python
print(msg.find("world")) # 8 (index of substring)
print(msg.split())     # ['hello', 'world']
```

---

### 🔤 String Concatenation

```python
first = "Hello"
second = "World"

print(first + " " + second) # Hello World
```

---

### 📝 String Formatting

1. **f-strings (recommended)**

```python
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

2. **format() method**

```python
print("My name is {} and I am {} years old.".format(name, age))
```

---

### 🔍 Useful String Checks

```python
word = "Python"

print(word.isalpha())  # True (only letters)
print("123".isdigit()) # True
print("abc123".isalnum()) # True
print("hello".startswith("he")) # True
print("hello".endswith("lo"))   # True
```

---

### 📝 Practice Tasks (Day 4)

1. Take a string input and print the first and last characters.
2. Write a program to reverse a string using slicing.
3. Count how many times the letter `a` appears in a string.
4. Ask the user for their full name and print it in uppercase.
5. Format a string to display: *“My favorite subject is ___ and I am ___ years old.”*
