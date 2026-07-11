"""Find maximum using nested if."""


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
else:
    max_number = None
    if first_number >= second_number:
        if first_number >= third_number:
            max_number = first_number
        else:
            max_number = third_number
    else:
        if second_number >= third_number:
            max_number = second_number
        else:
            max_number = third_number
    print(f"Maximum number: {max_number}")
finally:
    print("Operation completed.")
