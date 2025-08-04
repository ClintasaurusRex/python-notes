# List Comprehensions with Data Aggregation

List comprehensions provide a concise way to create new lists based on existing iterables. You can integrate data aggregation functions like `sum()`, `min()`, and `max()` directly within list comprehensions to perform calculations on the elements of the new list as it's being created.

---

## Calculating the Sum of Squares

```python
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum([n * n for n in numbers])
print(sum_of_squares)
# Output: 55
```

In this example, the list comprehension `[n * n for n in numbers]` creates a list of squares, and the `sum()` function calculates the sum of these squares.

---

## Finding the Minimum of Transformed Values

```python
numbers = [-3, -1, 0, 1, 3]
min_absolute = min([abs(n) for n in numbers])
print(min_absolute)
# Output: 0
```

Here, the list comprehension `[abs(n) for n in numbers]` creates a list of absolute values, and the `min()` function finds the minimum value in this list.

---

## Finding the Maximum of Filtered Values

```python
numbers = [1, 2, 3, 4, 5, 6]
max_even = max([n for n in numbers if n % 2 == 0])
print(max_even)
# Output: 6
```

In this example, the list comprehension `[n for n in numbers if n % 2 == 0]` creates a list of even numbers, and the `max()` function finds the maximum value in this list.
