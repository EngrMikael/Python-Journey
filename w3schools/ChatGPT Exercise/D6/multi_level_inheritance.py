# Exercise 8 — Multi-level Inheritance (Extended)

# Goal: Deepen your understanding of inheritance chains.

# Instructions:

# Create 3 classes:

# Device → has a method power_on() that prints 
# "Device is now on."

# Computer(Device) → has a method boot() 
# that prints "Computer is booting...".

# Laptop(Computer) → has a method open_lid() 
# that prints "Laptop lid opened."

# Create a Laptop object and call all three methods.

# Expected Output Example:

# Device is now on.
# Computer is booting...
# Laptop lid opened.

class Device:
    def power_on(self):
        print("The device is now on.")
        
class Computer(Device):
    def boot(self):
        print("Computer is booting...")
        
class Laptop(Computer):
    def open_lid(self):
        print("Laptop lid opened.")
        
laptop1 = Laptop()

laptop1.power_on()
laptop1.boot()
laptop1.open_lid()