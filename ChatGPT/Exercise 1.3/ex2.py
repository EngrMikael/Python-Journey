'''
Exercise 2:
Ask the user for a number. Check if it’s:

Positive

Negative

Or Zero
'''
userIn = int(input("Enter Number: "))

if userIn > 0:
    print("Positive")
elif userIn < 0:
    print("Negative")
else:
    print("Zero")