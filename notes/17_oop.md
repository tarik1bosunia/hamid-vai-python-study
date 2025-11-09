# Python Object-Oriented Programming (OOP) — A Practical Guide

> **📚 Learning Objective**: Master OOP concepts to write cleaner, more maintainable, and reusable Python code.

OOP helps you model real-world concepts as Python objects. This guide is hands-on: short explanations followed by runnable examples and gotchas. Feel free to copy, paste, and experiment.

---

## 📑 Table of Contents

1. [What is OOP?](#what-is-oop)
2. [Classes and Objects](#classes-and-objects)
3. [The `__init__` Method (Constructor)](#the-__init__-method-constructor)
4. [Instance Attributes vs Class Attributes](#instance-attributes-vs-class-attributes)
5. [Methods](#methods)
6. [The `self` Parameter](#the-self-parameter)
7. [Encapsulation](#encapsulation)
8. [Inheritance](#inheritance)
9. [Polymorphism](#polymorphism)
10. [Special Methods (Magic/Dunder Methods)](#special-methods-magicdunder-methods)
11. [Class Methods and Static Methods](#class-methods-and-static-methods)
12. [Property Decorators](#property-decorators)
13. [Real-World Example: DNA Sequence Analyzer](#real-world-example-dna-sequence-analyzer)
14. [Common Pitfalls and Best Practices](#common-pitfalls-and-best-practices)

---

## What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects** (data + behavior) rather than functions and logic alone.

### Why Use OOP?

✅ **Modularity**: Code is organized into reusable classes  
✅ **Maintainability**: Changes are localized to specific classes  
✅ **Reusability**: Inherit and extend existing classes  
✅ **Abstraction**: Hide complex implementation details  

### Four Pillars of OOP

1. **Encapsulation** - Bundling data and methods together
2. **Inheritance** - Creating new classes from existing ones
3. **Polymorphism** - Same interface, different implementations
4. **Abstraction** - Hiding complex details, showing only essentials

---

## Classes and Objects

### What is a Class?

A **class** is a blueprint for creating objects. It defines attributes (data) and methods (behavior).

### What is an Object?

An **object** is an instance of a class. You can create multiple objects from one class.

### Basic Syntax

```python
# Define a class
class Dog:
    pass  # Empty class for now

# Create objects (instances)
dog1 = Dog()
dog2 = Dog()

print(dog1)  # <__main__.Dog object at 0x...>
print(dog2)  # <__main__.Dog object at 0x...>
print(dog1 == dog2)  # False (different objects)
```

**Key Point**: Each object has a unique memory address.

---

## The `__init__` Method (Constructor)

The `__init__` method is called automatically when you create a new object. It initializes the object's attributes.

### Syntax

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create objects with initial values
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  # Buddy
print(dog2.age)   # 5
```

### With Default Parameters

```python
class Dog:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

dog1 = Dog("Buddy")  # age defaults to 0
dog2 = Dog("Max", 5)

print(dog1.age)  # 0
print(dog2.age)  # 5
```

---

## Instance Attributes vs Class Attributes

### Instance Attributes

- Unique to each object
- Defined in `__init__` using `self`

### Class Attributes

- Shared by all instances of the class
- Defined directly in the class body

### Example

```python
class Dog:
    species = "Canis familiaris"  # Class attribute (shared)
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute (unique)
        self.age = age    # Instance attribute (unique)

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Instance attributes are different
print(dog1.name)  # Buddy
print(dog2.name)  # Max

# Class attribute is shared
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris
print(Dog.species)   # Canis familiaris

# Modifying class attribute affects all instances
Dog.species = "Canis lupus"
print(dog1.species)  # Canis lupus
print(dog2.species)  # Canis lupus
```

### ⚠️ Common Pitfall: Mutable Class Attributes

```python
# ❌ WRONG: Don't use mutable defaults as class attributes
class Dog:
    tricks = []  # Shared by all instances!
    
    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog()
dog2 = Dog()

dog1.add_trick("sit")
print(dog2.tricks)  # ['sit'] - UNEXPECTED!

# ✅ CORRECT: Use instance attributes
class Dog:
    def __init__(self):
        self.tricks = []  # Each instance has its own list
    
    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog()
dog2 = Dog()

dog1.add_trick("sit")
print(dog1.tricks)  # ['sit']
print(dog2.tricks)  # [] - EXPECTED!
```

---

## Methods

Methods are functions defined inside a class. They define the behavior of objects.

### Instance Methods

- Operate on instance data
- First parameter is always `self`

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_age_in_human_years(self):
        return self.age * 7

dog = Dog("Buddy", 3)
print(dog.bark())  # Buddy says Woof!
print(dog.get_age_in_human_years())  # 21
```

### Methods with Parameters

```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def greet(self, person_name):
        return f"{self.name} greets {person_name}!"

dog = Dog("Buddy")
print(dog.greet("Alice"))  # Buddy greets Alice!
```

---

## The `self` Parameter

`self` refers to the current instance of the class. It gives you access to the instance's attributes and methods.

### Why `self`?

- Python doesn't automatically know which object you're working with
- `self` makes it explicit

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1  # self.count refers to this instance's count
    
    def get_count(self):
        return self.count

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()
c2.increment()

print(c1.get_count())  # 2
print(c2.get_count())  # 1
```

### 💡 Note

- You can name it anything, but `self` is the convention
- Python automatically passes the instance as the first argument

```python
class Test:
    def method(this):  # 'this' instead of 'self' (not recommended)
        print(this)

obj = Test()
obj.method()  # Works, but don't do this!
```

---

## Encapsulation

**Encapsulation** means bundling data and methods together, and controlling access to them.

### Public, Protected, and Private

In Python, access control is by convention:

| Prefix | Type | Access | Example |
|--------|------|--------|---------|
| None | Public | Anyone can access | `self.name` |
| `_` | Protected | Internal use (by convention) | `self._age` |
| `__` | Private | Name mangled | `self.__secret` |

### Example

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._account_id = "12345"  # Protected (convention)
        self.__balance = balance     # Private (name mangled)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 1000)

# Public access
print(account.owner)  # Alice

# Protected access (still accessible, but discouraged)
print(account._account_id)  # 12345

# Private access (not directly accessible)
# print(account.__balance)  # AttributeError!

# Use public methods instead
print(account.get_balance())  # 1000
account.deposit(500)
print(account.get_balance())  # 1500

# Name mangling reveals the private attribute (don't do this!)
print(account._BankAccount__balance)  # 1500
```

### Why Encapsulation?

✅ Control how data is accessed and modified  
✅ Prevent accidental changes  
✅ Hide implementation details  
✅ Make refactoring easier  

---

## Inheritance

**Inheritance** allows you to create a new class based on an existing class.

- **Parent/Base/Super Class**: The class being inherited from
- **Child/Derived/Sub Class**: The class that inherits

### Basic Inheritance

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

# Child class
class Dog(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

### Using `super()`

`super()` lets you call methods from the parent class.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def info(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent __init__
        self.breed = breed
    
    def info(self):
        base_info = super().info()  # Call parent method
        return f"{base_info} of breed {self.breed}"

dog = Dog("Buddy", "Golden Retriever")
print(dog.info())  # Buddy is a Dog of breed Golden Retriever
```

### Multiple Inheritance

Python supports multiple inheritance (inheriting from multiple classes).

```python
class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming fast!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())   # Flying high!
print(duck.swim())  # Swimming fast!
print(duck.quack()) # Quack!
```

### Method Resolution Order (MRO)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B
print(D.mro())     # Shows the order: D -> B -> C -> A -> object
```

---

## Polymorphism

**Polymorphism** means "many forms". The same method name can behave differently in different classes.

### Duck Typing

"If it walks like a duck and quacks like a duck, it's a duck."

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_it_speak(animal):
    print(animal.speak())  # Works with any object that has speak()

dog = Dog()
cat = Cat()
duck = Duck()

make_it_speak(dog)   # Woof!
make_it_speak(cat)   # Meow!
make_it_speak(duck)  # Quack!
```

### Polymorphism with Inheritance

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 10), Circle(7), Rectangle(3, 4)]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 50
# Area: 153.86
# Area: 12
```

---

## Special Methods (Magic/Dunder Methods)

Special methods (also called magic or dunder methods) start and end with double underscores (`__`). They let you customize how your objects behave.

### Common Special Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `__init__` | Constructor | `obj = MyClass()` |
| `__str__` | Human-readable string | `str(obj)`, `print(obj)` |
| `__repr__` | Developer-friendly string | `repr(obj)` |
| `__len__` | Length | `len(obj)` |
| `__eq__` | Equality | `obj1 == obj2` |
| `__lt__` | Less than | `obj1 < obj2` |
| `__add__` | Addition | `obj1 + obj2` |
| `__getitem__` | Indexing | `obj[key]` |
| `__setitem__` | Setting items | `obj[key] = value` |
| `__call__` | Make object callable | `obj()` |

### Examples

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        # For end users
        return f"{self.title} by {self.author}"
    
    def __repr__(self):
        # For developers (should ideally recreate the object)
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages

book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 592)
book3 = Book("Python Crash Course", "Eric Matthes", 544)

print(book1)              # Python Crash Course by Eric Matthes
print(repr(book1))        # Book('Python Crash Course', 'Eric Matthes', 544)
print(len(book1))         # 544
print(book1 == book3)     # True
print(book1 == book2)     # False
print(book1 < book2)      # True (544 < 592)
```

### Arithmetic Operations

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)

v3 = v1 + v2
print(v3)  # Vector(7, 10)

v4 = v1 * 3
print(v4)  # Vector(6, 9)
```

### Making Objects Callable

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## Class Methods and Static Methods

### Instance Methods

- Work with instance data
- First parameter is `self`

### Class Methods

- Work with class data
- First parameter is `cls`
- Decorated with `@classmethod`
- Can be used as alternative constructors

### Static Methods

- Don't work with instance or class data
- No special first parameter
- Decorated with `@staticmethod`
- Used for utility functions

### Example

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Instance method
    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    # Class method (alternative constructor)
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    # Static method (utility function)
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Using instance method
date1 = Date(2024, 3, 15)
print(date1.display())  # 2024-03-15

# Using class method
date2 = Date.from_string("2024-12-25")
print(date2.display())  # 2024-12-25

# Using static method
print(Date.is_leap_year(2024))  # True
print(Date.is_leap_year(2023))  # False
```

### When to Use Each?

| Type | When to Use |
|------|-------------|
| **Instance Method** | Needs access to instance data (`self`) |
| **Class Method** | Needs access to class data or alternative constructor |
| **Static Method** | Related to the class but doesn't need instance or class data |

---

## Property Decorators

**Properties** let you add getter, setter, and deleter methods to an attribute, making it look like a simple attribute from outside.

### Without Properties (Ugly)

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

temp = Temperature(25)
print(temp.get_celsius())  # 25
temp.set_celsius(30)
print(temp.get_celsius())  # 30
```

### With Properties (Clean)

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)      # 25 (looks like an attribute!)
print(temp.fahrenheit)   # 77.0

temp.celsius = 30        # Uses setter
print(temp.celsius)      # 30

# temp.celsius = -300    # ValueError!
```

### Read-Only Property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2
    
    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

circle = Circle(5)
print(circle.radius)         # 5
print(circle.area)           # 78.5
print(circle.circumference)  # 31.400000000000002

# circle.area = 100  # AttributeError (read-only)
```

---

## Real-World Example: DNA Sequence Analyzer

Let's build a practical bioinformatics class that uses OOP principles.

```python
class DNASequence:
    """
    A class to represent and analyze DNA sequences.
    """
    
    # Class attribute: valid nucleotides
    VALID_NUCLEOTIDES = set("ATCG")
    
    def __init__(self, sequence, name="Unnamed"):
        """
        Initialize a DNA sequence.
        
        Args:
            sequence (str): DNA sequence string
            name (str): Name/ID of the sequence
        """
        self.name = name
        self.sequence = sequence.upper().strip()
        self._validate()
    
    def _validate(self):
        """Private method to validate the sequence."""
        invalid = set(self.sequence) - self.VALID_NUCLEOTIDES
        if invalid:
            raise ValueError(f"Invalid nucleotides found: {invalid}")
    
    @property
    def length(self):
        """Get the length of the sequence."""
        return len(self.sequence)
    
    @property
    def gc_content(self):
        """Calculate GC content as a percentage."""
        if self.length == 0:
            return 0.0
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return (gc_count / self.length) * 100
    
    def complement(self):
        """Return the complement sequence."""
        complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complement_map[base] for base in self.sequence)
    
    def reverse_complement(self):
        """Return the reverse complement sequence."""
        return self.complement()[::-1]
    
    def transcribe(self):
        """Transcribe DNA to RNA (T -> U)."""
        return self.sequence.replace('T', 'U')
    
    def count_nucleotides(self):
        """Return a dictionary of nucleotide counts."""
        return {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'G': self.sequence.count('G'),
            'C': self.sequence.count('C')
        }
    
    @classmethod
    def from_file(cls, filename):
        """
        Alternative constructor: create DNA sequence from a file.
        
        Args:
            filename (str): Path to file containing DNA sequence
        
        Returns:
            DNASequence: New DNASequence object
        """
        with open(filename, 'r') as f:
            lines = f.readlines()
            name = lines[0].strip().lstrip('>')
            sequence = ''.join(line.strip() for line in lines[1:])
        return cls(sequence, name)
    
    def __str__(self):
        """User-friendly string representation."""
        preview = self.sequence[:50] + "..." if self.length > 50 else self.sequence
        return f"{self.name}: {preview} (Length: {self.length})"
    
    def __repr__(self):
        """Developer-friendly representation."""
        return f"DNASequence('{self.sequence[:20]}...', '{self.name}')"
    
    def __len__(self):
        """Support len() function."""
        return self.length
    
    def __eq__(self, other):
        """Support equality comparison."""
        return self.sequence == other.sequence
    
    def __add__(self, other):
        """Support concatenation with + operator."""
        new_seq = self.sequence + other.sequence
        new_name = f"{self.name}+{other.name}"
        return DNASequence(new_seq, new_name)
    
    def __getitem__(self, index):
        """Support indexing and slicing."""
        return self.sequence[index]


# Usage examples
if __name__ == "__main__":
    # Create a DNA sequence
    dna = DNASequence("ATCGATCGATCG", "Sample1")
    
    print(dna)  # Sample1: ATCGATCGATCG (Length: 12)
    print(f"Length: {len(dna)}")  # 12
    print(f"GC Content: {dna.gc_content:.2f}%")  # 50.00%
    
    print(f"Complement: {dna.complement()}")  # TAGCTAGCTAGC
    print(f"Reverse Complement: {dna.reverse_complement()}")  # CGATCGATCGAT
    print(f"RNA: {dna.transcribe()}")  # AUCGAUCGAUCG
    
    print(f"Nucleotide counts: {dna.count_nucleotides()}")
    # {'A': 3, 'T': 3, 'G': 3, 'C': 3}
    
    # Indexing
    print(f"First nucleotide: {dna[0]}")  # A
    print(f"First 6 bases: {dna[:6]}")    # ATCGAT
    
    # Concatenation
    dna2 = DNASequence("GGCCTTAA", "Sample2")
    combined = dna + dna2
    print(combined)  # Sample1+Sample2: ATCGATCGATCGGGCCTTAA (Length: 20)
    
    # Comparison
    dna3 = DNASequence("ATCGATCGATCG", "Sample3")
    print(dna == dna3)  # True (same sequence)
    print(dna == dna2)  # False (different sequence)
```

### Key OOP Concepts Used

✅ **Encapsulation**: Private validation method (`_validate`)  
✅ **Properties**: Computed attributes (`length`, `gc_content`)  
✅ **Class Methods**: Alternative constructor (`from_file`)  
✅ **Special Methods**: `__str__`, `__repr__`, `__len__`, `__eq__`, `__add__`, `__getitem__`  
✅ **Class Attributes**: Shared constants (`VALID_NUCLEOTIDES`)  

---

## Common Pitfalls and Best Practices

### ❌ Pitfall 1: Mutable Default Arguments

```python
# WRONG
class DNACollection:
    def __init__(self, sequences=[]):  # DON'T DO THIS!
        self.sequences = sequences

# All instances share the same list!
col1 = DNACollection()
col2 = DNACollection()
col1.sequences.append("ATCG")
print(col2.sequences)  # ['ATCG'] - UNEXPECTED!

# ✅ CORRECT
class DNACollection:
    def __init__(self, sequences=None):
        self.sequences = sequences if sequences is not None else []
```

### ❌ Pitfall 2: Forgetting `self`

```python
# WRONG
class Dog:
    def __init__(self, name):
        name = name  # Missing self!
    
    def bark(self):
        print(name)  # Missing self!

# ✅ CORRECT
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name)
```

### ❌ Pitfall 3: Modifying Class Attributes Incorrectly

```python
class Counter:
    count = 0  # Class attribute
    
    def __init__(self):
        self.count += 1  # Creates instance attribute!

# ✅ CORRECT
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1  # Modifies class attribute
```

### ✅ Best Practice 1: Use Properties for Computed Attributes

```python
# GOOD
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14 * self.radius ** 2
```

### ✅ Best Practice 2: Use `__repr__` for Debugging

```python
class Gene:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence
    
    def __repr__(self):
        return f"Gene(name='{self.name}', sequence='{self.sequence[:20]}...')"
```

### ✅ Best Practice 3: Prefer Composition Over Inheritance

Sometimes it's better to include an object rather than inherit from it.

```python
# Instead of inheriting
class Dog(list):  # Is a dog really a list?
    pass

# Use composition
class Dog:
    def __init__(self):
        self.tricks = []  # Has a list
```

### ✅ Best Practice 4: Follow Naming Conventions

- Class names: `PascalCase` (e.g., `DNASequence`)
- Methods/attributes: `snake_case` (e.g., `gc_content`)
- Private: `_single_underscore` (e.g., `_validate`)
- Name mangling: `__double_underscore` (e.g., `__private_data`)
- Constants: `UPPER_CASE` (e.g., `MAX_LENGTH`)

---

## 📝 Practice Exercises

### Exercise 1: Student Class

Create a `Student` class with:
- Attributes: `name`, `age`, `grades` (list)
- Methods: `add_grade()`, `average_grade()`, `is_passing()` (average >= 60)

<details>
<summary>Solution</summary>

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def is_passing(self):
        return self.average_grade() >= 60
    
    def __str__(self):
        return f"{self.name} (Age: {self.age}, Average: {self.average_grade():.2f})"

# Test
student = Student("Alice", 20)
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(student)  # Alice (Age: 20, Average: 85.00)
print(student.is_passing())  # True
```
</details>

### Exercise 2: Bank Account with Inheritance

Create:
- `BankAccount` base class with `deposit()` and `withdraw()`
- `SavingsAccount` with interest calculation
- `CheckingAccount` with overdraft protection

<details>
<summary>Solution</summary>

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False
    
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f"{self.owner}'s account: ${self._balance:.2f}"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.01):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return True
        return False

# Test
savings = SavingsAccount("Alice", 1000, 0.05)
print(savings)  # Alice's account: $1000.00
savings.add_interest()
print(savings)  # Alice's account: $1050.00

checking = CheckingAccount("Bob", 100, 50)
checking.withdraw(120)  # Uses overdraft
print(checking)  # Bob's account: $-20.00
```
</details>

### Exercise 3: RNA Sequence Class

Create an `RNASequence` class similar to `DNASequence` with:
- Valid nucleotides: A, U, C, G (not T!)
- Method to translate to protein (simplified)
- Method to find start codon (AUG)

---

## 🎓 Summary

### Key Takeaways

1. **Classes** are blueprints; **objects** are instances
2. **`__init__`** initializes objects
3. **`self`** refers to the current instance
4. **Encapsulation**: Bundle data and methods, control access
5. **Inheritance**: Reuse code from parent classes
6. **Polymorphism**: Same interface, different implementations
7. **Special methods**: Customize object behavior
8. **Properties**: Make methods look like attributes
9. **Class methods**: Work with class data
10. **Static methods**: Utility functions

### When to Use OOP?

✅ Modeling real-world entities (Dog, Student, BankAccount)  
✅ Creating reusable components (DNASequence)  
✅ Managing complex state (GameCharacter)  
✅ Building frameworks and libraries  

❌ Simple scripts with procedural logic  
❌ One-time data processing  
❌ Pure mathematical computations  

---

## 📚 Further Reading

- [Python Official Tutorial - Classes](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)

---

**Happy Coding! 🐍✨**
