"""Find difference between two sets."""

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

difference = set()

for number in prime_numbers:
    if number not in odd_numbers:
        difference.add(number)

print(f"Difference: {difference}")
