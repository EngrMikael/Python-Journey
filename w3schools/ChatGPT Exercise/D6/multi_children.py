# Exercise 5 — Multiple Children

# Goal: Practice multiple child classes from 
# one parent.

# Instructions:

# Create a parent class Vehicle with 
# properties brand and year.

# Create two child classes: Car and Motorcycle.

# Both should inherit from Vehicle.

# Each child class should have its own unique method:

# Car → drive() prints "The car is driving."

# Motorcycle → ride() prints "The motorcycle is riding."

# Create one object of each and call their methods.

# Expected Output Example:

# The car is driving.

# The motorcycle is riding.
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Motorcycle(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)
    def ride(self):
        print("The motorcycle is riding.")
class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand, year)
    def drive(self):
        print("The car is driving.")

motor1 = Motorcycle("Honda", 2025)
car1 = Car("Toyota", 2025)
motor1.ride()
car1.drive()