"""Perform all arithmetic operations on two numbers."""


try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print("Arithmetic Operations:")
    print("-" * 40)
    print(f"Addition        : {first_number + second_number}")
    print(f"Subtraction     : {first_number - second_number}")
    print(f"Multiplication  : {first_number * second_number}")
    print(f"Division        : {first_number / second_number:.2f}")
    print(f"Floor Division  : {first_number // second_number}")
    print(f"Modulus         : {first_number % second_number}")
    print(f"Exponentiation  : {first_number ** second_number}")
    print("-" * 40)

except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
