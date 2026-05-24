"""Check subset and superset."""

numbers = {1, 2, 3, 4, 5, 6, 7}
even_numbers = {2, 4, 6, 8}

# Check subset
is_subset = True

for number in even_numbers:
    if number not in numbers:
        is_subset = False
        break

print(f"Is subset ? {is_subset}")

# Check superset
is_superset = True

for number in even_numbers:
    if number not in numbers:
        is_superset = False
        break

print(f"Is superset? {is_superset}")
