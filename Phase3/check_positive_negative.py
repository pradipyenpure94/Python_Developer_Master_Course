"""Check positive or negative."""


def check_number(num: int) -> str:
    """Check whether number is positive, negative or zero.

    Args:
        num (int): Input number.

    Returns:
        str: Message indicating whether the number is positive, negative or
        zero.
    """
    if num < 0:
        return f"{num} is a negative number."
    elif num > 0:
        return f"{num} is a positive number."
    else:
        return f"{num} is zero."


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        print(check_number(num=number))
    except ValueError:
        print("Invalid input! Please enter a valid input.")
