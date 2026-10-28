"""Reverse an integer without converting it to a string."""

number = 12345
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Reversed number: {reversed_number}")
