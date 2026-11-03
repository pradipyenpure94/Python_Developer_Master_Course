"""Check whether a number lies within a given range."""

number = float(input("Enter the number: "))

# Check the number is found between the given range.
is_number = 0 <= number <= 10
print(f"Is number found: {is_number}")
