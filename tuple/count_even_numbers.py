"""Count even numbers in tuple."""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

count = sum(1 for number in t if number % 2 == 0)
print(f"Count even numbers: {count}")
