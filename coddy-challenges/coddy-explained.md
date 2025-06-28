# Coddy Explained – Organized Solutions with Explanations

---

## 1. Sum of Digits

### Solution 1

```python
def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    print(total)
```

**Why?**

- Numbers like `123` are stored as a single value in Python.
- If you want to work with each digit (`1`, `2`, `3`), you need a way to separate them.
- When you convert the number to a string (`str(123)` becomes `'123'`), each digit becomes a character in the string.
- You can then loop through the string and process each digit individually.
- `int(digit)` converts the character back to an integer so you can add it to the total.

---

### Solution 2 (List Comprehension)

```python
def sum_of_digits(num):
    split = sum(int(d) for d in str(num))
    print(split)
```

**Why?**

- This uses a generator expression: `int(d) for d in str(num)` creates each digit as an integer.
- `sum(...)` adds up all those digits.
- This is a more concise way to do the same thing as the first solution.

**Example Usage:**

```python
sum_of_digits(123)  # Output: 6
```

---

## 2. Looping with Range (Commented Example)

```python
for i in range(20, 9, -2):
    print(i)
```

**Why?**

- `range(20, 9, -2)` starts at 20, stops before 9, and steps down by 2 each time.
- This would print: 20, 18, 16, 14, 12, 10.

---

## 3. Summing User Input Numbers

```python
n = int(input())
res = 0
print('-------------------------------------------')
for i in range(n):
    a = int(input())
    res += a
print(res)
```

**Why?**

- Asks the user how many numbers they want to sum (`n`).
- Loops `n` times, each time asking for a number and adding it to `res`.
- Prints the total sum at the end.

---

## 4. Sum Numbers from 1 to 10,000

```python
def sum_numbers():
    sum = 0
    for i in range(1, 10001):
        sum += i
    print(sum)
```

**Why?**

- Loops from 1 to 10,000 (inclusive).
- Adds each number to `sum`.
- Prints the total, which is the sum of the first 10,000 natural numbers.

---

## 5. FizzBuzz

```python
print("product sum----------------")
print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    for i in range(1, num + 1):  # include 'num' itself
        if i % 3 == 0 and i % 7 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 7 == 0:
            print("Buzz")
        else:
            print(i)

number = int(input())
fizzbuzz(number)
```

**Why?**

- Loops from 1 to the user’s number.
- Prints "FizzBuzz" if the number is divisible by both 3 and 7.
- Prints "Fizz" if divisible by 3, "Buzz" if divisible by 7.
- Otherwise, prints the number itself.
- Classic programming exercise for practicing conditionals and loops.

---

## 6. Change Element in a List

### Version 1: Replace Element at Index

```python
def change_element(lst, index, new_element):
    # Make a copy to avoid changing the original list
    modified_list = lst.copy()
    # Change the element at the given index
    modified_list[index] = new_element
    return modified_list

# Example usage:
result = change_element([1, 2, 3], 0, 9)
print(result)  # Output: [9, 2, 3]
```

**Why?**

- Copies the list so the original isn’t changed.
- Updates the element at the specified index.
- Returns the modified list.

---

### Version 2: Replace with First Element from Another List

```python
def change_element(list1, index, list2):
    modified_list1 = list1.copy()
    modified_list2 = list2.copy()
    modified_list1[index] = modified_list2[0]
    return modified_list1

# Example usage:
result = change_element([1, 2, 3], 1, [5, 6, 7])
print(result)  # Output: [1, 5, 3]
```

**Why?**

- Copies both lists to avoid changing the originals.
- Replaces the element at the given index in the first list with the **first element** from the second list.
- Returns the modified list.

---

## 7. Product of Numbers in a List

```python
def prod(lst):
    product = 1
    for num in lst:
        product *= num
    print(product)

prod([1, 2, 3])  # Output: 6
```

**What is this code doing?**

