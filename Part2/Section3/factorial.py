"""Factorial using loop."""

MIN_NUMBER = 0
MAX_NUMBER = 100


def validate_number(number: int) -> None:
    """Raise ValueError if number is negative."""
    if number < MIN_NUMBER:
        raise ValueError(
            "Factorial is defined only "
            "for non-negative integers.")

    if number > MAX_NUMBER:
        raise ValueError(f"Number cannot exceed {MAX_NUMBER}")


def calculate_factorial(number: int) -> int:
    """Return a factorial number."""
    if number == 0 or number == 1:
        return 1
    fact = 1
    for multiplier in range(2, number + 1):
        fact *= multiplier
    return fact


def main() -> None:
    """Run the Main Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("Operation cancelled by the user.")
    else:
        result = calculate_factorial(number=number)
        print(f"Factorial of {number} is: {result}")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
