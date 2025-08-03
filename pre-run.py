new_students = {}

def add_student(name: str, age: int, courses: list[str]):
    new_students[name] = {
        'age': age,
        'grades': set(),
        'courses': set(courses)        
    }

def top_students(threshold: float):
    top_students = []
    

add_student('Alice', 20, ['Math', 'Science'])
add_student("Bob", 22, ["Math", "Chemistry"])
add_student("Charlie", 21, ["Physics", "Biology"])
for name, info in new_students.items():
    print(f"Name: {name}, Age: {info['age']}, Courses: {', '.join(info['courses'])}")