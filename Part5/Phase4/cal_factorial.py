"""Function to calculate factorial."""

MAX_NUMBER = 100


def calculate_factorial(number: int) -> int:
    """
    Return the factorial of a number.

    Args:
        number (int): Input number.

    Returns:
        int: A factorial number.

    Raises:
        ValueError: If number less than zero
        and factorial number limit exceeded.
    """
    if number < 0:
        raise ValueError(
            "Factorial number is not defined for negative number."
        )
    if number > MAX_NUMBER:
        raise ValueError(
            "The Factorial of number is limit exceed "
            f"(Max Limit: {MAX_NUMBER}).")

    if number == 0 or number == 1:
        return 1

    fact = 1

    for i in range(1, number + 1):
        fact *= i

    return fact


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
        result = calculate_factorial(number=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        print(f"Factorial of {number} is: {result}")
