"""Decimal to binary."""


def convert_decimal_to_binary(num: int) -> str:
    """
    Return the decimal to binary conversion.

    Args:
        num (int): Input decimal number.

    Returns:
        str: Binary number.
    """
    return bin(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = convert_decimal_to_binary(num=number)
        print(f"Decimal to Binary conversion: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
