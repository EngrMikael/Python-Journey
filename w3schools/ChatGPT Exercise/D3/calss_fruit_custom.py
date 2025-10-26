# Exercise 6 — Custom Self Name

# Create a class Fruit where you don’t use self 
# as the parameter name.

# Example: use this or obj instead.
# The class should print a message 
# showing the fruit name when created.

class Fruit:
    def __init__(this, name):
        this.name = name
    def display_fruit(this):
        print(f"Fruit name: {this.name}")

input_fruit = input("Enter Fruit Name: ")
fruit_info = Fruit(input_fruit)
fruit_info.display_fruit()