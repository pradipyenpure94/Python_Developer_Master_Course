"""Recursive binary conversion."""


def decimal_to_binary_conversion(num: int) -> str:
    """
    Return the binary representation of a decimal number.

    Args:
        num (int): Input number.

    Returns:
        str: Binary representation of the input number.
    """
    if num < 0:
        return "-" + decimal_to_binary_conversion(abs(num))
    if num <= 1:
        return str(num)
    return decimal_to_binary_conversion(num // 2) + str(num % 2)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = decimal_to_binary_conversion(num=number)
        print(f"Decimal to binary conversion: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
