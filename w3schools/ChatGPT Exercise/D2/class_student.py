# Using self

# Create a class Student that:

# Has properties name and grade

# Has a method show_info() that prints both
# Create an object and call show_info().

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def show_info(self):
        print(f"\nStudent Name: {self.name}\nGrade: {self.grade}")

p1_name = input("Enter Student 1's Name: ")
p1_grade = input("Enter Student 1's Grade: ")
p2_name = input("Enter Student 2's Name: ")
p2_grade = input("Enter Student 2's Grade: ")

p1_info = Student(p1_name, p1_grade)
p2_info = Student(p2_name, p2_grade)

p1_info.show_info()
p2_info.show_info()