"""Reverse a number."""

try:
    number = int(input("Enter a number: "))
    sign = 1 if number > 0 else -1
    temp = abs(number)
    reversed_number = 0
    while temp > 0:
        reversed_number = reversed_number * 10 + temp % 10
        temp //= 10
    print(f"Reversed number: {reversed_number * sign}")
except ValueError:
    print("Invalid input! Please enter an integer.")
