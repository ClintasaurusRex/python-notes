inventory = {}
print(inventory)

def add_item(item: str, price: float, stock: int):
  if item in inventory:
    print(f"Error: Item '{item}' already exists.")
  else:
    inventory[item] = {"price": float(price), "stock": stock}
    print(f"Item '{item}' added successfully.")
    
# add_item("Apple", 0.5, 100)
# add_item("Banana", 0.2, 50)
# add_item("Apple", 0.6, 30) 
# print(inventory)  


def update_stock(item:str, quantity: int):
  if item not in inventory:
    print(f"Error: '{item}' not found.")
  else:
    new_stock = inventory[item]["stock"] + quantity
    if new_stock < 0:
      print(f"Error: Insufficient stock for '{item}'.")
    else:
      inventory[item]["stock"] = new_stock
      print(f"Stock for '{item}' updated successfully.")
      
def check_availability(item: str):
  if item not in inventory:
    return "Item no found"
  else:
    stock = inventory[item]["stock"]
    return stock
      
def sales_report(sales: dict):
    total = 0
    for item, quantity_sold in sales.items():
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        else:
            price = inventory[item]["price"]
            stock = inventory[item]["stock"]
            if quantity_sold > stock:
                print(f"Error: Insufficient stock for '{item}'.")
            else:
                revenue = price * quantity_sold
                total += revenue
                inventory[item]["stock"] -= quantity_sold
                print(f"Sold {quantity_sold} of '{item}' for ${revenue:.2f}.")
    return f"Total revenue: ${total:.2f}"
    
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)
# testing = {}
# testing['beats'] = {"stock": 20, "price": float(0.70)}
# print(testing)

# # Starter code: Multi-level dictionary practice

# school = {
#     "students": {
#         "Alice": {
#             "age": 20,
#             "grades": {"Math": 90, "Physics": 85},
#             "clubs": ["Chess", "Robotics"]
#         },
#         "Bob": {
#             "age": 22,
#             "grades": {"Math": 75, "Biology": 80},
#             "clubs": ["Drama"]
#         }
#     },
#     "teachers": {
#         "Mrs. Smith": {
#             "subject": "Math",
#             "room": 101
#         },
#         "Mr. Lee": {
#             "subject": "Biology",
#             "room": 102
#         }
#     }
# }

# # Practice: Try to print the following
# # 1. Alice's age
# # 2. Bob's Biology grade
# # 3. Mrs. Smith's room number
# # 4. All clubs Alice is in
# # 5. The subject Mr. Lee teaches

# # Example:
# print(school["students"]["Alice"]["age"])  # Should print 20
# # Add your own print statements below to practice!
# def get_grade(name: str):
#     student = school.get('students')[name].get('grades')
#     for subject, grade in student.items():
#         student_grade = f"{name}'s grades are: {subject}: {grade}"
#     print(student_grade)
    
# get_grade("Bob")