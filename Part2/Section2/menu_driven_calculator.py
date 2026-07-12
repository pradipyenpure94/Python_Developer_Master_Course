"""Menu-driven calculator."""


def main() -> None:
    """Run the Calculator application."""
    while True:
        print("Arithmetic Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice not in {"1", "2", "3", "4", "5", "6", "7"}:
            print("Invalid choice. Please select a valid option.")
        elif choice == "7":
            print("Exit from operations.")
            break
        elif choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass


if __name__ == "__main__":
    main()