- Defines a function `prod` that takes a list of numbers as input.
- Initializes a variable `product` to 1.
- Loops through each number in the list (`for num in lst:`).
- Multiplies `product` by each number in the list (`product *= num`).
- After the loop, prints the final product.
- For the example `[1, 2, 3]`, it calculates `1 * 2 * 3 = 6` and prints `6`.

**Why do we start with 1 when finding the product?**

- If you start with 0, any number multiplied by 0 is 0, so the result would always be 0.
- 1 is the **multiplicative identity**: multiplying by 1 does not change the value of the other number.
- Starting with 1 ensures the product is correct, just like how you start with 0 when adding numbers (since 0 is the additive identity).

**Summary:**

- This function multiplies all the numbers in a list together.
- Initializing the product as 1 is essential for correct multiplication.

---

## 8. Reversing a List Using Slicing

```python
def reversed(lst):
    print(lst[::-1])

reversed([1, 2, 3])  # Output: [3, 2, 1]
```

**What is this code doing?**

- Defines a function `reversed` that takes a list as input.
- Uses slicing with `[::-1]` to create a new list that is the reverse of the original.
- Prints the reversed list.
- For the example `[1, 2, 3]`, it outputs `[3, 2, 1]`.

**Why does `lst[::-1]` reverse the list?**

- The slicing syntax `lst[start:stop:step]` allows you to extract parts of a list.
- When you use `[::-1]`, you are telling Python:
  - Start from the end of the list and move backwards (step is -1).
  - This creates a new list with all the elements in reverse order.
- No need for a loop or extra code—Python handles the reversal efficiently with slicing.

**Summary:**

- Slicing with `[::-1]` is a quick and Pythonic way to reverse a list.
- It works for any list, regardless of its contents or length.

---

## 9. Finding Indices Based on Conditions

```python
lst = list(map(int, input().split(",")))
# Write your code below
indices = []
for index, num in enumerate(lst):
    if num < 50 or num % 5 == 0:
        indices.append(index)
print(indices)
```

**What is this code doing?**

- Gets comma-separated numbers from user input and converts them to a list of integers.
- Creates an empty list called `indices` to store the positions of numbers that meet our criteria.
- Uses `enumerate()` to loop through the list, getting both the index (position) and the number at each position.
- Checks if each number is either less than 50 OR divisible by 5.
- If the condition is met, adds the index (position) to our `indices` list.
- Prints the final list of indices.

**Why does this work?**

- `input().split(",")` takes user input like "2,4,6,8,10" and splits it into a list of strings: `["2", "4", "6", "8", "10"]`.
- `map(int, ...)` converts each string to an integer: `[2, 4, 6, 8, 10]`.
- `list(...)` converts the map object to a proper list.
- `enumerate(lst)` gives us pairs of (index, value): `(0, 2), (1, 4), (2, 6), (3, 8), (4, 10)`.
- `num < 50 or num % 5 == 0` checks if the number meets either condition (less than 50 OR divisible by 5).
- `indices.append(index)` adds the position (not the number itself) to our results list.

**Example walkthrough:**

For input "2,4,6,8,10":

- Index 0, number 2: 2 < 50 ✓ → add index 0
- Index 1, number 4: 4 < 50 ✓ → add index 1
- Index 2, number 6: 6 < 50 ✓ → add index 2
- Index 3, number 8: 8 < 50 ✓ → add index 3
- Index 4, number 10: 10 < 50 ✓ and 10 % 5 == 0 ✓ → add index 4

Output: `[0, 1, 2, 3, 4]`

**Summary:**

- This program finds the positions (indices) of numbers that are either below 50 or divisible by 5.
- It returns the indices, not the actual numbers themselves.

---

## 10. Advanced List Slicing Programs

These are four different programs that demonstrate various list slicing techniques and conditional logic for processing user input.

---

### Program 1: Four Different Slicing Operations

**Problem Description:**
Create a program that receives a list as input and prints four new lists based on specific slicing operations.

