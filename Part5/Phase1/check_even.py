"""Check whether a number is even or odd."""


try:
    number = int(input("Enter the number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
except ValueError as error:
    print(f"Error: {error}")
except KeyboardInterrupt:
    print("\nOperation cancelled by the user.")
