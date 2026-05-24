"""Find intersection of two sets."""

prime_numbers = {2, 3, 5, 7, 11, 13}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

common_numbers = prime_numbers & odd_numbers
print(f"Common numbers: {common_numbers}")
