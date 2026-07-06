"""Find smallest of three numbers."""

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    if first_number <= second_number and first_number <= third_number:
        print(f"Smallest number: {first_number}")
    elif second_number <= third_number and second_number <= first_number:
        print(f"Smallest number: {second_number}")
    else:
        print(f"Smallest number: {third_number}")
finally:
    print("Operation completed.")
