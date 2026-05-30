"""Calculate factorial using function."""


def calculate_factorial_number(num: int) -> int:
    """
    Return the factorial number of input numbers.

    Args:
        num (int): Input number.

    Returns:
        int: Factorial number.
    """
    if num < 0:
        raise ValueError("Factorial number is not defined for negative number.")
    if num == 0:
        return 1
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = calculate_factorial_number(num=number)
        print(f"Factorial number: {result}")
    except ValueError as error:
        print(f"Error: {error}")
