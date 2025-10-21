
'''
Greenhouse Manager (full script) Build a script that asks for these inputs:

temperature (float)

humidity (float)

rain (True/False)

light_level (0-100)

soil_moisture (0-100)

Requirements (implement as a clear, maintainable single script):

If (temperature > 32 and humidity < 45) and not rain and soil_moisture < 30 → print "Irrigation + Cooling ON".

Else if rain or soil_moisture >= 30 → print "Irrigation OFF - soil OK or raining".

If light_level < 15 or (temperature > 30 and humidity < 40) → print "Grow lights ON" (this can be independent of irrigation decision).

The script should print a clear summary at the end listing which systems are ON and which are OFF.

this was documented using 'Mintlify Doc Writer'
'''
# The lines `irrigation_on = False`, `cooling_on = False`, `grow_light_state = False`, and `isRain =
# False` are initializing variables to store the state of different systems in the greenhouse. Here's
# what each variable represents:
irrigation_on = False
cooling_on = False
grow_light_state = False
isRain = False

# The code snippet you provided is responsible for taking user inputs for various environmental
# factors related to a greenhouse. Here's what each line does:
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
rain = input("Is it Raining? (y/n): ").lower().strip()
light_level = int(input("Enter Light Level: (0-100): "))
soil_moisture = int(input("Enter Soil Moisture Level: (0-100): "))

# `isRain = rain == "y"` is a line of code that checks if the user input for rain is equal to "y". It
# assigns the result of this comparison (True or False) to the variable `isRain`. This way, `isRain`
# will be True if the user input for rain is "y" and False otherwise. This helps in determining
# whether it is raining or not based on the user input.
isRain = rain == "y"

# The code snippet you provided is implementing the logic for the irrigation system based on the given
# requirements for a greenhouse manager script. Here's a breakdown of what the code does:
#Irrigation system
if (temperature > 32 and humidity < 45) and not isRain and soil_moisture < 30:
    print("Irrigation + Cooling ON")
    irrigation_on = True
    cooling_on = True

elif isRain or soil_moisture >= 30:
    print("Irrigation OFF! Soil OK or Raining")

else:
    print("Irrigation OFF - Conditions not met")

# The code snippet you provided is determining the state of the grow lights in the greenhouse based on
# the given conditions. Here's a breakdown of what the code does:
#Grow Light State
if light_level < 15 or (temperature > 30 and humidity < 40):
    print("Grow Lights ON!")
    grow_light_state = True
else: 
    print("Grow Lights OFF!")

# The code snippet you provided with `#System Status` and the subsequent lines is responsible for
# printing a summary of the current status of different systems in the greenhouse based on the
# conditions evaluated earlier in the script.
#System Status
print("\n====System Status Summary====")
print(f"Irrigation: {'ON' if irrigation_on else 'OFF'}")
print(f"Cooling: {'ON' if cooling_on else 'OFF'}")
print(f"Grow Lights: {'ON' if grow_light_state else 'OFF'}")
print("=============================")