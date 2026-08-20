"""
__len__()

Create a Library class containing books.

Make:

    len(library)

return the number of books.
"""


class Library:
    """Represent a library."""

    def __init__(self, books: list[str]) -> None:
        self.books = books

    def __len__(self) -> int:
        return len(self.books)


def main() -> None:
    """Run the main program."""
    books = ["SQL", "Python", "DSA"]
    library = Library(books=books)
    print(f"Number of Books: {len(library)}")


if __name__ == "__main__":
    main()
