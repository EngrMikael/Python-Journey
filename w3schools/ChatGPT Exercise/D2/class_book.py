# Exercise 2 — Class with __init__()

# Create a class Book that:

# Has title and author as parameters in __init__()
# Automatically prints "Book created!" 
# when an object is made

# Then, create two book objects 
# with different titles and authors.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def book_creating(self):
        print(f"Book Created! \"{self.title}\"")

book1_title = input("Enter Book 1 Title: ")
book1_author = input("Enter Book 1 Author: ")
book1_shelfed = Book(book1_title, book1_author)
book1_shelfed.book_creating()

book2_title = input("Enter Book 2 Title: ")
book2_author = input("Enter Book 1 Author: ")
book2_shelfed = Book(book2_title, book2_author)
book2_shelfed.book_creating()