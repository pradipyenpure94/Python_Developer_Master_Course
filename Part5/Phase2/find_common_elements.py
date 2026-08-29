"""Find common elements between two lists."""

prime_numbers = [1, 2, 3, 5, 7, 11, 13]
even_numbers = [2, 4, 6, 8, 10]
common_elements = []

for number in even_numbers:
    if number in prime_numbers:
        common_elements.append(number)

print(f"Common elements: {common_elements}")
