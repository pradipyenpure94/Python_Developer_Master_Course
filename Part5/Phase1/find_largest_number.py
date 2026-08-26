"""Find the largest of two numbers."""


try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if first_number > second_number:
        print(f"{first_number} is the largest number.")
    elif second_number > first_number:
        print(f"{second_number} is the largest number.")
    else:
        print("Both are equal numbers.")
