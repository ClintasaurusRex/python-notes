from car import Car
from student import Student

my_car = Car()
print(type(my_car))
print("--------------------------")
student1 = Student()
student2 = Student()

student1.name = "Alice"
student2.name = "Bob"

student1.grade = "A"
student2.grade = "B"

print(f"{student1.name} has grade {student1.grade} at {Student.school}")
print(f"{student2.name} has grade {student2.grade} at {Student.school}")