# Exercise 9 — Inheritance with Input

# Goal: Combine user input with inheritance.

# Instructions:

# Create a parent class Person with properties 
# firstname and lastname.

# Create a child class Student that inherits 
# from Person and adds a course property.

# Ask the user to input their 
# firstname, lastname, and course.

# Print a message like:
# "Hello, [firstname] [lastname]! Welcome to the 
# [course] course."

# Expected Output Example:

# Enter firstname: John
# Enter lastname: Doe
# Enter course: Computer Science
# Hello, John Doe! Welcome to the Computer 
# Science course.


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Student(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course
    def __str__(self):
        return f"Hello, {self.firstname} {self.lastname}! Welcome to the {self.course} course."
    
firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
course = input("Enter course: ")

student_info = Student(firstname, lastname, course)
print(student_info)