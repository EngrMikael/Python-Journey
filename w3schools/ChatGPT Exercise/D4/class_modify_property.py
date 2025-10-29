# Exercise 3: Modify Class Property

# Now:

# Change Car.wheels to 6

# Print both cars’ wheels again.

# Hint: This should affect all cars 
# (unless they have their own instance version).

class Car:
    wheels = 4
    def __init__(self, model, year = 2025):
        self.model = model
        self.year  = year
    def display_info(self):
        print(f"\nModel: {self.model}\nYear: {self.year}\nWheels: {self.wheels}")
car1_model = input("Enter Model: ")
car1_info = Car(car1_model)
car2_model = input("Enter Model: ")
car2_info = Car(car2_model)
car1_info.display_info()
car2_info.display_info()
Car.wheels = 6
car1_info.display_info()
car2_info.display_info()