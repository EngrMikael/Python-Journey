# This Python code snippet prompts the user to enter a temperature value, which is then converted to a
# floating-point number using the `float()` function. The entered temperature value is stored in the
# variable `ins`.
ins = float(input("Enter the Temperature: "))
reading = f"The adjusted reading is {ins + 0.5}"
print(reading)