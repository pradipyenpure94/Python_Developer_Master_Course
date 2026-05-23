"""Remove duplicate from tuple."""

numbers = (1, 2, 3, 1, 5, 6, 2, 4, 5, 6, 7, 8, 9, 5)

seen = set()
unique_numbers = tuple(number for number in numbers if not (
    number in seen or seen.add(number)))
print(f"Unique numbers: {unique_numbers}")
