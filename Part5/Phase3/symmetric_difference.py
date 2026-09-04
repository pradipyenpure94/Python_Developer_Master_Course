"""Find symmetric difference."""

prime_numbers = {2, 3, 5, 7, 11, 13}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

symmetric_difference = prime_numbers.symmetric_difference(odd_numbers)
print(f"Symmetric difference: {symmetric_difference}")
