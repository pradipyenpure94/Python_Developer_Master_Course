"""Check even or odd."""


def is_even_number(number: int) -> bool:
    """Check whether a number is even or odd.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is even, otherwise False.
    """
    return number % 2 == 0


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_even_number(number=num):
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    except ValueError:
        print("Invalid input! Please enter a valid input.")
