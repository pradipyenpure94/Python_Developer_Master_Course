"""count occurrences in tuple."""

my_tuple = (1, 9, 9, 3)
target = 9
count = sum(1 for number in my_tuple if number == target)

print(f"Count occurrences: {count}")
