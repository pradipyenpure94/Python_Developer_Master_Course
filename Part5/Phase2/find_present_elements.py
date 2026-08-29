"""Find elements present in the first list."""

prime_numbers = [2, 3, 5, 7, 11, 13]
odd_numbers = [1, 3, 5, 7, 9]
result = []

for number in prime_numbers:
    if number not in odd_numbers:
        result.append(number)

print(f"Result: {result}")
