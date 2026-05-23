"""Remove duplicate from tuple."""

numbers = (1, 2, 3, 1, 5, 6, 2, 4, 5, 6, 7, 8, 9, 5)

unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

result = tuple(unique_numbers)
print(f"Unique numbers: {result}")
