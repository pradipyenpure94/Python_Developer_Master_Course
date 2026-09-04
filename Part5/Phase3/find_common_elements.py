"""Find common elements between two lists using set."""

prime_numbers = [2, 3, 5, 7, 11, 13]
even_numbers = [2, 4, 6, 8, 10]

common_elements = set(prime_numbers).intersection(set(even_numbers))
print(f"Common Elements: {common_elements}")
