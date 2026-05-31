"""Count digits in number."""


def count_digits_in_number(num: int) -> int:
    """
    Return the count of digits in number.

    Args:
        num (int): Input number.

    Returns:
        int: Count of digits in number.
    """
    temp = abs(num)
    count = 0
    if temp == 0:
        count += 1

    while temp > 0:
        count += 1
        temp //= 10
    return count


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = count_digits_in_number(number)
        print(f"Count digits: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
