"""Find difference between two sets."""

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19}
odd_numbers = {1, 3, 5, 7, 9, 11, 13}

prime_numbers_list = list(prime_numbers)
index = 0
difference = set()

while index < len(prime_numbers_list):
    number = prime_numbers_list[index]
    if number not in odd_numbers:
        difference.add(number)
    index += 1

print(f"Difference: {difference}")
