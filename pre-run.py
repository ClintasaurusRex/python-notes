# How the ternary operator works
# The ternary operator is a shorthand way of writing an if-else statement. 
# it allows you to assign a value based on a condition in a single line.

#  Challenge 1
# score = int(input())
# status = "Pass" if score > 50 else "Fail" 
# print(status)

#--------------------------------------- Challenge 2

# Write a program that takes a float input temperature representing the current temp in Celcius. 
# Use the ternary operator to determine a warning status based on the temperature

# temperature = float(input())
# status = "Hot" if temperature > 30 else "Normal"
# print(status)


# -------------------------------------- Challenge 3

# Membership checks in Python let you check if a value exists in a collection like a 
# list, tuple, set, or dictionary using in and not in.Membership checks in Python let 
# you check if a value exists in a collection like a list, tuple, set, or dictionary using in and not in.

# names = ["Alice", "Bob", "Charlie"]
# grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# if "Alice" in names:
#   print("Alice is in the list.")
# if "David" not in names:
#   print("David is not in the list.")

# if "Bob" in grades:
#   print("Bob is in the dictionary.")
# if "Eve" not in names:
#   print("Eve is not in the dictionary.")

# def check_inventory(products, quantities):

#   if "Apples" in products:
#     print("Apples are in stock.")
#   if "Oranges" not in products:
#     print("Oranges are not in stock")
#   if "Bananas" in quantities:
#     print("Bananas quantity is tracked.")
#   if "Grapes" not in quantities:
#     print("Grapes quantity is not tracked")

# check_inventory(["Apples","Bananas","Milk","Bread","Eggs"],
# {"Bananas":30,"Milk":10,"Bread":20})


# ----------------------------------Challenge 4
list1 = [1,2,3]
list2 = list1

print(list1 is list2)
print(list1 is not list2)
print("-----------------------------------------------------")

def compare_strings(str1, str2):
 
  compared = {}
  compared['is_substring'] = str1 in str2
  compared['starts_with'] = str2.startswith(str1)
  compared['ends_with'] = str2.endswith(str1)
  compared['is_equal'] = str1.lower() == str2.lower()
  print(compared)
  

st1 = "hello"
st2 = 'HELLO'
compare_strings(st1, st2)