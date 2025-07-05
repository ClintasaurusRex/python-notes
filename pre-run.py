
print('--------------------------Looping Through Dictionaries-----------------------')
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
      