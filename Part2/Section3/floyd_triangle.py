"""Floyd Triangle."""

from print_star_patterns import validate_number


def print_floyd_pattern(rows: int) -> None:
    """Print Floyd Triangle pattern."""
    current_number = 1
    for i in range(1, rows + 1):
        for _ in range(1, i + 1):
            print(current_number, end=" ")
            current_number += 1
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
        print_floyd_pattern(rows=rows)
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
