"""
Library Management System (Mini Project)

Features:
    1. Add Book
    2. Remove Book
    3. Search Book
    4. Issue Book
    5. Return Book
    6. Store data in file
    7. Exception Handling
    8. Functions
    9. Dictionaries
    10. Loops
"""
from pathlib import Path

FILE_PATH = "Part1/library_mang_sys.txt"
FILE_NAME = Path(FILE_PATH).name
HEADERS = "id,name,total_qty,available_qty\n"


def create_txt_file() -> None:
    """Create a .txt File if not exist."""
    if not Path(FILE_PATH).exists():
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
        print(f"{FILE_NAME} is created successfully.")


def load_books_data() -> list[str]:
    """Fetch all books data."""
    try:
        with open(file=FILE_PATH, mode="r", encoding="utf-8") as file_obj:
            file_obj.readline()
            return file_obj.readlines()
    except PermissionError:
        print("Permission denied.")
        return []
    except OSError as error:
        print(f"Error: {error}")
        return []


def save_books_data(books: list[str]) -> None:
    """Saved books data into .txt File."""
    try:
        with open(file=FILE_PATH, mode="w", encoding="utf-8") as file_obj:
            file_obj.write(HEADERS)
            file_obj.writelines(books)
    except PermissionError:
        print("Permission denied.")
    except OSError as error:
        print(f"Error: {error}")


def validate_unique_book_name(name: str, books: list[str]) -> str | None:
    """
    Return a validate book name.

    Args:
        name (str): Input book name.

    Returns:
        str: Return a unique name otherwise None.

    Raises:
        ValueError: If not name raise error message.
    """
    if not name:
        raise ValueError("Name cannot be empty.")

    # Return a unique book name,
    book_lists = [
        parse_book_record(book=record)[1].casefold() for record in books]
    book_name = name.strip().casefold()
    if book_name not in book_lists:
        return book_name
    raise ValueError("Book name must be unique.")


def validate_book_quantity(quantity: int) -> None:
    """
    Validate book quantity.

    Args:
        quantity (int): Input book quantity.

    Raises:
        ValueError: If quantiy less than zero then raise error message.
    """
    if quantity <= 0:
        raise ValueError("Book quantity must be greater than zero.")


def build_book_record(book_id: int, name: str, quantity: int,
                    available_qty: int) -> str:
    """
    Build and return a book record.

    Args:
        book_id (int): Input book id.
        name (str): Input book name.
        quantity (int): Input book total quantity.
        available_qty (int): Input book available quantity.

    Returns:
        str: Build and return a book record.
    """
    return f"{book_id},{name},{quantity},{available_qty}\n"


def generate_next_book_id(books: list[str]) -> int:
    """
    Return a Auto generated next book Id.

    Args:
        books (list[str]]): Input list of book records.

    Returns:
        int: Auto generated book ID.
    """
    if not books:
        return 1
    return max(int(parse_book_record[0]) for book in books) + 1


def parse_book_record(book: str) -> list[str]:
    """Returned the book record"""
    return book.strip().split(",")


def add_book(books: list[str]) -> None:
    """Add a new book name into .txt File."""
    try:
        # Auto generated Book ID.
        book_id = generate_next_book_id(books=books)

        book_name = input("Enter a book name: ").strip()
        validate_unique_book_name(name=book_name, books=books)

        book_quantity = int(input("Enter a book quantity: "))
        validate_book_quantity(quantity=book_quantity)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        new_record = build_book_record(
            book_id=book_id,
            name=book_name,
            quantity=book_quantity,
            available_qty=book_quantity
        )
        books.append(new_record)
        save_books_data(books=books)
        print("Added a new book into .txt File.")
    finally:
        print("Operation completed.")


