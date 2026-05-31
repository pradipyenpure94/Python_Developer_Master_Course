"""Product of digits."""


def product_of_digits(num: int) -> int:
    """
    Return the product of digits in number.

    Args:
        num (int): Input number.

    Returns:
        int: Product of digits in number.
    """
    temp = abs(num)
    if temp == 0:
        return 0

    total = 1

    while temp > 0:
        digit = temp % 10
        total *= digit
        temp //= 10
    return total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = product_of_digits(num=number)
        print(f"Product of digits: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
