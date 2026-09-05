"""Create a calculator using functions."""


def addition(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


def subtraction(first_number: int, second_number: int) -> int:
    """Return the subtraction of two numbers."""
    return first_number - second_number


def multiplication(first_number: int, second_number: int) -> int:
    """Return the multiplication of two numbers."""
    return first_number * second_number


def division(first_number: int, second_number: int) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


def main() -> None:
    """Run the main program."""

    while True:
        print("Arithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice not in {"1", "2", "3", "4", "5"}:
                print("Invalid choice. Please select valid options (1-5).")
                continue

            if choice == "5":
                print("Exit from operations.")
                break

            first_number = int(input("Enter the first number: "))
            second_number = int(input("Enter the second number: "))

            if choice == "1":
                result = addition(
                    first_number=first_number,
                    second_number=second_number
                )
                print(f"Addition: {result}")
            elif choice == "2":
                result = subtraction(
                    first_number=first_number,
                    second_number=second_number
                )
                print(f"Subtraction: {result}")
            elif choice == "3":
                result = multiplication(
                    first_number=first_number,
                    second_number=second_number
                )
                print(f"Multiplication: {result}")
            elif choice == "4":
                try:
                    result = division(
                        first_number=first_number,
                        second_number=second_number
                    )
                except ZeroDivisionError as error:
                    print(f"Error: {error}")
                else:
                    print(f"Division: {result}")
        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
