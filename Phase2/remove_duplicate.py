"""Remove duplicates element from list."""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

seen = set()
unique_numbers = list(filter(
    lambda number: number not in seen and not seen.add(number), numbers))

print(f"Unique numbers: {unique_numbers}")
