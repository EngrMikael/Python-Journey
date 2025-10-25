# Exercise 3 — Default Values

# Create a class Pet with:

# name and animal_type parameters

# Default value for animal_type should be "Dog"
# Create two objects — one with the default type, 
# and one with a custom type.

class Pet:
    def __init__(self, name, animal_type = "Dog"):
        self.name = name
        self.animal_type = animal_type
    def pet_info(self):
        print(f"\nPet Name: {self.name}\nPet Type: {self.animal_type}")
        
pet1_name = input("Enter pet 1's Name: ")
pet2_name = input("Enter pet 2's Name: ")
pet2_type = input("Enter pet 2's Type: ")

pet1_stat = Pet(pet1_name)
pet2_stat = Pet(pet2_name, pet2_type)
pet1_stat.pet_info()
pet2_stat.pet_info()