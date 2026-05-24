"""Check subset and superset."""

numbers = {1, 2, 3, 4, 5, 6}
even_numbers = {2, 4, 6}

# Check subset
result = even_numbers.issubset(numbers)
print(f"Is subset ? {result}")

# Check superset
result = numbers.issuperset(even_numbers)
print(f"Is superset? {result}")
