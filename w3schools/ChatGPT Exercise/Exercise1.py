class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
input_name = input("Enter your Name: ")
input_age = int(input("Enter your Age: "))

person1 = Person(input_name, input_age)

print(f"Hello! {person1.name}, you are {person1.age} years old")