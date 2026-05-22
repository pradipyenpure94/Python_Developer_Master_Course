"""Find duplicate numbers without using set."""

numbers = [1, 2, 3, 4, 5, 6, 8, 5, 2, 1, 5, 9, 3, 5, 7]
freq = {}

duplicate_numbers = [number
                     for index, number in enumerate(numbers)
                     if numbers.count(number) > 1 and
                     number not in numbers[:index]]
print(f"Duplicate numbers: {duplicate_numbers}")
