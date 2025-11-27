# Mini Calculator Project - Complete Guide

## Project Overview

Build a fully-featured console-based calculator application that demonstrates fundamental Python concepts including functions, user input, error handling, and control flow. This project serves as an excellent introduction to practical Python programming and software design principles.

**Skills Demonstrated:**
- Function definition and organization
- User input handling and validation
- Error handling and exception management
- Control flow (if/elif/else, loops)
- String formatting and output
- Code organization and modularity

**Project Difficulty:** Beginner  
**Estimated Time:** 2-4 hours  
**Prerequisites:** Basic Python syntax, functions, conditionals

---

## Version 1: Basic Calculator

### Features
- Four basic operations: +, -, ×, ÷
- Simple menu-driven interface
- Division by zero handling
- Input validation

### Complete Code

```python
"""
Basic Calculator - Version 1
Performs basic arithmetic operations
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """
    Return the quotient of x divided by y.
    Returns error message if y is zero.
    """
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def main():
    """Main calculator interface."""
    print("=" * 40)
    print("     SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nSelect operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (×)")
    print("4. Divide (÷)")
    print("=" * 40)
    
    # Get operation choice
    choice = input("\nEnter choice (1/2/3/4): ").strip()
    
    # Validate choice
    if choice not in ('1', '2', '3', '4'):
        print("❌ Invalid choice! Please select 1, 2, 3, or 4.")
        return
    
    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input! Please enter valid numbers.")
        return
    
    # Perform calculation
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "×"
    else:  # choice == '4'
        result = divide(num1, num2)
        operation = "÷"
    
    # Display result
    print("\n" + "=" * 40)
    print(f"Result: {num1} {operation} {num2} = {result}")
    print("=" * 40)

if __name__ == "__main__":
    main()
```

### Sample Output

```
========================================
     SIMPLE CALCULATOR
========================================

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (×)
4. Divide (÷)
========================================

Enter choice (1/2/3/4): 1
Enter first number: 15.5
Enter second number: 7.3

========================================
Result: 15.5 + 7.3 = 22.8
========================================
```

---

## Version 2: Enhanced Calculator with Loop

### New Features
- Continuous operation (loop until user quits)
- Memory function (store last result)
- Operation history
- Enhanced error messages

### Complete Code

```python
"""
Enhanced Calculator - Version 2
Continuous operation with memory and history
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_number(prompt, allow_memory=False, memory=None):
    """
    Get a number from user with optional memory support.
    
    Args:
        prompt: Input prompt message
        allow_memory: If True, user can enter 'M' to use memory
        memory: Current memory value
    
    Returns:
        float: The entered number
    """
    while True:
        user_input = input(prompt).strip().upper()
        
        if allow_memory and user_input == 'M' and memory is not None:
            print(f"  (Using memory: {memory})")
            return memory
        
        try:
            return float(user_input)
        except ValueError:
            print("  ❌ Invalid input! Please enter a valid number.")

def display_menu():
    """Display calculator menu."""
    print("\n" + "=" * 50)
    print("           CALCULATOR - Enhanced Version")
    print("=" * 50)
    print("Operations:")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (×)")
    print("  4. Divide (÷)")
    print("  5. View History")
    print("  6. Clear Memory")
    print("  Q. Quit")
    print("=" * 50)

def main():
    """Main calculator with continuous operation."""
    memory = None
    history = []
    
    print("Welcome to Enhanced Calculator!")
    print("Tip: Enter 'M' to use last result\n")
    
    while True:
        display_menu()
        
        choice = input("\nEnter choice: ").strip().upper()
        
        # Handle quit
        if choice == 'Q':
            print("\n✓ Thank you for using Calculator!")
            break
        
        # Handle history view
        if choice == '5':
            if not history:
                print("\n  No calculations yet.")
            else:
                print("\n  Calculation History:")
                for i, calc in enumerate(history, 1):
                    print(f"  {i}. {calc}")
            continue
        
        # Handle memory clear
        if choice == '6':
            memory = None
            print("\n  ✓ Memory cleared!")
            continue
        
        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("\n  ❌ Invalid choice! Please try again.")
            continue
        
        # Get numbers
        print()
        num1 = get_number("First number: ", allow_memory=True, memory=memory)
        num2 = get_number("Second number: ", allow_memory=True, memory=memory)
        
        # Perform operation
        try:
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "×"
            else:  # choice == '4'
                result = divide(num1, num2)
                operation = "÷"
            
            # Store in memory and history
            memory = result
            calc_string = f"{num1} {operation} {num2} = {result}"
            history.append(calc_string)
            
            # Display result
            print("\n" + "-" * 50)
            print(f"  Result: {calc_string}")
            print(f"  (Stored in memory)")
            print("-" * 50)
            
        except ValueError as e:
            print(f"\n  ❌ Error: {e}")
        except Exception as e:
            print(f"\n  ❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

---

## Version 3: Scientific Calculator

### New Features
- Advanced operations (power, square root, percentage)
- Trigonometric functions (sin, cos, tan)
- Logarithmic functions
- Constants (π, e)

### Complete Code

```python
"""
Scientific Calculator - Version 3
Advanced mathematical operations
"""

