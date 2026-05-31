"""Find largest digit."""


def find_largest_digit(num: int) -> int:
    """Return the largest digit from number.

    Args:
        num (int): Input number.

    Returns:
        int: Largest digit from number.
    """
    temp = abs(num)
    largest_digit = 0

    while temp > 0:
        digit = temp % 10
        if digit > largest_digit:
            largest_digit = digit
        temp //= 10
    return largest_digit


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = find_largest_digit(num=number)
        print(f"Largest digit: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
