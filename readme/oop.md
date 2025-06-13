# Object-Oriented Programming (OOP) in Python: A Comprehensive Guide

## Table of Contents

- [Introduction](#introduction)
- [What is OOP?](#what-is-oop)
- [Classes and Objects](#classes-and-objects)
- [Defining a Class](#defining-a-class)
- [Creating Objects (Instances)](#creating-objects-instances)
- [Instance Attributes and Methods](#instance-attributes-and-methods)
- [The **init** Method (Constructor)](#the-__init__-method-constructor)
- [Class Attributes and Methods](#class-attributes-and-methods)
- [Inheritance](#inheritance)
- [Method Overriding](#method-overriding)
- [Encapsulation and Private Members](#encapsulation-and-private-members)
- [Real-World Example: Modeling a Bank Account](#real-world-example-modeling-a-bank-account)
- [Conclusion](#conclusion)

---

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes. It helps you model real-world entities, reuse code, and build more maintainable programs.

---

## What is OOP?

OOP is based on four main principles:

- **Encapsulation**: Bundling data and methods together.
- **Abstraction**: Hiding complex details and showing only the essentials.
- **Inheritance**: Creating new classes from existing ones.
- **Polymorphism**: Using a unified interface for different data types.

---

## Classes and Objects

- **Class**: A blueprint for creating objects.
- **Object**: An instance of a class.

---

## Defining a Class

Use the `class` keyword to define a class.

```python
class Dog:
    pass  # An empty class
```

---

## Creating Objects (Instances)

Create an object by calling the class as if it were a function.

```python
my_dog = Dog()
```

---

## Instance Attributes and Methods

Attributes and methods defined inside a class belong to each object (instance).

```python
class Dog:
    def bark(self):
        print("Woof!")

my_dog = Dog()
my_dog.bark()  # Output: Woof!
```

---

## The **init** Method (Constructor)

The `__init__` method initializes new objects with default or user-provided values.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
```

---

## Class Attributes and Methods

Class attributes are shared by all instances. Use `@classmethod` for class methods.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    @classmethod
    def common_species(cls):
        return cls.species

print(Dog.common_species())  # Output: Canis familiaris
```

---

## Inheritance

A class can inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

my_dog = Dog()
my_dog.speak()  # Output: Woof!
```

---

## Method Overriding

A subclass can override methods from its parent class.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

my_cat = Cat()
my_cat.speak()  # Output: Meow!
```

---

## Encapsulation and Private Members

Prefix an attribute or method with an underscore `_` to indicate it is intended as private.

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private by convention
```

---

## Real-World Example: Modeling a Bank Account

Let's solve a real-world problem using OOP: modeling a simple bank account.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

account = BankAccount("Alice", 100)
account.deposit(50)      # Deposited $50. New balance: $150
account.withdraw(70)     # Withdrew $70. New balance: $80
account.withdraw(200)    # Insufficient funds!
```

---

## Conclusion

OOP helps you organize and structure your code for complex programs. Practice creating your own classes and objects to become a more effective Python programmer.
