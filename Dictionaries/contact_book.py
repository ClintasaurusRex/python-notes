





print("-----------------------Dictionary Methods----------------------------")

# items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# items = my_dict.items()
# print(items)
# Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}


# -- keys(): Returns a view object that displays a list of all the keys in the dictionary.
# -- values(): Returns a view object that displays a list of all the values in the dictionary.

# Step 2: Access All Keys and Values
# Print all students and grades
print(f"Students: {grades.keys()}")
print(f"Grades: {grades.values()}")

# Output
# Students: dict_keys(['Alice', 'Bob', 'Charlie'])
# Grades: dict_values([85, 90, 78])

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade

# -- get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value (or None if no default is specified).

# Get Bob's grade using get() method
bob = grades.get("Bob")
print(f"Bob's grade: {bob}")
# Bob's grade: 90

# Step 5: Remove a Student
# Remove Charlie using pop() method

# -- pop(key): Removes the element with the specified key and returns its value.

# Print the updated dictionary
popped = grades.pop("Charlie")
print(f"Updated Grades: {grades}")
# Updated Grades: {'Alice': 85, 'Bob': 90, 'Diana': 92}


print('--------------------------Looping Through Dictionaries-----------------------')
data1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
def freq_counter(data_list):
   new_dict = {}
   for item in data_list:
      if item in new_dict:
         new_dict[item] += 1
      else:
         new_dict[item] = 1
   print(new_dict)
freq_counter(data1)

print("----------------------------------print_product_details-----------------------------------")
data = {"name":"Laptop","brand":"Dell","price":799.99,"stock":15}

def print_product_details(product_data):
   if not product_data:
      print("No product information available")
   for key, value in product_data.items():
      print(f"{key.capitalize()}: {value}")

print_product_details(data)
print_product_details({})


print("----------------------------------print_employee_details-----------------------------------")
details = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}
mt = {}

def print_employee_details(employee_data):
    # Write code here
    if not employee_data:
     print("not data")
    else: 
      for key, value in employee_data.items():
     
        print(f"{key}: {value}")
       
       

print_employee_details(details)
print_employee_details(mt)


print("----------------Checking for Keys-------------------") 
inventory = {"apple":10,"banana":5,"orange":7}
# banana


def check_inventory(inventory, item):
  if item in inventory:
     print(f"{item} is in stock. Quantity: {int(inventory[item])}")
  else:
     print(f"{item} is not in stock.")
     
     

check_inventory(inventory, "banana")



# When working with dictionaries you often need to check if a specific key exists. Python provides simple ways to check for the presence of keys in a dictionary

# Using the in keyword

employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}

if "Alice" in employees:
  print("Alice is in the company.")
if "John" not in employees:
  print("John is not in the company.")

# If you need to check many names do it like this 
employees = {"Alice": "HR", "Bob": "Engineering", "Diana": "Marketing"}
names_to_check = ["Alice", "John", "Diana"]

for name in names_to_check:
    if name in employees:
        print(f"{name} is in the company.")
    else:
        print(f"{name} is not in the company.")



# users = {
#     'user123': {
#         'name': 'Alice',
#         'email': 'alice@example.com',
#         'profile': {
#             'age': 30,
#             'city': 'New York',
#             'interests': ['coding', 'hiking']
#         }
#     },
#     'user456': {
#         'name': 'Bob',
#         'email': 'bob@example.com',
#         'profile': {
#             'age': 25,
#             'city': 'London',
#             'interests': ['music', 'reading']
#         }
#     }
# }

# for user_id, user_info in users.items():
#   print(f"\nProcessing User ID: {user_id}")
  

#   name = user_info.get("name", "No Data")
#   print(f"\tName: - {name}")
  
#   if "profile" in user_info:
#     profile_data = user_info['profile']
#     for k, v in profile_data.items():
#       print(k, v)
      
#       print(f"\t - {k.capitalize()}: {v}")
      