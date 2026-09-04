"""Create a function add two numbers."""


def add_two_numbers(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


def main() -> None:
    """Run the main program."""
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = add_two_numbers(
            first_number=first_number,
            second_number=second_number
        )
        print(f"Addition: {result}")


if __name__ == "__main__":
    main()
