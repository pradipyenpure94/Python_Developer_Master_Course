"""Build a robust calculator with exception handling."""


def addition(first_number: int, second_number: int) -> int:
    """Return the addition of two numbers."""
    return first_number + second_number


def division(first_number: int, second_number: int) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


def main() -> None:
    """Run the main program."""
    while True:
        print("1. Addition")
        print("2. Division")
        print("3. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice not in {"1", "2", "3"}:
                print("Please select a valid option (1-3).")
                continue

            if choice == "3":
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

            if choice == "2":
                result = division(
                    first_number=first_number,
                    second_number=second_number
                )
                print(f"Division: {result}")
        except (ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by the user.")
            break


if __name__ == "__main__":
    main()
