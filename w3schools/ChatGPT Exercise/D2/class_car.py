# Exercise 1 — Class Creation

# Create a class named Car that has:

# A property brand

# A property model

# Then create two objects from that class 
# and display their brand and model.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print(f"\nBrand: {self.brand} \nModel: {self.model}")

car1_brand = input("Enter Brand: ")
car1_model = input("Enter Model: ")
car2_brand = input("Enter Brand: ")
car2_model = input("Enter Model: ")

car1_info = Car(car1_brand, car1_model)
car2_info = Car(car2_brand, car2_model)

car1_info.display_info()
car2_info.display_info()