```python
# Create a program that receives a list as input and prints four new lists based on the following slicing operations:

# A list containing every fourth element, starting from index 2
# A list containing all elements from the 3rd element to the 3rd to last element
# A list containing every element in reverse order, skipping every other element
# A list containing the first three and last three elements of the original list
# Name the lists list1, list2, list3 and list4 - accordingly.

original_list = input().split(',')  # Get input and split by commas
# Write your code below
list1 = original_list[2::4]          # Every 4th element starting from index 2
list2 = original_list[2:-2]          # From 3rd element to 3rd-to-last
list3 = original_list[::-2]          # Reverse order, every other element
list4 = original_list[:3] + original_list[-3:]  # First 3 + last 3

# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)
```

**How Each Slice Works:**

1. **`list1 = original_list[2::4]`**

   - **Start:** Index 2 (3rd element)
   - **Step:** 4 (every 4th element)
   - **Example:** With `[a,b,c,d,e,f,g,h,i,j]` → Gets `[c,g]`

2. **`list2 = original_list[2:-2]`**

   - **Start:** Index 2 (3rd element)
   - **End:** -2 (up to but not including 2nd-to-last)
   - **Example:** With `[a,b,c,d,e,f,g,h,i,j]` → Gets `[c,d,e,f,g,h]`

3. **`list3 = original_list[::-2]`**

   - **Start:** End of list (omitted with negative step)
   - **Step:** -2 (every other element, backwards)
   - **Example:** With `[a,b,c,d,e,f,g,h,i,j]` → Gets `[j,h,f,d,b]`

4. **`list4 = original_list[:3] + original_list[-3:]`**
   - **First part:** `[:3]` gets first 3 elements
   - **Second part:** `[-3:]` gets last 3 elements
   - **Concatenation:** Combines both parts
   - **Example:** With `[a,b,c,d,e,f,g,h,i,j]` → Gets `[a,b,c,h,i,j]`

**Example Input/Output:**

```
Input: "1,2,3,4,5,6,7,8,9,10"
Output:
List 1: ['3', '7']
List 2: ['3', '4', '5', '6', '7', '8']
List 3: ['10', '8', '6', '4', '2']
List 4: ['1', '2', '3', '8', '9', '10']
```

---

### Program 2: Three Slicing Operations with Middle Calculation

**Problem Description:**
Create a program that receives a list as input and prints three new lists based on specific slicing operations including middle calculation.

```python
# Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:

# A list containing every third element, starting from index 1 (the second element)
# A list containing all the elements from the 6th element to the 1st in reverse order
# A list containing every second element starting from the middle of the list to the end

lst = input().split(",")  # Get input and split by commas

# Every third element starting from index 1 (2nd element)
lst1 = lst[1::3]
print(lst1)

# From 6th element (index 5) to 1st element (index 0) in reverse
lst2 = lst[6::-1]  # Note: This starts from 7th element (index 6)
print(lst2)

# Calculate middle point and get every 2nd element from there to end
middle = len(lst) // 2  # Integer division to find middle index
lst3 = lst[middle::2]   # From middle to end, every 2nd element
print(lst3)
```

**How Each Operation Works:**

1. **`lst1 = lst[1::3]`**

   - **Start:** Index 1 (2nd element)
   - **Step:** 3 (every 3rd element)
   - **Why index 1?** "Starting from index 1" means the second element (0-based indexing)

2. **`lst2 = lst[6::-1]`**

   - **Start:** Index 6 (7th element)
   - **End:** Beginning of list
   - **Step:** -1 (reverse order)
   - **Note:** This actually starts from the 7th element, not 6th as described

3. **`lst3 = lst[middle::2]`**
   - **Middle calculation:** `len(lst) // 2` finds the middle index
   - **From middle to end:** Every 2nd element
   - **Dynamic:** Middle changes based on list length

