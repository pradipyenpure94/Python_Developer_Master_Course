"""Function to check prime."""


def is_prime(number: int) -> bool:
    """
    Check whether a number is prime.

    Args:
        number (int): Input number.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")
    else:
        if is_prime(number=number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
