"""Lambda for even/ odd."""


def is_even_number(num: int) -> bool:
    """
    Check whether number is a even or odd.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is even, otherwise False.
    """
    is_even = lambda x: x % 2 == 0
    return is_even(num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_even_number(num=number):
            print(f"{number} is even number.")
        else:
            print(f"{number} is odd number.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
