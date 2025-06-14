# Working with Lists in Python

## Table of Contents

- [Introduction](#introduction)
- [Looping Over Lists](#looping-over-lists)
- [Using range() with Lists](#using-range-with-lists)
- [List Built-in Functions](#list-built-in-functions)
  - [len()](#len)
  - [sum(), min(), max()](#sum-min-max)
  - [sorted()](#sorted)
  - [reversed()](#reversed)
- [List Comprehensions](#list-comprehensions)
- [Enumerate and Indexing](#enumerate-and-indexing)
- [Conclusion](#conclusion)

---

## Introduction

Lists are a core data structure in Python, allowing you to store and manipulate collections of items. This guide covers common ways to work with lists, including looping, built-in functions, and useful techniques.

---

## Looping Over Lists

You can process each item in a list using a `for` loop.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

_This is the most common way to access each element in a list._

---

## Using range() with Lists

The `range()` function generates a sequence of numbers, often used for looping a specific number of times or accessing list indices.

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

_Use `range()` when you need the index as well as the value._

---

## List Built-in Functions

Python provides several built-in functions for working with lists:

### len()

Returns the number of items in a list.

```python
print(len(fruits))  # 3
```

### sum(), min(), max()

- **sum()**: Returns the sum of all elements (numeric lists).
- **min()**: Returns the smallest element.
- **max()**: Returns the largest element.

```python
numbers = [2, 5, 1]
print(sum(numbers))  # 8
print(min(numbers))  # 1
print(max(numbers))  # 5
```

### sorted()

Returns a new sorted list from the elements of any iterable.

```python
print(sorted(fruits))
```

### reversed()

Returns an iterator that accesses the given list in the reverse order.

```python
for fruit in reversed(fruits):
    print(fruit)
```

---

## List Comprehensions

A concise way to create lists using a single line of code.

List comprehensions are powerful because they let you **transform** each item in a list or **filter** items based on a condition, all in one readable line.

- **Transforming:** You can apply an operation to every item in a sequence.
- **Filtering:** You can include only items that meet a condition.

**Examples:**

_Transforming each item:_

```python
numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares)  # [1, 4, 9, 16]
```

_Filtering items:_

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6]
```

_Transforming and filtering together:_

```python
numbers = [1, 2, 3, 4, 5, 6]
squared_evens = [x**2 for x in numbers if x % 2 == 0]
print(squared_evens)  # [4, 16, 36]
```

_List comprehensions make your code shorter, clearer, and often more efficient when working with lists._

---

## Enumerate and Indexing

The `enumerate()` function is useful when you need both the index (position) and the value from a list while looping. Instead of manually keeping track of the index with a counter, `enumerate()` automatically provides it for you.

**Why is this useful?**

- It makes your code cleaner and less error-prone.
- You can easily access or modify items at specific positions.
- It's especially helpful when you need to display or process both the index and the value.

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
```

_Output:_

```
Index 0: apple
Index 1: banana
Index 2: cherry
```

_Use `enumerate()` whenever you need both the index and the value in a loop._

---

## Conclusion

Mastering list operations and built-in functions will make your Python code more efficient and expressive. Practice these techniques to become more comfortable working with lists.
