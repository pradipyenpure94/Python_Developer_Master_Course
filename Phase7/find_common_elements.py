"""Find common elements between two lists."""

prime_numbers = [2, 3, 5, 7, 11, 13]
even_numbers = [2, 4, 6, 8, 10]

result = list(number for number in prime_numbers if number in even_numbers)
print(result)
