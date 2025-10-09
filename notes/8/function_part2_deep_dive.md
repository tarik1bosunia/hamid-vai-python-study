# Day 8 — Functions (Part 2): Deep Dive

Level up your function skills with scope, annotations, recursion, generators, decorators, error handling, and pro tips. All examples are copy‑paste ready.

---

## 1) Function Signatures & Parameter Kinds

Python distinguishes **how** arguments are passed.

```python
# a = positional-only, / marks end of positional-only
# c = keyword-only, * marks start of keyword-only
# b = can be positional or keyword

def f(a, /, b, *, c):
    print(a, b, c)

f(1, 2, c=3)        # ✅ OK
# f(a=1, b=2, c=3)  # ❌ a is positional-only
# f(1, 2, 3)        # ❌ c must be keyword
```

**Ordering rule:** `positional-only` → `pos-or-key` → `*args` → `keyword-only` → `**kwargs`.

```python
def signature_demo(x, y=0, /, z=1, *args, scale=1, **opts):
    return (x + y + z + sum(args)) * scale

signature_demo(1, 2, 3, 4, 5, scale=10, debug=True)
```

---

## 2) Scope: local, nonlocal, global

```python
counter = 0  # global

def tick():
    global counter
    counter += 1

# Closures with nonlocal

def make_acc(start=0):
    total = start
    def add(delta):
        nonlocal total
        total += delta
        return total
    return add

acc = make_acc(10)
print(acc(5))  # 15
print(acc(2))  # 17
```

**Rule of thumb:** prefer returning values to mutating globals. Use `nonlocal` to update state captured by an inner function.

---

## 3) Mutable Default Arguments (Common Gotcha)

```python
# Bad: the same list persists across calls

def append_bad(item, bucket=[]):
    bucket.append(item)
    return bucket

# Good: create a fresh list each call

def append_good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

---

## 4) Docstrings & Type Annotations

```python
def norm(x: float, y: float) -> float:
    """Return Euclidean norm of (x, y).

    Example:
        >>> norm(3, 4)
        5.0
    """
    return (x**2 + y**2) ** 0.5

print(norm.__doc__)
```

* **Docstrings** help users (`help(func)`) and tools.
* **Type hints** are not enforced at runtime but power linters/IDEs and `mypy`.

---

## 5) Recursion (with and without memoization)

```python
# Basic recursion

def fact(n: int) -> int:
    if n < 2:
        return 1
    return n * fact(n - 1)

# Fibonacci with memoization
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))
```

**Tip:** Use `@lru_cache` to speed up pure (deterministic, no side‑effects) recursive functions.

---

## 6) First‑Class & Higher‑Order Functions

```python
def apply_twice(f, x):
    return f(f(x))

print(apply_twice(lambda t: t + 1, 3))  # 5

# Currying with partial
from functools import partial

pow2 = partial(pow, exp=2)        # works when keyword exists
square = partial(pow, 2)          # or positional
print(square(7))  # 49
```

---

## 7) Closures (Remembering Values)

```python
def power_maker(p):
    def raise_p(x):
        return x ** p
    return raise_p

cube = power_maker(3)
print(cube(4))  # 64
```

Closures capture variables from the defining scope—great for configurable functions.

---

## 8) Decorators (Wrap Behavior)

```python
import time
from functools import wraps

def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = time.perf_counter() - t0
            print(f"{fn.__name__} took {dt:.4f}s")
    return wrapper

@timeit
def slow_add(a, b):
    time.sleep(0.3)
    return a + b

print(slow_add(2, 3))
```

* Use `@wraps` to preserve `__name__`, `__doc__`, and signature metadata.

---

## 9) Generators & `yield`

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for t in countdown(3):
    print(t)
```

**Why generators?** They are memory‑efficient (lazy). Perfect for streaming/large data.

### Generator Pipelines

```python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def filter_nonempty(lines):
    for ln in lines:
        if ln:
            yield ln

# Compose lazily
# for ln in filter_nonempty(read_lines("data.txt")):
#     print(ln)
```

---

## 10) Iterators & `__iter__` / `__next__`

