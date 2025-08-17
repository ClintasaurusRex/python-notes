# Higher-Order Functions in Python: Complete Reference Guide

This guide covers Python's built-in higher-order functions that take other functions as arguments or ### Example 2: Filter Words by Length (with Lambda)

````python
words = ["cat", "elephant", "dog", "hippopot### Example 2: Find Maximum (with Lambda)

```python
from functools import reduce

numbers = [3, 7, 2, 9### Example 2: Sort Tuples by Second Element (with Lambda)

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)
````

**Output:**

```
[('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

### Example 2b: Sort Tuples by Second Element (with Regular Function)

```python
def get_grade(student):
    return student[1]

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=get_grade)
print(sorted_by_grade)
```

**Output:**

````
[('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```= reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)
````

**Output:**

```
9
```

### Example 2b: Find Maximum (with Regular Function)

```python
from functools import reduce

def find_max(x, y):
    return x if x > y else y

numbers = [3, 7, 2, 9, 1]
maximum = reduce(find_max, numbers)
print(maximum)
```

**Output:**

````
9
```ong_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)
````

**Output:**

```
['elephant', 'hippopotamus']
```

### Example 2b: Filter Words by Length (with Regular Function)

```python
def is_long_word(word):
    return len(word) > 3

words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
long_words = list(filter(is_long_word, words))
print(long_words)
```

**Output:**

````
['elephant', 'hippopotamus']
```ons as results. These functions enable functional programming patterns and help write more concise, readable code.

## Table of Contents

1. [Quick Reference Guide](#quick-reference-guide)
2. [map()](#map)
3. [filter()](#filter)
4. [reduce()](#reduce)
5. [sorted()](#sorted)
6. [zip()](#zip)
7. [enumerate()](#enumerate)
8. [any() and all()](#any-and-all)

---

## Quick Reference Guide

| Function                     | Description                                             | Returns                           |
| ---------------------------- | ------------------------------------------------------- | --------------------------------- |
| `map(func, iterable)`        | Applies function to every item in iterable              | Iterator of results               |
| `filter(func, iterable)`     | Filters items based on function returning True/False    | Iterator of filtered items        |
| `reduce(func, iterable)`     | Applies function cumulatively to reduce to single value | Single accumulated value          |
| `sorted(iterable, key=func)` | Returns sorted list using optional key function         | New sorted list                   |
| `zip(*iterables)`            | Combines multiple iterables element-wise                | Iterator of tuples                |
| `enumerate(iterable)`        | Returns index-value pairs                               | Iterator of (index, value) tuples |
| `any(iterable)`              | Returns True if any element is truthy                   | Boolean                           |
| `all(iterable)`              | Returns True if all elements are truthy                 | Boolean                           |

---

## map()

The `map()` function applies a given function to every item in an iterable and returns a map object (iterator).

### Syntax

```python
map(function, iterable)
````

### Example 1: Square Numbers (with Lambda)

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
```

**Output:**

```
[1, 4, 9, 16, 25]
```

### Example 1b: Square Numbers (with Regular Function)

```python
def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)
```

**Output:**

```
[1, 4, 9, 16, 25]
```

### Example 2: Convert to Uppercase

```python
words = ["hello", "world", "python"]
uppercase = list(map(str.upper, words))
print(uppercase)
```

**Output:**

```
['HELLO', 'WORLD', 'PYTHON']
```

### Example 3: Multiple Iterables (with Lambda)

```python
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, numbers1, numbers2))
print(result)
```

**Output:**

```
[5, 7, 9]
```

### Example 3b: Multiple Iterables (with Regular Function)

```python
def add_numbers(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = list(map(add_numbers, numbers1, numbers2))
print(result)
```

**Output:**

```
[5, 7, 9]
```

---

## filter()

The `filter()` function creates an iterator from elements of an iterable for which a function returns True.

### Syntax

```python
filter(function, iterable)
```

### Example 1: Filter Even Numbers (with Lambda)

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
```

**Output:**

```
[2, 4, 6, 8, 10]
```

### Example 1b: Filter Even Numbers (with Regular Function)

```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(is_even, numbers))
print(evens)
```

**Output:**

```
[2, 4, 6, 8, 10]
```

### Example 2: Filter Words by Length (with Lambda)

```python
words = ["cat", "elephant", "dog", "hippopotamus", "ant"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)
```

**Output:**

```
['elephant', 'hippopotamus']
```

### Example 3: Filter None Values

```python
mixed_list = [1, None, 3, "", 5, 0, 7]
filtered = list(filter(None, mixed_list))
print(filtered)
```

**Output:**

```
[1, 3, 5, 7]
```

---

## reduce()

The `reduce()` function applies a function cumulatively to the items in an iterable to reduce it to a single value.

**Note:** `reduce()` must be imported from the `functools` module.

### Syntax

```python
from functools import reduce
reduce(function, iterable[, initializer])
```

### Example 1: Sum All Numbers (with Lambda)

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
```

**Output:**

```
15
```

### Example 1b: Sum All Numbers (with Regular Function)

```python
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
total = reduce(add, numbers)
print(total)
```

**Output:**

```
15
```

### Example 2: Find Maximum (with Lambda)

```python
from functools import reduce

numbers = [3, 7, 2, 9, 1]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)
```

**Output:**

```
9
```

### Example 3: Concatenate Strings

```python
from functools import reduce

words = ["Python", "is", "awesome"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)
```

**Output:**

```
Python is awesome
```

---

## sorted()

The `sorted()` function returns a new sorted list from an iterable, with an optional key function for custom sorting.

### Syntax

```python
sorted(iterable, key=function, reverse=False)
```

### Example 1: Sort by Length (with Built-in Function)

```python
words = ["python", "java", "c", "javascript"]
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)
```

**Output:**

```
['c', 'java', 'python', 'javascript']
```

### Example 1b: Sort by Length (with Lambda)

```python
words = ["python", "java", "c", "javascript"]
sorted_by_length = sorted(words, key=lambda word: len(word))
print(sorted_by_length)
```

**Output:**

```
['c', 'java', 'python', 'javascript']
```

### Example 2: Sort Tuples by Second Element (with Lambda)

```python
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)
```

**Output:**

```
[('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

### Example 3: Sort in Reverse Order

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_desc = sorted(numbers, reverse=True)
print(sorted_desc)
```

**Output:**

```
[9, 6, 5, 4, 3, 2, 1, 1]
```

---

## zip()

The `zip()` function combines multiple iterables element-wise, creating tuples of corresponding elements.

### Syntax

```python
zip(*iterables)
```

### Example 1: Combine Two Lists

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(combined)
```

**Output:**

```
[('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### Example 2: Transpose a Matrix

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = list(zip(*matrix))
print(transposed)
```

**Output:**

```
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

### Example 3: Create Dictionary from Two Lists

```python
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = dict(zip(keys, values))
print(person)
```

**Output:**

```
{'name': 'Alice', 'age': 25, 'city': 'New York'}
```

---

## enumerate()

The `enumerate()` function returns an iterator of tuples containing indices and values from an iterable.

### Syntax

```python
enumerate(iterable, start=0)
```

### Example 1: Basic Enumeration

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**

```
0: apple
1: banana
2: cherry
```

### Example 2: Start from Different Index

```python
colors = ["red", "green", "blue"]
enumerated = list(enumerate(colors, start=1))
print(enumerated)
```

**Output:**

```
[(1, 'red'), (2, 'green'), (3, 'blue')]
```

### Example 3: Find Index of Item

```python
numbers = [10, 20, 30, 40, 50]
target = 30
for index, value in enumerate(numbers):
    if value == target:
        print(f"Found {target} at index {index}")
        break
```

**Output:**

```
Found 30 at index 2
```

---

## any() and all()

These functions test the truthiness of elements in an iterable.

### any()

Returns `True` if any element in the iterable is truthy.

### all()

Returns `True` if all elements in the iterable are truthy.

### Syntax

```python
any(iterable)
all(iterable)
```

### Example 1: Basic Usage

```python
numbers = [0, 1, 2, 3]
print(any(numbers))  # True (1, 2, 3 are truthy)
print(all(numbers))  # False (0 is falsy)
```

**Output:**

```
True
False
```

### Example 2: Check Conditions

```python
grades = [85, 92, 78, 96, 88]

# Check if any grade is above 90
has_excellent = any(grade > 90 for grade in grades)
print(f"Any excellent grades: {has_excellent}")

# Check if all grades are passing (>= 70)
all_passing = all(grade >= 70 for grade in grades)
print(f"All passing: {all_passing}")
```

**Output:**

```
Any excellent grades: True
All passing: True
```

### Example 3: Validate Data

```python
usernames = ["alice", "bob", "charlie"]

# Check if any username is empty
has_empty = any(len(name) == 0 for name in usernames)
print(f"Has empty username: {has_empty}")

# Check if all usernames are valid (length > 2)
all_valid = all(len(name) > 2 for name in usernames)
print(f"All valid usernames: {all_valid}")
```

**Output:**

```
Has empty username: False
All valid usernames: True
```

---

## Summary

Higher-order functions in Python provide powerful tools for functional programming:

- **`map()`**: Transform every element in an iterable
- **`filter()`**: Select elements based on conditions
- **`reduce()`**: Combine elements into a single value
- **`sorted()`**: Create sorted versions with custom criteria
- **`zip()`**: Combine multiple iterables
- **`enumerate()`**: Add indices to iterables
- **`any()`/`all()`**: Test conditions across iterables

These functions often work well with lambda expressions and can make your code more concise and readable when used appropriately.
