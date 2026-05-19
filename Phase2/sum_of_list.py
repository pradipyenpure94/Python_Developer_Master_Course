"""Sum of all elements in list."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
index = 0

while index < len(numbers):
    total += numbers[index]
    index += 1
print(f"Sum of List: {total}")
