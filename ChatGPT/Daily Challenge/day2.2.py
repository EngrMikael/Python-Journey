'''
Level 2: “Even or Odd Reporter” (For loop + conditional)
Problem:

Given a list of numbers, print:

"<num> is even" if divisible by 2

"<num> is odd" if not

Example:
numbers = [3, 7, 10, 22, 15]


Expected output:

3 is odd
7 is odd
10 is even
22 is even
15 is odd

Hint:

Use % (modulo) operator and a simple for loop.

Goal: Practice looping through lists and applying conditional logic to each item.
Documented using Mintlify Doc Writer
'''


# The line `numbers = [int(x.strip()) for x in input("Enter 5 numbers separated by commas:
# ").split(",")]` is creating a list called `numbers` by taking input from the user.
numbers = [int(x.strip()) for x in input("Enter 5 numbers separated by commas: ").split(",")]

# This code snippet is iterating through each element in the `numbers` list using a for loop.
for i in range(len(numbers)):
    if numbers[i] == 0:
        print(numbers[i], ": Zero")
    elif numbers[i] % 2 == 0:
        print(numbers[i], ": even")
    else:
        print(numbers[i], ": odd")
