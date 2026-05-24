"""Find intersection of two sets."""

prime_numbers = {2, 3, 5, 7, 11, 13}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

common_numbers = set()
index = 0
prime_list_numbers = list(prime_numbers)

while index < len(prime_numbers):
    number = prime_list_numbers[index]
    if number in odd_numbers:
        common_numbers.add(number)
    index += 1

print(f"Common numbers: {common_numbers}")
