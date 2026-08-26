"""Find the largest of three numbers."""


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
else:
    if first_number >= second_number and first_number >= third_number:
        print(f"{first_number} is the largest number.")
    elif second_number >= first_number and second_number >= third_number:
        print(f"{second_number} is the largest number.")
    else:
        print(f"{third_number} is the largest number.")
