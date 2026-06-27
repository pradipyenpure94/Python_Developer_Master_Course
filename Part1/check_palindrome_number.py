"""Check whether a number is palindrome."""

from reverse_an_int import reverse_number


def is_palindrome_number(num: int) -> bool:
    """
    Check whether a number is a palindrome.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is a palindrome, otherwise False.
    """
    if num < 0:
        return False
    return num == reverse_number(num=num)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if is_palindrome_number(num=number):
            print(f"{number} is a palindrome.")
        else:
            print(f"{number} is not a palindrome.")
    finally:
        print("Operation completed.")
