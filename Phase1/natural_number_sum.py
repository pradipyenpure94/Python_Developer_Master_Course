"""Calculate the sum of natural numbers."""

try:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer greater than zero.")
    else:
        total = n * (n + 1) // 2
        print(f"The sum of natural numbers from 1 to {n} is {total}.")
except ValueError:
    print("Invalid input! Please enter an integer.")
