# Exercise 6 — Overriding with super()

# Goal: Combine method overriding with super().

# Instructions:

# Create a class Employee with a method info() 
# that prints "This is an employee."

# Create a class Manager that inherits 
# from Employee and overrides the info() method.

# Inside Manager’s info() method, use super().info() 
# before printing "This employee is a manager."

# Create a Manager object and call info().

# Expected Output Example:

# This is an employee.
# This employee is a manager.
class Employee:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("This is an employee")
class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
    def info(self):
        super().info()
        print("This employee is a manager.")
employee1 = Manager("Pips")
employee1.info()