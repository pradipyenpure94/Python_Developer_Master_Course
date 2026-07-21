"""Number Pyramid."""

from print_star_patterns import validate_number


def print_number_pyramid(rows: int) -> None:
    """Print the Number Pyramid pattern."""
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()


def main() -> None:
    """Run the Main Program."""
    try:
        rows = int(input("Enter the number of rows: "))
        validate_number(number=rows)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print_number_pyramid(rows=rows)
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
