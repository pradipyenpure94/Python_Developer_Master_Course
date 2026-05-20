"""Move all zeros to end."""

numbers = [1, 2, 0, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 1, 4, 5]

non_zeros_numbers = []
zeros_count = 0

for number in numbers:
    if number != 0:
        non_zeros_numbers.append(number)
    else:
        zeros_count += 1

move_zeros_to_end = non_zeros_numbers + [0] * zeros_count
print(f"Move all zeros to end: {move_zeros_to_end}")
