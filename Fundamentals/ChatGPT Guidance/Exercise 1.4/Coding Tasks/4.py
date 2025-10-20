'''
AC controller — Inputs: temp, humidity, window_open (True/False).

If temp > 30 and humidity > 70 and not window_open → AC ON

If window_open → Ventilation only

Else → AC OFF
'''
temp = int(input("Enter Temperature: "))
hum = int(input("Enter Humidity: "))
win_state = input("Is the Window Open? (y/n): ").lower()

if win_state == "y":
    win_state = True
else:
    win_state = False

if temp > 30 and hum > 70 and win_state == False: 
    print("AC ON!")
elif win_state == True:
    print("Ventilation Only!")
else:
    print("AC OFF!")