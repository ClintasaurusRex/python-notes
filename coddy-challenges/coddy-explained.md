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
