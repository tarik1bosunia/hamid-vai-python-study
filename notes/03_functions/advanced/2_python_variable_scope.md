# Python Variable Scope — `local`, `nonlocal`, and `global`

Understanding variable **scope** means knowing **where** each variable lives and **who can access or modify it**.

Python has 4 levels of scope — summarized by the LEGB rule:

| Level | Meaning                                                       | Example                             |
| ----- | ------------------------------------------------------------- | ----------------------------------- |
| L     | **Local** – inside the current function                       | variables defined within a function |
| E     | **Enclosing** – inside outer functions (for nested functions) | captured variables in closures      |
| G     | **Global** – defined at the top level of a module             | global constants or counters        |
| B     | **Built-in** – provided by Python itself                      | `len`, `range`, `print`, etc.       |

---

## 🔹 1. Local Scope

Variables defined inside a function are **local** to that function.

```python
def greet():
    message = "Hello"
    print(message)  # message is local

greet()
# print(message)  # ❌ Error: message is not defined
```

When you exit the function, the local variable disappears.

---

## 🔹 2. Global Scope

A variable defined **outside all functions** is **global**.

To modify a global variable **inside** a function, use the `global` keyword.

```python
counter = 0  # global variable

def tick():
    global counter     # tells Python to use the global counter
    counter += 1       # modify global variable

for _ in range(3):
    tick()

print(counter)  # Output: 3
```

If you forget the `global` keyword, Python will assume you’re creating a **new local variable**, not updating the global one.

---

## 🔹 3. Enclosing & Nonlocal Scope

Nested functions can **remember variables** from their enclosing (outer) functions. These are called **closures**.

```python
def make_acc(start=0):
    total = start  # 'total' is in enclosing scope of 'add'

    def add(delta):
        nonlocal total  # refers to 'total' in enclosing scope, not global
        total += delta
        return total

    return add
```

Now, when you call `make_acc`, it returns a function (`add`) that *remembers* its own `total` value.

```python
acc = make_acc(10)
print(acc(5))  # 15  → 10 + 5
print(acc(2))  # 17  → previous total (15) + 2
```

Each call to `make_acc()` creates a **separate memory** for `total`.

---

## 🧠 How It Works

1. `make_acc()` defines an inner function `add()`.
2. When `make_acc()` returns `add`, the variable `total` still lives — it’s captured in the closure.
3. Each time you call `acc(...)`, it uses that saved `total` and updates it using `nonlocal`.

---

## ✅ Quick Summary

| Keyword    | Used Inside    | Refers To                | Purpose                                |
| ---------- | -------------- | ------------------------ | -------------------------------------- |
| (none)     | function       | local variable           | normal local variable creation         |
| `global`   | function       | module/global scope      | modify a global variable               |
| `nonlocal` | inner function | outer/enclosing function | modify a variable from enclosing scope |

---

## 🧩 Example Visualization

```
Global: counter = 0
↓
 tick() modifies counter using 'global'

make_acc() defines:
   total = 10 (enclosing)
   add() uses nonlocal total

 acc = make_acc(10)
 acc(5) → total = 15
 acc(2) → total = 17
```

---

### 🏁 Key Takeaways

* Use **local** variables for temporary values.
* Use **global** only when necessary (avoid for shared mutable state).
* Use **nonlocal** for closures that update variables in outer scopes.
* Closures make your functions **stateful and powerful** — they remember context without using global variables.
