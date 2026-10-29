"""Merge two sorted lists into one sorted list."""

even_numbers = [10, 2, 4, 6, 8]
odd_numbers = [11, 1, 3, 5, 7, 9]

sorted_even_numbers = sorted(even_numbers)
sorted_odd_numbers = sorted(odd_numbers)
print(f"Sorted Even numbers: {sorted_even_numbers}")
print(f"Sorted Odd numbers: {sorted_odd_numbers}")
numbers = sorted_odd_numbers + sorted_even_numbers
sorted_numbers = sorted(numbers)
print(f"Sorted numbers: {sorted_numbers}")
