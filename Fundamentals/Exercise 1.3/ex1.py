'''
Exercise 1:
Create a program that checks the temperature:

If above 30, print: "Turn on cooling system."

If below 20, print: "Turn on heating system."

Otherwise, print: "Temperature is normal."

'''
userIn = int(input("Enter Temp: "))

if userIn > 30:
    print("Turn on Cooling System!")
elif userIn < 20:
    print("Turn on Heating System!")
else:
    print("Temperature is Normal :)")
    
'''

a higher level, to battle the exception errors
try:
    userIn = int(input("Enter Temp: "))

    if userIn > 30:
        print("Turn on Cooling System!")
    elif userIn < 20:
        print("Turn on Heating System!")
    else:
        print("Temperature is Normal :)")
except ValueError:
    print("Invalid Input")

'''
