"""Remove duplicate values while preserving their original order."""

numbers = [1, 0, 1, 0, 1, 9, 9, 3]

unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(f"Unique numbers: {unique_numbers}")
