"""Find intersection of two sets."""

prime_numbers = {2, 3, 5, 7, 11, 13}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

common_numbers = set()

for number in odd_numbers:
    if number in prime_numbers:
        common_numbers.add(number)

print(f"Common numbers: {common_numbers}")
