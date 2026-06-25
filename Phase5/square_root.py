"""
Square Root Calculator.
Raise an exception for negative numbers.
"""
from math import sqrt

try:
    number = int(input("Enter a number: "))
    if number < 0:
        raise ValueError("Please enter a non-negative number.")

    # To get square root of number.
    square_root = sqrt(number)

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print(f"Square root of {number} is: {square_root:.2f}")
finally:
    print("Operation completed.")
