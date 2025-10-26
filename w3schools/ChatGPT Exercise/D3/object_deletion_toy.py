# Exercise 7 — Deleting Objects

# Create a class Toy that prints "Toy created!" 
# when initialized.
# Then delete the object 
# using del and see what happens when you 
# try to print it again.
class Toy:
    def __init__(self, name):
        self.name = name
    def display_object(self):
        print(f"Toy Name: {self.name}")
    def delete_object(self):
        print(f"Toy Deleted: {self.name}")
        del self.name
        

toy = input("Enter Toy: ")
toy_create = Toy(toy)
del_dis = int(input("Do you want to delete or view? (1/2): "))
if del_dis == 1:
    toy_create.delete_object()
elif del_dis == 2:
    toy_create.display_object()
else:
    print("Unavailabe Input!")