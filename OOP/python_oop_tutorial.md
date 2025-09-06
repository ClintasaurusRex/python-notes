# Python Object-Oriented Programming (OOP) - Beginner's Guide

Welcome to the world of Object-Oriented Programming in Python! This tutorial will guide you through the fundamental concepts of OOP, helping you understand how to write cleaner, more organized, and reusable code.

## Table of Contents
1. [What is Object-Oriented Programming?](#what-is-object-oriented-programming)
2. [Classes and Objects](#classes-and-objects)
3. [Attributes and Methods](#attributes-and-methods)
4. [The `__init__` Method (Constructor)](#the-init-method-constructor)
5. [Encapsulation](#encapsulation)
6. [Inheritance](#inheritance)
7. [Polymorphism](#polymorphism)
8. [Putting It All Together: Final Project](#putting-it-all-together-final-project)
9. [Summary](#summary)

---

## What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into **objects** and **classes**. Think of it as a way to model real-world things in your code.

### Key Benefits of OOP:
- **Organization**: Code is more structured and easier to understand
- **Reusability**: Write code once, use it many times
- **Modularity**: Break complex problems into smaller, manageable pieces
- **Maintainability**: Easier to update and fix code

### The Four Pillars of OOP:
1. **Encapsulation**: Bundling data and methods together
2. **Inheritance**: Creating new classes based on existing ones
3. **Polymorphism**: Using the same interface for different types
4. **Abstraction**: Hiding complex implementation details

---

## Classes and Objects

### What is a Class?
A **class** is like a blueprint or template. It defines what properties and behaviors something should have, but it's not the actual thing itself.

Think of a class like a cookie cutter - it defines the shape, but it's not a cookie.

### What is an Object?
An **object** is an actual instance of a class. It's like the cookie made from the cookie cutter.

### Basic Class Example

```python
# Define a simple class
class Dog:
    pass  # Empty class for now

# Create objects (instances) of the class
my_dog = Dog()
your_dog = Dog()

print(type(my_dog))  # <class '__main__.Dog'>
print(my_dog)        # <__main__.Dog object at 0x...>
```

**Output:**
```
<class '__main__.Dog'>
<__main__.Dog object at 0x7f8b8c0d2a90>
```

---

## Attributes and Methods

### Attributes
**Attributes** are variables that belong to a class or object. They store data about the object.

### Methods
**Methods** are functions that belong to a class. They define what the object can do.

### Example with Attributes and Methods

```python
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis lupus"
    
    # Instance method
    def bark(self):
        return "Woof! Woof!"
    
    def sit(self):
        return "The dog is sitting"

# Create a dog object
buddy = Dog()

# Access class attribute
print(f"Species: {buddy.species}")

# Call methods
print(buddy.bark())
print(buddy.sit())
```

**Output:**
```
Species: Canis lupus
Woof! Woof!
The dog is sitting
```

---

## The `__init__` Method (Constructor)

The `__init__` method is a special method called a **constructor**. It runs automatically when you create a new object and is used to set up the object's initial state.

### Example with Constructor

```python
class Dog:
    def __init__(self, name, age, breed):
        # Instance attributes
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is a {self.age}-year-old {self.breed}"

# Create dog objects with different attributes
buddy = Dog("Buddy", 3, "Golden Retriever")
max_dog = Dog("Max", 5, "German Shepherd")

# Use the objects
print(buddy.get_info())
print(max_dog.bark())
print(f"Buddy's age: {buddy.age}")
```

**Output:**
```
Buddy is a 3-year-old Golden Retriever
Max says Woof!
Buddy's age: 3
```

### Understanding `self`
- `self` refers to the current instance of the class
- It's automatically passed as the first parameter to instance methods
- Use `self` to access attributes and methods of the current object

---

## Encapsulation

**Encapsulation** is about bundling data (attributes) and methods that work on that data into a single unit (class). It also involves controlling access to the internal state of an object.

### Public, Protected, and Private Attributes

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner              # Public attribute
        self._account_number = "123456" # Protected (convention: single underscore)
        self.__balance = initial_balance # Private (name mangling: double underscore)
    
    # Public method to access private balance
    def get_balance(self):
        return self.__balance
    
    # Public method to modify private balance safely
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Invalid withdrawal amount or insufficient funds"

# Create a bank account
account = BankAccount("Alice", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: ${account.get_balance()}")
print(account.deposit(500))
print(account.withdraw(200))

# This would work (public)
print(f"Owner: {account.owner}")

# This would work but not recommended (protected)
print(f"Account Number: {account._account_number}")

# This would cause an AttributeError (private)
# print(account.__balance)  # Uncomment to see the error
```

**Output:**
```
Owner: Alice
Balance: $1000
Deposited $500. New balance: $1500
Withdrew $200. New balance: $1300
Owner: Alice
Account Number: 123456
```

---

## Inheritance

**Inheritance** allows you to create a new class based on an existing class. The new class inherits attributes and methods from the parent class and can add its own or modify existing ones.

### Basic Inheritance Example

```python
# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canis lupus")  # Call parent constructor
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Override parent method
    def eat(self):
        return f"{self.name} is munching on dog food"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Felis catus")
        self.breed = breed
    
    def meow(self):
        return f"{self.name} says Meow!"
    
    # Override parent method
    def sleep(self):
        return f"{self.name} is napping in a sunny spot"

# Create instances
buddy = Dog("Buddy", "Golden Retriever")
whiskers = Cat("Whiskers", "Persian")

# Use inherited methods
print(buddy.eat())     # Uses overridden method
print(buddy.sleep())   # Uses inherited method
print(buddy.bark())    # Uses Dog-specific method

print(whiskers.eat())  # Uses inherited method
print(whiskers.sleep()) # Uses overridden method
print(whiskers.meow()) # Uses Cat-specific method
```

**Output:**
```
Buddy is munching on dog food
Buddy is sleeping
Buddy says Woof!
Whiskers is eating
Whiskers is napping in a sunny spot
Whiskers says Meow!
```

### Multiple Inheritance Example

```python
class Flyer:
    def fly(self):
        return "Flying through the sky"

class Swimmer:
    def swim(self):
        return "Swimming in the water"

# Multiple inheritance
class Duck(Animal, Flyer, Swimmer):
    def __init__(self, name):
        super().__init__(name, "Anas platyrhynchos")
    
    def quack(self):
        return f"{self.name} says Quack!"

donald = Duck("Donald")
print(donald.eat())   # From Animal
print(donald.fly())   # From Flyer
print(donald.swim())  # From Swimmer
print(donald.quack()) # From Duck
```

**Output:**
```
Donald is eating
Flying through the sky
Swimming in the water
Donald says Quack!
```

---

## Polymorphism

**Polymorphism** means "many forms." It allows objects of different classes to be treated as objects of a common base class, while still maintaining their own specific behaviors.

### Example of Polymorphism

```python
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphism in action
def print_shape_info(shape):
    """This function works with any Shape object"""
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 20)

# Create different shapes
shapes = [
    Rectangle(5, 4),
    Circle(3),
    Triangle(6, 4, 5, 5, 6)
]

# Use polymorphism - same function works with different shape types
for shape in shapes:
    print(f"Shape: {shape.__class__.__name__}")
    print_shape_info(shape)
```

**Output:**
```
Shape: Rectangle
Area: 20.00
Perimeter: 18.00
--------------------
Shape: Circle
Area: 28.27
Perimeter: 18.85
--------------------
Shape: Triangle
Area: 12.00
Perimeter: 16.00
--------------------
```

---

## Putting It All Together: Final Project

Let's create a simple **Library Management System** that demonstrates all OOP concepts:

```python
class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies  # Protected attribute
        self._available_copies = copies
    
    def get_info(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"
    
    def is_available(self):
        return self._available_copies > 0
    
    def borrow(self):
        if self.is_available():
            self._available_copies -= 1
            return True
        return False
    
    def return_book(self):
        if self._available_copies < self._copies:
            self._available_copies += 1
            return True
        return False
    
    def get_availability(self):
        return f"{self._available_copies}/{self._copies} copies available"

class EBook(Book):
    def __init__(self, title, author, isbn, file_size, format_type="PDF"):
        super().__init__(title, author, isbn, copies=float('inf'))  # Unlimited copies
        self.file_size = file_size
        self.format_type = format_type
    
    def download(self):
        return f"Downloading {self.title} ({self.file_size}MB, {self.format_type})"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Digital ({self.format_type}, {self.file_size}MB)"
    
    def is_available(self):
        return True  # EBooks are always available

class AudioBook(Book):
    def __init__(self, title, author, isbn, duration, narrator):
        super().__init__(title, author, isbn, copies=float('inf'))  # Unlimited copies
        self.duration = duration
        self.narrator = narrator
    
    def play(self):
        return f"Playing '{self.title}' narrated by {self.narrator}"
    
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} - Audiobook ({self.duration}, narrated by {self.narrator})"
    
    def is_available(self):
        return True  # Audiobooks are always available

class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []  # Private attribute
    
    def add_book(self, book):
        self.__books.append(book)
        print(f"Added: {book.get_info()}")
    
    def find_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_books(self):
        print(f"\n--- {self.name} Catalog ---")
        for i, book in enumerate(self.__books, 1):
            print(f"{i}. {book.get_info()}")
            print(f"   {book.get_availability()}")
    
    def borrow_book(self, title):
        book = self.find_book(title)
        if book:
            if book.borrow():
                return f"You borrowed: {book.get_info()}"
            else:
                return f"Sorry, '{title}' is not available"
        return f"Book '{title}' not found"
    
    def return_book(self, title):
        book = self.find_book(title)
        if book:
            if book.return_book():
                return f"Thank you for returning: {book.get_info()}"
            else:
                return f"Error: All copies of '{title}' are already returned"
        return f"Book '{title}' not found"

# Demonstration
def main():
    # Create a library
    library = Library("Central City Library")
    
    # Add different types of books (Polymorphism)
    books = [
        Book("The Python Programming Language", "Guido van Rossum", "978-0134034287", 3),
        EBook("Digital Minimalism", "Cal Newport", "978-0525542872", 2.5, "EPUB"),
        AudioBook("Atomic Habits", "James Clear", "978-0735211292", "5h 35m", "James Clear"),
        Book("Clean Code", "Robert Martin", "978-0132350884", 2)
    ]
    
    for book in books:
        library.add_book(book)
    
    # Display catalog
    library.list_books()
    
    # Borrow books
    print(f"\n{library.borrow_book('Clean Code')}")
    print(f"{library.borrow_book('Digital Minimalism')}")
    print(f"{library.borrow_book('Clean Code')}")  # Second copy
    print(f"{library.borrow_book('Clean Code')}")  # Third copy
    print(f"{library.borrow_book('Clean Code')}")  # Should fail
    
    # Show updated catalog
    library.list_books()
    
    # Return a book
    print(f"\n{library.return_book('Clean Code')}")
    
    # Special methods for digital books
    ebook = library.find_book("Digital Minimalism")
    if isinstance(ebook, EBook):
        print(f"\n{ebook.download()}")
    
    audiobook = library.find_book("Atomic Habits")
    if isinstance(audiobook, AudioBook):
        print(f"{audiobook.play()}")

if __name__ == "__main__":
    main()
```

**Expected Output:**
```
Added: 'The Python Programming Language' by Guido van Rossum (ISBN: 978-0134034287)
Added: 'Digital Minimalism' by Cal Newport (ISBN: 978-0525542872) - Digital (EPUB, 2.5MB)
Added: 'Atomic Habits' by James Clear (ISBN: 978-0735211292) - Audiobook (5h 35m, narrated by James Clear)
Added: 'Clean Code' by Robert Martin (ISBN: 978-0132350884)

--- Central City Library Catalog ---
1. 'The Python Programming Language' by Guido van Rossum (ISBN: 978-0134034287)
   3/3 copies available
2. 'Digital Minimalism' by Cal Newport (ISBN: 978-0525542872) - Digital (EPUB, 2.5MB)
   inf/inf copies available
3. 'Atomic Habits' by James Clear (ISBN: 978-0735211292) - Audiobook (5h 35m, narrated by James Clear)
   inf/inf copies available
4. 'Clean Code' by Robert Martin (ISBN: 978-0132350884)
   2/2 copies available

You borrowed: 'Clean Code' by Robert Martin (ISBN: 978-0132350884)
You borrowed: 'Digital Minimalism' by Cal Newport (ISBN: 978-0525542872) - Digital (EPUB, 2.5MB)
You borrowed: 'Clean Code' by Robert Martin (ISBN: 978-0132350884)
Sorry, 'Clean Code' is not available

--- Central City Library Catalog ---
1. 'The Python Programming Language' by Guido van Rossum (ISBN: 978-0134034287)
   3/3 copies available
2. 'Digital Minimalism' by Cal Newport (ISBN: 978-0525542872) - Digital (EPUB, 2.5MB)
   inf/inf copies available
3. 'Atomic Habits' by James Clear (ISBN: 978-0735211292) - Audiobook (5h 35m, narrated by James Clear)
   inf/inf copies available
4. 'Clean Code' by Robert Martin (ISBN: 978-0132350884)
   0/2 copies available

Thank you for returning: 'Clean Code' by Robert Martin (ISBN: 978-0132350884)

Downloading Digital Minimalism (2.5MB, EPUB)
Playing 'Atomic Habits' narrated by James Clear
```

---

## Summary

Congratulations! You've learned the fundamental concepts of Object-Oriented Programming in Python:

### Key Concepts Covered:

1. **Classes and Objects**: Templates (classes) and instances (objects)
2. **Attributes and Methods**: Data storage and functionality
3. **Constructor (`__init__`)**: Setting up object initial state
4. **Encapsulation**: Bundling data and methods, controlling access
5. **Inheritance**: Creating new classes based on existing ones
6. **Polymorphism**: Same interface, different implementations

### Best Practices:

- Use descriptive class and method names
- Keep classes focused on a single responsibility
- Use encapsulation to protect internal data
- Leverage inheritance to reduce code duplication
- Design for polymorphism when you need flexibility

### Next Steps:

- Practice creating your own classes for real-world objects
- Learn about abstract classes and interfaces
- Explore advanced topics like decorators and metaclasses
- Study design patterns (Singleton, Factory, Observer, etc.)
- Build larger projects using OOP principles

Remember: OOP is a powerful tool for organizing code, but it's not always necessary for every problem. Use it when it makes your code cleaner, more maintainable, and easier to understand.

Happy coding! 🐍✨
