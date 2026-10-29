"""Separate even and odd numbers into two lists."""

numbers = tuple(range(1, 11))

even_numbers = list(number for number in numbers if number % 2 == 0)
odd_numbers = list(number for number in numbers if number % 2 == 1)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
