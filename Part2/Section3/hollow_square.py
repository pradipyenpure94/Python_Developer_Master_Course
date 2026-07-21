"""Hollow Square."""

from print_star_patterns import validate_number


def print_hollow_square(rows: int) -> None:
    """Print Hollow Square pattern."""
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("* " * rows)
        else:
            print("* " + "  " * (rows - 2) + "*")


def main() -> None:
    """Print Run the Program."""
    try:
        rows = int(input("Enter the number of rows: "))
        validate_number(number=rows)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print_hollow_square(rows=rows)
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
