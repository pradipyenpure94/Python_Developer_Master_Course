"""Calculator Main Program."""

from calculator import addition, multiplication, division


def main() -> None:
    """Run the main program."""
    print(f"Addition       : {addition(10, 20.5, 20.9, 30)}")
    print(f"Multiplication : {multiplication(10, 5, 2.5)}")

    try:
        print(f"Division       : {division(first_number=10, second_number=3):.2f}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
