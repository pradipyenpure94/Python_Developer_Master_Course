"""Handle multiple exceptions."""


def division(first_number: int, second_number: int) -> float:
    """Return the division of two numbers."""
    return first_number / second_number


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = division(first_number=first_number, second_number=second_number)
except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")
else:
    print(f"Division: {result}")
finally:
    print("Attempt division operations.")
