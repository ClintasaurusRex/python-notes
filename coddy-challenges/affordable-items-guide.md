# Beginner's Guide: How the 'Affordable Items' Program Works

This guide will walk you through every part of the program that takes a list of prices, a list of item names, and a budget per item, and tells you:

- Which items you can afford
- The total budget needed for those items
- How many items you can't afford

---

## 1. Inputs: What the Program Receives

The program expects three inputs from the user:

1. **A list of prices** (e.g., `10,20,5,50`)
2. **A list of item names** (e.g., `apple,banana,pear,grapes`)
3. **A budget per item** (e.g., `15`)

All inputs are entered one after the other, each on a new line.

---

## 2. Step-by-Step Code Explanation

### Step 1: Get the List of Prices

```python
prices = input().split(",")
```

- `input()` gets a line of text from the user (e.g., `10,20,5,50`).
- `.split(",")` splits the string into a list wherever there is a comma.
- Now, `prices` is a list of strings: `['10', '20', '5', '50']`.

### Step 2: Convert Prices to Integers

```python
for i in range(len(prices)):
    prices[i] = int(prices[i])
```

- Loops through each price in the list.
- `int(prices[i])` converts the string to an integer.
- After this, `prices` is `[10, 20, 5, 50]` (a list of numbers).

### Step 3: Get the List of Item Names

```python
items = input().split(",")
```

- Gets another line of input (e.g., `apple,banana,pear,grapes`).
- Splits it into a list: `['apple', 'banana', 'pear', 'grapes']`.

### Step 4: Get the Budget Per Item

```python
budget_per_item = int(input())
```

- Gets a single number from the user (e.g., `15`).
- Converts it to an integer.

### Step 5: Prepare to Store Results

```python
affordable_items = []
cant_afford = 0
total_needed = 0
```

- `affordable_items`: an empty list to store names of items you can afford.
- `cant_afford`: a counter for items you can't afford (starts at 0).
- `total_needed`: keeps track of the total price of all affordable items (starts at 0).

### Step 6: Check Each Item

```python
for i in range(len(items)):
    price = prices[i]
    item = items[i]
    if price <= budget_per_item:
        affordable_items.append(item)
        total_needed += price
    else:
        cant_afford += 1
```

- Loops through each item and its price (using their position in the list).
- `price = prices[i]` gets the price for the current item.
- `item = items[i]` gets the name of the current item.
- `if price <= budget_per_item:` checks if you can afford it.
  - If yes:
    - Adds the item name to `affordable_items`.
    - Adds the price to `total_needed`.
  - If not:
    - Increases `cant_afford` by 1.

### Step 7: Print the Results

```python
print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)
```

- Shows the list of items you can buy.
- Shows the total money needed for those items.
- Shows how many items you couldn't afford.

---

## 3. Example Walkthrough

Suppose you enter:

```
10,20,5,50
apple,banana,pear,grapes
15
```

- Prices: `[10, 20, 5, 50]`
- Items: `['apple', 'banana', 'pear', 'grapes']`
- Budget per item: `15`

The program checks each item:

- apple: 10 <= 15 → can buy
- banana: 20 > 15 → can't buy
- pear: 5 <= 15 → can buy
- grapes: 50 > 15 → can't buy

So:

- Can buy: `['apple', 'pear']`
- Total budget needed: `10 + 5 = 15`
- Can't afford: `2`

---

## 4. Key Concepts Used

- **Input and Output**: Getting and displaying information.
- **Lists**: Storing multiple values.
- **Loops**: Doing something for each item in a list.
- **Conditionals**: Making decisions with `if` and `else`.
- **Indexing**: Accessing items in a list by their position.

---

## 5. Tips for Beginners

- Always check that your lists (prices and items) are the same length!
- Use `print()` statements to debug and see what your variables contain at each step.
- Try changing the input values to see how the output changes.

---

This guide should help you understand every part of the program. If you get stuck, read through each step and try to match it to the code!