**Example Input/Output:**

```
Input: "1,2,3,4,5,6,7,8,9,10"
Output:
['2', '5', '8']                    # lst1: Every 3rd from index 1
['7', '6', '5', '4', '3', '2', '1'] # lst2: From 7th to 1st in reverse
['5', '7', '9']                    # lst3: From middle (index 5) every 2nd
```

**Why Calculate Middle?**

- For a list of length 10, `middle = 10 // 2 = 5`
- This ensures the slicing adapts to different list sizes automatically

---

### Program 3: Conditional List Processing

**Problem Description:**
Create a program that processes lists differently based on their length.

```python
# Create a program that takes a list and prints:

# For lists with 5 or more items: the first two and last two items
# For lists with less than 5 items: the first and last item only

input_list = input().split(', ')  # Note: Split by ', ' (comma + space)

# Write your code below
if len(input_list) > 5:  # More than 5 items (as written in original)
    result = input_list[:2] + input_list[-2:]  # First 2 + last 2
    print(result)
elif len(input_list) < 5:  # Less than 5 items
    result = input_list[:1] + input_list[-1:]  # First 1 + last 1
    print(result)
# Note: Original code doesn't handle exactly 5 items!
```

**How the Logic Works:**

1. **Input Processing:**

   - `input().split(', ')` splits on comma + space
   - This handles input like "cat, dog, bird, fish"

2. **Condition 1: `len(input_list) > 5`**

   - **First two:** `input_list[:2]` gets elements at indices 0, 1
   - **Last two:** `input_list[-2:]` gets last 2 elements
   - **Concatenation:** `+` combines both slices

3. **Condition 2: `len(input_list) < 5`**
   - **First one:** `input_list[:1]` gets element at index 0 (as a list)
   - **Last one:** `input_list[-1:]` gets last element (as a list)
   - **Why `[:1]` and `[-1:]`?** To keep results as lists for consistency

**Example Input/Output:**

_Case 1: 6 items_

```
Input: "cat, dog, bird, fish, hamster, snake"
Output: ['cat', 'dog', 'hamster', 'snake']
```

_Case 2: 3 items_

```
Input: "cat, dog, bird"
Output: ['cat', 'bird']
```

**Important Note:** The original code has a gap - it doesn't handle exactly 5 items! Lists with exactly 5 items won't produce any output.

---

### Program 4: Middle Elements Extraction

**Problem Description:**
Extract middle elements from a list, handling both even and odd length lists differently.

```python
# Extract middle elements based on list length
lst = input().split(",")  # Example input: "1,2,3,4,5,6,7,8,9,10"

lst_len = len(lst)  # Get the length of the list

if lst_len % 2 == 0:  # Even number of elements
    mid = lst_len // 2          # Find middle index
    result = lst[mid-1:mid+1]   # Get 2 middle elements
    print(result)
else:  # Odd number of elements
    mid = lst_len // 2          # Find middle index
    result = lst[mid-1:mid+2]   # Get 3 middle elements
    print(result)
```

**How Middle Calculation Works:**

1. **Even Length Lists:**

   - **Length = 10:** `mid = 10 // 2 = 5`
   - **Slice:** `lst[4:6]` gets elements at indices 4 and 5
   - **Why mid-1 to mid+1?** In a 10-element list (indices 0-9), middle elements are at indices 4 and 5

2. **Odd Length Lists:**
   - **Length = 9:** `mid = 9 // 2 = 4`
   - **Slice:** `lst[3:6]` gets elements at indices 3, 4, and 5
   - **Why mid-1 to mid+2?** Gets the true middle element plus one on each side

**Visual Examples:**

_Even length (10 elements):_

```
Indices: 0 1 2 3 4 5 6 7 8 9
Values:  1 2 3 4 5 6 7 8 9 10
                 ^ ^
               mid-1 mid  (indices 4,5)
Result: ['5', '6']
```

