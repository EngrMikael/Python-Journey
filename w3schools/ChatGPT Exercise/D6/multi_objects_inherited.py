# Exercise 7 — Inheritance and Lists

# Goal: Store multiple objects and access 
# inherited methods.

# Instructions:

# Create a parent class Person with name and age.

# Create a child class Teacher that inherits 
# from Person and adds a subject property.

# Create a list of 3 teachers and use a loop 
# to print their names and subjects.

# Expected Output Example:

# Mr. Lee teaches Math
# Ms. Cruz teaches Science
# Mrs. Torres teaches English

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
p1 = Teacher("Mr. Lee", 30, "Math")
p2 = Teacher("Ms. Cruz", 30, "Science")
p3 = Teacher("Mrs. Torres", 30, "English")

teacher_list = [p1, p2, p3]
for teacher in teacher_list:
    print(f"{teacher.name} teaches {teacher.subject}")