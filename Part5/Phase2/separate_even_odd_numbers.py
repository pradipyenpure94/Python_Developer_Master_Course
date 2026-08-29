"""Separate even and odd numbers."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]
print(f"Even numbers : {even_numbers}")
print(f"Odd numbers  : {odd_numbers}")
