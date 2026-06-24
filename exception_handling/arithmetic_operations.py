"""
1. Take two inputs from the user.
2. Performs +,/,*,-.
3. Handles ValueError and ZeroDivisionError.
4. Uses Else and finally.
"""


def addition(num1: float, num2: float) -> float:
    """
    Return the addition of two numbers.

    Args:
        num1 (float): First input number.
        num2 (float): Second input number.

    Returns:
        float: Addition of two numbers.
    """
    return num1 + num2


def subtraction(num1: float, num2: float) -> float:
    """
    Return the subtraction of two numbers.

    Args:
        num1 (float): First input number.
        num2 (float): Second input number.

    Returns:
        float: Subtraction of two numbers.
    """
    return num1 - num2


def multiplication(num1: float, num2: float) -> float:
    """
    Return the multiplication of two numbers.

    Args:
        num1 (float): First input number.
        num2 (float): Second input number.

    Returns:
        float: Multiplication of two numbers.
    """
    return num1 * num2


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


OPERATIONS = {
    "1": ("Addition", addition),
    "2": ("Subtraction", subtraction),
    "3": ("Multiplication", multiplication),
    "4": ("Division", division),
}


def main() -> None:
    """Menu driven calculator application."""

    while True:
        print("Arithmetic operations menu: ")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid choice. Please select valid operations (1-5).")
            continue

        if choice == "5":
            print("Exit from operations.")
            break

        try:
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            label, operation = OPERATIONS[choice]

            result = operation(num1=first_number, num2=second_number)

        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break
        else:
            print(f"{label} result: {result:.2f}")
        finally:
            print("Operation completed.")

        print("-" * 50)


if __name__ == "__main__":
    main()
