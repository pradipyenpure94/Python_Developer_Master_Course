"""check whether a number is positive, negative or zero."""

try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("The number is negative.")
    elif number > 0:
        print("The number is positive.")
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input! Please enter an integer.")
