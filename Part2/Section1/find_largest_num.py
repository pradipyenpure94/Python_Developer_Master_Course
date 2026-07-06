"""Find largest of three numbers."""

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    if first_number >= second_number and first_number >= third_number:
        print(f"Largest number: {first_number}")
    elif second_number >= third_number and second_number >= first_number:
        print(f"Largest number: {second_number}")
    else:
        print(f"Largest number: {third_number}")
finally:
    print("Operation completed.")
