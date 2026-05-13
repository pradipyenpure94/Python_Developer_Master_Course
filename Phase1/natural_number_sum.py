"""Sum of natural numbers."""

try:
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Negative number is not defined for calculating sum of natural numbers.")
    else:
        total = 0
        for number in range(1, n + 1):
            total += number
        print(f"The sum of natural numbers from 1 to {n} is {total}")
except ValueError:
    print("Invalid input! Please enter an integer.")
