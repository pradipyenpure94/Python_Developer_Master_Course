"""Find the common elements in two list."""

prime_numbers = [2, 3, 5, 7, 11, 13]
odd_numbers = [1, 3, 5, 7, 9, 11, 13]
common_numbers = list(filter(lambda x: x in odd_numbers, prime_numbers))
print(f"Common elements: {common_numbers}")
