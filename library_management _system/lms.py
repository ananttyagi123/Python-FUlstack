class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Not Available" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"'{title}' added to library.")

    def display_books(self):
        print("\n Available Books:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed & book.is_borrowed <= 3 :
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
                return
        print(f" Book '{title}' is not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
                return
        print(f" Book '{title}' not found or was not borrowed.")


# Example usage
library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

library.display_books()

library.borrow_book("1984")
library.display_books()

library.return_book("1984")
library.display_books()
