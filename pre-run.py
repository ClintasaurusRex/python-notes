print("------------------------------------------Basic Error Handling ---------------------------------")
print("------------------------------------------Challenge One ---------------------------------")
# Common types of exceptions include TypeError, ValueError, IOError, and ZeroDivisionError. 
# For example, a TypeError occurs when an operation is performed on a value of an inappropriate type, 
# and a ZeroDivisionError occurs when a number is divided by zero.
# try:
#     user_input = input("Enter a number: ")
#     number = int(user_input)
#     print(f"You entered: {number}")
# except ValueError:
#     print("Invalid input! Please enter a valid number.")

print("------------------------------------------Challenge Two ---------------------------------")

def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        value = int(input_string)     
        # Calculate 100 divided by the input value
        result = 100 / value       
        # Return the result
        return result
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        return "Input must be a number!"
    except ZeroDivisionError:
        # Handle the case where input is zero
        return "Cannot divide by zero!"
    except:
        # Handle any other unexpected exceptions
        return "An unexpected error occurred!"

print(process_data("0"))

print("------------------------------------------Challenge Three ---------------------------------")
testCase = ["apple:3", "banana:2","milk:5"]

def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
            item, quantity = order.split(":")
            try:
                quantity = int(quantity)
            except ValueError:
                print(f"Invalid quantity: {order}")
                continue
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue
            if item in cart:
                cart[item] += quantity
            else:
                cart[item] = quantity
        except Exception:
            print(f"Unexpected error: {order}")
    return cart

print(handle_shopping_cart(testCase))
print("------------------------------------------Basic Error Handling ---------------------------------")
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