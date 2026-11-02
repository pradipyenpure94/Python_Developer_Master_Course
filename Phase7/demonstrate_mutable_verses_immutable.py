"""Demonstrate mutable versus immutable objects using lists and integers."""

# Integer is immutable
number = 10
print(id(number))
number += 1
print(id(number))

# List is mutable
even_numbers = [2, 4, 6, 8, 10]
print(id(even_numbers))
even_numbers.append(12)
print(id(even_numbers))
