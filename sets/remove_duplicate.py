"""Remove duplicates from list."""

numbers = [1, 2, 2, 3, 4, 4, 5]

seen = set()
unique_numbers = [number for number in numbers
                  if not (number in seen or seen.add(number))]
print(f"Unique numbers: {unique_numbers}")
