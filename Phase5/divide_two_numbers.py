"""
Divide two numbers.
Handle ZeroDivisionError.
"""


def division(num1: float, num2: float) -> float:
    """
    Return the division of two numbers.

    Args:
        num1 (float): First input number.
        num2 (float): Second input number.

    Returns:
        float: Division of two numbers.
    """
    return num1 / num2


if __name__ == "__main__":
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        result = division(num1=first_number, num2=second_number)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except KeyboardInterrupt:
        print("\nProgram Interrupted.")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation completed.")
