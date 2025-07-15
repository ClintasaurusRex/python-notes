# Membership Checks in Python: A Comprehensive Guide

This guide provides a detailed look at membership checks in Python using the `in` and `not in` operators. Membership checks are used to test whether a value or variable is found in a sequence (like a list, tuple, string, or dictionary).

---

## 1. Membership Checks in Lists

Lists are one of the most common data types to check for membership.

```python
# --- Membership in Lists ---
fruits = ["apple", "banana", "cherry"]

# Check if "banana" is in the list
if "banana" in fruits:
    print("Yes, 'banana' is in the fruits list.") # This will be printed

# Check if "mango" is not in the list
if "mango" not in fruits:
    print("Yes, 'mango' is not in the fruits list.") # This will be printed
```

### Example in a function

```python
def is_fruit_available(fruit, fruit_list):
    """Checks if a fruit is in the list of available fruits."""
    return fruit in fruit_list

fruits = ["apple", "banana", "cherry"]
print(f"Is 'apple' available? {is_fruit_available('apple', fruits)}")
print(f"Is 'mango' available? {is_fruit_available('mango', fruits)}")
```

---

## 2. Membership Checks in Tuples

Membership checks work the same way for tuples.

```python
# --- Membership in Tuples ---
colors = ("red", "green", "blue")

if "green" in colors:
    print("Yes, 'green' is a color.")

if "yellow" not in colors:
    print("No, 'yellow' is not a color.")
```

---

## 3. Membership Checks in Strings

You can check for the presence of a character or a substring within a string.

```python
# --- Membership in Strings ---
sentence = "hello world"

# Check for a character
if "h" in sentence:
    print("The character 'h' is in the sentence.")

# Check for a substring
if "world" in sentence:
    print("The substring 'world' is in the sentence.")

if "python" not in sentence:
    print("The substring 'python' is not in the sentence.")
```

---

## 4. Membership Checks in Dictionaries

For dictionaries, the `in` operator checks for the presence of **keys**, not values.

### Checking for Keys

```python
# --- Membership in Dictionaries (Keys) ---
user = {"username": "coder123", "email": "coder@example.com", "level": 5}

# Check for a key
if "username" in user:
    print("The key 'username' exists in the user dictionary.")

if "password" not in user:
    print("The key 'password' does not exist.")
```

### Checking for Values

To check for a value, you need to use the `.values()` method.

```python
# --- Membership in Dictionaries (Values) ---
user = {"username": "coder123", "email": "coder@example.com", "level": 5}

if "coder123" in user.values():
    print("The value 'coder123' exists in the user dictionary.")

if 10 not in user.values():
    print("The value 10 does not exist in the user dictionary.")
```

### Checking for Key-Value Pairs

To check for a key-value pair, use the `.items()` method.

```python
# --- Membership in Dictionaries (Items) ---
user = {"username": "coder123", "email": "coder@example.com", "level": 5}

if ("level", 5) in user.items():
    print("The item ('level', 5) exists in the user dictionary.")
```

---

## Practical Scenario: Access Control

Let's combine these concepts in a simple access control scenario.

```python
# --- Practical Scenario: Access Control ---
allowed_users_list = ["Alice", "Bob", "Charlie"]
user_permissions_dict = {
    "Alice": "admin",
    "Bob": "editor",
    "David": "viewer"
}

def check_access(username):
    """
    Checks if a user is in the allowed list and what their permission level is.
    """
    print(f"Checking access for: {username}")
    # Check if the user is in the list of allowed users
    if username in allowed_users_list:
        print(f"Welcome, {username}!")
        # Now check for permissions in the dictionary
        if username in user_permissions_dict:
            permission = user_permissions_dict[username]
            print(f"Your permission level is: {permission}")
            # You can even do a membership check on the permission string
            if "admin" in permission:
                print("You have full administrative access.")
        else:
            print("You are an allowed user, but have no specific permissions assigned.")
    else:
        print(f"Access denied for {username}.")

check_access("Alice")
print("-" * 10)
check_access("David") # Not in the allowed list
print("-" * 10)
check_access("Charlie") # In the allowed list but not in the permissions dictionary
```
