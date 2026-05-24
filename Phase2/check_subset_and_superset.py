"""Check subset and superset."""

numbers = {1, 2, 3, 4, 5, 6}
even_numbers = {2, 4, 6}

# Check subset
result = True

for number in even_numbers:
    if number not in numbers:
        result = False
        break

print(f"Is subset ? {result}")

# Check superset
result = True

for number in even_numbers:
    if number not in numbers:
        result = False
        break

print(f"Is superset? {result}")
