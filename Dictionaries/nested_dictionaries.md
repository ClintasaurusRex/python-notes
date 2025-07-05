# A Comprehensive Guide to Nested Dictionaries in Python

A nested dictionary is a dictionary that contains other dictionaries as values. This powerful feature allows you to create complex, hierarchical data structures, perfect for modeling real-world relationships, managing configuration settings, or working with structured data formats like JSON.

This guide provides a detailed walkthrough of creating, accessing, modifying, and iterating over nested dictionaries, along with best practices and advanced techniques.

---

```python
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}

# Accessing a nested value
print(students["Alice"]["age"])  # Output: 20

# Adding a new key-value pair to a nested dictionary
students["Alice"]["major"] = "Math"
print(students["Alice"])  # Output: {'age': 20, 'grade': 'A', 'major': 'Math'}
```

## 1. Understanding the Structure

Think of a nested dictionary as a tree. Each key can lead to a simple value (like a string or number) or branch off into another dictionary.

```python
# Example: A dictionary of users with detailed profiles
users = {
    'user123': {
        'name': 'Alice',
        'email': 'alice@example.com',
        'profile': {
            'age': 30,
            'city': 'New York',
            'interests': ['coding', 'hiking']
        }
    },
    'user456': {
        'name': 'Bob',
        'email': 'bob@example.com',
        'profile': {
            'age': 25,
            'city': 'London',
            'interests': ['music', 'reading']
        }
    }
}
```

In this structure:

- The top-level keys (`'user123'`, `'user456'`) map to user dictionaries.
- Each user dictionary contains keys like `'name'` and `'profile'`.
- The `'profile'` key maps to another dictionary, creating the nesting.
- You can even nest other data structures, like the list of `'interests'`.

---

## 2. Accessing Nested Values

To retrieve data from a nested dictionary, you chain keys together.

### a. Direct Access with Square Brackets `[]`

This is the most direct way to access a value. However, it will raise a `KeyError` if any key in the chain does not exist.

```python
# Get Alice's email
alice_email = users['user123']['email']
print(f"Alice's email: {alice_email}")  # Output: Alice's email: alice@example.com

# Get Bob's first interest
bob_interest = users['user456']['profile']['interests'][0]
print(f"Bob's first interest: {bob_interest}") # Output: Bob's first interest: music

# This would cause an error because the key 'country' does not exist
# print(users['user456']['profile']['country'])  # Raises KeyError
```

### b. Safe Access with the `.get()` Method

To avoid `KeyError`, use the `.get()` method. It returns `None` (or a default value you provide) if a key is not found. This is crucial for safely navigating complex structures.

```python
# Safely get a value that exists
profile = users.get('user123', {}).get('profile', {})
alice_age = profile.get('age')
print(f"Alice's age: {alice_age}") # Output: Alice's age: 30

# Safely try to get a value from a non-existent key
# By providing an empty dictionary {} as the default, we prevent an error on the second .get()
user789_profile = users.get('user789', {}).get('profile')
print(f"User 789's profile: {user789_profile}") # Output: User 789's profile: {}

# You can also provide a more descriptive default value
city = users.get('user456', {}).get('profile', {}).get('city', 'Not specified')
print(f"Bob's city: {city}") # Output: Bob's city: London
```

---

## 3. Modifying Nested Dictionaries

You can add, update, or delete items at any level of a nested dictionary.

### a. Updating a Value

Use chained keys to pinpoint the value you want to change.

```python
# Change Alice's city to 'San Francisco'
users['user123']['profile']['city'] = 'San Francisco'
print(users['user123']['profile'])
# Output: {'age': 30, 'city': 'San Francisco', 'interests': ['coding', 'hiking']}
```

### b. Adding a New Key-Value Pair

You can add new keys to any dictionary in the structure.

```python
# Add a 'status' to Bob's profile
users['user456']['profile']['status'] = 'active'
print(users['user456']['profile'])
# Output: {'age': 25, 'city': 'London', 'interests': ['music', 'reading'], 'status': 'active'}
```

### c. Safely Adding with `.setdefault()`

If you're not sure whether a nested dictionary exists, `.setdefault()` is very useful. It returns the value for a key if it exists, or creates the key with a default value if it doesn't.

```python
# Add a 'settings' dictionary for a new user, 'user789'
# setdefault ensures the 'user789' key is created with an empty dict if it doesn't exist
user_settings = users.setdefault('user789', {}).setdefault('settings', {})
user_settings['theme'] = 'dark'

print(users['user789'])
# Output: {'settings': {'theme': 'dark'}}
```

### d. Deleting Items with `del`

The `del` keyword can remove any key-value pair.

```python
# Delete Bob's email
del users['user456']['email']
print(users['user456'])
# Output: {'name': 'Bob', 'profile': {'age': 25, 'city': 'London', 'interests': ['music', 'reading'], 'status': 'active'}}
```

---

## 4. Iterating Through Nested Dictionaries

Use nested loops or recursion to process all the data in a nested structure.

### a. Nested `for` Loops

This is ideal when you know the depth and structure of the dictionary.

