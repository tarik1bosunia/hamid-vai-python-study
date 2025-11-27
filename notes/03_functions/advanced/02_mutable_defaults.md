# Mutable Default Arguments - Common Pitfall

## ⚠️ The Dangerous Default

One of Python's most surprising behaviors: **mutable default arguments are evaluated once at function definition**, not each call. This leads to unexpected shared state.

---

## 🧩 The Problem

### ❌ Wrong: Shared Mutable Default

```python
def add_sequence(seq, collection=[]):
    """DANGEROUS: collection is shared across calls!"""
    collection.append(seq)
    return collection

# Each call reuses the SAME list!
result1 = add_sequence("ATCG")
print(result1)  # ['ATCG']

result2 = add_sequence("GCTA")
print(result2)  # ['ATCG', 'GCTA']  # 😱 Unexpected!

result3 = add_sequence("TAGC")
print(result3)  # ['ATCG', 'GCTA', 'TAGC']  # 😱 Still growing!
```

**Why?** The empty list `[]` is created **once** when Python defines the function, and all calls share that same list object.

---

## ✅ The Solution

### Use `None` as Default

```python
def add_sequence(seq, collection=None):
    """CORRECT: Create fresh list for each call"""
    if collection is None:
        collection = []  # New list each time
    
    collection.append(seq)
    return collection

# Each call gets a new list
result1 = add_sequence("ATCG")
print(result1)  # ['ATCG']

result2 = add_sequence("GCTA")
print(result2)  # ['GCTA']  # ✅ Fresh list!

result3 = add_sequence("TAGC")
print(result3)  # ['TAGC']  # ✅ Fresh list!
```

---

## 🧬 Bioinformatics Examples

### Example 1: Sequence Collection

```python
# ❌ WRONG
def collect_orfs(sequence, orf_list=[]):
    """Broken: orf_list shared across calls"""
    start = sequence.find('ATG')
    if start != -1:
        orf_list.append((start, sequence[start:start+9]))
    return orf_list

# ✅ CORRECT
def collect_orfs(sequence, orf_list=None):
    """Fixed: Create new list if not provided"""
    if orf_list is None:
        orf_list = []
    
    start = sequence.find('ATG')
    if start != -1:
        orf_list.append((start, sequence[start:start+9]))
    return orf_list

# Test
seq1_orfs = collect_orfs("ATGAAATAG")
seq2_orfs = collect_orfs("GCTATGCCC")
# Now seq1_orfs and seq2_orfs are separate!
```

### Example 2: Quality Filtering

```python
# ❌ WRONG
def filter_reads(reads, passed=[], failed=[]):
    """Broken: passed and failed are shared!"""
    for seq, quality in reads:
        if quality > 30:
            passed.append(seq)
        else:
            failed.append(seq)
    return passed, failed

# ✅ CORRECT
def filter_reads(reads, passed=None, failed=None):
    """Fixed: Create new lists"""
    if passed is None:
        passed = []
    if failed is None:
        failed = []
    
    for seq, quality in reads:
        if quality > 30:
            passed.append(seq)
        else:
            failed.append(seq)
    
    return passed, failed

# Test
batch1 = [("ATCG", 35), ("GCTA", 25)]
p1, f1 = filter_reads(batch1)

batch2 = [("TAGC", 40), ("CGAT", 20)]
p2, f2 = filter_reads(batch2)

print(f"Batch 1 passed: {len(p1)}, failed: {len(f1)}")
print(f"Batch 2 passed: {len(p2)}, failed: {len(f2)}")
```

### Example 3: Annotation Builder

```python
# ❌ WRONG
def parse_gff_line(line, features={}):
    """Broken: features dict is shared!"""
    fields = line.split('\t')
    feature_type = fields[2]
    features[feature_type] = features.get(feature_type, 0) + 1
    return features

# ✅ CORRECT
def parse_gff_line(line, features=None):
    """Fixed: Create new dict"""
    if features is None:
        features = {}
    
    fields = line.split('\t')
    feature_type = fields[2]
    features[feature_type] = features.get(feature_type, 0) + 1
    return features

# Test
line1 = "chr1\t.\tgene\t1000\t2000\t.\t+\t.\tID=gene1"
line2 = "chr1\t.\tCDS\t1200\t1800\t.\t+\t.\tID=cds1"

f1 = parse_gff_line(line1)
f2 = parse_gff_line(line2)
# Now f1 and f2 are separate dictionaries
```

---

## 🔍 Understanding the Issue

### What Python Actually Does

```python
def func(items=[]):
    return items

# At function DEFINITION time, Python creates:
# func.items_default = []  # A single list object

# Every call uses this same object:
# func(items=func.items_default)
```

### Visualizing the Problem

```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst

# Check the default object
print(id(append_item.__defaults__[0]))  # Memory address

result1 = append_item(1)
print(id(result1))  # Same address!

result2 = append_item(2)
print(id(result2))  # Same address!

# They're the SAME object
print(result1 is result2)  # True
```

---

## 🎯 When Mutable Defaults Are Okay

### Intentional Caching

```python
def expensive_calculation(n, cache={}):
    """Intentionally use shared cache"""
    if n in cache:
        return cache[n]
    
    # Expensive computation
    result = sum(i**2 for i in range(n))
    cache[n] = result
    return result

# Cache persists across calls
print(expensive_calculation(1000))  # Calculates
print(expensive_calculation(1000))  # Returns cached
```

**Note:** For production code, use `@lru_cache` instead.

---

## 📝 Practice Tasks

### Basic
1. Fix a broken function that uses `results=[]` as default
2. Create sequence parser with proper default handling
3. Write quality filter avoiding mutable defaults

### Intermediate
4. Debug code with multiple mutable defaults (`[], {}`)
5. Refactor existing broken code
6. Implement proper default for nested data structures

### Advanced
7. Create intentional cache using mutable default (then replace with `@lru_cache`)
8. Write test cases that catch mutable default bugs
9. Build linter rule to detect this pattern

---

## 💡 Key Takeaways

✓ **Mutable defaults** (lists, dicts, sets) are evaluated once at definition  
✓ All calls **share the same object** - dangerous!  
✓ **Solution:** Use `None` as default, create new object in function  
✓ Pattern: `if param is None: param = []`  
✓ Applies to: lists `[]`, dicts `{}`, sets `set()`, custom objects  
✓ **Not a problem** for immutable defaults (numbers, strings, tuples, None)  
✓ Intentional caching is rare valid use case  
✓ Use `@lru_cache` instead of manual caching  
✓ This catches even experienced Python developers!
