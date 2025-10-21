'''
Positive-even checker — Write a program that asks for a number and prints
"Positive even" if the number is > 0 and divisible by 2, otherwise prints "Other"
'''

num = int(input("Enter a Number: "))

if num % 2 == 0 and num > 0:
    print("The number is Positive Even")
else:
    print("Others")
