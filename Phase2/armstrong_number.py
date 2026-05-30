"""Check armstrong number."""


def digit_count(num: int) -> int:
    """
    Return the digit count.

    Args:
        num (int): Input number.

    Returns:
        int: Digit count.
    """
    temp = num
    count = 0
    if temp == 0:
        count = 1
    while temp > 0:
        count += 1
        temp //= 10
    return count


def is_armstrong_number(num: int) -> bool:
    """
    Check whether number is armstrong number.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is an armstrong, otherwise False.
    """
    if num < 0:
        raise ValueError("Number is not defined for negative number.")
    num_digit_count = digit_count(num)
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digit_count
        temp //= 10
    return total == num


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_armstrong_number(num=number):
            print(f"{number} is an armstrong number.")
        else:
            print(f"{number} is not an armstrong number.")
    except ValueError as error:
        print(f"Error: {error}")
