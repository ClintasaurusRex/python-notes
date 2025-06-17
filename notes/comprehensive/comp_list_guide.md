# Comprehensive Python Lists Guide

## Table of Contents

1. [Introduction to Lists](#introduction-to-lists) - What are lists and why use them
2. [Creating Lists](#creating-lists) - Different ways to create lists
3. [Accessing List Elements](#accessing-list-elements) - Indexing and retrieving data
4. [Modifying Lists](#modifying-lists) - Changing list contents
5. [List Slicing](#list-slicing) - Working with portions of lists
6. [Built-in List Methods](#built-in-list-methods) - All 11 essential list methods
7. [Built-in Functions for Lists](#built-in-functions-for-lists) - Python functions that work with lists
8. [List Comprehensions](#list-comprehensions) - Creating lists efficiently
9. [Nested Lists](#nested-lists) - Lists within lists
10. [Common List Patterns](#common-list-patterns) - Frequent use cases
11. [Performance Considerations](#performance-considerations) - Optimization tips
12. [Real-World Examples](#real-world-examples) - Practical applications
13. [Best Practices](#best-practices) - Writing clean list code
14. [Common Pitfalls](#common-pitfalls) - What to avoid

---

## Introduction to Lists

Lists are one of the most fundamental and versatile data structures in Python. They are **ordered collections** that can store multiple items of any data type.

### Key Characteristics:
- **Ordered**: Items have a defined order and maintain that order
- **Mutable**: You can change, add, or remove items after creation
- **Allow duplicates**: The same value can appear multiple times
- **Mixed data types**: Can store integers, strings, floats, other lists, etc.

### When to Use Lists:
- Storing multiple related items (shopping cart, student names, scores)
- When order matters (steps in a process, rankings)
- When you need to modify the collection frequently
- For sequences that might grow or shrink during program execution

```python
# Example: Why lists are useful
shopping_cart = ["apples", "bread", "milk", "eggs"]
scores = [85, 92, 78, 96, 88]
mixed_data = ["John", 25, 5.9, True, [1, 2, 3]]

print(f"Shopping cart has {len(shopping_cart)} items")
print(f"Average score: {sum(scores) / len(scores)}")
```

---

## Creating Lists

### 1. Empty Lists
```python
# Method 1: Using square brackets
empty_list1 = []

# Method 2: Using list() constructor
empty_list2 = list()

print(empty_list1)  # Output: []
print(empty_list2)  # Output: []
```

### 2. Lists with Initial Values
```python
# Numbers
numbers = [1, 2, 3, 4, 5]

# Strings
fruits = ["apple", "banana", "orange"]

# Mixed data types
mixed = ["Alice", 25, 3.14, True]

# Using repetition
zeros = [0] * 5  # [0, 0, 0, 0, 0]
repeated = ["hello"] * 3  # ["hello", "hello", "hello"]

print(numbers)   # Output: [1, 2, 3, 4, 5]
print(fruits)    # Output: ['apple', 'banana', 'orange']
print(mixed)     # Output: ['Alice', 25, 3.14, True]
print(zeros)     # Output: [0, 0, 0, 0, 0]
```

### 3. Creating Lists from Other Iterables
```python
# From strings
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# From range
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
evens = list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]

# From tuples
tuple_data = (1, 2, 3)
list_data = list(tuple_data)  # [1, 2, 3]

print(letters)    # Output: ['h', 'e', 'l', 'l', 'o']
print(numbers)    # Output: [1, 2, 3, 4, 5]
print(evens)      # Output: [0, 2, 4, 6, 8, 10]
```

---

## Accessing List Elements

### 1. Positive Indexing (0-based)
```python
fruits = ["apple", "banana", "cherry", "date"]

first_fruit = fruits[0]    # "apple"
second_fruit = fruits[1]   # "banana"
last_fruit = fruits[3]     # "date"

print(f"First: {first_fruit}")   # Output: First: apple
print(f"Second: {second_fruit}") # Output: Second: banana
print(f"Last: {last_fruit}")     # Output: Last: date
```

### 2. Negative Indexing (from the end)
```python
fruits = ["apple", "banana", "cherry", "date"]

last_fruit = fruits[-1]      # "date"
second_last = fruits[-2]     # "cherry"
first_fruit = fruits[-4]     # "apple"

print(f"Last: {last_fruit}")       # Output: Last: date
print(f"Second last: {second_last}") # Output: Second last: cherry
print(f"First: {first_fruit}")     # Output: First: apple
```

### 3. Checking if Item Exists
```python
fruits = ["apple", "banana", "cherry"]

# Using 'in' operator
if "apple" in fruits:
    print("Apple is in the list")  # Output: Apple is in the list

if "grape" not in fruits:
    print("Grape is not in the list")  # Output: Grape is not in the list

# Getting index of item
apple_index = fruits.index("apple")
print(f"Apple is at index: {apple_index}")  # Output: Apple is at index: 0
```

---

## Modifying Lists

### 1. Changing Individual Elements
```python
fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")  # Output: Original: ['apple', 'banana', 'cherry']

# Change single element
fruits[1] = "blueberry"
print(f"After change: {fruits}")  # Output: After change: ['apple', 'blueberry', 'cherry']

# Change multiple elements using slicing
fruits[0:2] = ["orange", "grape"]
print(f"After multiple changes: {fruits}")  # Output: After multiple changes: ['orange', 'grape', 'cherry']
```

### 2. Adding Elements
```python
numbers = [1, 2, 3]

# Add single element at the end
numbers.append(4)
print(f"After append: {numbers}")  # Output: After append: [1, 2, 3, 4]

# Add multiple elements at the end
numbers.extend([5, 6, 7])
print(f"After extend: {numbers}")  # Output: After extend: [1, 2, 3, 4, 5, 6, 7]

# Insert at specific position
numbers.insert(0, 0)  # Insert 0 at index 0
print(f"After insert: {numbers}")  # Output: After insert: [0, 1, 2, 3, 4, 5, 6, 7]
```

### 3. Removing Elements
```python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# Remove first occurrence of specific value
fruits.remove("banana")
print(f"After remove: {fruits}")  # Output: After remove: ['apple', 'cherry', 'banana', 'date']

# Remove and return element at specific index
removed_item = fruits.pop(1)  # Remove item at index 1
print(f"Removed: {removed_item}")  # Output: Removed: cherry
print(f"After pop: {fruits}")      # Output: After pop: ['apple', 'banana', 'date']

# Remove last element
last_item = fruits.pop()
print(f"Last removed: {last_item}")  # Output: Last removed: date
print(f"Final list: {fruits}")       # Output: Final list: ['apple', 'banana']
```

---

## List Slicing

Slicing allows you to extract portions of a list using the syntax `list[start:end:step]`.

### 1. Basic Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive)
slice1 = numbers[2:6]    # [2, 3, 4, 5]

# Get elements from start to index 4 (exclusive)
slice2 = numbers[:4]     # [0, 1, 2, 3]

# Get elements from index 6 to end
slice3 = numbers[6:]     # [6, 7, 8, 9]

# Get all elements (copy of list)
slice4 = numbers[:]      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Slice [2:6]: {slice1}")
print(f"Slice [:4]: {slice2}")
print(f"Slice [6:]: {slice3}")
print(f"Slice [:]: {slice4}")
```

### 2. Slicing with Step
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Every second element
evens = numbers[::2]     # [0, 2, 4, 6, 8]

# Every second element starting from index 1
odds = numbers[1::2]     # [1, 3, 5, 7, 9]

# Every third element from index 1 to 8
slice_step = numbers[1:8:3]  # [1, 4, 7]

# Reverse the list
reversed_list = numbers[::-1]  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f"Evens: {evens}")
print(f"Odds: {odds}")
print(f"Step 3: {slice_step}")
print(f"Reversed: {reversed_list}")
```

### 3. Negative Indices in Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Last 3 elements
last_three = numbers[-3:]    # [7, 8, 9]

# All except last 2 elements
except_last_two = numbers[:-2]  # [0, 1, 2, 3, 4, 5, 6, 7]

# From third-to-last to second-to-last
middle = numbers[-3:-1]      # [7, 8]

print(f"Last three: {last_three}")
print(f"Except last two: {except_last_two}")
print(f"Middle: {middle}")
```

---

## Built-in List Methods

### 1. `append(item)` - Add single item to end
```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Can append any data type
numbers = [1, 2, 3]
numbers.append([4, 5])  # Adds the entire list as one element
print(numbers)  # Output: [1, 2, 3, [4, 5]]
```

### 2. `extend(iterable)` - Add all items from iterable to end
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

# Can extend with any iterable
fruits = ["apple"]
fruits.extend("hello")  # Extends with each character
print(fruits)  # Output: ['apple', 'h', 'e', 'l', 'l', 'o']
```

### 3. `insert(index, item)` - Insert item at specific position
```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # Insert at index 1
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Insert at beginning
numbers = [2, 3, 4]
numbers.insert(0, 1)
print(numbers)  # Output: [1, 2, 3, 4]

# Insert beyond list length (appends to end)
numbers.insert(100, 5)
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

### 4. `remove(item)` - Remove first occurrence of item
```python
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")  # Removes first occurrence
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# Raises ValueError if item not found
try:
    fruits.remove("grape")
except ValueError:
    print("Grape not found in list")
```

### 5. `pop(index)` - Remove and return item at index (default: last item)
```python
fruits = ["apple", "banana", "cherry"]

# Remove last item
last_fruit = fruits.pop()
print(f"Removed: {last_fruit}")  # Output: Removed: cherry
print(f"List: {fruits}")         # Output: List: ['apple', 'banana']

# Remove item at specific index
first_fruit = fruits.pop(0)
print(f"Removed: {first_fruit}")  # Output: Removed: apple
print(f"List: {fruits}")          # Output: List: ['banana']
```

### 6. `clear()` - Remove all items from list
```python
fruits = ["apple", "banana", "cherry"]
print(f"Before clear: {fruits}")  # Output: Before clear: ['apple', 'banana', 'cherry']

fruits.clear()
print(f"After clear: {fruits}")   # Output: After clear: []
```

### 7. `index(item, start, end)` - Return index of first occurrence
```python
fruits = ["apple", "banana", "cherry", "banana"]

# Find index of first occurrence
banana_index = fruits.index("banana")
print(f"First banana at index: {banana_index}")  # Output: First banana at index: 1

# Find index within a range
second_banana = fruits.index("banana", 2)  # Start searching from index 2
print(f"Second banana at index: {second_banana}")  # Output: Second banana at index: 3

# Raises ValueError if not found
try:
    grape_index = fruits.index("grape")
except ValueError:
    print("Grape not found")
```

### 8. `count(item)` - Return number of occurrences
```python
numbers = [1, 2, 3, 2, 2, 4, 5, 2]

count_of_2 = numbers.count(2)
print(f"Number 2 appears {count_of_2} times")  # Output: Number 2 appears 4 times

count_of_6 = numbers.count(6)
print(f"Number 6 appears {count_of_6} times")  # Output: Number 6 appears 0 times

# Works with any data type
fruits = ["apple", "banana", "apple", "cherry"]
apple_count = fruits.count("apple")
print(f"Apple appears {apple_count} times")    # Output: Apple appears 2 times
```

### 9. `sort(key=None, reverse=False)` - Sort list in place
```python
# Sort numbers
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(f"Sorted numbers: {numbers}")  # Output: Sorted numbers: [1, 1, 2, 3, 4, 5, 9]

# Sort in descending order
numbers.sort(reverse=True)
print(f"Descending: {numbers}")      # Output: Descending: [9, 5, 4, 3, 2, 1, 1]

# Sort strings
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(f"Sorted fruits: {fruits}")    # Output: Sorted fruits: ['apple', 'banana', 'cherry']

# Sort by custom criteria (length of string)
words = ["python", "java", "c", "javascript"]
words.sort(key=len)
print(f"Sorted by length: {words}")  # Output: Sorted by length: ['c', 'java', 'python', 'javascript']

# Sort case-insensitive
names = ["Alice", "bob", "Charlie"]
names.sort(key=str.lower)
print(f"Case-insensitive: {names}")  # Output: Case-insensitive: ['Alice', 'bob', 'Charlie']
```

### 10. `reverse()` - Reverse list in place
```python
numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")  # Output: Original: [1, 2, 3, 4, 5]

numbers.reverse()
print(f"Reversed: {numbers}")  # Output: Reversed: [5, 4, 3, 2, 1]

# Works with any data type
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(f"Reversed fruits: {fruits}")  # Output: Reversed fruits: ['cherry', 'banana', 'apple']
```

### 11. `copy()` - Return shallow copy of list
```python
original = [1, 2, 3, [4, 5]]
copied = original.copy()

print(f"Original: {original}")  # Output: Original: [1, 2, 3, [4, 5]]
print(f"Copied: {copied}")      # Output: Copied: [1, 2, 3, [4, 5]]

# Modifying copied list doesn't affect original (for immutable elements)
copied[0] = 99
print(f"Original after modification: {original}")  # Output: Original after modification: [1, 2, 3, [4, 5]]
print(f"Copied after modification: {copied}")      # Output: Copied after modification: [99, 2, 3, [4, 5]]

# But nested mutable objects are still referenced
copied[3].append(6)
print(f"Original nested list: {original}")  # Output: Original nested list: [1, 2, 3, [4, 5, 6]]
print(f"Copied nested list: {copied}")      # Output: Copied nested list: [99, 2, 3, [4, 5, 6]]
```

---

## Built-in Functions for Lists

### 1. `len(list)` - Get number of items
```python
fruits = ["apple", "banana", "cherry"]
count = len(fruits)
print(f"Number of fruits: {count}")  # Output: Number of fruits: 3

empty_list = []
print(f"Empty list length: {len(empty_list)}")  # Output: Empty list length: 0
```

### 2. `max(list)` and `min(list)` - Get maximum/minimum values
```python
numbers = [3, 7, 2, 9, 1, 5]
maximum = max(numbers)
minimum = min(numbers)
print(f"Max: {maximum}, Min: {minimum}")  # Output: Max: 9, Min: 1

# Works with strings (alphabetical order)
fruits = ["apple", "banana", "cherry"]
print(f"Max fruit: {max(fruits)}")  # Output: Max fruit: cherry
print(f"Min fruit: {min(fruits)}")  # Output: Min fruit: apple

# Custom key function
words = ["python", "java", "c"]
longest = max(words, key=len)
shortest = min(words, key=len)
print(f"Longest: {longest}, Shortest: {shortest}")  # Output: Longest: python, Shortest: c
```

### 3. `sum(list)` - Get sum of numeric values
```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum: {total}")  # Output: Sum: 15

# With start value
total_with_start = sum(numbers, 10)  # Start with 10
print(f"Sum with start: {total_with_start}")  # Output: Sum with start: 25

# Calculate average
average = sum(numbers) / len(numbers)
print(f"Average: {average}")  # Output: Average: 3.0
```

### 4. `sorted(list)` - Return new sorted list (doesn't modify original)
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
sorted_numbers = sorted(numbers)
print(f"Original: {numbers}")        # Output: Original: [3, 1, 4, 1, 5, 9, 2]
print(f"Sorted: {sorted_numbers}")   # Output: Sorted: [1, 1, 2, 3, 4, 5, 9]

# Reverse order
descending = sorted(numbers, reverse=True)
print(f"Descending: {descending}")   # Output: Descending: [9, 5, 4, 3, 2, 1, 1]

# Custom sorting
words = ["python", "java", "c", "javascript"]
by_length = sorted(words, key=len)
print(f"By length: {by_length}")     # Output: By length: ['c', 'java', 'python', 'javascript']
```

### 5. `reversed(list)` - Return reverse iterator
```python
numbers = [1, 2, 3, 4, 5]
reversed_iter = reversed(numbers)
reversed_list = list(reversed_iter)

print(f"Original: {numbers}")        # Output: Original: [1, 2, 3, 4, 5]
print(f"Reversed: {reversed_list}")  # Output: Reversed: [5, 4, 3, 2, 1]

# Use in for loop
print("Reversed iteration:")
for num in reversed(numbers):
    print(num, end=" ")  # Output: 5 4 3 2 1
print()  # New line
```

### 6. `enumerate(list)` - Get index and value pairs
```python
fruits = ["apple", "banana", "cherry"]

# Basic enumeration
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Start from different number
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output:
# 1: apple
# 2: banana
# 3: cherry

# Create list of tuples
indexed_fruits = list(enumerate(fruits))
print(indexed_fruits)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
```

### 7. `zip(list1, list2, ...)` - Combine multiple lists
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

# Zip two lists
name_age_pairs = list(zip(names, ages))
print(name_age_pairs)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Zip three lists
full_info = list(zip(names, ages, cities))
print(full_info)  # Output: [('Alice', 25, 'New York'), ('Bob', 30, 'London'), ('Charlie', 35, 'Tokyo')]

# Use in for loop
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Output:
# Alice is 25 years old and lives in New York
# Bob is 30 years old and lives in London
# Charlie is 35 years old and lives in Tokyo
```

### 8. `any(list)` and `all(list)` - Boolean operations
```python
# any() - Returns True if any element is True
bool_list1 = [False, False, True, False]
bool_list2 = [False, False, False]
print(f"Any True in list1: {any(bool_list1)}")  # Output: Any True in list1: True
print(f"Any True in list2: {any(bool_list2)}")  # Output: Any True in list2: False

# all() - Returns True if all elements are True
bool_list3 = [True, True, True]
bool_list4 = [True, False, True]
print(f"All True in list3: {all(bool_list3)}")  # Output: All True in list3: True
print(f"All True in list4: {all(bool_list4)}")  # Output: All True in list4: False

# Practical examples
numbers = [2, 4, 6, 8, 10]
all_even = all(num % 2 == 0 for num in numbers)
print(f"All numbers are even: {all_even}")  # Output: All numbers are even: True

scores = [85, 92, 78, 96, 88]
any_failing = any(score < 60 for score in scores)
print(f"Any failing scores: {any_failing}")  # Output: Any failing scores: False
```

---

## List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists or other iterables.

### 1. Basic List Comprehensions
```python
# Traditional approach
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(f"Traditional: {squares}")  # Output: Traditional: [1, 4, 9, 16, 25]

# List comprehension approach
squares_comp = [x ** 2 for x in range(1, 6)]
print(f"Comprehension: {squares_comp}")  # Output: Comprehension: [1, 4, 9, 16, 25]

# From existing list
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")  # Output: Doubled: [2, 4, 6, 8, 10]
```

### 2. List Comprehensions with Conditions
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")  # Output: Evens: [2, 4, 6, 8, 10]

# Square only odd numbers
odd_squares = [x ** 2 for x in numbers if x % 2 == 1]
print(f"Odd squares: {odd_squares}")  # Output: Odd squares: [1, 9, 25, 49, 81]

# Filter and transform strings
words = ["apple", "banana", "cherry", "date"]
long_words_upper = [word.upper() for word in words if len(word) > 5]
print(f"Long words: {long_words_upper}")  # Output: Long words: ['BANANA', 'CHERRY']
```

### 3. Complex List Comprehensions
```python
# Nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened: {flattened}")  # Output: Flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Conditional expressions (ternary operator)
numbers = [1, 2, 3, 4, 5]
labels = ["odd" if x % 2 == 1 else "even" for x in numbers]
print(f"Labels: {labels}")  # Output: Labels: ['odd', 'even', 'odd', 'even', 'odd']

# Multiple conditions
numbers = range(1, 21)
special = [x for x in numbers if x % 2 == 0 if x % 3 == 0]
print(f"Even and divisible by 3: {special}")  # Output: Even and divisible by 3: [6, 12, 18]
```

### 4. List Comprehensions with Functions
```python
# Using built-in functions
words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")  # Output: Lengths: [5, 5, 6]

# Using custom functions
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 21)
primes = [x for x in numbers if is_prime(x)]
print(f"Primes: {primes}")  # Output: Primes: [2, 3, 5, 7, 11, 13, 17, 19]
```

---

## Nested Lists

Lists can contain other lists, creating multi-dimensional structures.

### 1. Creating Nested Lists
```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# List of lists with different lengths
irregular = [
    [1, 2],
    [3, 4, 5, 6],
    [7]
]

# Mixed nested structure
mixed = [
    "hello",
    [1, 2, 3],
    ["a", "b"],
    [[1, 2], [3, 4]]
]

print(f"Matrix: {matrix}")
print(f"Irregular: {irregular}")
print(f"Mixed: {mixed}")
```

### 2. Accessing Nested Lists
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access row
first_row = matrix[0]  # [1, 2, 3]
print(f"First row: {first_row}")

# Access specific element
element = matrix[1][2]  # Row 1, Column 2 = 6
print(f"Element [1][2]: {element}")

# Access with variables
row, col = 2, 1
element = matrix[row][col]  # 8
print(f"Element [{row}][{col}]: {element}")
```

### 3. Modifying Nested Lists
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Original: {matrix}")

# Modify single element
matrix[0][0] = 99
print(f"After modification: {matrix}")

# Modify entire row
matrix[1] = [40, 50, 60]
print(f"After row change: {matrix}")

# Add new row
matrix.append([10, 11, 12])
print(f"After adding row: {matrix}")
```

### 4. Iterating Through Nested Lists
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate through rows
print("Row by row:")
for row in matrix:
    print(row)

# Iterate through all elements
print("\nAll elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
print()

# Using enumerate for indices
print("\nWith indices:")
for i, row in enumerate(matrix):
    for j, element in enumerate(row):
        print(f"[{i}][{j}] = {element}")
```

### 5. Common Operations with Nested Lists
```python
# Create 3x3 matrix filled with zeros
rows, cols = 3, 3
zeros_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print(f"Zeros matrix: {zeros_matrix}")

# Transpose matrix (swap rows and columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transposed = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print(f"Original: {matrix}")
print(f"Transposed: {transposed}")

# Sum all elements
total = sum(sum(row) for row in matrix)
print(f"Sum of all elements: {total}")

# Find maximum element
max_element = max(max(row) for row in matrix)
print(f"Maximum element: {max_element}")
```

---

## Common List Patterns

### 1. Finding Elements
```python
# Find all indices of an element
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

numbers = [1, 2, 3, 2, 4, 2, 5]
indices = find_all_indices(numbers, 2)
print(f"All indices of 2: {indices}")  # Output: All indices of 2: [1, 3, 5]

# Find element with condition
def find_first_greater_than(lst, threshold):
    for i, x in enumerate(lst):
        if x > threshold:
            return i, x
    return None

result = find_first_greater_than([1, 3, 2, 7, 5], 4)
print(f"First element > 4: {result}")  # Output: First element > 4: (3, 7)
```

### 2. Filtering and Transforming
```python
# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 1, 4, 3, 5]
unique = remove_duplicates(numbers)
print(f"Unique elements: {unique}")  # Output: Unique elements: [1, 2, 3, 4, 5]

# Filter by multiple criteria
def filter_strings(strings, min_length=3, must_contain="a"):
    return [s for s in strings if len(s) >= min_length and must_contain in s]

words = ["cat", "dog", "apple", "banana", "at", "car"]
filtered = filter_strings(words)
print(f"Filtered words: {filtered}")  # Output: Filtered words: ['cat', 'apple', 'banana', 'car']
```

### 3. Grouping and Partitioning
```python
# Group by property
def group_by_length(strings):
    groups = {}
    for string in strings:
        length = len(string)
        if length not in groups:
            groups[length] = []
        groups[length].append(string)
    return groups

words = ["cat", "dog", "apple", "banana", "at", "car"]
grouped = group_by_length(words)
print(f"Grouped by length: {grouped}")
# Output: Grouped by length: {3: ['cat', 'dog', 'car'], 5: ['apple'], 6: ['banana'], 2: ['at']}

# Partition into two lists
def partition(lst, condition):
    true_list = []
    false_list = []
    for item in lst:
        if condition(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = partition(numbers, lambda x: x % 2 == 0)
print(f"Evens: {evens}")  # Output: Evens: [2, 4, 6, 8, 10]
print(f"Odds: {odds}")    # Output: Odds: [1, 3, 5, 7, 9]
```

### 4. Mathematical Operations
```python
# Calculate running sum
def running_sum(numbers):
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)
    return result

numbers = [1, 2, 3, 4, 5]
cumulative = running_sum(numbers)
print(f"Running sum: {cumulative}")  # Output: Running sum: [1, 3, 6, 10, 15]

# Moving average
def moving_average(numbers, window_size):
    if len(numbers) < window_size:
        return []
    result = []
    for i in range(len(numbers) - window_size + 1):
        window = numbers[i:i + window_size]
        avg = sum(window) / window_size
        result.append(avg)
    return result

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
averages = moving_average(data, 3)
print(f"Moving averages (window=3): {averages}")
# Output: Moving averages (window=3): [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
```

---

## Performance Considerations

### 1. List vs Other Data Structures
```python
import time

# List operations timing
def time_list_operations():
    # Append operations
    lst = []
    start_time = time.time()
    for i in range(100000):
        lst.append(i)
    append_time = time.time() - start_time
    print(f"Append 100k items: {append_time:.4f} seconds")
    
    # Search operations
    start_time = time.time()
    99999 in lst
    search_time = time.time() - start_time
    print(f"Search in 100k items: {search_time:.4f} seconds")

time_list_operations()
```

### 2. Efficient List Operations
```python
# Efficient: List comprehension
numbers = range(1000000)
squares_comp = [x ** 2 for x in numbers]

# Less efficient: Loop with append
squares_loop = []
for x in numbers:
    squares_loop.append(x ** 2)

# Efficient: Using extend for multiple items
result = []
data_chunks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for chunk in data_chunks:
    result.extend(chunk)  # Better than multiple appends

# Efficient: Pre-allocate when size is known
size = 1000
pre_allocated = [0] * size  # Better than growing list item by item
```

### 3. Memory Considerations
```python
# Memory-efficient: Generator vs List
def squares_generator(n):
    for i in range(n):
        yield i ** 2

def squares_list(n):
    return [i ** 2 for i in range(n)]

# Generator uses memory as needed
gen = squares_generator(1000000)  # Very little memory used initially

# List creates all items immediately
lst = squares_list(1000000)  # All items in memory immediately

# Use generators for large datasets when you don't need all items at once
```

---

## Real-World Examples

### 1. Student Grade Management
```python
class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grades):
        self.students.append({
            'name': name,
            'grades': grades,
            'average': sum(grades) / len(grades) if grades else 0
        })
    
    def get_top_students(self, n=3):
        sorted_students = sorted(self.students, key=lambda x: x['average'], reverse=True)
        return sorted_students[:n]
    
    def get_failing_students(self, threshold=60):
        return [student for student in self.students if student['average'] < threshold]
    
    def class_statistics(self):
        all_grades = []
        for student in self.students:
            all_grades.extend(student['grades'])
        
        return {
            'class_average': sum(all_grades) / len(all_grades) if all_grades else 0,
            'highest_grade': max(all_grades) if all_grades else 0,
            'lowest_grade': min(all_grades) if all_grades else 0,
            'total_students': len(self.students)
        }

# Usage example
gm = GradeManager()
gm.add_student("Alice", [85, 92, 78, 96])
gm.add_student("Bob", [76, 82, 88, 79])
gm.add_student("Charlie", [45, 52, 48, 58])

print("Top students:", gm.get_top_students(2))
print("Failing students:", gm.get_failing_students())
print("Class stats:", gm.class_statistics())
```

### 2. Shopping Cart System
```python
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        # Check if item already exists
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                return
        
        # Add new item
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item['name'] != name]
    
    def update_quantity(self, name, new_quantity):
        for item in self.items:
            if item['name'] == name:
                if new_quantity <= 0:
                    self.remove_item(name)
                else:
                    item['quantity'] = new_quantity
                break
    
    def get_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)
    
    def get_item_count(self):
        return sum(item['quantity'] for item in self.items)
    
    def apply_discount(self, discount_percent):
        for item in self.items:
            item['price'] *= (1 - discount_percent / 100)
    
    def get_receipt(self):
        receipt = "Shopping Cart Receipt\n"
        receipt += "-" * 30 + "\n"
        
        for item in self.items:
            line_total = item['price'] * item['quantity']
            receipt += f"{item['name']:<15} x{item['quantity']:<3} ${line_total:>8.2f}\n"
        
        receipt += "-" * 30 + "\n"
        receipt += f"Total: ${self.get_total():.2f}\n"
        receipt += f"Items: {self.get_item_count()}\n"
        
        return receipt

# Usage example
cart = ShoppingCart()
cart.add_item("Apple", 1.50, 3)
cart.add_item("Bread", 2.99, 1)
cart.add_item("Milk", 3.49, 2)
cart.add_item("Apple", 1.50, 2)  # This will increase quantity

print(cart.get_receipt())
cart.apply_discount(10)  # 10% discount
print("\nAfter 10% discount:")
print(cart.get_receipt())
```

### 3. Data Analysis Example
```python
def analyze_sales_data(sales_data):
    """
    Analyze monthly sales data
    sales_data: list of dictionaries with 'month', 'sales', 'region'
    """
    
    # Total sales
    total_sales = sum(sale['sales'] for sale in sales_data)
    
    # Average monthly sales
    avg_monthly = total_sales / len(sales_data) if sales_data else 0
    
    # Best and worst months
    best_month = max(sales_data, key=lambda x: x['sales']) if sales_data else None
    worst_month = min(sales_data, key=lambda x: x['sales']) if sales_data else None
    
    # Sales by region
    regions = {}
    for sale in sales_data:
        region = sale['region']
        if region not in regions:
            regions[region] = []
        regions[region].append(sale['sales'])
    
    region_totals = {region: sum(sales) for region, sales in regions.items()}
    
    # Growth analysis (comparing consecutive months)
    growth_rates = []
    sorted_data = sorted(sales_data, key=lambda x: x['month'])
    
    for i in range(1, len(sorted_data)):
        prev_sales = sorted_data[i-1]['sales']
        curr_sales = sorted_data[i]['sales']
        growth_rate = ((curr_sales - prev_sales) / prev_sales) * 100 if prev_sales > 0 else 0
        growth_rates.append({
            'month': sorted_data[i]['month'],
            'growth_rate': growth_rate
        })
    
    return {
        'total_sales': total_sales,
        'average_monthly': avg_monthly,
        'best_month': best_month,
        'worst_month': worst_month,
        'region_totals': region_totals,
        'growth_rates': growth_rates
    }

# Sample data
sales_data = [
    {'month': 'Jan', 'sales': 50000, 'region': 'North'},
    {'month': 'Feb', 'sales': 45000, 'region': 'North'},
    {'month': 'Mar', 'sales': 62000, 'region': 'South'},
    {'month': 'Apr', 'sales': 58000, 'region': 'South'},
    {'month': 'May', 'sales': 67000, 'region': 'East'},
    {'month': 'Jun', 'sales': 71000, 'region': 'East'},
]

analysis = analyze_sales_data(sales_data)
print("Sales Analysis:")
print(f"Total Sales: ${analysis['total_sales']:,}")
print(f"Average Monthly: ${analysis['average_monthly']:,.2f}")
print(f"Best Month: {analysis['best_month']['month']} (${analysis['best_month']['sales']:,})")
print(f"Worst Month: {analysis['worst_month']['month']} (${analysis['worst_month']['sales']:,})")
print("Region Totals:", analysis['region_totals'])
print("Growth Rates:", analysis['growth_rates'])
```

### 4. Simple Game Inventory
```python
class GameInventory:
    def __init__(self):
        self.items = []
        self.max_slots = 20
    
    def add_item(self, item_name, quantity=1, item_type="misc"):
        # Check if item already exists
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] += quantity
                print(f"Added {quantity} {item_name}(s). Total: {item['quantity']}")
                return True
        
        # Check if inventory is full
        if len(self.items) >= self.max_slots:
            print("Inventory is full!")
            return False
        
        # Add new item
        self.items.append({
            'name': item_name,
            'quantity': quantity,
            'type': item_type
        })
        print(f"Added {quantity} {item_name}(s) to inventory")
        return True
    
    def use_item(self, item_name, quantity=1):
        for i, item in enumerate(self.items):
            if item['name'] == item_name:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    print(f"Used {quantity} {item_name}(s)")
                    
                    # Remove item if quantity reaches 0
                    if item['quantity'] == 0:
                        self.items.pop(i)
                        print(f"{item_name} removed from inventory")
                    return True
                else:
                    print(f"Not enough {item_name}. Have: {item['quantity']}, Need: {quantity}")
                    return False
        
        print(f"{item_name} not found in inventory")
        return False
    
    def get_items_by_type(self, item_type):
        return [item for item in self.items if item['type'] == item_type]
    
    def sort_inventory(self, by='name'):
        if by == 'name':
            self.items.sort(key=lambda x: x['name'])
        elif by == 'quantity':
            self.items.sort(key=lambda x: x['quantity'], reverse=True)
        elif by == 'type':
            self.items.sort(key=lambda x: x['type'])
    
    def show_inventory(self):
        if not self.items:
            print("Inventory is empty")
            return
        
        print(f"\n=== Inventory ({len(self.items)}/{self.max_slots} slots) ===")
        print(f"{'Item':<20} {'Qty':<5} {'Type':<10}")
        print("-" * 35)
        
        for item in self.items:
            print(f"{item['name']:<20} {item['quantity']:<5} {item['type']:<10}")
        print()

# Usage example
inventory = GameInventory()

# Add items
inventory.add_item("Health Potion", 5, "consumable")
inventory.add_item("Magic Sword", 1, "weapon")
inventory.add_item("Gold Coin", 100, "currency")
inventory.add_item("Health Potion", 3, "consumable")  # Add more to existing
inventory.add_item("Shield", 1, "armor")

inventory.show_inventory()

# Use items
inventory.use_item("Health Potion", 2)
inventory.use_item("Gold Coin", 50)

# Show items by type
print("Consumables:", inventory.get_items_by_type("consumable"))

# Sort and display
inventory.sort_inventory(by='type')
inventory.show_inventory()
```

---

## Best Practices

### 1. Naming and Documentation
```python
# Good: Descriptive names
student_grades = [85, 92, 78, 96]
valid_email_addresses = ["user@example.com", "admin@site.org"]

# Bad: Unclear names
lst = [85, 92, 78, 96]
data = ["user@example.com", "admin@site.org"]

# Good: Document complex operations
def process_student_scores(scores):
    """
    Process a list of student scores and return statistics.
    
    Args:
        scores (list): List of numeric scores
    
    Returns:
        dict: Statistics including average, min, max, and grade distribution
    """
    if not scores:
        return {'error': 'No scores provided'}
    
    return {
        'average': sum(scores) / len(scores),
        'minimum': min(scores),
        'maximum': max(scores),
        'count': len(scores)
    }
```

### 2. Avoiding Common Mistakes
```python
# Mistake: Modifying list while iterating
numbers = [1, 2, 3, 4, 5, 6]

# Wrong way
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # This can skip elements!

# Right way: Create new list
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 != 0]

# Or iterate backwards
numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)

# Mistake: Creating shallow copies with multiplication
matrix = [[0] * 3] * 3  # Wrong! All rows are the same object
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - all rows changed!

# Correct way
matrix = [[0] * 3 for _ in range(3)]  # Each row is a separate object
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - only first row changed
```

### 3. Performance Best Practices
```python
# Use list comprehensions instead of loops when possible
# Faster
squares = [x**2 for x in range(1000)]

# Slower
squares = []
for x in range(1000):
    squares.append(x**2)

# Use extend() instead of multiple append() calls
# Faster
result = []
data_chunks = [[1, 2], [3, 4], [5, 6]]
for chunk in data_chunks:
    result.extend(chunk)

# Slower
result = []
data_chunks = [[1, 2], [3, 4], [5, 6]]
for chunk in data_chunks:
    for item in chunk:
        result.append(item)

# Use 'in' for membership testing with small lists
# For large datasets, consider using sets
small_list = [1, 2, 3, 4, 5]
if 3 in small_list:  # OK for small lists
    print("Found")

large_list = list(range(10000))
large_set = set(large_list)  # Convert to set for faster lookups
if 5000 in large_set:  # Much faster for large collections
    print("Found")
```

### 4. Code Organization
```python
# Good: Break complex operations into functions
def clean_data(raw_data):
    """Remove invalid entries from data list."""
    return [item for item in raw_data if item is not None and item != ""]

def calculate_statistics(data):
    """Calculate basic statistics for numeric data."""
    if not data:
        return {}
    
    return {
        'mean': sum(data) / len(data),
        'median': sorted(data)[len(data) // 2],
        'range': max(data) - min(data)
    }

def process_dataset(raw_data):
    """Main processing pipeline for dataset."""
    cleaned_data = clean_data(raw_data)
    numeric_data = [float(x) for x in cleaned_data if str(x).replace('.', '').isdigit()]
    stats = calculate_statistics(numeric_data)
    return stats

# Good: Use constants for magic numbers
MAX_ITEMS = 100
DEFAULT_TIMEOUT = 30
VALID_GRADES = ['A', 'B', 'C', 'D', 'F']

def validate_grade(grade):
    return grade in VALID_GRADES
```

---

## Common Pitfalls

### 1. Index Errors
```python
# Problem: Accessing non-existent indices
my_list = [1, 2, 3]

# This will raise IndexError
try:
    print(my_list[5])
except IndexError as e:
    print(f"Error: {e}")

# Solutions:
# 1. Check length first
if len(my_list) > 5:
    print(my_list[5])
else:
    print("Index out of range")

# 2. Use get() method for dictionaries, or create safe_get for lists
def safe_get(lst, index, default=None):
    try:
        return lst[index]
    except IndexError:
        return default

result = safe_get(my_list, 5, "Not found")
print(result)  # Output: Not found
```

### 2. Mutable Default Arguments
```python
# Problem: Using mutable objects as default arguments
def add_item_wrong(item, target_list=[]):  # Wrong!
    target_list.append(item)
    return target_list

list1 = add_item_wrong("a")
list2 = add_item_wrong("b")
print(list1)  # Output: ['a', 'b'] - Unexpected!
print(list2)  # Output: ['a', 'b'] - Same object!

# Solution: Use None as default
def add_item_correct(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

list1 = add_item_correct("a")
list2 = add_item_correct("b")
print(list1)  # Output: ['a']
print(list2)  # Output: ['b']
```

### 3. Shallow vs Deep Copy Issues
```python
import copy

# Problem with nested lists
original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy - nested lists are still references
shallow_copy = original.copy()
shallow_copy[0][0] = 99
print(original)  # Output: [[99, 2, 3], [4, 5, 6]] - Original changed!

# Solution: Deep copy for nested structures
original = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 99
print(original)  # Output: [[1, 2, 3], [4, 5, 6]] - Original unchanged
print(deep_copy)  # Output: [[99, 2, 3], [4, 5, 6]]
```

### 4. Memory Issues with Large Lists
```python
# Problem: Creating very large lists in memory
# This could cause memory issues
try:
    huge_list = [0] * 10**9  # 1 billion zeros
except MemoryError:
    print("Not enough memory!")

# Solutions:
# 1. Use generators for large sequences
def large_sequence(n):
    for i in range(n):
        yield i * i

# Use only what you need
for i, value in enumerate(large_sequence(10**6)):
    if i >= 10:  # Only process first 10 items
        break
    print(value)

# 2. Process data in chunks
def process_in_chunks(data, chunk_size=1000):
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i+chunk_size]
        # Process chunk
        yield sum(chunk)  # Example processing

# 3. Use array module for numeric data (more memory efficient)
import array
numeric_array = array.array('i', [1, 2, 3, 4, 5])  # More memory efficient than list
```

### 5. Incorrect List Comparisons
```python
# Problem: Comparing lists with floating-point numbers
list1 = [0.1 + 0.2, 0.4 + 0.5]
list2 = [0.3, 0.9]

print(list1 == list2)  # Output: False (due to floating-point precision)
print(list1[0])        # Output: 0.30000000000000004

# Solution: Use approximate comparison for floats
def lists_approximately_equal(list1, list2, tolerance=1e-9):
    if len(list1) != len(list2):
        return False
    
    for a, b in zip(list1, list2):
        if abs(a - b) > tolerance:
            return False
    return True

result = lists_approximately_equal(list1, list2)
print(result)  # Output: True
```

---

This comprehensive guide covers everything you need to know about Python lists. Use it as a reference while coding, and practice with the examples to build your skills!