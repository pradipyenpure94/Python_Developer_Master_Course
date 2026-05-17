"""Count even numbers in tuple."""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

count = 0
index = 0
tuple_length = len(t)

while index < tuple_length:
    if t[index] % 2 == 0:
        count += 1

    index += 1

print(f"Number of even elements: {count}")
