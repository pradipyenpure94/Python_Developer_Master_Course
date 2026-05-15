"""Even numbers from list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
