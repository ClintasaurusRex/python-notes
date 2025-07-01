# Guide: Rounding Numbers in Python

This guide explains how to write a Python program that takes a number and the number of decimal places as input, then outputs the rounded result. The program demonstrates user input, type conversion, and the use of the built-in `round()` function.

---

## 1. Program Overview

The program performs these steps:

1. Takes a number as input from the user (as a float).
2. Takes the number of decimal places to round to (as an integer).
3. Rounds the number to the specified decimal places.
4. Prints the rounded result.

---

## 2. Step-by-Step Explanation

### a) Taking User Input

```python
num = float(input())
```

- `input()` gets a string from the user.
- `float()` converts the string to a floating-point number.

### b) Getting Decimal Places

```python
decimal_places = int(input())
```

- `input()` gets another string from the user.
- `int()` converts it to an integer, representing the number of decimal places.

### c) Rounding the Number

```python
rounded = round(num, decimal_places)
```

- `round()` takes two arguments: the number and the number of decimal places.
- It returns the rounded value.

### d) Outputting the Result

```python
print(rounded)
```

- Prints the rounded number to the screen.

---

## 3. Example Run

```
Input:
3.14159
2

Output:
3.14
```

---

## 4. Practice

- Try different numbers and decimal places.
- What happens if you enter 0 for decimal places?
- Try negative numbers or very large numbers.

---

## 5. Summary Table

| Step           | Code Example                    | Description                               |
| -------------- | ------------------------------- | ----------------------------------------- |
| Input as float | `num = float(input())`          | Get a floating-point number from the user |
| Input as int   | `decimal_places = int(input())` | Get an integer from the user              |
| Rounding       | `round(num, decimal_places)`    | Round to specified decimal places         |
| Output         | `print(rounded)`                | Print the result                          |

---

This program is a simple way to practice user input, type conversion, and rounding in Python!
