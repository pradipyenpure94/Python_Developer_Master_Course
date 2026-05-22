"""Find duplicate numbers without using set."""

numbers = [1, 2, 3, 4, 5, 6, 8, 5, 2, 1, 5, 9, 3, 5, 7]
duplicate_numbers = []
freq = {}

for number in numbers:
    freq[number] = freq.get(number, 0) + 1

for number, count in freq.items():
    if count > 1:
        duplicate_numbers.append(number)

print(f"Duplicate numbers: {duplicate_numbers}")
