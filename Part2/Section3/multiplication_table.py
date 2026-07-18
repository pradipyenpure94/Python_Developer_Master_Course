"""Multiplication table."""

TABLE_START = 1
TABLE_LIMIT = 10


def print_multiplication_table(number: int) -> None:
    """Print the multiplication table."""
    for multiplier in range(TABLE_START, TABLE_LIMIT + 1):
        print(f"{number:>5} {'x':>3} {multiplier:>5} = {number * multiplier}")


def main() -> None:
    """Run the main Program."""
    try:
        number = int(input("Enter the number: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print_multiplication_table(number=number)
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
