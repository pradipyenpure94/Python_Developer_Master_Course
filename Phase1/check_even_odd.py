"""Check whether a number is even or odd."""

try:
    number = int(input("Enter a number: "))
    result = "even" if number % 2 == 0 else "odd"
    print(f"The number is {result}.")
except ValueError:
    print("Invalid input! Please enter an integer.")
