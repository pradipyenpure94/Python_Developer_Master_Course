"""Find largest consecutive sequence."""

numbers = [10, 5, 12, 3, 55, 4, 11, 13]

numbers_set = set(numbers)
max_sequence_length = 0

for number in numbers_set:
    if number - 1 not in numbers_set:
        current_number = number
        current_length = 1

        while current_number + 1 in numbers_set:
            current_number += 1
            current_length += 1

        max_sequence_length = max(max_sequence_length, current_length)

print(f"Consecutive sequence: {max_sequence_length}")
