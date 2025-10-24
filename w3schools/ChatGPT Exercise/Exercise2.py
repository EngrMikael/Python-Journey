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

print("\nList of People: ")
for p in people:
    print(f"{p.name} is {p.age} years old")