import math

# ===== Basic Operations =====

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# ===== Advanced Operations =====

def power(x, y):
    """Calculate x raised to power y."""
    return x ** y

def square_root(x):
    """Calculate square root of x."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(x)

def percentage(x, y):
    """Calculate x% of y."""
    return (x / 100) * y

# ===== Trigonometric Functions =====

def sine(x, degrees=True):
    """Calculate sine of x (degrees by default)."""
    if degrees:
        x = math.radians(x)
    return math.sin(x)

def cosine(x, degrees=True):
    """Calculate cosine of x (degrees by default)."""
    if degrees:
        x = math.radians(x)
    return math.cos(x)

def tangent(x, degrees=True):
    """Calculate tangent of x (degrees by default)."""
    if degrees:
        x = math.radians(x)
    return math.tan(x)

# ===== Logarithmic Functions =====

def natural_log(x):
    """Calculate natural logarithm (base e)."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x)

def log_base_10(x):
    """Calculate logarithm base 10."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log10(x)

# ===== Main Program =====

def display_menu():
    """Display scientific calculator menu."""
    print("\n" + "=" * 60)
    print("         SCIENTIFIC CALCULATOR")
    print("=" * 60)
    print("Basic Operations:")
    print("  1. Add              2. Subtract")
    print("  3. Multiply         4. Divide")
    print("\nAdvanced Operations:")
    print("  5. Power (x^y)      6. Square Root")
    print("  7. Percentage       8. Absolute Value")
    print("\nTrigonometry (degrees):")
    print("  9. Sine            10. Cosine")
    print(" 11. Tangent")
    print("\nLogarithms:")
    print(" 12. Natural Log    13. Log base 10")
    print("\nConstants:")
    print(" 14. π (pi)         15. e (Euler's number)")
    print("\nOther:")
    print("  H. History         C. Clear Memory       Q. Quit")
    print("=" * 60)

def main():
    """Main scientific calculator."""
    memory = None
    history = []
    
    print("🔬 Welcome to Scientific Calculator!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter choice: ").strip().upper()
        
        # Handle quit
        if choice == 'Q':
            print("\n✓ Thank you for using Scientific Calculator!")
            break
        
        # Handle history
        if choice == 'H':
            if not history:
                print("\n  No calculations yet.")
            else:
                print("\n  Calculation History:")
                for i, calc in enumerate(history[-10:], 1):  # Show last 10
                    print(f"  {i}. {calc}")
            continue
        
        # Handle clear memory
        if choice == 'C':
            memory = None
            print("\n  ✓ Memory cleared!")
            continue
        
        # Handle constants
        if choice == '14':
            print(f"\n  π = {math.pi}")
            memory = math.pi
            history.append(f"π = {math.pi}")
            continue
        
        if choice == '15':
            print(f"\n  e = {math.e}")
            memory = math.e
            history.append(f"e = {math.e}")
            continue
        
        # Operations requiring two numbers
        two_number_ops = ['1', '2', '3', '4', '5', '7']
        # Operations requiring one number
        one_number_ops = ['6', '8', '9', '10', '11', '12', '13']
        
        if choice not in two_number_ops + one_number_ops:
            print("\n  ❌ Invalid choice!")
            continue
        
        try:
            # Get input(s)
            if choice in two_number_ops:
                num1 = float(input("\nFirst number: "))
                num2 = float(input("Second number: "))
            else:
                num1 = float(input("\nEnter number: "))
            
            # Perform operation
            if choice == '1':
                result = add(num1, num2)
                calc = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                calc = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                calc = f"{num1} × {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                calc = f"{num1} ÷ {num2} = {result}"
            elif choice == '5':
                result = power(num1, num2)
                calc = f"{num1}^{num2} = {result}"
            elif choice == '6':
                result = square_root(num1)
                calc = f"√{num1} = {result}"
            elif choice == '7':
                result = percentage(num1, num2)
                calc = f"{num1}% of {num2} = {result}"
            elif choice == '8':
                result = abs(num1)
                calc = f"|{num1}| = {result}"
            elif choice == '9':
                result = sine(num1)
                calc = f"sin({num1}°) = {result}"
            elif choice == '10':
                result = cosine(num1)
                calc = f"cos({num1}°) = {result}"
            elif choice == '11':
                result = tangent(num1)
                calc = f"tan({num1}°) = {result}"
            elif choice == '12':
                result = natural_log(num1)
                calc = f"ln({num1}) = {result}"
            elif choice == '13':
                result = log_base_10(num1)
                calc = f"log₁₀({num1}) = {result}"
            
            # Store and display
            memory = result
            history.append(calc)
            
            print("\n" + "-" * 60)
            print(f"  Result: {calc}")
            print(f"  (Stored in memory)")
            print("-" * 60)
            
        except ValueError as e:
            print(f"\n  ❌ Error: {e}")
        except Exception as e:
            print(f"\n  ❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

---

## Bioinformatics Extension: Sequence Calculator

### Features
- Calculate GC content
- Count nucleotide/amino acid frequencies
- Compute molecular weight
- Calculate melting temperature (Tm)

### Code

```python
"""
Bioinformatics Sequence Calculator
Special calculations for DNA/RNA/Protein sequences
"""

def gc_content(sequence):
    """Calculate GC content percentage."""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100 if sequence else 0

def nucleotide_count(sequence):
    """Count each nucleotide in sequence."""
    sequence = sequence.upper()
    return {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }

def molecular_weight_dna(sequence):
    """Calculate molecular weight of DNA sequence (g/mol)."""
    weights = {'A': 331.2, 'T': 322.2, 'G': 347.2, 'C': 307.2}
    sequence = sequence.upper()
    return sum(weights.get(base, 0) for base in sequence)

def melting_temperature(sequence):
    """
    Calculate Tm using Wallace rule (for sequences <14 bp).
    Tm = 4(G+C) + 2(A+T)
    """
    sequence = sequence.upper()
    gc = sequence.count('G') + sequence.count('C')
    at = sequence.count('A') + sequence.count('T')
    return 4 * gc + 2 * at

def main():
    """Bioinformatics calculator interface."""
    print("=" * 60)
    print("     BIOINFORMATICS SEQUENCE CALCULATOR")
    print("=" * 60)
    print("\nCalculations:")
    print("  1. GC Content (%)")
    print("  2. Nucleotide Count")
    print("  3. Molecular Weight")
    print("  4. Melting Temperature (Tm)")
    print("  Q. Quit")
    print("=" * 60)
    
    while True:
        choice = input("\nEnter choice: ").strip().upper()
        
        if choice == 'Q':
            break
        
        if choice not in ('1', '2', '3', '4'):
            print("❌ Invalid choice!")
            continue
        
        sequence = input("Enter DNA sequence: ").strip()
        
        if not sequence:
            print("❌ Empty sequence!")
            continue
        
        print("\n" + "-" * 60)
        
        if choice == '1':
            gc = gc_content(sequence)
            print(f"GC Content: {gc:.2f}%")
        
        elif choice == '2':
            counts = nucleotide_count(sequence)
            print("Nucleotide Counts:")
            for base, count in counts.items():
                print(f"  {base}: {count}")
        
        elif choice == '3':
            mw = molecular_weight_dna(sequence)
            print(f"Molecular Weight: {mw:.2f} g/mol")
        
        elif choice == '4':
            tm = melting_temperature(sequence)
            print(f"Melting Temperature (Tm): {tm}°C")
        
        print("-" * 60)

if __name__ == "__main__":
    main()
```

---

## Practice Exercises

### Basic Level

1. **Add Help Function**: Create a help menu explaining each operation.

2. **Format Output**: Improve number formatting (limit decimal places).

3. **Input Validation**: Add more robust error checking for all inputs.

4. **Clear Screen**: Add function to clear console between operations.

5. **Color Output**: Use colorama library to add colored output.

### Intermediate Level

6. **Save to File**: Export calculation history to text file.

7. **Load Previous Session**: Read history from file on startup.

8. **Keyboard Shortcuts**: Allow operations using symbols (+, -, *, /).

9. **Expression Parser**: Allow input like "5 + 3 * 2" and evaluate correctly.

10. **Unit Converter**: Add temperature, length, weight conversions.

### Advanced Level

11. **GUI Version**: Convert to tkinter or PyQt graphical interface.

12. **Complex Numbers**: Add support for complex number calculations.

13. **Matrix Operations**: Implement matrix addition, multiplication, determinant.

14. **Equation Solver**: Solve quadratic equations (ax² + bx + c = 0).

15. **Statistical Functions**: Add mean, median, standard deviation calculators.

---

## Key Takeaways

1. **Functions = Organization**: Each operation as a function makes code modular and testable.

2. **Error Handling**: Always validate input and handle exceptions (division by zero, invalid input).

3. **User Experience**: Clear menus, helpful messages, and formatted output improve usability.

4. **Incremental Development**: Start simple, add features progressively.

5. **Memory and History**: Enhance usability by storing results.

6. **Code Reusability**: Scientific calculator extends basic calculator by adding functions.

7. **Testing**: Test edge cases (zero, negative numbers, very large numbers).

8. **Documentation**: Docstrings explain what each function does.

---

## References

- **Python math module**: https://docs.python.org/3/library/math.html
- **Input validation**: https://realpython.com/python-input-output/
- **Exception handling**: https://docs.python.org/3/tutorial/errors.html

---

**Next Steps**: Try implementing the advanced exercises, or combine the calculator with file I/O to create a desktop application!
