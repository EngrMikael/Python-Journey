# Exercise 9 — Multiple Parameters

# Create a class Employee that takes in name, 
# position, and salary, and has a method 
# to print all three in one formatted sentence.

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def display_info(self):
        print(f"\nEmployee Info:\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}")

employee_name = input("Enter Employee Name: ")
employee_position = input("Enter Position: ")
employee_salary = int(input("Enter Salary: "))

employee_info = Employee(employee_name, employee_position, employee_salary)
employee_info.display_info()