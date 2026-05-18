"""Find common elements."""

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common_elements = set()
list_set = list(set1)
index = 0

while index < len(list_set):
    current_number = list_set[index]
    if current_number in set2:
        common_elements.add(current_number)
    index += 1

print(f"Common elements: {common_elements}")
