"""Calculating the sum of natural numbers."""

try:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Negative number is not defined for calculating sum of natural numbers.")
    else:
        total = 0
        i = 1
        while i <= n:
            total += i
            i += 1
        print(f"The sum of natural numbers from 1 to {n} is {total}")
except ValueError:
    print("Invalid input! Please enter an integer.")
