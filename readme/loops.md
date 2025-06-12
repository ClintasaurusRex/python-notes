# Python Loops: A Comprehensive Guide

## Table of Contents

- [Introduction](#introduction)
- [For Loops](#for-loops)
- [While Loops](#while-loops)
- [Loop Control Statements](#loop-control-statements)
  - [break](#break)
  - [continue](#continue)
  - [else with Loops](#else-with-loops)
- [Nested Loops](#nested-loops)
- [Looping with range()](#looping-with-range)
- [Enumerate and Zip](#enumerate-and-zip)
- [List Comprehensions](#list-comprehensions)
- [Conclusion](#conclusion)

---

## Introduction

Loops are fundamental in Python for repeating actions. The two main types are `for` and `while` loops. This guide covers their usage, control statements, and best practices.

---

## For Loops

A `for` loop iterates over a sequence (like a list, tuple, or string):

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

- Use for: Iterating over items in a collection.

---

## While Loops

A `while` loop repeats as long as a condition is `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

- Use for: Repeating until a condition changes.

---

## Loop Control Statements

### break

- Exits the loop immediately.

```python
for n in range(10):
    if n == 5:
        break
    print(n)
```

### continue

- Skips the rest of the current loop iteration.

```python
for n in range(5):
    if n == 2:
        continue
    print(n)
```

### else with Loops

- The `else` block runs if the loop completes without a `break`.

```python
for n in range(3):
    print(n)
else:
    print("Done!")
```

---

## Nested Loops

A loop inside another loop:

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

---

## Looping with range()

- `range()` generates a sequence of numbers.

```python
for i in range(1, 6):
    print(i)
```

---

## Enumerate and Zip

- **enumerate()**: Get index and value while looping.
  ```python
  for i, value in enumerate(["a", "b", "c"]):
      print(i, value)
  ```
- **zip()**: Loop over multiple sequences in parallel.
  ```python
  names = ["Alice", "Bob"]
  scores = [85, 92]
  for name, score in zip(names, scores):
      print(name, score)
  ```

---

## List Comprehensions

- Compact way to create lists using loops.

```python
squares = [x**2 for x in range(5)]
```

---

## Conclusion

Loops are essential for automation and repetitive tasks in Python. Mastering them will make your code more efficient and expressive.
