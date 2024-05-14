from book import Book
from library import Library

# Creating book instances
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("1984", "George Orwell", 1949)

# Creating library instance
library = Library()

# Adding books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying all books in the library
library.display_books()

# Borrowing a book
book1.borrow()

# Displaying book info
book1.display_info()

# Returning a book
book1.return_book()

# Displaying book info
book1.display_info()

# Removing a book
library.remove_book(book2)

# Displaying all books in the library
library.display_books()
