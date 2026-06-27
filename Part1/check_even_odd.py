"""Check whether a number is even or odd."""


def is_even_number(num: int) -> bool:
    """
    Check whether the given number is even.

    Args:
        num (int): Input number.

    Returns:
        bool: True if the number is even, otherwise False.
    """
    if num % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        if is_even_number(num=number):
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")
    finally:
        print("Operation completed.")
