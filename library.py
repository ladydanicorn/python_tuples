# Assignment 2

#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data 
# within tuples and lists.

#Problem Statement: You are maintaining a library system where each book is stored as 
# a tuple within a list. Your task is to update this system by adding new books 
# and ensuring no duplicates.

#Existing Library Data:

#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#- Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.

def add_book(library, title, author):
    # tuple for new books
    new_book = (title, author)

    #check if in library
    for book in library:
        if book == new_book:
            print(f"{title} by {author} already exists.")
            return library
        
    # add new book 
    library.append(new_book)
    print(f"Add {title} by {author} to the library.")

    return library

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# add books

library = add_book(library, "Super Real Book", "Real Person Jr.")
library = add_book(library, "Book Titles for Dummies", "Dr. Dude")
library = add_book(library, "1984", "George Orwell") #duplicate for test

print("\nUpdated Library:")
for book in library:
    print(f"'{book[0]}' by {book[1]}")
