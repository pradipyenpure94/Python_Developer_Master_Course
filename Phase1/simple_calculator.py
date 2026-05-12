"""Simple calculator."""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"\nAddition: {num1 + num2}")
    print(f"Subtraction: {num1 - num2}")
    print(f"Multiplication: {num1 * num2}")
    print(f"Division: {num1 / num2:.2f}")

except (ValueError, ZeroDivisionError) as error:
    print(f"Error: {error}")
