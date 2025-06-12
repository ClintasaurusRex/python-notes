# Writing Functions in Python

## Table of Contents

- [Introduction](#introduction)
- [Defining a Function](#defining-a-function)
- [Function Parameters and Arguments](#function-parameters-and-arguments)
- [Return Values](#return-values)
- [Default and Keyword Arguments](#default-and-keyword-arguments)
- [Docstrings and Documentation](#docstrings-and-documentation)
- [Solving Problems with Functions](#solving-problems-with-functions)
  - [Example: Counting Vowels in a String](#example-counting-vowels-in-a-string)
  - [Example: Finding the Maximum in a List](#example-finding-the-maximum-in-a-list)
- [Conclusion](#conclusion)

---

## Introduction

Functions are reusable blocks of code that perform a specific task. They help organize your code, avoid repetition, and make programs easier to read and maintain.

---

## Defining a Function

Use the `def` keyword to define a function, followed by the function name and parentheses.

```python
def greet():
    print("Hello!")

greet()  # Output: Hello!
```

---

## Function Parameters and Arguments

You can pass information to functions using parameters (in the definition) and arguments (when calling).

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

---

## Return Values

Functions can return values using the `return` statement.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

---

## Default and Keyword Arguments

You can provide default values for parameters and use keyword arguments when calling functions.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Bob")  # Output: Hello, Bob!
greet("Bob", greeting="Hi")  # Output: Hi, Bob!
```

---

## Docstrings and Documentation

A docstring is a special string at the start of a function that describes what it does.

```python
def square(x):
    """Return the square of x."""
    return x * x

print(square.__doc__)  # Output: Return the square of x.
```

---

## Solving Problems with Functions

Functions are powerful tools for breaking down and solving real-world problems. Here are some examples:

### Example: Counting Vowels in a String

Let's write a function to count the number of vowels in a string.

```python
def count_vowels(text):
    """Return the number of vowels in the input string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

sentence = "Hello, how are you?"
print(count_vowels(sentence))  # Output: 7
```

### Example: Finding the Maximum in a List

Let's write a function to find the maximum value in a list (without using the built-in `max()` function).

```python
def find_max(numbers):
    """Return the maximum value in a list of numbers."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

nums = [3, 7, 2, 9, 4]
print(find_max(nums))  # Output: 9
```

---

## Conclusion

Writing functions is essential for structuring your code and solving problems efficiently. Practice creating your own functions to become a more effective Python programmer.
