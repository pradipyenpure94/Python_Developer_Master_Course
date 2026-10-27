"""Take two numbers as input and perform all arithmetic operations."""


try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print(f"Addition: {first_number + second_number}")
    print(f"Subtraction: {first_number - second_number}")
    print(f"Multiplication: {first_number * second_number}")
    print(f"Division: {first_number / second_number:.2f}")
    print(f"Floor Division: {first_number // second_number}")
    print(f"Modulus: {first_number % second_number}")
    print(f"Exponent: {first_number ** second_number}")

except (ZeroDivisionError, ValueError) as error:
    print(f"Error: {error}")