def view_books(books: list[str]) -> None:
    """
    Display list of books from .txt File.
    Args:
        books (list[str | int]): Input list of books.
    """
    if not books:
        print("Books not available in store.")
    else:
        print("List of Books:")
        print(" -" * 30)
        print(f" | {'ID':>5} | {'Name':<20} | {'Total Qty.':>5} |"
            f" {'Available Qty.':>5} | ")
        print(" -" * 30)
        for book in books:
            book_id, name, total, available = parse_book_record(book=book)
            print(f" | {book_id:>5} | {name:<20} | {total:>10} |"
                f" {available:>10} | ")
        print(" -" * 30)


def remove_book(books: list[str]) -> None:
    """Remove book from .txt File."""
    try:
        book_id = int(input("Enter a book ID: "))

    except ValueError:
        print("Invalid input. Please enter a valid book ID (int).")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for index, book in enumerate(books):
            if parse_book_record(book=book)[0] == str(book_id):
                books.pop(index)
                save_books_data(books=books)
                print("Successfully removed book.")
                break
        else:
            print("Book not available in store.")


def search_book(books: list[str]) -> None:
    """
    Search book record from .txt File.

    Args:
        books (list[str | int]): Input list of books.
    """
    try:
        book_id = int(input("Enter a book ID: "))
    except ValueError:
        print("Invalid input. Please enter a book ID (int).")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for book in books:
            record = parse_book_record(book=book)
            if record[0] == str(book_id):
                print("Book Details:")
                print(f"\tBook ID: {record[0]}\n"
                    f"\tName: {record[1]}\n"
                    f"\tStock Quantity: {record[2]}\n"
                    f"\tAvailable Quantity: {record[3]}")
                break
        else:
            print("Book not available in store.")


def issue_book(books: list[str]) -> None:
    """
    Issue (deduct qty.) book from .txt File.

    Args:
        books (list[str | int]): Input list of books.
    """
    try:
        book_id = int(input("Enter a book ID to issue: "))
    except ValueError:
        print("Invalid input. Please enter a valid input (int).")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        for index, book in enumerate(books):
            record = parse_book_record(book=book)
            if record[0] == str(book_id):
                available_qty = int(record[3])
                if available_qty == 0:
                    print("Book out of stock.")
                    return

                available_qty -= 1
                record = build_book_record(
                    book_id=record[0],
                    name=record[1],
                    quantity=record[2],
                    available_qty=available_qty
                )
                books[index] = record
                save_books_data(books=books)
                print("Book issued successfully.")
                break
        else:
            print("Book not available in store.")


def return_book(books: list[str]) -> None:
    """
    Return a book to store.

    Args:
        books (list[str | int]): Input list of books.
    """
    try:
        book_id = int(input("Enter a book ID to return book: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("Program interrupted.")
    else:
        for index, book in enumerate(books):
            exist_book_id, name, qty, available = parse_book_record(book=book)
            if exist_book_id == str(book_id):
                available_qty = int(available)
                if available_qty < int(qty):
                    available_qty += 1
                    return_book_record = build_book_record(
                        book_id=exist_book_id,
                        name=name,
                        quantity=qty,
                        available_qty=available_qty
                    )
                    books[index] = return_book_record
                    save_books_data(books=books)
                    print("Return book successfully.")
                else:
                    print("Book already returned.")
                break
        else:
            print("Book not available in store.")


def main() -> None:
    """Running Library Management System App."""

    # Create a .txt File if not exist.
    create_txt_file()
    # Fetch all books data
    books = load_books_data()

    while True:
        print("Library Management System Operations:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")
        try:
            # Accept input choice.
            choice = input("Enter your choice: ")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
        else:
            if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
                print("Invalid choice. Please select a valid option (1-7).")

            elif choice == "7":
                print("Exit from Operations.")
                break

            elif choice == "1":
                add_book(books=books)

            elif choice == "2":
                view_books(books=books)

            elif choice == "3":
                remove_book(books=books)
            elif choice == "4":
                search_book(books=books)

            elif choice == "5":
                issue_book(books=books)

            elif choice == "6":
                return_book(books=books)

            print("-" * 50)


if __name__ == "__main__":
    main()
