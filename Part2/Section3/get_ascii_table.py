"""Print ASCII Table."""


START_ASCII = 0
END_ASCII = 127


def validate_ascii_number(number: int) -> None:
    """
    Validate the ASCII number.

    Args:
        number (int): Input ASCII number.

    Raises:
        ValueError: The ASCII number range is outside. It is not allowed.
    """
    if not START_ASCII <= number <= END_ASCII:
        raise ValueError(
            "The ASCII number must be between "
            f"{START_ASCII} and {END_ASCII}."
        )


def validate_ascii_range(
    start_ascii_number: int,
    end_ascii_number: int
) -> None:
    """Validate the ASCII input range."""
    if not start_ascii_number <= end_ascii_number:
        raise ValueError(
            "The START ASCII number must be less than "
            "or equal to the END ASCII number."
        )


def print_ascii_table(start_ascii_number: int, end_ascii_number: int) -> None:
    """Print the ASCII table from the given two input numbers."""
    print("-" * 20)
    print(f"{'ASCII':>5}   {'CHARACTER':<5}")
    print("-" * 20)
    for number in range(start_ascii_number, end_ascii_number + 1):
        print(f"{number:>5}   {chr(number):<5}")
    print("-" * 20)


def main() -> None:
    """Run the Main Program."""
    try:
        start_ascii_number = int(input("Enter the START ASCII number: "))
        validate_ascii_number(number=start_ascii_number)
        end_ascii_number = int(input("Enter the END ASCII number:"))
        validate_ascii_number(number=end_ascii_number)
        validate_ascii_range(
            start_ascii_number=start_ascii_number,
            end_ascii_number=end_ascii_number
        )

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\n Operation cancelled by the user.")
    else:
        print_ascii_table(
            start_ascii_number=start_ascii_number,
            end_ascii_number=end_ascii_number
        )
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
