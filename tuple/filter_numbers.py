"""Filter numbers greater than 10."""

t = (105, 236, 45, 65, 12, 32, 2, 3, 74, 8, 9, 96, 5, 61, 420, 21, 3, 45, 6)
print(f"Numbers: {t}")
filtered_numbers = tuple(number for number in t if number > 10)
print(f"Numbers greater than 10: {filtered_numbers}")
