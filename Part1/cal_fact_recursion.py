"""Calculate factorial using recursion."""


def calculate_factorial(num: int) -> int:
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

    return num * calculate_factorial(num=num - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = calculate_factorial(num=number)
    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    else:
        print(f"Factorial of {number} is: {result}")
    finally:
        print("Operation completed.")
