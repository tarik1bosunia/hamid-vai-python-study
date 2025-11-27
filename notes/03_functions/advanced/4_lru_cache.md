# Understanding `functools.lru_cache` in Python ⚡

`@lru_cache` is a **built-in decorator** that automatically stores (“caches”) the results of previous function calls. When the same function is called again with the same arguments, Python returns the **cached result** instead of recomputing it — saving a lot of time in recursive or repetitive computations.

---

## 🔹 What Does LRU Mean?

**LRU** stands for **Least Recently Used** — meaning the cache automatically discards the oldest results when it reaches a maximum size (`maxsize`).

You can think of it as a small memory of recent function calls.

---

## 🧮 Example 1 — Without Cache (Slow Recursion)

```python
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Works
print(fib(35))  # Very slow ❌
```

**Why slow?** Each `fib()` call recomputes earlier results many times.

```
fib(5)
├─ fib(4)
│  ├─ fib(3)
│  │  ├─ fib(2)
│  │  │  ├─ fib(1)
│  │  │  └─ fib(0)
│  │  └─ fib(1)
│  └─ fib(2)
│     ├─ fib(1)
│     └─ fib(0)
└─ fib(3)   ← recomputed again!
```

That’s an **exponential time** algorithm (O(2ⁿ)).

---

## ✅ Example 2 — With `@lru_cache` (Fast Memoization)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))  # Instant ⚡
```

### 🧩 How It Works

* When you call `fib(5)`, results like `fib(3)` and `fib(4)` are stored in cache.
* If `fib(3)` is needed again later, Python returns the **cached result**.
* No recomputation = massive speedup.

| Version           | Time Complexity | Speed       |
| ----------------- | --------------- | ----------- |
| Without cache     | O(2ⁿ)           | ❌ Very slow |
| With `@lru_cache` | O(n)            | ✅ Fast      |

---

## ⚙️ Parameters of `@lru_cache`

```python
@lru_cache(maxsize=None)
```

* **`maxsize=None`** → Unlimited cache size.
* **`maxsize=128`** (default) → Keeps the 128 most recently used results.
* Old results are discarded automatically once cache is full.

Example:

```python
@lru_cache(maxsize=100)
def square(x):
    return x * x
```

---

## 🔍 Inspecting the Cache

You can view performance statistics using:

```python
print(fib.cache_info())
```

Example output:

```
CacheInfo(hits=28, misses=31, maxsize=None, currsize=31)
```

| Field        | Meaning                                       |
| ------------ | --------------------------------------------- |
| **hits**     | Number of times cached result was used        |
| **misses**   | Number of times the result was newly computed |
| **maxsize**  | Cache capacity                                |
| **currsize** | How many results are stored currently         |

---

## 🔄 Clearing the Cache

```python
fib.cache_clear()
```

This resets all stored results — useful for testing or when inputs change.

---

## 🧩 Example 3 — Factorial for Comparison

```python
def fact(n: int) -> int:
    if n < 2:
        return 1
    return n * fact(n - 1)
```

This recursion is efficient because it doesn’t recompute previous values — each call is unique. But Fibonacci reuses the same subproblems, making it a perfect candidate for caching.

---

## 💡 Where `lru_cache` Shines

* Recursive algorithms (like Fibonacci, DFS, dynamic programming)
* Expensive calculations (API calls, I/O heavy tasks)
* Repeated function calls with identical arguments

---

## 🧭 Summary

| Concept           | Description                                       |
| ----------------- | ------------------------------------------------- |
| **Decorator**     | `@lru_cache`                                      |
| **Purpose**       | Memorize function results to avoid recalculations |
| **Improvement**   | Turns exponential recursion into linear time      |
| **Best For**      | Recursive or repeated computations                |
| **Control Tools** | `.cache_info()` and `.cache_clear()`              |

---

### ✅ Takeaway

`@lru_cache` turns your **slow recursive function** into a **fast, memory‑efficient version** — all with just **one line of code**.

> 💡 “Compute once, reuse forever (until cache is full).”
