print("-----------------------------------------------Advanced Functions -----------------------------------")
print("-------------------------------------------Challenge One ---------------------------------------------")
# ---------------------------------------Returning Multiple Values -------------------------------------------

def get_student_info():
    name = "Bob"
    age = 20
    major = "Computer Science"
    return name, age, major

student_name, student_age, student_major = get_student_info()
print(student_name)
print(student_age)
print(student_major)

# ----------------------------------------- second challenge of challenge one- ------------------------

def get_product_info():
    name = "Laptop"
    price = 999.88
    rating = 4.5
    return name, price, rating

product_name, product_price, product_rating = get_product_info()
print(product_name)
print(product_price)
print(product_rating)

print("------------------------------------------Challenge 2 Lambda Functions ---------------------------------")
# Create a Lambda function that multiplies three numbers
multiply = lambda num1, num2, num3: num1 * num2 * num3
result = multiply(2,3,4)
print(result)

print("-----------------------------------------------Advanced Functions -----------------------------------")
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