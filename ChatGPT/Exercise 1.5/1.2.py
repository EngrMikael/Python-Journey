def calculate_two_num(num1, num2, operator):
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Invalid"
    }
    return operations.get(operator, "Invalid Operator")


num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
operator = input("Enter Operator: (+, -, /, *): ")

result = calculate_two_num(num1, num2, operator)
print(f"The Result is: {result}")