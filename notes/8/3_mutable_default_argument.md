# Mutable Default Arguments in Python — The Good vs The Bad 🧠

Python’s default arguments are powerful, but they hide a common pitfall when used with **mutable objects** (like lists or dictionaries). Let’s break it down step-by-step 👇

---

## 🔹 1. Background — Default Arguments Are Evaluated Once

When Python defines a function, **default argument values are evaluated only once**, not every time the function is called.

So if your default is a **mutable object** (`[]`, `{}`, etc.), every call **reuses the same object** in memory.

---

## ❌ The “Bad” Example — Shared Mutable Default

```python
def append_bad(item, bucket=[]):
    bucket.append(item)
    return bucket

print(append_bad(1))  # [1]
print(append_bad(2))  # [1, 2]
print(append_bad(3))  # [1, 2, 3]
```

### 🧩 Output

```
[1]
[1, 2]
[1, 2, 3]
```

### ⚠️ What Happened?

* The list `[]` was created **once** when Python read the function definition.
* Each function call reused that same list object.
* As a result, the list keeps growing across calls — even though you might expect a fresh one.

---

## ✅ The “Good” Example — Create a Fresh List Each Time

```python
def append_good(item, bucket=None):
    if bucket is None:
        bucket = []  # Create a new list for every call
    bucket.append(item)
    return bucket

print(append_good(1))  # [1]
print(append_good(2))  # [2]
print(append_good(3))  # [3]
```

### 🧩 Output

```
[1]
[2]
[3]
```

### ✅ Why It Works

* The default value `bucket=None` is **immutable**.
* Each time the function is called without a bucket, it creates a **new empty list** inside the function.
* Each call has its **own independent list**, avoiding shared state.

---

## 🔍 Visualizing the Difference

| Function Call    | Default Object Used? | List in Memory | Output      |
| ---------------- | -------------------- | -------------- | ----------- |
| `append_bad(1)`  | ✅ existing `[]`      | same list      | `[1]`       |
| `append_bad(2)`  | ✅ same list          | same list      | `[1, 2]`    |
| `append_bad(3)`  | ✅ same list          | same list      | `[1, 2, 3]` |
| `append_good(1)` | ❌ creates new        | new list       | `[1]`       |
| `append_good(2)` | ❌ creates new        | new list       | `[2]`       |
| `append_good(3)` | ❌ creates new        | new list       | `[3]`       |

---

## 💡 When Shared Mutable Defaults *Are* Useful

Sometimes you might *want* a shared mutable default — for example, caching results between calls:

```python
def cache_result(x, _cache={}):
    if x in _cache:
        print("Returning from cache")
        return _cache[x]
    print("Calculating...")
    _cache[x] = x ** 2
    return _cache[x]

print(cache_result(4))  # Calculating... 16
print(cache_result(4))  # Returning from cache 16
```

✅ Here, the shared `_cache` dictionary is **intentionally reused** to store results for performance.

---

## 🧭 Summary

| Concept                              | Behavior                         | Best Practice                                   |
| ------------------------------------ | -------------------------------- | ----------------------------------------------- |
| Default arguments are evaluated once | Mutable defaults are **shared**  | Use immutable defaults (like `None`, `0`, `''`) |
| Shared mutable state                 | Can cause unexpected results     | Create new object inside function               |
| When needed (e.g., caching)          | Use shared default intentionally | Clearly document it                             |

---

### 🏁 Takeaway

* 🧩 Mutable defaults can lead to **unexpected shared state**.
* ✅ Use `None` as a placeholder and **initialize inside** the function.
* ⚙️ Only use shared mutable defaults when you truly want persistence (e.g., caching).

**Rule of Thumb:**

> Use `None` for default parameters when the argument could be a mutable object.
