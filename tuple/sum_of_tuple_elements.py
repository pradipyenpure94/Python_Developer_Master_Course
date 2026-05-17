"""Sum of tuple elements."""

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

total = 0
index = 0
length = len(t)

while index < length:
    total += t[index]

    index += 1

print(f"Sum of tuple elements: {total}")
