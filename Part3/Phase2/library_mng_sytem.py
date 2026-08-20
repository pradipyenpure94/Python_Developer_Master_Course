"""
Library Management System

Create:

    Book
    Member
    Library

Implement:

    add book
    search book
    issue book
    return book
    display books

Use OOP principles wherever appropriate.
"""


class Book:
    """Represent a book."""

    def __init__(self, book_id: int, title: str, author: str) -> None:
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.issued_to = None

    def __str__(self) -> str:
        """Return book information."""

        status = "Available" if self.is_available else "Issued"
        issued_to = self.issued_to.name if self.issued_to else "Nobody"
        return (
            f"Book ID    : {self.book_id}\n"
            f"Title      : {self.title}\n"
            f"Author     : {self.author}\n"
            f"Status     : {status}\n"
            f"Issued To  : {issued_to}"
        )


class Member:
    """Represent a library member."""

    def __init__(self, member_id: int, name: str) -> None:
        self.member_id = member_id
        self.name = name

    def __str__(self) -> str:
        """Return the member information."""
        return (
            f"Member ID: {self.member_id}\n"
            f"Member Name: {self.name}"
        )


class Library:
    """Represent a library."""

    def __init__(self) -> None:
        self.books: list[Book] = []
        self.members: list[Member] = []

    def add_member(self, member: Member) -> None:
        """Add member to the library."""
        self.members.append(member)

    def add_book(self, book: Book) -> None:
        """Add book to the library."""
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def search_book(self, title: str) -> None:
        """Search for a book by title."""
        for book in self.books:
            if book.title.casefold() == title.casefold():
                print("-" * 40)
                print("Book Found.")
                print(book)
                print("-" * 40)
                return
        print(f"Book {title} not found.")

    def issue_book(self, book_id: int, member: Member) -> None:
        """Issue an available book."""
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    book.issued_to = member
                    print(
                        f"Book '{book.title}' issued to "
                        f"{member.name} successfully.")
                else:
                    print(f"Book '{book.title}' is already issued.")
                return
        print(f"{book_id} not found.")

    def return_book(self, book_id: int) -> None:
        """Return an issued book."""
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    book.issued_to = None
                    print(f"Book {book.title} returned successfully.")
                else:
                    print(f"Book {book.title} is already available.")
                return
        print(f"Book ID {book_id} not found.")

    def display_books(self) -> None:
        """Display all books."""
        if not self.books:
            print("No books available in the library.")
            return

        print("-" * 40)
        print("Library Books")
        print("-" * 40)
        for book in self.books:
            print(book)
            print("-" * 40)


def main() -> None:
    """Run the library management system."""

    library = Library()

    book1 = Book(book_id=101, title="SQL", author="ABC")
    book2 = Book(book_id=102, title="DSA", author="ABC")
    book3 = Book(book_id=103, title="Python", author="ABC")

    member = Member(member_id=1, name="Pradip")

    library.add_book(book=book1)
    library.add_book(book=book2)
    library.add_book(book=book3)

    print()
    library.add_member(member=member)
    print()

    library.display_books()
    print()

    library.search_book(title="DSA")
    print()

    library.issue_book(book_id=102, member=member)
    print()

    library.display_books()
    print()

    library.return_book(book_id=102)
    print()

    library.display_books()


if __name__ == "__main__":
    main()
