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

def add_grade(name: str, grade: int):
    key = name.capitalize()
    if key not in student_records:
        print(f"Student '{name}' not found.")
    else:
        student_records[key]['grades'].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
  
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
    
def filter_top_students(threshold: float):
    top_students = []
    for name, info in student_records.items():
        if info['grades'] and calculate_average_grade(name) >= threshold:
            top_students.append(name)
    return top_students

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list