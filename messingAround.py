first_name = 'ada'
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

print(full_name.title())

count = 0 
numbers = []

while count < 10:
  count += 1
  numbers.append(count)

print(numbers)

print("Max: ",max(numbers))
print("Min: ",min(numbers))
print("Sum: ",sum(numbers))

print("---------------------Working with Lists----------------------")
for number in numbers:
  print(number)
  # print("Whoopty doo what does it all mean Basil")


print("-----------------------------------------------------------")
fruits = ["apple", "banana", "cherry"]

squares = [x ** 2 for x in range(5)]
print(squares)

for index, fruit in enumerate(fruits):
  print(f"Index {index}: {fruit}")

fruitsCopy = fruits[:] # using the slice method or you can use .copy()
print("this is a copy: ", fruitsCopy)

my_foods = ['steak', 'pizza', 'chicken']
friends_food = my_foods[:]
friends_food.append('fish')

print(f"My favorite foods are {my_foods} and my friends favorite food is {friends_food}")


def countVowels(text):
  vowels = "aeiouAEIOU"
  count = 0

  for char in text:
    if char in vowels:
      count += 1
  return count
sentence = "Hello, how are you?"
print(countVowels(sentence))
print('one two three')

# name = input()
# age = int(input())
# # Write code here
# age = age + 10
# print(f'In 10 years, {name} will be {age} years old')

# user_input = int(input("Pick 1 or 0:\n"))
# if user_input == 1:
#     print("F")
# else:
#     print("T")

def remove_duplicates_and_sort(numbers):
    # Convert the list to a set to remove duplicates, then back to a list
    no_dupes = []
    for num in numbers:
       if not num in no_dupes:
          no_dupes.append(num)
         
    return sorted(no_dupes)

numbers = [4, 2, 7, 4, 2, 9, 1]
result = remove_duplicates_and_sort(numbers)
print(result)  # Output: [1, 2, 4, 7, 9]

# def bill_calc(bill):
#   tip = float(bill * 0.20)
#   return format(bill + tip, ".2f")

# print(bill_calc(20.25))

# for i in range(1, 11):
#   print(i)

#   number = 27
# power_of_two = 1

# while power_of_two <= number:
#     power_of_two *= 2

# print(power_of_two)

# for i in range(20, 9, -2):
#   print(i)
# n = int(input())
# res = 0
# print('-------------------------------------------')
# for i in range(n):
#     a = int(input())
#     res += a

# print(res)

# def sum_numbers():
#     sum = 0
#     for i in range(1, 10001):
#         sum += i 
#     print(sum)

# n = int(input())
# for _ in range(n):
#     print(sum_numbers())

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

# Get input and cast to int
number = int(input())

# Call the function
fizzbuzz(number)

def change_element(lst, index, new_element): # THIS IS IMPORTANT
    # Make a copy to avoid changing the original list
    modified_list = lst.copy()
    # Change the element at the given index
    modified_list[index] = new_element
    return modified_list

# Example usage:
result = change_element([1, 2, 3], 0, 9)
print(result)  # Output: [9, 2, 3]\


# Create a function named change_element that receives 3 arguments:

# First argument is a list
# Second argument is an index
# Third argument is another list
# The function should replace the element at the given index in the first list with the first element from the second list.

# Example:

# change_element([1, 2, 3], 1, [5, 6, 7]) should return [1, 5, 3]
def change_element(list1, index, list2):
    # Write your code below
    modified_list1 = list1.copy()
    modified_list2 = list2.copy()

    modified_list1[index] = modified_list2[0]
    return modified_list1

change_element([1, 2, 3], 1, [5, 6, 7])