'''
Smart lighting — Inputs: motion (True/False), light_level (0-100). Rules:

If motion is True and light_level < 40 → Light ON

If motion is True and 40 <= light_level < 70 → Half power

If motion is False → Light OFF Write this with a mix of and/or and at least one
elif branch.
'''

motion = (input("Is there a movement? (y/n)")).lower()
light = int(input("Light Levels: (0-100)"))

if motion == "y":
    motion = True
else: 
    motion = False

if motion == True and light < 40:
    print("Light is Turned ON")
elif motion == True and 40 <= light < 70:
    print("Half Powered")
elif motion == False and 0 == light <= 100:
    print("Someone left the Lights ON, damn")
else:
    print("Light is turned OFF")