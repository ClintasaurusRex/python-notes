from car import Car
from student import Student
from bank_account import BankAccount
from book import Book
from calculator import Calculator



print("--------------------------")

potter = Book("Harry Potter", "J.K. Rowling", 400)
print(f"'{potter.title}' by '{potter.author}' with {potter.pages} pages")



print("--------------------------")

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

print("--------------------------")
calc = Calculator()

print(f"Add: {calc.add(50)}")

print(f"Subtract: {calc.subtract(5)}")

print(f"Multiply: {calc.multiply(10)}")

print(f"Divide: {calc.divide(0)}")

calc.clear()
print(calc.get_result())

print("--------------------------")

def my_decorator(func):
  def wrapper():
    print("Before function runs")
    func()
    print("After function runs")
  return wrapper

@my_decorator
def say_hello():
  print("Hello")
  
say_hello()