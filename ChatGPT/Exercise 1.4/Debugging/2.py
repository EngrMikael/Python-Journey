'''
motion = input("Motion? (True/False): ") == "True"
locked = input("Locked? (True/False): ") == "True"
if motion == True or locked == True:
    print("Unlocking door...")
else:
    print("Keep locked")
'''

motion = input("Motion? (True/False): ") == "True"
locked = input("Locked? (True/False): ") == "True"

if motion == "True":
    motion = True
else: 
    motion = False
if locked == "True":
    locked = True
else:
    locked = False
    
if motion == True or locked == True:
    print("Unlocking door...")
else:
    print("Keep locked")

