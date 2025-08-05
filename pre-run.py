
# -------------------------------------- Basic List Comprehensions ---------------------------------
print("-------------------------------------Challenge One ------------------------------------------")
nums = [1,2,3,4,5]
def double_numbers(numbers):
    return [n* 2 for n in numbers]

print(double_numbers(nums))

print("------------------------------------Challenge Two --------------------------------------------")
# -------------------------------------- Creating Simple Lists ---------------------------------------
l1 = ["python", "list", "comprehension", "challenge"]

def get_word_length(words):
    word_length = [len(word) for word in words]
    return word_length

print(get_word_length(l1))

# length = [len(item) for item in l1]
# print(length)

print("------------------------------------Challenge Three --------------------------------------------")
#  ---------------------------------------- Adding Conditions ------------------------------------------
l2 = [-3, -2, 0, 1, 2, 3]

def filter_and_square(numbers):
    new_list = [n * n for n in numbers if n > 0]
    return new_list

print(filter_and_square(l2))
# new_list = [n * n for n in l2 if n > 0]
# print(new_list)

print("------------------------------------Challenge Four --------------------------------------------")
#  ---------------------------------------- Using Data Aggregation ------------------------------------------
numbers = [-10, -5, 0, 2, 4, 7, 10, 12]

def sum_positive_numbers(numbers):
    posi_nums = sum([n for n in numbers if n > 0 and n % 2 ==0])
    return posi_nums

print(sum_positive_numbers(numbers))

# sum_positive = sum([n for n in numbers if n > 0 and n % 2 == 0])
# print(sum_positive)

print("------------------------------------Challenge Five --------------------------------------------")
#  ---------------------------------------- House of Lists ------------------------------------------
list_of_lists = [[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]

def house_of_lists(list_of_lists):
    # Filter inner lists with sum <= 50
    filtered_lists = [lst for lst in list_of_lists if sum(lst) <= 50]
    # Extract numbers less than 5 from each filtered list
    extracted = [num for lst in filtered_lists for num in lst if num < 5]
    return extracted

# Example usage:
list_of_lists = [[10, 20, 30], [1, 2, 3], [5, 50, 5], [0, 3, 6, 9]]
print(house_of_lists(list_of_lists))  # Output: [1, 2, 3, 0, 3]

# -------------------------------------- Basic List Comprehensions ---------------------------------

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