```python
class Count:
    def __init__(self, start=0):
        self.n = start
    def __iter__(self):
        return self
    def __next__(self):
        self.n += 1
        return self.n

c = Count()
for _ in range(3):
    print(next(c))  # 1, 2, 3
```

---

## 11) Functional Tools: `map`, `filter`, `reduce`

```python
nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x*x, nums))
odd = list(filter(lambda x: x % 2, nums))

from functools import reduce
sum_all = reduce(lambda a, b: a + b, nums, 0)

print(squares, odd, sum_all)
```

> Prefer list comprehensions for readability, but know these tools.

---

## 12) Error Handling inside Functions

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")
    except TypeError:
        raise ValueError("Inputs must be numbers")

print(safe_div(6, 2))  # 3.0
print(safe_div(6, 0))  # inf
```

**Tip:** Raise precise errors with clear messages; catch only what you can handle meaningfully.

---

## 13) Defensive Programming & Contracts

```python
def mean(xs: list[float]) -> float:
    assert len(xs) > 0, "xs must be non-empty"
    for x in xs:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be numeric")
    return sum(xs) / len(xs)
```

* Use `assert` for internal invariants (may be disabled with `-O`).
* Use `raise` for user‑facing validation.

---

## 14) Packing & Unpacking (`*` and `**`)

```python
def area(w, h):
    return w * h

rect = (3, 4)
print(area(*rect))  # 12

opts = {"sep": " | ", "end": "\n\n"}
print("A", "B", **opts)
```

---

## 15) Small Utilities with Lambdas

```python
# Sort by last name then first name
names = ["Ada Lovelace", "Grace Hopper", "Alan Turing"]
print(sorted(names, key=lambda s: (s.split()[-1], s.split()[0])))

# Inline key functions
records = [("x", 10), ("y", 3), ("z", 7)]
print(max(records, key=lambda r: r[1]))
```

---

## 16) Performance Notes

* Prefer local variables; attribute/global lookups are slower inside hot loops.
* Use generators for large data; avoid building massive lists if you only iterate once.
* Memoize pure functions with `@lru_cache`.

---

## 17) Testing Functions Quickly

```python
def is_pal(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

# Quick checks
assert is_pal("Madam, I'm Adam")
assert not is_pal("Hello")
print("All tests passed!")
```

---

## 18) Putting It Together: Mini Case Study

```python
from functools import lru_cache, wraps

# 1) clean input (pure)
def clean_tokens(text: str) -> list[str]:
    return [t.lower() for t in text.split() if t.isalpha()]

# 2) term frequency (pure)
@lru_cache(maxsize=1024)
def tf(word: str, *docs: str) -> float:
    """Term frequency of `word` across documents."""
    count = 0
    total = 0
    for d in docs:
        toks = clean_tokens(d)
        total += len(toks)
        count += sum(1 for t in toks if t == word)
    return count / total if total else 0.0

# 3) timing decorator for diagnostics
def diag(fn):
    @wraps(fn)
    def w(*a, **k):
        val = fn(*a, **k)
        print(f"{fn.__name__} -> {val}")
        return val
    return w

@diag
def relevance(word, doc):
    return tf(word, doc)

print(relevance("python", "Python is fun. python rocks!"))
```

---

## 19) Practice Tasks (Part 2)

1. **Signature mastery:** Write a function `stats(a, /, *vals, mean=True, *, round_to=2)` that returns either mean or median of `vals` scaled by `a`, rounded to `round_to` decimals.
2. **Closure:** Build `make_limiter(n)` that returns a function which allows only the first `n` calls; later calls raise `RuntimeError`.
3. **Decorator:** Create `@retry(times=3)` that retries a function on `ValueError` and re‑raises if still failing.
4. **Generator:** Implement `window(seq, k)` yielding sliding windows of size `k` over `seq`.
5. **Performance:** Add `@lru_cache` to a recursive function (e.g., grid paths) and compare speed.

---

## 20) Quick Reference

* Positional‑only: `def f(a, /): ...`
* Keyword‑only: `def f(*, k): ...`
* Packs: `*args`, `**kwargs`
* Unpack calls: `f(*seq)`, `f(**mapping)`
* Memoize: `from functools import lru_cache`
* Preserve metadata: `from functools import wraps`
