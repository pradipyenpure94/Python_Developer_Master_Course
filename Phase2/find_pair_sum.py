"""Find pairs with given sum."""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1]
target = 3

seen = set()
pairs = {
    tuple(sorted((number, target - number)))
    for number in numbers
    if (target - number) in seen or not seen.add(number)
}

print(f"Sum pairs: {pairs}")
