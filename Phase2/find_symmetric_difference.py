"""Find symmetric difference between two sets."""

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {2, 4, 6, 8, 10, 11, 12, 13}

left_diff = numbers.difference(even_numbers)
right_diff = even_numbers.difference(numbers)

symmetric_difference = left_diff.union(right_diff)

print(f"Symmetric difference: {symmetric_difference}")
