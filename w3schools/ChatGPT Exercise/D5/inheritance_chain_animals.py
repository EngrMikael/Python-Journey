# Exercise 4 — Multi-level Inheritance

# Goal: Build a small inheritance chain.

# Instructions:

# Create a new class Puppy that inherits from Dog.

# Add a new property age and a method 
# introduce() that prints something like:
# "I am a 2-year-old Beagle!"

# Create a Puppy object and 
# call all available methods from 
# Animal, Dog, and Puppy.

# Expected Output Example:

# Dog makes a sound
# Woof! Woof!
# I am a 2-year-old Beagle!

class Animal:
    def __init__(self, species):
        self.species = species
    def sound(self):
        print("Some Generic Sound")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed
    def sound(self):
        print("Dog makes a sound")
    def bark(self):
        print("Woof! " * 2)
        
class Puppy(Dog):
    def __init__(self, species, breed, age):
        super().__init__(species, breed)
        self.age = age
    def puppy_greet(self):
        print(f"I am a {self.age}-year-old {self.breed}!")
puppy1 = Puppy("Canine", "Beagle", 2)
puppy1.sound()       
puppy1.bark()        
puppy1.puppy_greet() 