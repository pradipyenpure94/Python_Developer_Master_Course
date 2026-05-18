"""Remove duplicates from list."""

numbers = [1, 2, 2, 3, 4, 4, 5]

seen = set()
unique_numbers = []
index = 0

while index < len(numbers):
    current_number = numbers[index]
    if current_number not in seen:
        unique_numbers.append(current_number)
        seen.add(current_number)
    index += 1

print(f"Unique numbers: {unique_numbers}")
