# Python Sequence Operators: Complete Tutorial and Problem-Solving Guide

## Table of Contents

1. [Introduction to Sequence Operators](#introduction-to-sequence-operators)
2. [Basic Sequence Operators](#basic-sequence-operators)
3. [Indexing and Slicing Operators](#indexing-and-slicing-operators)
4. [Membership Operators](#membership-operators)
5. [Concatenation and Repetition](#concatenation-and-repetition)
6. [Comparison Operators](#comparison-operators)
7. [Problem-Solving Patterns](#problem-solving-patterns)
8. [Advanced Techniques](#advanced-techniques)
9. [Performance Considerations](#performance-considerations)
10. [Best Practices](#best-practices)

---

## Introduction to Sequence Operators

Sequence operators in Python are powerful tools that work with ordered collections like lists, tuples, strings, and ranges. They allow you to manipulate, access, and analyze sequences efficiently.

**Common Python Sequences:**
- Lists: `[1, 2, 3, 4, 5]`
- Tuples: `(1, 2, 3, 4, 5)`
- Strings: `"hello world"`
- Ranges: `range(1, 6)`

## Basic Sequence Operators

### Length Operator: `len()`

```python
# Finding length of different sequences
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

text = "Hello World"
print(len(text))     # 11

coordinates = (10, 20, 30)
print(len(coordinates))  # 3

# Problem: Check if list is empty
def is_empty(sequence):
    return len(sequence) == 0

print(is_empty([]))     # True
print(is_empty([1, 2])) # False
```

### Index Access: `sequence[index]`

```python
# Basic indexing
fruits = ["apple", "banana", "cherry", "date"]

# Positive indexing (0-based)
print(fruits[0])   # "apple"
print(fruits[2])   # "cherry"

# Negative indexing (from end)
print(fruits[-1])  # "date"
print(fruits[-2])  # "cherry"

# Problem: Get first and last elements safely
def get_first_last(sequence):
    if len(sequence) == 0:
        return None, None
    elif len(sequence) == 1:
        return sequence[0], sequence[0]
    else:
        return sequence[0], sequence[-1]

print(get_first_last([1, 2, 3, 4]))  # (1, 4)
print(get_first_last([5]))           # (5, 5)
print(get_first_last([]))            # (None, None)
```

## Indexing and Slicing Operators

### Basic Slicing: `sequence[start:end:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing patterns
print(numbers[2:6])    # [2, 3, 4, 5] - from index 2 to 5
print(numbers[:5])     # [0, 1, 2, 3, 4] - from start to index 4
print(numbers[5:])     # [5, 6, 7, 8, 9] - from index 5 to end
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - full copy

# Negative slicing
print(numbers[-3:])    # [7, 8, 9] - last 3 elements
print(numbers[:-2])    # [0, 1, 2, 3, 4, 5, 6, 7] - all except last 2

# Step slicing
print(numbers[::2])    # [0, 2, 4, 6, 8] - every 2nd element
print(numbers[1::2])   # [1, 3, 5, 7, 9] - every 2nd, starting from 1
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reverse
```

### Advanced Slicing Patterns

```python
data = list(range(20))  # [0, 1, 2, ..., 19]

# Complex slicing combinations
print(data[2:15:3])    # [2, 5, 8, 11, 14] - every 3rd from 2 to 14
print(data[10:2:-2])   # [10, 8, 6, 4] - backwards with step 2
print(data[-5:-1])     # [15, 16, 17, 18] - slice near the end

# Problem: Extract every nth element starting from position m
def extract_pattern(sequence, start, step):
    return sequence[start::step]

numbers = list(range(100))
print(extract_pattern(numbers, 5, 7))  # Every 7th element starting from 5

# Problem: Get middle elements
def get_middle(sequence):
    length = len(sequence)
    if length % 2 == 0:
        # Even length: return middle two elements
        mid = length // 2
        return sequence[mid-1:mid+1]
    else:
        # Odd length: return middle element
        mid = length // 2
        return sequence[mid:mid+1]

print(get_middle([1, 2, 3, 4]))     # [2, 3]
print(get_middle([1, 2, 3, 4, 5]))  # [3]
```

### Slice Assignment (Lists Only)

```python
# Replacing elements with slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Replace a section
numbers[2:5] = [20, 30, 40]
print(numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Insert elements
numbers[3:3] = [25, 35]
print(numbers)  # [0, 1, 20, 25, 35, 30, 40, 5, 6, 7, 8, 9]

# Delete elements
numbers[2:6] = []
print(numbers)  # [0, 1, 30, 40, 5, 6, 7, 8, 9]

# Replace with step
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] = [10, 30, 50, 70, 90]
print(numbers)  # [10, 1, 30, 3, 50, 5, 70, 7, 90, 9]
```

## Membership Operators

### `in` and `not in` Operators

```python
# Basic membership testing
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)     # True
print("grape" in fruits)     # False
print("grape" not in fruits) # True

# String membership
text = "Hello World"
print("World" in text)   # True
print("world" in text)   # False (case sensitive)
print("xyz" not in text) # True

# Problem: Check if all items exist
def all_items_exist(items, container):
    return all(item in container for item in items)

shopping_list = ["milk", "bread", "eggs"]
available = ["milk", "bread", "eggs", "cheese", "butter"]
print(all_items_exist(shopping_list, available))  # True

# Problem: Filter items based on membership
def filter_existing(items, valid_items):
    return [item for item in items if item in valid_items]

user_input = ["apple", "grape", "banana", "kiwi"]
available_fruits = ["apple", "banana", "cherry"]
result = filter_existing(user_input, available_fruits)
print(result)  # ['apple', 'banana']
```

### Advanced Membership Patterns

```python
# Case-insensitive membership
def case_insensitive_in(item, container):
    return item.lower() in [x.lower() for x in container]

fruits = ["Apple", "Banana", "Cherry"]
print(case_insensitive_in("apple", fruits))  # True

# Partial membership (substring)
def contains_substring(substring, strings):
    return [s for s in strings if substring in s]

words = ["python", "programming", "computer", "science"]
result = contains_substring("pro", words)
print(result)  # ['programming']

# Multiple membership checks
def count_matches(items, container):
    return sum(1 for item in items if item in container)

search_items = ["a", "e", "i", "o", "u"]
text = "Hello World"
vowel_count = count_matches(search_items, text.lower())
print(vowel_count)  # 3
```

## Concatenation and Repetition

### Concatenation Operator: `+`

```python
# Basic concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# String concatenation
greeting = "Hello" + " " + "World"
print(greeting)  # "Hello World"

# Tuple concatenation
coords1 = (1, 2)
coords2 = (3, 4)
all_coords = coords1 + coords2
print(all_coords)  # (1, 2, 3, 4)

# Problem: Merge multiple lists
def merge_lists(*lists):
    result = []
    for lst in lists:
        result = result + lst
    return result

list_a = [1, 2]
list_b = [3, 4]
list_c = [5, 6]
merged = merge_lists(list_a, list_b, list_c)
print(merged)  # [1, 2, 3, 4, 5, 6]
```

### Repetition Operator: `*`

```python
# Basic repetition
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

dashes = "-" * 10
print(dashes)  # "----------"

# Problem: Create multiplication table
def create_row(number, length):
    return [number] * length

row_of_threes = create_row(3, 4)
print(row_of_threes)  # [3, 3, 3, 3]

# Problem: Create pattern strings
def create_pattern(char, count, separator=" "):
    return separator.join([char] * count)

pattern = create_pattern("*", 5)
print(pattern)  # "* * * * *"

# Problem: Initialize 2D list (be careful with references!)
def create_2d_list(rows, cols, default=0):
    # Correct way - each row is a separate list
    return [[default] * cols for _ in range(rows)]

matrix = create_2d_list(3, 4)
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# Wrong way - all rows reference the same list!
# wrong_matrix = [[0] * 4] * 3  # Don't do this!
```

### Advanced Concatenation and Repetition

```python
# Conditional concatenation
def smart_join(list1, list2, condition):
    if condition:
        return list1 + list2
    else:
        return list2 + list1

result = smart_join([1, 2], [3, 4], True)
print(result)  # [1, 2, 3, 4]

# Variable repetition
def create_pyramid(height):
    pyramid = []
    for i in range(1, height + 1):
        row = "*" * i
        pyramid.append(row)
    return pyramid

pyramid = create_pyramid(5)
for row in pyramid:
    print(row)
# Output:
# *
# **
# ***
# ****
# *****

# Alternating patterns
def alternating_pattern(pattern1, pattern2, count):
    result = []
    for i in range(count):
        if i % 2 == 0:
            result.extend(pattern1)
        else:
            result.extend(pattern2)
    return result

pattern = alternating_pattern([1, 2], [3, 4], 4)
print(pattern)  # [1, 2, 3, 4, 1, 2, 3, 4]
```

## Comparison Operators

### Basic Comparisons

```python
# List comparisons
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)  # True - same elements in same order
print(list1 == list3)  # False - different elements
print(list1 < list3)   # True - lexicographic comparison

# String comparisons
print("apple" < "banana")  # True - alphabetical order
print("Apple" < "apple")   # True - uppercase comes first in ASCII

# Tuple comparisons
coord1 = (1, 2)
coord2 = (1, 3)
coord3 = (2, 1)
print(coord1 < coord2)  # True - first element same, second element smaller
print(coord1 < coord3)  # True - first element smaller
```

### Advanced Comparison Patterns

```python
# Problem: Sort by multiple criteria
def sort_by_criteria(items):
    # Sort by length first, then alphabetically
    return sorted(items, key=lambda x: (len(x), x))

words = ["cat", "elephant", "dog", "ant", "bear"]
sorted_words = sort_by_criteria(words)
print(sorted_words)  # ['ant', 'cat', 'dog', 'bear', 'elephant']

# Problem: Find lexicographically largest/smallest
def find_extremes(sequences):
    if not sequences:
        return None, None
    return min(sequences), max(sequences)

lists = [[1, 2], [1, 3], [0, 5], [2, 1]]
smallest, largest = find_extremes(lists)
print(f"Smallest: {smallest}, Largest: {largest}")  # [0, 5], [2, 1]

# Problem: Check if sequence is sorted
def is_sorted(sequence, reverse=False):
    if reverse:
        return sequence == sorted(sequence, reverse=True)
    else:
        return sequence == sorted(sequence)

print(is_sorted([1, 2, 3, 4]))     # True
print(is_sorted([4, 3, 2, 1], True))  # True
print(is_sorted([1, 3, 2, 4]))     # False
```

## Problem-Solving Patterns

### Pattern 1: Data Extraction and Filtering

```python
# Problem: Extract specific elements based on position
def extract_positions(data, positions):
    """Extract elements at specific positions"""
    return [data[i] for i in positions if 0 <= i < len(data)]

numbers = [10, 20, 30, 40, 50, 60, 70]
positions = [0, 2, 4, 6, 10]  # Note: position 10 doesn't exist
result = extract_positions(numbers, positions)
print(result)  # [10, 30, 50, 70]

# Problem: Get every nth element with offset
def get_pattern_elements(sequence, offset, step):
    """Get every step-th element starting from offset"""
    return sequence[offset::step]

data = list(range(20))
every_third_from_2 = get_pattern_elements(data, 2, 3)
print(every_third_from_2)  # [2, 5, 8, 11, 14, 17]

# Problem: Split sequence into chunks
def chunk_sequence(sequence, chunk_size):
    """Split sequence into chunks of specified size"""
    chunks = []
    for i in range(0, len(sequence), chunk_size):
        chunks.append(sequence[i:i + chunk_size])
    return chunks

numbers = list(range(15))
chunks = chunk_sequence(numbers, 4)
print(chunks)  # [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14]]
```

### Pattern 2: Sequence Manipulation

```python
# Problem: Rotate sequence left or right
def rotate_sequence(sequence, positions, direction='left'):
    """Rotate sequence by specified positions"""
    if not sequence:
        return sequence
    
    length = len(sequence)
    positions = positions % length
    
    if direction == 'left':
        return sequence[positions:] + sequence[:positions]
    else:  # right
        return sequence[-positions:] + sequence[:-positions]

data = [1, 2, 3, 4, 5, 6, 7]
rotated_left = rotate_sequence(data, 2, 'left')
rotated_right = rotate_sequence(data, 2, 'right')
print(f"Original: {data}")
print(f"Rotated left 2: {rotated_left}")   # [3, 4, 5, 6, 7, 1, 2]
print(f"Rotated right 2: {rotated_right}") # [6, 7, 1, 2, 3, 4, 5]

# Problem: Interleave two sequences
def interleave_sequences(seq1, seq2):
    """Interleave elements from two sequences"""
    result = []
    min_length = min(len(seq1), len(seq2))
    
    # Interleave common length
    for i in range(min_length):
        result.append(seq1[i])
        result.append(seq2[i])
    
    # Add remaining elements
    result.extend(seq1[min_length:])
    result.extend(seq2[min_length:])
    
    return result

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6]
interleaved = interleave_sequences(list1, list2)
print(interleaved)  # [1, 2, 3, 4, 5, 6, 7, 9]

# Problem: Remove duplicates while preserving order
def remove_duplicates_ordered(sequence):
    """Remove duplicates while preserving original order"""
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

data_with_dupes = [1, 2, 3, 2, 4, 1, 5, 3]
unique_ordered = remove_duplicates_ordered(data_with_dupes)
print(unique_ordered)  # [1, 2, 3, 4, 5]
```

### Pattern 3: Sequence Analysis

```python
# Problem: Find all indices of an element
def find_all_indices(sequence, target):
    """Find all indices where target appears"""
    return [i for i, item in enumerate(sequence) if item == target]

data = [1, 2, 3, 2, 4, 2, 5]
indices = find_all_indices(data, 2)
print(indices)  # [1, 3, 5]

# Problem: Find longest increasing subsequence
def longest_increasing_subsequence(sequence):
    """Find the longest increasing subsequence"""
    if not sequence:
        return []
    
    current_seq = [sequence[0]]
    longest_seq = [sequence[0]]
    
    for i in range(1, len(sequence)):
        if sequence[i] > current_seq[-1]:
            current_seq.append(sequence[i])
        else:
            if len(current_seq) > len(longest_seq):
                longest_seq = current_seq[:]
            current_seq = [sequence[i]]
    
    if len(current_seq) > len(longest_seq):
        longest_seq = current_seq
    
    return longest_seq

numbers = [1, 3, 2, 4, 5, 1, 6, 7, 8]
lis = longest_increasing_subsequence(numbers)
print(lis)  # [1, 6, 7, 8]

# Problem: Check if sequence is palindrome
def is_palindrome(sequence):
    """Check if sequence reads the same forwards and backwards"""
    return sequence == sequence[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # True
print(is_palindrome("racecar"))        # True
print(is_palindrome([1, 2, 3, 4]))     # False
```

### Pattern 4: Window Operations

```python
# Problem: Sliding window maximum
def sliding_window_max(sequence, window_size):
    """Find maximum in each sliding window"""
    if window_size > len(sequence):
        return [max(sequence)] if sequence else []
    
    result = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        result.append(max(window))
    return result

numbers = [1, 3, 2, 5, 4, 6, 1, 7]
window_maxes = sliding_window_max(numbers, 3)
print(window_maxes)  # [3, 5, 5, 6, 6, 7]

# Problem: Moving average
def moving_average(sequence, window_size):
    """Calculate moving average with specified window size"""
    if window_size > len(sequence):
        return [sum(sequence) / len(sequence)] if sequence else []
    
    result = []
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        result.append(sum(window) / window_size)
    return result

prices = [10, 12, 13, 12, 15, 16, 14, 13]
avg_prices = moving_average(prices, 3)
print([round(avg, 2) for avg in avg_prices])  # [11.67, 12.33, 13.33, 14.33, 15.0, 14.33]

# Problem: Find all substrings of length k
def all_substrings(sequence, length):
    """Find all contiguous subsequences of specified length"""
    result = []
    for i in range(len(sequence) - length + 1):
        result.append(sequence[i:i + length])
    return result

text = "programming"
substrings = all_substrings(text, 4)
print(substrings)  # ['prog', 'rogr', 'ogra', 'gram', 'ramm', 'ammi', 'mmin', 'ming']
```

## Advanced Techniques

### Working with Nested Sequences

```python
# Problem: Flatten nested lists
def flatten_list(nested_list):
    """Flatten a nested list structure"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], 7]
flattened = flatten_list(nested)
print(flattened)  # [1, 2, 3, 4, 5, 6, 7]

# Problem: Transpose matrix (2D list)
def transpose_matrix(matrix):
    """Transpose a 2D matrix"""
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    return transposed

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = transpose_matrix(matrix)
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Using zip for transpose (more Pythonic)
def transpose_with_zip(matrix):
    return [list(row) for row in zip(*matrix)]

transposed_zip = transpose_with_zip(matrix)
print(transposed_zip)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### String Sequence Operations

```python
# Problem: Find common prefix
def longest_common_prefix(strings):
    """Find the longest common prefix among strings"""
    if not strings:
        return ""
    
    prefix = ""
    for i in range(len(strings[0])):
        char = strings[0][i]
        if all(i < len(s) and s[i] == char for s in strings):
            prefix += char
        else:
            break
    
    return prefix

words = ["programming", "program", "progress"]
prefix = longest_common_prefix(words)
print(prefix)  # "progr"

# Problem: Word pattern matching
def matches_pattern(pattern, words):
    """Check if words match a pattern (a=first word, b=second word, etc.)"""
    if len(pattern) != len(words):
        return False
    
    char_to_word = {}
    word_to_char = {}
    
    for char, word in zip(pattern, words):
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    
    return True

pattern = "abba"
words = ["dog", "cat", "cat", "dog"]
print(matches_pattern(pattern, words))  # True

# Problem: Run-length encoding
def run_length_encode(sequence):
    """Encode sequence using run-length encoding"""
    if not sequence:
        return []
    
    result = []
    current_item = sequence[0]
    count = 1
    
    for i in range(1, len(sequence)):
        if sequence[i] == current_item:
            count += 1
        else:
            result.append((current_item, count))
            current_item = sequence[i]
            count = 1
    
    result.append((current_item, count))
    return result

data = "aaabbccccaa"
encoded = run_length_encode(data)
print(encoded)  # [('a', 3), ('b', 2), ('c', 4), ('a', 2)]
```

### Memory-Efficient Operations

```python
# Problem: Process large sequences without loading entirely
def process_large_sequence_chunks(sequence, chunk_size, processor):
    """Process large sequence in chunks to save memory"""
    results = []
    for i in range(0, len(sequence), chunk_size):
        chunk = sequence[i:i + chunk_size]
        result = processor(chunk)
        results.append(result)
    return results

def sum_chunk(chunk):
    return sum(chunk)

large_numbers = list(range(1000))
chunk_sums = process_large_sequence_chunks(large_numbers, 100, sum_chunk)
print(len(chunk_sums))  # 10 chunks
print(chunk_sums[:3])   # First 3 chunk sums

# Problem: Generator-based sequence operations
def sliding_window_generator(sequence, window_size):
    """Memory-efficient sliding window using generator"""
    for i in range(len(sequence) - window_size + 1):
        yield sequence[i:i + window_size]

# Usage with generator
numbers = list(range(20))
for window in sliding_window_generator(numbers, 5):
    print(f"Window: {window}, Sum: {sum(window)}")
    if sum(window) > 50:  # Process until condition
        break
```

## Performance Considerations

### Time Complexity of Sequence Operations

```python
import time

# Demonstrate performance differences
def timing_comparison():
    large_list = list(range(100000))
    
    # O(1) operations
    start = time.time()
    _ = large_list[50000]  # Index access
    index_time = time.time() - start
    
    start = time.time()
    _ = large_list[-1]  # Last element
    last_time = time.time() - start
    
    # O(n) operations
    start = time.time()
    _ = 50000 in large_list  # Membership test
    membership_time = time.time() - start
    
    start = time.time()
    _ = large_list + [1]  # Concatenation
    concat_time = time.time() - start
    
    print(f"Index access: {index_time:.8f}s")
    print(f"Last element: {last_time:.8f}s")
    print(f"Membership test: {membership_time:.6f}s")
    print(f"Concatenation: {concat_time:.6f}s")

# timing_comparison()

# Efficient vs inefficient patterns
def inefficient_concatenation(lists):
    """Inefficient: O(n²) complexity"""
    result = []
    for lst in lists:
        result = result + lst  # Creates new list each time
    return result

def efficient_concatenation(lists):
    """Efficient: O(n) complexity"""
    result = []
    for lst in lists:
        result.extend(lst)  # Modifies existing list
    return result

# Or even better with sum()
def best_concatenation(lists):
    """Most efficient for this specific case"""
    return sum(lists, [])
```

### Memory Optimization

```python
# Problem: Memory-efficient sequence processing
def memory_efficient_processing():
    # Instead of storing all intermediate results
    def inefficient_way(sequence):
        doubled = [x * 2 for x in sequence]
        filtered = [x for x in doubled if x > 10]
        squared = [x ** 2 for x in filtered]
        return squared
    
    # Use generator expressions for large data
    def efficient_way(sequence):
        return [x ** 2 for x in (x * 2 for x in sequence) if x * 2 > 10]
    
    # Or use itertools for even better memory efficiency
    import itertools
    
    def most_efficient_way(sequence):
        doubled = map(lambda x: x * 2, sequence)
        filtered = filter(lambda x: x > 10, doubled)
        squared = map(lambda x: x ** 2, filtered)
        return list(squared)  # Only convert to list if needed
    
    test_data = range(1000)
    result1 = inefficient_way(test_data)
    result2 = efficient_way(test_data)
    result3 = most_efficient_way(test_data)
    
    print(f"All results equal: {result1 == result2 == result3}")

# memory_efficient_processing()
```

## Best Practices

### 1. Choose the Right Operation

```python
# Good practices for different scenarios

# For membership testing with large sequences, use sets
def efficient_membership_check():
    large_list = list(range(10000))
    large_set = set(large_list)
    
    # Slow: O(n) for each check
    # result = [x for x in [5000, 7500, 9999] if x in large_list]
    
    # Fast: O(1) for each check
    result = [x for x in [5000, 7500, 9999] if x in large_set]
    return result

# For frequent indexing, prefer lists over strings
def string_vs_list_indexing():
    text = "This is a long string for testing"
    text_list = list(text)
    
    # Multiple indexing operations are faster on lists
    indices = [0, 5, 10, 15, 20, 25, 30]
    
    # String indexing (slower for many operations)
    chars_from_string = [text[i] for i in indices if i < len(text)]
    
    # List indexing (faster for many operations)
    chars_from_list = [text_list[i] for i in indices if i < len(text_list)]
    
    return chars_from_string == chars_from_list  # Should be True
```

### 2. Error Handling

```python
# Safe sequence operations with error handling
def safe_sequence_operations():
    def safe_index(sequence, index, default=None):
        """Safely access sequence element by index"""
        try:
            return sequence[index]
        except IndexError:
            return default
    
    def safe_slice(sequence, start=None, end=None, step=None):
        """Safely slice sequence with bounds checking"""
        length = len(sequence)
        
        # Handle negative indices and out-of-bounds
        if start is not None and start < 0:
            start = max(0, length + start)
        if end is not None and end < 0:
            end = max(0, length + end)
        
        return sequence[start:end:step]
    
    def safe_find(sequence, target, default=-1):
        """Safely find index of element"""
        try:
            return sequence.index(target)
        except ValueError:
            return default
    
    # Examples
    data = [1, 2, 3, 4, 5]
    print(safe_index(data, 10, "Not found"))  # "Not found"
    print(safe_slice(data, -10, 10))          # [1, 2, 3, 4, 5]
    print(safe_find(data, 6))                 # -1

safe_sequence_operations()
```

### 3. Readable Code Patterns

```python
# Write clear and maintainable sequence operations
def readable_patterns():
    # Use descriptive variable names for slicing
    def extract_header_body_footer(data):
        HEADER_SIZE = 3
        FOOTER_SIZE = 2
        
        if len(data) < HEADER_SIZE + FOOTER_SIZE:
            return data, [], []
        
        header = data[:HEADER_SIZE]
        footer = data[-FOOTER_SIZE:]
        body = data[HEADER_SIZE:-FOOTER_SIZE]
        
        return header, body, footer
    
    # Use named constants for magic numbers
    CHUNK_SIZE = 4
    OVERLAP = 1
    
    def overlapping_chunks(sequence):
        step = CHUNK_SIZE - OVERLAP
        chunks = []
        for i in range(0, len(sequence) - OVERLAP, step):
            chunk = sequence[i:i + CHUNK_SIZE]
            if len(chunk) == CHUNK_SIZE:
                chunks.append(chunk)
        return chunks
    
    # Example usage
    test_data = list(range(20))
    header, body, footer = extract_header_body_footer(test_data)
    print(f"Header: {header}")
    print(f"Body length: {len(body)}")
    print(f"Footer: {footer}")
    
    chunks = overlapping_chunks(test_data)
    print(f"Overlapping chunks: {chunks[:3]}...")  # Show first 3

readable_patterns()
```

## Summary

Sequence operators in Python are powerful tools for manipulating ordered data. Key takeaways:

1. **Indexing and Slicing**: Master `[start:end:step]` syntax for flexible data access
2. **Membership Testing**: Use `in` and `not in` for efficient searching
3. **Concatenation and Repetition**: Combine sequences with `+` and `*`
4. **Performance**: Consider time complexity and memory usage for large datasets
5. **Error Handling**: Implement safe operations for robust code
6. **Readability**: Use descriptive names and constants for maintainable code

Practice these patterns with different sequence types (lists, tuples, strings) to become proficient in Python sequence manipulation!
