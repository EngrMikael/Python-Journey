def calculate_two_num(num1, num2, operator):
    if operator == "+":
        answer = num1 + num2
        return answer
    elif operator == "-":
        answer = num1 - num2
        return answer
    elif operator == "/":
        answer = num1 / num2
        return answer
    elif operator == "*":
        answer = num1 * num2
        return answer
    else:
        answer = "invalid operator and numbers"
        return answer


num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))
operator = input("Enter Operator: (+, -, /, *): ")

result = calculate_two_num(num1, num2, operator)
print(f"The Result is: {result}")


# this script is not very pythonic is it?