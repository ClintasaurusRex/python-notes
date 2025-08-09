# Advanced Python Functions: Complete Reference Guide

This comprehensive guide covers advanced function concepts in Python, including returning multiple values, lambda functions, and recursive functions. All examples include practical applications and expected outputs.

## Table of Contents

1. [Returning Multiple Values](#returning-multiple-values)
2. [Lambda Functions](#lambda-functions)
3. [Recursive Functions](#recursive-functions)

---

## Returning Multiple Values

Functions in Python can return multiple values by separating them with commas. This creates a tuple that can be unpacked into multiple variables.

### Basic Syntax

```python
def function_name():
    value1 = "something"
    value2 = "something else"
    value3 = "another thing"
    return value1, value2, value3

# Unpack the returned tuple
var1, var2, var3 = function_name()
```

### Example 1: Student Information

```python
def get_student_info():
    name = "Bob"
    age = 20
    major = "Computer Science"
    return name, age, major

student_name, student_age, student_major = get_student_info()
print(student_name)    # Output: Bob
print(student_age)     # Output: 20
print(student_major)   # Output: Computer Science
```

### Example 2: Product Information

```python
def get_product_info():
    name = "Laptop"
    price = 999.88
    rating = 4.5
    return name, price, rating

product_name, product_price, product_rating = get_product_info()
print(product_name)    # Output: Laptop
print(product_price)   # Output: 999.88
print(product_rating)  # Output: 4.5
```

### Key Points:

- Values are returned as a tuple
- You can unpack into separate variables
- Useful for functions that need to return related data
- Makes code cleaner than using dictionaries for simple cases

---

## Lambda Functions

Lambda functions are small, anonymous functions that can have any number of arguments but only one expression. They're perfect for short, simple operations.

### Basic Syntax

```python
lambda arguments: expression
```

### Example 1: Basic Math Operations

```python
# Multiply three numbers
multiply = lambda num1, num2, num3: num1 * num2 * num3
result = multiply(2, 3, 4)
print(result)  # Output: 24

# Add two numbers
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8
```

### Example 2: Variable Arguments with \*args

```python
# Calculate average of multiple numbers
average = lambda *args: sum(args) / len(args)
result = average(10, 15, 20, 25)
print(result)  # Output: 17.5
```

### Example 3: Conditional Logic in Lambdas

```python
# Grade status based on score
grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"

# Categorize numbers
categorize_number = lambda num: "Positive" if num > 0 else "Zero" if num == 0 else "Negative"

print(categorize_number(-5))  # Output: Negative
print(categorize_number(0))   # Output: Zero
print(categorize_number(10))  # Output: Positive
```

### Example 4: Lambda with Higher-Order Functions

```python
# Sorting tuples by second element (age)
students = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

def sort_tuples(data):
    sorted_data = sorted(data, key=lambda x: x[1])
    return sorted_data

print(sort_tuples(students))
# Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```

### Common Use Cases for Lambdas:

- **Sorting**: Custom sort keys
- **Filtering**: Simple conditions
- **Mapping**: Quick transformations
- **Event handling**: GUI callbacks
- **Functional programming**: With `map()`, `filter()`, `reduce()`

### Lambda Best Practices:

- Keep them simple (one expression only)
- Use for short-lived, throwaway functions
- If the logic gets complex, use a regular function instead
- Perfect for higher-order functions like `sorted()`, `map()`, `filter()`

---

## Recursive Functions

Recursive functions are functions that call themselves. They consist of a base case (stopping condition) and a recursive case (where the function calls itself with modified parameters).

### Basic Structure

```python
def recursive_function(parameter):
    # Base case - stopping condition
    if stopping_condition:
        return base_value

    # Recursive case - function calls itself
    return recursive_function(modified_parameter)
```

### Example 1: Countdown Function

```python
def count_down(n):
    print(n)
    if n == 0:  # Base case
        return
    count_down(n - 1)  # Recursive call

count_down(3)
# Output:
# 3
# 2
# 1
# 0
```

### Example 2: Countdown with Custom Messages

```python
def print_sequence(n):
    print(f"T-minus {n}")
    if n == 1:  # Base case
        print("Blast off!")
        return
    print_sequence(n - 1)  # Recursive call

print_sequence(3)
# Output:
# T-minus 3
# T-minus 2
# T-minus 1
# Blast off!
```

### Example 3: Fibonacci Sequence

```python
def fibonacci(n):
    if n == 1:        # Base case 1
        return 0
    elif n == 2:      # Base case 2
        return 1
    else:             # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1))  # Output: 0
print(fibonacci(2))  # Output: 1
print(fibonacci(6))  # Output: 5
```

### Example 4: Sum of Digits

```python
def sum_digits(n):
    if n < 10:        # Base case - single digit
        return n
    else:             # Recursive case
        return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # Output: 10 (1 + 2 + 3 + 4)
print(sum_digits(1001))  # Output: 2 (1 + 0 + 0 + 1)
```

**How it works:**

- `n % 10` gets the last digit
- `n // 10` removes the last digit
- Keep calling until `n < 10` (single digit)

### Example 5: Sum Nested Lists

```python
def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):    # If element is a list
            total += sum_nested(element) # Recursive call
        else:                           # If element is a number
            total += element
    return total

nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(sum_nested(nested_list))  # Output: 28
```

**How it works:**

- Iterate through each element
- If element is a list, recursively sum its contents
- If element is a number, add it to total
- `isinstance(element, list)` checks if element is a list

### Recursive Function Guidelines:

1. **Always have a base case** - prevents infinite recursion
2. **Make progress toward the base case** - each call should get closer to stopping
3. **Handle edge cases** - empty lists, zero, negative numbers, etc.
4. **Consider performance** - recursion can be memory-intensive for large inputs
5. **Think about the problem structure** - recursion works well for tree-like or self-similar problems

### Common Recursive Patterns:

- **Mathematical sequences** (Fibonacci, factorials)
- **Tree traversals** (file systems, data structures)
- **Divide and conquer** (merge sort, quick sort)
- **Backtracking** (puzzles, pathfinding)
- **Nested data processing** (JSON parsing, nested lists)

---

## Summary

These advanced function concepts provide powerful tools for writing clean, efficient Python code:

- **Multiple return values** simplify functions that need to return related data
- **Lambda functions** provide concise ways to write simple functions
- **Recursive functions** elegantly solve problems that have self-similar structure

Mastering these concepts will make your Python code more expressive and help you tackle complex programming challenges with confidence.
