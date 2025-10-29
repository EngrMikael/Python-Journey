# Exercise 1: Define & Access Properties

# Create a class Car that has:

# Instance properties: brand, year

# Class property: wheels = 4

# Then:

# Create two car objects.

# Print their brand, year, and number of wheels.

# Expected Behavior:
# Each car has its own brand/year, 
# but they both share the same number of wheels.
<<<<<<< HEAD
class Car:
    wheels = 4
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def display_info(self):
        print(f"\nBrand: {self.brand}\nYear: {self.year}\nWheel Count: {self.wheels}")

car1_brand = input("Enter Brand for Car 1: ")
car1_year = input("Enter Year for Car 1: ")
car1_info = Car(car1_brand, car1_year)
car2_brand = input("Enter Brand for Car 2: ")
car2_year = input("Enter Year for Car 2: ")
car2_info = Car(car2_brand, car2_year)
car1_info.display_info()
car2_info.display_info()
=======
# i was busy today i will not be able to update
>>>>>>> 76f171a0ed27acc3be6d1a0e2ad47953caa85608
