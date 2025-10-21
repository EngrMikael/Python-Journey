device = input("input device: ")
sel_sliced = device[0:5]
user_sel_sliced = int(input("How many letters to be sliced: "))

if(sel_sliced == device[0:user_sel_sliced]):
    print("Match")
else:
    print("Mismatch")
    