"""Find unique elements."""

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 6, 7}

unique_elements = set1 ^ set2
print(f"Unique elements: {unique_elements}")
