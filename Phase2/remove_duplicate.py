"""Remove duplicates element from list."""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        seen.add(number)
        unique_numbers.append(number)

print(f"Unique numbers: {unique_numbers}")
