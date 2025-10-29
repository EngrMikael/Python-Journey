# Exercise 5: Add New Properties

# For car1, add a new property:

# car1.color = "red"


# Then print it.
# Now print car2.color — what happens?

# Goal: Understand dynamic property addition.
class Car:
    def __init__(self, model, year = 2025):
        self.model = model
        self.year = year
car1_model = input("Enter Car 1 Model: ")
car2_model = input("Enter Car 2 Model: ")
car1_info = Car(car1_model)
car2_info = Car(car2_model)
car1_info.color = "Red"
print(f"\nCar 1 Color: {car1_info.color}")
print(f"Car 2 Color: {car2_info.color}")