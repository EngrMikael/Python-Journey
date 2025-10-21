'''
Advanced: 5. Create a greenhouse control script:

Inputs: temperature, humidity, rain, light_level

If (temperature > 32 and humidity < 45) and not rain → print Irrigation + Cooling ON

Else if (rain or light_level < 10) → print Pause systems

Else → print Maintain monitoring.
'''

tempt = int(input("Enter Tempt: "))
hum = int(input("Enter Hum: "))
rain = (input("Is it raining: ")).lower()
light = int(input("Enter Light Values: "))

if rain == "yes":
    rain = True;
else: 
    rain = False

if (tempt > 32 and hum < 45) and rain == False:
    print("Irrigation and Cooling is turned ON")
elif (rain == False or light < 10):
    print("System is Paused!")
else:
    print("Maintain Monitoring")