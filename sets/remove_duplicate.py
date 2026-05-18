"""Remove duplicates from list."""

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(f"Unique numbers: {unique_numbers}")
