"""Find symmetric difference between two sets."""

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {2, 4, 6, 8, 10, 11, 12, 13}

symmetric_difference = numbers ^ even_numbers
print(f"Symmetric difference: {symmetric_difference}")
