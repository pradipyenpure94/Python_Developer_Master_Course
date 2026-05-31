"""Check whether number is a perfect number or not."""


def is_perfect_number(num: int) -> bool:
    """
    Check whether number is a perfect number or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if number is a perfect number otherwise False.
    """
    if num <= 0:
        raise ValueError("Number must be greater than zero.")

    total = 0
    i = 1

    while i < num:
        if num % i == 0:
            total += i
        i += 1
    return num == total


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_perfect_number(num=number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    except ValueError as error:
        print(f"Error: {error}")
