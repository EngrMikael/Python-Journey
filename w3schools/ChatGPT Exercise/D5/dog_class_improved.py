# Exercise 3 — Add Methods and Override

# Goal: Add a unique method and override an inherited one.

# Instructions:

# In the Dog class, create a method called bark() 
# that prints "Woof! Woof!".

# Override the parent’s sound() method 
# so it prints "Dog makes a sound".

# Create an object of Dog and call both sound() 
# and bark().

# Expected Output Example:

# Dog makes a sound
# Woof! Woof!

class Animal:
    def __init__(self, species):
        self.species = species
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed
    def sound(self):
        print("Dog makes a Sound")
    def bark(self):
        print("Woof!" * 2)
dog1 = Dog("Canine", "Beagle")

dog1.sound()
dog1.bark()