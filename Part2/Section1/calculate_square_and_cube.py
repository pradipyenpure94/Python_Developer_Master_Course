"""Calculate square and cube."""

try:
    number = int(input("Enter the number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    square_number = number ** 2
    cube_number = number ** 3
    print(f"Input number: {number}")
    print(f"Square number: {square_number}")
    print(f"Cube number: {cube_number}")
finally:
    print("Operation completed.")
