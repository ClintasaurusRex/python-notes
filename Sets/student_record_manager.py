student_records = {}

# def check_student(name: str):
#   key = name.capitalize()
#   if key in student_records:
#         return (f"Student '{name}' already exists.")

def add_student(name: str, age: int, courses: list[str]):
    key = name.capitalize()
    if key in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[key] = {
            'age': age,
            'grades': set(),
            'courses': set(courses)
        }
        print(f"Student '{name}' added successfully.")
        
# Create a function named add_grade that takes two arguments: name (string) and grade (integer). 
# The function should:
# Check if the student name exists in the student_records dictionary.
# If it does not exist, print "Student '<name>' not found.".
# If the name exists, add the grade to the student's grades set.
# Print "Grade <grade> added for student '<name>'.".

def add_grade(name: str, grade: int):
    key = name.capitalize()
    if key not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[key]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'")
  
def is_enrolled(name: str, course: str):
  key = name.capitalize()
  if key not in student_records:
    print(f"Student '{name}' not found.")
    return False
  elif course in student_records[key]['courses']:
    return True
  else:
    return False
  
  
def calculate_average_grade(name: str):
  key = name.capitalize()
  if key not in student_records:
    print(f"Student '{name}' not found.")
    return None
  grades = student_records[key]['grades']
  if not grades:
    print('f"Student {name} not found')
    
  average = sum(grades) / len(grades)
  return average
  
def list_students_by_course(course: str):
  enrolled_students = []
  for name, info in student_records.items():
    if course in info['courses']:
      enrolled_students.append(name)
    
  return enrolled_students
    

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
print(list_students_by_course("Math"))  # Should return ["Alice", "Bob"]
print(list_students_by_course("Physics"))  # Should return ["Alice", "Diana"]
print(list_students_by_course("Biology"))  # Should return ["Bob"]
print(list_students_by_course("History"))  # Should return an empty list
# print(calculate_average_grade("Alice"))  # Should return 87.5
# print(calculate_average_grade("Bob"))  # Should return 75.0
# print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
# print(calculate_average_grade("Alice"))  # Should return 87.5 again
# list_students_by_course('Math')
print(student_records)