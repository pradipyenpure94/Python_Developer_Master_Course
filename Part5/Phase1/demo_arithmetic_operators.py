"""Demonstrate the arithmetic operators."""

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print(f"Addition          : {first_number + second_number}")
    print(f"Subtraction       : {first_number - second_number}")
    print(f"Multiplication    : {first_number * second_number}")
    print(f"Division          : {first_number / second_number:.2f}")
    print(f"Floor Division    : {first_number // second_number}")
    print(f"Exponentiation     : {first_number ** second_number}")

except (ZeroDivisionError, ValueError) as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
