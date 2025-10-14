'''
Exercise 3:
Given humidity = 75, check:

If humidity is above 80 → print "Too humid!"

If between 50 and 80 → print "Comfortable."

Else → print "Too dry!"
'''

humidity = int(input("Enter Humidity: "))

if humidity > 80:
    print("Too Humid!")
elif humidity >= 50 and humidity <= 80:
    print("Comfortable")
else:
    print("Too DRY!!")