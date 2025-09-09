from car import Car
from student import Student
from bank_account import BankAccount

my_account = BankAccount()
my_account.deposit(100)
my_account.withdraw(30)
print(f"Current balance: ${my_account.get_balance()}")


print("--------------------------")
my_car = Car()
print(type(my_car))
# my_car.color = "White".lower()
# my_car.model = "WRX"
# my_car.honk() 
# my_car.describe()
print("--------------------------")
student1 = Student()
student2 = Student()

student1.name = "Alice"
student2.name = "Bob"

student1.grade = "A"
student2.grade = "B"

print(f"{student1.name} has grade {student1.grade} at {Student.school}")
print(f"{student2.name} has grade {student2.grade} at {Student.school}")

print("--------------------------")

my_car.year = 2020
my_car.make = "Toyota"
my_car.model = "Corolla"
my_car.display_info()