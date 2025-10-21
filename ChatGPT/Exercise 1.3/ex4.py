'''
Exercise 4 (Challenge):
Simulate a simple weather station:

Ask user to input temperature and rain = True/False

If temperature < 25 and rain == True, print "Cool and rainy."

If temperature > 30 and rain == False, print "Hot and dry."

Otherwise, print "Mild weather."
'''
userInTem = int(input("Input Temperature: "))
userInR = input("Input Rain: ").strip().lower()

if userInR in ["true", "1", "yes", "y"]:
    userInR = True
else:
    userInR = False

if userInTem < 25 and userInR:
    print("Cool and Rainy")
elif userInTem > 30 and not userInR:
    print("Hot and Dry")
else:
    print("Mild Weather")
