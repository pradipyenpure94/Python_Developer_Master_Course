"""Count even numbers in tuple."""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

count = 0

for number in t:
    if number % 2 == 0:
        count += 1

print(f"Number of even elements: {count}")
