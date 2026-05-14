"""Check whether a number is a strong number."""


def factorial(num: int) -> int:
    """Calculate the factorial of number.
    Args:
        num (int): input number
    Returns:
        int: factorial number
    """
    if num == 0:
        return 1

    fact = 1

    for i in range(1, num + 1):
        fact *= i
    return fact


try:
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        temp = number
        total = 0

        while temp > 0:
            digit = temp % 10
            total += factorial(digit)
            temp //= 10

        if number == total:
            print(f"{number} is a strong number.")
        else:
            print(f"{number} is not a strong number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
