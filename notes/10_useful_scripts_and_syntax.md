# Day 10: Useful Scripts & Syntax (Notebook 3)

On this day, we practice **small but useful Python scripts** and learn **common syntax patterns** that make coding easier.

---

### ✅ Example 1: Swap Two Variables

```python
a = 10
b = 20

# Pythonic way to swap
a, b = b, a
print("a =", a, "b =", b)
```

**Output:**

```
a = 20 b = 10
```

---

### ✅ Example 2: Find Maximum in a List

```python
nums = [5, 9, 2, 7, 3]
print("Max:", max(nums))
print("Min:", min(nums))
```

---

### ✅ Example 3: Check if a Number is Prime

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(12))  # False
```

---

### ✅ Example 4: Factorial using Loop

```python
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))  # 120
```

---

### ✅ Example 5: Fibonacci Sequence

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(10)
```

**Output:**

```
0 1 1 2 3 5 8 13 21 34
```

---

### ✅ Example 6: Palindrome Checker

```python
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(is_palindrome("Madam"))     # True
print(is_palindrome("Hello"))     # False
```

---

### ✅ Example 7: Count Words in a Sentence

```python
sentence = "Python makes coding simple and powerful"
words = sentence.split()
print("Word count:", len(words))
```

---

### ✅ Example 8: Find Duplicates in a List

```python
nums = [1, 2, 3, 2, 4, 5, 1]
duplicates = [x for x in set(nums) if nums.count(x) > 1]
print("Duplicates:", duplicates)
```

---

### ✅ Example 9: Dictionary Word Frequency

```python
text = "apple banana apple orange banana apple"
words = text.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
```

**Output:**

```
{'apple': 3, 'banana': 2, 'orange': 1}
```

---

### ✅ Example 10: List Comprehension Tricks

```python
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
evens = [x for x in nums if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)
```

---

### 📝 Practice Tasks (Day 10)

1. Write a script to calculate the sum of digits of a number.
2. Write a function to generate the first N prime numbers.
3. Create a script to check if a string is a palindrome.
4. Write a function to count vowels in a sentence.
5. Generate a list of cubes of numbers 1–10 using list comprehension.
6. Write a script to find the second largest number in a list.


### see this also 
[1. range function in python](./10/1_range_function_in_python.md)

