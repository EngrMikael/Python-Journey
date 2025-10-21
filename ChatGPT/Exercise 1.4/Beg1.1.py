'''
Ask for temperature and humidity.

If temperature > 30 and humidity < 50: print Activate fan.

Else: print Stable environment.
'''

Tempt = int(input("Enter Temperature: "))
Hum = int(input("Enter Humidity: "))

if Tempt > 30 and Hum < 50:
    print("Activating Fan!")
else:
    print("The Environment is Stable")