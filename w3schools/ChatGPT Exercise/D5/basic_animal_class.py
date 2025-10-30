# Exercise 1 — Basic Inheritance

# Goal: Create a parent and child class.

# Instructions:

# Create a class Animal with a property species 
# and a method sound() that prints 
# "Some generic sound".

# Create a child class Dog 
# that inherits from Animal.

# Create a Dog object, 
# and call its sound() method.

# Expected Output Example:

# Some generic sound

class Animal:
    def __init__(self, species):
        self.species = species
    def sound(self):
        print("Some generic sound")
class Dog(Animal):
    pass

dog = Dog("Brownie")
dog.sound()