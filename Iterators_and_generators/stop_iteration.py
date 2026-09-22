"""Demonstrate StopIteration."""


prime_numbers = [2, 3, 5, 7, 11]

iterator = iter(prime_numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        print("Iterator is exhausted.")
        break
