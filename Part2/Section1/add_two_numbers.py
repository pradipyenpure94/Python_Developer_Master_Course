"""Add two numbers."""

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    # Addition of two numbers.
    result = first_number + second_number
    print(f"Addition: {result}")
finally:
    print("Operation completed.")
