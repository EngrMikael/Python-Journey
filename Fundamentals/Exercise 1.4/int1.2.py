'''
Smart home AC control:

Inputs: temperature, humidity, window_open (True/False)

If temperature > 30 and humidity > 70 and not window_open: print AC ON

Else: print AC OFF

'''

tempt = int(input("Enter Temperature: "))
hum = int(input("Enter Humidity: "))
window = (input("Enter Status of Widow: (Open/Close)")).lower()

if window == "open":
    window = True
else:
    window = False

if tempt > 30 and hum > 70 and window != False:
    print("AC is Turned ON!")
else:
    print("AC OFF")