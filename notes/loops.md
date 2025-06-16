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

A `for` loop is used to repeat actions for each item in a sequence (like a list, tuple, or string). It's perfect when you know exactly what you want to loop over—like every element in a list, every character in a string, or every line in a file.

**How it works:**

- The loop grabs each item from the sequence, one at a time, and runs the indented code block for each item.
- When it reaches the end of the sequence, the loop stops.

**Common uses:**

- Processing every item in a list (e.g., printing, modifying, or checking values)
- Iterating over characters in a string
- Reading lines from a file

**Example:**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output:
# apple
# banana
# cherry
```

_This is the most common way to access each element in a list._

---

## While Loops

A `while` loop is used when you want to repeat actions, but you don't know in advance how many times you'll need to loop. It keeps going as long as a condition is `True`.

**How it works:**

- The loop checks the condition before each run.
- If the condition is `True`, it runs the indented code block.
- If the condition is `False`, the loop stops.

**Common uses:**

- Waiting for user input or a certain event
- Repeating until a calculation reaches a target
- Looping until a list is empty or a value is found

**Example:**

```python
count = 0
while count < 5:
    print(count)  # Output:
# 0
# 1
# 2
# 3
# 4
    count += 1
```

_Use for: Repeating until a condition changes. Great for open-ended or interactive tasks!_

---

## Loop Control Statements

Loop control statements let you change the flow of your loops:

- **break**: Stop the loop immediately, even if there are more items/iterations left.
- **continue**: Skip the rest of the current loop iteration and move to the next one.
- **else**: Attach an `else` block to a loop; it runs only if the loop wasn't stopped by `break`.

**Why use them?**

- To exit early when you find what you need (e.g., searching for a value)
- To skip unwanted items (e.g., skip blank lines)
- To run code only if the loop finished normally

**Examples:**

### break

```python
for n in range(10):
    if n == 5:
        break
    print(n)  # Output:
# 0
# 1
# 2
# 3
# 4
```

_Use `break` to exit a loop as soon as a condition is met._

### continue

```python
for n in range(5):
    if n == 2:
        continue
    print(n)  # Output:
# 0
# 1
# 3
# 4
```

_Use `continue` to skip over certain items or cases in your loop._

### else with Loops

```python
for n in range(3):
    print(n)  # Output:
# 0
# 1
# 2
else:
    print("Done!")  # Output:
# Done!
```

_The `else` block runs only if the loop wasn't stopped by `break`—great for search tasks!_

---

## Nested Loops

A nested loop is a loop inside another loop. The inner loop runs completely for each iteration of the outer loop.

**Think of it like this (Analogy):**

Imagine you have a list of chores for the week (Outer Loop - Days of the Week) and for each day, you have a list of specific tasks (Inner Loop - Tasks for that Day).

- **Outer Loop (Days):** Monday, Tuesday, Wednesday...
  - **Inner Loop (Tasks for Monday):** Wake up, Brush teeth, Eat breakfast, Go to work.
  - **Inner Loop (Tasks for Tuesday):** Wake up, Brush teeth, Eat breakfast, Go to gym.
  - And so on...

The inner "Tasks" loop has to finish all its items for "Monday" before the outer "Days" loop can move on to "Tuesday."

**How it works (Step-by-Step):**

1.  **Outer loop starts:** It picks the first item from its sequence.
2.  **Inner loop starts:** It runs through _all_ its items, one by one, using the current item from the outer loop.
3.  **Inner loop finishes:** Once the inner loop has gone through all its items, it stops.
4.  **Outer loop continues:** The outer loop moves to its _next_ item.
5.  **Repeat:** The inner loop starts again from the beginning, running through all its items for the new outer loop item.
6.  This continues until the outer loop has gone through all _its_ items.

**Visualizing Nested Loops:**

Let's say you want to print coordinates for a small grid (like on a map):

```python
# Outer loop for rows (let's say 2 rows)
for row in range(2):  # row will be 0, then 1
    # Inner loop for columns (let's say 3 columns)
    for col in range(3):  # col will be 0, then 1, then 2
        print(f"({row}, {col})") # Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
```

**Breakdown of the Grid Example:**

1.  **Outer Loop (row = 0):**

    - The outer loop starts, `row` is `0`.
    - **Inner Loop (col):**
      - `col` becomes `0`. Prints `(0, 0)`.
      - `col` becomes `1`. Prints `(0, 1)`.
      - `col` becomes `2`. Prints `(0, 2)`.
    - Inner loop finishes for `row = 0`.

2.  **Outer Loop (row = 1):**

    - The outer loop moves to the next item, `row` is `1`.
    - **Inner Loop (col):**
      - `col` becomes `0`. Prints `(1, 0)`.
      - `col` becomes `1`. Prints `(1, 1)`.
      - `col` becomes `2`. Prints `(1, 2)`.
    - Inner loop finishes for `row = 1`.

3.  **Outer loop finishes:** Both loops are done.

**Hands-On Example: Pairing Items from Two Lists**

Imagine you have two lists: `adjectives = ["big", "red"]` and `nouns = ["car", "ball"]`. You want to create all possible combinations:

```python
adjectives = ["big", "red"]
nouns = ["car", "ball"]

for adj in adjectives:  # Outer loop
    for noun in nouns:    # Inner loop
        print(f"{adj} {noun}") # Output:
