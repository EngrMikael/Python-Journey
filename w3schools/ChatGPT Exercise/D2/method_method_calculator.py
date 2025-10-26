# Exercise 5 — Method Calling Another Method

# Create a class Calculator with:

# A method add(a, b) that returns the sum

# A method display_sum(a, b) 
# that calls add() internally and prints the result

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def display_sum(self):
        add = [self.a, self.b]
        step_add = sum(add)
        print(f"Sum of {self.a} and {self.b} is {step_add}")
        
    
a_input = int(input("Enter first Value: "))
b_input = int(input("Enter second Value: "))
final = Calculator(a_input, b_input)
final.display_sum()

