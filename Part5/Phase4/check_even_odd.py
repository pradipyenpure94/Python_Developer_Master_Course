"""Function to check even/odd."""


def is_even(number: int) -> bool:
    """
    Check whether a number is an even.

    Args:
        number (int): Input number.

    Returns:
        bool: True, if the number is an even, otherwise False.
    """
    return number % 2 == 0


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_even(number=number):
            print(f"{number} is an even number.")
        else:
            print(f"{number} is a odd number.")
