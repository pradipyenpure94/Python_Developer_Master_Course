"""Check prime number."""


def is_prime_number(num: int) -> bool:
    """
    Check whether number is prime or not.

    Args:
        num (int): Input number.

    Returns:
        bool: True if number is prime Otherwise False.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if is_prime_number(num=number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
