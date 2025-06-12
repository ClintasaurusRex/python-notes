# Working with Dictionaries in Python

## Table of Contents

- [Introduction](#introduction)
- [Creating a Dictionary](#creating-a-dictionary)
- [Accessing Values](#accessing-values)
- [Adding and Modifying Entries](#adding-and-modifying-entries)
- [Removing Entries](#removing-entries)
- [Looping Through Dictionaries](#looping-through-dictionaries)
- [Dictionary Built-in Methods](#dictionary-built-in-methods)
  - [keys()](#keys)
  - [values()](#values)
  - [items()](#items)
  - [get()](#get)
  - [pop() and popitem()](#pop-and-popitem)
  - [update()](#update)
  - [clear()](#clear)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [Conclusion](#conclusion)

---

## Introduction

Dictionaries are a core data structure in Python that store key-value pairs. They are useful for fast lookups, organizing data, and mapping relationships between items.

---

## Creating a Dictionary

You can create a dictionary using curly braces `{}` with key-value pairs, or with the `dict()` constructor.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
empty_dict = {}
other = dict(animal="dog", color="brown")
```

---

## Accessing Values

Access values by their key. If the key does not exist, you'll get a `KeyError` unless you use `get()`.

```python
print(person["name"])  # Alice
print(person.get("age"))  # 30
print(person.get("height", "Not found"))  # Not found
```

---

## Adding and Modifying Entries

Assign a value to a key to add or update an entry.

```python
person["email"] = "alice@example.com"  # Add new key
person["age"] = 31  # Update existing key
```

---

## Removing Entries

Use `del`, `pop()`, or `popitem()` to remove entries.

```python
del person["city"]  # Remove by key
age = person.pop("age")  # Remove and return value
last = person.popitem()  # Remove and return last inserted pair (Python 3.7+)
```

---

## Looping Through Dictionaries

You can loop through keys, values, or key-value pairs.

```python
# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Dictionary Built-in Methods

### keys()

Returns a view of all keys in the dictionary.

```python
print(person.keys())
```

### values()

Returns a view of all values in the dictionary.

```python
print(person.values())
```

### items()

Returns a view of all key-value pairs as tuples.

```python
print(person.items())
```

### get()

Returns the value for a key if it exists, otherwise returns a default value.

```python
print(person.get("name", "Unknown"))
```

### pop() and popitem()

Removes a key and returns its value, or removes and returns the last inserted key-value pair.

```python
person.pop("name")
person.popitem()
```

### update()

Updates the dictionary with key-value pairs from another dictionary or iterable.

```python
person.update({"country": "USA"})
```

### clear()

Removes all items from the dictionary.

```python
person.clear()
```

---

## Dictionary Comprehensions

A concise way to create dictionaries from sequences or other dictionaries.

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Conclusion

Dictionaries are essential for mapping and organizing data in Python. Mastering their methods and operations will make your code more efficient and expressive.
