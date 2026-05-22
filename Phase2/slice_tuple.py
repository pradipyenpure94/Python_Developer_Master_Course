"""Slice tuple."""

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
start = 0
end = len(numbers)
step = 2

even_numbers = tuple(numbers[start:end:step])
print(f"Even numbers (slice tuple): {even_numbers}")
