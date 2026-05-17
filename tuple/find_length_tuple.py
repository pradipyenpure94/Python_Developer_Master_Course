"""Find length of tuple."""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

tuple_length = sum(1 for _ in t)
print(f"Tuple length: {tuple_length}")
