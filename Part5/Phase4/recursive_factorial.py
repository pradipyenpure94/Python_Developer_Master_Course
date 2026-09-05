"""Recursive factorial."""


def factorial(number: int) -> int:
    """
    Return the factorial number.

    Args:
        number (int): Input number.

    Returns:
        int: A factorial number.
    """
    if number == 0 or number == 1:
        return 1
    return number * factorial(number=number - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
        if number < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        result = factorial(number=number)
        print(f"The factorial of {number} is: {result}")