# big car
# big ball
# red car
# red ball
```

**Step-by-step for the pairing example:**

1.  **Outer loop (adj = "big"):**

    - `adj` is "big".
    - **Inner loop (noun):**
      - `noun` is "car". Prints "big car".
      - `noun` is "ball". Prints "big ball".
    - Inner loop finishes for `adj = "big"`.

2.  **Outer loop (adj = "red"):**
    - `adj` is "red".
    - **Inner loop (noun):**
      - `noun` is "car". Prints "red car".
      - `noun` is "ball". Prints "red ball".
    - Inner loop finishes for `adj = "red"`.

**Common uses:**

- Working with grids, matrices, or 2D data (like pixels in an image, cells in a spreadsheet).
- Comparing every pair of items in two lists (or within the same list).
- Generating combinations or permutations (like all possible outfits from shirts and pants).
- Creating patterns (like stars in a pyramid shape).

**Example (from before, with updated output format for clarity):**

```python
for i in range(2):  # Outer loop: i will be 0, then 1
    for j in range(3):  # Inner loop: j will be 0, then 1, then 2 (for each i)
        print(f"i={i}, j={j}") # Output:
# i=0, j=0
# i=0, j=1
# i=0, j=2
# i=1, j=0
# i=1, j=1
# i=1, j=2
```

_Use nested loops for problems that need to compare or combine multiple sets of data, or when you need to perform an action multiple times for each item in an outer set._

**Explanation of the output (reiterated for clarity):**

- The outer loop (`i`) runs twice: first with `i = 0`, then with `i = 1`.
- **For each** value of `i`, the inner loop (`j`) runs completely (three times: `j = 0`, `j = 1`, and `j = 2`).
- So, the pairs printed are:
  - When `i = 0`: (i=0, j=0), (i=0, j=1), (i=0, j=2)
  - When `i = 1`: (i=1, j=0), (i=1, j=1), (i=1, j=2)
- This is why you see all combinations of `i` and `j` in the output.

**Key takeaway for ADHD learners:**
Focus on one loop at a time.

1.  Outer loop picks ONE item.
2.  Inner loop does ALL its work with that ONE item.
3.  Then, outer loop picks its NEXT item, and the inner loop does ALL its work again.
    It's like dealing one hand of cards (outer loop picks a player), and then that player plays all their cards (inner loop actions for that player), before moving to the next player.

---

## Looping with range()

The `range()` function is a super handy way to generate a sequence of numbers for your loops.

**How it works:**

- `range(stop)` gives numbers from 0 up to (but not including) `stop`.
- `range(start, stop)` gives numbers from `start` up to (but not including) `stop`.
- `range(start, stop, step)` lets you control the increment (or decrement).

**Common uses:**

- Looping a specific number of times
- Generating sequences of numbers
- Accessing list items by index

**Example:**

```python
for i in range(1, 6):
    print(i)  # Output:
# 1
# 2
# 3
# 4
# 5
```

_Use `range()` when you need to count, step, or access by index!_

---

## More Examples with range()

Here are some practical examples using `range()` with explanations:

### Example 1: Numbers divisible by 4 between 30 and 80

This loop prints all numbers between 30 and 80 (inclusive) that are divisible by 4. The `if num % 4 == 0` condition checks for divisibility.

```python
print("Numbers divisible by 4 between 30-80:")  # Output:
# Numbers divisible by 4 between 30-80:
for num in range(30, 81):
    if num % 4 == 0:
        print(num, end=", ")  # Output:
# 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80,
print()  # new line
```

### Example 2: First 8 odd numbers from 15

This uses `range(15, 15 + 2*8, 2)` to generate the first 8 odd numbers starting from 15. The step of 2 ensures only odd numbers are included.

```python
print("\nFirst 8 odd numbers from 15:")  # Output: First 8 odd numbers from 15:
for n in range(15, 15 + 2*8, 2):
    print(n, end=", ")  # Output: 15, 17, 19, 21, 23, 25, 27, 29,
print()  # new line
```

### Example 3: Counting backwards, divisible by 5

This loop counts backwards from 50 to 6, printing numbers divisible by 5. The step of -1 makes the range count down.

```python
print("\nCounting backwards, divisible by 5:")  # Output: Counting backwards, divisible by 5:
for n1 in range(50, 5, -1):
    if n1 % 5 == 0:
        print(n1, end=", ")  # Output: 50, 45, 40, 35, 30, 25, 20, 15, 10,
print()  # new line
```

### Example 4: Product of numbers divisible by 3 (1-30)

This calculates the product of all numbers from 1 to 30 that are divisible by 3. The product is updated inside the loop.

```python
print("\nProduct of numbers divisible by 3 (1-30):")  # Output: Product of numbers divisible by 3 (1-30):
product = 1
for n2 in range(1, 31):
    if n2 % 3 == 0:
        product *= n2
print(product)  # Output: 214277011200
```

---

## Enumerate and Zip

- **enumerate()**: Get index and value while looping.
  ```python
  for i, value in enumerate(["a", "b", "c"]):
      print(i, value)  # Output: 0 a\n1 b\n2 c
  ```
- **zip()**: Loop over multiple sequences in parallel.
  ```python
  names = ["Alice", "Bob"]
  scores = [85, 92]
  for name, score in zip(names, scores):
      print(name, score)  # Output: Alice 85\nBob 92
  ```

---

## List Comprehensions

- Compact way to create lists using loops.

```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

---

## Conclusion

Loops are essential for automation and repetitive tasks in Python. Mastering them will make your code more efficient and expressive.
