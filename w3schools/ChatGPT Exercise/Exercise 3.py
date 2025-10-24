class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print(f"Hi! My name is {self.name}, and I'm {self.age} years old.")
            
name = input("Enter your name: ")
age = int(input("Enter your age: "))

p = Person(name, age)
p.introduce()