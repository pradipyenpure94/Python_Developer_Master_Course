"""Lambda with conditional expression."""


def is_even_number(num: int) -> str:
    """Check whether number is a even or odd.
    Args:
        num (int): Input number.
    Returns:
        str: "Even" if number is even otherwise "Odd"
    """
    check_num = lambda x: "Even" if x % 2 == 0 else "Odd"
    return check_num(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = is_even_number(num=number)
        print(f"Is number: {result}")
    except ValueError:
        print("Invalid input! Please enter an integer.")
