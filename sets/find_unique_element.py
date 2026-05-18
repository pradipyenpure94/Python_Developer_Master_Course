"""Find unique elements."""

set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 6, 7}

unique_elements = {number for number in set1.union(set2)
                   if (number in set1) != (number in set2)}
print(f"Unique elements: {unique_elements}")
