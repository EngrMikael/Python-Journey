# LEVEL 2 — Deep Dive
# 🧩 Exercise 4: Class vs Instance Shadowing

# Add this to your Car test:

# car1.wheels = 8

# Then print:

# print(car1.wheels)
# print(car2.wheels)
# print(Car.wheels)


# Question: Why is car1’s value 
# different from the rest?

# (Hint: You “shadowed” the class property 
# by creating a new instance property.)
class Car:
    wheels = 4
    def __init__(self, model, year = 2025):
        self.model = model
        self.year = year
    def display_info(self):
        print(f"\nModel: {self.model}\nYear: {self.year}\nWheels: {self.wheels}")
car1_model = input("Enter Car1 Model: ")
car1_info = Car(car1_model)
car2_model = input("Enter Car2 Model: ")
car2_info = Car(car2_model)
car2_info.wheels = 8
print(car1_info.wheels)
print(car2_info.wheels)
print(Car.wheels)