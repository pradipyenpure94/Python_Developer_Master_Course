"""Calculate factorial of a number (loop)."""


def calculate_factorial_number(num: int) -> int:
    """
    Return the factorial of the input number.

    Args:
        num (int): Input number.

    Returns:
        int: Factorial of the input number.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative number.")

    if num == 0:
        return 1

    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = calculate_factorial_number(num=number)
    except ValueError as error:
        print(f"{error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print(f"Factorial of {number} is: {result}")
    finally:
        print("Operation completed.")
