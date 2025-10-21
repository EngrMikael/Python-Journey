'''
Level 1: “Temperature Monitor” (Basic if logic)
Problem:

Write a program that asks the user to input a temperature (in °C).
Then print:

"Too Cold" if below 20

"Just Right" if between 20–30

"Too Hot" if above 30

 Hint:

Use if, elif, and else.

Goal: Learn clean conditional structures and readable comparisons.

documented using "Mintlify Doc Writer"
'''

# `temperature = int(input("Enter Temperature °C: "))` is a line of code in Python that prompts the
# user to enter a temperature in degrees Celsius. The `input()` function takes user input as a string,
# and `int()` converts that input into an integer so that it can be compared with numerical values in
# the subsequent if-elif-else statements.
temperature = int(input("Enter Temperature °C: "))

# This block of code is implementing a basic temperature monitoring program in Python. Here's what
# each part does:
if temperature < 20:
    print("Too Cold")
elif 30 >= temperature >= 20:
    print("Just Right")
else:
    print("Too Hot")