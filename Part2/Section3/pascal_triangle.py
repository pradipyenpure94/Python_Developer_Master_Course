"""Pascal Triangle."""

from math import comb
from print_star_patterns import validate_number


def print_pascal_triangle(rows: int) -> None:
    """Print Pascal's triangle pattern"""
    for i in range(rows):
        print(" " * (rows - i), end="")
        for j in range(i + 1):
            print(comb(i, j), end=" ")
        print()


def main() -> None:
    """Run the main Program."""
    try:
        rows = int(input("Enter the number of rows: "))
        validate_number(number=rows)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print_pascal_triangle(rows=rows)
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
