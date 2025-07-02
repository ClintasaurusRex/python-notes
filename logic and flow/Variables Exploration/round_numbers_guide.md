# Guide: Calculating Discounted Prices in Python

This tutorial explains how to write a Python function that calculates the discounted price of an item, based on the original price and a discount percentage. The code example is from `pre-run.py`.

---

## 1. Problem Statement

Write a function that:
- Takes the original price of an item and a discount percentage as arguments.
- Calculates the discount amount.
- Subtracts the discount from the original price.
- Rounds the result to 2 decimal places.
- Returns the final discounted price.

---

## 2. Example Code

```python
def calculate_discount(price, discount_percentage):
    discount = float(price) * float(discount_percentage) / 100
    calc_with_discount = price - discount
    return round(calc_with_discount, 2)

print(calculate_discount(75.5, 10))      # 67.95
print(calculate_discount(349.99, 25.5))  # 260.24
```

---

## 3. Step-by-Step Explanation

1. **Calculate the discount amount:**
   - `discount = float(price) * float(discount_percentage) / 100`
   - This finds the percentage of the price to discount.
2. **Subtract the discount from the original price:**
   - `calc_with_discount = price - discount`
3. **Round the result to 2 decimal places:**
   - `return round(calc_with_discount, 2)`
4. **Return the final price:**
   - The function returns the discounted price, rounded to two decimals.

---

## 4. Example Output

```
67.95
260.24
```

---

## 5. Practice

- Try different prices and discount percentages.
- What happens if you use a discount percentage of 100?
- Experiment with rounding by changing the number of decimal places in the `round()` function.

---

## 6. Summary Table

| Step                     | Code Example                              | Description                                      |
| ------------------------ | ----------------------------------------- | ------------------------------------------------ |
| Calculate discount       | `discount = float(price) * float(discount_percentage) / 100` | Calculate the discount amount                    |
| Subtract discount        | `calc_with_discount = price - discount` | Calculate the price after discount               |
| Rounding                 | `return round(calc_with_discount, 2)`    | Round the final price to 2 decimal places       |
| Output                   | `print(calculate_discount(75.5, 10))`    | Print the discounted price                      |

---

This guide provided a concise way to learn about calculating discounted prices in Python, covering problem statement, example code, step-by-step explanation, and practice exercises.
