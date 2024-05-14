class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        status = "Available" if not self.is_borrowed else "Borrowed"
        print(f"Status: {status}")
        print()

    def borrow(self):
        if self.is_borrowed:
            print("This book is already borrowed.")
        else:
            self.is_borrowed = True
            print("Book borrowed successfully.")

    def return_book(self):
        if not self.is_borrowed:
            print("This book is not currently borrowed.")
        else:
            self.is_borrowed = False
            print("Book returned successfully.")
