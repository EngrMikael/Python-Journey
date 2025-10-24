class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
people = []

for i in range(3):
    name = input(f"Enter name of person {i+1}: ")
    age = int(input(f"Enter age of person {i+1}: "))
    person = Person(name, age)
    people.append(person)

for p in people:
    if p.age >= 18:
        print(f"{p.name} is {p.age}")
