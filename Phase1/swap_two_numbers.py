"""Swap two numbers."""

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    num1, num2 = num2, num1

    print("\nSwapped numbers:")
    print("First number: ", num1)
    print("Second number: ", num2)
except ValueError:
    print("Invalid input! Please enter an integer.")
