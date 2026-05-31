"""Find smallest digit."""


def find_smallest_digit(num: int) -> int:
    """Return the smallest digit from number.

    Args:
        num (int): Input number.

    Returns:
        int: Smallest digit.
    """
    temp = abs(num)

    if temp == 0:
        return 0

    smallest_digit = 9

    while temp > 0:
        digit = temp % 10
        if digit < smallest_digit:
            smallest_digit = digit
        temp //= 10
    return smallest_digit


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = find_smallest_digit(num=number)
        print(f"Smallest digit: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
