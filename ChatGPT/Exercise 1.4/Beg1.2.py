'''

Ask if the user has money and if store_open.

If both True: print Go shopping!

Else: print Maybe later.
'''

balance = input("Do you have Money? (y/n)").lower()
stats = input("Is the Shop Open? (y/n)").lower

if balance == "y" and stats == "y":
    print("Go Shopping!")
else:
    print("Maybe Later! Brokeeeee")