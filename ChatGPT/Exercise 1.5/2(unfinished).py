# in this script i want to know if i can use 2 different functions
# on another function without external help(AI or search)

def greet(name, age, sex):
    greeting = f"Hello {name}, I see that you're {age}, and a {sex}"
    return greeting


name = input("What's your name: ")
age = int(input("How old are you: "))
sex = input("Enter Sex: (male/female): ")

print(greet(name, age, sex))