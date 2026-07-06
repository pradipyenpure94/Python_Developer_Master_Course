"""Swap two numbers."""

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print("After swapping the numbers:")
    first_number, second_number = second_number, first_number
    print(f"First number: {first_number}")
    print(f"Second number: {second_number}")
finally:
    print("Operation completed.")
