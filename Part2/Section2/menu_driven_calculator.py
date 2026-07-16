"""Menu-driven calculator."""

VALID_CHOICES = {"1", "2", "3", "4", "5", "6", "7", "8"}


def validate_non_zero_divisor(number: float) -> None:
    """Raise ZeroDivisionError if the divisor is zero."""
    if number == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")


def main() -> None:
    """Run the Calculator application."""

    while True:
        print("Arithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Floor Division")
        print("6. Power")
        print("7. Modulus")
        print("8. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in VALID_CHOICES:
                print("Invalid choice. Please select a valid option.")
                continue

            if choice == "8":
                print("Exit from operations.")
                break

            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))

            if choice in {"4", "5", "7"}:
                validate_non_zero_divisor(number=second_number)

            if choice == "1":
                print(f"Addition: {first_number + second_number}")
            elif choice == "2":
                print(f"Subtraction: {first_number - second_number}")
            elif choice == "3":
                print(f"Multiplication: {first_number * second_number}")
            elif choice == "4":
                print(f"Division: {(first_number / second_number):.2f}")
            elif choice == "5":
                print(f"Floor Division: {first_number // second_number}")
            elif choice == "6":
                print(f"Exponent Power: {first_number ** second_number}")
            elif choice == "7":
                print(f"Modulus: {first_number % second_number}")

        except ZeroDivisionError as error:
            print(f"Error: {error}")
        except ValueError as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break
        finally:
            print("Operation finished.")

        print("-" * 50)


if __name__ == "__main__":
    main()
