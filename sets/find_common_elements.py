"""Find common elements."""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common_elements = set()

for number in set1:
    if number in set2:
        common_elements.add(number)

print(f"Common elements: {common_elements}")
