"""Remove duplicates element from list."""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

seen = set()
unique_numbers = [number for number in numbers
                  if not (number in seen or seen.add(number))]
print(f"Unique numbers: {unique_numbers}")
