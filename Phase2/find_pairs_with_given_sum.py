"""Find pairs with given sum."""

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
target = 10

pairs = []
seen = set()
index = 0
numbers_list = list(numbers)

while index < len(numbers_list):
    number = numbers_list[index]
    difference = target - number

    if difference in seen:
        pairs.append((difference, number))

    seen.add(number)

    index += 1

print(f"Sum pairs: {pairs}")
