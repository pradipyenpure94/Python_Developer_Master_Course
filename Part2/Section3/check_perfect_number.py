"""Perfect number."""


from math import isqrt

# As per the business requirements, Defined the limits.
MIN_NUMBER = 1
MAX_NUMBER = 999999


def validate_number(number: int) -> None:
    """
    Validate the number.

    Args:
        number (int): Input number.

    Raises:
        ValueError: If the number is outside range, it is not allowed.
    """
    if not MIN_NUMBER <= number <= MAX_NUMBER:
        raise ValueError(
            "The number must be between "
            f"{MIN_NUMBER} and {MAX_NUMBER}.")


def is_perfect_number(number: int) -> bool:
    """
    Check whether the number is a perfect number.

    Args:
        number (int): Input number.

    Returns:
        bool: True, if the number is a perfect number; otherwise, False.
    """
    if number == MIN_NUMBER:
        return False

    divisor_sum = 1

    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            divisor_sum += divisor

            paired_divisor = number // divisor

            if paired_divisor != divisor:
                divisor_sum += paired_divisor

    return number == divisor_sum


def main() -> None:
    """Run the Program."""
    try:
        number = int(input("Enter the number: "))
        validate_number(number=number)

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_perfect_number(number=number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