_Odd length (9 elements):_

```
Indices: 0 1 2 3 4 5 6 7 8
Values:  1 2 3 4 5 6 7 8 9
               ^ ^ ^
             mid-1 mid mid+1  (indices 3,4,5)
Result: ['4', '5', '6']
```

**Example Input/Output:**

_Even length:_

```
Input: "cat,dog,bird,fish,hamster,snake,rabbit,turtle,mouse,frog"
Output: ['hamster', 'snake']
```

_Odd length:_

```
Input: "cat,dog,bird,fish,hamster,snake,rabbit,turtle,mouse"
Output: ['fish', 'hamster', 'snake']
```

**Why This Approach?**

- **Even lists:** No single middle element, so take the two center elements
- **Odd lists:** One true middle element, but code takes 3 for symmetry
- **`//` operator:** Integer division ensures we get whole number indices

---

## 11. List Comparison and Slicing Practice

### Program 1: Find Non-Mutual Friends

**Problem Description:**
Given two lists of names (representing two people's friend lists), return a list of names that are friends with only one person (not mutual friends).

```python
# Find friends that are not mutual between two lists

def not_mutual_friends(list1, list2):
    only_lst1 = [friend for friend in list1 if friend not in list2]  # Friends only in list1
    only_lst2 = [friend for friend in list2 if friend not in list1]  # Friends only in list2
    non_mutual = only_lst1 + only_lst2  # Combine both
    return non_mutual

# Example usage:
result = not_mutual_friends(["John", "Emma", "Mike", "Sarah"], ["Emma", "Tom", "Sarah", "Peter"])
print(result)
```

**What is this code doing?**

- Defines a function that takes two lists.
- Uses list comprehensions to find names only in one list and not the other.
- Combines both lists to get all non-mutual friends.
- Returns the result.

**Output:**

```
['John', 'Mike', 'Tom', 'Peter']
```

**Guide:**

- Use list comprehensions to filter out mutual friends.
- Combine the unique friends from both lists.
- This is useful for comparing any two sets of data to find differences.

---

### Program 2: Elements in First List but Not in Second

**Problem Description:**
Given two lists from user input, print all elements that are in the first list but NOT in the second list.

```python
# Get two lists from user input, separated by commas
lst1 = input().split(",")
lst2 = input().split(",")

# Find elements in lst1 not in lst2
new_lst = []
for item in lst1:
    if item not in lst2:
        new_lst.append(item)
print(new_lst)
```

**What is this code doing?**

- Takes two comma-separated lists from the user.
- Loops through the first list and checks if each item is NOT in the second list.
- Adds non-matching items to a new list.
- Prints the result.

**Example Input:**

```
a,b,c,d
a,c,e
```

**Output:**

```
['b', 'd']
```

**Guide:**

- This is a classic way to find the difference between two lists.
- You can use list comprehensions for a shorter version: `[item for item in lst1 if item not in lst2]`

---

### Program 3: List Slicing and Pattern Construction

**Problem Description:**
Given a list of numbers from user input, create a new list by combining the first element, the original list, the reversed list, and the last element, then repeat this pattern twice.

```python
# Get a list of numbers from user input (space-separated)
numbers = input().split()

# Slicing and pattern construction
reverse_lst = numbers[::-1]      # Reverse the list
first = numbers[:1]              # First element as a list
last = numbers[-1:]              # Last element as a list
new_lst = first + numbers + reverse_lst + last  # Combine pattern
repeat = new_lst * 2             # Repeat pattern twice
print(repeat)
```

**What is this code doing?**

- Takes a space-separated list of numbers from the user.
- Slices to get the first and last elements as lists.
- Reverses the list using slicing (`[::-1]`).
- Combines: first + original + reversed + last.
- Repeats the pattern twice.
- Prints the final list.

**Example Input:**

```
1 2 3
```

**Output:**

```
['1', '2', '3', '3', '2', '1', '1', '1', '2', '3', '3', '2', '1', '1']
```

**Guide:**

- Slicing is a powerful way to manipulate lists.
- You can use `[::-1]` to reverse, `[:1]` for the first element, and `[-1:]` for the last.
- Combining and repeating patterns is common in data processing and formatting.

---

## 12. Further List Comparison and Pattern Challenges

### Program 1: Symmetric Difference with Sets (Alternative Non-Mutual Friends)

**Problem Description:**
Find all names that are only in one of two friend lists, using set operations for efficiency and clarity.

```python
def not_mutual_friends_set(list1, list2):
    # Use set symmetric difference to find non-mutual friends
    return list(set(list1) ^ set(list2))

# Example usage:
result = not_mutual_friends_set(["John", "Emma", "Mike", "Sarah"], ["Emma", "Tom", "Sarah", "Peter"])
print(sorted(result))
```

**What is this code doing?**

- Converts both lists to sets.
- Uses the `^` operator (symmetric difference) to find all elements that are in either set, but not both.
- Converts the result back to a list.
- `sorted(result)` is used for consistent output order (since sets are unordered).

**Output:**

```
['John', 'Mike', 'Peter', 'Tom']
```

**Guide:**

- Set operations are much faster for large lists.
- Symmetric difference is a direct way to find non-mutual elements.
- Use `set(list1) - set(list2)` for items only in `list1`.

---

### Program 2: List Intersection (Mutual Friends)

**Problem Description:**
Find all names that appear in both friend lists (mutual friends).

```python
def mutual_friends(list1, list2):
    # Use set intersection to find mutual friends
    return list(set(list1) & set(list2))

# Example usage:
result = mutual_friends(["John", "Emma", "Mike", "Sarah"], ["Emma", "Tom", "Sarah", "Peter"])
print(sorted(result))
```

**What is this code doing?**

- Converts both lists to sets.
- Uses the `&` operator (intersection) to find all elements present in both sets.
- Converts the result back to a list.
- `sorted(result)` is used for consistent output order.

**Output:**

```
['Emma', 'Sarah']
```

**Guide:**

- Set intersection is the most efficient way to find common elements between two lists.
- Useful for social network analysis, group comparisons, and more.

---

### Program 3: List Union (All Unique Friends)

**Problem Description:**
Combine two friend lists into one list of all unique names (no duplicates).

```python
def all_unique_friends(list1, list2):
    # Use set union to combine all unique names
    return list(set(list1) | set(list2))

# Example usage:
result = all_unique_friends(["John", "Emma", "Mike", "Sarah"], ["Emma", "Tom", "Sarah", "Peter"])
print(sorted(result))
```

**What is this code doing?**

- Converts both lists to sets.
- Uses the `|` operator (union) to combine all unique elements from both sets.
- Converts the result back to a list.
- `sorted(result)` is used for consistent output order.

**Output:**

```
['Emma', 'John', 'Mike', 'Peter', 'Sarah', 'Tom']
```

**Guide:**

- Set union is the fastest way to merge lists and remove duplicates.
- Useful for combining groups, mailing lists, or any scenario where you want all unique items.

---

### Program 4: List Difference with List Comprehension (Alternative Syntax)

**Problem Description:**
Find all items in the first list that are not in the second list, using a list comprehension for brevity.

```python
lst1 = input().split(",")
lst2 = input().split(",")
# List comprehension version
diff = [item for item in lst1 if item not in lst2]
print(diff)
```

**What is this code doing?**

- Takes two comma-separated lists as input.
- Uses a list comprehension to filter out items in `lst1` that are also in `lst2`.
- Prints the result.

**Example Input/Output:**

```
Input:
a,b,c,d
a,c,e
Output:
['b', 'd']
```

**Guide:**

- List comprehensions are concise and Pythonic for filtering.
- This is equivalent to the loop-based approach, but shorter.

---
