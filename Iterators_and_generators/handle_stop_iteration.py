"""Handle StopIteration."""

numbers = [10, 20, 30]

iterators = iter(numbers)

while True:
    try:
        print(next(iterators))
    except StopIteration:
        print("Error: StopIteration")
        break
