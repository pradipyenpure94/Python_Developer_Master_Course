"""Find missing numbers."""

all_numbers = set(range(1, 11))
given_numbers = {1, 3, 5, 8}
missing_numbers = all_numbers - given_numbers
print(f"Missing numbers: {missing_numbers}")
