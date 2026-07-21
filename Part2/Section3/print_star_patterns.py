"""Print Patterns (star)."""

MIN_ROWS = 5
MAX_ROWS = 15

VALID_CHOICES = {"1", "2", "3", "4", "5", "6"}


def validate_number(number: int) -> None:
    """Validate the input number."""
    if not MIN_ROWS <= number <= MAX_ROWS:
        raise ValueError(
            "The number must be between "
            f"{MIN_ROWS} and {MAX_ROWS}."
        )


def half_pyramid_star(rows: int) -> None:
    """Print the Half Pyramid (star)"""
    for i in range(rows):
        for _ in range(i + 1):
            print("*", end=" ")
        print()


def inverted_half_pyramid_star(rows: int) -> None:
    """Print Inverted Half Pyramid star pattern."""
    for i in range(rows, 0, -1):
        for _ in range(i):
            print("*", end=" ")
        print()


def right_aligned_pyramid(rows: int) -> None:
    """Print a right-aligned half pyramid star pattern."""
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
    print()


def full_pyramid(rows: int) -> None:
    """Print full pyramid star pattern."""
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))


def print_diamond(rows: int) -> None:
    """Print diamond pattern."""
    # Print upper triangle
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * (2 * i - 1))
    # Print bottom triangle
    for j in range(rows - 1, 0, -1):
        print(" " * (rows - j), end="")
        print("*" * (2 * j - 1))


def main() -> None:
    """Run the Main Program."""

    while True:
        print("1. Half Pyramid")
        print("2. Inverted Half Pyramid")
        print("3. Right Aligned Pyramid")
        print("4. Full Pyramid")
        print("5. Diamond")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in VALID_CHOICES:
                print("Invalid choice. Please enter a valid choice (1-6).")
                continue

            elif choice == "6":
                print("Exit from operations.")
                break

            no_of_rows = int(input("Enter the number of rows: "))
            validate_number(number=no_of_rows)

            if choice == "1":
                half_pyramid_star(rows=no_of_rows)

            elif choice == "2":
                inverted_half_pyramid_star(rows=no_of_rows)

            elif choice == "3":
                right_aligned_pyramid(rows=no_of_rows)

            elif choice == "4":
                full_pyramid(rows=no_of_rows)

            elif choice == "5":
                print_diamond(rows=no_of_rows)

        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
