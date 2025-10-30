# Exercise 2 — Using super()

# Goal: Extend functionality while keeping inheritance.

# Instructions:

# Modify the Dog class to include 
# its own __init__() method that 
# adds a property breed.

# Use super().__init__() to inherit 
# the species property from Animal.

# Create a dog named “Beagle” 
# with species “Canine”.

# Print both properties.

# Expected Output Example:

# Species: Canine
# Breed: Beagle

class Animal:
    def __init__(self, species):
        self.species = species
    def sound(self):
        print("Some generic sound")
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

dog1 = Dog("Canine", "Beagle")
print(f"Breed: {dog1.breed}")
print(f"Species: {dog1.species}")