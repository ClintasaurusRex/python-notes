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
# lambda arguments: expression
# add = lambda x, y: x + y
# result = add(5, 3)
# print(result)
# Output: 8

# Create a Lambda function that multiplies three numbers
multiply = lambda num1, num2, num3: num1 * num2 * num3
result1 = multiply(2,3,4)
print(result1)

# -----------------------------------------Second Lambda Challenge ============================
# Create a lambda function that calculates the average of four numbers
average = lambda *args: sum(args) / len(args)
result = average(10,15,20,25)
print(result)

print("------------------------------------------Challenge 3 Lambda Functions Part 2 ---------------------------------")

# Read a number from input
number = -5

# Define your lambda function here
grade_status = lambda score: "Amazing!" if score == 100 else "Pass" if score >= 60 else "Fail"
categorize_number = lambda num: "Positive" if num > 0 else "Zero" if num == 0 else "Negative" 

# Call your lambda function with the input number and print the result
print(categorize_number(number))

print("------------------------------------------Challenge 4 Sort Lambda ---------------------------------")

tup = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

def sort_tuples(data):
  sorted_data = sorted(data, key=lambda x: x[1])
  return sorted_data
print(sort_tuples(tup))

print("------------------------------------------Challenge 5 Recursive ---------------------------------")
def count_down(n):
    print(n)
    if n == 0:
        return
    count_down(n - 1)

count_down(3)


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