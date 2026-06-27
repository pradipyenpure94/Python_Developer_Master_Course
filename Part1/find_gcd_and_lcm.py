"""Find GCD and LCM of two numbers."""

from math import gcd, lcm


def find_gcd(num1: int, num2: int) -> int:
    """
    Return the GCD of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Greatest common divisor of input two numbers.
    """
    # Uses the Euclidean algoritham to find GCD.
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def find_lcm(num1: int, num2: int) -> int:
    """
    Return the LCM of two numbers.

    Args:
        num1 (int): First input number.
        num2 (int): Second input number.

    Returns:
        int: Least common multiple of two input numbers.
    """
    # Avoids division by zero, if both inputs are zero.
    if num1 == 0 or num2 == 0:
        return 0
    # LCM formulae: (a * b) / GCD(a , b)
    return (num1 * num2) / find_gcd(num1=num1, num2=num2)


def main() -> None:
    """Main Program."""

    while True:
        print("1. GCD")
        print("2. LCM")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "3":
                print("Exit.")
                break

            elif choice not in {"1", "2", "3"}:
                print("Invalid choice. Please select a valid choice (1-3)")
                continue

            first_number = int(input("Enter first number: "))
            second_number = int(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please enter an integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
        else:
            if choice == "1":
                result = find_gcd(num1=first_number, num2=second_number)
                print(f"GCD: {result}")

            elif choice == "2":
                result = find_lcm(num1=first_number, num2=second_number)
                print(f"LCM: {result}")
        finally:
            print("Operation completed.")
            print("-" * 30)


if __name__ == "__main__":
    main()
