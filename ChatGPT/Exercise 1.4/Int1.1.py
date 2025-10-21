'''
Intermediate: 1. Simulate a smart lighting system:

Inputs: light_sensor (True/False), motion (True/False)

If both True → print Light ON

If only one True → print Half power mode

Else → print Light OFF
'''

light_sensor = input("Did the Light Sensor Detect Light? (y/n) ")
motion_sensor = input("Is there Movements? (y/n)  ")


if light_sensor == "y":
    light_sensor = True
else:
    light_sensor = False
    
if motion_sensor == "y":
    motion_sensor = True
else:
    motion_sensor = False
    

if light_sensor == True and motion_sensor == True:
    print("Light On")
elif light_sensor == True or motion_sensor == True:
    print("Half Power Mode")
else:
    print("Light Off")