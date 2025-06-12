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