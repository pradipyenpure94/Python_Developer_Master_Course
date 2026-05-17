"""Remove duplicates from tuple."""

t = (1, 2, 3, 4, 5, 6, 1, 2, 3)
unique_tuple = ()

for number in t:
    if number not in unique_tuple:
        unique_tuple += (number,)
print(f"Unique tuple: {unique_tuple}")
