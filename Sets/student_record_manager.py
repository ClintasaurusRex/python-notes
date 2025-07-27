student_records = {}

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

add_student('Clint', 30, [])
add_student('Clint', 30, [])
print(student_records)