"""Find greatest among N numbers."""

try:
    no_of_inputs = int(input("How many numbers do you want to enter? "))

    # Validate no.of inputs
    if no_of_inputs <= 0:
        raise ValueError("Number of inputs must be greater than zero.")

    # Store user input numbers.
    input_numbers = []

    for i in range(1, no_of_inputs + 1):
        number = float(input(f"Enter the number {i}: "))
        input_numbers.append(number)


except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    print("-" * 20)
    # Find the max. number.
    max_number = max(input_numbers)
    print(f"Maximum number: {max_number}")
finally:
    print("Operation completed.")
