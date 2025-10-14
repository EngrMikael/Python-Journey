# This Python code snippet is creating variables `device`, `cost`, and `wifi` with values "Raspberry
# Pi", 8000, and False respectively.
device = "Raspberry Pi"
cost = 8000
wifi = False

concat = "".join(["Device name: ", str(device), " Cost: ", str(cost), " Does it require Wi-Fi: ",str(wifi)])

'''
advanced version :
concat = f"Device name: {device} Cost: {cost} Does it require Wi-Fi: {wifi}"
'''
print(concat)