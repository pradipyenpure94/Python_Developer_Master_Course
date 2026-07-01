"""Create a calculator using functions."""


def addition(num1: int, num2: int) -> int:
    """
    Return the addition of two input numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Addition of two input numbers.
    """
    return num1 + num2


def subtraction(num1: int, num2: int) -> int:
    """
    Return the subtraction of two input numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Subtraction of two input numbers.
    """
    return num1 - num2


def multiplication(num1: int, num2: int) -> int:
    """
    Return the multiplication of two input numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Multiplication of two input numbers.
    """
    return num1 * num2


def division(num1: int, num2: int) -> float:
    """
    Return the division of two input numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        float: Division of two input numbers.
    """
    return num1 / num2


OPERATIONS = {
    "1": ("Addition", addition),
    "2": ("Subtraction", subtraction),
    "3": ("Multiplication", multiplication),
    "4": ("Division", division),
}


def main() -> None:
    """Run the calculator application."""

    while True:
        print("Operations menu: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = input("Enter your choice (1-5): ")

            if choice not in {"1", "2", "3", "4", "5"}:
                print("Invalid choice. Please select a valid option (1-5):")
                continue

            elif choice == "5":
                print("Exit from operations.")
                break

            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))

            label, operation = OPERATIONS[choice]
            result = operation(first_number, second_number)

        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break
        except (ZeroDivisionError, ValueError) as error:
            print(f"Error: {error}")
        else:
            print(f"{label} result: {result:.2f}")
        finally:
            print("Operation completed.")

        print("-" * 30)


if __name__ == "__main__":
    main()
