# Basic Error Handling in Python: Complete Reference Guide

This comprehensive guide covers error handling concepts in Python, including try-except blocks, specific exception types, and practical applications. All examples include detailed explanations and expected outputs.

## Table of Contents

1. [Introduction to Error Handling](#introduction-to-error-handling)
2. [Basic Try-Except Structure](#basic-try-except-structure)
3. [Handling Multiple Exception Types](#handling-multiple-exception-types)
4. [Complex Error Handling with Data Processing](#complex-error-handling-with-data-processing)
5. [Best Practices](#best-practices)

---

## Introduction to Error Handling

Error handling in Python allows your program to gracefully handle unexpected situations without crashing. Instead of letting errors terminate your program, you can catch them and respond appropriately.

### Common Exception Types

| Exception Type      | Description                           | Example Cause                              |
| ------------------- | ------------------------------------- | ------------------------------------------ |
| `ValueError`        | Inappropriate value for the operation | Converting "abc" to integer                |
| `ZeroDivisionError` | Division by zero                      | `10 / 0`                                   |
| `TypeError`         | Operation on inappropriate type       | Adding string to integer                   |
| `IndexError`        | List index out of range               | Accessing `list[10]` when list has 5 items |
| `KeyError`          | Dictionary key doesn't exist          | Accessing non-existent dictionary key      |
| `FileNotFoundError` | File doesn't exist                    | Opening a non-existent file                |

---

## Basic Try-Except Structure

The fundamental structure for handling errors uses `try` and `except` blocks.

### Syntax

```python
try:
    # Code that might raise an exception
    risky_operation()
except SpecificException:
    # Handle the specific exception
    handle_error()
```

### Example 1: Input Validation

**Problem**: Get user input and convert it to an integer, handling invalid input gracefully.

```python
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

**Sample Outputs:**

```
# Valid input
Enter a number: 42
You entered: 42

# Invalid input
Enter a number: abc
Invalid input! Please enter a valid number.
```

**Key Points:**

- `int()` raises `ValueError` when given invalid input
- The `except ValueError` block catches only this specific error
- Program continues running instead of crashing

---

## Handling Multiple Exception Types

You can handle different types of exceptions with separate `except` blocks, allowing for specific error messages and handling strategies.

### Example 2: Mathematical Operations with Multiple Error Types

**Problem**: Create a function that performs division and handles multiple potential errors.

```python
def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        value = int(input_string)
        # Calculate 100 divided by the input value
        result = 100 / value
        # Return the result
        return result
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        return "Input must be a number!"
    except ZeroDivisionError:
        # Handle the case where input is zero
        return "Cannot divide by zero!"
    except:
        # Handle any other unexpected exceptions
        return "An unexpected error occurred!"
```

**Sample Outputs:**

```python
print(process_data("10"))    # Output: 10.0
print(process_data("0"))     # Output: Cannot divide by zero!
print(process_data("abc"))   # Output: Input must be a number!
print(process_data("5"))     # Output: 20.0
```

**How It Works:**

1. **Normal Operation**: `process_data("10")`

   - Converts "10" to integer: `value = 10`
   - Calculates: `result = 100 / 10 = 10.0`
   - Returns: `10.0`

2. **ZeroDivisionError**: `process_data("0")`

   - Converts "0" to integer: `value = 0`
   - Attempts: `result = 100 / 0` → raises `ZeroDivisionError`
   - Caught by: `except ZeroDivisionError`
   - Returns: `"Cannot divide by zero!"`

3. **ValueError**: `process_data("abc")`
   - Attempts: `int("abc")` → raises `ValueError`
   - Caught by: `except ValueError`
   - Returns: `"Input must be a number!"`

### Exception Handling Order

```python
try:
    # risky code
except SpecificException:      # Most specific first
    # handle specific error
except AnotherSpecificException:
    # handle another specific error
except Exception:              # More general
    # handle any other exception
except:                        # Catch-all (least specific)
    # handle any remaining errors
```

**Important**: More specific exceptions should be handled before more general ones.

---

## Complex Error Handling with Data Processing

### Example 3: Shopping Cart with Comprehensive Error Handling

**Problem**: Process a list of shopping orders, handling various input format errors and data validation issues.

```python
def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            # Check if the order contains a colon
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue

            # Split the order into item and quantity
            item, quantity = order.split(":")

            # Try to convert quantity to integer
            try:
                quantity = int(quantity)
            except ValueError:
                print(f"Invalid quantity: {order}")
                continue

            # Check for negative quantities
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue

            # Add to cart (accumulate if item already exists)
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity

        except Exception:
            print(f"Unexpected error: {order}")

    return cart
```

**Sample Test Case:**

```python
testCase = ["apple:3", "banana:2", "milk:5"]
result = handle_shopping_cart(testCase)
print(result)
```

**Expected Output:**

```
{'apple': 3, 'banana': 2, 'milk': 5}
```

**Testing Error Cases:**

```python
error_cases = [
    "apple:3",      # Valid
    "banana",       # Missing colon
    "milk:abc",     # Invalid quantity
    "bread:-2",     # Negative quantity
    "cheese:5"      # Valid
]

result = handle_shopping_cart(error_cases)
```

**Expected Output:**

```
Invalid format: banana
Invalid quantity: milk:abc
Negative quantity not allowed: bread:-2
{'apple': 3, 'cheese': 5}
```

### Step-by-Step Breakdown

**For each order, the function:**

1. **Format Validation**: Checks if order contains ":"

   - `"banana"` → Missing colon → Print error, skip to next

2. **Parsing**: Splits order into item and quantity

   - `"apple:3"` → `item = "apple"`, `quantity = "3"`

3. **Type Conversion**: Converts quantity to integer

   - `"3"` → `3` (success)
   - `"abc"` → raises `ValueError` → Print error, skip to next

4. **Value Validation**: Checks for negative quantities

   - `quantity = -2` → Print error, skip to next

5. **Dictionary Update**: Adds valid items to cart
   - If item exists: add to existing quantity
   - If new item: create new entry

### Error Handling Strategies Used

1. **Input Validation**: Check format before processing
2. **Nested Try-Except**: Handle conversion errors separately
3. **Continue Statement**: Skip invalid entries without stopping processing
4. **Accumulation Logic**: Handle duplicate items appropriately
5. **Graceful Degradation**: Return partial results even with some errors

---

## Best Practices

### 1. Be Specific with Exception Types

```python
# Good - specific exception handling
try:
    value = int(user_input)
except ValueError:
    print("Please enter a valid number")

# Less ideal - too general
try:
    value = int(user_input)
except:
    print("Something went wrong")
```

### 2. Use Multiple Except Blocks

```python
try:
    result = calculate_something()
except ValueError:
    print("Invalid value provided")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### 3. Don't Ignore Exceptions

```python
# Good - handle the exception appropriately
try:
    risky_operation()
except SpecificException:
    log_error("Operation failed")
    return default_value

# Bad - silently ignoring errors
try:
    risky_operation()
except:
    pass  # This hides potential problems
```

### 4. Use Continue or Return Appropriately

```python
# In loops, use continue to skip problematic items
for item in items:
    try:
        process_item(item)
    except ValueError:
        print(f"Skipping invalid item: {item}")
        continue  # Move to next item

# In functions, return early for error conditions
def process_data(data):
    try:
        validate_data(data)
    except ValidationError:
        return None  # Early return for invalid data

    return process_valid_data(data)
```

### 5. Provide Meaningful Error Messages

```python
# Good - specific and helpful
except ValueError:
    print(f"Invalid quantity '{quantity}' for item '{item}'. Please use a number.")

# Less helpful - too vague
except ValueError:
    print("Error occurred")
```

---

## Summary

Error handling is essential for creating robust Python applications. Key takeaways:

- **Use try-except blocks** to handle anticipated errors gracefully
- **Be specific** about which exceptions you catch
- **Handle different exception types** with appropriate responses
- **Provide helpful error messages** to users
- **Continue processing** when possible rather than stopping completely
- **Validate input** before using it in operations
- **Test error conditions** to ensure your handling works correctly

With these techniques, your programs will be more resilient and provide better user experiences when things don't go as expected.
