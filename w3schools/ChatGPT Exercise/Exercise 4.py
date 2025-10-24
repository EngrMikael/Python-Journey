class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def life_stage(self):
        if self.age < 13:
            print(f"{self.name} is a child")
        elif self.age < 20:
            print(f"{self.name} is a teenager")
        elif self.age < 60:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is a senior")

name = input("Enter Your name: ")
age = int(input("Enter your age: "))

person = Person(name, age)
person.life_stage()