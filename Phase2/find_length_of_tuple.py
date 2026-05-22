"""Find the length of tuple."""

numbers = (2, 4, 6, 8, 10)

length_of_tuple = sum(1 for _ in numbers)
print(f"Length of tuple: {length_of_tuple}")
