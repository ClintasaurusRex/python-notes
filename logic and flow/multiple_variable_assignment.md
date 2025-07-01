# Guide: Python Variable Assignment and Unpacking

This tutorial explains the concepts demonstrated in the `pre-run.py` program. You'll learn how to assign values to multiple variables in a single line, use chained assignment, unpack lists into variables, and swap variable values without a temporary variable.

---

## 1. Assigning Multiple Variables in One Line

You can assign values to several variables at once using a single line:

```python
name, age, city = "Alice", 30, "New York"
```

- `name` gets the value `"Alice"`
- `age` gets the value `30`
- `city` gets the value `"New York"`

This is called **tuple unpacking** or **multiple assignment**.

---

## 2. Chained Assignment

You can assign the same value to multiple variables in one line:

```python
x = y = z = 100
```

- All three variables (`x`, `y`, and `z`) are set to `100`.

---

## 3. List Creation and Unpacking

Create a list and assign its elements to variables in a single line:

```python
colors = ["red", "green", "blue"]
color1, color2, color3 = colors
```

- `colors` is a list containing three strings.
- `color1`, `color2`, and `color3` are assigned the values from the list, respectively.

---

## 4. Printing the Results

The program prints the values to show the assignments:

```python
print(f"Name: {name}, Age: {age}, City: {city}")
print(f"x: {x}, y: {y}, z: {z}")
print(f"Colors: {color1}, {color2}, {color3}")
```

---

---

## 5. Using Placeholder Variables in Loops and Unpacking

### a) Placeholder in Loops

When you need to loop a certain number of times but don't need the loop variable, use an underscore (`_`) as a placeholder:

```python
for _ in range(5):
    print("Iteration")
```

This will print "Iteration" five times. The underscore tells readers that the loop variable is intentionally unused.

### b) Placeholder in List Unpacking

You can also use underscores to ignore specific values when unpacking a list:

```python
numbers = [10, 20, 30, 40, 50]
first, _, middle, _, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")
```

Here, `first` gets 10, `middle` gets 30, and `last` gets 50. The underscores ignore the second and fourth values.

Python allows you to swap the values of two variables in a single line, without needing a temporary variable:

```python
# Initialize variables x and y
x = 5
y = 10

# Swap the values
x, y = y, x

print(f"x: {x}")
print(f"y: {y}")
```

**How it works:**

- The right side `(y, x)` creates a tuple of the current values of `y` and `x`.
- The left side `x, y` unpacks those values back into the variables, effectively swapping them.

**Output:**

```
x: 10
y: 5
```

---

## Summary Table

| Concept                  | Example Code                  | Description                                |
| ------------------------ | ----------------------------- | ------------------------------------------ |
| Multiple Assignment      | `a, b, c = 1, 2, 3`           | Assigns 1 to a, 2 to b, 3 to c             |
| Chained Assignment       | `x = y = z = 100`             | All variables get the value 100            |
| List Unpacking           | `a, b, c = [1, 2, 3]`         | Assigns 1 to a, 2 to b, 3 to c from a list |
| Variable Swapping        | `x, y = y, x`                 | Swaps the values of x and y                |
| Placeholder in Loop      | `for _ in range(5):`          | Loop where the variable is unused          |
| Placeholder in Unpacking | `a, _, b, _, c = [1,2,3,4,5]` | Ignores values during unpacking            |

---

## Practice

Try changing the values or adding more variables to practice these techniques!
