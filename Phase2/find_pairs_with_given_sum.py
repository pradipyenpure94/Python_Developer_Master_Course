"""Find pairs with given sum."""

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
target = 10

seen = set()
pairs = []

for number in numbers:
    difference = target - number
    if difference in seen:
        pairs.append((difference, number))
    seen.add(number)

print(f"Sum pairs: {pairs}")
