# Conditional Statements in Python: A Comprehensive Guide

## Table of Contents

- [Introduction](#introduction)
- [The if Statement](#the-if-statement)
- [if-else Statement](#if-else-statement)
- [elif (Else If)](#elif-else-if)
- [Nested Conditionals](#nested-conditionals)
- [Comparison Operators](#comparison-operators)
- [Logical Operators and Chaining](#logical-operators-and-chaining)
- [Short-Circuit Evaluation](#short-circuit-evaluation)
- [Ternary Conditional Expressions](#ternary-conditional-expressions)
- [Conclusion](#conclusion)

---

## Introduction

Conditional statements let you control the flow of your Python programs by executing code only when certain conditions are met. They are essential for decision-making in your code.

---

## The if Statement

The `if` statement checks a condition and runs a block of code if the condition is `True`.

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

---

## if-else Statement

The `else` block runs if the `if` condition is `False`.

```python
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

---

## elif (Else If)

Use `elif` to check multiple conditions in sequence.

```python
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")
```

---

## Nested Conditionals

You can place conditionals inside other conditionals for more complex logic.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID required.")
else:
    print("Entry denied.")
```

---

## Comparison Operators

Used to compare values in conditions:

| Operator | Description           | Example  |
| -------- | --------------------- | -------- |
| `==`     | Equal to              | `a == b` |
| `!=`     | Not equal to          | `a != b` |
| `>`      | Greater than          | `a > b`  |
| `<`      | Less than             | `a < b`  |
| `>=`     | Greater than or equal | `a >= b` |
| `<=`     | Less than or equal    | `a <= b` |

---

## Logical Operators and Chaining

Logical operators let you combine multiple conditions in a single statement. This is called chaining conditionals.

- **and**: All conditions must be `True`.
- **or**: At least one condition must be `True`.
- **not**: Inverts the condition (True becomes False, and vice versa).

**Examples:**

```python
age = 25
has_ticket = True
has_id = False

# Using 'and': both conditions must be True
if age >= 18 and has_ticket:
    print("You can enter.")

# Using 'or': at least one condition must be True
if has_ticket or has_id:
    print("You have access.")

# Using 'not': inverts the condition
if not has_id:
    print("You need to bring your ID.")

# Chaining multiple conditions
if (age >= 18 and has_ticket) or has_id:
    print("Entry allowed by age and ticket, or by ID.")
```

---

## Short-Circuit Evaluation

Python stops evaluating logical expressions as soon as the result is known.

```python
x = 5
if x > 0 or 1/0 == 1:
    print("No error, because the first condition is True.")
```

---

## Ternary Conditional Expressions

A compact way to write simple if-else statements.

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

---

## Conclusion

Conditional statements are fundamental for making decisions in Python programs. Practice using `if`, `elif`, `else`, and logical operators to control your program's logic and flow.
