# Exercise 10 — DRY Principle in Action

# Imagine you have to print the details of 
# three products (name, price, stock)
# Instead of repeating print statements, 
# use a class to store and display them neatly.


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def display_market(self):
        print(f"\nStock info: \nName: {self.name}\nPrice: {self.price}\nStock: {self.stock}")

stock_name = input("Enter Stock Name: ")
stock_price = int(input("Enter Price: "))
stock_stock = input("Enter Stock: ")  

stock_info = Product(stock_name, stock_price, stock_stock)
display = input("Do you want to display Stock info? (y/n): ").strip().lower()

if display == "y":
    stock_info.display_market()
elif display == "n":
    print("Bye")
else:
    print("Invalid Input")