"""Binary to decimal."""


def convert_binary_to_decimal(num: str) -> int:
    """Return the binary to decimal number.

    Args:
        num (int): Input binary number.

    Returns:
        int: Decimal number.
    """
    if any(number not in {"0", "1"} for number in num):
        raise ValueError("Binary number must contain 0 or 1")

    total = 0
    for power, digit in enumerate(num):
        digit = int(digit)
        total += digit * (digit ** power)
    return total


if __name__ == "__main__":
    number = input("Enter binary number: ")
    result = convert_binary_to_decimal(num=number)
    print(f"Binary to Decimal conversion: {result}")
