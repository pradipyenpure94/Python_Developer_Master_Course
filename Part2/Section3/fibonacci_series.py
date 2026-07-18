"""Fibonacci series."""

# As per the business requirement, defined terms.
MIN_TERM = 1
MAX_TERM = 100
FIRST_TERM = 0
SECOND_TERM = 1


def validate_number(number: int) -> None:
    """Validate the number."""
    if not MIN_TERM <= number <= MAX_TERM:
        raise ValueError(
            "The input number should be between "
            f"{MIN_TERM} and {MAX_TERM}."
        )


def generate_fibonacci_series(number: int) -> str:
    """Return the fibonacci series as a comma-separated string."""

    first_number = FIRST_TERM
    second_number = SECOND_TERM
    series = []

    for _ in range(number):
        series.append(first_number)
        first_number, second_number = second_number, \
            first_number + second_number

    return ",".join(str(item) for item in series)


def main() -> None:
    """Run the Main Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = generate_fibonacci_series(number=number)
        print(f"Fibonacci Numbers: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
