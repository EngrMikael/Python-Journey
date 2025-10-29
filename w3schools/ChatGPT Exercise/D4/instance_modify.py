# Exercise 2: Modify Instance Properties

# Using your Car class:

# Change the year of only one car.

# Print both cars’ years — notice what happens.

# Hint: Instance properties 
# belong to each object individually.

class Car:
    def __init__(self, model, year = 2025):
        self.model = model
        self.year = year
    def display_info(self):
        print(f"\nModel: {self.model}\nYear: {self.year}")

car1_model = input("Enter Model: ")
car1_year = int(input("Enter Year: "))
car1_info = Car(car1_model, car1_year)
car2_model = input("Enter Model: ")
car2_info = Car(car1_model)
car1_info.display_info()
car2_info.display_info()