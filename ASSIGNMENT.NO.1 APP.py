class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_book(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id}, Title: {self.title}, "
              f"Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display_patron(self):
        print(f"ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print("Patron registered successfully.")

    def borrow_book(self, book_id, patron_id):
        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book is None:
            print("Book not found.")
        elif patron is None:
            print("Patron not found.")
        elif not book.is_available:
            print("Book is already borrowed.")
        else:
            book.is_available = False
            patron.borrowed_books.append(book.title)
            print(f"'{book.title}' borrowed successfully by {patron.name}.")

    def return_book(self, book_id, patron_id):
        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book is None:
            print("Book not found.")
        elif patron is None:
            print("Patron not found.")
        elif book.title not in patron.borrowed_books:
            print("This book was not borrowed by this patron.")
        else:
            book.is_available = True
            patron.borrowed_books.remove(book.title)
            print(f"'{book.title}' returned successfully.")

    def display_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_book()

    def display_patrons(self):
        print("\n--- Registered Patrons ---")
        for patron in self.patrons:
            patron.display_patron()


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice. Please try again.")
