# Write a program that:

# Takes a number as input from the user (float).

# Takes the number of decimal places to round to (integer).

# Outputs the rounded number.

num = float(input())
decimal_places = int(input())
rounded = round(num, decimal_places)
print(rounded)

# Guide: Calculating Discounted Prices in Python

This tutorial explains how to write a Python function that calculates the discounted price of an item, based on the original price and a discount percentage. The code example is from `pre-run.py`.

---

## 1. Problem Statement

Write a function that:

- Takes the original price of an item and a discount percentage as arguments.
- Calculates the discount amount.
- Subtracts the discount
