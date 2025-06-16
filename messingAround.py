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
for i in range(3):
    for j in range(3):
        print(i, j)