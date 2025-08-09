# Advanced Python Functions: A Guide

This guide covers advanced function concepts in Python, including how to return multiple values from a function and how to use lambda functions for concise, on-the-fly operations.

## Table of Contents

1. [Returning Multiple Values](#returning-multiple-values)
2. [Lambda Functions](#lambda-functions)

---

## Returning Multiple Values

In Python, a function can return multiple values by packing them into a tuple. When you call the function, you can unpack the returned tuple into multiple variables. This is a clean and readable way to handle functions that need to output more than one piece of information.

### Syntax and Example

The values are simply separated by commas in the `return` statement.

```python
def get_student_info():
    """
    Returns a student's name, age, and major.
    """
    name = "Alice"
    age = 20
    major = "Computer Science"
    return name, age, major

# Unpack the returned tuple into three variables
student_name, student_age, student_major = get_student_info()

print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Major: {student_major}")
```

### Output

```
Name: Alice
Age: 20
Major: Computer Science
```

---

## Lambda Functions

A **lambda function** is a small, anonymous function defined with the `lambda` keyword. It can take any number of arguments but can only have one expression. Lambda functions are syntactically restricted to a single expression and are typically used when you need a simple function for a short period.

### Syntax

The syntax for a lambda function is:
`lambda arguments: expression`

### Example: A Simple Multiplier

Here’s a lambda function that multiplies three numbers.

```python
multiply = lambda x, y, z: x * y * z

result = multiply(2, 3, 4)
print(f"The result is: {result}")
```

### Output

```
The result is: 24
```

### Common Use Case: Sorting with a Lambda

Lambda functions are often used as arguments to higher-order functions like `sorted()`, `map()`, and `filter()`. For example, you can use a lambda to specify a custom sort key.

```python
# A list of tuples (student, grade)
students = [("Alice", 88), ("Bob", 95), ("Charlie", 82)]

# Sort the list of students by their grade (the second item in the tuple)
sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
```

### Output

```
[('Charlie', 82), ('Alice', 88), ('Bob', 95)]
```
