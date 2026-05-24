"""Find common elements in two lists using set."""

prime_numbers = [2, 3, 5, 7]
odd_numbers = [1, 3, 5, 7]

odd_numbers_set = set(odd_numbers)
common_elements = [number for number in prime_numbers
                   if number in odd_numbers_set]
print(f"Common elements: {common_elements}")
