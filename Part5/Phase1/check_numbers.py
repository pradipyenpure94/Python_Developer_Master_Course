"""Check whether a number is positive, negative or zero."""


try:
    number = int(input("Enter the number: "))
    if number > 0:
        print("Number is positive.")
    elif number < 0:
        print("Number is negative.")
    else:
        print("Zero number.")

except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
