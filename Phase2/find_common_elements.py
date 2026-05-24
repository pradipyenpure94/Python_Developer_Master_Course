"""Find common elements in two lists using set."""

prime_numbers = [2, 3, 5, 7]
odd_numbers = [1, 3, 5, 7]

common_elements = list(set(prime_numbers).intersection(set(odd_numbers)))
print(f"Common elements: {common_elements}")