```python
# Loop through each user and print their details
for user_id, user_info in users.items():
    print(f"\nProcessing User ID: {user_id}")

    name = user_info.get('name', 'N/A')
    print(f"  Name: {name}")

    # Safely access and iterate through the profile
    if 'profile' in user_info:
        profile_data = user_info['profile']
        for key, value in profile_data.items():
            print(f"    - {key.capitalize()}: {value}")
```

**Output:**

```
Processing User ID: user123
  Name: Alice
    - Age: 30
    - City: San Francisco
    - Interests: ['coding', 'hiking']

Processing User ID: user456
  Name: Bob
    - Age: 25
    - City: London
    - Interests: ['music', 'reading']
    - Status: active

Processing User ID: user789
  Name: N/A
```

### b. Recursive Iteration (Advanced)

For dictionaries with unknown or varying depth, a recursive function is a powerful solution.

```python
def print_nested_dict(d, indent=0):
    """Recursively prints the key-value pairs of a nested dictionary."""
    for key, value in d.items():
        if isinstance(value, dict):
            print('  ' * indent + f"{key}:")
            print_nested_dict(value, indent + 1)
        else:
            print('  ' * indent + f"{key}: {value}")

print_nested_dict(users)
```

**Output:**

```
user123:
  name: Alice
  email: alice@example.com
  profile:
    age: 30
    city: San Francisco
    interests: ['coding', 'hiking']
user456:
  name: Bob
  profile:
    age: 25
    city: London
    interests: ['music', 'reading']
    status: active
user789:
  settings:
    theme: dark
```

---

## 5. Built-in Functions and Methods

Python provides several built-in functions and dictionary methods that are essential for effective dictionary manipulation.

### a. Core Functions

- **`len(d)`**: Returns the number of key-value pairs in the dictionary.
- **`str(d)`**: Returns a string representation of the dictionary.

```python
print(f"Number of users: {len(users)}") # Output: Number of users: 3
```

### b. Essential Dictionary Methods

- **`.keys()`**: Returns a view object that displays a list of all the keys.
- **`.values()`**: Returns a view object that displays a list of all the values.
- **`.items()`**: Returns a view object that displays a list of key-value tuples.

These are particularly useful for iteration:

```python
# Get all user IDs (keys)
user_ids = users.keys()
print(f"User IDs: {user_ids}") # Output: dict_keys(['user123', 'user456', 'user789'])

# Get all user data (values)
# Note: .values() will return a view of the dictionaries, not the raw data inside them
all_user_data = users.values()

# Get all key-value pairs
all_items = users.items()
```

- **`.pop(key, default)`**: Removes the specified key and returns the corresponding value. If the key is not found, it returns the `default` value if provided, otherwise it raises a `KeyError`.

```python
# Remove a user and get their data
removed_user_data = users.pop('user789')
print(f"Removed user data: {removed_user_data}")
# Output: Removed user data: {'settings': {'theme': 'dark'}}
print(f"Remaining users: {len(users)}") # Output: Remaining users: 2
```

- **`.update(other_dict)`**: Merges the dictionary with another dictionary or with an iterable of key-value pairs. If a key already exists, its value is updated.

```python
# Add a new user and update an existing one
users.update({
    'user123': {
        'name': 'Alice Smith', # This will update the name
        'email': 'alice.smith@example.com',
        'profile': users['user123']['profile'] # Preserve existing profile
    },
    'user999': {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'profile': {}
    }
})

print(users['user123']['name']) # Output: Alice Smith
print(users['user999']) # Output: {'name': 'Charlie', 'email': 'charlie@example.com', 'profile': {}}
```

---

## 6. Common Patterns and Best Practices

### a. Lists of Dictionaries

A very common pattern is a list where each item is a dictionary. This is often used for query results from a database or API.

```python
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1200},
    {'id': 2, 'name': 'Mouse', 'price': 25},
    {'id': 3, 'name': 'Keyboard', 'price': 75}
]

# Find a product by name
for product in products:
    if product['name'] == 'Mouse':
        print(f"Found Mouse! Price: ${product['price']}")
        break
```

### b. Working with JSON

JSON (JavaScript Object Notation) is a standard data format that maps almost perfectly to Python dictionaries. The `json` module makes it easy to convert between them.

```python
import json

# Convert the 'users' dictionary to a JSON string (e.g., to send over a network)
json_string = json.dumps(users, indent=4)
# print(json_string)

# Convert a JSON string back into a Python dictionary
data = json.loads(json_string)
print(data['user123']['name']) # Output: Alice
```

### c. Use `copy.deepcopy` for Nested Structures

A standard `.copy()` is a _shallow_ copy. For nested dictionaries, this means the nested dictionaries are referenced, not copied. Modifying a nested dictionary in the copy will also modify the original. Use `copy.deepcopy()` to create a fully independent copy.

```python
import copy

users_copy = copy.deepcopy(users)

# Modify the copy
users_copy['user123']['profile']['city'] = 'Miami'

# The original remains unchanged
print(f"Original city: {users['user123']['profile']['city']}   # Output: Original city: San Francisco
print(f"Copied city: {users_copy['user123']['profile']['city']} # Output: Copied city: Miami
```
