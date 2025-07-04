# Dictionaries Part 1

recipe_book = {"Pancakes": ["flour", "milk", "eggs", "sugar"],
               "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
               }

print("-------------------------------------RECIPE BOOK---------------------------------------")
print(recipe_book.get("Pancakes"))
recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"].append("blueberries")
print(recipe_book)

# Create a function named update_inventory that takes three parameters: inventory_dict (a dictionary), item (a string), and quantity (an integer). The function should update the inventory_dict with the new item and quantity. If the item already exists in the inventory, its quantity should be increased by the given amount. If the item does not exist, a new item should be added with the given quantity. The function should return the updated dictionary.

print("-------------------------------------RECIPE Inventory---------------------------------------\n")
fruits = {"apples":50,"bananas":30}
def update_inventory(inventory_dict, item, quantity):
    # Write code here
    if item in inventory_dict:
       inventory_dict[item] += quantity
    else:
       inventory_dict[item] = quantity
    return inventory_dict

print (update_inventory(fruits, "apples", 25))


# Create a function named update_employee_info that takes three parameters: employee_dict (a dictionary), key (a string), and value. The function should update the employee_dict with the new key and value. If the key already exists, its value should be updated. If the key does not exist, a new key-value pair should be added. The function should return the updated dictionary.

def update_employee_info(employee_dict, key, value):
    # Write code here
    employee_dict[key] = value
    return employee_dict

print("------------------------------UPDATE EMPLOYEE INFO---------------------\n")
print(update_employee_info({"name": "Alice", "age": 30, "department": "HR"}, "name", "Bob"))


print("-------------------------------CREATE BOOk--------------------------\n")
def create_book_dict(title, author, year):
  return {
    "title": title,
    "author": author,
    "year": year
  }

print(create_book_dict("To Kill a Mockingbird", "Harper Lee", 1960))

print("-------------------------------CREATE STUDENT DICT--------------------------")

def create_student_dict(name, age, major):
  return {
    "name": name,
    "age": age,
    "major": major
  }

print(create_student_dict("Alice", 30, "pooping"))



print("-------------------------------------Accessing Values-----------------------------")
def get_capital(country_capitals, country_name):
  # This function takes a dictionary of country capitals and a country name (key).
  # It returns the capital city (value) for the given country.
  # Example: get_capital({"Norway": "Oslo"}, "Norway") returns "Oslo"
  return country_capitals[country_name]

country_capitals = {"Norway": "Oslo", "Sweden": "Stockholm", "Denmark": "Copenhagen"}
print(get_capital(country_capitals, "Norway"))  # Output: Oslo



print("-----------------------------------Create Book Dict--------------------------")
def create_book_dict(title, author, year):
  return{"title": title, "author": author, 'year': year}


print("-----------------------------------Create Students Dict--------------------------")
def create_student_dict(name, age, major):
  # Creating a dictionary with keys and values:
  # Each key (e.g., "name") is a string that describes the data.
  # Each value (e.g., name) is the variable passed to the function.
  # This allows you to store related information together in a structured way.
  return {
    "name": name,    # The student's name (string)
    "age": age,      # The student's age (number)
    "major": major   # The student's major/field of study (string)
  }