"""Import and reuse custom functions."""

import calculator


def main() -> None:
    """Run the main program."""
    print(f"Addition       : {calculator.add(
        first_number=10,
        second_number=2.5
    ):.2f}")
    print(f"Subtraction    : {calculator.sub(
        first_number=10,
        second_number=8.5
    ):.2f}")
    print(f"Multiplication : {calculator.mul(
        first_number=10.5,
        second_number=2
    ):.2f}")

    try:
        result = calculator.div(first_number=10.8, second_number=2.4)
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    else:
        print(f"Division       : {result:.2f}")


if __name__ == "__main__":
    main()
