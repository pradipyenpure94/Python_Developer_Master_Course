"""Find common elements in two lists using set."""

prime_numbers = [2, 3, 5, 7]
odd_numbers = [1, 3, 5, 7]

common_elements = []
odd_numbers_set = set(odd_numbers)
index = 0

while index < len(prime_numbers):
    number = prime_numbers[index]
    if number in odd_numbers_set:
        common_elements.append(number)
    index += 1

print(f"Common elements: {common_elements}")
