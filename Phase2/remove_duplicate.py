"""Remove duplicates element from list."""

numbers = [10, 50, 40, 20, 30, 50, 80, 90, 70, 60, 40, 20]

unique_numbers = []
seen = set()
index = 0

while index < len(numbers):
    current_number = numbers[index]
    if current_number not in seen:
        seen.add(current_number)
        unique_numbers.append(current_number)
    index += 1

print(f"Unique numbers: {unique_numbers}")
