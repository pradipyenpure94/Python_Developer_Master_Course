"""Check positive, negative or zero."""

try:
    number = int(input("Enter the number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
except KeyboardInterrupt:
    print("\nProgram interrupted.")
else:
    if number > 0:
        print(f"{number} is a positive number.")
    elif number < 0:
        print(f"{number} is a negative number.")
    else:
        print("The number is zero.")
finally:
    print("Operation completed.")
