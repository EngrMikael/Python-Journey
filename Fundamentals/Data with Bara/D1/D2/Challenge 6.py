# Generate a random integer between 1 and 100,
# and check if the result is an even number
# i tried to make this as readable as posible that i know how
# i used formatted string and a ternary

import random

random_number = random.randint(1, 100)

print(f"Even number: {random_number}") if random_number % 2 == 0 else print(f"Odd Number: {random_number}")
    