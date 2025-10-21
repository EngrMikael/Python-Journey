device = "RaspberryPi"
print(device + " Model 5") # Concatenation
print(device * 2) # Repeat twice
print(device[0:5]) # Slice (first 5 letters)

spliced = device[0:5]
print(spliced)

if(device[0:5] == spliced):
    print(1)
else: 
    print(0)