"""Remove duplicate from tuple."""

t = (1, 2, 3, 4, 5, 6, 1, 2, 3)
unique_tuple = tuple(set(t))
print(f"Unique tuple: {unique_tuple}")
