"""Check whether a number is even or odd."""


def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == "__main__":
    try:
        number = int(input("Enter the number: "))
    except ValueError as error:
        print(f"Error: {error}")
    else:
        if is_even(number=number):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
