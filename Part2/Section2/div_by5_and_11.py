"""Divisibility by 5 and 11."""

FIRST_DIVISOR = 5
SECOND_DIVISOR = 11


def main() -> None:
    """Run Divisibility program."""
    try:
        number = int(input("Enter the number: "))
    except ValueError as error:
        print(f"Error: {error}")
    else:
        if number % FIRST_DIVISOR == 0 and number % SECOND_DIVISOR == 0:
            print(
                f"{number} is divisible by {FIRST_DIVISOR} and "
                f"{SECOND_DIVISOR}."
            )
        else:
            print(
                f"{number} is not divisible by {FIRST_DIVISOR} and "
                f"{SECOND_DIVISOR}."
            )
    finally:
        print("Operation finished.")


if __name__ == "__main__":
    main()
