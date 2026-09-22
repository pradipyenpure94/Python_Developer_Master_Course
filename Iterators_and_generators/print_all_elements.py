"""Print all elements using while + next()."""


even_numbers = [2, 4, 6, 8, 10]

iterator = iter(even_numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Iterator is exhausted.")
        break
