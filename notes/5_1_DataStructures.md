# Day 5: Data Structures

### 📋 Lists

* Ordered, changeable, allows duplicates.
* Created with square brackets `[]`.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Access
print(fruits[0])   # apple

# Modify
fruits[1] = "orange"
print(fruits)

# Methods
fruits.append("grape")
fruits.remove("apple")
print(fruits)

# Slicing
print(fruits[:2])  # first 2 elements
```

---

### 🔒 Tuples

* Ordered, **immutable** (cannot change), allows duplicates.
* Created with parentheses `()`.

```python
colors = ("red", "green", "blue")
print(colors[0])   # red

# Tuples cannot be changed
# colors[0] = "yellow" → ❌ Error
```

---

### 🔑 Sets

* Unordered, no duplicates.
* Created with curly braces `{}`.

```python
nums = {1, 2, 3, 3, 4}
print(nums)  # {1, 2, 3, 4}

nums.add(5)
nums.remove(2)

print(nums)

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B) # Union → {1, 2, 3, 4, 5}
print(A & B) # Intersection → {3}
print(A - B) # Difference → {1, 2}
```

---

### 📖 Dictionaries

* Key-value pairs.
* Created with curly braces `{}`.

```python
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

# Access
print(student["name"])  # Alice

# Modify
student["age"] = 21
print(student)

# Add new key-value
student["gpa"] = 3.8
print(student)

# Methods
print(student.keys())   # dict_keys([...])
print(student.values()) # dict_values([...])
print(student.items())  # dict_items([...])
```

---

### 📝 Practice Tasks (Day 5)

1. Create a list of 5 numbers and print the sum and average.
2. Store 3 favorite colors in a tuple and print them.
3. Create a set of numbers and demonstrate union and intersection.
4. Make a dictionary with keys: name, age, city. Print values nicely.
5. Update a dictionary to add a new key `country`.
