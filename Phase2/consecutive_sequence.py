"""Find smallest consecutive sequence."""

numbers = [10, 5, 12, 3, 55, 4, 11, 13]

numbers_set = set(numbers)
min_sequence_length = float('inf')

for number in numbers_set:
    if number - 1 not in numbers_set:
        current_number = number
        current_length = 1

        while current_number + 1 in numbers_set:
            current_number += 1
            current_length += 1

        if current_length > 1:
            min_sequence_length = min(min_sequence_length, current_length)

if min_sequence_length != float('inf'):
    print(f"Consecutive sequence: {min_sequence_length}")
else:
    print("No consecutive sequence found.")
