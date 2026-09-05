"""Use filter() to find positive numbers."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, 0]

filter_positive_numbers = list(filter(lambda x: x > 0, numbers))
print(f"Filtered positive numbers: {filter_positive_numbers}")
